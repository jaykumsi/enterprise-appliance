# Retail Supply Chain: SET OPERATIONS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/SET_OPERATIONS.md)

## Teaching and troubleshooting

Both inputs need compatible column counts and types. UNION removes duplicate complete rows; UNION ALL keeps them. INTERSECT and EXCEPT compare the selected values, not hidden keys.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### SET_OPERATIONS-01-26 — Union

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Open'
UNION
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Closed'
ORDER BY WarehouseID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-01-30 — Union

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 150
UNION
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 3
ORDER BY MovementCategory;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-01-34 — Union

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate < '20240301'
UNION
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate >= '20240201'
ORDER BY MovementValue;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-01-38 — Union

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID <= 8
UNION
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID >= 5
ORDER BY MovementID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-01-42 — Union

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 100
UNION
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 2
ORDER BY MovementCategory, Status;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-02-26 — Union All

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Open'
UNION ALL
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Closed'
ORDER BY WarehouseID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-02-30 — Union All

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 150
UNION ALL
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 3
ORDER BY MovementCategory;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-02-34 — Union All

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate < '20240301'
UNION ALL
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate >= '20240201'
ORDER BY MovementValue;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-02-38 — Union All

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID <= 8
UNION ALL
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID >= 5
ORDER BY MovementID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-02-42 — Union All

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 100
UNION ALL
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 2
ORDER BY MovementCategory, Status;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-03-26 — Intersect

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Open'
INTERSECT
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Closed'
ORDER BY WarehouseID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-03-30 — Intersect

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 150
INTERSECT
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 3
ORDER BY MovementCategory;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-03-34 — Intersect

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate < '20240301'
INTERSECT
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate >= '20240201'
ORDER BY MovementValue;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-03-38 — Intersect

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID <= 8
INTERSECT
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID >= 5
ORDER BY MovementID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-03-42 — Intersect

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 100
INTERSECT
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 2
ORDER BY MovementCategory, Status;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-04-26 — Except

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Open'
EXCEPT
SELECT WarehouseID FROM [retail_supply_chain].[StockMovements] WHERE Status = 'Closed'
ORDER BY WarehouseID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-04-30 — Except

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 150
EXCEPT
SELECT MovementCategory FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 3
ORDER BY MovementCategory;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-04-34 — Except

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate < '20240301'
EXCEPT
SELECT MovementValue FROM [retail_supply_chain].[StockMovements] WHERE MovementDate >= '20240201'
ORDER BY MovementValue;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-04-38 — Except

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID <= 8
EXCEPT
SELECT MovementID FROM [retail_supply_chain].[StockMovements] WHERE MovementID >= 5
ORDER BY MovementID;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

### SET_OPERATIONS-04-42 — Except

**Question**

[Canonical questions](../questions/SET_OPERATIONS.md)

**Reference answer**

```sql
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovementValue >= 100
EXCEPT
SELECT MovementCategory, Status FROM [retail_supply_chain].[StockMovements] WHERE MovedUnits >= 2
ORDER BY MovementCategory, Status;
```

**Check and explain:** UNION ALL preserves multiplicity; UNION/INTERSECT/EXCEPT eliminate duplicates. EXCEPT is left minus right. Set operators treat NULL values as equal when comparing rows.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Union: progression

**Beginner:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B01

**Analysis audit**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Keep null values and stored token spaces.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,Segment FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Segment] AS [Segment] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "A"], [2, 1, "2024-01-02", "200.0000", "B"], [4, 2, "2024-01-03", null, "A"], [5, 3, "2024-02-01", "50.0000", "B"], [6, 3, "2024-02-10", "300.0000", "C"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B02

**Known versus unknown**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero is not unknown.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,MetricValue FROM E WHERE MetricValue IS NOT NULL
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 7 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000"], [2, 1, "200.0000"], [5, 3, "50.0000"], [6, 3, "300.0000"], [7, 4, "0.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B03

**Unknown-value queue**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An empty queue must have the requested columns.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,ActivityDate FROM E WHERE MetricValue IS NULL
)
SELECT [EventID] AS [MovementID],[ActivityDate] AS [ActivityDate] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, "2024-01-03"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B04

**Threshold review**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The lower bound is inclusive;unknown values cannot pass.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,MetricValue FROM E WHERE MetricValue>=100
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "100.0000"], [2, "200.0000"], [6, "300.0000"], [11, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B05

**Deterministic shortlist**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return fewer than five if fewer qualify;ties do not expand the result.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT TOP (5) EventID,MetricValue FROM E WHERE MetricValue IS NOT NULL ORDER BY MetricValue DESC,EventID
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MetricValue DESC,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[6, "300.0000"], [2, "200.0000"], [11, "120.0000"], [1, "100.0000"], [10, "80.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B06

**Active-owner totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown owner has null total,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420.0000"], [2, 1, 0, null], [3, 2, 2, "350.0000"], [4, 2, 2, "80.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B07

**All-owner coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Count real activity,not an outer-join placeholder.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420.0000"], [2, 1, 0, null], [3, 2, 2, "350.0000"], [4, 2, 2, "80.0000"], [5, 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B08

**Segment profile**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Use SQL Server collation equality for segment grouping.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 4, 3, "180.0000"], ["B", 3, 3, "370.0000"], ["C", 1, 1, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B09

**Owner segment coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated activity in one segment does not duplicate its owner/segment pair.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT DISTINCT OwnerID,Segment FROM E
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "A"], [1, "B"], [2, "A"], [3, "B"], [3, "C"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B10

**Observed-month totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not fabricate missing months in this question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
M AS (
SELECT DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,MetricValue FROM E
),
Report AS (
SELECT MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM M GROUP BY MonthStart
)
SELECT [MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 3, 2, "300.0000"], ["2024-02-01", 3, 3, "350.0000"], ["2024-11-01", 1, 1, "80.0000"], ["2024-12-01", 1, 1, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B11

**Daily workload**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Different source rows on the same day remain separate contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,ActivityDate
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,ActivityDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 1, "100.0000"], [1, "2024-01-02", 1, "200.0000"], [1, "2024-12-31", 1, "120.0000"], [2, "2024-01-03", 1, null], [3, "2024-02-01", 1, "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B12

**No eligible activity**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An owner with an unknown-value row is active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT p.OwnerID FROM Owners p WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=p.OwnerID)
)
SELECT [OwnerID] AS [WarehouseID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[5]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B13

**Visible parent link**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A parent excluded by the analysis eligibility rule is not visible here.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.ParentID,c.MetricValue AS ChildValue,p.MetricValue AS ParentValue FROM E c JOIN E p ON p.EventID=c.ParentID
)
SELECT [EventID] AS [MovementID],[ParentID] AS [ParentID],[ChildValue] AS [ChildValue],[ParentValue] AS [ParentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "200.0000", "100.0000"], [4, 2, null, "200.0000"], [5, 2, "50.0000", "200.0000"], [10, 5, "80.0000", "50.0000"], [11, 5, "120.0000", "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B14

**Bounded-value counts**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return0 for a segment with no values in the interval.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,SUM(CASE WHEN MetricValue BETWEEN 100 AND 200 THEN 1 ELSE 0 END) AS InRangeCount FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[InRangeCount] AS [InRangeCount] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 4, 1], ["B", 3, 2], ["C", 1, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-B15

**Value sign reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-b15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. All four classes must sum to EventCount;empty input returns five zero counts.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT COUNT(*) AS EventCount,COUNT(*)-COUNT(MetricValue) AS UnknownCount,COALESCE(SUM(CASE WHEN MetricValue<0 THEN 1 ELSE 0 END),0) AS NegativeCount,COALESCE(SUM(CASE WHEN MetricValue=0 THEN 1 ELSE 0 END),0) AS ZeroCount,COALESCE(SUM(CASE WHEN MetricValue>0 THEN 1 ELSE 0 END),0) AS PositiveCount FROM E
)
SELECT [EventCount] AS [EventCount],[UnknownCount] AS [UnknownCount],[NegativeCount] AS [NegativeCount],[ZeroCount] AS [ZeroCount],[PositiveCount] AS [PositiveCount] FROM Report ORDER BY EventCount OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[8, 1, 0, 1, 6]]
```

**Intermediate:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I01

**Exactly two per owner**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Ties cannot expand a two-row limit.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC,EventID) AS Position FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,Position FROM R WHERE Position<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[Position] AS [Position] FROM Report ORDER BY WarehouseID,Position OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [3, 6, "300.0000", 1], [3, 5, "50.0000", 2], [4, 10, "80.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I02

**Two value positions with ties**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Several rows may share rank2;all must remain.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC) AS ValueRank FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,ValueRank FROM R WHERE ValueRank<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[ValueRank] AS [ValueRank] FROM Report ORDER BY WarehouseID,ValueRank,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [3, 6, "300.0000", 1], [3, 5, "50.0000", 2], [4, 10, "80.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I03

**Running value and knowledge**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown prefix has null RunningValue.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,COUNT(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningKnownCount FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[RunningValue] AS [RunningValue],[RunningKnownCount] AS [RunningKnownCount] FROM Report ORDER BY WarehouseID,ActivityDate,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "100.0000", 1], [2, 1, "2024-01-02", "200.0000", "300.0000", 2], [11, 1, "2024-12-31", "120.0000", "420.0000", 3], [4, 2, "2024-01-03", null, null, 0], [5, 3, "2024-02-01", "50.0000", "50.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I04

**Previous row delta**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not skip an unknown predecessor.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
P AS (
SELECT *,LAG(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousValue FROM E
),
Report AS (
SELECT EventID,OwnerID,MetricValue,PreviousValue,MetricValue-PreviousValue AS Delta FROM P
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PreviousValue] AS [PreviousValue],[Delta] AS [Delta] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", null, null], [2, 1, "200.0000", "100.0000", "100.0000"], [11, 1, "120.0000", "200.0000", "-80.0000"], [4, 2, null, null, null], [5, 3, "50.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I05

**Share before filtering**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Filtered-out owners must still contribute to the denominator.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,SUM(MetricValue) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank,SUM(TotalValue) OVER(PARTITION BY Segment) AS SegmentTotal FROM T
),
Report AS (
SELECT Segment,OwnerID,TotalValue,ValueRank,SegmentTotal,CAST(100.0*TotalValue/NULLIF(SegmentTotal,0) AS decimal(19,6)) AS SharePercent FROM R WHERE ValueRank<=2
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[SegmentTotal] AS [SegmentTotal],[SharePercent] AS [SharePercent] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "180.0000", "55.555555555555555555555555555555555555555555555556"], ["A", 4, "80.0000", 2, "180.0000", "44.444444444444444444444444444444444444444444444444"], ["B", 1, "320.0000", 1, "370.0000", "86.486486486486486486486486486486486486486486486486"], ["B", 3, "50.0000", 2, "370.0000", "13.513513513513513513513513513513513513513513513514"], ["C", 3, "300.0000", 1, "300.0000", "100"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I06

**Every required segment**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Required AS (
SELECT N'A' AS Segment UNION ALL SELECT N'B' UNION ALL SELECT N'C'
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT t.OwnerID,t.EventCount,t.TotalValue FROM T t WHERE NOT EXISTS(SELECT 1 FROM Required r WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=t.OwnerID AND e.Kind=r.Segment))
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I07

**Prior calendar window**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.OwnerID,COUNT(p.MetricValue) AS PriorKnownCount,CAST(AVG(CAST(p.MetricValue AS decimal(28,6))) AS decimal(28,6)) AS PriorAverage FROM E c LEFT JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate GROUP BY c.EventID,c.OwnerID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[PriorKnownCount] AS [PriorKnownCount],[PriorAverage] AS [PriorAverage] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 0, null], [2, 1, 1, "100.0000"], [11, 1, 0, null], [4, 2, 0, null], [5, 3, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I08

**First and last known rows**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero participates;do not independently take the minimum value instead of the first row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT OwnerID,EventID,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS FirstPos,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate DESC,EventID DESC) AS LastPos FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT p.OwnerID,MAX(CASE WHEN k.FirstPos=1 THEN k.EventID END) AS FirstEventID,MAX(CASE WHEN k.LastPos=1 THEN k.EventID END) AS LastEventID FROM Owners p LEFT JOIN K k ON k.OwnerID=p.OwnerID GROUP BY p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[LastEventID] AS [LastEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 11], [2, null, null], [3, 5, 6], [4, 7, 10], [5, null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I09

**Complete 2024 calendar**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Each owner has exactly12 rows;2025 activity cannot enter2024.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Months AS (
SELECT CAST('20240101' AS date) AS MonthStart UNION ALL SELECT DATEADD(month,1,MonthStart) FROM Months WHERE MonthStart<'20241201'
),
T AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' GROUP BY OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1)
),
Report AS (
SELECT p.OwnerID,m.MonthStart,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p CROSS JOIN Months m LEFT JOIN T t ON t.OwnerID=p.OwnerID AND t.MonthStart=m.MonthStart
)
SELECT [OwnerID] AS [WarehouseID],[MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 60 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 2, 2, "300.0000"], [1, "2024-02-01", 0, 0, "0"], [1, "2024-03-01", 0, 0, "0"], [1, "2024-04-01", 0, 0, "0"], [1, "2024-05-01", 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I10

**Dominant segments**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The best of several negative totals is the least negative,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,Segment,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,Segment HAVING COUNT(MetricValue)>0
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY TotalValue DESC) AS ValueRank FROM T
),
Report AS (
SELECT OwnerID,Segment,TotalValue FROM R WHERE ValueRank=1
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "B", "320.0000"], [3, "C", "300.0000"], [4, "A", "80.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I11

**Same-day repeated values**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,MetricValue,COUNT(*) AS Multiplicity FROM E GROUP BY OwnerID,ActivityDate,MetricValue HAVING COUNT(*)>=2
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Multiplicity] AS [Multiplicity] FROM Report ORDER BY WarehouseID,ActivityDate,MetricValue OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I12

**First threshold crossing**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Owners with no positive values produce no threshold crossing.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,SUM(MetricValue) OVER(PARTITION BY OwnerID) AS TotalValue FROM E WHERE MetricValue>0
),
C AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS Choice FROM R WHERE RunningValue>=0.8*TotalValue
),
Report AS (
SELECT OwnerID,EventID,RunningValue,TotalValue FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[RunningValue] AS [RunningValue],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, "420.0000", "420.0000"], [3, 6, "350.0000", "350.0000"], [4, 10, "80.0000", "80.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I13

**Owner median**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. No known values gives count0 and null median,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue,EventID) AS Position,COUNT(*) OVER(PARTITION BY OwnerID) AS KnownCount FROM E WHERE MetricValue IS NOT NULL
),
T AS (
SELECT OwnerID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM K WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.KnownCount,0) AS KnownCount,t.MedianValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[KnownCount] AS [KnownCount],[MedianValue] AS [MedianValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, "120.0000"], [2, 0, null], [3, 2, "175.0000"], [4, 2, "40.0000"], [5, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I14

**Two-generation comparison**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two joins cannot follow an excluded parent through to its grandparent.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,p.EventID AS ParentEventID,g.EventID AS GrandparentEventID,c.MetricValue,p.MetricValue AS ParentValue,g.MetricValue AS GrandparentValue FROM E c LEFT JOIN E p ON p.EventID=c.ParentID LEFT JOIN E g ON g.EventID=p.ParentID
)
SELECT [EventID] AS [MovementID],[ParentEventID] AS [ParentEventID],[GrandparentEventID] AS [GrandparentEventID],[MetricValue] AS [MetricValue],[ParentValue] AS [ParentValue],[GrandparentValue] AS [GrandparentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, null, "100.0000", null, null], [2, 1, null, "200.0000", "100.0000", null], [4, 2, 1, null, "200.0000", "100.0000"], [5, 2, 1, "50.0000", "200.0000", "100.0000"], [6, null, null, "300.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-I15

**Largest inactive gap**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-i15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
L AS (
SELECT OwnerID,ActivityDate AS EndDate,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS StartDate FROM D
),
R AS (
SELECT *,DATEDIFF(day,StartDate,EndDate) AS GapDays,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY DATEDIFF(day,StartDate,EndDate) DESC,StartDate) AS Choice FROM L WHERE StartDate IS NOT NULL
),
Report AS (
SELECT p.OwnerID,r.StartDate,r.EndDate,r.GapDays FROM Owners p LEFT JOIN R r ON r.OwnerID=p.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[GapDays] AS [GapDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", "2024-12-31", 364], [2, null, null, null], [3, "2024-02-01", "2024-02-10", 9], [4, "2024-02-29", "2024-11-03", 248], [5, null, null, null]]
```

**Advanced:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A01

