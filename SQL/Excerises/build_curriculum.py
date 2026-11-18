"""Generate the student and instructor SQL Server exercise books. Python stdlib only."""
from pathlib import Path
import json
import re
from collections import Counter
import domain_projects as projects

ROOT = Path(__file__).resolve().parent
DOMAINS = [
    ('Retail', 'retail', 'Orders', 'Customers', 'order value', 'customer'),
    ('Banking / Finance', 'banking', 'Transactions', 'Accounts', 'transaction amount', 'account'),
    ('Pharma', 'pharma', 'Batches', 'Suppliers', 'batch cost', 'supplier'),
    ('Healthcare', 'healthcare', 'Encounters', 'Patients', 'encounter charge', 'patient'),
    ('Oil', 'oil', 'Shipments', 'Sites', 'shipment value', 'site'),
    ('Retail Supply Chain', 'retail_supply_chain', 'StockMovements', 'Warehouses', 'movement value', 'warehouse'),
    ('Retail Logistics', 'retail_logistics', 'Shipments', 'Customers', 'freight charge', 'customer'),
    ('E-commerce', 'ecommerce', 'Orders', 'Customers', 'order value', 'customer'),
    ('Brokerage', 'brokerage', 'TradeOrders', 'BrokerageAccounts', 'estimated order value', 'account'),
]
BOOKS = {}
RECORDS = []

def add(topic, subtopic, domain, variant, prompt, sql='', check='', answer=''):
    subs = BOOKS.setdefault(topic, {})
    rows = subs.setdefault(subtopic, [])
    sid = list(subs).index(subtopic)+1
    domain_index=next(i for i,d in enumerate(DOMAINS) if d[0]==domain[0])
    # Keep the original five-domain assignment IDs stable; append new-domain IDs.
    number=variant*5+domain_index+1 if domain_index<5 else 26+variant*4+(domain_index-5)
    eid = f'{topic.upper()}-{sid:02d}-{number:02d}'
    row = dict(id=eid, topic=topic, subtopic=subtopic, domain=domain[0],
               prompt=prompt, sql=sql.strip(), check=check, answer=answer)
    rows.append(row)
    RECORDS.append(row)

def table(d):
    return f'[{d[1]}].[{d[2]}]'

def party(d):
    return f'[{d[1]}].[{d[3]}]'

def exercise(topic, subtopic, maker):
    # Five task patterns for each connected domain project.
    for v in range(5):
        for d in DOMAINS:
            result = maker(d, v)
            add(topic, subtopic, d, v, *result)

def query(d, prompt, projection, tail='', check='Compare the complete result with the reference query, including NULLs and duplicate rows.'):
    return (f'{d[0]}: {prompt} Use `{table(d)}`.',
            f'SELECT {projection}\nFROM {table(d)}{tail};', check)

def scratch(body, seed=''):
    return 'DROP TABLE IF EXISTS #Work;\n' + seed + body + '\nDROP TABLE IF EXISTS #Work;'


def core_queries():
    specs = {
        'Select': [
            ('List record IDs, labels and amounts, ordered by record ID.', 'RecordID, Label, Amount', '\nORDER BY RecordID'),
            ('Return each distinct category once, sorted by category.', 'DISTINCT Category', '\nORDER BY Category'),
            ('Show record ID and Amount multiplied by Quantity as ExtendedAmount; preserve unknown amounts.', 'RecordID, Amount * Quantity AS ExtendedAmount', '\nORDER BY RecordID'),
            ('Show record ID, category as BusinessGroup and status as WorkflowState.', 'RecordID, Category AS BusinessGroup, Status AS WorkflowState', '\nORDER BY RecordID'),
            ('Return distinct category/status combinations, ordered by both columns.', 'DISTINCT Category, Status', '\nORDER BY Category, Status')],
        'Where': [
            ("Find Open records; return ID and status.", 'RecordID, Status', "\nWHERE Status = 'Open' ORDER BY RecordID"),
            ('Find known amounts of at least 150 in category B; return ID and amount.', 'RecordID, Amount', "\nWHERE Amount >= 150 AND Category = 'B' ORDER BY RecordID"),
            ('Find unknown amounts; return ID and amount.', 'RecordID, Amount', '\nWHERE Amount IS NULL ORDER BY RecordID'),
            ('Find events in January 2024 using an inclusive start and exclusive end; return IDs and dates.', 'RecordID, EventDate', "\nWHERE EventDate >= '20240101' AND EventDate < '20240201' ORDER BY RecordID"),
            ('Find records that are Open or Pending, with a positive amount; return ID, status and amount.', 'RecordID, Status, Amount', "\nWHERE (Status = 'Open' OR Status = 'Pending') AND Amount > 0 ORDER BY RecordID")],
        'Group By': [
            ('Count records per category.', 'Category, COUNT(*) AS RecordCount', '\nGROUP BY Category ORDER BY Category'),
            ('Total known amounts per status.', 'Status, SUM(Amount) AS TotalAmount', '\nGROUP BY Status ORDER BY Status'),
            ('Return average known amount for each category/status pair.', 'Category, Status, AVG(Amount) AS AverageAmount', '\nGROUP BY Category, Status ORDER BY Category, Status'),
            ('Count events by calendar year and month.', 'YEAR(EventDate) AS EventYear, MONTH(EventDate) AS EventMonth, COUNT(*) AS RecordCount', '\nGROUP BY YEAR(EventDate), MONTH(EventDate) ORDER BY EventYear, EventMonth'),
            ('Return each party ID (including the NULL group), record count and total quantity.', 'PartyID, COUNT(*) AS RecordCount, SUM(Quantity) AS TotalQuantity', '\nGROUP BY PartyID ORDER BY PartyID')],
        'Having': [
            ('Find categories with more than three records; show count.', 'Category, COUNT(*) AS RecordCount', '\nGROUP BY Category HAVING COUNT(*) > 3 ORDER BY Category'),
            ('Find statuses with total known amounts above 500; show total.', 'Status, SUM(Amount) AS TotalAmount', '\nGROUP BY Status HAVING SUM(Amount) > 500 ORDER BY Status'),
            ('Among positive amounts, find categories averaging at least 150; show average.', 'Category, AVG(Amount) AS AverageAmount', '\nWHERE Amount > 0 GROUP BY Category HAVING AVG(Amount) >= 150 ORDER BY Category'),
            ('Find party IDs with at least two records; exclude NULL party IDs; show count.', 'PartyID, COUNT(*) AS RecordCount', '\nWHERE PartyID IS NOT NULL GROUP BY PartyID HAVING COUNT(*) >= 2 ORDER BY PartyID'),
            ('Find categories containing an unknown amount; show total and known-amount counts.', 'Category, COUNT(*) AS TotalCount, COUNT(Amount) AS KnownCount', '\nGROUP BY Category HAVING COUNT(*) > COUNT(Amount) ORDER BY Category')],
        'Order By': [
            ('List IDs and amounts from lowest to highest amount, NULL first, then ID.', 'RecordID, Amount', '\nORDER BY Amount, RecordID'),
            ('List IDs and amounts from highest to lowest amount, then ID ascending.', 'RecordID, Amount', '\nORDER BY Amount DESC, RecordID'),
            ('List IDs, categories and dates, grouped by category then newest date first and ID ascending.', 'RecordID, Category, EventDate', '\nORDER BY Category, EventDate DESC, RecordID'),
            ('List IDs and amounts ascending but place unknown amounts last.', 'RecordID, Amount', '\nORDER BY CASE WHEN Amount IS NULL THEN 1 ELSE 0 END, Amount, RecordID'),
            ('List IDs and status in business priority Open, Pending, Closed, then ID.', 'RecordID, Status', "\nORDER BY CASE Status WHEN 'Open' THEN 1 WHEN 'Pending' THEN 2 ELSE 3 END, RecordID")],
        'Top': [
            ('Return exactly the three highest-valued records, breaking ties by ID ascending.', 'TOP (3) RecordID, Amount', '\nORDER BY Amount DESC, RecordID'),
            ('Return the two earliest events, breaking ties by ID.', 'TOP (2) RecordID, EventDate', '\nORDER BY EventDate, RecordID'),
            ('Return the top three amount positions and all amount ties at the cutoff. Order by amount descending only.', 'TOP (3) WITH TIES RecordID, Amount', '\nORDER BY Amount DESC'),
            ('Return the highest-valued Open record, breaking ties by ID.', 'TOP (1) RecordID, Amount', "\nWHERE Status = 'Open' ORDER BY Amount DESC, RecordID"),
            ('Return the top 25 percent of records by latest date, then ID ascending.', 'TOP (25) PERCENT RecordID, EventDate', '\nORDER BY EventDate DESC, RecordID')]
    }
    for sub, variants in specs.items():
        exercise('DQL', sub, lambda d,v, variants=variants: query(d,*variants[v]))

    operators = [('Equality Operator (=)', '='), ('Inequality Operator (<>)', '<>'), ('Greater Than (>)','>'), ('Greater Than or Equal To (>=)','>='), ('Less Than (<)','<'), ('Less Than or Equal To (<=)','<=')]
    for sub, op in operators:
        def make(d,v,op=op):
            clauses = [f'Amount {op} 200', f'Quantity {op} 2', f"EventDate {op} CONVERT(date,'20240201',112)", f"Amount {op} 100 AND Category = 'A'", f'PartyID {op} 2']
            return query(d, f'Return RecordID, Amount, Quantity, EventDate and PartyID for rows satisfying `{clauses[v]}`. Explain whether NULL operands pass this predicate.', 'RecordID, Amount, Quantity, EventDate, PartyID', f'\nWHERE {clauses[v]} ORDER BY RecordID', 'NULL comparisons yield UNKNOWN, so those rows do not pass WHERE; compare IDs and values to the reference.')
        exercise('OPERATORS',sub,make)
    predicates = {
        'IN Operator': ["Category IN ('A','C')", "Status IN ('Open','Pending')", 'PartyID IN (1,3)', 'Amount IN (100,200,300)', f'PartyID IN (SELECT PartyID FROM {{p}} WHERE Region = \'North\')'],
        'NOT IN Operator': ["Category NOT IN ('A','C')", "Status NOT IN ('Closed')", 'PartyID NOT IN (1,3)', 'Amount NOT IN (100,200,300)', 'RecordID NOT IN (SELECT ParentID FROM {t} WHERE ParentID IS NOT NULL)'],
        'LIKE Operator': ["Label LIKE N'%Alpha%'", "Label LIKE N'%-%'", "Label LIKE N'____-%'", "Label LIKE N'%Three%'", "Label LIKE N'% '"],
        'NOT LIKE Operator': ["Label NOT LIKE N'%Alpha%'", "Label NOT LIKE N'%One%'", "Label NOT LIKE N'____-%'", "Label NOT LIKE N'%Three%'", "Label NOT LIKE N'% '"],
        'BETWEEN Operator': ['Amount BETWEEN 100 AND 200', 'Quantity BETWEEN 2 AND 3', "EventDate BETWEEN '20240101' AND '20240131'", "RecordID BETWEEN 3 AND 8 AND Status = 'Pending'", 'Amount NOT BETWEEN 100 AND 200'],
    }
    for sub, variants in predicates.items():
        def make(d,v,variants=variants):
            pred = variants[v].format(p=party(d),t=table(d))
            note = ' Explain NULL handling for NOT IN.' if 'NOT IN' in pred else ''
            return query(d,f'Return IDs and labels satisfying `{pred}`.{note}', 'RecordID, Label', f'\nWHERE {pred} ORDER BY RecordID', 'Compare record IDs; BETWEEN includes both endpoints. Unknown values do not pass predicates. Text matching follows the column\'s existing collation.')
        exercise('OPERATORS',sub,make)
    for exists in [True,False]:
        def make(d,v,exists=exists):
            conditions = ['f.PartyID = p.PartyID', "f.PartyID = p.PartyID AND f.Status = 'Open'", 'f.PartyID = p.PartyID AND f.Amount >= 200', "f.PartyID = p.PartyID AND f.EventDate >= '20240201'", 'f.PartyID = p.PartyID AND f.Amount IS NULL']
            op = 'EXISTS' if exists else 'NOT EXISTS'
            return (f'{d[0]}: Return party IDs and names from `{party(d)}` for which {op} a row in `{table(d)}` satisfying `{conditions[v]}` (aliases p and f).',f'SELECT p.PartyID, p.PartyName FROM {party(d)} p\nWHERE {op} (SELECT 1 FROM {table(d)} f WHERE {conditions[v]})\nORDER BY p.PartyID;', 'Each qualifying party appears once, regardless of the number of matching facts.')
        exercise('OPERATORS','EXISTS Operator' if exists else 'NOT EXISTS Operator',make)

