# E-commerce: DATATYPES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DATATYPES.md)

## Teaching and troubleshooting

Check precision, scale, length and NULL behavior. Ask the student to predict the converted value before executing. Distinguish conversion failure, truncation and rounding.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DATATYPES-01-28 — INT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value int = 2147483647;
SELECT @Value AS Value;
```

**Check and explain:** INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

### DATATYPES-01-32 — INT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value int NULL);
INSERT #Work VALUES (1,2147483647),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

### DATATYPES-01-36 — INT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value int = 2147483647;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

### DATATYPES-01-40 — INT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value int NULL);
INSERT #Work VALUES (2147483647),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

### DATATYPES-01-44 — INT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(2147483647 AS int) AS TypedValue;
```

**Check and explain:** INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

### DATATYPES-02-28 — BIGINT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value bigint = CAST(2147483648 AS bigint);
SELECT @Value AS Value;
```

**Check and explain:** BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

### DATATYPES-02-32 — BIGINT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value bigint NULL);
INSERT #Work VALUES (1,CAST(2147483648 AS bigint)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

### DATATYPES-02-36 — BIGINT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value bigint = CAST(2147483648 AS bigint);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

### DATATYPES-02-40 — BIGINT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value bigint NULL);
INSERT #Work VALUES (CAST(2147483648 AS bigint)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

### DATATYPES-02-44 — BIGINT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CAST(2147483648 AS bigint) AS bigint) AS TypedValue;
```

**Check and explain:** BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

### DATATYPES-03-28 — DECIMAL

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value decimal(5,2) = 999.99;
SELECT @Value AS Value;
```

**Check and explain:** DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

### DATATYPES-03-32 — DECIMAL

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value decimal(5,2) NULL);
INSERT #Work VALUES (1,999.99),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

### DATATYPES-03-36 — DECIMAL

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value decimal(5,2) = 999.99;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

### DATATYPES-03-40 — DECIMAL

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value decimal(5,2) NULL);
INSERT #Work VALUES (999.99),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

### DATATYPES-03-44 — DECIMAL

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(999.99 AS decimal(5,2)) AS TypedValue;
```

**Check and explain:** DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

### DATATYPES-04-28 — NUMERIC

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value numeric(7,2) = 12345.67;
SELECT @Value AS Value;
```

**Check and explain:** NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

### DATATYPES-04-32 — NUMERIC

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value numeric(7,2) NULL);
INSERT #Work VALUES (1,12345.67),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

### DATATYPES-04-36 — NUMERIC

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value numeric(7,2) = 12345.67;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

### DATATYPES-04-40 — NUMERIC

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value numeric(7,2) NULL);
INSERT #Work VALUES (12345.67),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

### DATATYPES-04-44 — NUMERIC

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(12345.67 AS numeric(7,2)) AS TypedValue;
```

**Check and explain:** NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

### DATATYPES-05-28 — FLOAT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value float = 0.1;
SELECT @Value AS Value;
```

**Check and explain:** FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

### DATATYPES-05-32 — FLOAT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value float NULL);
INSERT #Work VALUES (1,0.1),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

### DATATYPES-05-36 — FLOAT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value float = 0.1;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

### DATATYPES-05-40 — FLOAT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value float NULL);
INSERT #Work VALUES (0.1),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

### DATATYPES-05-44 — FLOAT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(0.1 AS float) AS TypedValue;
```

**Check and explain:** FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

### DATATYPES-06-28 — DATE

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value date = CONVERT(date,'20240229',112);
SELECT @Value AS Value;
```

**Check and explain:** DATE has no time or offset. It stores a date value, not a display format.

### DATATYPES-06-32 — DATE

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value date NULL);
INSERT #Work VALUES (1,CONVERT(date,'20240229',112)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

### DATATYPES-06-36 — DATE

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value date = CONVERT(date,'20240229',112);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

### DATATYPES-06-40 — DATE

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value date NULL);
INSERT #Work VALUES (CONVERT(date,'20240229',112)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

### DATATYPES-06-44 — DATE

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(date,'20240229',112) AS date) AS TypedValue;
```

**Check and explain:** DATE has no time or offset. It stores a date value, not a display format.

