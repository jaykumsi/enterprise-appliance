# Pharma: SUBSTRING practice solutions

[Instructor index](README.md) · [Student practice](../questions/SUBSTRING_PRACTICE.md)

Ask students to count positions and predict the result first. Literal examples are independent of the dataset. Table examples use the small fixture for the stated sample results.

### PHARMA-SUB-01: First characters

Extract the first four characters of ABCDEFGH.

```sql
SELECT SUBSTRING(N'ABCDEFGH', 1, 4) AS Result;
```

**Explanation:** Start 1 and count 4 includes positions 1 through 4.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "ABCD"
  ]
]
```

### PHARMA-SUB-02: Middle characters

Extract three characters of ABCDEFGH starting at position 3.

```sql
SELECT SUBSTRING(N'ABCDEFGH', 3, 3) AS Result;
```

**Explanation:** Positions 3, 4 and 5 contain C, D and E.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "CDE"
  ]
]
```

### PHARMA-SUB-03: Start and end positions

Extract positions 4 through 7 of ABCDEFGH. Calculate the length first.

```sql
SELECT SUBSTRING(N'ABCDEFGH', 4, 7 - 4 + 1) AS Result;
```

**Explanation:** Length is 7 - 4 + 1 = 4. It is not 7.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "DEFG"
  ]
]
```

### PHARMA-SUB-04: One character

Return only the hyphen from ALPHA-ONE using numeric start and length.

```sql
SELECT SUBSTRING(N'ALPHA-ONE', 6, 1) AS Result;
```

**Explanation:** The hyphen is the sixth character; length 1 selects it alone.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "-"
  ]
]
```

### PHARMA-SUB-05: Long requested length

Predict and return SUBSTRING of ABCDE starting at 4 with length 20. Does it add spaces?

```sql
SELECT SUBSTRING(N'ABCDE', 4, 20) AS Result;
```

**Explanation:** Only D and E remain. The function does not pad the result.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "DE"
  ]
]
```

### PHARMA-SUB-06: Beyond the end and zero length

Return two results from ABCDE: start 8 with length 2, and start 2 with length 0. Explain each.

```sql
SELECT SUBSTRING(N'ABCDE', 8, 2) AS BeyondEnd, SUBSTRING(N'ABCDE', 2, 0) AS ZeroLength;
```

**Explanation:** Both return empty text. One begins beyond the string; the other requests no characters. Neither result is NULL.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "",
    ""
  ]
]
```

### PHARMA-SUB-07: Spaces change positions

For the text with two leading and two trailing spaces, "  ALPHA-ONE  ", return the first five raw characters and the first five characters after TRIM.

```sql
SELECT SUBSTRING(N'  ALPHA-ONE  ', 1, 5) AS RawResult,
       SUBSTRING(TRIM(N'  ALPHA-ONE  '), 1, 5) AS TrimmedResult;
```

**Explanation:** The first two raw positions are spaces, leaving room for only ALP. After trimming, A is position 1.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "  ALP",
    "ALPHA"
  ]
]
```

### PHARMA-SUB-08: Extract a code segment

From RX-2024-015, extract the four-digit year and the three-digit final code using fixed positions. Keep the leading zero in 015.

```sql
SELECT SUBSTRING(N'RX-2024-015', 4, 4) AS YearText,
       SUBSTRING(N'RX-2024-015', 9, 3) AS CodeText;
```

**Explanation:** The year occupies positions 4–7 and the final code 9–11. Keep the result as text to retain the leading zero.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    "2024",
    "015"
  ]
]
```

### PHARMA-SUB-09: NULL input

Apply SUBSTRING with start 1 and length 3 to a NULL nvarchar value. Return the raw result and another result with the fallback text Missing.

```sql
SELECT SUBSTRING(CAST(NULL AS nvarchar(20)), 1, 3) AS RawResult,
       COALESCE(SUBSTRING(CAST(NULL AS nvarchar(20)), 1, 3), N'Missing') AS DisplayResult;
```

**Explanation:** SUBSTRING of NULL returns NULL. COALESCE supplies the requested display value without changing the original data.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    null,
    "Missing"
  ]
]
```

### PHARMA-SUB-10: Safe delimiter extraction

For ALPHA-ONE, SOLO and -START, return the prefix before the first hyphen and the suffix after it. If there is no hyphen, return the entire text as the prefix and NULL as the suffix. Keep an empty prefix for -START.

```sql
;WITH Samples AS (
    SELECT 1 AS SampleID, N'ALPHA-ONE' AS TextValue
    UNION ALL SELECT 2, N'SOLO'
    UNION ALL SELECT 3, N'-START'
), Positions AS (
    SELECT *, CHARINDEX(N'-', TextValue) AS HyphenPosition FROM Samples
)
SELECT SampleID,
       SUBSTRING(TextValue, 1, CASE WHEN HyphenPosition > 0 THEN HyphenPosition - 1 ELSE 100 END) AS Prefix,
       CASE WHEN HyphenPosition > 0 THEN SUBSTRING(TextValue, HyphenPosition + 1, 100) END AS Suffix
FROM Positions ORDER BY SampleID;
```

**Explanation:** Find the delimiter first. Prefix length is position - 1; suffix starts at position + 1. The CASE inside the length argument prevents a negative length when there is no hyphen.

**Expected rows** (JSON: `null` means SQL NULL; `""` means empty text; spaces inside strings are significant):

```json
[
  [
    1,
    "ALPHA",
    "ONE"
  ],
  [
    2,
    "SOLO",
    null
  ],
  [
    3,
    "",
    "START"
  ]
]
```

### PHARMA-SUB-11: Apply to the domain table

From `[pharma].[Batches]`, return `BatchID`, the raw `BatchCode`, and the first three characters after trimming `BatchCode`. Order by `BatchID`. Do not update the stored data.

```sql
SELECT BatchID, BatchCode, SUBSTRING(TRIM(BatchCode), 1, 3) AS Prefix
FROM [pharma].[Batches] ORDER BY BatchID;
```

**Explanation:** TRIM produces an expression for this SELECT; it does not change the table. With the small fixture, IDs 1–3 yield Alp, bet and Gam.

### PHARMA-SUB-12: Split the domain reference safely

From `[pharma].[Batches]`, trim `BatchCode`, find its first hyphen, and return `BatchID`, ReferencePrefix and ReferenceSuffix. Use the full trimmed reference as prefix and NULL suffix if a hyphen is missing. Order by `BatchID`.

```sql
;WITH Cleaned AS (
    SELECT BatchID, TRIM(BatchCode) AS CleanReference FROM [pharma].[Batches]
), Positions AS (
    SELECT *, CHARINDEX(N'-', CleanReference) AS HyphenPosition FROM Cleaned
)
SELECT BatchID,
       SUBSTRING(CleanReference, 1,
           CASE WHEN HyphenPosition > 0 THEN HyphenPosition - 1 ELSE 80 END) AS ReferencePrefix,
       CASE WHEN HyphenPosition > 0
            THEN SUBSTRING(CleanReference, HyphenPosition + 1, 80) END AS ReferenceSuffix
FROM Positions ORDER BY BatchID;
```

**Explanation:** The declared maximum length of BatchCode is 80 characters. The CTEs expose intermediate steps so students can inspect them. Small-fixture IDs 1–3 return Alpha/One, beta/Two and Gamma/Three.