def aggregates_and_sets():
    for fn in ['COUNT','SUM','AVG','MAX','MIN']:
        def make(d,v,fn=fn):
            col = '*' if fn == 'COUNT' else 'Amount'
            variants = [(f'Return {fn} over {col} for all records.', f'{fn}({col}) AS Result',''),
                        (f'Return {fn} over Amount for each category.', f'Category, {fn}(Amount) AS Result','\nGROUP BY Category ORDER BY Category'),
                        (f'Return {fn} over Quantity for Open records.', f'{fn}("Quantity") AS Result',"\nWHERE Status = 'Open'"),
                        (f'Return {fn} over DISTINCT Amount.', f'{fn}(DISTINCT Amount) AS Result',''),
                        (f'Return {fn} over Amount per party ID, excluding NULL party IDs.', f'PartyID, {fn}(Amount) AS Result','\nWHERE PartyID IS NOT NULL GROUP BY PartyID ORDER BY PartyID')]
            a,b,c=variants[v]
            return query(d,a,b.replace('"Quantity"','Quantity'),c,'COUNT(*) counts rows; other column aggregates ignore NULL. On the full fixture: COUNT(*)=12, COUNT(Amount)=11, SUM(Amount)=1700, MIN=0, MAX=300.')
        exercise('AGGREGATES',fn.title(),make)
    for op in ['UNION','UNION ALL','INTERSECT','EXCEPT']:
        def make(d,v,op=op):
            t=table(d)
            cols = ['PartyID','Category','Amount','RecordID','Category, Status']
            filters = [("Status = 'Open'","Status = 'Closed'"),('Amount >= 150','Quantity >= 3'),("EventDate < '20240301'","EventDate >= '20240201'"),('RecordID <= 8','RecordID >= 5'),('Amount >= 100','Quantity >= 2')]
            col=cols[v]; a,b=filters[v]
            return (f'{d[0]}: Apply {op} to two selections of `{col}` from `{t}`. Left filter: `{a}`. Right filter: `{b}`. Order by the selected column(s).',f'SELECT {col} FROM {t} WHERE {a}\n{op}\nSELECT {col} FROM {t} WHERE {b}\nORDER BY {col};', 'UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.')
        exercise('SET_OPERATIONS',op.title(),make)

def joins():
    for kind in ['INNER','LEFT','RIGHT','FULL','CROSS']:
        def make(d,v,kind=kind):
            p,t=party(d),table(d)
            if kind=='CROSS':
                variants = [
                    ('List every party/record ID pair.',f'SELECT p.PartyID, f.RecordID FROM {p} p CROSS JOIN {t} f ORDER BY p.PartyID, f.RecordID;', '60 rows: 5 parties times 12 records.'),
                    ('List every North-region party paired with every Open record.',f"SELECT p.PartyID, f.RecordID FROM {p} p CROSS JOIN {t} f WHERE p.Region = 'North' AND f.Status = 'Open' ORDER BY p.PartyID, f.RecordID;",'8 rows: 2 North parties times 4 Open records.'),
                    ('Pair each party with planning categories A, B and C (use a VALUES table).',f"SELECT p.PartyID, c.Category FROM {p} p CROSS JOIN (VALUES ('A'),('B'),('C')) c(Category) ORDER BY p.PartyID, c.Category;",'15 planning combinations.'),
                    ('Count the Cartesian product of all parties and all records.',f'SELECT COUNT(*) AS PairCount FROM {p} p CROSS JOIN {t} f;','One row, PairCount=60.'),
                    ('Cross join parties and records, then filter equal PartyID values; return party and record IDs.',f'SELECT p.PartyID, f.RecordID FROM {p} p CROSS JOIN {t} f WHERE p.PartyID = f.PartyID ORDER BY p.PartyID, f.RecordID;','10 rows; equivalent to the corresponding inner join.')]
                a,b,c=variants[v]
                return (f'{d[0]}: {a} Tables: `{p}` and `{t}`.',b,c)
            if kind=='RIGHT':
                frm=f'{t} f RIGHT JOIN {p} p ON p.PartyID = f.PartyID'
            else:
                frm=f'{p} p {kind} JOIN {t} f ON p.PartyID = f.PartyID'
            desc={'INNER':'matched parties and records only','LEFT':'all parties, including parties with no records','RIGHT':'all parties, including parties with no records (facts on the left)','FULL':'all parties and all records, including both unmatched sides'}[kind]
            variants=[
                (f'Use a {kind} JOIN to list party ID, party name and record ID for {desc}.', 'p.PartyID, p.PartyName, f.RecordID','','ORDER BY p.PartyID, f.RecordID'),
                (f'Use a {kind} JOIN for {desc}, but only Open records may match; place that condition in ON. Return party and record IDs.', 'p.PartyID, f.RecordID'," AND f.Status = 'Open'",'ORDER BY p.PartyID, f.RecordID'),
                (f'Use a {kind} JOIN for {desc}; return party ID, name and count of matched records per party. For FULL JOIN, include the NULL party group.', 'p.PartyID, p.PartyName, COUNT(f.RecordID) AS RecordCount','','GROUP BY p.PartyID, p.PartyName ORDER BY p.PartyID'),
                (f'Use a {kind} JOIN for {desc}; return both party IDs and record ID, then keep rows with an unmatched side (either key is NULL).', 'p.PartyID AS MasterPartyID, f.PartyID AS FactPartyID, f.RecordID','','WHERE p.PartyID IS NULL OR f.RecordID IS NULL ORDER BY p.PartyID, f.RecordID'),
                (f'Use a {kind} JOIN for {desc}; retain North-region parties only using WHERE and return party ID, record ID and amount.', 'p.PartyID, f.RecordID, f.Amount','','WHERE p.Region = \'North\' ORDER BY p.PartyID, f.RecordID')]
            a,b,c,e=variants[v]
            return (f'{d[0]}: {a} Join `{p}` p and `{t}` f on PartyID.',f'SELECT {b}\nFROM {frm}{c}\n{e};','Baseline cardinalities: INNER=10; LEFT=RIGHT=11 (preserving parties); FULL=13. An ON filter and a WHERE filter can preserve different unmatched rows. The INNER unmatched-side task correctly returns zero rows.')
        exercise('JOINS',kind.title()+' Join',make)