### DATATYPES-07-28 — DATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetime = CONVERT(datetime,'2024-04-15T13:30:45.123',126);
SELECT @Value AS Value;
```

**Check and explain:** DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

### DATATYPES-07-32 — DATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value datetime NULL);
INSERT #Work VALUES (1,CONVERT(datetime,'2024-04-15T13:30:45.123',126)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

### DATATYPES-07-36 — DATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetime = CONVERT(datetime,'2024-04-15T13:30:45.123',126);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

### DATATYPES-07-40 — DATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value datetime NULL);
INSERT #Work VALUES (CONVERT(datetime,'2024-04-15T13:30:45.123',126)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

### DATATYPES-07-44 — DATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(datetime,'2024-04-15T13:30:45.123',126) AS datetime) AS TypedValue;
```

**Check and explain:** DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

### DATATYPES-08-28 — SMALLDATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value smalldatetime = CONVERT(smalldatetime,'2024-04-15T13:30:45',126);
SELECT @Value AS Value;
```

**Check and explain:** SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

### DATATYPES-08-32 — SMALLDATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value smalldatetime NULL);
INSERT #Work VALUES (1,CONVERT(smalldatetime,'2024-04-15T13:30:45',126)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

### DATATYPES-08-36 — SMALLDATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value smalldatetime = CONVERT(smalldatetime,'2024-04-15T13:30:45',126);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

### DATATYPES-08-40 — SMALLDATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value smalldatetime NULL);
INSERT #Work VALUES (CONVERT(smalldatetime,'2024-04-15T13:30:45',126)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

### DATATYPES-08-44 — SMALLDATETIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(smalldatetime,'2024-04-15T13:30:45',126) AS smalldatetime) AS TypedValue;
```

**Check and explain:** SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

### DATATYPES-09-28 — DATETIMEOFFSET

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetimeoffset(3) = CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127);
SELECT @Value AS Value;
```

**Check and explain:** DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

### DATATYPES-09-32 — DATETIMEOFFSET

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value datetimeoffset(3) NULL);
INSERT #Work VALUES (1,CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

### DATATYPES-09-36 — DATETIMEOFFSET

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetimeoffset(3) = CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

### DATATYPES-09-40 — DATETIMEOFFSET

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value datetimeoffset(3) NULL);
INSERT #Work VALUES (CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

### DATATYPES-09-44 — DATETIMEOFFSET

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(datetimeoffset(3),'2024-04-15T13:30:45.123+05:30',127) AS datetimeoffset(3)) AS TypedValue;
```

**Check and explain:** DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

### DATATYPES-10-28 — TIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value time(3) = CONVERT(time(3),'13:30:45.123');
SELECT @Value AS Value;
```

**Check and explain:** TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

### DATATYPES-10-32 — TIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value time(3) NULL);
INSERT #Work VALUES (1,CONVERT(time(3),'13:30:45.123')),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

### DATATYPES-10-36 — TIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value time(3) = CONVERT(time(3),'13:30:45.123');
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

### DATATYPES-10-40 — TIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value time(3) NULL);
INSERT #Work VALUES (CONVERT(time(3),'13:30:45.123')),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

### DATATYPES-10-44 — TIME

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(time(3),'13:30:45.123') AS time(3)) AS TypedValue;
```

**Check and explain:** TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

### DATATYPES-11-28 — DATETIME2

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetime2(3) = CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126);
SELECT @Value AS Value;
```

**Check and explain:** DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

### DATATYPES-11-32 — DATETIME2

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value datetime2(3) NULL);
INSERT #Work VALUES (1,CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126)),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

### DATATYPES-11-36 — DATETIME2

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value datetime2(3) = CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126);
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

### DATATYPES-11-40 — DATETIME2

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value datetime2(3) NULL);
INSERT #Work VALUES (CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126)),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

### DATATYPES-11-44 — DATETIME2

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(datetime2(3),'2024-04-15T13:30:45.123',126) AS datetime2(3)) AS TypedValue;
```

**Check and explain:** DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

### DATATYPES-12-28 — CHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value char(5) = 'US';
SELECT @Value AS Value;
```

**Check and explain:** CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

### DATATYPES-12-32 — CHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value char(5) NULL);
INSERT #Work VALUES (1,'US'),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

### DATATYPES-12-36 — CHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value char(5) = 'US';
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

### DATATYPES-12-40 — CHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value char(5) NULL);
INSERT #Work VALUES ('US'),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

### DATATYPES-12-44 — CHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST('US' AS char(5)) AS TypedValue;
```