**Session boundaries and comparable recovery**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
L AS (
SELECT *,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousDate FROM E
),
S AS (
SELECT *,SUM(CASE WHEN PreviousDate IS NULL OR DATEDIFF(day,PreviousDate,ActivityDate)>30 THEN 1 ELSE 0 END) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS SessionNo FROM L
),
T AS (
SELECT OwnerID,SessionNo,MIN(ActivityDate) AS StartDate,MAX(ActivityDate) AS EndDate,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM S GROUP BY OwnerID,SessionNo
),
P AS (
SELECT *,LAG(TotalValue) OVER(PARTITION BY OwnerID ORDER BY SessionNo) AS PreviousValue FROM T
),
Report AS (
SELECT o.OwnerID,COALESCE(p.SessionNo,0) AS SessionNo,p.StartDate,p.EndDate,COALESCE(p.EventCount,0) AS EventCount,COALESCE(p.KnownCount,0) AS KnownCount,CASE WHEN p.SessionNo IS NULL THEN CAST(0 AS decimal(38,4)) ELSE p.TotalValue END AS TotalValue,p.PreviousValue,CAST(100.0*(p.TotalValue-p.PreviousValue)/NULLIF(p.PreviousValue,0) AS decimal(38,6)) AS GrowthPercent FROM Owners o LEFT JOIN P p ON p.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[SessionNo] AS [SessionNo],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[PreviousValue] AS [PreviousValue],[GrowthPercent] AS [GrowthPercent] FROM Report ORDER BY WarehouseID,SessionNo OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 7 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "2024-01-02", 2, 2, "300.0000", null, null], [1, 2, "2024-12-31", "2024-12-31", 1, 1, "120.0000", "300.0000", "-60"], [2, 1, "2024-01-03", "2024-01-03", 1, 0, null, null, null], [3, 1, "2024-02-01", "2024-02-10", 2, 2, "350.0000", null, null], [4, 1, "2024-02-29", "2024-02-29", 1, 1, "0.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A02

**Prior-window median anomaly**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
H AS (
SELECT c.EventID,p.EventID AS HistoryID,p.MetricValue,ROW_NUMBER() OVER(PARTITION BY c.EventID ORDER BY p.MetricValue,p.EventID) AS Position,COUNT(*) OVER(PARTITION BY c.EventID) AS KnownCount FROM E c JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate WHERE p.MetricValue IS NOT NULL
),
M AS (
SELECT EventID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM H WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY EventID
),
Report AS (
SELECT e.EventID,e.OwnerID,e.MetricValue,COALESCE(m.KnownCount,0) AS PriorKnownCount,m.MedianValue AS PriorMedian,CASE WHEN e.MetricValue>2*m.MedianValue THEN 1 ELSE 0 END AS IsAnomaly FROM E e LEFT JOIN M m ON m.EventID=e.EventID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PriorKnownCount] AS [PriorKnownCount],[PriorMedian] AS [PriorMedian],[IsAnomaly] AS [IsAnomaly] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", 0, null, 0], [2, 1, "200.0000", 1, "100.0000", 0], [11, 1, "120.0000", 0, null, 0], [4, 2, null, 0, null, 0], [5, 3, "50.0000", 0, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A03

**Smallest complete tie groups reaching80 percent**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
G AS (
SELECT Segment,TotalValue,CAST(SUM(TotalValue) AS decimal(28,4)) AS PeerTotal FROM T GROUP BY Segment,TotalValue
),
C AS (
SELECT *,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment ORDER BY TotalValue DESC ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS CumulativeValue,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank FROM G
),
Report AS (
SELECT t.Segment,t.OwnerID,t.TotalValue,c.ValueRank,c.CumulativeValue,c.SegmentTotal FROM T t JOIN C c ON c.Segment=t.Segment AND c.TotalValue=t.TotalValue WHERE c.CumulativeValue-c.PeerTotal<0.8*c.SegmentTotal
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[CumulativeValue] AS [CumulativeValue],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "100.0000", "180.0000"], ["A", 4, "80.0000", 2, "180.0000", "180.0000"], ["B", 1, "320.0000", 1, "320.0000", "370.0000"], ["C", 3, "300.0000", 1, "300.0000", "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A04

**Six-month cohort retention**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
FirstSeen AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(MIN(ActivityDate)),MONTH(MIN(ActivityDate)),1) AS CohortMonth FROM E GROUP BY OwnerID
),
C AS (
SELECT * FROM FirstSeen WHERE CohortMonth>='20240101' AND CohortMonth<'20250101'
),
N AS (
SELECT 0 AS MonthOffset UNION ALL SELECT MonthOffset+1 FROM N WHERE MonthOffset<5
),
A AS (
SELECT DISTINCT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS ActivityMonth FROM E
),
Report AS (
SELECT c.CohortMonth,n.MonthOffset,DATEADD(month,n.MonthOffset,c.CohortMonth) AS ActivityMonth,COUNT(*) AS CohortSize,COUNT(a.OwnerID) AS ActiveOwners,CAST(100.0*COUNT(a.OwnerID)/COUNT(*) AS decimal(19,6)) AS RetentionPercent FROM C c CROSS JOIN N n LEFT JOIN A a ON a.OwnerID=c.OwnerID AND a.ActivityMonth=DATEADD(month,n.MonthOffset,c.CohortMonth) GROUP BY c.CohortMonth,n.MonthOffset
)
SELECT [CohortMonth] AS [CohortMonth],[MonthOffset] AS [MonthOffset],[ActivityMonth] AS [ActivityMonth],[CohortSize] AS [CohortSize],[ActiveOwners] AS [ActiveOwners],[RetentionPercent] AS [RetentionPercent] FROM Report ORDER BY CohortMonth,MonthOffset OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 0, "2024-01-01", 2, 2, "100"], ["2024-01-01", 1, "2024-02-01", 2, 0, "0"], ["2024-01-01", 2, "2024-03-01", 2, 0, "0"], ["2024-01-01", 3, "2024-04-01", 2, 0, "0"], ["2024-01-01", 4, "2024-05-01", 2, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A05

**Longest activity run with one missing day**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
N AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS Position FROM D
),
C AS (
SELECT s.OwnerID,s.ActivityDate AS StartDate,e.ActivityDate AS EndDate,e.Position-s.Position+1 AS ActiveDays,DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1) AS MissingDays FROM N s JOIN N e ON e.OwnerID=s.OwnerID AND e.Position>=s.Position WHERE DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1)<=1
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActiveDays DESC,StartDate,EndDate) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartDate,r.EndDate,COALESCE(r.ActiveDays,0) AS ActiveDays,COALESCE(r.MissingDays,0) AS MissingDays FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[ActiveDays] AS [ActiveDays],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", "2024-01-02", 2, 0], [2, "2024-01-03", "2024-01-03", 1, 0], [3, "2024-02-01", "2024-02-01", 1, 0], [4, "2024-02-29", "2024-02-29", 1, 0], [5, null, null, 0, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A06

**Cycle-safe parent resolution**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Walk AS (
SELECT EventID AS StartID,EventID AS CurrentID,ParentID AS NextID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT w.StartID,e.EventID,e.ParentID,CAST(w.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),w.Depth+1 FROM Walk w JOIN E e ON e.EventID=w.NextID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',w.VisitPath)=0 AND w.Depth<100
),
Terminal AS (
SELECT w.*,CASE WHEN w.NextID IS NOT NULL AND CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 THEN 1 ELSE 0 END AS CycleFlag,CASE WHEN w.NextID IS NOT NULL AND NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID) THEN 1 ELSE 0 END AS BoundaryFlag FROM Walk w WHERE w.NextID IS NULL OR CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 OR NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID)
),
Report AS (
SELECT StartID AS EventID,CurrentID AS TerminalEventID,CASE WHEN NextID IS NULL THEN CurrentID END AS RootEventID,Depth,CycleFlag,BoundaryFlag,VisitPath FROM Terminal
)
SELECT [EventID] AS [MovementID],[TerminalEventID] AS [TerminalEventID],[RootEventID] AS [RootEventID],[Depth] AS [Depth],[CycleFlag] AS [CycleFlag],[BoundaryFlag] AS [BoundaryFlag],[VisitPath] AS [VisitPath] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, 0, 0, 0, "/1/"], [2, 1, 1, 1, 0, 0, "/2/1/"], [4, 1, 1, 2, 0, 0, "/4/2/1/"], [5, 1, 1, 2, 0, 0, "/5/2/1/"], [6, 6, null, 0, 0, 1, "/6/"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A07

**As-of correction-chain survivors**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Versions AS (
SELECT EventID AS RootID,EventID,ActivityDate,MetricValue,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E WHERE ParentID IS NULL UNION ALL SELECT v.RootID,e.EventID,e.ActivityDate,e.MetricValue,CAST(v.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),v.Depth+1 FROM Versions v JOIN E e ON e.ParentID=v.EventID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',v.VisitPath)=0 AND v.Depth<100
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY RootID ORDER BY ActivityDate DESC,EventID DESC) AS Choice FROM Versions WHERE ActivityDate<='20241231'
),
Report AS (
SELECT e.EventID AS RootEventID,r.EventID AS SelectedEventID,r.ActivityDate,r.MetricValue,r.Depth FROM E e LEFT JOIN R r ON r.RootID=e.EventID AND r.Choice=1 WHERE e.ParentID IS NULL
)
SELECT [RootEventID] AS [RootEventID],[SelectedEventID] AS [SelectedEventID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Depth] AS [Depth] FROM Report ORDER BY RootEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, "2024-12-31", "120.0000", 3]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A08