def string_functions():
    exprs = {
        'Length Function (LEN)': [('LEN(Label)','label length excluding trailing spaces'),('LEN(TRIM(Label))','trimmed label length'),('LEN(Note)','note length, preserving NULL'),("LEN(Label + N'!') - 1",'label length including trailing spaces'),('LEN(REPLACE(Label,N\'-\',N\'\'))','label length after removing hyphens (trailing spaces excluded)')],
        'Substring Function (SUBSTRING)': [('SUBSTRING(Label,1,5)','first five characters'),('SUBSTRING(Label,3,4)','four characters starting at position three'),("SUBSTRING(Label,CHARINDEX(N'-',Label)+1,80)",'text after the first hyphen'),('SUBSTRING(TRIM(Label),2,3)','three characters from position two after trimming'),('SUBSTRING(Note,1,4)','first four note characters')],
        'Concatenation Operator (+)': [("Label + N' / ' + Category",'label, slash separator and category'),("Category + ':' + Status",'category and status separated by a colon'),("N'ID-' + CONVERT(nvarchar(12),RecordID)",'ID- followed by record ID'),("Label + N': ' + ISNULL(Note,N'missing')",'label, colon-space and note with missing as fallback'),("CONVERT(nvarchar(10),EventDate,23) + N' ' + Label",'ISO date, space and label')],
        'Lower Function (LOWER)': [('LOWER(Label)','lowercase label'),('LOWER(TRIM(Label))','trimmed lowercase label'),('LOWER(Status)','lowercase status'),('LOWER(Note)','lowercase note'),("LOWER(Category + '-' + Status)",'lowercase category-status key')],
        'Upper Function (UPPER)': [('UPPER(Label)','uppercase label'),('UPPER(TRIM(Label))','trimmed uppercase label'),('UPPER(Status)','uppercase status'),('UPPER(Note)','uppercase note'),("UPPER(Category + '-' + Status)",'uppercase category-status key')],
        'Trim Function (TRIM)': [('TRIM(Label)','label without leading or trailing spaces'),('TRIM(Note)','trimmed note'),('LOWER(TRIM(Label))','trimmed lowercase label'),('LEN(TRIM(Label))','trimmed label length'),("TRIM(Label) + N':' + TRIM(Status)",'trimmed label and status joined by a colon')],
        'Ltrim Function (LTRIM)': [('LTRIM(Label)','label without leading spaces'),('LEN(Label)-LEN(LTRIM(Label))','number of leading spaces'),('LTRIM(Note)','note without leading spaces'),("LTRIM(N'   ' + Label)",'label after adding three leading spaces then removing all leading spaces'),('LOWER(LTRIM(Label))','lowercase label without leading spaces')],
        'Rtrim Function (RTRIM)': [('RTRIM(Label)','label without trailing spaces'),('(DATALENGTH(Label)-DATALENGTH(RTRIM(Label)))/2','number of trailing spaces in the nvarchar label'),('RTRIM(Note)','note without trailing spaces'),("RTRIM(Label + N'   ')",'label after appending three spaces then removing trailing spaces'),('UPPER(RTRIM(Label))','uppercase label without trailing spaces')],
        'Charindex Function (CHARINDEX)': [("CHARINDEX(N'-',Label)",'first hyphen position'),("CHARINDEX(N'a',LOWER(Label))",'first lowercase a position in the lowercased label'),("CHARINDEX(N'-',Label,6)",'first hyphen position at or after character six'),("CHARINDEX(N'z',LOWER(Label))",'first z position, or zero if absent'),("CHARINDEX(N'firm',Note)",'firm substring position in the note')],
        'Left Function (LEFT)': [('LEFT(Label,3)','first three untrimmed characters'),('LEFT(TRIM(Label),5)','first five trimmed characters'),("LEFT(Label,CHARINDEX(N'-',Label)-1)",'prefix before the hyphen (all fixture labels have one)'),('LEFT(Status,1)','status initial'),('LEFT(Note,4)','first four note characters')],
        'Right Function (RIGHT)': [('RIGHT(Label,3)','last three untrimmed characters'),('RIGHT(TRIM(Label),4)','last four trimmed characters'),("RIGHT(Label,LEN(Label + N'!')-1-CHARINDEX(N'-',Label))",'suffix after the hyphen, preserving trailing spaces'),('RIGHT(Status,2)','last two status characters'),("RIGHT(N'0000'+CONVERT(nvarchar(12),RecordID),4)",'record ID padded to four digits')],
        'Reverse Function (REVERSE)': [('REVERSE(Label)','reversed raw label'),('REVERSE(TRIM(Label))','reversed trimmed label'),('REVERSE(Status)','reversed status'),('REVERSE(Note)','reversed note'),('LEFT(REVERSE(TRIM(Label)),3)','first three characters of the reversed trimmed label')],
        'Replace Function (REPLACE)': [("REPLACE(Label,N'-',N' ')",'label with hyphens replaced by spaces'),("REPLACE(Label,N' ',N'')",'label with all spaces removed'),("REPLACE(LOWER(Label),N'alpha',N'priority')",'lowercase label with alpha replaced by priority'),("REPLACE(Status,'Pending','Review')",'status with Pending replaced by Review'),("REPLACE(Note,N'confirmed',N'checked')",'note with confirmed replaced by checked')],
        'Case Statement (CASE)': [("CASE WHEN Amount IS NULL THEN 'Unknown' WHEN Amount >= 200 THEN 'High' ELSE 'Standard' END",'amount band Unknown / High (at least 200) / Standard'),("CASE Status WHEN 'Open' THEN 1 WHEN 'Pending' THEN 2 ELSE 3 END",'status priority Open=1, Pending=2, otherwise 3'),("CASE WHEN PartyID IS NULL THEN 'Missing' ELSE 'Present' END",'party ID presence flag'),("CASE WHEN Quantity >= 3 THEN 'Bulk' ELSE 'Small' END",'quantity band Bulk (at least 3) or Small'),("CASE WHEN EventDate < '20240701' THEN 'H1' ELSE 'H2-or-later' END",'H1 if before July 2024, otherwise H2-or-later')],
        'ISNULL Function (ISNULL)': [('ISNULL(Amount,0)','amount with NULL replaced by zero'),("ISNULL(Note,N'not recorded')",'note with not recorded fallback'),('ISNULL(PartyID,-1)','party ID with -1 fallback'),('ISNULL(Amount,0)*Quantity','extended amount with zero for missing amount'),("ISNULL(Note,ISNULL(BackupNote,N'unavailable'))",'first non-NULL of Note, BackupNote, unavailable using nested ISNULL')],
        'Coalesce Function (COALESCE)': [("COALESCE(Note,BackupNote,N'unavailable')",'first non-NULL of Note, BackupNote, unavailable'),('COALESCE(Amount,0)','amount with zero fallback'),("COALESCE(BackupNote,Note,N'unavailable')",'first non-NULL of BackupNote, Note, unavailable'),("COALESCE(CONVERT(nvarchar(12),PartyID),N'unassigned')",'party ID text with unassigned fallback'),("COALESCE(NULLIF(TRIM(Note),N''),BackupNote,N'unavailable')",'note ignoring blank/NULL notes, then backup, then unavailable')],
    }
    for sub, variants in exprs.items():
        def make(d,v,variants=variants):
            expr,desc=variants[v]
            return query(d,f'Return RecordID and {desc} as Result, in record ID order.',f'RecordID, {expr} AS Result','\nORDER BY RecordID','Return 12 rows. Preserve the fixture whitespace and NULL values; the reference expression specifies the expected result for every row.')
        exercise('STRING_FUNCTIONS',sub,make)

