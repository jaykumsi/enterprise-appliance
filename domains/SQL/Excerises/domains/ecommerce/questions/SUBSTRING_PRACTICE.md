# E-commerce: extra SUBSTRING practice

[Question index](README.md)

## Read this first

`SUBSTRING(text, start, length)` takes characters from text.

- `start` is the first position to include. SQL Server starts counting at **1**.
- `length` is how many characters to take, not the ending position.
- For positive start positions, ending position = start + length - 1.
- Spaces count as characters. Trim only when the question asks you to.

```text
Text:      A L P H A - O N E
Position:  1 2 3 4 5 6 7 8 9
```

### Worked example 1: take three characters

```sql
SELECT SUBSTRING(N'ALPHA-ONE', 2, 3) AS Result;
```

Result: `LPH`. Start at position 2; take positions 2, 3 and 4. The third argument is a count of 3.

### Worked example 2: extract positions 3 through 5

Length = 5 - 3 + 1 = 3.

```sql
SELECT SUBSTRING(N'ALPHA-ONE', 3, 3) AS Result;
```

Result: `PHA`. Using 5 as the length would take positions 3 through 7 instead.

### Worked example 3: extract after a hyphen

```sql
SELECT SUBSTRING(N'ALPHA-ONE', CHARINDEX(N'-', N'ALPHA-ONE') + 1, 100) AS Result;
```

CHARINDEX returns 6. Start at 6 + 1 = 7 to skip the hyphen. Result: `ONE`.
The length 100 is deliberately larger than the remaining text: SQL Server returns the available characters without padding.
For a real column, choose a length that covers its declared maximum. Check for a missing hyphen before subtracting 1 to extract a prefix.

### Common mistakes to discuss

| Mistake | How to explain it |
|---|---|
| Starting at 0 | Count from 1 for these exercises. Start 0 has special behavior; it is not the first character position. |
| Passing the ending position as length | Calculate end - start + 1. |
| Forgetting leading spaces | Display the raw value inside brackets and count the spaces. |
| Assuming a long length adds spaces | It returns only the available text. |
| Subtracting 1 when CHARINDEX returns 0 | A negative length raises an error; handle a missing delimiter first. |
| Treating NULL as empty text | NULL is unknown. Empty text has a known length of zero. |

For each exercise, write down the start, length and predicted result before running SQL.


## Practice exercises

### ECOMMERCE-SUB-01: First characters

Extract the first four characters of ABCDEFGH.

### ECOMMERCE-SUB-02: Middle characters

Extract three characters of ABCDEFGH starting at position 3.

### ECOMMERCE-SUB-03: Start and end positions

Extract positions 4 through 7 of ABCDEFGH. Calculate the length first.

### ECOMMERCE-SUB-04: One character

Return only the hyphen from ALPHA-ONE using numeric start and length.

### ECOMMERCE-SUB-05: Long requested length

Predict and return SUBSTRING of ABCDE starting at 4 with length 20. Does it add spaces?

### ECOMMERCE-SUB-06: Beyond the end and zero length

Return two results from ABCDE: start 8 with length 2, and start 2 with length 0. Explain each.

### ECOMMERCE-SUB-07: Spaces change positions

For the text with two leading and two trailing spaces, "  ALPHA-ONE  ", return the first five raw characters and the first five characters after TRIM.

### ECOMMERCE-SUB-08: Extract a code segment

From RX-2024-015, extract the four-digit year and the three-digit final code using fixed positions. Keep the leading zero in 015.

### ECOMMERCE-SUB-09: NULL input

Apply SUBSTRING with start 1 and length 3 to a NULL nvarchar value. Return the raw result and another result with the fallback text Missing.

### ECOMMERCE-SUB-10: Safe delimiter extraction

For ALPHA-ONE, SOLO and -START, return the prefix before the first hyphen and the suffix after it. If there is no hyphen, return the entire text as the prefix and NULL as the suffix. Keep an empty prefix for -START.

### ECOMMERCE-SUB-11: Apply to the domain table

From `[ecommerce].[Orders]`, return `OrderID`, the raw `OrderReference`, and the first three characters after trimming `OrderReference`. Order by `OrderID`. Do not update the stored data.

### ECOMMERCE-SUB-12: Split the domain reference safely

From `[ecommerce].[Orders]`, trim `OrderReference`, find its first hyphen, and return `OrderID`, ReferencePrefix and ReferenceSuffix. Use the full trimmed reference as prefix and NULL suffix if a hyphen is missing. Order by `OrderID`.