**FIFO interval allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Supply AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='A' AND MetricValue>0
),
Demand AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='B' AND MetricValue>0
),
Matches AS (
SELECT s.OwnerID,s.EventID AS SupplyEventID,d.EventID AS DemandEventID,(CASE WHEN s.EndValue<d.EndValue THEN s.EndValue ELSE d.EndValue END)-(CASE WHEN s.EndValue-s.MetricValue>d.EndValue-d.MetricValue THEN s.EndValue-s.MetricValue ELSE d.EndValue-d.MetricValue END) AS AllocatedValue FROM Supply s JOIN Demand d ON d.OwnerID=s.OwnerID AND s.EndValue>d.EndValue-d.MetricValue AND d.EndValue>s.EndValue-s.MetricValue
),
Result AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,CAST(0 AS decimal(38,4)) AS UnmatchedValue FROM Matches UNION ALL SELECT s.OwnerID,s.EventID,NULL,0,s.MetricValue-COALESCE(x.UsedValue,0) FROM Supply s LEFT JOIN(SELECT SupplyEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY SupplyEventID)x ON x.SupplyEventID=s.EventID WHERE s.MetricValue>COALESCE(x.UsedValue,0) UNION ALL SELECT d.OwnerID,NULL,d.EventID,0,d.MetricValue-COALESCE(x.UsedValue,0) FROM Demand d LEFT JOIN(SELECT DemandEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY DemandEventID)x ON x.DemandEventID=d.EventID WHERE d.MetricValue>COALESCE(x.UsedValue,0)
),
Report AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,UnmatchedValue FROM Result
)
SELECT [OwnerID] AS [WarehouseID],[SupplyEventID] AS [SupplyEventID],[DemandEventID] AS [DemandEventID],[AllocatedValue] AS [AllocatedValue],[UnmatchedValue] AS [UnmatchedValue] FROM Report ORDER BY WarehouseID,SupplyEventID,DemandEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, 2, "0", "100.0000"], [1, null, 11, "0", "120.0000"], [1, 1, 2, "100.0000", "0"], [3, null, 5, "0", "50.0000"], [4, 10, null, "0", "80.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A09

**Conserved largest-remainder allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
W AS (
SELECT *,CAST(SUM(TotalValue) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal FROM T
),
Units AS (
SELECT *,CAST(TotalValue*10000 AS decimal(28,0)) AS TotalUnits,CAST(SegmentTotal*10000 AS decimal(28,0)) AS SegmentUnits FROM W
),
Numerators AS (
SELECT *,CAST(TotalUnits*10000 AS decimal(33,0)) AS NumeratorUnits FROM Units
),
Remainders AS (
SELECT *,NumeratorUnits%SegmentUnits AS RemainderUnits FROM Numerators
),
Bases AS (
SELECT *,CAST((NumeratorUnits-RemainderUnits)/SegmentUnits AS int) AS BasePoints FROM Remainders
),
R AS (
SELECT *,10000-SUM(BasePoints) OVER(PARTITION BY Segment) AS RemainingPoints,ROW_NUMBER() OVER(PARTITION BY Segment ORDER BY RemainderUnits DESC,OwnerID) AS RemainderPosition FROM Bases
),
Report AS (
SELECT Segment,OwnerID,TotalValue,BasePoints+CASE WHEN RemainderPosition<=RemainingPoints THEN 1 ELSE 0 END AS BasisPoints,SegmentTotal FROM R
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[BasisPoints] AS [BasisPoints],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 5556, "180.0000"], ["A", 4, "80.0000", 4444, "180.0000"], ["B", 1, "320.0000", 8649, "370.0000"], ["B", 3, "50.0000", 1351, "370.0000"], ["C", 3, "300.0000", 10000, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A10

**Complete inactivity intervals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' UNION SELECT OwnerID,CAST('20231231' AS date) FROM Owners UNION SELECT OwnerID,CAST('20250101' AS date) FROM Owners
),
L AS (
SELECT OwnerID,ActivityDate,LEAD(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS NextDate FROM D
),
Report AS (
SELECT OwnerID,DATEADD(day,1,ActivityDate) AS StartDate,DATEADD(day,-1,NextDate) AS EndDate,DATEDIFF(day,ActivityDate,NextDate)-1 AS MissingDays FROM L WHERE DATEDIFF(day,ActivityDate,NextDate)>1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID,StartDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 10 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-03", "2024-12-30", 363], [2, "2024-01-01", "2024-01-02", 2], [2, "2024-01-04", "2024-12-31", 363], [3, "2024-01-01", "2024-01-31", 31], [3, "2024-02-02", "2024-02-09", 8]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A11

**Ordered three-stage funnel**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
C AS (
SELECT a.OwnerID,a.EventID AS FirstEventID,b.EventID AS SecondEventID,c.EventID AS ThirdEventID,a.ActivityDate AS StartDate,c.ActivityDate AS EndDate,ROW_NUMBER() OVER(PARTITION BY a.OwnerID ORDER BY c.ActivityDate,c.EventID,b.ActivityDate DESC,b.EventID DESC,a.ActivityDate DESC,a.EventID DESC) AS Choice FROM E a JOIN E b ON b.OwnerID=a.OwnerID AND (b.ActivityDate>a.ActivityDate OR(b.ActivityDate=a.ActivityDate AND b.EventID>a.EventID)) JOIN E c ON c.OwnerID=b.OwnerID AND (c.ActivityDate>b.ActivityDate OR(c.ActivityDate=b.ActivityDate AND c.EventID>b.EventID)) WHERE a.Kind='A' AND b.Kind='B' AND c.Kind='C'
),
Report AS (
SELECT OwnerID,FirstEventID,SecondEventID,ThirdEventID,StartDate,EndDate FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[SecondEventID] AS [SecondEventID],[ThirdEventID] AS [ThirdEventID],[StartDate] AS [StartDate],[EndDate] AS [EndDate] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A12

**Earliest rolling coverage with witnesses**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate AS TriggerDate FROM E
),
W AS (
SELECT d.OwnerID,d.TriggerDate,e.Kind AS Segment,e.EventID,ROW_NUMBER() OVER(PARTITION BY d.OwnerID,d.TriggerDate,e.Kind ORDER BY e.ActivityDate DESC,e.EventID DESC) AS Position FROM D d JOIN E e ON e.OwnerID=d.OwnerID AND e.ActivityDate>=DATEADD(day,-29,d.TriggerDate) AND e.ActivityDate<=d.TriggerDate WHERE e.Kind IN('A','B','C')
),
P AS (
SELECT OwnerID,TriggerDate,MAX(CASE WHEN Segment='A' THEN EventID END) AS AEventID,MAX(CASE WHEN Segment='B' THEN EventID END) AS BEventID,MAX(CASE WHEN Segment='C' THEN EventID END) AS CEventID FROM W WHERE Position=1 GROUP BY OwnerID,TriggerDate HAVING COUNT(*)=3
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY TriggerDate) AS Choice FROM P
),
Report AS (
SELECT OwnerID,TriggerDate,AEventID,BEventID,CEventID FROM R WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[TriggerDate] AS [TriggerDate],[AEventID] AS [AEventID],[BEventID] AS [BEventID],[CEventID] AS [CEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A13

**Distinct descendant exposure with cycles**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Down AS (
SELECT EventID AS StartID,EventID AS NodeID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT d.StartID,e.EventID,CAST(d.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),d.Depth+1 FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)=0 AND d.Depth<100
),
DistinctNodes AS (
SELECT DISTINCT StartID,NodeID FROM Down WHERE Depth>0
),
T AS (
SELECT d.StartID,COUNT(*) AS DescendantCount,COUNT(e.MetricValue) AS KnownCount,SUM(e.MetricValue) AS TotalValue FROM DistinctNodes d JOIN E e ON e.EventID=d.NodeID GROUP BY d.StartID
),
Cycles AS (
SELECT DISTINCT d.StartID FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)>0
),
Report AS (
SELECT e.EventID,COALESCE(t.DescendantCount,0) AS DescendantCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.StartID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,CASE WHEN c.StartID IS NULL THEN 0 ELSE 1 END AS CycleFlag FROM E e LEFT JOIN T t ON t.StartID=e.EventID LEFT JOIN Cycles c ON c.StartID=e.EventID
)
SELECT [EventID] AS [MovementID],[DescendantCount] AS [DescendantCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[CycleFlag] AS [CycleFlag] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 5, 4, "450.0000", 0], [2, 4, 3, "250.0000", 0], [4, 0, 0, "0", 0], [5, 2, 2, "200.0000", 0], [6, 0, 0, "0", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A14

**Best mean-centered contiguous block**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
OwnerStats AS (
SELECT OwnerID,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS KnownTotal FROM E GROUP BY OwnerID
),
N AS (
SELECT e.*,CAST(s.KnownCount AS decimal(4,0))*e.MetricValue-CAST(s.KnownTotal AS decimal(28,4)) AS ScoreValue,ROW_NUMBER() OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID) AS Position,SUM(CASE WHEN e.MetricValue IS NULL THEN 1 ELSE 0 END) OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID ROWS UNBOUNDED PRECEDING) AS BlockID FROM E e JOIN OwnerStats s ON s.OwnerID=e.OwnerID
),
P AS (
SELECT *,CAST(SUM(ScoreValue) OVER(PARTITION BY OwnerID,BlockID ORDER BY Position ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS PrefixValue FROM N WHERE MetricValue IS NOT NULL
),
C AS (
SELECT s.OwnerID,s.EventID AS StartEventID,e.EventID AS EndEventID,s.Position AS StartPosition,e.Position AS EndPosition,e.PrefixValue-s.PrefixValue+s.ScoreValue AS BlockScore,e.Position-s.Position+1 AS EventCount FROM P s JOIN P e ON e.OwnerID=s.OwnerID AND e.BlockID=s.BlockID AND e.Position>=s.Position
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY BlockScore DESC,StartPosition,EndPosition) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartEventID,r.EndEventID,r.BlockScore,COALESCE(r.EventCount,0) AS EventCount FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartEventID] AS [StartEventID],[EndEventID] AS [EndEventID],[BlockScore] AS [BlockScore],[EventCount] AS [EventCount] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "180.0000", 1], [2, null, null, null, 0], [3, 6, 6, "250.0000", 1], [4, 10, 10, "80.0000", 1], [5, null, null, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-01-A15

**Five-table reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-01-a15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') UNION SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Eligible AS (
SELECT f.* FROM [retail_supply_chain].[StockMovements] f JOIN E e ON e.EventID=f.[MovementID]
),
HeaderTotals AS (
SELECT [WarehouseID] AS OwnerID,COUNT(*) AS EventCount,COUNT([MovementValue]) AS KnownCount,SUM([MovementValue]) AS TotalValue FROM Eligible GROUP BY [WarehouseID]
),
Net AS (
SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM Eligible GROUP BY WarehouseID,ProductID
),
Balances AS (
SELECT b.WarehouseID AS OwnerID,SUM(b.OpeningQuantity) AS OpeningUnits,SUM(b.QuantityOnHand) AS StoredUnits,SUM(COALESCE(n.NetUnits,0)) AS SelectedNetUnits,SUM(b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0))) AS QuantityDifference,SUM(b.QuantityOnHand*p.UnitCost) AS StandardStockValue FROM retail_supply_chain.StockBalances b JOIN retail_supply_chain.Products p ON p.ProductID=b.ProductID LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID GROUP BY b.WarehouseID
),
Missing AS (
SELECT n.WarehouseID AS OwnerID,COUNT(*) AS MissingBalancePairs FROM Net n WHERE NOT EXISTS(SELECT 1 FROM retail_supply_chain.StockBalances b WHERE b.WarehouseID=n.WarehouseID AND b.ProductID=n.ProductID) GROUP BY n.WarehouseID
),
SupplierLead AS (
SELECT e.WarehouseID AS OwnerID,MAX(s.LeadTimeDays) AS MaxLeadTimeDays FROM Eligible e JOIN retail_supply_chain.Suppliers s ON s.SupplierID=e.SupplierID GROUP BY e.WarehouseID
),
Report AS (
SELECT o.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.OwnerID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,COALESCE(b.OpeningUnits,0) AS OpeningUnits,COALESCE(b.StoredUnits,0) AS StoredUnits,COALESCE(b.SelectedNetUnits,0) AS SelectedNetUnits,COALESCE(b.QuantityDifference,0) AS QuantityDifference,COALESCE(b.StandardStockValue,0) AS StandardStockValue,COALESCE(m.MissingBalancePairs,0) AS MissingBalancePairs,l.MaxLeadTimeDays FROM Owners o LEFT JOIN HeaderTotals t ON t.OwnerID=o.OwnerID LEFT JOIN Balances b ON b.OwnerID=o.OwnerID LEFT JOIN Missing m ON m.OwnerID=o.OwnerID LEFT JOIN SupplierLead l ON l.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[OpeningUnits] AS [OpeningUnits],[StoredUnits] AS [StoredUnits],[SelectedNetUnits] AS [SelectedNetUnits],[QuantityDifference] AS [QuantityDifference],[StandardStockValue] AS [StandardStockValue],[MissingBalancePairs] AS [MissingBalancePairs],[MaxLeadTimeDays] AS [MaxLeadTimeDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420", "40", "36", "-4", "0", "327", 0, 3], [2, 1, 0, null, "20", "31", "4", "7", "483", 0, 1], [3, 2, 2, "350", "20", "21", "1", "0", "138", 0, 3], [4, 2, 2, "80", "40", "42", "5", "-3", "449", 0, 3], [5, 0, 0, "0", "0", "0", "0", "0", "0", 0, null]]
```

### Union All: progression

**Beginner:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B01

**Analysis audit**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Keep null values and stored token spaces.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,Segment FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Segment] AS [Segment] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "A"], [2, 1, "2024-01-02", "200.0000", "B"], [3, 2, "2024-01-02", "200.0000", "C"], [4, 2, "2024-01-03", null, "A"], [5, 3, "2024-02-01", "50.0000", "B"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B02

**Known versus unknown**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero is not unknown.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,MetricValue FROM E WHERE MetricValue IS NOT NULL
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 11 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000"], [2, 1, "200.0000"], [3, 2, "200.0000"], [5, 3, "50.0000"], [6, 3, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B03

**Unknown-value queue**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An empty queue must have the requested columns.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,ActivityDate FROM E WHERE MetricValue IS NULL
)
SELECT [EventID] AS [MovementID],[ActivityDate] AS [ActivityDate] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, "2024-01-03"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B04

**Threshold review**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The lower bound is inclusive;unknown values cannot pass.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,MetricValue FROM E WHERE MetricValue>=100
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "100.0000"], [2, "200.0000"], [3, "200.0000"], [6, "300.0000"], [8, "150.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B05

**Deterministic shortlist**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return fewer than five if fewer qualify;ties do not expand the result.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT TOP (5) EventID,MetricValue FROM E WHERE MetricValue IS NOT NULL ORDER BY MetricValue DESC,EventID
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MetricValue DESC,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[6, "300.0000"], [9, "300.0000"], [2, "200.0000"], [3, "200.0000"], [12, "200.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B06

**Active-owner totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown owner has null total,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420.0000"], [2, 3, 2, "400.0000"], [3, 2, 2, "350.0000"], [4, 4, 4, "530.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B07

**All-owner coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Count real activity,not an outer-join placeholder.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420.0000"], [2, 3, 2, "400.0000"], [3, 2, 2, "350.0000"], [4, 4, 4, "530.0000"], [5, 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B08

**Segment profile**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Use SQL Server collation equality for segment grouping.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 4, 3, "180.0000"], ["B", 4, 4, "520.0000"], ["C", 4, 4, "1000.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B09

**Owner segment coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated activity in one segment does not duplicate its owner/segment pair.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT DISTINCT OwnerID,Segment FROM E
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 9 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "A"], [1, "B"], [2, "A"], [2, "C"], [3, "B"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B10

**Observed-month totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not fabricate missing months in this question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
M AS (
SELECT DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,MetricValue FROM E
),
Report AS (
SELECT MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM M GROUP BY MonthStart
)
SELECT [MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 4, 3, "500.0000"], ["2024-02-01", 3, 3, "350.0000"], ["2024-03-01", 2, 2, "450.0000"], ["2024-11-01", 1, 1, "80.0000"], ["2024-12-01", 1, 1, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B11

**Daily workload**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Different source rows on the same day remain separate contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,ActivityDate
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,ActivityDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 1, "100.0000"], [1, "2024-01-02", 1, "200.0000"], [1, "2024-12-31", 1, "120.0000"], [2, "2024-01-02", 1, "200.0000"], [2, "2024-01-03", 1, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B12

**No eligible activity**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An owner with an unknown-value row is active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT p.OwnerID FROM Owners p WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=p.OwnerID)
)
SELECT [OwnerID] AS [WarehouseID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[5]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B13

**Visible parent link**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A parent excluded by the analysis eligibility rule is not visible here.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.ParentID,c.MetricValue AS ChildValue,p.MetricValue AS ParentValue FROM E c JOIN E p ON p.EventID=c.ParentID
)
SELECT [EventID] AS [MovementID],[ParentID] AS [ParentID],[ChildValue] AS [ChildValue],[ParentValue] AS [ParentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 11 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "200.0000", "100.0000"], [3, 1, "200.0000", "100.0000"], [4, 2, null, "200.0000"], [5, 2, "50.0000", "200.0000"], [6, 3, "300.0000", "200.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B14

**Bounded-value counts**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return0 for a segment with no values in the interval.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,SUM(CASE WHEN MetricValue BETWEEN 100 AND 200 THEN 1 ELSE 0 END) AS InRangeCount FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[InRangeCount] AS [InRangeCount] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 4, 1], ["B", 4, 3], ["C", 4, 2]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-B15

**Value sign reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-b15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. All four classes must sum to EventCount;empty input returns five zero counts.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT COUNT(*) AS EventCount,COUNT(*)-COUNT(MetricValue) AS UnknownCount,COALESCE(SUM(CASE WHEN MetricValue<0 THEN 1 ELSE 0 END),0) AS NegativeCount,COALESCE(SUM(CASE WHEN MetricValue=0 THEN 1 ELSE 0 END),0) AS ZeroCount,COALESCE(SUM(CASE WHEN MetricValue>0 THEN 1 ELSE 0 END),0) AS PositiveCount FROM E
)
SELECT [EventCount] AS [EventCount],[UnknownCount] AS [UnknownCount],[NegativeCount] AS [NegativeCount],[ZeroCount] AS [ZeroCount],[PositiveCount] AS [PositiveCount] FROM Report ORDER BY EventCount OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[12, 1, 0, 1, 10]]
```

**Intermediate:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I01

**Exactly two per owner**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Ties cannot expand a two-row limit.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC,EventID) AS Position FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,Position FROM R WHERE Position<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[Position] AS [Position] FROM Report ORDER BY WarehouseID,Position OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [2, 3, "200.0000", 1], [2, 12, "200.0000", 2], [3, 6, "300.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I02

**Two value positions with ties**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Several rows may share rank2;all must remain.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC) AS ValueRank FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,ValueRank FROM R WHERE ValueRank<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[ValueRank] AS [ValueRank] FROM Report ORDER BY WarehouseID,ValueRank,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [2, 3, "200.0000", 1], [2, 12, "200.0000", 1], [3, 6, "300.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I03

**Running value and knowledge**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown prefix has null RunningValue.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,COUNT(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningKnownCount FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[RunningValue] AS [RunningValue],[RunningKnownCount] AS [RunningKnownCount] FROM Report ORDER BY WarehouseID,ActivityDate,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "100.0000", 1], [2, 1, "2024-01-02", "200.0000", "300.0000", 2], [11, 1, "2024-12-31", "120.0000", "420.0000", 3], [3, 2, "2024-01-02", "200.0000", "200.0000", 1], [4, 2, "2024-01-03", null, "200.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I04

**Previous row delta**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not skip an unknown predecessor.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
P AS (
SELECT *,LAG(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousValue FROM E
),
Report AS (
SELECT EventID,OwnerID,MetricValue,PreviousValue,MetricValue-PreviousValue AS Delta FROM P
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PreviousValue] AS [PreviousValue],[Delta] AS [Delta] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", null, null], [2, 1, "200.0000", "100.0000", "100.0000"], [11, 1, "120.0000", "200.0000", "-80.0000"], [3, 2, "200.0000", null, null], [4, 2, null, "200.0000", null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I05

**Share before filtering**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Filtered-out owners must still contribute to the denominator.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,SUM(MetricValue) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank,SUM(TotalValue) OVER(PARTITION BY Segment) AS SegmentTotal FROM T
),
Report AS (
SELECT Segment,OwnerID,TotalValue,ValueRank,SegmentTotal,CAST(100.0*TotalValue/NULLIF(SegmentTotal,0) AS decimal(19,6)) AS SharePercent FROM R WHERE ValueRank<=2
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[SegmentTotal] AS [SegmentTotal],[SharePercent] AS [SharePercent] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 7 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "180.0000", "55.555555555555555555555555555555555555555555555556"], ["A", 4, "80.0000", 2, "180.0000", "44.444444444444444444444444444444444444444444444444"], ["B", 1, "320.0000", 1, "520.0000", "61.538461538461538461538461538461538461538461538462"], ["B", 4, "150.0000", 2, "520.0000", "28.846153846153846153846153846153846153846153846154"], ["C", 2, "400.0000", 1, "1000.0000", "40"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I06

**Every required segment**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Required AS (
SELECT N'A' AS Segment UNION ALL SELECT N'B' UNION ALL SELECT N'C'
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT t.OwnerID,t.EventCount,t.TotalValue FROM T t WHERE NOT EXISTS(SELECT 1 FROM Required r WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=t.OwnerID AND e.Kind=r.Segment))
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, 4, "530.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I07

**Prior calendar window**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.OwnerID,COUNT(p.MetricValue) AS PriorKnownCount,CAST(AVG(CAST(p.MetricValue AS decimal(28,6))) AS decimal(28,6)) AS PriorAverage FROM E c LEFT JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate GROUP BY c.EventID,c.OwnerID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[PriorKnownCount] AS [PriorKnownCount],[PriorAverage] AS [PriorAverage] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 0, null], [2, 1, 1, "100.0000"], [11, 1, 0, null], [3, 2, 0, null], [4, 2, 1, "200.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I08

**First and last known rows**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero participates;do not independently take the minimum value instead of the first row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT OwnerID,EventID,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS FirstPos,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate DESC,EventID DESC) AS LastPos FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT p.OwnerID,MAX(CASE WHEN k.FirstPos=1 THEN k.EventID END) AS FirstEventID,MAX(CASE WHEN k.LastPos=1 THEN k.EventID END) AS LastEventID FROM Owners p LEFT JOIN K k ON k.OwnerID=p.OwnerID GROUP BY p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[LastEventID] AS [LastEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 11], [2, 3, 12], [3, 5, 6], [4, 7, 10], [5, null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I09

**Complete 2024 calendar**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Each owner has exactly12 rows;2025 activity cannot enter2024.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Months AS (
SELECT CAST('20240101' AS date) AS MonthStart UNION ALL SELECT DATEADD(month,1,MonthStart) FROM Months WHERE MonthStart<'20241201'
),
T AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' GROUP BY OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1)
),
Report AS (
SELECT p.OwnerID,m.MonthStart,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p CROSS JOIN Months m LEFT JOIN T t ON t.OwnerID=p.OwnerID AND t.MonthStart=m.MonthStart
)
SELECT [OwnerID] AS [WarehouseID],[MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 60 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 2, 2, "300.0000"], [1, "2024-02-01", 0, 0, "0"], [1, "2024-03-01", 0, 0, "0"], [1, "2024-04-01", 0, 0, "0"], [1, "2024-05-01", 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I10

**Dominant segments**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The best of several negative totals is the least negative,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,Segment,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,Segment HAVING COUNT(MetricValue)>0
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY TotalValue DESC) AS ValueRank FROM T
),
Report AS (
SELECT OwnerID,Segment,TotalValue FROM R WHERE ValueRank=1
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "B", "320.0000"], [2, "C", "400.0000"], [3, "C", "300.0000"], [4, "C", "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I11

**Same-day repeated values**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,MetricValue,COUNT(*) AS Multiplicity FROM E GROUP BY OwnerID,ActivityDate,MetricValue HAVING COUNT(*)>=2
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Multiplicity] AS [Multiplicity] FROM Report ORDER BY WarehouseID,ActivityDate,MetricValue OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I12

**First threshold crossing**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Owners with no positive values produce no threshold crossing.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,SUM(MetricValue) OVER(PARTITION BY OwnerID) AS TotalValue FROM E WHERE MetricValue>0
),
C AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS Choice FROM R WHERE RunningValue>=0.8*TotalValue
),
Report AS (
SELECT OwnerID,EventID,RunningValue,TotalValue FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[RunningValue] AS [RunningValue],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, "420.0000", "420.0000"], [2, 12, "400.0000", "400.0000"], [3, 6, "350.0000", "350.0000"], [4, 9, "450.0000", "530.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I13

**Owner median**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. No known values gives count0 and null median,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue,EventID) AS Position,COUNT(*) OVER(PARTITION BY OwnerID) AS KnownCount FROM E WHERE MetricValue IS NOT NULL
),
T AS (
SELECT OwnerID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM K WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.KnownCount,0) AS KnownCount,t.MedianValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[KnownCount] AS [KnownCount],[MedianValue] AS [MedianValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, "120.0000"], [2, 2, "200.0000"], [3, 2, "175.0000"], [4, 4, "115.0000"], [5, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I14

**Two-generation comparison**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two joins cannot follow an excluded parent through to its grandparent.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,p.EventID AS ParentEventID,g.EventID AS GrandparentEventID,c.MetricValue,p.MetricValue AS ParentValue,g.MetricValue AS GrandparentValue FROM E c LEFT JOIN E p ON p.EventID=c.ParentID LEFT JOIN E g ON g.EventID=p.ParentID
)
SELECT [EventID] AS [MovementID],[ParentEventID] AS [ParentEventID],[GrandparentEventID] AS [GrandparentEventID],[MetricValue] AS [MetricValue],[ParentValue] AS [ParentValue],[GrandparentValue] AS [GrandparentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, null, "100.0000", null, null], [2, 1, null, "200.0000", "100.0000", null], [3, 1, null, "200.0000", "100.0000", null], [4, 2, 1, null, "200.0000", "100.0000"], [5, 2, 1, "50.0000", "200.0000", "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-I15

**Largest inactive gap**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-i15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
L AS (
SELECT OwnerID,ActivityDate AS EndDate,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS StartDate FROM D
),
R AS (
SELECT *,DATEDIFF(day,StartDate,EndDate) AS GapDays,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY DATEDIFF(day,StartDate,EndDate) DESC,StartDate) AS Choice FROM L WHERE StartDate IS NOT NULL
),
Report AS (
SELECT p.OwnerID,r.StartDate,r.EndDate,r.GapDays FROM Owners p LEFT JOIN R r ON r.OwnerID=p.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[GapDays] AS [GapDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", "2024-12-31", 364], [2, "2024-01-03", "2025-01-01", 364], [3, "2024-02-01", "2024-02-10", 9], [4, "2024-03-10", "2024-11-03", 238], [5, null, null, null]]
```

**Advanced:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A01

**Session boundaries and comparable recovery**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
L AS (
SELECT *,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousDate FROM E
),
S AS (
SELECT *,SUM(CASE WHEN PreviousDate IS NULL OR DATEDIFF(day,PreviousDate,ActivityDate)>30 THEN 1 ELSE 0 END) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS SessionNo FROM L
),
T AS (
SELECT OwnerID,SessionNo,MIN(ActivityDate) AS StartDate,MAX(ActivityDate) AS EndDate,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM S GROUP BY OwnerID,SessionNo
),
P AS (
SELECT *,LAG(TotalValue) OVER(PARTITION BY OwnerID ORDER BY SessionNo) AS PreviousValue FROM T
),
Report AS (
SELECT o.OwnerID,COALESCE(p.SessionNo,0) AS SessionNo,p.StartDate,p.EndDate,COALESCE(p.EventCount,0) AS EventCount,COALESCE(p.KnownCount,0) AS KnownCount,CASE WHEN p.SessionNo IS NULL THEN CAST(0 AS decimal(38,4)) ELSE p.TotalValue END AS TotalValue,p.PreviousValue,CAST(100.0*(p.TotalValue-p.PreviousValue)/NULLIF(p.PreviousValue,0) AS decimal(38,6)) AS GrowthPercent FROM Owners o LEFT JOIN P p ON p.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[SessionNo] AS [SessionNo],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[PreviousValue] AS [PreviousValue],[GrowthPercent] AS [GrowthPercent] FROM Report ORDER BY WarehouseID,SessionNo OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "2024-01-02", 2, 2, "300.0000", null, null], [1, 2, "2024-12-31", "2024-12-31", 1, 1, "120.0000", "300.0000", "-60"], [2, 1, "2024-01-02", "2024-01-03", 2, 1, "200.0000", null, null], [2, 2, "2025-01-01", "2025-01-01", 1, 1, "200.0000", "200.0000", "0"], [3, 1, "2024-02-01", "2024-02-10", 2, 2, "350.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A02

**Prior-window median anomaly**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
H AS (
SELECT c.EventID,p.EventID AS HistoryID,p.MetricValue,ROW_NUMBER() OVER(PARTITION BY c.EventID ORDER BY p.MetricValue,p.EventID) AS Position,COUNT(*) OVER(PARTITION BY c.EventID) AS KnownCount FROM E c JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate WHERE p.MetricValue IS NOT NULL
),
M AS (
SELECT EventID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM H WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY EventID
),
Report AS (
SELECT e.EventID,e.OwnerID,e.MetricValue,COALESCE(m.KnownCount,0) AS PriorKnownCount,m.MedianValue AS PriorMedian,CASE WHEN e.MetricValue>2*m.MedianValue THEN 1 ELSE 0 END AS IsAnomaly FROM E e LEFT JOIN M m ON m.EventID=e.EventID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PriorKnownCount] AS [PriorKnownCount],[PriorMedian] AS [PriorMedian],[IsAnomaly] AS [IsAnomaly] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", 0, null, 0], [2, 1, "200.0000", 1, "100.0000", 0], [11, 1, "120.0000", 0, null, 0], [3, 2, "200.0000", 0, null, 0], [4, 2, null, 1, "200.0000", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A03

**Smallest complete tie groups reaching80 percent**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
G AS (
SELECT Segment,TotalValue,CAST(SUM(TotalValue) AS decimal(28,4)) AS PeerTotal FROM T GROUP BY Segment,TotalValue
),
C AS (
SELECT *,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment ORDER BY TotalValue DESC ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS CumulativeValue,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank FROM G
),
Report AS (
SELECT t.Segment,t.OwnerID,t.TotalValue,c.ValueRank,c.CumulativeValue,c.SegmentTotal FROM T t JOIN C c ON c.Segment=t.Segment AND c.TotalValue=t.TotalValue WHERE c.CumulativeValue-c.PeerTotal<0.8*c.SegmentTotal
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[CumulativeValue] AS [CumulativeValue],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 7 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "100.0000", "180.0000"], ["A", 4, "80.0000", 2, "180.0000", "180.0000"], ["B", 1, "320.0000", 1, "320.0000", "520.0000"], ["B", 4, "150.0000", 2, "470.0000", "520.0000"], ["C", 2, "400.0000", 1, "400.0000", "1000.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A04

**Six-month cohort retention**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
FirstSeen AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(MIN(ActivityDate)),MONTH(MIN(ActivityDate)),1) AS CohortMonth FROM E GROUP BY OwnerID
),
C AS (
SELECT * FROM FirstSeen WHERE CohortMonth>='20240101' AND CohortMonth<'20250101'
),
N AS (
SELECT 0 AS MonthOffset UNION ALL SELECT MonthOffset+1 FROM N WHERE MonthOffset<5
),
A AS (
SELECT DISTINCT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS ActivityMonth FROM E
),
Report AS (
SELECT c.CohortMonth,n.MonthOffset,DATEADD(month,n.MonthOffset,c.CohortMonth) AS ActivityMonth,COUNT(*) AS CohortSize,COUNT(a.OwnerID) AS ActiveOwners,CAST(100.0*COUNT(a.OwnerID)/COUNT(*) AS decimal(19,6)) AS RetentionPercent FROM C c CROSS JOIN N n LEFT JOIN A a ON a.OwnerID=c.OwnerID AND a.ActivityMonth=DATEADD(month,n.MonthOffset,c.CohortMonth) GROUP BY c.CohortMonth,n.MonthOffset
)
SELECT [CohortMonth] AS [CohortMonth],[MonthOffset] AS [MonthOffset],[ActivityMonth] AS [ActivityMonth],[CohortSize] AS [CohortSize],[ActiveOwners] AS [ActiveOwners],[RetentionPercent] AS [RetentionPercent] FROM Report ORDER BY CohortMonth,MonthOffset OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 0, "2024-01-01", 2, 2, "100"], ["2024-01-01", 1, "2024-02-01", 2, 0, "0"], ["2024-01-01", 2, "2024-03-01", 2, 0, "0"], ["2024-01-01", 3, "2024-04-01", 2, 0, "0"], ["2024-01-01", 4, "2024-05-01", 2, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A05

**Longest activity run with one missing day**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
N AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS Position FROM D
),
C AS (
SELECT s.OwnerID,s.ActivityDate AS StartDate,e.ActivityDate AS EndDate,e.Position-s.Position+1 AS ActiveDays,DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1) AS MissingDays FROM N s JOIN N e ON e.OwnerID=s.OwnerID AND e.Position>=s.Position WHERE DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1)<=1
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActiveDays DESC,StartDate,EndDate) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartDate,r.EndDate,COALESCE(r.ActiveDays,0) AS ActiveDays,COALESCE(r.MissingDays,0) AS MissingDays FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[ActiveDays] AS [ActiveDays],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", "2024-01-02", 2, 0], [2, "2024-01-02", "2024-01-03", 2, 0], [3, "2024-02-01", "2024-02-01", 1, 0], [4, "2024-02-29", "2024-03-01", 2, 0], [5, null, null, 0, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A06

**Cycle-safe parent resolution**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Walk AS (
SELECT EventID AS StartID,EventID AS CurrentID,ParentID AS NextID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT w.StartID,e.EventID,e.ParentID,CAST(w.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),w.Depth+1 FROM Walk w JOIN E e ON e.EventID=w.NextID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',w.VisitPath)=0 AND w.Depth<100
),
Terminal AS (
SELECT w.*,CASE WHEN w.NextID IS NOT NULL AND CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 THEN 1 ELSE 0 END AS CycleFlag,CASE WHEN w.NextID IS NOT NULL AND NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID) THEN 1 ELSE 0 END AS BoundaryFlag FROM Walk w WHERE w.NextID IS NULL OR CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 OR NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID)
),
Report AS (
SELECT StartID AS EventID,CurrentID AS TerminalEventID,CASE WHEN NextID IS NULL THEN CurrentID END AS RootEventID,Depth,CycleFlag,BoundaryFlag,VisitPath FROM Terminal
)
SELECT [EventID] AS [MovementID],[TerminalEventID] AS [TerminalEventID],[RootEventID] AS [RootEventID],[Depth] AS [Depth],[CycleFlag] AS [CycleFlag],[BoundaryFlag] AS [BoundaryFlag],[VisitPath] AS [VisitPath] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, 0, 0, 0, "/1/"], [2, 1, 1, 1, 0, 0, "/2/1/"], [3, 1, 1, 1, 0, 0, "/3/1/"], [4, 1, 1, 2, 0, 0, "/4/2/1/"], [5, 1, 1, 2, 0, 0, "/5/2/1/"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A07

**As-of correction-chain survivors**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Versions AS (
SELECT EventID AS RootID,EventID,ActivityDate,MetricValue,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E WHERE ParentID IS NULL UNION ALL SELECT v.RootID,e.EventID,e.ActivityDate,e.MetricValue,CAST(v.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),v.Depth+1 FROM Versions v JOIN E e ON e.ParentID=v.EventID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',v.VisitPath)=0 AND v.Depth<100
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY RootID ORDER BY ActivityDate DESC,EventID DESC) AS Choice FROM Versions WHERE ActivityDate<='20241231'
),
Report AS (
SELECT e.EventID AS RootEventID,r.EventID AS SelectedEventID,r.ActivityDate,r.MetricValue,r.Depth FROM E e LEFT JOIN R r ON r.RootID=e.EventID AND r.Choice=1 WHERE e.ParentID IS NULL
)
SELECT [RootEventID] AS [RootEventID],[SelectedEventID] AS [SelectedEventID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Depth] AS [Depth] FROM Report ORDER BY RootEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, "2024-12-31", "120.0000", 3]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A08

**FIFO interval allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Supply AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='A' AND MetricValue>0
),
Demand AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='B' AND MetricValue>0
),
Matches AS (
SELECT s.OwnerID,s.EventID AS SupplyEventID,d.EventID AS DemandEventID,(CASE WHEN s.EndValue<d.EndValue THEN s.EndValue ELSE d.EndValue END)-(CASE WHEN s.EndValue-s.MetricValue>d.EndValue-d.MetricValue THEN s.EndValue-s.MetricValue ELSE d.EndValue-d.MetricValue END) AS AllocatedValue FROM Supply s JOIN Demand d ON d.OwnerID=s.OwnerID AND s.EndValue>d.EndValue-d.MetricValue AND d.EndValue>s.EndValue-s.MetricValue
),
Result AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,CAST(0 AS decimal(38,4)) AS UnmatchedValue FROM Matches UNION ALL SELECT s.OwnerID,s.EventID,NULL,0,s.MetricValue-COALESCE(x.UsedValue,0) FROM Supply s LEFT JOIN(SELECT SupplyEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY SupplyEventID)x ON x.SupplyEventID=s.EventID WHERE s.MetricValue>COALESCE(x.UsedValue,0) UNION ALL SELECT d.OwnerID,NULL,d.EventID,0,d.MetricValue-COALESCE(x.UsedValue,0) FROM Demand d LEFT JOIN(SELECT DemandEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY DemandEventID)x ON x.DemandEventID=d.EventID WHERE d.MetricValue>COALESCE(x.UsedValue,0)
),
Report AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,UnmatchedValue FROM Result
)
SELECT [OwnerID] AS [WarehouseID],[SupplyEventID] AS [SupplyEventID],[DemandEventID] AS [DemandEventID],[AllocatedValue] AS [AllocatedValue],[UnmatchedValue] AS [UnmatchedValue] FROM Report ORDER BY WarehouseID,SupplyEventID,DemandEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, 2, "0", "100.0000"], [1, null, 11, "0", "120.0000"], [1, 1, 2, "100.0000", "0"], [3, null, 5, "0", "50.0000"], [4, null, 8, "0", "70.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A09

**Conserved largest-remainder allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
W AS (
SELECT *,CAST(SUM(TotalValue) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal FROM T
),
Units AS (
SELECT *,CAST(TotalValue*10000 AS decimal(28,0)) AS TotalUnits,CAST(SegmentTotal*10000 AS decimal(28,0)) AS SegmentUnits FROM W
),
Numerators AS (
SELECT *,CAST(TotalUnits*10000 AS decimal(33,0)) AS NumeratorUnits FROM Units
),
Remainders AS (
SELECT *,NumeratorUnits%SegmentUnits AS RemainderUnits FROM Numerators
),
Bases AS (
SELECT *,CAST((NumeratorUnits-RemainderUnits)/SegmentUnits AS int) AS BasePoints FROM Remainders
),
R AS (
SELECT *,10000-SUM(BasePoints) OVER(PARTITION BY Segment) AS RemainingPoints,ROW_NUMBER() OVER(PARTITION BY Segment ORDER BY RemainderUnits DESC,OwnerID) AS RemainderPosition FROM Bases
),
Report AS (
SELECT Segment,OwnerID,TotalValue,BasePoints+CASE WHEN RemainderPosition<=RemainingPoints THEN 1 ELSE 0 END AS BasisPoints,SegmentTotal FROM R
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[BasisPoints] AS [BasisPoints],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 5556, "180.0000"], ["A", 4, "80.0000", 4444, "180.0000"], ["B", 1, "320.0000", 6154, "520.0000"], ["B", 3, "50.0000", 961, "520.0000"], ["B", 4, "150.0000", 2885, "520.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A10

**Complete inactivity intervals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' UNION SELECT OwnerID,CAST('20231231' AS date) FROM Owners UNION SELECT OwnerID,CAST('20250101' AS date) FROM Owners
),
L AS (
SELECT OwnerID,ActivityDate,LEAD(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS NextDate FROM D
),
Report AS (
SELECT OwnerID,DATEADD(day,1,ActivityDate) AS StartDate,DATEADD(day,-1,NextDate) AS EndDate,DATEDIFF(day,ActivityDate,NextDate)-1 AS MissingDays FROM L WHERE DATEDIFF(day,ActivityDate,NextDate)>1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID,StartDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 11 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-03", "2024-12-30", 363], [2, "2024-01-01", "2024-01-01", 1], [2, "2024-01-04", "2024-12-31", 363], [3, "2024-01-01", "2024-01-31", 31], [3, "2024-02-02", "2024-02-09", 8]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A11

**Ordered three-stage funnel**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
C AS (
SELECT a.OwnerID,a.EventID AS FirstEventID,b.EventID AS SecondEventID,c.EventID AS ThirdEventID,a.ActivityDate AS StartDate,c.ActivityDate AS EndDate,ROW_NUMBER() OVER(PARTITION BY a.OwnerID ORDER BY c.ActivityDate,c.EventID,b.ActivityDate DESC,b.EventID DESC,a.ActivityDate DESC,a.EventID DESC) AS Choice FROM E a JOIN E b ON b.OwnerID=a.OwnerID AND (b.ActivityDate>a.ActivityDate OR(b.ActivityDate=a.ActivityDate AND b.EventID>a.EventID)) JOIN E c ON c.OwnerID=b.OwnerID AND (c.ActivityDate>b.ActivityDate OR(c.ActivityDate=b.ActivityDate AND c.EventID>b.EventID)) WHERE a.Kind='A' AND b.Kind='B' AND c.Kind='C'
),
Report AS (
SELECT OwnerID,FirstEventID,SecondEventID,ThirdEventID,StartDate,EndDate FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[SecondEventID] AS [SecondEventID],[ThirdEventID] AS [ThirdEventID],[StartDate] AS [StartDate],[EndDate] AS [EndDate] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, 7, 8, 9, "2024-02-29", "2024-03-10"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A12

**Earliest rolling coverage with witnesses**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate AS TriggerDate FROM E
),
W AS (
SELECT d.OwnerID,d.TriggerDate,e.Kind AS Segment,e.EventID,ROW_NUMBER() OVER(PARTITION BY d.OwnerID,d.TriggerDate,e.Kind ORDER BY e.ActivityDate DESC,e.EventID DESC) AS Position FROM D d JOIN E e ON e.OwnerID=d.OwnerID AND e.ActivityDate>=DATEADD(day,-29,d.TriggerDate) AND e.ActivityDate<=d.TriggerDate WHERE e.Kind IN('A','B','C')
),
P AS (
SELECT OwnerID,TriggerDate,MAX(CASE WHEN Segment='A' THEN EventID END) AS AEventID,MAX(CASE WHEN Segment='B' THEN EventID END) AS BEventID,MAX(CASE WHEN Segment='C' THEN EventID END) AS CEventID FROM W WHERE Position=1 GROUP BY OwnerID,TriggerDate HAVING COUNT(*)=3
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY TriggerDate) AS Choice FROM P
),
Report AS (
SELECT OwnerID,TriggerDate,AEventID,BEventID,CEventID FROM R WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[TriggerDate] AS [TriggerDate],[AEventID] AS [AEventID],[BEventID] AS [BEventID],[CEventID] AS [CEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, "2024-03-10", 7, 8, 9]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A13

**Distinct descendant exposure with cycles**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Down AS (
SELECT EventID AS StartID,EventID AS NodeID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT d.StartID,e.EventID,CAST(d.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),d.Depth+1 FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)=0 AND d.Depth<100
),
DistinctNodes AS (
SELECT DISTINCT StartID,NodeID FROM Down WHERE Depth>0
),
T AS (
SELECT d.StartID,COUNT(*) AS DescendantCount,COUNT(e.MetricValue) AS KnownCount,SUM(e.MetricValue) AS TotalValue FROM DistinctNodes d JOIN E e ON e.EventID=d.NodeID GROUP BY d.StartID
),
Cycles AS (
SELECT DISTINCT d.StartID FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)>0
),
Report AS (
SELECT e.EventID,COALESCE(t.DescendantCount,0) AS DescendantCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.StartID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,CASE WHEN c.StartID IS NULL THEN 0 ELSE 1 END AS CycleFlag FROM E e LEFT JOIN T t ON t.StartID=e.EventID LEFT JOIN Cycles c ON c.StartID=e.EventID
)
SELECT [EventID] AS [MovementID],[DescendantCount] AS [DescendantCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[CycleFlag] AS [CycleFlag] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, 10, "1600.0000", 0], [2, 6, 5, "700.0000", 0], [3, 3, 3, "500.0000", 0], [4, 2, 2, "450.0000", 0], [5, 2, 2, "200.0000", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A14

**Best mean-centered contiguous block**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
OwnerStats AS (
SELECT OwnerID,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS KnownTotal FROM E GROUP BY OwnerID
),
N AS (
SELECT e.*,CAST(s.KnownCount AS decimal(4,0))*e.MetricValue-CAST(s.KnownTotal AS decimal(28,4)) AS ScoreValue,ROW_NUMBER() OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID) AS Position,SUM(CASE WHEN e.MetricValue IS NULL THEN 1 ELSE 0 END) OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID ROWS UNBOUNDED PRECEDING) AS BlockID FROM E e JOIN OwnerStats s ON s.OwnerID=e.OwnerID
),
P AS (
SELECT *,CAST(SUM(ScoreValue) OVER(PARTITION BY OwnerID,BlockID ORDER BY Position ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS PrefixValue FROM N WHERE MetricValue IS NOT NULL
),
C AS (
SELECT s.OwnerID,s.EventID AS StartEventID,e.EventID AS EndEventID,s.Position AS StartPosition,e.Position AS EndPosition,e.PrefixValue-s.PrefixValue+s.ScoreValue AS BlockScore,e.Position-s.Position+1 AS EventCount FROM P s JOIN P e ON e.OwnerID=s.OwnerID AND e.BlockID=s.BlockID AND e.Position>=s.Position
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY BlockScore DESC,StartPosition,EndPosition) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartEventID,r.EndEventID,r.BlockScore,COALESCE(r.EventCount,0) AS EventCount FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartEventID] AS [StartEventID],[EndEventID] AS [EndEventID],[BlockScore] AS [BlockScore],[EventCount] AS [EventCount] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "180.0000", 1], [2, 3, 3, "0.0000", 1], [3, 6, 6, "250.0000", 1], [4, 8, 9, "740.0000", 2], [5, null, null, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-02-A15

**Five-table reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-02-a15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NOT NULL UNION ALL SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [MovementValue] IS NULL
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Eligible AS (
SELECT f.* FROM [retail_supply_chain].[StockMovements] f JOIN E e ON e.EventID=f.[MovementID]
),
HeaderTotals AS (
SELECT [WarehouseID] AS OwnerID,COUNT(*) AS EventCount,COUNT([MovementValue]) AS KnownCount,SUM([MovementValue]) AS TotalValue FROM Eligible GROUP BY [WarehouseID]
),
Net AS (
SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM Eligible GROUP BY WarehouseID,ProductID
),
Balances AS (
SELECT b.WarehouseID AS OwnerID,SUM(b.OpeningQuantity) AS OpeningUnits,SUM(b.QuantityOnHand) AS StoredUnits,SUM(COALESCE(n.NetUnits,0)) AS SelectedNetUnits,SUM(b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0))) AS QuantityDifference,SUM(b.QuantityOnHand*p.UnitCost) AS StandardStockValue FROM retail_supply_chain.StockBalances b JOIN retail_supply_chain.Products p ON p.ProductID=b.ProductID LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID GROUP BY b.WarehouseID
),
Missing AS (
SELECT n.WarehouseID AS OwnerID,COUNT(*) AS MissingBalancePairs FROM Net n WHERE NOT EXISTS(SELECT 1 FROM retail_supply_chain.StockBalances b WHERE b.WarehouseID=n.WarehouseID AND b.ProductID=n.ProductID) GROUP BY n.WarehouseID
),
SupplierLead AS (
SELECT e.WarehouseID AS OwnerID,MAX(s.LeadTimeDays) AS MaxLeadTimeDays FROM Eligible e JOIN retail_supply_chain.Suppliers s ON s.SupplierID=e.SupplierID GROUP BY e.WarehouseID
),
Report AS (
SELECT o.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.OwnerID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,COALESCE(b.OpeningUnits,0) AS OpeningUnits,COALESCE(b.StoredUnits,0) AS StoredUnits,COALESCE(b.SelectedNetUnits,0) AS SelectedNetUnits,COALESCE(b.QuantityDifference,0) AS QuantityDifference,COALESCE(b.StandardStockValue,0) AS StandardStockValue,COALESCE(m.MissingBalancePairs,0) AS MissingBalancePairs,l.MaxLeadTimeDays FROM Owners o LEFT JOIN HeaderTotals t ON t.OwnerID=o.OwnerID LEFT JOIN Balances b ON b.OwnerID=o.OwnerID LEFT JOIN Missing m ON m.OwnerID=o.OwnerID LEFT JOIN SupplierLead l ON l.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[OpeningUnits] AS [OpeningUnits],[StoredUnits] AS [StoredUnits],[SelectedNetUnits] AS [SelectedNetUnits],[QuantityDifference] AS [QuantityDifference],[StandardStockValue] AS [StandardStockValue],[MissingBalancePairs] AS [MissingBalancePairs],[MaxLeadTimeDays] AS [MaxLeadTimeDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 3, 3, "420", "40", "36", "-4", "0", "327", 0, 3], [2, 3, 2, "400", "20", "31", "11", "0", "483", 0, 1], [3, 2, 2, "350", "20", "21", "1", "0", "138", 0, 3], [4, 4, 4, "530", "40", "42", "2", "0", "449", 0, 3], [5, 0, 0, "0", "0", "0", "0", "0", "0", 0, null]]
```

### Intersect: progression

**Beginner:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B01

**Analysis audit**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Keep null values and stored token spaces.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,Segment FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Segment] AS [Segment] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "A"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B02

**Known versus unknown**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero is not unknown.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,MetricValue FROM E WHERE MetricValue IS NOT NULL
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B03

**Unknown-value queue**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An empty queue must have the requested columns.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,ActivityDate FROM E WHERE MetricValue IS NULL
)
SELECT [EventID] AS [MovementID],[ActivityDate] AS [ActivityDate] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B04

