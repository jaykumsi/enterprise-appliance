# Retail Supply Chain: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_SUPPLY_CHAIN-ADV-01 — Monthly activity with missing months and growth

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Months AS (
    SELECT CAST('20240101' AS date) AS MonthStart
    UNION ALL
    SELECT DATEADD(month, 1, MonthStart)
    FROM Months WHERE MonthStart < CAST('20241201' AS date)
), Activity AS (
    SELECT WarehouseID, DATEFROMPARTS(YEAR(MovementDate), MONTH(MovementDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(MovementValue) AS KnownValueCount,
           SUM(MovementValue) AS TotalValue
    FROM [retail_supply_chain].[StockMovements]
    WHERE MovementDate >= '20240101' AND MovementDate < '20250101'
    GROUP BY WarehouseID, DATEFROMPARTS(YEAR(MovementDate), MONTH(MovementDate), 1)
), Filled AS (
    SELECT p.WarehouseID, p.WarehouseName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [retail_supply_chain].[Warehouses] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.WarehouseID = p.WarehouseID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY WarehouseID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY WarehouseID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### RETAIL_SUPPLY_CHAIN-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT WarehouseID, MovementDate FROM [retail_supply_chain].[StockMovements]
), Numbered AS (
    SELECT WarehouseID, MovementDate,
           DATEDIFF(day, '20000101', MovementDate)
           - ROW_NUMBER() OVER (PARTITION BY WarehouseID ORDER BY MovementDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT WarehouseID, MIN(MovementDate) AS StreakStart, MAX(MovementDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY WarehouseID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.WarehouseID, p.WarehouseName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [retail_supply_chain].[Warehouses] p ON p.WarehouseID = s.WarehouseID
ORDER BY s.WarehouseID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### RETAIL_SUPPLY_CHAIN-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT MovementCategory, WarehouseID, SUM(MovementValue) AS TotalValue
    FROM [retail_supply_chain].[StockMovements] GROUP BY MovementCategory, WarehouseID HAVING COUNT(MovementValue) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY MovementCategory ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY MovementCategory) AS CategoryTotal
    FROM Totals
)
SELECT r.MovementCategory, r.WarehouseID, p.WarehouseName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [retail_supply_chain].[Warehouses] p ON p.WarehouseID = r.WarehouseID
WHERE r.ValueRank <= 2
ORDER BY r.MovementCategory, r.ValueRank, r.WarehouseID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### RETAIL_SUPPLY_CHAIN-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.MovementID, COUNT(priorRow.MovementValue) AS PriorKnownCount,
           AVG(CAST(priorRow.MovementValue AS decimal(19,4))) AS PriorAverage
    FROM [retail_supply_chain].[StockMovements] currentRow
    LEFT JOIN [retail_supply_chain].[StockMovements] priorRow ON priorRow.WarehouseID = currentRow.WarehouseID
        AND priorRow.MovementDate >= DATEADD(day, -30, currentRow.MovementDate)
        AND priorRow.MovementDate < currentRow.MovementDate
    GROUP BY currentRow.MovementID
)
SELECT f.MovementID, f.WarehouseID, f.MovementDate, f.MovementValue, h.PriorKnownCount, h.PriorAverage
FROM [retail_supply_chain].[StockMovements] f JOIN History h ON h.MovementID = f.MovementID
WHERE h.PriorKnownCount > 0 AND f.MovementValue > 1.5 * h.PriorAverage
ORDER BY f.WarehouseID, f.MovementDate, f.MovementID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### RETAIL_SUPPLY_CHAIN-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [retail_supply_chain].[StockMovements] WHERE MovementDate >= '20240101' AND MovementDate < '20250101'
), Totals AS (
    SELECT WarehouseID, COUNT(*) AS EventCount, COUNT(MovementValue) AS KnownValueCount,
           SUM(MovementValue) AS TotalValue
    FROM YearActivity GROUP BY WarehouseID
)
SELECT p.WarehouseID, p.WarehouseName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [retail_supply_chain].[Warehouses] p JOIN Totals t ON t.WarehouseID = p.WarehouseID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.WarehouseID = p.WarehouseID AND f.MovementCategory = required.RequiredType
    )
)
ORDER BY p.WarehouseID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