**Check and explain:** CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

### DATATYPES-13-28 — VARCHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value varchar(20) = 'Batch-A';
SELECT @Value AS Value;
```

**Check and explain:** VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

### DATATYPES-13-32 — VARCHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value varchar(20) NULL);
INSERT #Work VALUES (1,'Batch-A'),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

### DATATYPES-13-36 — VARCHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value varchar(20) = 'Batch-A';
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

### DATATYPES-13-40 — VARCHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value varchar(20) NULL);
INSERT #Work VALUES ('Batch-A'),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

### DATATYPES-13-44 — VARCHAR(n)

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST('Batch-A' AS varchar(20)) AS TypedValue;
```

**Check and explain:** VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

### DATATYPES-14-28 — BINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value binary(4) = 0x0102;
SELECT @Value AS Value;
```

**Check and explain:** BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

### DATATYPES-14-32 — BINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value binary(4) NULL);
INSERT #Work VALUES (1,0x0102),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

### DATATYPES-14-36 — BINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value binary(4) = 0x0102;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

### DATATYPES-14-40 — BINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value binary(4) NULL);
INSERT #Work VALUES (0x0102),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

### DATATYPES-14-44 — BINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(0x0102 AS binary(4)) AS TypedValue;
```

**Check and explain:** BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

### DATATYPES-15-28 — VARBINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value varbinary(max) = 0x01020304;
SELECT @Value AS Value;
```

**Check and explain:** VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

### DATATYPES-15-32 — VARBINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value varbinary(max) NULL);
INSERT #Work VALUES (1,0x01020304),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

### DATATYPES-15-36 — VARBINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value varbinary(max) = 0x01020304;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

### DATATYPES-15-40 — VARBINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value varbinary(max) NULL);
INSERT #Work VALUES (0x01020304),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

### DATATYPES-15-44 — VARBINARY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(0x01020304 AS varbinary(max)) AS TypedValue;
```

**Check and explain:** VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

### DATATYPES-16-28 — UNIQUEIDENTIFIER

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value uniqueidentifier = CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc');
SELECT @Value AS Value;
```

**Check and explain:** UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

### DATATYPES-16-32 — UNIQUEIDENTIFIER

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value uniqueidentifier NULL);
INSERT #Work VALUES (1,CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc')),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

### DATATYPES-16-36 — UNIQUEIDENTIFIER

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value uniqueidentifier = CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc');
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

### DATATYPES-16-40 — UNIQUEIDENTIFIER

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value uniqueidentifier NULL);
INSERT #Work VALUES (CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc')),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

### DATATYPES-16-44 — UNIQUEIDENTIFIER

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(CONVERT(uniqueidentifier,'12345678-1234-1234-1234-123456789abc') AS uniqueidentifier) AS TypedValue;
```

**Check and explain:** UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

### DATATYPES-17-28 — BIT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value bit = 1;
SELECT @Value AS Value;
```

**Check and explain:** A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

### DATATYPES-17-32 — BIT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value bit NULL);
INSERT #Work VALUES (1,1),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

### DATATYPES-17-36 — BIT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value bit = 1;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

### DATATYPES-17-40 — BIT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value bit NULL);
INSERT #Work VALUES (1),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

### DATATYPES-17-44 — BIT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(1 AS bit) AS TypedValue;
```

**Check and explain:** A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

### DATATYPES-18-28 — MONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value money = 1234.5678;
SELECT @Value AS Value;
```

**Check and explain:** MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

### DATATYPES-18-32 — MONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value money NULL);
INSERT #Work VALUES (1,1234.5678),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

### DATATYPES-18-36 — MONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value money = 1234.5678;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

### DATATYPES-18-40 — MONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value money NULL);
INSERT #Work VALUES (1234.5678),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

### DATATYPES-18-44 — MONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(1234.5678 AS money) AS TypedValue;
```

**Check and explain:** MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