**Threshold review**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The lower bound is inclusive;unknown values cannot pass.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,MetricValue FROM E WHERE MetricValue>=100
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B05

**Deterministic shortlist**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return fewer than five if fewer qualify;ties do not expand the result.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT TOP (5) EventID,MetricValue FROM E WHERE MetricValue IS NOT NULL ORDER BY MetricValue DESC,EventID
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MetricValue DESC,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B06

**Active-owner totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown owner has null total,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B07

**All-owner coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Count real activity,not an outer-join placeholder.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, "100.0000"], [2, 0, 0, "0"], [3, 0, 0, "0"], [4, 0, 0, "0"], [5, 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B08

**Segment profile**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Use SQL Server collation equality for segment grouping.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, 1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B09

**Owner segment coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated activity in one segment does not duplicate its owner/segment pair.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT DISTINCT OwnerID,Segment FROM E
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "A"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B10

**Observed-month totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not fabricate missing months in this question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
M AS (
SELECT DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,MetricValue FROM E
),
Report AS (
SELECT MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM M GROUP BY MonthStart
)
SELECT [MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 1, 1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B11

**Daily workload**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Different source rows on the same day remain separate contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,ActivityDate
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,ActivityDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 1, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B12

**No eligible activity**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An owner with an unknown-value row is active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT p.OwnerID FROM Owners p WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=p.OwnerID)
)
SELECT [OwnerID] AS [WarehouseID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2], [3], [4], [5]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B13

