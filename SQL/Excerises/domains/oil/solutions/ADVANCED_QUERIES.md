# Oil: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### OIL-ADV-01 — Monthly activity with missing months and growth

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
    SELECT SiteID, DATEFROMPARTS(YEAR(ShipDate), MONTH(ShipDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(ShipmentValue) AS KnownValueCount,
           SUM(ShipmentValue) AS TotalValue
    FROM [oil].[Shipments]
    WHERE ShipDate >= '20240101' AND ShipDate < '20250101'
    GROUP BY SiteID, DATEFROMPARTS(YEAR(ShipDate), MONTH(ShipDate), 1)
), Filled AS (
    SELECT p.SiteID, p.SiteName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [oil].[Sites] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.SiteID = p.SiteID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY SiteID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY SiteID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### OIL-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT SiteID, ShipDate FROM [oil].[Shipments]
), Numbered AS (
    SELECT SiteID, ShipDate,
           DATEDIFF(day, '20000101', ShipDate)
           - ROW_NUMBER() OVER (PARTITION BY SiteID ORDER BY ShipDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT SiteID, MIN(ShipDate) AS StreakStart, MAX(ShipDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY SiteID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.SiteID, p.SiteName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [oil].[Sites] p ON p.SiteID = s.SiteID
ORDER BY s.SiteID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### OIL-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT ShipmentType, SiteID, SUM(ShipmentValue) AS TotalValue
    FROM [oil].[Shipments] GROUP BY ShipmentType, SiteID HAVING COUNT(ShipmentValue) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY ShipmentType ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY ShipmentType) AS CategoryTotal
    FROM Totals
)
SELECT r.ShipmentType, r.SiteID, p.SiteName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [oil].[Sites] p ON p.SiteID = r.SiteID
WHERE r.ValueRank <= 2
ORDER BY r.ShipmentType, r.ValueRank, r.SiteID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### OIL-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.ShipmentID, COUNT(priorRow.ShipmentValue) AS PriorKnownCount,
           AVG(CAST(priorRow.ShipmentValue AS decimal(19,4))) AS PriorAverage
    FROM [oil].[Shipments] currentRow
    LEFT JOIN [oil].[Shipments] priorRow ON priorRow.SiteID = currentRow.SiteID
        AND priorRow.ShipDate >= DATEADD(day, -30, currentRow.ShipDate)
        AND priorRow.ShipDate < currentRow.ShipDate
    GROUP BY currentRow.ShipmentID
)
SELECT f.ShipmentID, f.SiteID, f.ShipDate, f.ShipmentValue, h.PriorKnownCount, h.PriorAverage
FROM [oil].[Shipments] f JOIN History h ON h.ShipmentID = f.ShipmentID
WHERE h.PriorKnownCount > 0 AND f.ShipmentValue > 1.5 * h.PriorAverage
ORDER BY f.SiteID, f.ShipDate, f.ShipmentID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### OIL-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [oil].[Shipments] WHERE ShipDate >= '20240101' AND ShipDate < '20250101'
), Totals AS (
    SELECT SiteID, COUNT(*) AS EventCount, COUNT(ShipmentValue) AS KnownValueCount,
           SUM(ShipmentValue) AS TotalValue
    FROM YearActivity GROUP BY SiteID
)
SELECT p.SiteID, p.SiteName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [oil].[Sites] p JOIN Totals t ON t.SiteID = p.SiteID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.SiteID = p.SiteID AND f.ShipmentType = required.RequiredType
    )
)
ORDER BY p.SiteID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