### DATATYPES-19-28 — SMALLMONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value smallmoney = 123.4567;
SELECT @Value AS Value;
```

**Check and explain:** SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

### DATATYPES-19-32 — SMALLMONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, Value smallmoney NULL);
INSERT #Work VALUES (1,123.4567),(2,NULL);
SELECT * FROM #Work ORDER BY ID;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

### DATATYPES-19-36 — SMALLMONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @Value smallmoney = 123.4567;
SELECT @Value AS Value, DATALENGTH(@Value) AS ValueBytes;
```

**Check and explain:** DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

### DATATYPES-19-40 — SMALLMONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(Value smallmoney NULL);
INSERT #Work VALUES (123.4567),(NULL);
SELECT COUNT(*) AS TotalRows, COUNT(Value) AS KnownRows FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

### DATATYPES-19-44 — SMALLMONEY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
SELECT CAST(123.4567 AS smallmoney) AS TypedValue;
```

**Check and explain:** SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

### DATATYPES-20-28 — TEXT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int, LegacyNote text NULL);
INSERT #Work VALUES (1,'legacy note');
SELECT ID, CAST(LegacyNote AS varchar(max)) AS Note FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** legacy note is returned as modern text.

### DATATYPES-20-32 — TEXT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int, LegacyNote text NULL);
INSERT #Work VALUES (1,'legacy note');
SELECT ID, DATALENGTH(LegacyNote) AS NoteBytes FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** The sample has 11 ASCII bytes.

### DATATYPES-20-36 — TEXT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int, LegacyNote text NULL);
INSERT #Work VALUES (1,'legacy note');
SELECT ID FROM #Work WHERE CAST(LegacyNote AS varchar(max)) LIKE '%note%';
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** ID 1 matches.

### DATATYPES-20-40 — TEXT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int, LegacyNote text NULL);
INSERT #Work VALUES (1,'legacy note');
ALTER TABLE #Work ALTER COLUMN LegacyNote varchar(max) NULL;
SELECT * FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Contents survive conversion; inspect the new type with sp_help.

### DATATYPES-20-44 — TEXT

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int, LegacyNote text NULL);
INSERT #Work VALUES (1,'legacy note');
SELECT ID, SUBSTRING(LegacyNote,1,6) AS Prefix FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

### DATATYPES-21-28 — XML

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @x xml = N'<record id="1"><amount>125.50</amount></record>';
SELECT @x AS Document;
```

**Check and explain:** One XML value.

### DATATYPES-21-32 — XML

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @x xml = N'<record id="1"><amount>125.50</amount></record>';
SELECT @x.value('(/record/@id)[1]','int') AS OrderID;
```

**Check and explain:** OrderID=1.

### DATATYPES-21-36 — XML

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @x xml = N'<record id="1"><amount>125.50</amount></record>';
SELECT @x.value('(/record/amount/text())[1]','decimal(12,2)') AS OrderTotal;
```

**Check and explain:** OrderTotal=125.50.

### DATATYPES-21-40 — XML

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @x xml = N'<record id="1"><amount>125.50</amount></record>';
SELECT @x.exist('/record/amount') AS HasAmount;
```

**Check and explain:** HasAmount=1.

### DATATYPES-21-44 — XML

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @x xml = N'<record id="1"><amount>125.50</amount></record>';
SELECT @x.query('/record') AS RecordXml;
```

**Check and explain:** A record element with its id and amount is returned.

### DATATYPES-22-28 — GEOGRAPHY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);
SELECT @g.STAsText() AS Wkt;
```

**Check and explain:** WKT uses longitude then latitude, while Point takes latitude then longitude.

### DATATYPES-22-32 — GEOGRAPHY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);
SELECT @g.Lat AS Latitude, @g.Long AS Longitude;
```

**Check and explain:** 41.8781 and -87.6298.

### DATATYPES-22-36 — GEOGRAPHY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);
SELECT @g.STSrid AS SRID;
```

**Check and explain:** 4326.

### DATATYPES-22-40 — GEOGRAPHY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);
SELECT @g.STDistance(@g) AS Distance;
```

**Check and explain:** 0 meters for this SRID.

### DATATYPES-22-44 — GEOGRAPHY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geography = geography::Point(41.8781,-87.6298,4326);
SELECT @g.STDistance(geography::Point(40.7128,-74.0060,4326)) AS DistanceMeters;
```

**Check and explain:** Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

### DATATYPES-23-28 — GEOMETRY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);
SELECT @g.STAsText() AS Wkt;
```