**Visible parent link**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A parent excluded by the analysis eligibility rule is not visible here.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.ParentID,c.MetricValue AS ChildValue,p.MetricValue AS ParentValue FROM E c JOIN E p ON p.EventID=c.ParentID
)
SELECT [EventID] AS [MovementID],[ParentID] AS [ParentID],[ChildValue] AS [ChildValue],[ParentValue] AS [ParentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B14

**Bounded-value counts**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return0 for a segment with no values in the interval.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,SUM(CASE WHEN MetricValue BETWEEN 100 AND 200 THEN 1 ELSE 0 END) AS InRangeCount FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[InRangeCount] AS [InRangeCount] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-B15

**Value sign reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-b15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. All four classes must sum to EventCount;empty input returns five zero counts.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT COUNT(*) AS EventCount,COUNT(*)-COUNT(MetricValue) AS UnknownCount,COALESCE(SUM(CASE WHEN MetricValue<0 THEN 1 ELSE 0 END),0) AS NegativeCount,COALESCE(SUM(CASE WHEN MetricValue=0 THEN 1 ELSE 0 END),0) AS ZeroCount,COALESCE(SUM(CASE WHEN MetricValue>0 THEN 1 ELSE 0 END),0) AS PositiveCount FROM E
)
SELECT [EventCount] AS [EventCount],[UnknownCount] AS [UnknownCount],[NegativeCount] AS [NegativeCount],[ZeroCount] AS [ZeroCount],[PositiveCount] AS [PositiveCount] FROM Report ORDER BY EventCount OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 0, 0, 0, 1]]
```

**Intermediate:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I01

**Exactly two per owner**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Ties cannot expand a two-row limit.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC,EventID) AS Position FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,Position FROM R WHERE Position<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[Position] AS [Position] FROM Report ORDER BY WarehouseID,Position OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I02

**Two value positions with ties**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Several rows may share rank2;all must remain.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC) AS ValueRank FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,ValueRank FROM R WHERE ValueRank<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[ValueRank] AS [ValueRank] FROM Report ORDER BY WarehouseID,ValueRank,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I03

**Running value and knowledge**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown prefix has null RunningValue.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,COUNT(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningKnownCount FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[RunningValue] AS [RunningValue],[RunningKnownCount] AS [RunningKnownCount] FROM Report ORDER BY WarehouseID,ActivityDate,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", "100.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I04

**Previous row delta**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not skip an unknown predecessor.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
P AS (
SELECT *,LAG(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousValue FROM E
),
Report AS (
SELECT EventID,OwnerID,MetricValue,PreviousValue,MetricValue-PreviousValue AS Delta FROM P
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PreviousValue] AS [PreviousValue],[Delta] AS [Delta] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I05

**Share before filtering**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Filtered-out owners must still contribute to the denominator.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,SUM(MetricValue) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank,SUM(TotalValue) OVER(PARTITION BY Segment) AS SegmentTotal FROM T
),
Report AS (
SELECT Segment,OwnerID,TotalValue,ValueRank,SegmentTotal,CAST(100.0*TotalValue/NULLIF(SegmentTotal,0) AS decimal(19,6)) AS SharePercent FROM R WHERE ValueRank<=2
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[SegmentTotal] AS [SegmentTotal],[SharePercent] AS [SharePercent] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "100.0000", "100"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I06

**Every required segment**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Required AS (
SELECT N'A' AS Segment UNION ALL SELECT N'B' UNION ALL SELECT N'C'
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT t.OwnerID,t.EventCount,t.TotalValue FROM T t WHERE NOT EXISTS(SELECT 1 FROM Required r WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=t.OwnerID AND e.Kind=r.Segment))
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I07

**Prior calendar window**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.OwnerID,COUNT(p.MetricValue) AS PriorKnownCount,CAST(AVG(CAST(p.MetricValue AS decimal(28,6))) AS decimal(28,6)) AS PriorAverage FROM E c LEFT JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate GROUP BY c.EventID,c.OwnerID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[PriorKnownCount] AS [PriorKnownCount],[PriorAverage] AS [PriorAverage] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I08

**First and last known rows**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero participates;do not independently take the minimum value instead of the first row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT OwnerID,EventID,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS FirstPos,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate DESC,EventID DESC) AS LastPos FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT p.OwnerID,MAX(CASE WHEN k.FirstPos=1 THEN k.EventID END) AS FirstEventID,MAX(CASE WHEN k.LastPos=1 THEN k.EventID END) AS LastEventID FROM Owners p LEFT JOIN K k ON k.OwnerID=p.OwnerID GROUP BY p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[LastEventID] AS [LastEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1], [2, null, null], [3, null, null], [4, null, null], [5, null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I09

**Complete 2024 calendar**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Each owner has exactly12 rows;2025 activity cannot enter2024.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Months AS (
SELECT CAST('20240101' AS date) AS MonthStart UNION ALL SELECT DATEADD(month,1,MonthStart) FROM Months WHERE MonthStart<'20241201'
),
T AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' GROUP BY OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1)
),
Report AS (
SELECT p.OwnerID,m.MonthStart,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p CROSS JOIN Months m LEFT JOIN T t ON t.OwnerID=p.OwnerID AND t.MonthStart=m.MonthStart
)
SELECT [OwnerID] AS [WarehouseID],[MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 60 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 1, 1, "100.0000"], [1, "2024-02-01", 0, 0, "0"], [1, "2024-03-01", 0, 0, "0"], [1, "2024-04-01", 0, 0, "0"], [1, "2024-05-01", 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I10

**Dominant segments**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The best of several negative totals is the least negative,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,Segment,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,Segment HAVING COUNT(MetricValue)>0
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY TotalValue DESC) AS ValueRank FROM T
),
Report AS (
SELECT OwnerID,Segment,TotalValue FROM R WHERE ValueRank=1
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "A", "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I11

**Same-day repeated values**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,MetricValue,COUNT(*) AS Multiplicity FROM E GROUP BY OwnerID,ActivityDate,MetricValue HAVING COUNT(*)>=2
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Multiplicity] AS [Multiplicity] FROM Report ORDER BY WarehouseID,ActivityDate,MetricValue OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I12

**First threshold crossing**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Owners with no positive values produce no threshold crossing.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,SUM(MetricValue) OVER(PARTITION BY OwnerID) AS TotalValue FROM E WHERE MetricValue>0
),
C AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS Choice FROM R WHERE RunningValue>=0.8*TotalValue
),
Report AS (
SELECT OwnerID,EventID,RunningValue,TotalValue FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[RunningValue] AS [RunningValue],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I13

**Owner median**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. No known values gives count0 and null median,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue,EventID) AS Position,COUNT(*) OVER(PARTITION BY OwnerID) AS KnownCount FROM E WHERE MetricValue IS NOT NULL
),
T AS (
SELECT OwnerID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM K WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.KnownCount,0) AS KnownCount,t.MedianValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[KnownCount] AS [KnownCount],[MedianValue] AS [MedianValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000"], [2, 0, null], [3, 0, null], [4, 0, null], [5, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I14

**Two-generation comparison**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two joins cannot follow an excluded parent through to its grandparent.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,p.EventID AS ParentEventID,g.EventID AS GrandparentEventID,c.MetricValue,p.MetricValue AS ParentValue,g.MetricValue AS GrandparentValue FROM E c LEFT JOIN E p ON p.EventID=c.ParentID LEFT JOIN E g ON g.EventID=p.ParentID
)
SELECT [EventID] AS [MovementID],[ParentEventID] AS [ParentEventID],[GrandparentEventID] AS [GrandparentEventID],[MetricValue] AS [MetricValue],[ParentValue] AS [ParentValue],[GrandparentValue] AS [GrandparentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, null, "100.0000", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-I15

**Largest inactive gap**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-i15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
L AS (
SELECT OwnerID,ActivityDate AS EndDate,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS StartDate FROM D
),
R AS (
SELECT *,DATEDIFF(day,StartDate,EndDate) AS GapDays,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY DATEDIFF(day,StartDate,EndDate) DESC,StartDate) AS Choice FROM L WHERE StartDate IS NOT NULL
),
Report AS (
SELECT p.OwnerID,r.StartDate,r.EndDate,r.GapDays FROM Owners p LEFT JOIN R r ON r.OwnerID=p.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[GapDays] AS [GapDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, null, null], [2, null, null, null], [3, null, null, null], [4, null, null, null], [5, null, null, null]]
```

**Advanced:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A01

**Session boundaries and comparable recovery**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
L AS (
SELECT *,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousDate FROM E
),
S AS (
SELECT *,SUM(CASE WHEN PreviousDate IS NULL OR DATEDIFF(day,PreviousDate,ActivityDate)>30 THEN 1 ELSE 0 END) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS SessionNo FROM L
),
T AS (
SELECT OwnerID,SessionNo,MIN(ActivityDate) AS StartDate,MAX(ActivityDate) AS EndDate,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM S GROUP BY OwnerID,SessionNo
),
P AS (
SELECT *,LAG(TotalValue) OVER(PARTITION BY OwnerID ORDER BY SessionNo) AS PreviousValue FROM T
),
Report AS (
SELECT o.OwnerID,COALESCE(p.SessionNo,0) AS SessionNo,p.StartDate,p.EndDate,COALESCE(p.EventCount,0) AS EventCount,COALESCE(p.KnownCount,0) AS KnownCount,CASE WHEN p.SessionNo IS NULL THEN CAST(0 AS decimal(38,4)) ELSE p.TotalValue END AS TotalValue,p.PreviousValue,CAST(100.0*(p.TotalValue-p.PreviousValue)/NULLIF(p.PreviousValue,0) AS decimal(38,6)) AS GrowthPercent FROM Owners o LEFT JOIN P p ON p.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[SessionNo] AS [SessionNo],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[PreviousValue] AS [PreviousValue],[GrowthPercent] AS [GrowthPercent] FROM Report ORDER BY WarehouseID,SessionNo OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "2024-01-01", 1, 1, "100.0000", null, null], [2, 0, null, null, 0, 0, "0", null, null], [3, 0, null, null, 0, 0, "0", null, null], [4, 0, null, null, 0, 0, "0", null, null], [5, 0, null, null, 0, 0, "0", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A02

**Prior-window median anomaly**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
H AS (
SELECT c.EventID,p.EventID AS HistoryID,p.MetricValue,ROW_NUMBER() OVER(PARTITION BY c.EventID ORDER BY p.MetricValue,p.EventID) AS Position,COUNT(*) OVER(PARTITION BY c.EventID) AS KnownCount FROM E c JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate WHERE p.MetricValue IS NOT NULL
),
M AS (
SELECT EventID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM H WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY EventID
),
Report AS (
SELECT e.EventID,e.OwnerID,e.MetricValue,COALESCE(m.KnownCount,0) AS PriorKnownCount,m.MedianValue AS PriorMedian,CASE WHEN e.MetricValue>2*m.MedianValue THEN 1 ELSE 0 END AS IsAnomaly FROM E e LEFT JOIN M m ON m.EventID=e.EventID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PriorKnownCount] AS [PriorKnownCount],[PriorMedian] AS [PriorMedian],[IsAnomaly] AS [IsAnomaly] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "100.0000", 0, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A03

**Smallest complete tie groups reaching80 percent**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
G AS (
SELECT Segment,TotalValue,CAST(SUM(TotalValue) AS decimal(28,4)) AS PeerTotal FROM T GROUP BY Segment,TotalValue
),
C AS (
SELECT *,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment ORDER BY TotalValue DESC ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS CumulativeValue,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank FROM G
),
Report AS (
SELECT t.Segment,t.OwnerID,t.TotalValue,c.ValueRank,c.CumulativeValue,c.SegmentTotal FROM T t JOIN C c ON c.Segment=t.Segment AND c.TotalValue=t.TotalValue WHERE c.CumulativeValue-c.PeerTotal<0.8*c.SegmentTotal
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[CumulativeValue] AS [CumulativeValue],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 1, "100.0000", "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A04

**Six-month cohort retention**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
FirstSeen AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(MIN(ActivityDate)),MONTH(MIN(ActivityDate)),1) AS CohortMonth FROM E GROUP BY OwnerID
),
C AS (
SELECT * FROM FirstSeen WHERE CohortMonth>='20240101' AND CohortMonth<'20250101'
),
N AS (
SELECT 0 AS MonthOffset UNION ALL SELECT MonthOffset+1 FROM N WHERE MonthOffset<5
),
A AS (
SELECT DISTINCT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS ActivityMonth FROM E
),
Report AS (
SELECT c.CohortMonth,n.MonthOffset,DATEADD(month,n.MonthOffset,c.CohortMonth) AS ActivityMonth,COUNT(*) AS CohortSize,COUNT(a.OwnerID) AS ActiveOwners,CAST(100.0*COUNT(a.OwnerID)/COUNT(*) AS decimal(19,6)) AS RetentionPercent FROM C c CROSS JOIN N n LEFT JOIN A a ON a.OwnerID=c.OwnerID AND a.ActivityMonth=DATEADD(month,n.MonthOffset,c.CohortMonth) GROUP BY c.CohortMonth,n.MonthOffset
)
SELECT [CohortMonth] AS [CohortMonth],[MonthOffset] AS [MonthOffset],[ActivityMonth] AS [ActivityMonth],[CohortSize] AS [CohortSize],[ActiveOwners] AS [ActiveOwners],[RetentionPercent] AS [RetentionPercent] FROM Report ORDER BY CohortMonth,MonthOffset OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 0, "2024-01-01", 1, 1, "100"], ["2024-01-01", 1, "2024-02-01", 1, 0, "0"], ["2024-01-01", 2, "2024-03-01", 1, 0, "0"], ["2024-01-01", 3, "2024-04-01", 1, 0, "0"], ["2024-01-01", 4, "2024-05-01", 1, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A05

**Longest activity run with one missing day**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
N AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS Position FROM D
),
C AS (
SELECT s.OwnerID,s.ActivityDate AS StartDate,e.ActivityDate AS EndDate,e.Position-s.Position+1 AS ActiveDays,DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1) AS MissingDays FROM N s JOIN N e ON e.OwnerID=s.OwnerID AND e.Position>=s.Position WHERE DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1)<=1
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActiveDays DESC,StartDate,EndDate) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartDate,r.EndDate,COALESCE(r.ActiveDays,0) AS ActiveDays,COALESCE(r.MissingDays,0) AS MissingDays FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[ActiveDays] AS [ActiveDays],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", "2024-01-01", 1, 0], [2, null, null, 0, 0], [3, null, null, 0, 0], [4, null, null, 0, 0], [5, null, null, 0, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A06

**Cycle-safe parent resolution**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Walk AS (
SELECT EventID AS StartID,EventID AS CurrentID,ParentID AS NextID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT w.StartID,e.EventID,e.ParentID,CAST(w.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),w.Depth+1 FROM Walk w JOIN E e ON e.EventID=w.NextID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',w.VisitPath)=0 AND w.Depth<100
),
Terminal AS (
SELECT w.*,CASE WHEN w.NextID IS NOT NULL AND CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 THEN 1 ELSE 0 END AS CycleFlag,CASE WHEN w.NextID IS NOT NULL AND NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID) THEN 1 ELSE 0 END AS BoundaryFlag FROM Walk w WHERE w.NextID IS NULL OR CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 OR NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID)
),
Report AS (
SELECT StartID AS EventID,CurrentID AS TerminalEventID,CASE WHEN NextID IS NULL THEN CurrentID END AS RootEventID,Depth,CycleFlag,BoundaryFlag,VisitPath FROM Terminal
)
SELECT [EventID] AS [MovementID],[TerminalEventID] AS [TerminalEventID],[RootEventID] AS [RootEventID],[Depth] AS [Depth],[CycleFlag] AS [CycleFlag],[BoundaryFlag] AS [BoundaryFlag],[VisitPath] AS [VisitPath] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, 0, 0, 0, "/1/"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A07

**As-of correction-chain survivors**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Versions AS (
SELECT EventID AS RootID,EventID,ActivityDate,MetricValue,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E WHERE ParentID IS NULL UNION ALL SELECT v.RootID,e.EventID,e.ActivityDate,e.MetricValue,CAST(v.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),v.Depth+1 FROM Versions v JOIN E e ON e.ParentID=v.EventID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',v.VisitPath)=0 AND v.Depth<100
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY RootID ORDER BY ActivityDate DESC,EventID DESC) AS Choice FROM Versions WHERE ActivityDate<='20241231'
),
Report AS (
SELECT e.EventID AS RootEventID,r.EventID AS SelectedEventID,r.ActivityDate,r.MetricValue,r.Depth FROM E e LEFT JOIN R r ON r.RootID=e.EventID AND r.Choice=1 WHERE e.ParentID IS NULL
)
SELECT [RootEventID] AS [RootEventID],[SelectedEventID] AS [SelectedEventID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Depth] AS [Depth] FROM Report ORDER BY RootEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-01", "100.0000", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A08