def dates():
    specs = {
        'Current Date and time (GETDATE)': [('GETDATE()','current server-local date/time (repeat alongside each record)'),('CONVERT(date,GETDATE())','current server-local date'),('DATEDIFF(day,EventDate,CONVERT(date,GETDATE()))','calendar day boundaries from event date to server-local today'),('DATEADD(day,7,GETDATE())','server-local time seven days from now'),('CONVERT(varchar(19),GETDATE(),120)','current server-local time formatted yyyy-mm-dd hh:mm:ss')],
        'Date Part Function (DATEPART)': [('DATEPART(year,EventDate)','event year'),('DATEPART(month,EventDate)','event month'),('DATEPART(day,EventDate)','day of month'),('DATEPART(quarter,EventDate)','quarter'),('DATEPART(hour,EventTime)','event hour')],
        'Date Difference Function (DATEDIFF)': [("DATEDIFF(day,EventDate,CONVERT(date,'20250101',112))",'day boundaries to 2025-01-01'),("DATEDIFF(month,EventDate,CONVERT(date,'20250101',112))",'month boundaries to 2025-01-01'),("DATEDIFF(year,EventDate,CONVERT(date,'20250101',112))",'year boundaries to 2025-01-01 (not completed years)'),('DATEDIFF(minute,CONVERT(datetime2(3),EventDate),EventTime)','minute boundaries from event midnight'),('DATEDIFF(second,EventTime,DATEADD(minute,90,EventTime))','second boundaries in a 90-minute interval')],
        'Date Addition/Subtraction': [('DATEADD(day,7,EventDate)','event date plus seven days'),('DATEADD(month,-1,EventDate)','event date minus one month'),('DATEADD(year,1,EventDate)','event date plus one year (observe leap day)'),('DATEADD(hour,6,EventTime)','event timestamp plus six hours'),('DATEADD(minute,-90,EventTime)','event timestamp minus ninety minutes')],
        'Date Formatting (FORMAT)': [(f"FORMAT(EventTime,'{fmt}','en-US')",f'event timestamp formatted {fmt} with en-US culture') for fmt in ['yyyy-MM-dd','dd MMM yyyy','MMMM yyyy','HH:mm:ss','yyyyMMdd']],
        'Weekday Function (DATEPART)': [('DATEPART(weekday,EventDate)','weekday number with Monday=1'),("CASE WHEN DATEPART(weekday,EventDate) IN (6,7) THEN 'Weekend' ELSE 'Weekday' END",'weekday/weekend classification'),('DATEPART(weekday,DATEADD(day,7,EventDate))','weekday number seven days later'),('DATEPART(weekday,DATEADD(day,1,EventDate))','weekday number on the next day'),('DATEADD(day,1-DATEPART(weekday,EventDate),EventDate)','Monday starting the event week')],
        'Date to String (Various formats)': [(f'CONVERT(varchar(10),EventDate,{n})',f'event date as {fmt} (style {n})') for n,fmt in [(23,'yyyy-mm-dd'),(101,'mm/dd/yyyy'),(103,'dd/mm/yyyy'),(112,'yyyymmdd'),(105,'dd-mm-yyyy')]],
        'DateTime to String (Various formats)': [(f'CONVERT(varchar(30),EventTime,{n})',f'event timestamp as text using CONVERT style {n}') for n in [120,121,126,113,109]],
        'String to Date (Various formats)': [(f"CONVERT(date,'{s}',{n})",f'typed date parsed from {s} using style {n}') for s,n in [('2024-04-15',23),('04/15/2024',101),('15/04/2024',103),('15.04.2024',104),('20240415',112)]],
        'String to DateTime (Various formats)': [(f"CONVERT(datetime2(3),'{s}',{n})",f'timestamp parsed from {s} using style {n}') for s,n in [('2024-04-15 13:30:45',120),('2024-04-15 13:30:45.375',121),('2024-04-15T13:30:45.375',126),('15/04/2024 13:30:45',103),('04/15/2024 13:30:45',101)]],
        'Date and Time': [('CONVERT(date,EventTime)','date portion of the timestamp'),('CONVERT(time(3),EventTime)','time portion of the timestamp'),('CONVERT(datetime2(3),EventDate)','date expanded to midnight'),('DATEPART(millisecond,EventTime)','millisecond component'),('DATEDIFF(second,CONVERT(datetime2(3),EventDate),EventTime)','seconds since midnight')],
        'Timezones': [(f"EventTime AT TIME ZONE 'UTC' AT TIME ZONE '{z}'",f'UTC EventTime converted to Windows zone {z}') for z in ['UTC','Eastern Standard Time','India Standard Time','Central Standard Time','Pacific Standard Time']],
        'UTC': [("EventTime AT TIME ZONE 'UTC'",'UTC offset attached to the known-UTC EventTime'),("RecordedAt AT TIME ZONE 'UTC'",'RecordedAt converted to UTC'),("SWITCHOFFSET(RecordedAt,'+00:00')",'RecordedAt normalized to zero offset'),('SYSUTCDATETIME()','current UTC timestamp (nondeterministic)'),("CONVERT(datetime2(3),RecordedAt AT TIME ZONE 'UTC')",'UTC wall time from RecordedAt, then remove offset metadata')],
        'Offsets': [(f"SWITCHOFFSET(RecordedAt,'{o}')",f'RecordedAt represented at fixed offset {o}, preserving the instant') for o in ['+00:00','+05:30','-05:00','+02:00','-08:00']],
        'Applying an Offset to a Date Datatype Column': [(f"TODATETIMEOFFSET(CONVERT(datetime2(3),EventDate),'{o}')",f'event date interpreted as midnight at fixed offset {o}; attach an offset, do not convert an instant') for o in ['+00:00','+05:30','-05:00','+02:00','-08:00']],
        'Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones)': [(f"EventTime AT TIME ZONE '{z}'",f'EventTime interpreted, for this exercise only, as local wall time in {z}, with the zone offset attached') for z in ['UTC','Eastern Standard Time','India Standard Time','Central Standard Time','Pacific Standard Time']],
        'Cast a DateTime Timezone to another TimeZone': [(f"RecordedAt AT TIME ZONE '{z}'",f'RecordedAt instant converted to {z}, keeping offset information') for z in ['Eastern Standard Time','India Standard Time','UTC','Central Standard Time','Pacific Standard Time']],
    }
    for sub, variants in specs.items():
        def make(d,v,variants=variants,sub=sub):
            expr,desc=variants[v]
            a,b,c=query(d,f'Return RecordID and {desc} as Result, ordered by RecordID.',f'RecordID, {expr} AS Result','\nORDER BY RecordID','Compare 12 rows to the reference. GETDATE/SYSUTCDATETIME results vary by execution time; compare type and relationship instead of exact clock value. Named zones apply rules for the event date; fixed offsets do not encode daylight saving rules.')
            if sub=='Weekday Function (DATEPART)':
                a+=' Set DATEFIRST to 1 explicitly.'
                b='SET DATEFIRST 1;\n'+b
                c='2024-01-01 is Monday: DATEPART(weekday)=1. DATEFIRST=1 makes Saturday/Sunday 6/7.'
            if 'String' in sub or sub=='Date Formatting (FORMAT)':
                b='SET LANGUAGE us_english;\n'+b
            return a,b,c
        exercise('DATE_FUNCTIONS',sub,make)

def analytics():
    def window(d,v,fn):
        t=table(d)
        if fn=='Aggregate Functions':
            exprs=['SUM(Amount) OVER (PARTITION BY Category)','AVG(Amount) OVER (PARTITION BY Status)','COUNT(*) OVER (PARTITION BY PartyID)','SUM(Amount) OVER (ORDER BY EventDate, RecordID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)','MAX(Amount) OVER () - Amount']
            desc=['category total repeated on every row','status average repeated on every row','party record count (NULL party IDs form one partition)','running total by EventDate then RecordID, using an explicit ROWS frame','difference between the global maximum amount and this row amount']
            return query(d,f'Return RecordID and {desc[v]} as Result using a window function.',f'RecordID, {exprs[v]} AS Result','\nORDER BY RecordID','Window functions retain all 12 source rows; NULL Amount remains NULL in subtraction. Running totals use a deterministic order.')
        if fn in ['ROW_NUMBER()','RANK()','DENSE_RANK()','NTILE(n)']:
            call={'ROW_NUMBER()':'ROW_NUMBER()','RANK()':'RANK()','DENSE_RANK()':'DENSE_RANK()','NTILE(n)':'NTILE(4)'}[fn]
            tie=', RecordID' if fn in ['ROW_NUMBER()','NTILE(n)'] else ''
            windows=[f'ORDER BY Amount DESC{tie}',f'PARTITION BY Category ORDER BY Amount DESC{tie}',f'PARTITION BY Status ORDER BY Amount DESC{tie}',f'ORDER BY EventDate{tie}',f'PARTITION BY Category ORDER BY Amount DESC{tie}']
            scope=['all records by decreasing amount','each category by decreasing amount','each status by decreasing amount','all records by increasing date','each category by decreasing amount'][v]
            prompt=f'{d[0]}: Use {call} over {scope} in `{t}`. '
            if tie: prompt+='Break ties by RecordID ascending. '
            else: prompt+='Equal ordering values must share a rank; do not add RecordID to the window order. '
            sql=f'SELECT RecordID, Category, Amount, {call} OVER ({windows[v]}) AS Position\nFROM {t}'
            if v==4:
                prompt+='Return only Position <= 2, showing RecordID, Category, Amount, Position.'
                sql=f';WITH Ranked AS (\n{sql}\n)\nSELECT RecordID, Category, Amount, Position FROM Ranked WHERE Position <= 2 ORDER BY Category, Position, RecordID;'
            else:
                prompt+='Return RecordID, Category, Amount and Position, in RecordID order.'
                sql+='\nORDER BY RecordID;'
            return prompt,sql,'RANK leaves gaps after ties; DENSE_RANK does not. ROW_NUMBER is unique within its partition. NTILE(4) splits rows into up to four buckets; it may separate equal amounts.'
        func=fn.split('(')[0]
        if func in ['LAG','LEAD']:
            exprs=[f'{func}(Amount) OVER (ORDER BY EventDate, RecordID)',f'{func}(Amount) OVER (PARTITION BY Category ORDER BY EventDate, RecordID)',f'{func}(Amount,2) OVER (ORDER BY EventDate, RecordID)',f'Amount - {func}(Amount) OVER (PARTITION BY PartyID ORDER BY EventDate, RecordID)',f'{func}(EventDate,1) OVER (PARTITION BY Category ORDER BY EventDate, RecordID)']
            direction='previous' if func=='LAG' else 'next'
            desc=[f'{direction} amount across all records',f'{direction} amount within category',f'amount two rows {"earlier" if func=="LAG" else "later"}',f'current minus {direction} amount within party',f'{direction} date within category']
        else:
            frame='ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING'
            exprs=[f'{func}(Amount) OVER (ORDER BY EventDate, RecordID {frame})',f'{func}(Amount) OVER (PARTITION BY Category ORDER BY EventDate, RecordID {frame})',f'{func}(Label) OVER (PARTITION BY Status ORDER BY EventDate, RecordID {frame})',f'Amount - {func}(Amount) OVER (PARTITION BY PartyID ORDER BY EventDate, RecordID {frame})',f'{func}(EventDate) OVER (PARTITION BY Category ORDER BY EventDate, RecordID {frame})']
            edge='first' if func=='FIRST_VALUE' else 'last'
            desc=[f'{edge} chronological amount across all records',f'{edge} chronological amount within category',f'{edge} chronological label within status',f'current amount minus {edge} chronological amount within party',f'{edge} chronological date within category']
        return query(d,f'Return RecordID and {desc[v]} as Result using {fn}. Order the window by EventDate, RecordID. Use the full partition for FIRST_VALUE/LAST_VALUE; do not skip NULLs.',f'RecordID, {exprs[v]} AS Result','\nORDER BY RecordID','Compare all rows, including NULL results at window boundaries or from NULL source amounts. LAST_VALUE requires the full-partition frame to find the final row.')
    for fn in ['Aggregate Functions','ROW_NUMBER()','RANK()','DENSE_RANK()','NTILE(n)','LAG()','LEAD()','FIRST_VALUE()','LAST_VALUE()']:
        exercise('ANALYTICAL_FUNCTIONS',fn,lambda d,v,fn=fn:window(d,v,fn))