**Check and explain:** LINESTRING with endpoints (0 0) and (3 4).

### DATATYPES-23-32 — GEOMETRY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);
SELECT @g.STLength() AS Length;
```

**Check and explain:** Length=5 coordinate units.

### DATATYPES-23-36 — GEOMETRY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);
SELECT @g.STNumPoints() AS Points;
```

**Check and explain:** Points=2.

### DATATYPES-23-40 — GEOMETRY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);
SELECT @g.STGeometryType() AS ShapeType;
```

**Check and explain:** LineString.

### DATATYPES-23-44 — GEOMETRY

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @g geometry = geometry::STGeomFromText('LINESTRING(0 0,3 4)',0);
SELECT @g.STStartPoint().STX AS X, @g.STStartPoint().STY AS Y;
```

**Check and explain:** X=0, Y=0; geometry does not imply meters.

### DATATYPES-24-28 — HIERARCHYID

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');
SELECT @h.ToString() AS Path;
```

**Check and explain:** /1/2/.

### DATATYPES-24-32 — HIERARCHYID

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');
SELECT @h.GetLevel() AS Level;
```

**Check and explain:** 2.

### DATATYPES-24-36 — HIERARCHYID

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');
SELECT @h.GetAncestor(1).ToString() AS ParentPath;
```

**Check and explain:** /1/.

### DATATYPES-24-40 — HIERARCHYID

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');
SELECT @h.IsDescendantOf(hierarchyid::Parse('/1/')) AS IsChild;
```

**Check and explain:** 1.

### DATATYPES-24-44 — HIERARCHYID

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @h hierarchyid = hierarchyid::Parse('/1/2/');
SELECT @h.GetDescendant(NULL,NULL).ToString() AS ChildPath;
```

**Check and explain:** /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

### DATATYPES-25-28 — ROWVERSION

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, OrderTotal int, VersionToken rowversion);
INSERT #Work(ID,OrderTotal) VALUES (1,100);
SELECT ID,OrderTotal,VersionToken FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

### DATATYPES-25-32 — ROWVERSION

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, OrderTotal int, VersionToken rowversion);
INSERT #Work(ID,OrderTotal) VALUES (1,100);
DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);
UPDATE #Work SET OrderTotal=200 WHERE ID=1;
SELECT CASE WHEN VersionToken<>@old THEN 1 ELSE 0 END AS Changed FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Changed=1. ROWVERSION is not a date/time.

### DATATYPES-25-36 — ROWVERSION

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, OrderTotal int, VersionToken rowversion);
INSERT #Work(ID,OrderTotal) VALUES (1,100);
DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);
UPDATE #Work SET OrderTotal=OrderTotal WHERE ID=1;
SELECT CASE WHEN VersionToken<>@old THEN 1 ELSE 0 END AS Changed FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

### DATATYPES-25-40 — ROWVERSION

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, OrderTotal int, VersionToken rowversion);
INSERT #Work(ID,OrderTotal) VALUES (1,100);
DECLARE @expected binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);
UPDATE #Work SET OrderTotal=150 WHERE ID=1 AND VersionToken=@expected;
SELECT @@ROWCOUNT AS AffectedRows;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** AffectedRows=1. ROWVERSION is not a date/time.

### DATATYPES-25-44 — ROWVERSION

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DROP TABLE IF EXISTS #Work;
CREATE TABLE #Work(ID int PRIMARY KEY, OrderTotal int, VersionToken rowversion);
INSERT #Work(ID,OrderTotal) VALUES (1,100);
DECLARE @old binary(8)=(SELECT VersionToken FROM #Work WHERE ID=1);
UPDATE #Work SET OrderTotal=150 WHERE ID=1;
UPDATE #Work SET OrderTotal=200 WHERE ID=1 AND VersionToken=@old;
SELECT @@ROWCOUNT AS AffectedRows;
SELECT OrderTotal FROM #Work;
DROP TABLE IF EXISTS #Work;
```

**Check and explain:** Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