**FIFO interval allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Supply AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='A' AND MetricValue>0
),
Demand AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='B' AND MetricValue>0
),
Matches AS (
SELECT s.OwnerID,s.EventID AS SupplyEventID,d.EventID AS DemandEventID,(CASE WHEN s.EndValue<d.EndValue THEN s.EndValue ELSE d.EndValue END)-(CASE WHEN s.EndValue-s.MetricValue>d.EndValue-d.MetricValue THEN s.EndValue-s.MetricValue ELSE d.EndValue-d.MetricValue END) AS AllocatedValue FROM Supply s JOIN Demand d ON d.OwnerID=s.OwnerID AND s.EndValue>d.EndValue-d.MetricValue AND d.EndValue>s.EndValue-s.MetricValue
),
Result AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,CAST(0 AS decimal(38,4)) AS UnmatchedValue FROM Matches UNION ALL SELECT s.OwnerID,s.EventID,NULL,0,s.MetricValue-COALESCE(x.UsedValue,0) FROM Supply s LEFT JOIN(SELECT SupplyEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY SupplyEventID)x ON x.SupplyEventID=s.EventID WHERE s.MetricValue>COALESCE(x.UsedValue,0) UNION ALL SELECT d.OwnerID,NULL,d.EventID,0,d.MetricValue-COALESCE(x.UsedValue,0) FROM Demand d LEFT JOIN(SELECT DemandEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY DemandEventID)x ON x.DemandEventID=d.EventID WHERE d.MetricValue>COALESCE(x.UsedValue,0)
),
Report AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,UnmatchedValue FROM Result
)
SELECT [OwnerID] AS [WarehouseID],[SupplyEventID] AS [SupplyEventID],[DemandEventID] AS [DemandEventID],[AllocatedValue] AS [AllocatedValue],[UnmatchedValue] AS [UnmatchedValue] FROM Report ORDER BY WarehouseID,SupplyEventID,DemandEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, null, "0", "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A09

**Conserved largest-remainder allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
W AS (
SELECT *,CAST(SUM(TotalValue) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal FROM T
),
Units AS (
SELECT *,CAST(TotalValue*10000 AS decimal(28,0)) AS TotalUnits,CAST(SegmentTotal*10000 AS decimal(28,0)) AS SegmentUnits FROM W
),
Numerators AS (
SELECT *,CAST(TotalUnits*10000 AS decimal(33,0)) AS NumeratorUnits FROM Units
),
Remainders AS (
SELECT *,NumeratorUnits%SegmentUnits AS RemainderUnits FROM Numerators
),
Bases AS (
SELECT *,CAST((NumeratorUnits-RemainderUnits)/SegmentUnits AS int) AS BasePoints FROM Remainders
),
R AS (
SELECT *,10000-SUM(BasePoints) OVER(PARTITION BY Segment) AS RemainingPoints,ROW_NUMBER() OVER(PARTITION BY Segment ORDER BY RemainderUnits DESC,OwnerID) AS RemainderPosition FROM Bases
),
Report AS (
SELECT Segment,OwnerID,TotalValue,BasePoints+CASE WHEN RemainderPosition<=RemainingPoints THEN 1 ELSE 0 END AS BasisPoints,SegmentTotal FROM R
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[BasisPoints] AS [BasisPoints],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[["A", 1, "100.0000", 10000, "100.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A10

**Complete inactivity intervals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' UNION SELECT OwnerID,CAST('20231231' AS date) FROM Owners UNION SELECT OwnerID,CAST('20250101' AS date) FROM Owners
),
L AS (
SELECT OwnerID,ActivityDate,LEAD(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS NextDate FROM D
),
Report AS (
SELECT OwnerID,DATEADD(day,1,ActivityDate) AS StartDate,DATEADD(day,-1,NextDate) AS EndDate,DATEDIFF(day,ActivityDate,NextDate)-1 AS MissingDays FROM L WHERE DATEDIFF(day,ActivityDate,NextDate)>1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID,StartDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", "2024-12-31", 365], [2, "2024-01-01", "2024-12-31", 366], [3, "2024-01-01", "2024-12-31", 366], [4, "2024-01-01", "2024-12-31", 366], [5, "2024-01-01", "2024-12-31", 366]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A11

**Ordered three-stage funnel**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
C AS (
SELECT a.OwnerID,a.EventID AS FirstEventID,b.EventID AS SecondEventID,c.EventID AS ThirdEventID,a.ActivityDate AS StartDate,c.ActivityDate AS EndDate,ROW_NUMBER() OVER(PARTITION BY a.OwnerID ORDER BY c.ActivityDate,c.EventID,b.ActivityDate DESC,b.EventID DESC,a.ActivityDate DESC,a.EventID DESC) AS Choice FROM E a JOIN E b ON b.OwnerID=a.OwnerID AND (b.ActivityDate>a.ActivityDate OR(b.ActivityDate=a.ActivityDate AND b.EventID>a.EventID)) JOIN E c ON c.OwnerID=b.OwnerID AND (c.ActivityDate>b.ActivityDate OR(c.ActivityDate=b.ActivityDate AND c.EventID>b.EventID)) WHERE a.Kind='A' AND b.Kind='B' AND c.Kind='C'
),
Report AS (
SELECT OwnerID,FirstEventID,SecondEventID,ThirdEventID,StartDate,EndDate FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[SecondEventID] AS [SecondEventID],[ThirdEventID] AS [ThirdEventID],[StartDate] AS [StartDate],[EndDate] AS [EndDate] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A12

**Earliest rolling coverage with witnesses**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate AS TriggerDate FROM E
),
W AS (
SELECT d.OwnerID,d.TriggerDate,e.Kind AS Segment,e.EventID,ROW_NUMBER() OVER(PARTITION BY d.OwnerID,d.TriggerDate,e.Kind ORDER BY e.ActivityDate DESC,e.EventID DESC) AS Position FROM D d JOIN E e ON e.OwnerID=d.OwnerID AND e.ActivityDate>=DATEADD(day,-29,d.TriggerDate) AND e.ActivityDate<=d.TriggerDate WHERE e.Kind IN('A','B','C')
),
P AS (
SELECT OwnerID,TriggerDate,MAX(CASE WHEN Segment='A' THEN EventID END) AS AEventID,MAX(CASE WHEN Segment='B' THEN EventID END) AS BEventID,MAX(CASE WHEN Segment='C' THEN EventID END) AS CEventID FROM W WHERE Position=1 GROUP BY OwnerID,TriggerDate HAVING COUNT(*)=3
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY TriggerDate) AS Choice FROM P
),
Report AS (
SELECT OwnerID,TriggerDate,AEventID,BEventID,CEventID FROM R WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[TriggerDate] AS [TriggerDate],[AEventID] AS [AEventID],[BEventID] AS [BEventID],[CEventID] AS [CEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A13

**Distinct descendant exposure with cycles**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Down AS (
SELECT EventID AS StartID,EventID AS NodeID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT d.StartID,e.EventID,CAST(d.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),d.Depth+1 FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)=0 AND d.Depth<100
),
DistinctNodes AS (
SELECT DISTINCT StartID,NodeID FROM Down WHERE Depth>0
),
T AS (
SELECT d.StartID,COUNT(*) AS DescendantCount,COUNT(e.MetricValue) AS KnownCount,SUM(e.MetricValue) AS TotalValue FROM DistinctNodes d JOIN E e ON e.EventID=d.NodeID GROUP BY d.StartID
),
Cycles AS (
SELECT DISTINCT d.StartID FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)>0
),
Report AS (
SELECT e.EventID,COALESCE(t.DescendantCount,0) AS DescendantCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.StartID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,CASE WHEN c.StartID IS NULL THEN 0 ELSE 1 END AS CycleFlag FROM E e LEFT JOIN T t ON t.StartID=e.EventID LEFT JOIN Cycles c ON c.StartID=e.EventID
)
SELECT [EventID] AS [MovementID],[DescendantCount] AS [DescendantCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[CycleFlag] AS [CycleFlag] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 0, 0, "0", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A14

**Best mean-centered contiguous block**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
OwnerStats AS (
SELECT OwnerID,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS KnownTotal FROM E GROUP BY OwnerID
),
N AS (
SELECT e.*,CAST(s.KnownCount AS decimal(4,0))*e.MetricValue-CAST(s.KnownTotal AS decimal(28,4)) AS ScoreValue,ROW_NUMBER() OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID) AS Position,SUM(CASE WHEN e.MetricValue IS NULL THEN 1 ELSE 0 END) OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID ROWS UNBOUNDED PRECEDING) AS BlockID FROM E e JOIN OwnerStats s ON s.OwnerID=e.OwnerID
),
P AS (
SELECT *,CAST(SUM(ScoreValue) OVER(PARTITION BY OwnerID,BlockID ORDER BY Position ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS PrefixValue FROM N WHERE MetricValue IS NOT NULL
),
C AS (
SELECT s.OwnerID,s.EventID AS StartEventID,e.EventID AS EndEventID,s.Position AS StartPosition,e.Position AS EndPosition,e.PrefixValue-s.PrefixValue+s.ScoreValue AS BlockScore,e.Position-s.Position+1 AS EventCount FROM P s JOIN P e ON e.OwnerID=s.OwnerID AND e.BlockID=s.BlockID AND e.Position>=s.Position
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY BlockScore DESC,StartPosition,EndPosition) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartEventID,r.EndEventID,r.BlockScore,COALESCE(r.EventCount,0) AS EventCount FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartEventID] AS [StartEventID],[EndEventID] AS [EndEventID],[BlockScore] AS [BlockScore],[EventCount] AS [EventCount] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, "0.0000", 1], [2, null, null, null, 0], [3, null, null, null, 0], [4, null, null, null, 0], [5, null, null, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-03-A15

**Five-table reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-03-a15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') INTERSECT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Eligible AS (
SELECT f.* FROM [retail_supply_chain].[StockMovements] f JOIN E e ON e.EventID=f.[MovementID]
),
HeaderTotals AS (
SELECT [WarehouseID] AS OwnerID,COUNT(*) AS EventCount,COUNT([MovementValue]) AS KnownCount,SUM([MovementValue]) AS TotalValue FROM Eligible GROUP BY [WarehouseID]
),
Net AS (
SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM Eligible GROUP BY WarehouseID,ProductID
),
Balances AS (
SELECT b.WarehouseID AS OwnerID,SUM(b.OpeningQuantity) AS OpeningUnits,SUM(b.QuantityOnHand) AS StoredUnits,SUM(COALESCE(n.NetUnits,0)) AS SelectedNetUnits,SUM(b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0))) AS QuantityDifference,SUM(b.QuantityOnHand*p.UnitCost) AS StandardStockValue FROM retail_supply_chain.StockBalances b JOIN retail_supply_chain.Products p ON p.ProductID=b.ProductID LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID GROUP BY b.WarehouseID
),
Missing AS (
SELECT n.WarehouseID AS OwnerID,COUNT(*) AS MissingBalancePairs FROM Net n WHERE NOT EXISTS(SELECT 1 FROM retail_supply_chain.StockBalances b WHERE b.WarehouseID=n.WarehouseID AND b.ProductID=n.ProductID) GROUP BY n.WarehouseID
),
SupplierLead AS (
SELECT e.WarehouseID AS OwnerID,MAX(s.LeadTimeDays) AS MaxLeadTimeDays FROM Eligible e JOIN retail_supply_chain.Suppliers s ON s.SupplierID=e.SupplierID GROUP BY e.WarehouseID
),
Report AS (
SELECT o.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.OwnerID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,COALESCE(b.OpeningUnits,0) AS OpeningUnits,COALESCE(b.StoredUnits,0) AS StoredUnits,COALESCE(b.SelectedNetUnits,0) AS SelectedNetUnits,COALESCE(b.QuantityDifference,0) AS QuantityDifference,COALESCE(b.StandardStockValue,0) AS StandardStockValue,COALESCE(m.MissingBalancePairs,0) AS MissingBalancePairs,l.MaxLeadTimeDays FROM Owners o LEFT JOIN HeaderTotals t ON t.OwnerID=o.OwnerID LEFT JOIN Balances b ON b.OwnerID=o.OwnerID LEFT JOIN Missing m ON m.OwnerID=o.OwnerID LEFT JOIN SupplierLead l ON l.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[OpeningUnits] AS [OpeningUnits],[StoredUnits] AS [StoredUnits],[SelectedNetUnits] AS [SelectedNetUnits],[QuantityDifference] AS [QuantityDifference],[StandardStockValue] AS [StandardStockValue],[MissingBalancePairs] AS [MissingBalancePairs],[MaxLeadTimeDays] AS [MaxLeadTimeDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, 1, "100", "40", "36", "1", "-5", "327", 0, 2], [2, 0, 0, "0", "20", "31", "0", "11", "483", 0, null], [3, 0, 0, "0", "20", "21", "0", "1", "138", 0, null], [4, 0, 0, "0", "40", "42", "0", "2", "449", 0, null], [5, 0, 0, "0", "0", "0", "0", "0", "0", 0, null]]
```

### Except: progression

**Beginner:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B01

**Analysis audit**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Keep null values and stored token spaces.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,Segment FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Segment] AS [Segment] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "2024-01-02", "200.0000", "B"], [5, 3, "2024-02-01", "50.0000", "B"], [6, 3, "2024-02-10", "300.0000", "C"], [11, 1, "2024-12-31", "120.0000", "B"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B02

**Known versus unknown**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero is not unknown.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,MetricValue FROM E WHERE MetricValue IS NOT NULL
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "200.0000"], [5, 3, "50.0000"], [6, 3, "300.0000"], [11, 1, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B03

**Unknown-value queue**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An empty queue must have the requested columns.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,ActivityDate FROM E WHERE MetricValue IS NULL
)
SELECT [EventID] AS [MovementID],[ActivityDate] AS [ActivityDate] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B04

**Threshold review**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The lower bound is inclusive;unknown values cannot pass.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,MetricValue FROM E WHERE MetricValue>=100
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, "200.0000"], [6, "300.0000"], [11, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B05

**Deterministic shortlist**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return fewer than five if fewer qualify;ties do not expand the result.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT TOP (5) EventID,MetricValue FROM E WHERE MetricValue IS NOT NULL ORDER BY MetricValue DESC,EventID
)
SELECT [EventID] AS [MovementID],[MetricValue] AS [MetricValue] FROM Report ORDER BY MetricValue DESC,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[6, "300.0000"], [2, "200.0000"], [11, "120.0000"], [5, "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B06

**Active-owner totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown owner has null total,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "320.0000"], [3, 2, 2, "350.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B07

**All-owner coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Count real activity,not an outer-join placeholder.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "320.0000"], [2, 0, 0, "0"], [3, 2, 2, "350.0000"], [4, 0, 0, "0"], [5, 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B08

**Segment profile**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Use SQL Server collation equality for segment grouping.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[["B", 3, 3, "370.0000"], ["C", 1, 1, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B09

**Owner segment coverage**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated activity in one segment does not duplicate its owner/segment pair.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT DISTINCT OwnerID,Segment FROM E
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "B"], [3, "B"], [3, "C"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B10

**Observed-month totals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not fabricate missing months in this question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
M AS (
SELECT DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,MetricValue FROM E
),
Report AS (
SELECT MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM M GROUP BY MonthStart
)
SELECT [MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 1, 1, "200.0000"], ["2024-02-01", 2, 2, "350.0000"], ["2024-12-01", 1, 1, "120.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B11

**Daily workload**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Different source rows on the same day remain separate contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,ActivityDate
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,ActivityDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", 1, "200.0000"], [1, "2024-12-31", 1, "120.0000"], [3, "2024-02-01", 1, "50.0000"], [3, "2024-02-10", 1, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B12

**No eligible activity**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An owner with an unknown-value row is active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT p.OwnerID FROM Owners p WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=p.OwnerID)
)
SELECT [OwnerID] AS [WarehouseID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[2], [4], [5]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B13

**Visible parent link**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A parent excluded by the analysis eligibility rule is not visible here.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.ParentID,c.MetricValue AS ChildValue,p.MetricValue AS ParentValue FROM E c JOIN E p ON p.EventID=c.ParentID
)
SELECT [EventID] AS [MovementID],[ParentID] AS [ParentID],[ChildValue] AS [ChildValue],[ParentValue] AS [ParentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[[5, 2, "50.0000", "200.0000"], [11, 5, "120.0000", "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B14

**Bounded-value counts**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Return0 for a segment with no values in the interval.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT Segment,COUNT(*) AS EventCount,SUM(CASE WHEN MetricValue BETWEEN 100 AND 200 THEN 1 ELSE 0 END) AS InRangeCount FROM E GROUP BY Segment
)
SELECT [Segment] AS [Segment],[EventCount] AS [EventCount],[InRangeCount] AS [InRangeCount] FROM Report ORDER BY Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[["B", 3, 2], ["C", 1, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-B15

**Value sign reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-b15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. All four classes must sum to EventCount;empty input returns five zero counts.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT COUNT(*) AS EventCount,COUNT(*)-COUNT(MetricValue) AS UnknownCount,COALESCE(SUM(CASE WHEN MetricValue<0 THEN 1 ELSE 0 END),0) AS NegativeCount,COALESCE(SUM(CASE WHEN MetricValue=0 THEN 1 ELSE 0 END),0) AS ZeroCount,COALESCE(SUM(CASE WHEN MetricValue>0 THEN 1 ELSE 0 END),0) AS PositiveCount FROM E
)
SELECT [EventCount] AS [EventCount],[UnknownCount] AS [UnknownCount],[NegativeCount] AS [NegativeCount],[ZeroCount] AS [ZeroCount],[PositiveCount] AS [PositiveCount] FROM Report ORDER BY EventCount OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 1 rows. First five rows (decimal/date values are serialized as text):

```json
[[4, 0, 0, 0, 4]]
```

**Intermediate:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I01

**Exactly two per owner**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Ties cannot expand a two-row limit.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC,EventID) AS Position FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,Position FROM R WHERE Position<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[Position] AS [Position] FROM Report ORDER BY WarehouseID,Position OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [3, 6, "300.0000", 1], [3, 5, "50.0000", 2]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I02

**Two value positions with ties**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Several rows may share rank2;all must remain.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY MetricValue DESC) AS ValueRank FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT OwnerID,EventID,MetricValue,ValueRank FROM R WHERE ValueRank<=2
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[MetricValue] AS [MetricValue],[ValueRank] AS [ValueRank] FROM Report ORDER BY WarehouseID,ValueRank,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "200.0000", 1], [1, 11, "120.0000", 2], [3, 6, "300.0000", 1], [3, 5, "50.0000", 2]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I03

**Running value and knowledge**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An all-unknown prefix has null RunningValue.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT EventID,OwnerID,ActivityDate,MetricValue,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,COUNT(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningKnownCount FROM E
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[RunningValue] AS [RunningValue],[RunningKnownCount] AS [RunningKnownCount] FROM Report ORDER BY WarehouseID,ActivityDate,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "2024-01-02", "200.0000", "200.0000", 1], [11, 1, "2024-12-31", "120.0000", "320.0000", 2], [5, 3, "2024-02-01", "50.0000", "50.0000", 1], [6, 3, "2024-02-10", "300.0000", "350.0000", 2]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I04

**Previous row delta**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not skip an unknown predecessor.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
P AS (
SELECT *,LAG(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousValue FROM E
),
Report AS (
SELECT EventID,OwnerID,MetricValue,PreviousValue,MetricValue-PreviousValue AS Delta FROM P
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PreviousValue] AS [PreviousValue],[Delta] AS [Delta] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "200.0000", null, null], [11, 1, "120.0000", "200.0000", "-80.0000"], [5, 3, "50.0000", null, null], [6, 3, "300.0000", "50.0000", "250.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I05

**Share before filtering**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Filtered-out owners must still contribute to the denominator.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,SUM(MetricValue) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank,SUM(TotalValue) OVER(PARTITION BY Segment) AS SegmentTotal FROM T
),
Report AS (
SELECT Segment,OwnerID,TotalValue,ValueRank,SegmentTotal,CAST(100.0*TotalValue/NULLIF(SegmentTotal,0) AS decimal(19,6)) AS SharePercent FROM R WHERE ValueRank<=2
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[SegmentTotal] AS [SegmentTotal],[SharePercent] AS [SharePercent] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["B", 1, "320.0000", 1, "370.0000", "86.486486486486486486486486486486486486486486486486"], ["B", 3, "50.0000", 2, "370.0000", "13.513513513513513513513513513513513513513513513514"], ["C", 3, "300.0000", 1, "300.0000", "100"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I06

**Every required segment**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Required AS (
SELECT N'A' AS Segment UNION ALL SELECT N'B' UNION ALL SELECT N'C'
),
T AS (
SELECT OwnerID,COUNT(*) AS EventCount,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID
),
Report AS (
SELECT t.OwnerID,t.EventCount,t.TotalValue FROM T t WHERE NOT EXISTS(SELECT 1 FROM Required r WHERE NOT EXISTS(SELECT 1 FROM E e WHERE e.OwnerID=t.OwnerID AND e.Kind=r.Segment))
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I07

**Prior calendar window**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,c.OwnerID,COUNT(p.MetricValue) AS PriorKnownCount,CAST(AVG(CAST(p.MetricValue AS decimal(28,6))) AS decimal(28,6)) AS PriorAverage FROM E c LEFT JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate GROUP BY c.EventID,c.OwnerID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[PriorKnownCount] AS [PriorKnownCount],[PriorAverage] AS [PriorAverage] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, 0, null], [11, 1, 0, null], [5, 3, 0, null], [6, 3, 1, "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I08

**First and last known rows**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Known zero participates;do not independently take the minimum value instead of the first row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT OwnerID,EventID,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS FirstPos,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate DESC,EventID DESC) AS LastPos FROM E WHERE MetricValue IS NOT NULL
),
Report AS (
SELECT p.OwnerID,MAX(CASE WHEN k.FirstPos=1 THEN k.EventID END) AS FirstEventID,MAX(CASE WHEN k.LastPos=1 THEN k.EventID END) AS LastEventID FROM Owners p LEFT JOIN K k ON k.OwnerID=p.OwnerID GROUP BY p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[LastEventID] AS [LastEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 11], [2, null, null], [3, 5, 6], [4, null, null], [5, null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I09

**Complete 2024 calendar**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Each owner has exactly12 rows;2025 activity cannot enter2024.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Months AS (
SELECT CAST('20240101' AS date) AS MonthStart UNION ALL SELECT DATEADD(month,1,MonthStart) FROM Months WHERE MonthStart<'20241201'
),
T AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS MonthStart,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS TotalValue FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' GROUP BY OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1)
),
Report AS (
SELECT p.OwnerID,m.MonthStart,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.EventCount IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue FROM Owners p CROSS JOIN Months m LEFT JOIN T t ON t.OwnerID=p.OwnerID AND t.MonthStart=m.MonthStart
)
SELECT [OwnerID] AS [WarehouseID],[MonthStart] AS [MonthStart],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,MonthStart OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 60 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", 1, 1, "200.0000"], [1, "2024-02-01", 0, 0, "0"], [1, "2024-03-01", 0, 0, "0"], [1, "2024-04-01", 0, 0, "0"], [1, "2024-05-01", 0, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I10

**Dominant segments**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The best of several negative totals is the least negative,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT OwnerID,Segment,SUM(MetricValue) AS TotalValue FROM E GROUP BY OwnerID,Segment HAVING COUNT(MetricValue)>0
),
R AS (
SELECT *,DENSE_RANK() OVER(PARTITION BY OwnerID ORDER BY TotalValue DESC) AS ValueRank FROM T
),
Report AS (
SELECT OwnerID,Segment,TotalValue FROM R WHERE ValueRank=1
)
SELECT [OwnerID] AS [WarehouseID],[Segment] AS [Segment],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID,Segment OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "B", "320.0000"], [3, "C", "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I11

**Same-day repeated values**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT OwnerID,ActivityDate,MetricValue,COUNT(*) AS Multiplicity FROM E GROUP BY OwnerID,ActivityDate,MetricValue HAVING COUNT(*)>=2
)
SELECT [OwnerID] AS [WarehouseID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Multiplicity] AS [Multiplicity] FROM Report ORDER BY WarehouseID,ActivityDate,MetricValue OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I12

**First threshold crossing**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Owners with no positive values produce no threshold crossing.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
R AS (
SELECT *,SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS RunningValue,SUM(MetricValue) OVER(PARTITION BY OwnerID) AS TotalValue FROM E WHERE MetricValue>0
),
C AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS Choice FROM R WHERE RunningValue>=0.8*TotalValue
),
Report AS (
SELECT OwnerID,EventID,RunningValue,TotalValue FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[EventID] AS [MovementID],[RunningValue] AS [RunningValue],[TotalValue] AS [TotalValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 11, "320.0000", "320.0000"], [3, 6, "350.0000", "350.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I13

**Owner median**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. No known values gives count0 and null median,not zero.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
K AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY MetricValue,EventID) AS Position,COUNT(*) OVER(PARTITION BY OwnerID) AS KnownCount FROM E WHERE MetricValue IS NOT NULL
),
T AS (
SELECT OwnerID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM K WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY OwnerID
),
Report AS (
SELECT p.OwnerID,COALESCE(t.KnownCount,0) AS KnownCount,t.MedianValue FROM Owners p LEFT JOIN T t ON t.OwnerID=p.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[KnownCount] AS [KnownCount],[MedianValue] AS [MedianValue] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, "160.0000"], [2, 0, null], [3, 2, "175.0000"], [4, 0, null], [5, 0, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I14

**Two-generation comparison**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two joins cannot follow an excluded parent through to its grandparent.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Report AS (
SELECT c.EventID,p.EventID AS ParentEventID,g.EventID AS GrandparentEventID,c.MetricValue,p.MetricValue AS ParentValue,g.MetricValue AS GrandparentValue FROM E c LEFT JOIN E p ON p.EventID=c.ParentID LEFT JOIN E g ON g.EventID=p.ParentID
)
SELECT [EventID] AS [MovementID],[ParentEventID] AS [ParentEventID],[GrandparentEventID] AS [GrandparentEventID],[MetricValue] AS [MetricValue],[ParentValue] AS [ParentValue],[GrandparentValue] AS [GrandparentValue] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, null, null, "200.0000", null, null], [5, 2, null, "50.0000", "200.0000", null], [6, null, null, "300.0000", null, null], [11, 5, 2, "120.0000", "50.0000", "200.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-I15

**Largest inactive gap**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-i15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
L AS (
SELECT OwnerID,ActivityDate AS EndDate,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS StartDate FROM D
),
R AS (
SELECT *,DATEDIFF(day,StartDate,EndDate) AS GapDays,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY DATEDIFF(day,StartDate,EndDate) DESC,StartDate) AS Choice FROM L WHERE StartDate IS NOT NULL
),
Report AS (
SELECT p.OwnerID,r.StartDate,r.EndDate,r.GapDays FROM Owners p LEFT JOIN R r ON r.OwnerID=p.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[GapDays] AS [GapDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", "2024-12-31", 364], [2, null, null, null], [3, "2024-02-01", "2024-02-10", 9], [4, null, null, null], [5, null, null, null]]
```

**Advanced:15 questions**

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A01

**Session boundaries and comparable recovery**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a01)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
L AS (
SELECT *,LAG(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID) AS PreviousDate FROM E
),
S AS (
SELECT *,SUM(CASE WHEN PreviousDate IS NULL OR DATEDIFF(day,PreviousDate,ActivityDate)>30 THEN 1 ELSE 0 END) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS SessionNo FROM L
),
T AS (
SELECT OwnerID,SessionNo,MIN(ActivityDate) AS StartDate,MAX(ActivityDate) AS EndDate,COUNT(*) AS EventCount,COUNT(MetricValue) AS KnownCount,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM S GROUP BY OwnerID,SessionNo
),
P AS (
SELECT *,LAG(TotalValue) OVER(PARTITION BY OwnerID ORDER BY SessionNo) AS PreviousValue FROM T
),
Report AS (
SELECT o.OwnerID,COALESCE(p.SessionNo,0) AS SessionNo,p.StartDate,p.EndDate,COALESCE(p.EventCount,0) AS EventCount,COALESCE(p.KnownCount,0) AS KnownCount,CASE WHEN p.SessionNo IS NULL THEN CAST(0 AS decimal(38,4)) ELSE p.TotalValue END AS TotalValue,p.PreviousValue,CAST(100.0*(p.TotalValue-p.PreviousValue)/NULLIF(p.PreviousValue,0) AS decimal(38,6)) AS GrowthPercent FROM Owners o LEFT JOIN P p ON p.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[SessionNo] AS [SessionNo],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[PreviousValue] AS [PreviousValue],[GrowthPercent] AS [GrowthPercent] FROM Report ORDER BY WarehouseID,SessionNo OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 6 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 1, "2024-01-02", "2024-01-02", 1, 1, "200.0000", null, null], [1, 2, "2024-12-31", "2024-12-31", 1, 1, "120.0000", "200.0000", "-40"], [2, 0, null, null, 0, 0, "0", null, null], [3, 1, "2024-02-01", "2024-02-10", 2, 2, "350.0000", null, null], [4, 0, null, null, 0, 0, "0", null, null]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A02