def ctes():
    def make(d,v,sub):
        t=table(d)
        base=[
            ("Open records",f"SELECT RecordID, Amount FROM {t} WHERE Status = 'Open'",'RecordID, Amount','RecordID'),
            ('category totals',f'SELECT Category, SUM(Amount) AS TotalAmount FROM {t} GROUP BY Category','Category, TotalAmount','Category'),
            ('party counts',f'SELECT PartyID, COUNT(*) AS RecordCount FROM {t} GROUP BY PartyID','PartyID, RecordCount','PartyID'),
            ('positive-amount records',f'SELECT RecordID, Amount FROM {t} WHERE Amount > 0','RecordID, Amount','RecordID'),
            ('year/month counts',f'SELECT YEAR(EventDate) AS Y, MONTH(EventDate) AS M, COUNT(*) AS RecordCount FROM {t} GROUP BY YEAR(EventDate), MONTH(EventDate)','Y, M, RecordCount','Y, M')]
        if sub=='Creating a CTE':
            label,body,cols,order=base[v]
            return (f'{d[0]}: Define a CTE named Report for {label} from `{t}`, then select `{cols}` ordered by `{order}`.',f';WITH Report AS (\n{body}\n)\nSELECT {cols} FROM Report ORDER BY {order};','The CTE is consumed by the immediately following statement; compare its full result with the reference.')
        if sub=='Using Multiple CTEs':
            conditions=["Status = 'Open'",'Amount > 0',"EventDate < '20240301'",'Quantity >= 2','Amount IS NOT NULL']
            pred=conditions[v]
            return (f'{d[0]}: Use Filtered and Totals CTEs in one statement: filter `{t}` by `{pred}`, then aggregate Amount per Category. Return categories with totals >= 100, ordered by Category.',f';WITH Filtered AS (SELECT Category, Amount FROM {t} WHERE {pred}),\nTotals AS (SELECT Category, SUM(Amount) AS TotalAmount FROM Filtered GROUP BY Category)\nSELECT Category, TotalAmount FROM Totals WHERE TotalAmount >= 100 ORDER BY Category;','Second CTE references the first; filtering happens before aggregation, and the final filter after aggregation.')
        if sub=='Recursive CTEs':
            if v<3:
                root=[1,2,3][v]
                return (f'{d[0]}: Traverse `{t}` from RecordID {root}, following ParentID to descendants. Include the root at depth zero; return RecordID, ParentID, Depth ordered by depth then ID. Limit recursion to 100.',f';WITH Tree AS (\n SELECT RecordID, ParentID, 0 AS Depth FROM {t} WHERE RecordID = {root}\n UNION ALL\n SELECT f.RecordID, f.ParentID, t.Depth + 1 FROM {t} f JOIN Tree t ON f.ParentID = t.RecordID\n)\nSELECT RecordID, ParentID, Depth FROM Tree ORDER BY Depth, RecordID OPTION (MAXRECURSION 100);',f'Fixture is acyclic. Expected subtree size for root {root}: '+str({1:12,2:7,3:4}[root])+'. The depth increments once per edge.')
            if v==3:
                return (f'{d[0]}: Generate dates 2024-01-01 through 2024-01-07 using a recursive CTE. Left join `{t}` to show daily record counts including zero days.',f";WITH Days AS (SELECT CONVERT(date,'20240101',112) AS D UNION ALL SELECT DATEADD(day,1,D) FROM Days WHERE D < '20240107')\nSELECT d.D, COUNT(f.RecordID) AS RecordCount FROM Days d LEFT JOIN {t} f ON f.EventDate = d.D GROUP BY d.D ORDER BY d.D OPTION (MAXRECURSION 100);",'Seven rows with counts 1, 2, 1, 0, 0, 0, 0.')
            return (f'{d[0]}: Recursively generate integers 1 through 4 as quantity targets. Left join `{t}` on Quantity and count records per target.',f';WITH Targets AS (SELECT 1 AS N UNION ALL SELECT N+1 FROM Targets WHERE N<4)\nSELECT x.N, COUNT(f.RecordID) AS RecordCount FROM Targets x LEFT JOIN {t} f ON f.Quantity = x.N GROUP BY x.N ORDER BY x.N OPTION (MAXRECURSION 100);','Four rows: each quantity target has three records.')
        if sub=='Common Use Cases for CTEs':
            variants=[
                ('Return the highest-amount record per category; break ties by ID.',f';WITH R AS (SELECT RecordID, Category, Amount, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Amount DESC, RecordID) AS N FROM {t}) SELECT RecordID, Category, Amount FROM R WHERE N=1 ORDER BY Category;','One record per category.'),
                ('Return records whose amount is greater than their category average.',f';WITH A AS (SELECT Category, AVG(Amount) AS MeanAmount FROM {t} GROUP BY Category) SELECT f.RecordID, f.Amount FROM {t} f JOIN A ON f.Category=A.Category WHERE f.Amount>A.MeanAmount ORDER BY f.RecordID;','Category averages ignore NULL amounts.'),
                ('Find repeated known Amount values and show their frequency.',f';WITH D AS (SELECT Amount, COUNT(*) AS N FROM {t} WHERE Amount IS NOT NULL GROUP BY Amount) SELECT Amount, N FROM D WHERE N>1 ORDER BY Amount;','Amount 200 occurs three times; 300 twice.'),
                ('Show running totals by date then ID; return only records where the running total exceeds 500.',f';WITH R AS (SELECT RecordID, SUM(Amount) OVER (ORDER BY EventDate,RecordID ROWS UNBOUNDED PRECEDING) AS RunningAmount FROM {t}) SELECT RecordID, RunningAmount FROM R WHERE RunningAmount>500 ORDER BY RecordID;','Filter after computing the window.'),
                ('List each master party with zero records using a CTE of distinct non-NULL fact PartyIDs.',f';WITH Active AS (SELECT DISTINCT PartyID FROM {t} WHERE PartyID IS NOT NULL) SELECT p.PartyID, p.PartyName FROM {party(d)} p LEFT JOIN Active a ON p.PartyID=a.PartyID WHERE a.PartyID IS NULL ORDER BY p.PartyID;','PartyID 5 only.')]
            a,b,c=variants[v]
            return f'{d[0]}: {a} Use a CTE and `{t}` (plus `{party(d)}` if needed).',b,c
        label,body,cols,order=base[v]
        return (f'{d[0]}: Refactor this derived-table report into a named CTE without changing output: `SELECT {cols} FROM ({body}) x ORDER BY {order};` Explain scope, readability and whether the CTE guarantees materialization or a speedup.',f';WITH Report AS ({body})\nSELECT {cols} FROM Report ORDER BY {order};','Output must equal the original report. A CTE names a query expression, is scoped to one statement, and does not guarantee caching, materialization or better performance.')
    for sub in ['Creating a CTE','Using Multiple CTEs','Recursive CTEs','Common Use Cases for CTEs','Benefits of Using CTEs']:
        exercise('CTE',sub,lambda d,v,sub=sub:make(d,v,sub))



