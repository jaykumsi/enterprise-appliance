# Healthcare: ADVANCED QUERIES — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/ADVANCED_QUERIES.md)

## Teaching and troubleshooting

Inspect each CTE independently. Check empty periods versus all-NULL periods, tied ranks, zero denominators and inclusive/exclusive date boundaries. Fixed expected results use the small fixture, not the large practice data.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### HEALTHCARE-ADV-01 — Monthly activity with missing months and growth

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
    SELECT PatientID, DATEFROMPARTS(YEAR(EncounterDate), MONTH(EncounterDate), 1) AS MonthStart,
           COUNT(*) AS EventCount, COUNT(Charge) AS KnownValueCount,
           SUM(Charge) AS TotalValue
    FROM [healthcare].[Encounters]
    WHERE EncounterDate >= '20240101' AND EncounterDate < '20250101'
    GROUP BY PatientID, DATEFROMPARTS(YEAR(EncounterDate), MONTH(EncounterDate), 1)
), Filled AS (
    SELECT p.PatientID, p.PatientName, m.MonthStart,
           COALESCE(a.EventCount, 0) AS EventCount,
           COALESCE(a.KnownValueCount, 0) AS KnownValueCount,
           CASE WHEN a.EventCount IS NULL THEN 0 ELSE a.TotalValue END AS TotalValue
    FROM [healthcare].[Patients] p CROSS JOIN Months m
    LEFT JOIN Activity a ON a.PatientID = p.PatientID AND a.MonthStart = m.MonthStart
), Compared AS (
    SELECT *, LAG(TotalValue) OVER (PARTITION BY PatientID ORDER BY MonthStart) AS PreviousMonthValue
    FROM Filled
)
SELECT *, 100.0 * (TotalValue - PreviousMonthValue) / NULLIF(PreviousMonthValue, 0) AS GrowthPercent
FROM Compared
ORDER BY PatientID, MonthStart
OPTION (MAXRECURSION 12);
```

**Check and explain:** Small fixture: 60 rows, 11 events in 2024, total known value 1500. Master 5 has twelve zero totals. Master 1 January total is 300; February growth is -100%; March growth is NULL because February was zero.

### HEALTHCARE-ADV-02 — Consecutive active-date streaks

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH ActiveDates AS (
    SELECT DISTINCT PatientID, EncounterDate FROM [healthcare].[Encounters]
), Numbered AS (
    SELECT PatientID, EncounterDate,
           DATEDIFF(day, '20000101', EncounterDate)
           - ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate) AS IslandKey
    FROM ActiveDates
), Streaks AS (
    SELECT PatientID, MIN(EncounterDate) AS StreakStart, MAX(EncounterDate) AS StreakEnd, COUNT(*) AS ActiveDays
    FROM Numbered GROUP BY PatientID, IslandKey HAVING COUNT(*) >= 2
)
SELECT s.PatientID, p.PatientName, s.StreakStart, s.StreakEnd, s.ActiveDays
FROM Streaks s JOIN [healthcare].[Patients] p ON p.PatientID = s.PatientID
ORDER BY s.PatientID, s.StreakStart;
```

**Check and explain:** Small fixture: three two-day streaks: master 1 Jan 1–2; master 2 Jan 2–3; master 4 Feb 29–Mar 1. Master 4 Mar 10 and master 2 Jan 1, 2025 are isolated, so they are excluded.

### HEALTHCARE-ADV-03 — Top contributors with ties and category share

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH Totals AS (
    SELECT EncounterType, PatientID, SUM(Charge) AS TotalValue
    FROM [healthcare].[Encounters] GROUP BY EncounterType, PatientID HAVING COUNT(Charge) > 0
), Ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY EncounterType ORDER BY TotalValue DESC) AS ValueRank,
           SUM(TotalValue) OVER (PARTITION BY EncounterType) AS CategoryTotal
    FROM Totals
)
SELECT r.EncounterType, r.PatientID, p.PatientName, r.TotalValue, r.ValueRank, r.CategoryTotal,
       100.0 * r.TotalValue / NULLIF(r.CategoryTotal, 0) AS SharePercent
FROM Ranked r JOIN [healthcare].[Patients] p ON p.PatientID = r.PatientID
WHERE r.ValueRank <= 2
ORDER BY r.EncounterType, r.ValueRank, r.PatientID;
```

**Check and explain:** Small fixture: 7 rows. Category A total=180, B=520, C=1000. Category C includes both masters tied at rank 2. In B, master 1 total=320 and master 4 total=150; their shares use denominator 520, including the filtered-out master 3 total of 50.

### HEALTHCARE-ADV-04 — Trailing 30-calendar-day comparison

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH History AS (
    SELECT currentRow.EncounterID, COUNT(priorRow.Charge) AS PriorKnownCount,
           AVG(CAST(priorRow.Charge AS decimal(19,4))) AS PriorAverage
    FROM [healthcare].[Encounters] currentRow
    LEFT JOIN [healthcare].[Encounters] priorRow ON priorRow.PatientID = currentRow.PatientID
        AND priorRow.EncounterDate >= DATEADD(day, -30, currentRow.EncounterDate)
        AND priorRow.EncounterDate < currentRow.EncounterDate
    GROUP BY currentRow.EncounterID
)
SELECT f.EncounterID, f.PatientID, f.EncounterDate, f.Charge, h.PriorKnownCount, h.PriorAverage
FROM [healthcare].[Encounters] f JOIN History h ON h.EncounterID = f.EncounterID
WHERE h.PriorKnownCount > 0 AND f.Charge > 1.5 * h.PriorAverage
ORDER BY f.PatientID, f.EncounterDate, f.EncounterID;
```

**Check and explain:** Small fixture: event IDs 2, 6, 8 and 9 qualify. Prior averages are 100, 50, 0 and 75 respectively. A known zero average is valid; missing history is not.

### HEALTHCARE-ADV-05 — Masters covering every required category

**Question**

[Canonical questions](../questions/ADVANCED_QUERIES.md)

**Reference answer**

```sql
;WITH RequiredTypes AS (
    SELECT 'A' AS RequiredType UNION ALL SELECT 'B' UNION ALL SELECT 'C'
), YearActivity AS (
    SELECT * FROM [healthcare].[Encounters] WHERE EncounterDate >= '20240101' AND EncounterDate < '20250101'
), Totals AS (
    SELECT PatientID, COUNT(*) AS EventCount, COUNT(Charge) AS KnownValueCount,
           SUM(Charge) AS TotalValue
    FROM YearActivity GROUP BY PatientID
)
SELECT p.PatientID, p.PatientName, t.EventCount, t.KnownValueCount, t.TotalValue
FROM [healthcare].[Patients] p JOIN Totals t ON t.PatientID = p.PatientID
WHERE NOT EXISTS (
    SELECT 1 FROM RequiredTypes required
    WHERE NOT EXISTS (
        SELECT 1 FROM YearActivity f
        WHERE f.PatientID = p.PatientID AND f.EncounterType = required.RequiredType
    )
)
ORDER BY p.PatientID;
```

**Check and explain:** Small fixture: only master 4 qualifies, with 4 events, 4 known values and total 530. Master 5 has no activity and does not qualify.