**Prior-window median anomaly**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a02)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
H AS (
SELECT c.EventID,p.EventID AS HistoryID,p.MetricValue,ROW_NUMBER() OVER(PARTITION BY c.EventID ORDER BY p.MetricValue,p.EventID) AS Position,COUNT(*) OVER(PARTITION BY c.EventID) AS KnownCount FROM E c JOIN E p ON p.OwnerID=c.OwnerID AND p.ActivityDate>=DATEADD(day,-30,c.ActivityDate) AND p.ActivityDate<c.ActivityDate WHERE p.MetricValue IS NOT NULL
),
M AS (
SELECT EventID,MAX(KnownCount) AS KnownCount,CAST(AVG(CAST(MetricValue AS decimal(28,6))) AS decimal(28,6)) AS MedianValue FROM H WHERE 2*Position BETWEEN KnownCount AND KnownCount+2 GROUP BY EventID
),
Report AS (
SELECT e.EventID,e.OwnerID,e.MetricValue,COALESCE(m.KnownCount,0) AS PriorKnownCount,m.MedianValue AS PriorMedian,CASE WHEN e.MetricValue>2*m.MedianValue THEN 1 ELSE 0 END AS IsAnomaly FROM E e LEFT JOIN M m ON m.EventID=e.EventID
)
SELECT [EventID] AS [MovementID],[OwnerID] AS [WarehouseID],[MetricValue] AS [MetricValue],[PriorKnownCount] AS [PriorKnownCount],[PriorMedian] AS [PriorMedian],[IsAnomaly] AS [IsAnomaly] FROM Report ORDER BY WarehouseID,MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 1, "200.0000", 0, null, 0], [11, 1, "120.0000", 0, null, 0], [5, 3, "50.0000", 0, null, 0], [6, 3, "300.0000", 1, "50.0000", 1]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A03

**Smallest complete tie groups reaching80 percent**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a03)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
G AS (
SELECT Segment,TotalValue,CAST(SUM(TotalValue) AS decimal(28,4)) AS PeerTotal FROM T GROUP BY Segment,TotalValue
),
C AS (
SELECT *,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment ORDER BY TotalValue DESC ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS CumulativeValue,CAST(SUM(PeerTotal) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal,DENSE_RANK() OVER(PARTITION BY Segment ORDER BY TotalValue DESC) AS ValueRank FROM G
),
Report AS (
SELECT t.Segment,t.OwnerID,t.TotalValue,c.ValueRank,c.CumulativeValue,c.SegmentTotal FROM T t JOIN C c ON c.Segment=t.Segment AND c.TotalValue=t.TotalValue WHERE c.CumulativeValue-c.PeerTotal<0.8*c.SegmentTotal
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[ValueRank] AS [ValueRank],[CumulativeValue] AS [CumulativeValue],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,ValueRank,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 2 rows. First five rows (decimal/date values are serialized as text):

```json
[["B", 1, "320.0000", 1, "320.0000", "370.0000"], ["C", 3, "300.0000", 1, "300.0000", "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A04

**Six-month cohort retention**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a04)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
FirstSeen AS (
SELECT OwnerID,DATEFROMPARTS(YEAR(MIN(ActivityDate)),MONTH(MIN(ActivityDate)),1) AS CohortMonth FROM E GROUP BY OwnerID
),
C AS (
SELECT * FROM FirstSeen WHERE CohortMonth>='20240101' AND CohortMonth<'20250101'
),
N AS (
SELECT 0 AS MonthOffset UNION ALL SELECT MonthOffset+1 FROM N WHERE MonthOffset<5
),
A AS (
SELECT DISTINCT OwnerID,DATEFROMPARTS(YEAR(ActivityDate),MONTH(ActivityDate),1) AS ActivityMonth FROM E
),
Report AS (
SELECT c.CohortMonth,n.MonthOffset,DATEADD(month,n.MonthOffset,c.CohortMonth) AS ActivityMonth,COUNT(*) AS CohortSize,COUNT(a.OwnerID) AS ActiveOwners,CAST(100.0*COUNT(a.OwnerID)/COUNT(*) AS decimal(19,6)) AS RetentionPercent FROM C c CROSS JOIN N n LEFT JOIN A a ON a.OwnerID=c.OwnerID AND a.ActivityMonth=DATEADD(month,n.MonthOffset,c.CohortMonth) GROUP BY c.CohortMonth,n.MonthOffset
)
SELECT [CohortMonth] AS [CohortMonth],[MonthOffset] AS [MonthOffset],[ActivityMonth] AS [ActivityMonth],[CohortSize] AS [CohortSize],[ActiveOwners] AS [ActiveOwners],[RetentionPercent] AS [RetentionPercent] FROM Report ORDER BY CohortMonth,MonthOffset OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 12 rows. First five rows (decimal/date values are serialized as text):

```json
[["2024-01-01", 0, "2024-01-01", 1, 1, "100"], ["2024-01-01", 1, "2024-02-01", 1, 0, "0"], ["2024-01-01", 2, "2024-03-01", 1, 0, "0"], ["2024-01-01", 3, "2024-04-01", 1, 0, "0"], ["2024-01-01", 4, "2024-05-01", 1, 0, "0"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A05

**Longest activity run with one missing day**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a05)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E
),
N AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS Position FROM D
),
C AS (
SELECT s.OwnerID,s.ActivityDate AS StartDate,e.ActivityDate AS EndDate,e.Position-s.Position+1 AS ActiveDays,DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1) AS MissingDays FROM N s JOIN N e ON e.OwnerID=s.OwnerID AND e.Position>=s.Position WHERE DATEDIFF(day,s.ActivityDate,e.ActivityDate)+1-(e.Position-s.Position+1)<=1
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY ActiveDays DESC,StartDate,EndDate) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartDate,r.EndDate,COALESCE(r.ActiveDays,0) AS ActiveDays,COALESCE(r.MissingDays,0) AS MissingDays FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[ActiveDays] AS [ActiveDays],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-02", "2024-01-02", 1, 0], [2, null, null, 0, 0], [3, "2024-02-01", "2024-02-01", 1, 0], [4, null, null, 0, 0], [5, null, null, 0, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A06

**Cycle-safe parent resolution**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a06)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Walk AS (
SELECT EventID AS StartID,EventID AS CurrentID,ParentID AS NextID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT w.StartID,e.EventID,e.ParentID,CAST(w.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),w.Depth+1 FROM Walk w JOIN E e ON e.EventID=w.NextID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',w.VisitPath)=0 AND w.Depth<100
),
Terminal AS (
SELECT w.*,CASE WHEN w.NextID IS NOT NULL AND CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 THEN 1 ELSE 0 END AS CycleFlag,CASE WHEN w.NextID IS NOT NULL AND NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID) THEN 1 ELSE 0 END AS BoundaryFlag FROM Walk w WHERE w.NextID IS NULL OR CHARINDEX('/'+CAST(w.NextID AS varchar(12))+'/',w.VisitPath)>0 OR NOT EXISTS(SELECT 1 FROM E e WHERE e.EventID=w.NextID)
),
Report AS (
SELECT StartID AS EventID,CurrentID AS TerminalEventID,CASE WHEN NextID IS NULL THEN CurrentID END AS RootEventID,Depth,CycleFlag,BoundaryFlag,VisitPath FROM Terminal
)
SELECT [EventID] AS [MovementID],[TerminalEventID] AS [TerminalEventID],[RootEventID] AS [RootEventID],[Depth] AS [Depth],[CycleFlag] AS [CycleFlag],[BoundaryFlag] AS [BoundaryFlag],[VisitPath] AS [VisitPath] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 2, null, 0, 0, 1, "/2/"], [5, 2, null, 1, 0, 1, "/5/2/"], [6, 6, null, 0, 0, 1, "/6/"], [11, 2, null, 2, 0, 1, "/11/5/2/"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A07

**As-of correction-chain survivors**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a07)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Versions AS (
SELECT EventID AS RootID,EventID,ActivityDate,MetricValue,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E WHERE ParentID IS NULL UNION ALL SELECT v.RootID,e.EventID,e.ActivityDate,e.MetricValue,CAST(v.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),v.Depth+1 FROM Versions v JOIN E e ON e.ParentID=v.EventID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',v.VisitPath)=0 AND v.Depth<100
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY RootID ORDER BY ActivityDate DESC,EventID DESC) AS Choice FROM Versions WHERE ActivityDate<='20241231'
),
Report AS (
SELECT e.EventID AS RootEventID,r.EventID AS SelectedEventID,r.ActivityDate,r.MetricValue,r.Depth FROM E e LEFT JOIN R r ON r.RootID=e.EventID AND r.Choice=1 WHERE e.ParentID IS NULL
)
SELECT [RootEventID] AS [RootEventID],[SelectedEventID] AS [SelectedEventID],[ActivityDate] AS [ActivityDate],[MetricValue] AS [MetricValue],[Depth] AS [Depth] FROM Report ORDER BY RootEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A08