### DATATYPES-26-28 — CURSOR

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @c CURSOR;
DECLARE @id int, @count int=0;
SET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT OrderID FROM [ecommerce].[Orders] WHERE 1=1 ORDER BY OrderID;
OPEN @c;
FETCH NEXT FROM @c INTO @id;
WHILE @@FETCH_STATUS=0
BEGIN
 SELECT @id AS OrderID;
 SET @count+=1;
 FETCH NEXT FROM @c INTO @id;
END;
CLOSE @c;
DEALLOCATE @c;
SELECT @count AS VisitedRows;
SELECT COUNT(*) AS SetBasedCount FROM [ecommerce].[Orders] WHERE 1=1;
```

**Check and explain:** VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

### DATATYPES-26-32 — CURSOR

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @c CURSOR;
DECLARE @id int, @count int=0;
SET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT OrderID FROM [ecommerce].[Orders] WHERE OrderStatus='Open' ORDER BY OrderID;
OPEN @c;
FETCH NEXT FROM @c INTO @id;
WHILE @@FETCH_STATUS=0
BEGIN
 SELECT @id AS OrderID;
 SET @count+=1;
 FETCH NEXT FROM @c INTO @id;
END;
CLOSE @c;
DEALLOCATE @c;
SELECT @count AS VisitedRows;
SELECT COUNT(*) AS SetBasedCount FROM [ecommerce].[Orders] WHERE OrderStatus='Open';
```

**Check and explain:** VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

### DATATYPES-26-36 — CURSOR

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @c CURSOR;
DECLARE @id int, @count int=0;
SET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT OrderID FROM [ecommerce].[Orders] WHERE OrderTotal IS NULL ORDER BY OrderID;
OPEN @c;
FETCH NEXT FROM @c INTO @id;
WHILE @@FETCH_STATUS=0
BEGIN
 SELECT @id AS OrderID;
 SET @count+=1;
 FETCH NEXT FROM @c INTO @id;
END;
CLOSE @c;
DEALLOCATE @c;
SELECT @count AS VisitedRows;
SELECT COUNT(*) AS SetBasedCount FROM [ecommerce].[Orders] WHERE OrderTotal IS NULL;
```

**Check and explain:** VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

### DATATYPES-26-40 — CURSOR

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @c CURSOR;
DECLARE @id int, @count int=0;
SET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT OrderID FROM [ecommerce].[Orders] WHERE OrderTotal>=200 ORDER BY OrderID;
OPEN @c;
FETCH NEXT FROM @c INTO @id;
WHILE @@FETCH_STATUS=0
BEGIN
 SELECT @id AS OrderID;
 SET @count+=1;
 FETCH NEXT FROM @c INTO @id;
END;
CLOSE @c;
DEALLOCATE @c;
SELECT @count AS VisitedRows;
SELECT COUNT(*) AS SetBasedCount FROM [ecommerce].[Orders] WHERE OrderTotal>=200;
```

**Check and explain:** VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

### DATATYPES-26-44 — CURSOR

**Question**

[Canonical questions](../questions/DATATYPES.md)

**Reference answer**

```sql
DECLARE @c CURSOR;
DECLARE @id int, @count int=0;
SET @c = CURSOR LOCAL FAST_FORWARD FOR SELECT OrderID FROM [ecommerce].[Orders] WHERE CustomerID IS NULL ORDER BY OrderID;
OPEN @c;
FETCH NEXT FROM @c INTO @id;
WHILE @@FETCH_STATUS=0
BEGIN
 SELECT @id AS OrderID;
 SET @count+=1;
 FETCH NEXT FROM @c INTO @id;
END;
CLOSE @c;
DEALLOCATE @c;
SELECT @count AS VisitedRows;
SELECT COUNT(*) AS SetBasedCount FROM [ecommerce].[Orders] WHERE CustomerID IS NULL;
```

**Check and explain:** VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### INT: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-01-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-01-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: INT is a signed 32-bit integer; 2147483648 needs BIGINT or another suitable exact type.

**Core reference:** Find `DATATYPES-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### BIGINT: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-02-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-02-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: BIGINT is a signed 64-bit integer. It does not automatically generate IDs; IDENTITY is a separate property.

**Core reference:** Find `DATATYPES-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### DECIMAL: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-03-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-03-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DECIMAL(5,2) has five total digits and two fractional digits; its range is -999.99 through 999.99.

