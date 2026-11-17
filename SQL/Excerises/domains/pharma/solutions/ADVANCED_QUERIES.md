# Pharma: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### PHARMA-ADV-01 — Monthly activity with missing months and growth

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
    SELECT SupplierID, DATEFROMPARTS(YEAR(ManufactureDate), MONTH(ManufactureDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(BatchCost) AS KnownValueCount,
           SUM(BatchCost) AS TotalValue
    FROM [pharma].[Batches]
    WHERE ManufactureDate >= '20240101' AND ManufactureDate < '20250101'
    GROUP BY SupplierID, DATEFROMPARTS(YEAR(ManufactureDate), MONTH(ManufactureDate), 1)
), Filled AS (
    SELECT p.SupplierID, p.SupplierName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [pharma].[Suppliers] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.SupplierID = p.SupplierID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY SupplierID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY SupplierID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### PHARMA-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT SupplierID, ManufactureDate FROM [pharma].[Batches]
), Numbered AS (
    SELECT SupplierID, ManufactureDate,
           DATEDIFF(day, '20000101', ManufactureDate)
           - ROW_NUMBER() OVER (PARTITION BY SupplierID ORDER BY ManufactureDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT SupplierID, MIN(ManufactureDate) AS StreakStart, MAX(ManufactureDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY SupplierID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.SupplierID, p.SupplierName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [pharma].[Suppliers] p ON p.SupplierID = s.SupplierID
ORDER BY s.SupplierID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### PHARMA-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT BatchType, SupplierID, SUM(BatchCost) AS TotalValue
    FROM [pharma].[Batches] GROUP BY BatchType, SupplierID HAVING COUNT(BatchCost) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY BatchType ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY BatchType) AS CategoryTotal
    FROM Totals
)
SELECT r.BatchType, r.SupplierID, p.SupplierName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [pharma].[Suppliers] p ON p.SupplierID = r.SupplierID
WHERE r.ValueRank <= 2
ORDER BY r.BatchType, r.ValueRank, r.SupplierID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### PHARMA-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.BatchID, COUNT(priorRow.BatchCost) AS PriorKnownCount,
           AVG(CAST(priorRow.BatchCost AS decimal(19,4))) AS PriorAverage
    FROM [pharma].[Batches] currentRow
    LEFT JOIN [pharma].[Batches] priorRow ON priorRow.SupplierID = currentRow.SupplierID
        AND priorRow.ManufactureDate >= DATEADD(day, -30, currentRow.ManufactureDate)
        AND priorRow.ManufactureDate < currentRow.ManufactureDate
    GROUP BY currentRow.BatchID
)
SELECT f.BatchID, f.SupplierID, f.ManufactureDate, f.BatchCost, h.PriorKnownCount, h.PriorAverage
FROM [pharma].[Batches] f JOIN History h ON h.BatchID = f.BatchID
WHERE h.PriorKnownCount > 0 AND f.BatchCost > 1.5 * h.PriorAverage
ORDER BY f.SupplierID, f.ManufactureDate, f.BatchID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### PHARMA-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [pharma].[Batches] WHERE ManufactureDate >= '20240101' AND ManufactureDate < '20250101'
), Totals AS (
    SELECT SupplierID, COUNT(*) AS EventCount, COUNT(BatchCost) AS KnownValueCount,
           SUM(BatchCost) AS TotalValue
    FROM YearActivity GROUP BY SupplierID
)
SELECT p.SupplierID, p.SupplierName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [pharma].[Suppliers] p JOIN Totals t ON t.SupplierID = p.SupplierID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.SupplierID = p.SupplierID AND f.BatchType = required.RequiredType
    )
)
ORDER BY p.SupplierID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