**FIFO interval allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a08)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Supply AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='A' AND MetricValue>0
),
Demand AS (
SELECT *,CAST(SUM(MetricValue) OVER(PARTITION BY OwnerID ORDER BY ActivityDate,EventID ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS EndValue FROM E WHERE Kind='B' AND MetricValue>0
),
Matches AS (
SELECT s.OwnerID,s.EventID AS SupplyEventID,d.EventID AS DemandEventID,(CASE WHEN s.EndValue<d.EndValue THEN s.EndValue ELSE d.EndValue END)-(CASE WHEN s.EndValue-s.MetricValue>d.EndValue-d.MetricValue THEN s.EndValue-s.MetricValue ELSE d.EndValue-d.MetricValue END) AS AllocatedValue FROM Supply s JOIN Demand d ON d.OwnerID=s.OwnerID AND s.EndValue>d.EndValue-d.MetricValue AND d.EndValue>s.EndValue-s.MetricValue
),
Result AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,CAST(0 AS decimal(38,4)) AS UnmatchedValue FROM Matches UNION ALL SELECT s.OwnerID,s.EventID,NULL,0,s.MetricValue-COALESCE(x.UsedValue,0) FROM Supply s LEFT JOIN(SELECT SupplyEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY SupplyEventID)x ON x.SupplyEventID=s.EventID WHERE s.MetricValue>COALESCE(x.UsedValue,0) UNION ALL SELECT d.OwnerID,NULL,d.EventID,0,d.MetricValue-COALESCE(x.UsedValue,0) FROM Demand d LEFT JOIN(SELECT DemandEventID,CAST(SUM(AllocatedValue) AS decimal(28,4)) AS UsedValue FROM Matches GROUP BY DemandEventID)x ON x.DemandEventID=d.EventID WHERE d.MetricValue>COALESCE(x.UsedValue,0)
),
Report AS (
SELECT OwnerID,SupplyEventID,DemandEventID,AllocatedValue,UnmatchedValue FROM Result
)
SELECT [OwnerID] AS [WarehouseID],[SupplyEventID] AS [SupplyEventID],[DemandEventID] AS [DemandEventID],[AllocatedValue] AS [AllocatedValue],[UnmatchedValue] AS [UnmatchedValue] FROM Report ORDER BY WarehouseID,SupplyEventID,DemandEventID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, null, 2, "0", "200.0000"], [1, null, 11, "0", "120.0000"], [3, null, 5, "0", "50.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A09

**Conserved largest-remainder allocation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a09)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
T AS (
SELECT Segment,OwnerID,CAST(SUM(MetricValue) AS decimal(28,4)) AS TotalValue FROM E WHERE MetricValue>0 GROUP BY Segment,OwnerID
),
W AS (
SELECT *,CAST(SUM(TotalValue) OVER(PARTITION BY Segment) AS decimal(28,4)) AS SegmentTotal FROM T
),
Units AS (
SELECT *,CAST(TotalValue*10000 AS decimal(28,0)) AS TotalUnits,CAST(SegmentTotal*10000 AS decimal(28,0)) AS SegmentUnits FROM W
),
Numerators AS (
SELECT *,CAST(TotalUnits*10000 AS decimal(33,0)) AS NumeratorUnits FROM Units
),
Remainders AS (
SELECT *,NumeratorUnits%SegmentUnits AS RemainderUnits FROM Numerators
),
Bases AS (
SELECT *,CAST((NumeratorUnits-RemainderUnits)/SegmentUnits AS int) AS BasePoints FROM Remainders
),
R AS (
SELECT *,10000-SUM(BasePoints) OVER(PARTITION BY Segment) AS RemainingPoints,ROW_NUMBER() OVER(PARTITION BY Segment ORDER BY RemainderUnits DESC,OwnerID) AS RemainderPosition FROM Bases
),
Report AS (
SELECT Segment,OwnerID,TotalValue,BasePoints+CASE WHEN RemainderPosition<=RemainingPoints THEN 1 ELSE 0 END AS BasisPoints,SegmentTotal FROM R
)
SELECT [Segment] AS [Segment],[OwnerID] AS [WarehouseID],[TotalValue] AS [TotalValue],[BasisPoints] AS [BasisPoints],[SegmentTotal] AS [SegmentTotal] FROM Report ORDER BY Segment,WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 3 rows. First five rows (decimal/date values are serialized as text):

```json
[["B", 1, "320.0000", 8649, "370.0000"], ["B", 3, "50.0000", 1351, "370.0000"], ["C", 3, "300.0000", 10000, "300.0000"]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A10

**Complete inactivity intervals**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a10)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate FROM E WHERE ActivityDate>='20240101' AND ActivityDate<'20250101' UNION SELECT OwnerID,CAST('20231231' AS date) FROM Owners UNION SELECT OwnerID,CAST('20250101' AS date) FROM Owners
),
L AS (
SELECT OwnerID,ActivityDate,LEAD(ActivityDate) OVER(PARTITION BY OwnerID ORDER BY ActivityDate) AS NextDate FROM D
),
Report AS (
SELECT OwnerID,DATEADD(day,1,ActivityDate) AS StartDate,DATEADD(day,-1,NextDate) AS EndDate,DATEDIFF(day,ActivityDate,NextDate)-1 AS MissingDays FROM L WHERE DATEDIFF(day,ActivityDate,NextDate)>1
)
SELECT [OwnerID] AS [WarehouseID],[StartDate] AS [StartDate],[EndDate] AS [EndDate],[MissingDays] AS [MissingDays] FROM Report ORDER BY WarehouseID,StartDate OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 8 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, "2024-01-01", "2024-01-01", 1], [1, "2024-01-03", "2024-12-30", 363], [2, "2024-01-01", "2024-12-31", 366], [3, "2024-01-01", "2024-01-31", 31], [3, "2024-02-02", "2024-02-09", 8]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A11

**Ordered three-stage funnel**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a11)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
C AS (
SELECT a.OwnerID,a.EventID AS FirstEventID,b.EventID AS SecondEventID,c.EventID AS ThirdEventID,a.ActivityDate AS StartDate,c.ActivityDate AS EndDate,ROW_NUMBER() OVER(PARTITION BY a.OwnerID ORDER BY c.ActivityDate,c.EventID,b.ActivityDate DESC,b.EventID DESC,a.ActivityDate DESC,a.EventID DESC) AS Choice FROM E a JOIN E b ON b.OwnerID=a.OwnerID AND (b.ActivityDate>a.ActivityDate OR(b.ActivityDate=a.ActivityDate AND b.EventID>a.EventID)) JOIN E c ON c.OwnerID=b.OwnerID AND (c.ActivityDate>b.ActivityDate OR(c.ActivityDate=b.ActivityDate AND c.EventID>b.EventID)) WHERE a.Kind='A' AND b.Kind='B' AND c.Kind='C'
),
Report AS (
SELECT OwnerID,FirstEventID,SecondEventID,ThirdEventID,StartDate,EndDate FROM C WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[FirstEventID] AS [FirstEventID],[SecondEventID] AS [SecondEventID],[ThirdEventID] AS [ThirdEventID],[StartDate] AS [StartDate],[EndDate] AS [EndDate] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A12

**Earliest rolling coverage with witnesses**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a12)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
D AS (
SELECT DISTINCT OwnerID,ActivityDate AS TriggerDate FROM E
),
W AS (
SELECT d.OwnerID,d.TriggerDate,e.Kind AS Segment,e.EventID,ROW_NUMBER() OVER(PARTITION BY d.OwnerID,d.TriggerDate,e.Kind ORDER BY e.ActivityDate DESC,e.EventID DESC) AS Position FROM D d JOIN E e ON e.OwnerID=d.OwnerID AND e.ActivityDate>=DATEADD(day,-29,d.TriggerDate) AND e.ActivityDate<=d.TriggerDate WHERE e.Kind IN('A','B','C')
),
P AS (
SELECT OwnerID,TriggerDate,MAX(CASE WHEN Segment='A' THEN EventID END) AS AEventID,MAX(CASE WHEN Segment='B' THEN EventID END) AS BEventID,MAX(CASE WHEN Segment='C' THEN EventID END) AS CEventID FROM W WHERE Position=1 GROUP BY OwnerID,TriggerDate HAVING COUNT(*)=3
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY TriggerDate) AS Choice FROM P
),
Report AS (
SELECT OwnerID,TriggerDate,AEventID,BEventID,CEventID FROM R WHERE Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[TriggerDate] AS [TriggerDate],[AEventID] AS [AEventID],[BEventID] AS [BEventID],[CEventID] AS [CEventID] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 0 rows. First five rows (decimal/date values are serialized as text):

```json
[]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A13

**Distinct descendant exposure with cycles**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a13)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Down AS (
SELECT EventID AS StartID,EventID AS NodeID,CAST('/'+CAST(EventID AS varchar(12))+'/' AS varchar(max)) AS VisitPath,0 AS Depth FROM E UNION ALL SELECT d.StartID,e.EventID,CAST(d.VisitPath+CAST(e.EventID AS varchar(12))+'/' AS varchar(max)),d.Depth+1 FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)=0 AND d.Depth<100
),
DistinctNodes AS (
SELECT DISTINCT StartID,NodeID FROM Down WHERE Depth>0
),
T AS (
SELECT d.StartID,COUNT(*) AS DescendantCount,COUNT(e.MetricValue) AS KnownCount,SUM(e.MetricValue) AS TotalValue FROM DistinctNodes d JOIN E e ON e.EventID=d.NodeID GROUP BY d.StartID
),
Cycles AS (
SELECT DISTINCT d.StartID FROM Down d JOIN E e ON e.ParentID=d.NodeID WHERE CHARINDEX('/'+CAST(e.EventID AS varchar(12))+'/',d.VisitPath)>0
),
Report AS (
SELECT e.EventID,COALESCE(t.DescendantCount,0) AS DescendantCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.StartID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,CASE WHEN c.StartID IS NULL THEN 0 ELSE 1 END AS CycleFlag FROM E e LEFT JOIN T t ON t.StartID=e.EventID LEFT JOIN Cycles c ON c.StartID=e.EventID
)
SELECT [EventID] AS [MovementID],[DescendantCount] AS [DescendantCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[CycleFlag] AS [CycleFlag] FROM Report ORDER BY MovementID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 4 rows. First five rows (decimal/date values are serialized as text):

```json
[[2, 2, 2, "170.0000", 0], [5, 1, 1, "120.0000", 0], [6, 0, 0, "0", 0], [11, 0, 0, "0", 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A14

**Best mean-centered contiguous block**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a14)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
OwnerStats AS (
SELECT OwnerID,COUNT(MetricValue) AS KnownCount,SUM(MetricValue) AS KnownTotal FROM E GROUP BY OwnerID
),
N AS (
SELECT e.*,CAST(s.KnownCount AS decimal(4,0))*e.MetricValue-CAST(s.KnownTotal AS decimal(28,4)) AS ScoreValue,ROW_NUMBER() OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID) AS Position,SUM(CASE WHEN e.MetricValue IS NULL THEN 1 ELSE 0 END) OVER(PARTITION BY e.OwnerID ORDER BY e.ActivityDate,e.EventID ROWS UNBOUNDED PRECEDING) AS BlockID FROM E e JOIN OwnerStats s ON s.OwnerID=e.OwnerID
),
P AS (
SELECT *,CAST(SUM(ScoreValue) OVER(PARTITION BY OwnerID,BlockID ORDER BY Position ROWS UNBOUNDED PRECEDING) AS decimal(28,4)) AS PrefixValue FROM N WHERE MetricValue IS NOT NULL
),
C AS (
SELECT s.OwnerID,s.EventID AS StartEventID,e.EventID AS EndEventID,s.Position AS StartPosition,e.Position AS EndPosition,e.PrefixValue-s.PrefixValue+s.ScoreValue AS BlockScore,e.Position-s.Position+1 AS EventCount FROM P s JOIN P e ON e.OwnerID=s.OwnerID AND e.BlockID=s.BlockID AND e.Position>=s.Position
),
R AS (
SELECT *,ROW_NUMBER() OVER(PARTITION BY OwnerID ORDER BY BlockScore DESC,StartPosition,EndPosition) AS Choice FROM C
),
Report AS (
SELECT o.OwnerID,r.StartEventID,r.EndEventID,r.BlockScore,COALESCE(r.EventCount,0) AS EventCount FROM Owners o LEFT JOIN R r ON r.OwnerID=o.OwnerID AND r.Choice=1
)
SELECT [OwnerID] AS [WarehouseID],[StartEventID] AS [StartEventID],[EndEventID] AS [EndEventID],[BlockScore] AS [BlockScore],[EventCount] AS [EventCount] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "80.0000", 1], [2, null, null, null, 0], [3, 6, 6, "250.0000", 1], [4, null, null, null, 0], [5, null, null, null, 0]]
```

#### RETAIL_SUPPLY_CHAIN-SET_OPERATIONS-04-A15

**Five-table reconciliation**

[Canonical question](../questions/SET_OPERATIONS.md#retail_supply_chain-set_operations-04-a15)

**Assessment model:** The two result sets must match complete values,nulls,multiplicity and required ordering. Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Analysis audit reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
)
SELECT EventID AS [MovementID],OwnerID AS [WarehouseID],ActivityDate AS AnalysisDate,MetricValue AS AnalysisValue,Segment AS AnalysisSegment,ParentID AS AnalysisParentID,Kind AS AnalysisKind FROM E ORDER BY EventID OPTION (MAXRECURSION 32767);
```

**Business report reference**

```sql
;WITH Focus_Eligible AS (
SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [WarehouseID] IN (SELECT [WarehouseID] FROM [retail_supply_chain].[Warehouses] WHERE Region='North') EXCEPT SELECT [MovementID] FROM [retail_supply_chain].[StockMovements] WHERE [Status]='Open'
),
Focus_FocusRows AS (
SELECT f.[MovementID] AS EventID,f.[WarehouseID] AS OwnerID,CAST(f.[MovementDate] AS date) AS ActivityDate,CAST(f.[MovementValue] AS decimal(28,4)) AS MetricValue,CAST(f.[MovementCategory] AS nvarchar(100)) AS Segment,f.[ParentMovementID] AS ParentID FROM [retail_supply_chain].[StockMovements] f JOIN Focus_Eligible x ON x.[MovementID]=f.[MovementID] WHERE 1=1
),
E AS (
SELECT x.*,original.[MovementCategory] AS Kind FROM Focus_FocusRows x JOIN [retail_supply_chain].[StockMovements] original ON original.[MovementID]=x.EventID
),
Owners AS (
SELECT [WarehouseID] AS OwnerID FROM [retail_supply_chain].[Warehouses]
),
Eligible AS (
SELECT f.* FROM [retail_supply_chain].[StockMovements] f JOIN E e ON e.EventID=f.[MovementID]
),
HeaderTotals AS (
SELECT [WarehouseID] AS OwnerID,COUNT(*) AS EventCount,COUNT([MovementValue]) AS KnownCount,SUM([MovementValue]) AS TotalValue FROM Eligible GROUP BY [WarehouseID]
),
Net AS (
SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM Eligible GROUP BY WarehouseID,ProductID
),
Balances AS (
SELECT b.WarehouseID AS OwnerID,SUM(b.OpeningQuantity) AS OpeningUnits,SUM(b.QuantityOnHand) AS StoredUnits,SUM(COALESCE(n.NetUnits,0)) AS SelectedNetUnits,SUM(b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0))) AS QuantityDifference,SUM(b.QuantityOnHand*p.UnitCost) AS StandardStockValue FROM retail_supply_chain.StockBalances b JOIN retail_supply_chain.Products p ON p.ProductID=b.ProductID LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID GROUP BY b.WarehouseID
),
Missing AS (
SELECT n.WarehouseID AS OwnerID,COUNT(*) AS MissingBalancePairs FROM Net n WHERE NOT EXISTS(SELECT 1 FROM retail_supply_chain.StockBalances b WHERE b.WarehouseID=n.WarehouseID AND b.ProductID=n.ProductID) GROUP BY n.WarehouseID
),
SupplierLead AS (
SELECT e.WarehouseID AS OwnerID,MAX(s.LeadTimeDays) AS MaxLeadTimeDays FROM Eligible e JOIN retail_supply_chain.Suppliers s ON s.SupplierID=e.SupplierID GROUP BY e.WarehouseID
),
Report AS (
SELECT o.OwnerID,COALESCE(t.EventCount,0) AS EventCount,COALESCE(t.KnownCount,0) AS KnownCount,CASE WHEN t.OwnerID IS NULL THEN CAST(0 AS decimal(38,4)) ELSE t.TotalValue END AS TotalValue,COALESCE(b.OpeningUnits,0) AS OpeningUnits,COALESCE(b.StoredUnits,0) AS StoredUnits,COALESCE(b.SelectedNetUnits,0) AS SelectedNetUnits,COALESCE(b.QuantityDifference,0) AS QuantityDifference,COALESCE(b.StandardStockValue,0) AS StandardStockValue,COALESCE(m.MissingBalancePairs,0) AS MissingBalancePairs,l.MaxLeadTimeDays FROM Owners o LEFT JOIN HeaderTotals t ON t.OwnerID=o.OwnerID LEFT JOIN Balances b ON b.OwnerID=o.OwnerID LEFT JOIN Missing m ON m.OwnerID=o.OwnerID LEFT JOIN SupplierLead l ON l.OwnerID=o.OwnerID
)
SELECT [OwnerID] AS [WarehouseID],[EventCount] AS [EventCount],[KnownCount] AS [KnownCount],[TotalValue] AS [TotalValue],[OpeningUnits] AS [OpeningUnits],[StoredUnits] AS [StoredUnits],[SelectedNetUnits] AS [SelectedNetUnits],[QuantityDifference] AS [QuantityDifference],[StandardStockValue] AS [StandardStockValue],[MissingBalancePairs] AS [MissingBalancePairs],[MaxLeadTimeDays] AS [MaxLeadTimeDays] FROM Report ORDER BY WarehouseID OPTION (MAXRECURSION 32767);
```

**Small-fixture expected report:** 5 rows. First five rows (decimal/date values are serialized as text):

```json
[[1, 2, 2, "320", "40", "36", "-5", "1", "327", 0, 3], [2, 0, 0, "0", "20", "31", "0", "11", "483", 0, null], [3, 2, 2, "350", "20", "21", "1", "0", "138", 0, 3], [4, 0, 0, "0", "40", "42", "0", "2", "449", 0, null], [5, 0, 0, "0", "0", "0", "0", "0", "0", 0, null]]
```