**Core reference:** Find `DATATYPES-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### NUMERIC: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-04-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-04-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-04-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-04-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-04-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: NUMERIC is synonymous with DECIMAL, with fixed precision and scale; it does not have a variable scale.

**Core reference:** Find `DATATYPES-04-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### FLOAT: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-05-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-05-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-05-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-05-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-05-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: FLOAT is approximate. Use an exact decimal type for currency or equality-sensitive calculations.

**Core reference:** Find `DATATYPES-05-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### DATE: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-06-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-06-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-06-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-06-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-06-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DATE has no time or offset. It stores a date value, not a display format.

**Core reference:** Find `DATATYPES-06-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### DATETIME: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-07-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-07-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-07-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-07-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-07-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DATETIME has limited fractional-second precision and no zone; DATETIME2 is preferable for new precise timestamps.

**Core reference:** Find `DATATYPES-07-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### SMALLDATETIME: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-08-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-08-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-08-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-08-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-08-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SMALLDATETIME rounds to minute precision; the sample rounds to 13:31:00.

**Core reference:** Find `DATATYPES-08-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### DATETIMEOFFSET: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-09-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-09-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-09-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-09-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-09-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DATETIMEOFFSET preserves an offset, not a named zone or its future daylight-saving rules.

**Core reference:** Find `DATATYPES-09-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### TIME: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-10-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-10-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-10-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-10-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-10-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: TIME contains neither a date nor an offset; it cannot uniquely identify an instant.

**Core reference:** Find `DATATYPES-10-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### DATETIME2: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-11-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-11-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-11-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-11-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-11-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DATETIME2 supports specified fractional-second precision but contains no time-zone metadata.

**Core reference:** Find `DATATYPES-11-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### CHAR(n): progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-12-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-12-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-12-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-12-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-12-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: CHAR pads to its declared length. DATALENGTH includes padding; LEN excludes trailing spaces.

**Core reference:** Find `DATATYPES-12-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### VARCHAR(n): progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-13-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-13-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-13-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-13-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-13-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: VARCHAR length is in bytes. Unicode behavior depends on collation; NVARCHAR is the explicit Unicode alternative.

**Core reference:** Find `DATATYPES-13-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### BINARY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-14-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-14-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-14-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-14-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-14-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: BINARY has fixed length and can pad shorter inputs. Inspect the resulting bytes before treating it as an external token.

**Core reference:** Find `DATATYPES-14-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### VARBINARY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-15-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-15-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-15-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-15-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-15-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: VARBINARY(MAX) stores variable-length bytes, not decoded image or document semantics.

**Core reference:** Find `DATATYPES-15-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### UNIQUEIDENTIFIER: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-16-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-16-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-16-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-16-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-16-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: UNIQUEIDENTIFIER is a 16-byte GUID value. A key constraint enforces uniqueness; the type alone does not.

**Core reference:** Find `DATATYPES-16-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### BIT: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-17-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-17-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-17-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-17-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-17-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: A nullable BIT can hold 0, 1 or NULL. NULL means unknown, not false.

**Core reference:** Find `DATATYPES-17-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### MONEY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-18-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-18-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-18-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-18-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-18-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: MONEY has four fractional digits. Prefer an explicitly chosen DECIMAL precision/scale for new financial calculations.

**Core reference:** Find `DATATYPES-18-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### SMALLMONEY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-19-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-19-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-19-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Two rows; the second value is NULL. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DATALENGTH measures expression bytes, not total on-disk row/index overhead. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: TotalRows=2 and KnownRows=1. SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-19-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-19-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SMALLMONEY has four fractional digits and a smaller range than MONEY: -214748.3648 to 214748.3647.

**Core reference:** Find `DATATYPES-19-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### TEXT: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-20-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-20-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-20-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: legacy note is returned as modern text.

**Core reference:** Find `DATATYPES-20-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: The sample has 11 ASCII bytes.

**Core reference:** Find `DATATYPES-20-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: ID 1 matches.

**Core reference:** Find `DATATYPES-20-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Contents survive conversion; inspect the new type with sp_help.

**Core reference:** Find `DATATYPES-20-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-20-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-20-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Prefix=legacy. TEXT is deprecated and has a finite maximum size; use varchar(max) or nvarchar(max).

**Core reference:** Find `DATATYPES-20-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### XML: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-21-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-21-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-21-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: One XML value.

