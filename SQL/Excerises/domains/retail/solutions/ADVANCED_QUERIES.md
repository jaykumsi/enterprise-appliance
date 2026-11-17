# Retail: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL-ADV-01 — Monthly activity with missing months and growth

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
    SELECT CustomerID, DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(OrderTotal) AS KnownValueCount,
           SUM(OrderTotal) AS TotalValue
    FROM [retail].[Orders]
    WHERE OrderDate >= '20240101' AND OrderDate < '20250101'
    GROUP BY CustomerID, DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1)
), Filled AS (
    SELECT p.CustomerID, p.CustomerName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [retail].[Customers] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.CustomerID = p.CustomerID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY CustomerID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY CustomerID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### RETAIL-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT CustomerID, OrderDate FROM [retail].[Orders]
), Numbered AS (
    SELECT CustomerID, OrderDate,
           DATEDIFF(day, '20000101', OrderDate)
           - ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT CustomerID, MIN(OrderDate) AS StreakStart, MAX(OrderDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY CustomerID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.CustomerID, p.CustomerName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [retail].[Customers] p ON p.CustomerID = s.CustomerID
ORDER BY s.CustomerID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### RETAIL-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT SalesChannel, CustomerID, SUM(OrderTotal) AS TotalValue
    FROM [retail].[Orders] GROUP BY SalesChannel, CustomerID HAVING COUNT(OrderTotal) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY SalesChannel ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY SalesChannel) AS CategoryTotal
    FROM Totals
)
SELECT r.SalesChannel, r.CustomerID, p.CustomerName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [retail].[Customers] p ON p.CustomerID = r.CustomerID
WHERE r.ValueRank <= 2
ORDER BY r.SalesChannel, r.ValueRank, r.CustomerID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### RETAIL-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.OrderID, COUNT(priorRow.OrderTotal) AS PriorKnownCount,
           AVG(CAST(priorRow.OrderTotal AS decimal(19,4))) AS PriorAverage
    FROM [retail].[Orders] currentRow
    LEFT JOIN [retail].[Orders] priorRow ON priorRow.CustomerID = currentRow.CustomerID
        AND priorRow.OrderDate >= DATEADD(day, -30, currentRow.OrderDate)
        AND priorRow.OrderDate < currentRow.OrderDate
    GROUP BY currentRow.OrderID
)
SELECT f.OrderID, f.CustomerID, f.OrderDate, f.OrderTotal, h.PriorKnownCount, h.PriorAverage
FROM [retail].[Orders] f JOIN History h ON h.OrderID = f.OrderID
WHERE h.PriorKnownCount > 0 AND f.OrderTotal > 1.5 * h.PriorAverage
ORDER BY f.CustomerID, f.OrderDate, f.OrderID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### RETAIL-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [retail].[Orders] WHERE OrderDate >= '20240101' AND OrderDate < '20250101'
), Totals AS (
    SELECT CustomerID, COUNT(*) AS EventCount, COUNT(OrderTotal) AS KnownValueCount,
           SUM(OrderTotal) AS TotalValue
    FROM YearActivity GROUP BY CustomerID
)
SELECT p.CustomerID, p.CustomerName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [retail].[Customers] p JOIN Totals t ON t.CustomerID = p.CustomerID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.CustomerID = p.CustomerID AND f.SalesChannel = required.RequiredType
    )
)
ORDER BY p.CustomerID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
