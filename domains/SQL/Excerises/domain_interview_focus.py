"""Subtopic-specific analysis populations for domain interview exercises.

The public contract describes the transformation without naming an algorithm.
Private SQL exposes a common internal row shape for independently tested tasks.
"""
QUERY_TOPICS={'DQL','OPERATORS','AGGREGATES','SET_OPERATIONS','JOINS',
              'STRING_FUNCTIONS','DATE_FUNCTIONS','ANALYTICAL_FUNCTIONS','CTE'}


def profile(model,topic,subtopic):
    mp=model['map']; schema=model['slug']; fact,master,pname=model['base']
    table=f'[{schema}].[{fact}]'; parent=f'[{schema}].[{master}]'
    pk,fk,amt,day,cat,status,label,tm,par=[mp[k] for k in
        ('RecordID','PartyID','Amount','EventDate','Category','Status','Label','EventTime','ParentID')]
    value=f'f.[{amt}]'; activity=f'f.[{day}]'; segment=f'f.[{cat}]'
    where='1=1'; extra=''; before=[]; note='Use every source row, with its stored value and calendar date.'
    if topic=='DQL':
        if subtopic=='Select':
            value=f'f.[{amt}]*CAST(f.[{mp["Quantity"]}] AS decimal(19,4))'
            note=f'The analysis value is `{amt}` multiplied by `{mp["Quantity"]}`; unknown values stay unknown.'
        elif subtopic=='Where':
            where=f"f.[{status}] IN ('Open','Pending') AND f.[{day}] >= '20240101' AND f.[{day}] < '20250101'"
            note=f'Only Open/Pending `{status}` rows in 2024 qualify.'
        elif subtopic in {'Group By','Having'}:
            agg=f'SELECT [{fk}] AS OwnerID, [{day}] AS ActivityDate, MIN([{pk}]) AS EventID, SUM([{amt}]) AS MetricValue, COUNT(*) AS SourceCount FROM {table} GROUP BY [{fk}],[{day}]'
            if subtopic=='Having': agg+=f' HAVING COUNT(*)>=2 OR SUM([{amt}])>=200'
            before=[('Daily',agg)]
            return dict(ctes=before+[('E','SELECT EventID,OwnerID,ActivityDate,CAST(MetricValue AS decimal(28,4)) AS MetricValue,CAST(\'DAILY\' AS nvarchar(100)) AS Segment,CAST(NULL AS int) AS ParentID FROM Daily')],
                        rule=f'Combine source rows at `{fk}`/`{day}` grain. Use the smallest contributing `{pk}` as the analysis row ID and the sum of known `{amt}` as analysis value; an all-unknown group stays unknown.'+(' Retain groups having at least two rows or known sum at least 200.' if subtopic=='Having' else ''),table=table,parent=parent)
        elif subtopic=='Order By':
            where=f'f.[{amt}] IS NOT NULL'
            note=f'Within each `{fk}`, retain the first three rows by `{amt}` descending, then `{pk}` ascending. Unknown values do not qualify.'
            before=[('Chosen',f'SELECT [{pk}],ROW_NUMBER() OVER(PARTITION BY [{fk}] ORDER BY [{amt}] DESC,[{pk}]) AS rn FROM {table} WHERE [{amt}] IS NOT NULL')]
            extra=f' JOIN Chosen c ON c.[{pk}]=f.[{pk}] AND c.rn<=3'
        else:
            note=f'Within each `{fk}`, retain all rows in its top two distinct known `{amt}` value positions; include all ties and exclude unknown values.'
            before=[('Chosen',f'SELECT [{pk}],DENSE_RANK() OVER(PARTITION BY [{fk}] ORDER BY [{amt}] DESC) AS rn FROM {table} WHERE [{amt}] IS NOT NULL')]
            extra=f' JOIN Chosen c ON c.[{pk}]=f.[{pk}] AND c.rn<=2'
    elif topic=='OPERATORS':
        ops={'Equality Operator (=)':'=','Inequality Operator (<>)':'<>','Greater Than (>)':'>',
             'Greater Than or Equal To (>=)':'>=','Less Than (<)':'<','Less Than or Equal To (<=)':'<='}
        if subtopic in ops:
            where=f'f.[{amt}] {ops[subtopic]} 200';note=f'Eligible rows satisfy `{amt} {ops[subtopic]} 200`; unknown values do not pass.'
        elif subtopic=='IN Operator':
            where=f"f.[{fk}] IN (SELECT [{fk}] FROM {parent} WHERE Region IN ('North','South'))";note=f'Only rows belonging to North- or South-region `{master}` IDs qualify;retain every category code for those owners.'
        elif subtopic=='NOT IN Operator':
            where=f'f.[{pk}] NOT IN (SELECT [{par}] FROM {table} WHERE [{par}] IS NOT NULL)'
            note=f'Retain rows whose `{pk}` is not referenced by any non-null `{par}`. A null parent in another row must not eliminate every candidate.'
        elif subtopic in {'LIKE Operator','NOT LIKE Operator'}:
            op='NOT LIKE' if subtopic.startswith('NOT') else 'LIKE'
            where=f"f.[{label}] {op} N'%-%'";note=f'Eligible rows have `{label}` {op.lower()} the pattern `%-%`,under the training database collation.'
        elif subtopic=='BETWEEN Operator':
            where=f'f.[{amt}] BETWEEN 100 AND 200';note=f'Eligible `{amt}` values lie in the inclusive interval [100,200]; unknown values do not pass.'
        else:
            op='NOT EXISTS' if subtopic.startswith('NOT') else 'EXISTS'
            where=f"{op} (SELECT 1 FROM {parent} p WHERE p.[{fk}]=f.[{fk}] AND p.Region='North')"
            note=f'Retain a source row only when a matching North-region `{master}` row {"does not exist" if op.startswith("NOT") else "exists"}.'
    elif topic=='AGGREGATES':
        fn=subtopic.upper(); exp='COUNT(*)' if fn=='COUNT' else f'{fn}(CAST([{amt}] AS decimal(28,4)))'
        before=[('Daily',f'SELECT MIN([{pk}]) AS EventID,[{fk}] AS OwnerID,[{day}] AS ActivityDate,{exp} AS MetricValue FROM {table} GROUP BY [{fk}],[{day}]')]
        return dict(ctes=before+[('E',"SELECT EventID,OwnerID,ActivityDate,CAST(MetricValue AS decimal(28,4)) AS MetricValue,CAST('DAILY' AS nvarchar(100)) AS Segment,CAST(NULL AS int) AS ParentID FROM Daily")],
                    rule=f'First form one analysis row per `{fk}`/`{day}`. Its ID is the smallest contributing `{pk}`,and its value is '+('the number of source rows,including rows with unknown values.' if fn=='COUNT' else f'the {subtopic.lower()} of known `{amt}`; an all-unknown group stays unknown.'),table=table,parent=parent)
    elif topic=='SET_OPERATIONS':
        op={'Union':'UNION','Union All':'UNION ALL','Intersect':'INTERSECT','Except':'EXCEPT'}[subtopic]
        # UNION ALL has two intentionally disjoint source populations. Other
        # tasks test multiset multiplicity directly in the foundation set.
        left=f'[{amt}] IS NOT NULL' if op=='UNION ALL' else f"[{fk}] IN (SELECT [{fk}] FROM {parent} WHERE Region='North')"
        right=f"[{status}]='Open'" if op!='UNION ALL' else f"[{amt}] IS NULL"
        before=[('Eligible',f"SELECT [{pk}] FROM {table} WHERE {left} {op} SELECT [{pk}] FROM {table} WHERE {right}")]
        extra=f' JOIN Eligible x ON x.[{pk}]=f.[{pk}]'
        note=f'Construct the eligible ID set using {op}: '+(f'the left population has known `{amt}` and the right has unknown `{amt}`.' if op=='UNION ALL' else f'the left population belongs to a North-region `{master}` owner and the right has `{status}=Open`.')+' For UNION ALL these populations are disjoint,so each source ID appears once;the separately supplied foundation tasks test duplicate preservation.'
    elif topic=='JOINS':
        if subtopic=='Cross Join':
            before=[('Required',"SELECT 'A' AS Segment UNION ALL SELECT 'B' UNION ALL SELECT 'C'")]
            extra=f' CROSS JOIN Required r';where=f'r.Segment=f.[{cat}]'
            note=f'Build the three-code grid A/B/C and retain only source rows matching their `{cat}` code. Keep zero-activity owners when the report asks for them.'
        else:
            jt={'Inner Join':'INNER','Left Join':'LEFT','Right Join':'RIGHT','Full Join':'FULL OUTER'}[subtopic]
            if jt=='RIGHT':
                extra=f' RIGHT JOIN {parent} p ON p.[{fk}]=f.[{fk}]';where=f'f.[{pk}] IS NOT NULL'
            else:
                extra=f' {jt} JOIN {parent} p ON p.[{fk}]=f.[{fk}]';where=f'f.[{pk}] IS NOT NULL'
            note=f'Relate `{fact}` and `{master}` on `{fk}` with {jt.lower()} preservation semantics. Only real source records count as activity; a preserved owner with no source rows must not become a phantom activity row. Reports requiring all owners must still include that owner.'
    elif topic=='STRING_FUNCTIONS':
        exprs={
            'Length Function (LEN)':(f'LEN(f.[{label}])',f'The analysis value is the character length of `{label}`,excluding trailing ASCII spaces.'),
            'Substring Function (SUBSTRING)':(f'SUBSTRING(f.[{label}],2,4)',f'Use characters 2 through 5 of `{label}` as a text token,using one-based positions.'),
            'Concatenation Operator (+)':(f"f.[{label}]+N':'+f.[{status}]",f'Use `{label}`,a colon and `{status}` as one text token,retaining stored spaces.'),
            'Lower Function (LOWER)':(f'LOWER(f.[{label}])',f'Convert `{label}` to lowercase as a text token.'),
            'Upper Function (UPPER)':(f'UPPER(f.[{label}])',f'Convert `{label}` to uppercase as a text token.'),
            'Trim Function (TRIM)':(f'TRIM(f.[{label}])',f'Remove leading and trailing ASCII spaces from `{label}` to form a text token.'),
            'Ltrim Function (LTRIM)':(f'LTRIM(f.[{label}])',f'Remove only leading ASCII spaces from `{label}` to form a text token.'),
            'Rtrim Function (RTRIM)':(f'RTRIM(f.[{label}])',f'Remove only trailing ASCII spaces from `{label}` to form a text token.'),
            'Charindex Function (CHARINDEX)':(f"CHARINDEX(N'-',f.[{label}])",f'The analysis value is the one-based first hyphen position in `{label}`,or zero when absent.'),
            'Left Function (LEFT)':(f'LEFT(f.[{label}],3)',f'The text token is the first three characters of `{label}`.'),
            'Right Function (RIGHT)':(f'RIGHT(f.[{label}],3)',f'The text token is the last three characters of `{label}`,including trailing spaces.'),
            'Reverse Function (REVERSE)':(f'REVERSE(f.[{label}])',f'The text token is the characters of `{label}` in reverse order.'),
            'Replace Function (REPLACE)':(f"REPLACE(f.[{label}],N'-',N'')",f'Remove every hyphen from `{label}` to form a text token.'),
            'Case Statement (CASE)':(f"CASE f.[{status}] WHEN 'Open' THEN 1 WHEN 'Pending' THEN 2 ELSE 3 END",f'The analysis value is the business priority of `{status}`: Open=1,Pending=2,Closed=3.'),
            'ISNULL Function (ISNULL)':(f"ISNULL(f.[{mp['Note']}],N'missing')",f'The text token is `{mp["Note"]}` with null replaced by `missing`; empty text stays empty.'),
            'Coalesce Function (COALESCE)':(f"COALESCE(f.[{mp['Note']}],f.[{mp['BackupNote']}],N'missing')",f'The text token is the first non-null of `{mp["Note"]}`,`{mp["BackupNote"]}`,then `missing`; empty text is a value.'),
        }
        expr,note=exprs[subtopic]
        if subtopic in {'Length Function (LEN)','Charindex Function (CHARINDEX)','Case Statement (CASE)'}:
            value=expr
        else:
            # DATALENGTH distinguishes left/right trim and case-sensitive
            # token bytes remain in Segment for group-sensitive questions.
            segment=expr;value=f'DATALENGTH({expr})/2.0'
            note+=' The token is the analysis segment,and its UTF-16 byte length divided by two is the analysis value;null token means unknown value. These fixtures use BMP text.'
    elif topic=='DATE_FUNCTIONS':
        if subtopic=='Current Date and time (GETDATE)':
            value=f"DATEDIFF(day,f.[{day}],CAST('20250101' AS date))"
            note=f'Use the fixed as-of date 2025-01-01,not the machine clock. The analysis value is the calendar-day age of `{day}` at that date. Demonstrate in a separate native check that your clock-injected implementation can accept a current-date value.'
        elif subtopic=='Date Part Function (DATEPART)':
            value=f'DATEPART(month,f.[{day}])';note=f'The analysis value is the calendar month number of `{day}`.'
        elif subtopic=='Date Difference Function (DATEDIFF)':
            value=f'DATEDIFF(day,(SELECT MIN(x.[{day}]) FROM {table} x WHERE x.[{fk}]=f.[{fk}]),f.[{day}])';note=f'The analysis value is the calendar-day difference from that owner\'s earliest stored `{day}` to the current `{day}`. Count midnight boundaries,not elapsed timestamp hours.'
        elif subtopic=='Date Addition/Subtraction':
            activity=f'DATEADD(day,7,f.[{day}])';note=f'Shift each activity date seven calendar days after `{day}`;keep the stored monetary value.'
        elif subtopic=='Weekday Function (DATEPART)':
            value=f"((DATEDIFF(day,'19000101',f.[{day}])%7+7)%7)+1";note=f'The analysis value is the ISO weekday of `{day}`:Monday1 through Sunday7,independent of connection DATEFIRST.'
        elif subtopic in {'Date Formatting (FORMAT)','Date to String (Various formats)','DateTime to String (Various formats)'}:
            expr=(f"FORMAT(f.[{day}],'yyyy-MM','en-US')" if subtopic.startswith('Date Formatting') else f'CONVERT(nvarchar(30),f.[{tm if subtopic.startswith("DateTime") else day}],126)')
            segment=expr;note=f'Keep the original analysis date/value and use '+('yyyy-MM with explicit en-US culture' if subtopic.startswith('Date Formatting') else ('ISO timestamp text with style126' if subtopic.startswith('DateTime') else 'ISO date text with style126'))+' as the analysis segment.'
        elif subtopic in {'String to Date (Various formats)','String to DateTime (Various formats)'}:
            activity=f"CONVERT(date,CONVERT(nvarchar(10),f.[{day}],23),23)";note=f'Round-trip `{day}` through unambiguous yyyy-mm-dd text and recover the same date. Ambiguous locale-dependent strings must not be introduced.'
        elif subtopic in {'Timezones','Cast a DateTime Timezone to another TimeZone'}:
            activity="CAST(f.RecordedAt AT TIME ZONE 'Eastern Standard Time' AS date)";note='The analysis date is the America/New_York local calendar date of the stored RecordedAt instant;use SQL Server Windows zone Eastern Standard Time,which includes daylight-saving rules.'
        elif subtopic=='UTC':
            activity="CAST(SWITCHOFFSET(f.RecordedAt,'+00:00') AS date)";note='The analysis date is the UTC calendar date of RecordedAt,converting the instant rather than replacing its offset.'
        elif subtopic=='Offsets':
            value='DATEPART(tzoffset,f.RecordedAt)';note='The analysis value is the stored RecordedAt UTC offset in signed minutes;keep its stored calendar activity date.'
        elif subtopic=='Applying an Offset to a Date Datatype Column':
            activity=f"CAST(SWITCHOFFSET(TODATETIMEOFFSET(CAST(f.[{day}] AS datetime2),'+00:00'),'+05:30') AS date)";note=f'Treat `{day}` midnight as UTC,then convert that instant to fixed +05:30;use the resulting local date.'
        elif subtopic.startswith('Cast a DateTime to DateTime'):
            activity=f"CAST((f.[{tm}] AT TIME ZONE 'UTC') AT TIME ZONE 'India Standard Time' AS date)";note=f'Treat the naive `{tm}` value as UTC,then convert the instant to India Standard Time and use its local date.'
        else:
            activity=f'CAST(f.[{tm}] AS date)';note=f'The analysis date is the calendar-date portion of `{tm}` without adding or converting a timezone.'
    elif topic=='ANALYTICAL_FUNCTIONS':
        if subtopic=='Aggregate Functions':expr=f'SUM(CAST([{amt}] AS decimal(28,4))) OVER(PARTITION BY [{fk}] ORDER BY [{day}],[{pk}] ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)';note='Use the per-owner running sum of known values through this source row as the analysis value;an entirely unknown prefix remains unknown.'
        elif subtopic in {'ROW_NUMBER()','RANK()','DENSE_RANK()','NTILE(n)'}:
            fn='NTILE(4)' if subtopic=='NTILE(n)' else subtopic
            order=f'[{amt}] DESC'+(f',[{pk}]' if subtopic in {'ROW_NUMBER()','NTILE(n)'} else '')
            expr=f'{fn} OVER(PARTITION BY [{fk}] ORDER BY {order})';note=f'Use '+({'ROW_NUMBER()':f'the per-owner descending-value position,breaking ties by `{pk}` ascending','RANK()':'the per-owner competition rank of descending values with gaps after ties','DENSE_RANK()':'the per-owner distinct descending-value rank without gaps','NTILE(n)':f'the per-owner quartile number using descending value then `{pk}` ascending'}[subtopic])+'. Unknown values sort last. Keep all source rows.'
        else:
            fn=subtopic[:-2];offset=',1' if fn in {'LAG','LEAD'} else ''
            frame=' ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING' if fn=='LAST_VALUE' else ''
            expr=f'{fn}([{amt}]{offset}) OVER(PARTITION BY [{fk}] ORDER BY [{day}],[{pk}]{frame})'
            note='The analysis value is '+{'LAG':'the immediately preceding source row value','LEAD':'the immediately following source row value','FIRST_VALUE':'the first source row value','LAST_VALUE':'the last source row value in the complete owner partition'}[fn]+f' for that `{fk}`,ordered by `{day}` then `{pk}`. Keep unknown values;do not skip them.'
        before=[('Windowed',f'SELECT *,{expr} AS AnalysisValue FROM {table}')]
        table_source='Windowed';value='f.AnalysisValue'
        query=f'SELECT f.[{pk}] AS EventID,f.[{fk}] AS OwnerID,CAST({activity} AS date) AS ActivityDate,CAST({value} AS decimal(28,4)) AS MetricValue,CAST({segment} AS nvarchar(100)) AS Segment,f.[{par}] AS ParentID FROM {table_source} f'
        return dict(ctes=before+[('E',query)],rule=note,table=table,parent=parent)
    elif topic=='CTE':
        if subtopic=='Recursive CTEs':
            before=[('Paths',f"SELECT [{pk}] AS StartID,[{pk}] AS CurrentID,[{par}] AS NextID,CAST('/'+CAST([{pk}] AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM {table} UNION ALL SELECT p.StartID,f.[{pk}],f.[{par}],CAST(p.VisitPath+CAST(f.[{pk}] AS varchar(12))+'/' AS varchar(max)),p.Depth+1 FROM Paths p JOIN {table} f ON f.[{pk}]=p.NextID WHERE p.Depth<100 AND CHARINDEX('/'+CAST(f.[{pk}] AS varchar(12))+'/',p.VisitPath)=0"),('Depths','SELECT StartID,MAX(Depth) AS Depth FROM Paths GROUP BY StartID')]
            extra=f' JOIN Depths d ON d.StartID=f.[{pk}]';value='d.Depth';note=f'The analysis value is the number of distinct parent edges reachable from `{pk}`,stopping before revisiting an ID. Maximum supported chain length is100;diagnose deeper inputs separately. A root has value0. Keep stored dates and category codes.'
        elif subtopic=='Using Multiple CTEs':
            before=[('OwnerTotals',f'SELECT [{fk}],SUM([{amt}]) AS Total FROM {table} GROUP BY [{fk}]'),('EligibleOwners',f'SELECT [{fk}] FROM OwnerTotals WHERE Total>=300')]
            extra=f' JOIN EligibleOwners a ON a.[{fk}]=f.[{fk}]';note=f'Only owners whose total known `{amt}` is at least300 qualify;keep each of their original rows.'
        elif subtopic=='Common Use Cases for CTEs':
            where=f'f.[{par}] IS NULL';note=f'Only root rows with null `{par}` qualify;retain unknown monetary values.'
        elif subtopic=='Benefits of Using CTEs':
            where=f'f.[{amt}] IS NOT NULL';note=f'Only known `{amt}` rows qualify. The submitted statement must define the eligible population once and reuse it consistently across report stages.'
        else:
            note=f'Use all `{fact}` rows as one explicitly defined analysis population. Do not repeat inconsistent filters in different report stages.'
    query=f'SELECT f.[{pk}] AS EventID,f.[{fk}] AS OwnerID,CAST({activity} AS date) AS ActivityDate,CAST({value} AS decimal(28,4)) AS MetricValue,CAST({segment} AS nvarchar(100)) AS Segment,f.[{par}] AS ParentID FROM {table} f{extra} WHERE {where}'
    return dict(ctes=before+[('E',query)],rule=note,table=table,parent=parent)