**Core reference:** Find `DATATYPES-21-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: OrderID=1.

**Core reference:** Find `DATATYPES-21-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: OrderTotal=125.50.

**Core reference:** Find `DATATYPES-21-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: HasAmount=1.

**Core reference:** Find `DATATYPES-21-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-21-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-21-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: A record element with its id and amount is returned.

**Core reference:** Find `DATATYPES-21-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### GEOGRAPHY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-22-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-22-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-22-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: WKT uses longitude then latitude, while Point takes latitude then longitude.

**Core reference:** Find `DATATYPES-22-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: 41.8781 and -87.6298.

**Core reference:** Find `DATATYPES-22-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: 4326.

**Core reference:** Find `DATATYPES-22-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: 0 meters for this SRID.

**Core reference:** Find `DATATYPES-22-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-22-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-22-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Positive geodesic distance in meters; compare with reference within 0.01 meter on the same SQL Server version.

**Core reference:** Find `DATATYPES-22-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### GEOMETRY: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-23-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-23-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-23-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: LINESTRING with endpoints (0 0) and (3 4).

**Core reference:** Find `DATATYPES-23-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Length=5 coordinate units.

**Core reference:** Find `DATATYPES-23-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Points=2.

**Core reference:** Find `DATATYPES-23-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: LineString.

**Core reference:** Find `DATATYPES-23-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-23-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-23-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: X=0, Y=0; geometry does not imply meters.

**Core reference:** Find `DATATYPES-23-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### HIERARCHYID: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-24-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-24-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-24-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: /1/2/.

**Core reference:** Find `DATATYPES-24-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: 2.

**Core reference:** Find `DATATYPES-24-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: /1/.

**Core reference:** Find `DATATYPES-24-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: 1.

**Core reference:** Find `DATATYPES-24-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-24-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-24-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: /1/2/1/. HIERARCHYID does not itself enforce a parent foreign key.

**Core reference:** Find `DATATYPES-24-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### ROWVERSION: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-25-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-25-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-25-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: The token is automatically generated and is 8 bytes; its exact value depends on the database. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Changed=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Changed=1, even though the business value is unchanged. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: AffectedRows=1. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-25-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-25-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Second update affects 0 rows; OrderTotal stays 150. ROWVERSION is not a date/time.

**Core reference:** Find `DATATYPES-25-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### CURSOR: progression

**Beginner:15 questions**

#### ECOMMERCE-DATATYPES-26-B01

**Valid baseline**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B02

**Missing input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B03

**Exact boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B04

**Two independent rows**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B05

**Duplicate proposal**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B06

**Metadata evidence**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B07

**Unknown versus zero**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B08

**Wrong type input**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B09

**Dependency order**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B10

**Rejected request preserves state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B11

**Deterministic presentation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B12

**Least sufficient permission**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B13

**Name and scope collision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B14

**Empty state**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-B15

**Independent acceptance check**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATATYPES-26-I01

**Batch with mixed validity**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I02

**Lossless round trip**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I03

**All conflicting keys**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I04

**Drift before change**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I05

**Application bypass**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I06

**Partial input correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I07

**Idempotency decision**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I08

**Reference membership**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I09

**Schema version precondition**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I10

**Before-image restoration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I14

**Two independent implementations**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-I15

**Auditable decision table**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATATYPES-26-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A03

**Crash after accepted effect**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A07

**Restartable chunked repair**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A08

**Stale authorization at execution**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A10

**Atomic publication boundary**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A11

**Type or scope spoofing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: VisitedRows = SetBasedCount = 12. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A12

**Nonunique history correction**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: VisitedRows = SetBasedCount = 4. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A13

**Owner failure and fencing**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: VisitedRows = SetBasedCount = 1. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A14

**Independent corruption detector**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: VisitedRows = SetBasedCount = 5. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATATYPES-26-A15

**Adversarial native case study**

[Canonical question](../questions/DATATYPES.md#ecommerce-datatypes-26-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: VisitedRows = SetBasedCount = 0. CURSOR is a variable/parameter type, not a normal table-column type. Prefer set-based SQL for this counting task.

**Core reference:** Find `DATATYPES-26-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