def data_types():
    ordinary = {
        'INT':('int','2147483647','whole-item count','INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.'),
        'BIGINT':('bigint','CAST(2147483648 AS bigint)','high-volume record identifier','BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.'),
        'DECIMAL':('decimal(5,2)','999.99','exact amount','DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.'),
        'NUMERIC':('numeric(7,2)','12345.67','exact quantity','NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.'),
        'FLOAT':('float','0.1','approximate sensor measurement','FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.'),
        'DATE':('date',"CONVERT(date,'20240229',112)",'business date','DATE has no time or offset. It stores a date value, not a display format.'),
        'DATETIME':('datetime',"CONVERT(datetime,'2024-04-15T13:30:45.123',126)",'legacy event time','DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.'),
        'SMALLDATETIME':('smalldatetime',"CONVERT(smalldatetime,'2024-04-15T13:30:45',126)",'minute-resolution appointment','SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.'),
        'DATETIMEOFFSET':('datetimeoffset(3)',"CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127)",'offset-aware event time','DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.'),
        'TIME':('time(3)',"CONVERT(time(3),'13:30:45.123')",'daily opening time','TIME contains neither a date nor an offset; it cannot uniquely identify an instant.'),
        'DATETIME2':('datetime2(3)',"CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126)",'precise event timestamp','DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.'),
        'CHAR(n)':('char(5)',"'US'",'fixed-width code','CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.'),
        'VARCHAR(n)':('varchar(20)',"'Batch-A'",'variable-length code','VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.'),
        'BINARY':('binary(4)','0x0102','fixed-width token','BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.'),
        'VARBINARY':('varbinary(max)','0x01020304','document bytes','VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.'),
        'UNIQUEIDENTIFIER':('uniqueidentifier',"CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc')",'distributed correlation ID','UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.'),
        'BIT':('bit','1','active flag','A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.'),
        'MONEY':('money','1234.5678','legacy amount','MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.'),
        'SMALLMONEY':('smallmoney','123.4567','small legacy amount','SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.'),
    }
    for sub,(typ,val,field,note) in ordinary.items():
        def make(d,v,typ=typ,val=val,field=field,note=note):
            prefix=f'{d[0]}: Model a {field} using `{typ}` and sample `{val}`. '
            variants=[
                ('Declare @Value with this type, assign the sample and return it.',f'DECLARE @Value {typ} = {val};\nSELECT @Value AS Value;',note),
                ('Create #Work(ID int primary key, Value of this type nullable). Insert ID 1 with the sample and ID 2 with NULL; return both.',scratch(f'CREATE TABLE #Work(ID int PRIMARY KEY, Value {typ} NULL);\nINSERT #Work VALUES (1,{val}),(2,NULL);\nSELECT * FROM #Work ORDER BY ID;'),'Two rows; the second value is NULL. '+note),
                ('Assign the sample to a typed variable; show its value and DATALENGTH in bytes. Explain what the byte count does and does not prove.',f'DECLARE @Value {typ} = {val};\nSELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;','DATALENGTH measures expression bytes, not total on-disk row/index overhead. '+note),
                ('Create a nullable typed column, insert the sample and NULL, and report COUNT(*) and COUNT(Value). Explain the difference.',scratch(f'CREATE TABLE #Work(Value {typ} NULL);\nINSERT #Work VALUES ({val}),(NULL);\nSELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;'),'TotalRows=2 and KnownRows=1. '+note),
                ('Assess whether this type is suitable for the stated field. Demonstrate a typed conversion of the sample and explain one limitation or alternative.',f'SELECT CAST({val} AS {typ}) AS TypedValue;',note)]
            a,b,c=variants[v]
            return prefix+a,b,c
        exercise('DATATYPES',sub,make)
    text_variants=[
        ('Store a legacy note and retrieve it after casting to varchar(max).',"SELECT ID, CAST(LegacyNote AS varchar(max)) AS Note FROM #Work;",'legacy note is returned as modern text.'),
        ('Report the stored byte length of the legacy note.',"SELECT ID, DATALENGTH(LegacyNote) AS NoteBytes FROM #Work;",'The sample has 11 ASCII bytes.'),
        ('Search the legacy note for the word note after converting to varchar(max).',"SELECT ID FROM #Work WHERE CAST(LegacyNote AS varchar(max)) LIKE '%note%';",'ID 1 matches.'),
        ('Migrate the legacy column to varchar(max), then show its contents.',"ALTER TABLE #Work ALTER COLUMN LegacyNote varchar(max) NULL;\nSELECT * FROM #Work;",'Contents survive conversion; inspect the new type with sp_help.'),
        ('Return the first six characters using SUBSTRING, then explain why TEXT should be replaced in new designs.',"SELECT ID, SUBSTRING(LegacyNote,1,6) AS Prefix FROM #Work;",'Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).')]
    exercise('DATATYPES','TEXT',lambda d,v:(f'{d[0]}: Create #Work(ID int, LegacyNote text) and insert (1, legacy note). '+text_variants[v][0],scratch("CREATE TABLE #Work(ID int, LegacyNote text NULL);\nINSERT #Work VALUES (1,'legacy note');\n"+text_variants[v][1]),text_variants[v][2]))
    special={
        'XML':("DECLARE @x xml = N'<record id=\"1\"><amount>125.50</amount></record>';",[
            ('Return the typed XML document.','SELECT @x AS Document;','One XML value.'),
            ('Extract the record id as int.',"SELECT @x.value('(/record/@id)[1]','int') AS RecordID;",'RecordID=1.'),
            ('Extract the amount as decimal(12,2).',"SELECT @x.value('(/record/amount/text())[1]','decimal(12,2)') AS Amount;",'Amount=125.50.'),
            ('Test whether a record amount element exists.',"SELECT @x.exist('/record/amount') AS HasAmount;",'HasAmount=1.'),
            ('Return the record element using query().',"SELECT @x.query('/record') AS RecordXml;",'A record element with its id and amount is returned.')]),
        'GEOGRAPHY':('DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);',[
            ('Return the point as WKT.','SELECT @g.STAsText() AS Wkt;','WKT uses longitude then latitude, while Point takes latitude then longitude.'),
            ('Return latitude and longitude.','SELECT @g.Lat AS Latitude, @g.Long AS Longitude;','41.8781 and -87.6298.'),
            ('Return its SRID.','SELECT @g.STSrid AS SRID;','4326.'),
            ('Measure its distance to itself.','SELECT @g.STDistance(@g) AS Distance;','0 meters for this SRID.'),
            ('Measure distance to geography::Point(40.7128,-74.0060,4326).','SELECT @g.STDistance(geography::Point(40.7128,-74.0060,4326)) AS DistanceMeters;','Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.')]),
        'GEOMETRY':("DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);",[
            ('Return the geometry as WKT.','SELECT @g.STAsText() AS Wkt;','LINESTRING with endpoints (0 0) and (3 4).'),
            ('Find its planar length.','SELECT @g.STLength() AS Length;','Length=5 coordinate units.'),
            ('Return its number of points.','SELECT @g.STNumPoints() AS Points;','Points=2.'),
            ('Return its geometry type.','SELECT @g.STGeometryType() AS ShapeType;','LineString.'),
            ('Return the start point coordinates.','SELECT @g.STStartPoint().STX AS X, @g.STStartPoint().STY AS Y;','X=0, Y=0; geometry does not imply meters.')]),
        'HIERARCHYID':("DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');",[
            ('Return the hierarchy path as text.','SELECT @h.ToString() AS Path;','/1/2/.'),
            ('Return the node level.','SELECT @h.GetLevel() AS Level;','2.'),
            ('Return the parent path.','SELECT @h.GetAncestor(1).ToString() AS ParentPath;','/1/.'),
            ('Test whether the node descends from /1/.',"SELECT @h.IsDescendantOf(hierarchyid::Parse('/1/')) AS IsChild;",'1.'),
            ('Generate a first child below this node.','SELECT @h.GetDescendant(NULL,NULL).ToString() AS ChildPath;','/1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.')]),
    }
    for sub,(setup,variants) in special.items():
        exercise('DATATYPES',sub,lambda d,v,setup=setup,variants=variants:(f'{d[0]}: Use this input: `{setup}` '+variants[v][0],setup+'\n'+variants[v][1],variants[v][2]))
    def rowversion(d,v):
        variants=[
            ('Insert ID=1, Amount=100; return the auto-generated rowversion.','SELECT ID,Amount,VersionToken FROM #Work;','The token is automatically generated and is 8 bytes; its exact value depends on the database.'),
            ('Capture the token, update Amount to 200, and prove the token changed.',"DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);\nUPDATE #Work SET Amount=200 WHERE ID=1;\nSELECT CASE WHEN VersionToken<>@old THEN 1 ELSE 0 END AS Changed FROM #Work;",'Changed=1.'),
            ('Capture the token, update Amount to itself, and prove the token still changes.',"DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);\nUPDATE #Work SET Amount=Amount WHERE ID=1;\nSELECT CASE WHEN VersionToken<>@old THEN 1 ELSE 0 END AS Changed FROM #Work;",'Changed=1, even though the business value is unchanged.'),
            ('Use the current token in an optimistic-concurrency update to Amount=150; report affected rows.',"DECLARE @expected binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);\nUPDATE #Work SET Amount=150 WHERE ID=1 AND VersionToken=@expected;\nSELECT @@ROWCOUNT AS AffectedRows;",'AffectedRows=1.'),
            ('Capture a token, perform an intervening update to 150, then attempt an update to 200 using the old token.',"DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);\nUPDATE #Work SET Amount=150 WHERE ID=1;\nUPDATE #Work SET Amount=200 WHERE ID=1 AND VersionToken=@old;\nSELECT @@ROWCOUNT AS AffectedRows;\nSELECT Amount FROM #Work;",'Second update affects 0 rows; Amount stays 150.')]
        a,b,c=variants[v]
        return f'{d[0]}: Create #Work(ID int primary key, Amount int, VersionToken rowversion), seed (1,100). {a}',scratch('CREATE TABLE #Work(ID int PRIMARY KEY, Amount int, VersionToken rowversion);\nINSERT #Work(ID,Amount) VALUES (1,100);\n'+b),c+' ROWVERSION is not a date/time.'
    exercise('DATATYPES','ROWVERSION',rowversion)
    def cursor(d,v):
        filters=['1=1',"Status='Open'",'Amount IS NULL','Amount>=200','PartyID IS NULL']
        t=table(d); pred=filters[v]
        sql=f'DECLARE @c CURSOR;\nDECLARE @id int, @count int=0;\nSET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT RecordID FROM {t} WHERE {pred} ORDER BY RecordID;\nOPEN @c;\nFETCH NEXT FROM @c INTO @id;\nWHILE @@FETCH_STATUS=0\nBEGIN\n SELECT @id AS RecordID;\n SET @count+=1;\n FETCH NEXT FROM @c INTO @id;\nEND;\nCLOSE @c;\nDEALLOCATE @c;\nSELECT @count AS VisitedRows;\nSELECT COUNT(*) AS SetBasedCount FROM {t} WHERE {pred};'
        return f'{d[0]}: Declare a CURSOR variable over `{t}` where `{pred}`. Visit IDs in order, count visits, close and deallocate the cursor; compare with a set-based count.',sql,f'VisitedRows = SetBasedCount = {[12,4,1,5,1][v]}. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.'
    exercise('DATATYPES','CURSOR',cursor)

