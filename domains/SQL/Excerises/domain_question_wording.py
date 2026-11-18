"""Resolve shared exercise terminology against each domain's actual schema."""
import re

QUERY_TOPICS = {
    'DQL', 'OPERATORS', 'AGGREGATES', 'SET_OPERATIONS', 'JOINS',
    'STRING_FUNCTIONS', 'DATE_FUNCTIONS', 'ANALYTICAL_FUNCTIONS', 'CTE',
}


def clarify_question(row, model):
    text = row['prompt']
    if row['topic'] not in QUERY_TOPICS:
        return text
    mp = model['map']
    fact, master, name = model['base']
    nouns = {
        'retail': ('order', 'customer'), 'banking': ('transaction', 'account'),
        'pharma': ('batch', 'supplier'), 'healthcare': ('encounter', 'patient'),
        'oil': ('shipment', 'site'), 'retail_supply_chain': ('stock movement', 'warehouse'),
        'retail_logistics': ('shipment', 'customer'),
        'ecommerce': ('order', 'customer'),
        'brokerage': ('trade order', 'brokerage account'),
    }
    event, owner = nouns[model['slug']]
    events = event + ('es' if event.endswith('batch') else 's')
    key, fk, category, status, amount, units, label, date, time = (
        mp[k] for k in ('RecordID', 'PartyID', 'Category', 'Status', 'Amount',
                       'Quantity', 'Label', 'EventDate', 'EventTime'))
    if row['topic'] == 'STRING_FUNCTIONS' and row['subtopic'] == 'Concatenation Operator (+)':
        sql = row['sql']
        if 'ISNULL(' in sql:
            instruction = (f'Join `{label}` and `Note` into one text value. Put a colon and a space (`: `) between them. '
                           'If `Note` is NULL, use the word `missing`.')
            example = "`SELECT N'Alpha-One' + N': ' + ISNULL(CAST(NULL AS nvarchar(100)), N'missing') AS Result;` → `Alpha-One: missing`. With Note = `confirmed`, the result would be `Alpha-One: confirmed`."
        elif "N' / '" in sql:
            instruction = f'Join `{label}` and `{category}` into one text value. Put ` / ` between them (a slash with a space on each side).'
            example = "`SELECT N'Alpha-One' + N' / ' + N'A' AS Result;` → `Alpha-One / A`."
        elif "N'ID-'" in sql:
            instruction = f'Put `ID-` before each `{key}`. Convert the number to text before joining it.'
            example = "`SELECT N'ID-' + CONVERT(nvarchar(12), 7) AS Result;` → `ID-7`."
        elif 'CONVERT(nvarchar(10)' in sql:
            instruction = f'Join `{date}` and `{label}` into one text value. Show the date as `yyyy-mm-dd` and put one space after it.'
            example = "`SELECT CONVERT(nvarchar(10), CAST('20240101' AS date), 23) + N' ' + N'Alpha-One' AS Result;` → `2024-01-01 Alpha-One`."
        else:
            instruction = f'Join `{category}` and `{status}` into one text value. Put a colon (`:`) between them, with no spaces.'
            example = "`SELECT N'A' + N':' + N'Open' AS Result;` → `A:Open`."
        return (f'{model["title"]}: {instruction}\n\n'
                f'**Worked example:** {example}\n\n'
                f'**Your turn:** Use the `+` operator with the columns in `[{model["slug"]}].[{fact}]`. '
                f'Show `{key}` and the joined text as `Result`. Sort by `{key}`. '
                'Keep any spaces already stored in the text columns. The example above uses sample text; your table results depend on its stored values.')
    replacements = {
        'party record count': f'{event} count per {fk}',
        'party and record IDs': f'{fk} and {key}',
        'party/record ID pair': f'{fk}/{key} pair',
        'party IDs': f'{fk} values', 'party ID': fk, 'PartyIDs': f'{fk} values',
        'party name': name, 'record IDs': f'{key} values', 'record ID': key,
        'category total': f'total {amount} per {category}',
        'status average': f'average {amount} per {status}',
        'event timestamp': time, 'event date': date,
        'event year': f'year of {date}', 'event month': f'month of {date}',
        'event hour': f'hour of {time}',
        'highest-valued': f'highest-{amount}', 'highest-amount': f'highest-{amount}',
        'positive-amount': f'positive-{amount}', 'known-amount': f'known-{amount}',
        'categories': f'{category} values', 'category': category,
        'statuses': f'{status} values', 'status': status,
        'amounts': f'{amount} values', 'amount': amount,
        'labels': f'{label} values', 'label': label, 'quantity': units,
        'party': owner, 'parties': owner + 's',
        'record': event, 'records': events, 'events': events,
        'note': mp['Note'], 'backup': mp['BackupNote'],
    }
    # Only prose changes: preserve SQL examples, string literals, and identifiers.
    pattern = r'\b(' + '|'.join(re.escape(k) for k in sorted(replacements, key=len, reverse=True)) + r')\b'
    parts = re.split(r'(`[^`]*`)', text)
    for i in range(0, len(parts), 2):
        part = re.sub(pattern, lambda m: replacements[m[0]], parts[i])
        part = re.sub(r'\bIDs\b', f'{key} values', part)
        part = re.sub(r'\bID\b(?!-)', key, part)
        # A second pass must not add another column qualifier.
        part = re.sub(r'\brunning total\b(?! of )', f'running total of {amount}', part)
        parts[i] = part
    text = ''.join(parts)
    replacements = {
        f'{fk} (including the NULL group)': f'{fk} (which is NOT NULL)',
        f'(NULL {fk} values form one partition)': f'({fk} is NOT NULL)',
        f'excluding NULL {fk} values': f'using {fk} (which is NOT NULL)',
        f'exclude NULL {fk} values;': f'{fk} is NOT NULL;',
        f'fact {fk} values': f'{fact}.{fk} values',
        f'{fk}, name and count': f'{fk}, {name} and count',
        f'{fk} values and names': f'{fk} and {name}',
        f'within {owner}': f'within each {fk} partition',
        'and dates': f'and {date} values',
        'increasing date': f'increasing {date}', 'newest date': f'newest {date}',
        'latest date': f'latest {date}', 'by date then': f'by {date} then',
        'chronological date': f'chronological {date}',
        'next date': f'next {date}', 'previous date': f'previous {date}',
        'Use a INNER JOIN': 'Use an INNER JOIN',
    }
    for before, after in replacements.items():
        text = text.replace(before, after)
    text = text.replace(
        f'Return distinct {category}/{status} combinations, ordered by both columns.',
        f'Return distinct combinations of `{category}` and `{status}`, ordered by `{category}`, then `{status}`.')
    if row['topic'] == 'JOINS':
        qf, qm = f'[{model["slug"]}].[{fact}]', f'[{model["slug"]}].[{master}]'
        if 'RIGHT JOIN' in text:
            text = text.replace(f'Join `{qm}` p and `{qf}` f on {fk}.',
                                f'Place `{qf}` f on the left and `{qm}` p on the right; join on `f.{fk} = p.{fk}`.')
        if 'FULL JOIN' not in row['subtopic'].upper():
            text = re.sub(r' For FULL JOIN, include the NULL .*? group\.', '', text)
        if 'INNER JOIN' in text and 'unmatched side' in text and 'Explain why' not in text:
            text += ' Explain why an INNER JOIN returns no unmatched rows.'
    if row['topic'] in {'STRING_FUNCTIONS', 'DATE_FUNCTIONS', 'ANALYTICAL_FUNCTIONS'}:
        # Name the source columns even when a drill describes only a substring,
        # date part, or window calculation. This does not disclose the expression.
        sql = re.sub(r"'(?:''|[^'])*'", '', row['sql'])
        columns = list(dict.fromkeys(mp.values()))
        inputs = [c for c in columns if c != key and re.search(r'\b' + re.escape(c) + r'\b', sql)]
        if inputs and 'Source columns:' not in text:
            text += ' Source columns: ' + ', '.join(f'`{c}`' for c in inputs) + '.'
    if row['topic'] == 'DQL':
        if 'by calendar year and month.' in text:
            text = text.replace('by calendar year and month.', f'by calendar year and month of `{date}`.')
        if 'January 2024' in text and date not in text:
            text += f' Filter `{date}`.'
        if 'earliest' in text and date not in text:
            text += f' Use `{date}` to determine chronological order.'
    if row['topic'] == 'STRING_FUNCTIONS' and any(x in text for x in ('presence flag', 'with -1 fallback', 'with unassigned fallback')):
        if 'no fallback is used' not in text:
            text += f' `{fk}` is NOT NULL in `{fact}`, so every row has a value and no fallback is used.'
    return text
