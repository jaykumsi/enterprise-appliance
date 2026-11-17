# Retail Manufacturing: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_MANUFACTURING-ADV-01 — Monthly activity with missing months and growth

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
    SELECT ProductID, DATEFROMPARTS(YEAR(ProductionDate), MONTH(ProductionDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(PlannedCost) AS KnownValueCount,
           SUM(PlannedCost) AS TotalValue
    FROM [retail_manufacturing].[ProductionOrders]
    WHERE ProductionDate >= '20240101' AND ProductionDate < '20250101'
    GROUP BY ProductID, DATEFROMPARTS(YEAR(ProductionDate), MONTH(ProductionDate), 1)
), Filled AS (
    SELECT p.ProductID, p.ProductName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [retail_manufacturing].[Products] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.ProductID = p.ProductID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY ProductID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY ProductID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### RETAIL_MANUFACTURING-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT ProductID, ProductionDate FROM [retail_manufacturing].[ProductionOrders]
), Numbered AS (
    SELECT ProductID, ProductionDate,
           DATEDIFF(day, '20000101', ProductionDate)
           - ROW_NUMBER() OVER (PARTITION BY ProductID ORDER BY ProductionDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT ProductID, MIN(ProductionDate) AS StreakStart, MAX(ProductionDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY ProductID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.ProductID, p.ProductName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [retail_manufacturing].[Products] p ON p.ProductID = s.ProductID
ORDER BY s.ProductID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### RETAIL_MANUFACTURING-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT ProductionCategory, ProductID, SUM(PlannedCost) AS TotalValue
    FROM [retail_manufacturing].[ProductionOrders] GROUP BY ProductionCategory, ProductID HAVING COUNT(PlannedCost) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY ProductionCategory ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY ProductionCategory) AS CategoryTotal
    FROM Totals
)
SELECT r.ProductionCategory, r.ProductID, p.ProductName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [retail_manufacturing].[Products] p ON p.ProductID = r.ProductID
WHERE r.ValueRank <= 2
ORDER BY r.ProductionCategory, r.ValueRank, r.ProductID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### RETAIL_MANUFACTURING-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.ProductionOrderID, COUNT(priorRow.PlannedCost) AS PriorKnownCount,
           AVG(CAST(priorRow.PlannedCost AS decimal(19,4))) AS PriorAverage
    FROM [retail_manufacturing].[ProductionOrders] currentRow
    LEFT JOIN [retail_manufacturing].[ProductionOrders] priorRow ON priorRow.ProductID = currentRow.ProductID
        AND priorRow.ProductionDate >= DATEADD(day, -30, currentRow.ProductionDate)
        AND priorRow.ProductionDate < currentRow.ProductionDate
    GROUP BY currentRow.ProductionOrderID
)
SELECT f.ProductionOrderID, f.ProductID, f.ProductionDate, f.PlannedCost, h.PriorKnownCount, h.PriorAverage
FROM [retail_manufacturing].[ProductionOrders] f JOIN History h ON h.ProductionOrderID = f.ProductionOrderID
WHERE h.PriorKnownCount > 0 AND f.PlannedCost > 1.5 * h.PriorAverage
ORDER BY f.ProductID, f.ProductionDate, f.ProductionOrderID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### RETAIL_MANUFACTURING-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [retail_manufacturing].[ProductionOrders] WHERE ProductionDate >= '20240101' AND ProductionDate < '20250101'
), Totals AS (
    SELECT ProductID, COUNT(*) AS EventCount, COUNT(PlannedCost) AS KnownValueCount,
           SUM(PlannedCost) AS TotalValue
    FROM YearActivity GROUP BY ProductID
)
SELECT p.ProductID, p.ProductName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [retail_manufacturing].[Products] p JOIN Totals t ON t.ProductID = p.ProductID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.ProductID = p.ProductID AND f.ProductionCategory = required.RequiredType
    )
)
ORDER BY p.ProductID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