def administration():
    def database(d,v):
        name=d[1].title()+'AssignmentLab'
        variants=[
            (f'Write a script to create an empty database named {name}. Run separately with instructor-authorized CREATE DATABASE permission.',f'USE master;\nGO\nCREATE DATABASE [{name}];\nGO\nSELECT name FROM sys.databases WHERE name=N\'{name}\';','One matching name after creation. Start with this name unused; do not run in a transaction.'),
            ('Report the current database name, ID and collation.',"SELECT DB_NAME() AS DatabaseName, DB_ID() AS DatabaseID, DATABASEPROPERTYEX(DB_NAME(),'Collation') AS Collation;",'Values describe the selected training database.'),
            ('List visible databases and their state and recovery model.', 'SELECT name, state_desc, recovery_model_desc FROM sys.databases ORDER BY name;','Results depend on permissions and the server; one row per visible database.'),
            ('List the current database data/log file logical names, types and allocated sizes in MB.', 'SELECT name, type_desc, size*8.0/1024 AS SizeMB FROM sys.database_files ORDER BY file_id;','size is stored in 8-KB pages; this reports allocated file size, not used space.'),
            ('Report current database compatibility level and explain how an instance, database and schema differ.', 'SELECT name, compatibility_level FROM sys.databases WHERE database_id=DB_ID();','An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.')]
        a,b,c=variants[v]
        return f'{d[0]}: {a}',b,c
    exercise('DATABASE_SCHEMA_USER','Database',database)
    def schema(d,v):
        name=d[1]+'AssignmentSchema'
        variants=[
            (f'Create schema {name} owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA.',f"EXEC(N'CREATE SCHEMA [{name}] AUTHORIZATION dbo;');\nSELECT name, USER_NAME(principal_id) AS OwnerName FROM sys.schemas WHERE name=N'{name}';",'OwnerName=dbo.'),
            (f'Create schema {name} and a table Records(ID int); show its two-part name, then drop the table followed by the schema.',f"EXEC(N'CREATE SCHEMA [{name}] AUTHORIZATION dbo;');\nCREATE TABLE [{name}].Records(ID int);\nSELECT SCHEMA_NAME(schema_id) AS SchemaName, name FROM sys.tables WHERE object_id=OBJECT_ID(N'{name}.Records');",'The table belongs to the new schema.'),
            ('List the tables belonging to the existing domain schema.',f"SELECT name FROM sys.tables WHERE schema_id=SCHEMA_ID(N'{d[1]}') ORDER BY name;",f'{d[2]} and {d[3]} after setup.'),
            (f'Create schema {name} and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema.',f"EXEC(N'CREATE SCHEMA [{name}] AUTHORIZATION dbo;');\nCREATE TABLE dbo.TransferLab(ID int);\nALTER SCHEMA [{name}] TRANSFER dbo.TransferLab;\nSELECT OBJECT_ID(N'{name}.TransferLab') AS TransferredObjectID;",'The object resolves under the new schema; choose an unused dbo.TransferLab name.'),
            (f'Create schema {name}, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA.',f"EXEC(N'CREATE SCHEMA [{name}];');\nALTER AUTHORIZATION ON SCHEMA::[{name}] TO dbo;\nSELECT USER_NAME(principal_id) AS OwnerName FROM sys.schemas WHERE name=N'{name}';",'OwnerName=dbo.')]
        a,b,c=variants[v]
        if v!=2:
            guard=f"IF SCHEMA_ID(N'{name}') IS NOT NULL THROW 51000, 'Use an unused schema name', 1;\n"
            if v==3: guard+="IF OBJECT_ID(N'dbo.TransferLab') IS NOT NULL THROW 51000, 'Use an unused scratch table name', 1;\n"
            b=guard+'BEGIN TRANSACTION;\nBEGIN TRY\n'+b+'\nROLLBACK TRANSACTION;\nEND TRY\nBEGIN CATCH\n IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;\n THROW;\nEND CATCH;'
        return f'{d[0]}: {a} Use a practice database.',b,c+' DDL requires appropriate database permissions.'
    exercise('DATABASE_SCHEMA_USER','Schema',schema)
    def user(d,v):
        name=d[1]+'LabReader'; s=d[1]
        variants=[
            (f'Create database user {name} WITHOUT LOGIN and show its authentication type.',f"SELECT name, authentication_type_desc FROM sys.database_principals WHERE name=N'{name}';",'Authentication type is NONE; this user cannot log in independently.'),
            (f'Grant {name} SELECT on schema {s} and inspect the explicit permission.',f'GRANT SELECT ON SCHEMA::[{s}] TO [{name}];', 'An explicit schema-level SELECT grant appears.'),
            (f'Grant then revoke SELECT on schema {s} for {name}. Explain why REVOKE is not DENY.',f'GRANT SELECT ON SCHEMA::[{s}] TO [{name}];\nREVOKE SELECT ON SCHEMA::[{s}] FROM [{name}];','No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only.'),
            (f'Set {name}\'s default schema to {s}; inspect it.',f"ALTER USER [{name}] WITH DEFAULT_SCHEMA=[{s}];\nSELECT name, default_schema_name FROM sys.database_principals WHERE name=N'{name}';",f'Default schema={s}; default schema does not grant permissions.'),
            (f'Create role {name}Role, grant it schema SELECT, add {name} to the role and inspect membership.',f"CREATE ROLE [{name}Role];\nGRANT SELECT ON SCHEMA::[{s}] TO [{name}Role];\nALTER ROLE [{name}Role] ADD MEMBER [{name}];\nSELECT USER_NAME(role_principal_id) AS RoleName, USER_NAME(member_principal_id) AS MemberName FROM sys.database_role_members WHERE member_principal_id=USER_ID(N'{name}');",'Membership shows the new reader role and user.')]
        a,b,c=variants[v]
        sql=f"IF DATABASE_PRINCIPAL_ID(N'{name}') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'{name}Role') IS NOT NULL THROW 51000, 'Use unused principal names', 1;\nBEGIN TRANSACTION;\nBEGIN TRY\nCREATE USER [{name}] WITHOUT LOGIN;\n{b}\nSELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'{name}');\nROLLBACK TRANSACTION;\nEND TRY\nBEGIN CATCH\n IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;\n THROW;\nEND CATCH;"
        return f'{d[0]}: {a} Use a fresh session with instructor-authorized principal-management permissions.',sql,c+' Database users and server logins are distinct. These labs need no password or server configuration change.'
    exercise('DATABASE_SCHEMA_USER','User',user)

