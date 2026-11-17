# Brokerage: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### BROKERAGE-ADV-01 — Monthly activity with missing months and growth

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
    SELECT AccountID, DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(EstimatedValue) AS KnownValueCount,
           SUM(EstimatedValue) AS TotalValue
    FROM [brokerage].[TradeOrders]
    WHERE OrderDate >= '20240101' AND OrderDate < '20250101'
    GROUP BY AccountID, DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1)
), Filled AS (
    SELECT p.AccountID, p.AccountName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [brokerage].[BrokerageAccounts] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.AccountID = p.AccountID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY AccountID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY AccountID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### BROKERAGE-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT AccountID, OrderDate FROM [brokerage].[TradeOrders]
), Numbered AS (
    SELECT AccountID, OrderDate,
           DATEDIFF(day, '20000101', OrderDate)
           - ROW_NUMBER() OVER (PARTITION BY AccountID ORDER BY OrderDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT AccountID, MIN(OrderDate) AS StreakStart, MAX(OrderDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY AccountID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.AccountID, p.AccountName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [brokerage].[BrokerageAccounts] p ON p.AccountID = s.AccountID
ORDER BY s.AccountID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### BROKERAGE-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT RoutingCategory, AccountID, SUM(EstimatedValue) AS TotalValue
    FROM [brokerage].[TradeOrders] GROUP BY RoutingCategory, AccountID HAVING COUNT(EstimatedValue) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY RoutingCategory ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY RoutingCategory) AS CategoryTotal
    FROM Totals
)
SELECT r.RoutingCategory, r.AccountID, p.AccountName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [brokerage].[BrokerageAccounts] p ON p.AccountID = r.AccountID
WHERE r.ValueRank <= 2
ORDER BY r.RoutingCategory, r.ValueRank, r.AccountID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### BROKERAGE-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.OrderID, COUNT(priorRow.EstimatedValue) AS PriorKnownCount,
           AVG(CAST(priorRow.EstimatedValue AS decimal(19,4))) AS PriorAverage
    FROM [brokerage].[TradeOrders] currentRow
    LEFT JOIN [brokerage].[TradeOrders] priorRow ON priorRow.AccountID = currentRow.AccountID
        AND priorRow.OrderDate >= DATEADD(day, -30, currentRow.OrderDate)
        AND priorRow.OrderDate < currentRow.OrderDate
    GROUP BY currentRow.OrderID
)
SELECT f.OrderID, f.AccountID, f.OrderDate, f.EstimatedValue, h.PriorKnownCount, h.PriorAverage
FROM [brokerage].[TradeOrders] f JOIN History h ON h.OrderID = f.OrderID
WHERE h.PriorKnownCount > 0 AND f.EstimatedValue > 1.5 * h.PriorAverage
ORDER BY f.AccountID, f.OrderDate, f.OrderID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### BROKERAGE-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [brokerage].[TradeOrders] WHERE OrderDate >= '20240101' AND OrderDate < '20250101'
), Totals AS (
    SELECT AccountID, COUNT(*) AS EventCount, COUNT(EstimatedValue) AS KnownValueCount,
           SUM(EstimatedValue) AS TotalValue
    FROM YearActivity GROUP BY AccountID
)
SELECT p.AccountID, p.AccountName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [brokerage].[BrokerageAccounts] p JOIN Totals t ON t.AccountID = p.AccountID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.AccountID = p.AccountID AND f.RoutingCategory = required.RequiredType
    )
)
ORDER BY p.AccountID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