def introduction():
    concepts={
        'Relational database fundamentals':('duplicate master details in every transaction','separate the master entity and transaction entity and reference a stable master key','primary key, foreign key and one-to-many relationship','a master name change is made once and all related facts still reference the same key'),
        'Structured Data Storage and Control':('negative quantities and untyped date strings entering the system','use typed columns plus NOT NULL, CHECK and key constraints','schema validation and a rejected invalid insert','a negative quantity is rejected while zero is accepted if the business rule permits it'),
        'Advanced Querying and Data Operations':('operators editing all records because a WHERE predicate is missing','preview the intended rows, apply a specific predicate and inspect affected rows inside a transaction','SELECT, INSERT, UPDATE and DELETE responsibilities','only the target rows change and a rollback restores the original values'),
        'Security and Regulatory Support':('reporting users receiving modification rights','grant a reporting role only required SELECT access; review grants, auditing and sensitive-data handling','least privilege, roles, auditing and a separate compliance review','the reader can query authorized objects and cannot modify them; this alone does not establish regulatory compliance'),
        'Performance and Scalability':('a growing report scanning far more rows than it returns','inspect the actual plan and measured I/O before evaluating an index on selective filter/join columns','actual execution plan, logical reads, representative workload and write cost','compare elapsed time and logical reads before and after, with identical results and acceptable write overhead'),
        'Analytics and Business Intelligence':('a dashboard double-counting master records after joining to details','define the metric grain, aggregate detail at the required grain and reconcile totals','grain, dimensions, measures and aggregate reconciliation','the dashboard total equals an independent detail-level control total'),
        'Transactional Workloads':('a multi-step business operation succeeding only halfway','enclose the related writes in one transaction with rollback on failure','atomicity, consistency, isolation and durability','an injected failure leaves neither a partial debit/charge nor its unmatched counterpart'),
        'Data Warehousing and BI':('daily reporting conflicting with live operational processing','define a separate reporting model and load schedule, recording source cutoffs and reconciliation totals','fact grain, dimensions, refresh latency and reconciliation','a repeated load does not duplicate facts and a published report states its data cutoff'),
        'Digital Content Management':('unversioned document metadata overwriting earlier editorial changes','store content metadata with a stable key and version/concurrency token; define where large content bytes live','metadata schema, content location and concurrency check','an update using a stale version is rejected rather than overwriting a newer edit'),
        'Enterprise Applications':('separate application modules maintaining inconsistent master IDs','share governed master keys, enforce references and define module-specific schema permissions','master-data ownership, foreign keys and application role boundaries','both modules resolve the same master ID and an unknown reference is rejected'),
    }
    for sub,(problem,control,terms,accept) in concepts.items():
        def make(d,v,problem=problem,control=control,terms=terms,accept=accept,sub=sub):
            subject=f'{d[2]} and {d[3]}'
            prompts=[
                f'For {subject}, explain how {sub.lower()} addresses {problem}. Name two relevant database concepts.',
                f'Design a small {subject} example illustrating this failure: {problem}. Propose a database-level response and explain one limitation.',
                f'Review this proposal for {subject}: "Let the application handle everything; no database design or validation is needed." Evaluate it specifically for {sub.lower()}.',
                f'Write an acceptance-test plan for {subject} that would detect {problem}. Include setup, action and an observable pass condition.',
                f'Write a short design-review note for {subject}: explain {problem}, recommend a control, define a success measure and identify one follow-up question for the owner.'
            ]
            answers=[
                f'A strong answer uses {subject} as its example, explains the risk of {problem}, and proposes: {control}. Relevant concepts: {terms}.',
                f'Construct a concrete pair of related {subject} records and a failure case. Response: {control}. State the rule being enforced and what still requires application/operational validation. Discuss {terms}.',
                f'Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, {control}. Discuss {terms}; do not claim a feature alone solves all operational concerns.',
                f'Setup: create a small valid {subject} baseline. Action: deliberately reproduce {problem} in a disposable environment, then apply the proposed control. Pass condition: {accept}. Preserve before/after evidence.',
                f'Risk: {problem}. Recommendation: {control}. Success measure: {accept}. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include {terms} in the review.'
            ]
            return f'{d[0]}: '+prompts[v], '', 'Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.',answers[v]
        exercise('INTRODUCTION',sub,make)


SOURCE_NAMES = {
    'INTRODUCTION':'introduction','DATABASE_SCHEMA_USER':'db-sch-user','DATATYPES':'datatypes',
    'DDL':'ddl','CONSTRAINTS':'ddl-constraints','DML':'dml','DATA_SETUP':'dql-data-setup',
    'DQL':'dql','OPERATORS':'dql-basic-operators','SET_OPERATIONS':'dql-set-operations',
    'JOINS':'dql-joins','STRING_FUNCTIONS':'dql-string-functions','DATE_FUNCTIONS':'dql-date-functions',
    'AGGREGATES':'dql-aggregate-functions','ANALYTICAL_FUNCTIONS':'dql-analytical-functions','CTE':'dql-cte'
}

def render():
    coverage=['# Coverage and assignment index','',
              f'The source hierarchy is mapped to teachable leaves. Each subtopic has {len(DOMAINS)*5} assignments across {len(DOMAINS)} connected domain projects. IDs are reference labels, not dates. The original IDs 01–25 are preserved; additional domains use IDs 26–45. Start with a domain brief, build its related tables and progress by demonstrated competency.',
              '', '| Topic | Subtopic | Count | Assignment range |', '|---|---|---:|---|']
    for topic,subs in BOOKS.items():
        source=f'https://github.com/tinitiateprime/sqlserver/blob/main/sqlserver-sql/sqlserver-{SOURCE_NAMES[topic]}.md'
        q=[f'# {topic.replace("_"," ")} — Student assignments','',f'Syllabus reference: [Tinitiate topic]({source}).','',
           'Choose [a domain](../README.md), such as Retail, and read its table guide. Create the tables in the order shown, then add the sample rows. If you only want to practice queries, ask your instructor to run [the setup script](../setup/01_create_and_seed.sql). Use SQL Server 2017 or later.','',
           'New to SQL? Read [the beginner guide](../BEGINNER_GUIDE.md). It explains table names, sample data, NULL and constraints.','',
           'Work through the exercises for your chosen domain. There is no daily schedule. Submit your SQL and the results it shows. When a question asks you to explain something, use your own words.','',
           'Keep the tables and initial sample rows for later exercises. Start each change exercise with the original sample data in a practice database. Ask your instructor to reset the practice tables between exercises; changes are kept when you run them.','']
        if topic=='DDL':
            q=['# DDL — Student assignments', '',
               'Choose one domain, such as Retail. Start with its five Create steps in order. Write the SQL for each question.', '',
               'Use an empty practice database in SQL Server 2017 or later. NOT NULL means a value is required; NULL means the value may be missing.', '',
               'For Alter and Drop, use a separate practice copy. Ask your instructor to reset it before each exercise. Changes are kept when you run them.', '',
               'After creating the tables, use the [domain guide](../README.md) to add sample rows before starting Alter and Drop.', '']
        a=[f'# {topic.replace("_"," ")} — Instructor solutions','',
           'Match answers by assignment ID. Run one block at a time in a fresh session or batch; do not concatenate blocks that redeclare variables. These are reference answers, not the only valid implementations.','',
           'Validate full values, column meanings, NULL behavior and duplicate multiplicity; compare order only where the task specifies it. Conceptual answers include a grading rubric. The fixture must match setup before query grading.','']
        for d in DOMAINS:
            for sub,rows in subs.items():
                q += [f'## {d[0]} — {sub}','']
                a += [f'## {d[0]} — {sub}','']
                for r in [r for r in rows if r['domain']==d[0]]:
                    q += [f'### {r["id"]} | {r["domain"]}','',r['prompt'],'']
                    a += [f'### {r["id"]} | {r["domain"]}','']
                    if r['sql']: a += ['```sql',r['sql'],'```','']
                    if r['answer']: a += [r['answer'],'']
                    a += ['**Validation:** '+r['check'],'']
        for sub,rows in subs.items():
            coverage += [f'| [{topic}](questions/{topic}.md) | {sub} | {len(rows)} | {rows[0]["id"]} – {rows[-1]["id"]} |']
        (ROOT/'questions'/f'{topic}.md').write_text('\n'.join(q),encoding='utf-8')
        (ROOT/'solutions'/f'{topic}_SOLUTIONS.md').write_text('\n'.join(a),encoding='utf-8')
    coverage += ['', '## Source mapping notes','',
                 '- All 16 linked Markdown topics in the source README are represented.',
                 '- Introduction: the definition, five named features and four named use cases are covered; the conclusion is a recap, not a separate learning objective.',
                 '- Datatypes: the five family headings map to all 26 named data types. Numeric: INT through FLOAT plus MONEY/SMALLMONEY/BIT; date/time: six types; strings: CHAR/VARCHAR/TEXT; binary: BINARY/VARBINARY; additional types: XML, GUID, spatial, hierarchy, rowversion and cursor.',
                 f'- DateTime and TimeZone → Date, Timezones, UTC, and Offsets → Date and Time / Timezones / UTC / Offsets / Applying an Offset: each leaf has {len(DOMAINS)*5} assignments, as do both casting/conversion leaves.',
                 '- UNION ALL is included because it appears in the linked set-operations lesson, even though omitted from the README contents list.',
                 f'- Each industry uses connected tables (five per domain; six for E-commerce and nine for Retail Supply Chain) with enforced PK/FK relationships. DDL Create and Data Setup work cumulatively on those tables. {len(DOMAINS)*6} additional domain reports and {len(DOMAINS)} capstone checklists connect the topic drills into projects.',
                 '', f'**Total: {len(BOOKS)} topics, {sum(len(x) for x in BOOKS.values())} subtopics, {len(RECORDS):,} assignments and matching answers.**','']
    (ROOT/'COVERAGE.md').write_text('\n'.join(coverage),encoding='utf-8')
    (ROOT/'curriculum.json').write_text(json.dumps(RECORDS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    for folder in ['questions','solutions','setup']:
        (ROOT/folder).mkdir(exist_ok=True)
    introduction(); administration(); data_types()
    projects.relational_lessons(add,DOMAINS); projects.constraint_lessons(add,DOMAINS)
    core_queries(); aggregates_and_sets(); joins(); string_functions(); dates(); analytics(); ctes()
    projects.remap_library(RECORDS)
    for row in RECORDS:
        row['prompt']=projects.student_english(row['prompt'])
    projects.create_setup(); render(); projects.write_projects(RECORDS)
    from large_data_setup import generate
    generate(projects.MODELS)
    from domain_interview_generate import generate as generate_domain_interviews
    generate_domain_interviews(projects.MODELS,RECORDS)
    assert len(BOOKS)==16
    assert len({r['id'] for r in RECORDS})==len(RECORDS)
    for subs in BOOKS.values():
        for rows in subs.values():
            assert len(rows)==5*len(DOMAINS)
            assert Counter(r['domain'] for r in rows)=={d[0]:5 for d in DOMAINS}
            assert all(r['sql'] or r['answer'] for r in rows)
    print(f'Generated {len(RECORDS)} assignments across {sum(map(len,BOOKS.values()))} subtopics in {len(BOOKS)} topic books.')

if __name__=='__main__':
    main()
