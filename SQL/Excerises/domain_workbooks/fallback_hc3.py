"""Replacement items, part 3: JOINS, OPERATORS, SET_OPERATIONS (see fallback_hc.py)."""
from fallback_hc import F

# ---------------- JOINS ----------------
F('JOINS-B02', 'Region on each encounter',
  'Show each encounter ID with the region of the patient it belongs to.',
  '''SELECT e.EncounterID, p.Region
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
ORDER BY e.EncounterID;''',
  'INNER JOIN matches each encounter to its patient through the shared PatientID column.')
F('JOINS-B03', 'Patient number on each encounter',
  'List each encounter reference with the patient number and the charge.',
  '''SELECT e.EncounterReference, p.PatientNumber, e.Charge
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
ORDER BY e.EncounterReference;''',
  'Use table aliases (e, p) to keep column references short and clear.')
F('JOINS-B07', 'Two joins in one query',
  'Show encounter ID, patient name and the date of the patient\'s first encounter for every encounter. Join Encounters to Patients, then to a derived table of first dates.',
  '''SELECT e.EncounterID, p.PatientName, f.FirstDate
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
JOIN (SELECT PatientID, MIN(EncounterDate) AS FirstDate
      FROM healthcare.Encounters
      GROUP BY PatientID) AS f ON f.PatientID = e.PatientID
ORDER BY e.EncounterID;''',
  'Each JOIN adds one more source. A derived table (a query in brackets with an alias) can be joined like any table.')
F('JOINS-B09', 'RIGHT JOIN',
  'Using RIGHT JOIN, list every patient and the encounters they had (patients with none must still appear).',
  '''SELECT p.PatientID, p.PatientName, e.EncounterID
FROM healthcare.Encounters AS e
RIGHT JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
ORDER BY p.PatientID, e.EncounterID;''',
  'RIGHT JOIN keeps every row of the right-hand table. It is the same as a LEFT JOIN with the tables swapped; most people write LEFT JOIN.')
F('JOINS-B10', 'Patients with no encounters',
  'Which patients have never had an encounter?',
  '''SELECT p.PatientID, p.PatientName
FROM healthcare.Patients AS p
LEFT JOIN healthcare.Encounters AS e ON e.PatientID = p.PatientID
WHERE e.EncounterID IS NULL
ORDER BY p.PatientID;''',
  'LEFT JOIN keeps every patient; patients with no match get NULL in the encounter columns. Filtering on IS NULL keeps only the unmatched ones (an anti-join). An empty result means every patient has encounters.')
F('JOINS-I01', 'Join with a filter on both sides',
  'For every Closed encounter of a North patient, show the patient name, encounter date and charge.',
  '''SELECT p.PatientName, e.EncounterDate, e.Charge
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE e.Status = 'Closed' AND p.Region = 'North'
ORDER BY e.EncounterDate, p.PatientName;''',
  'WHERE can filter on columns from any joined table.')
F('JOINS-I03', 'Self join: next encounter',
  'Pair each encounter with the same patient\'s next encounter. Show both IDs and dates.',
  '''WITH n AS (
    SELECT EncounterID, PatientID, EncounterDate,
           ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate, EncounterID) AS rn
    FROM healthcare.Encounters
)
SELECT a.PatientID, a.EncounterID, a.EncounterDate,
       b.EncounterID AS NextID, b.EncounterDate AS NextDate
FROM n AS a
JOIN n AS b ON b.PatientID = a.PatientID AND b.rn = a.rn + 1
ORDER BY a.PatientID, a.EncounterDate;''',
  'A self join joins a table to itself with two aliases. Numbering each patient\'s encounters first makes "the next one" a simple rn + 1 match.')
F('JOINS-I04', 'Days between encounters',
  'Using the self join, show how many days passed between each encounter and the same patient\'s next encounter. Show the 5 longest gaps.',
  '''WITH n AS (
    SELECT EncounterID, PatientID, EncounterDate,
           ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate, EncounterID) AS rn
    FROM healthcare.Encounters
)
SELECT TOP (5) a.PatientID, a.EncounterID, b.EncounterID AS NextID,
       DATEDIFF(day, a.EncounterDate, b.EncounterDate) AS GapDays
FROM n AS a
JOIN n AS b ON b.PatientID = a.PatientID AND b.rn = a.rn + 1
ORDER BY GapDays DESC, a.EncounterID;''',
  'Once both rows are side by side, DATEDIFF can compare them. LEAD() would give the same answer without a self join.')
F('JOINS-I05', 'Total charge per region',
  'Show each patient region with its number of encounters and total charge. Highest total first.',
  '''SELECT p.Region, COUNT(*) AS Encounters, SUM(e.Charge) AS TotalCharge
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
GROUP BY p.Region
ORDER BY TotalCharge DESC;''',
  'Join first, then GROUP BY a column from the joined table.')
F('JOINS-I07', 'Charge per unit on each encounter',
  'For each encounter show the patient name, ServiceUnits, charge and charge per unit. Highest charge per unit first (top 10).',
  '''SELECT TOP (10) p.PatientName, e.ServiceUnits, e.Charge,
       CAST(e.Charge / e.ServiceUnits AS decimal(12,2)) AS ChargePerUnit
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
ORDER BY ChargePerUnit DESC, e.EncounterID;''',
  'Calculations can mix columns from any of the joined tables.')
F('JOINS-I08', 'FULL OUTER JOIN',
  'Copy Encounters into #Enc and add one row for patient 7777 (who does not exist). Then show every patient and every copied encounter in one result: patients with no encounters and encounters with no patient both appear. Show only the unmatched rows.',
  '''SELECT EncounterID, PatientID INTO #Enc FROM healthcare.Encounters;
INSERT INTO #Enc VALUES (9999, 7777);

SELECT p.PatientID AS PatientSide, c.EncounterID, c.PatientID AS EncounterSide
FROM healthcare.Patients AS p
FULL OUTER JOIN #Enc AS c ON c.PatientID = p.PatientID
WHERE p.PatientID IS NULL OR c.EncounterID IS NULL
ORDER BY PatientSide, c.EncounterID;

DROP TABLE #Enc;''',
  'FULL OUTER JOIN keeps unmatched rows from both sides, with NULLs on the missing side. It is the tool for reconciling two lists.')
F('JOINS-I10', 'Patients with repeat activity',
  'Which patients have 3 or more encounters? Show the patient name, the number of encounters and the number of different encounter types.',
  '''SELECT p.PatientName, COUNT(*) AS Encounters, COUNT(DISTINCT e.EncounterType) AS Types
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
GROUP BY p.PatientID, p.PatientName
HAVING COUNT(*) >= 3
ORDER BY Encounters DESC, p.PatientName;''',
  'COUNT(*) counts rows; COUNT(DISTINCT ...) counts different values. HAVING filters the groups after counting.')
F('JOINS-A02', 'Top patient per region',
  'For each patient region, find the patient with the highest total charge. If two patients tie, show both.',
  '''WITH t AS (
    SELECT p.Region, p.PatientName, SUM(e.Charge) AS Total,
           RANK() OVER (PARTITION BY p.Region ORDER BY SUM(e.Charge) DESC) AS rnk
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
    GROUP BY p.Region, p.PatientID, p.PatientName
)
SELECT Region, PatientName, Total
FROM t
WHERE rnk = 1
ORDER BY Region;''',
  'Join, aggregate, rank inside each region with RANK (which keeps ties), then filter rank 1.')
F('JOINS-A03', 'Patient\'s latest encounter with details',
  'For every patient who has encounters, show their most recent encounter date and that encounter\'s type and charge.',
  '''SELECT p.PatientName, e.EncounterDate, e.EncounterType, e.Charge
FROM healthcare.Patients AS p
JOIN healthcare.Encounters AS e ON e.PatientID = p.PatientID
WHERE e.EncounterID = (SELECT TOP (1) e2.EncounterID
                       FROM healthcare.Encounters AS e2
                       WHERE e2.PatientID = p.PatientID
                       ORDER BY e2.EncounterDate DESC, e2.EncounterID DESC)
ORDER BY p.PatientName;''',
  'A correlated subquery picks the latest encounter for each patient; the join then brings that row\'s details. ROW_NUMBER in a CTE is the other common way.')
F('JOINS-A04', 'Joins that multiply rows',
  'Show each patient\'s total encounter charge and number of Open encounters. Make sure the charge is not double counted.',
  '''SELECT p.PatientID, p.PatientName,
       ISNULL(ch.TotalCharge, 0) AS TotalCharge,
       ISNULL(op.OpenEncounters, 0) AS OpenEncounters
FROM healthcare.Patients AS p
LEFT JOIN (SELECT PatientID, SUM(Charge) AS TotalCharge
           FROM healthcare.Encounters
           GROUP BY PatientID) AS ch ON ch.PatientID = p.PatientID
LEFT JOIN (SELECT PatientID, COUNT(*) AS OpenEncounters
           FROM healthcare.Encounters
           WHERE Status = 'Open'
           GROUP BY PatientID) AS op ON op.PatientID = p.PatientID
ORDER BY TotalCharge DESC, p.PatientID;''',
  'Joining two child row sets and then summing makes each charge count once per matching row (fan-out). Aggregating each set separately before joining fixes this. Interviewers often test whether you spot fan-out.')
F('JOINS-A05', 'Patients active again after a Pending encounter',
  'Find patients who had a Pending encounter and also have a later encounter after it. Show patient name, the Pending date and the later date.',
  '''SELECT DISTINCT p.PatientName, pe.EncounterDate AS PendingDate, la.EncounterDate AS LaterDate
FROM healthcare.Encounters AS pe
JOIN healthcare.Encounters AS la ON la.PatientID = pe.PatientID AND la.EncounterDate > pe.EncounterDate
JOIN healthcare.Patients  AS p  ON p.PatientID = pe.PatientID
WHERE pe.Status = 'Pending'
ORDER BY p.PatientName, PendingDate, LaterDate;''',
  'Joining the table to itself with a "later date" condition finds sequences of events. An empty result means no patient came back after a Pending encounter.')
F('JOINS-A06', 'Regions with no Open encounters',
  'List patient regions that have encounters but none of them are Open.',
  '''SELECT p.Region
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
GROUP BY p.Region
HAVING SUM(CASE WHEN e.Status = 'Open' THEN 1 ELSE 0 END) = 0
ORDER BY p.Region;''',
  'Conditional aggregation counts the Open rows per group; HAVING = 0 keeps groups with none. An empty result means every region has Open work.')
F('JOINS-A08', 'Three encounters in a row',
  'For each patient, show chains of three consecutive encounters (first, second, third) with their IDs, using two self joins.',
  '''WITH n AS (
    SELECT EncounterID, PatientID,
           ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate, EncounterID) AS rn
    FROM healthcare.Encounters
)
SELECT a.PatientID, a.EncounterID AS FirstID, b.EncounterID AS SecondID, c.EncounterID AS ThirdID
FROM n AS a
JOIN n AS b ON b.PatientID = a.PatientID AND b.rn = a.rn + 1
JOIN n AS c ON c.PatientID = a.PatientID AND c.rn = a.rn + 2
ORDER BY a.PatientID, a.rn;''',
  'Each extra self join adds one more step in the chain. For longer or unknown depths, use a recursive CTE instead.')
F('JOINS-A09', 'Patients active in the same week',
  'Find pairs of different patients who had an encounter in the same week of 2024. Show the week number and both patient IDs, each pair once.',
  '''SELECT DISTINCT DATEPART(week, a.EncounterDate) AS WeekNo, a.PatientID AS Patient1, b.PatientID AS Patient2
FROM healthcare.Encounters AS a
JOIN healthcare.Encounters AS b
  ON DATEPART(week, b.EncounterDate) = DATEPART(week, a.EncounterDate)
 AND YEAR(b.EncounterDate) = YEAR(a.EncounterDate)
 AND b.PatientID > a.PatientID
ORDER BY WeekNo, Patient1, Patient2;''',
  'The condition b.PatientID > a.PatientID removes self-pairs and keeps each pair once (A,B but not B,A).')
F('JOINS-A10', 'Most common type per region',
  'For each patient region, show the encounter type that occurs most often. Keep ties.',
  '''WITH c AS (
    SELECT p.Region, e.EncounterType, COUNT(*) AS n,
           RANK() OVER (PARTITION BY p.Region ORDER BY COUNT(*) DESC) AS rnk
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
    GROUP BY p.Region, e.EncounterType
)
SELECT Region, EncounterType, n AS Encounters
FROM c
WHERE rnk = 1
ORDER BY Region, EncounterType;''',
  'Count per group, rank within each region, keep rank 1. RANK keeps ties; ROW_NUMBER would pick one arbitrarily.')

# ---------------- OPERATORS ----------------
F('OPERATORS-B03', 'Greater than or equal',
  'List encounters with a charge of 240 or more.',
  '''SELECT EncounterID, Charge
FROM healthcare.Encounters
WHERE Charge >= 240
ORDER BY Charge, EncounterID;''',
  '>= includes the boundary value itself; > would exclude it.')
F('OPERATORS-B06', 'Starts with (LIKE)',
  'Find patients whose name starts with the same letter as patient 1\'s name.',
  '''DECLARE @letter nvarchar(1) = (SELECT LEFT(PatientName, 1) FROM healthcare.Patients WHERE PatientID = 1);

SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE PatientName LIKE @letter + '%'
ORDER BY PatientName;''',
  'LIKE \'x%\' means "starts with x": % matches any number of characters.')
F('OPERATORS-B07', 'Contains (LIKE)',
  'Find encounters whose EncounterReference contains \'202406\' anywhere (the references embed the date, so these are June 2024 encounters).',
  '''SELECT EncounterID, EncounterReference
FROM healthcare.Encounters
WHERE EncounterReference LIKE '%202406%'
ORDER BY EncounterID;''',
  '%text% means "contains": the pattern can match anywhere in the value. A leading % stops SQL Server from using an index seek, so on big tables prefer a real date filter.')
F('OPERATORS-B10', 'Arithmetic operators',
  'For each encounter, show ServiceUnits, ServiceUnits divided by 3, and the remainder of ServiceUnits divided by 3.',
  '''SELECT EncounterID, ServiceUnits,
       ServiceUnits / 3 AS WholeThirds,
       ServiceUnits % 3 AS Remainder
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'With two integers, / gives a whole number (decimals are dropped) and % gives the remainder.')
F('OPERATORS-I05', 'NOT LIKE',
  'List patients whose name does NOT contain the letter \'a\'.',
  '''SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE PatientName NOT LIKE '%a%'
ORDER BY PatientName;''',
  'NOT LIKE keeps the rows that do not match the pattern. NULL names would be excluded by both LIKE and NOT LIKE.')
F('OPERATORS-I10', 'String concatenation operator',
  'Show each patient as \'Name (Number)\', for example \'Olivia Bennett (PT-0000001)\'.',
  '''SELECT PatientName + ' (' + PatientNumber + ')' AS PatientLabel
FROM healthcare.Patients
ORDER BY PatientID;''',
  '+ joins text. If any part is NULL the whole result is NULL; CONCAT() treats NULL as empty text instead.')
F('OPERATORS-A02', 'Search ignoring case and spaces',
  'Find patients whose name contains \'ER\' in any letter case.',
  '''SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE UPPER(PatientName) LIKE '%ER%'
ORDER BY PatientName;''',
  'UPPER on both sides makes the search case-insensitive even on a case-sensitive collation. On large tables, wrapping a column in a function stops index seeks.')
F('OPERATORS-A04', 'Divide-by-zero safety',
  'Show each encounter\'s charge divided by (EncounterID % 5). Avoid errors when the divisor is 0.',
  '''SELECT EncounterID, Charge,
       Charge / NULLIF(EncounterID % 5, 0) AS SafeRatio
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'NULLIF(x, 0) returns NULL when x is 0, and dividing by NULL gives NULL instead of an error.')
F('OPERATORS-A10', 'Short-circuit is not guaranteed',
  'Return patients where the name has a space and the text before the first space is longer than 5 characters. Write it safely so CHARINDEX never gives a negative length.',
  '''SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE CHARINDEX(' ', PatientName) > 0
  AND LEN(LEFT(PatientName, CASE WHEN CHARINDEX(' ', PatientName) > 0
                                 THEN CHARINDEX(' ', PatientName) - 1 ELSE 0 END)) > 5
ORDER BY PatientName;''',
  'SQL Server may evaluate the conditions in any order, so the first test does not protect the second. Guard the risky part with CASE, which is evaluated in order.')

# ---------------- SET_OPERATIONS ----------------
F('SET_OPERATIONS-B06', 'Patients with no encounters with EXCEPT',
  'List patient IDs that have never had an encounter.',
  '''SELECT PatientID FROM healthcare.Patients
EXCEPT
SELECT PatientID FROM healthcare.Encounters
ORDER BY PatientID;''',
  'EXCEPT returns rows from the first query that are not in the second. Both queries must return the same number of columns with compatible types.')
F('SET_OPERATIONS-B08', 'Column names come from the first query',
  'Combine patient names and encounter references into one list with a column called Label and a Kind column.',
  '''SELECT PatientName AS Label, 'Patient' AS Kind FROM healthcare.Patients
UNION ALL
SELECT EncounterReference, 'Encounter' FROM healthcare.Encounters
ORDER BY Kind, Label;''',
  'The column names of a UNION come from the first query; aliases in the second query are ignored.')
F('SET_OPERATIONS-B09', 'Matching column count',
  'Combine patient names (text) with patient numbers (text) in one column called Label.',
  '''SELECT PatientName AS Label FROM healthcare.Patients
UNION ALL
SELECT PatientNumber FROM healthcare.Patients
ORDER BY Label;''',
  'Every query in a UNION must have the same number of columns, and matching columns must have compatible types.')
F('SET_OPERATIONS-I05', 'Regions without Open work',
  'Using EXCEPT, list regions that have encounters but none that are Open.',
  '''SELECT p.Region
FROM healthcare.Encounters AS e JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
EXCEPT
SELECT p.Region
FROM healthcare.Encounters AS e JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE e.Status = 'Open';''',
  'First list every region with encounters, then remove the regions that have an Open one. An empty result means every region has Open work.')
F('SET_OPERATIONS-I07', 'UNION with a join',
  'List everything that happened on 2024-12-31: the patient\'s name for each encounter, and the encounter reference, each on its own row with a Kind column.',
  '''SELECT p.PatientName AS Item, 'Patient' AS Kind
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE e.EncounterDate = '2024-12-31'
UNION ALL
SELECT EncounterReference, 'Encounter'
FROM healthcare.Encounters
WHERE EncounterDate = '2024-12-31'
ORDER BY Kind, Item;''',
  'Each query in a UNION can have its own joins and WHERE clause.')
F('SET_OPERATIONS-I08', 'Compare two versions of a table',
  'Data check: copy Patients into #PtCopy, change one region, then use EXCEPT to show which rows differ.',
  '''SELECT * INTO #PtCopy FROM healthcare.Patients;
UPDATE #PtCopy SET Region = 'Central' WHERE PatientID = 3;

SELECT PatientID, PatientName, PatientNumber, Region FROM #PtCopy
EXCEPT
SELECT PatientID, PatientName, PatientNumber, Region FROM healthcare.Patients;

DROP TABLE #PtCopy;''',
  'EXCEPT compares whole rows, so it finds any changed value without listing columns in a WHERE clause. It also treats NULLs as equal, unlike =.')
F('SET_OPERATIONS-A04', 'Full outer join with UNION',
  'Without FULL OUTER JOIN, list all patient IDs from Patients and Encounters with a flag showing where each appears (Both, Patients only, Encounters only).',
  '''SELECT PatientID, 'Both' AS FoundIn
FROM (SELECT PatientID FROM healthcare.Patients
      INTERSECT
      SELECT PatientID FROM healthcare.Encounters) AS b
UNION ALL
SELECT PatientID, 'Patients only'
FROM (SELECT PatientID FROM healthcare.Patients
      EXCEPT
      SELECT PatientID FROM healthcare.Encounters) AS p
UNION ALL
SELECT PatientID, 'Encounters only'
FROM (SELECT PatientID FROM healthcare.Encounters
      EXCEPT
      SELECT PatientID FROM healthcare.Patients) AS e
ORDER BY FoundIn, PatientID;''',
  'INTERSECT finds the overlap; each EXCEPT finds one side\'s leftovers. Stacked together they give a complete match report.')
F('SET_OPERATIONS-A05', 'Values shared by two groups',
  'Which months of 2024 have encounters from both a North patient and an East patient?',
  '''SELECT MONTH(e.EncounterDate) AS MonthNo
FROM healthcare.Encounters AS e JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE p.Region = 'North'
INTERSECT
SELECT MONTH(e.EncounterDate)
FROM healthcare.Encounters AS e JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE p.Region = 'East'
ORDER BY MonthNo;''',
  'INTERSECT returns the distinct values that appear in both results.')
F('SET_OPERATIONS-A07', 'Set compare: identical lists?',
  'Check whether the set of patients with Open encounters is exactly the same as the set of patients with Pending encounters. Return the count of differences in each direction.',
  '''SELECT
  (SELECT COUNT(*) FROM (SELECT PatientID FROM healthcare.Encounters WHERE Status = 'Open'
                         EXCEPT
                         SELECT PatientID FROM healthcare.Encounters WHERE Status = 'Pending') AS a) AS OpenNotPending,
  (SELECT COUNT(*) FROM (SELECT PatientID FROM healthcare.Encounters WHERE Status = 'Pending'
                         EXCEPT
                         SELECT PatientID FROM healthcare.Encounters WHERE Status = 'Open') AS b) AS PendingNotOpen;''',
  'Two sets are equal only when EXCEPT returns nothing in both directions.')
F('SET_OPERATIONS-A08', 'UNION ALL for an audit trail',
  'Build one timeline for patient 1: each encounter (as \'Encounter\') with its date, plus the date the record was entered (as \'Recorded\'), ordered by date.',
  '''SELECT EncounterDate AS EventDate, 'Encounter' AS EventType, EncounterReference AS Detail
FROM healthcare.Encounters
WHERE PatientID = 1
UNION ALL
SELECT CAST(RecordedAt AS date), 'Recorded', EncounterReference
FROM healthcare.Encounters
WHERE PatientID = 1
ORDER BY EventDate, EventType, Detail;''',
  'UNION ALL stacks different kinds of events into one list. It does not remove duplicates, which is what you want for an audit trail.')
F('SET_OPERATIONS-A09', 'EXCEPT vs NOT EXISTS with duplicates',
  'Compare EXCEPT and NOT EXISTS for \'encounters of patients without any Pending encounter\'. Show the row count from each and explain the difference.',
  '''SELECT
  (SELECT COUNT(*) FROM (SELECT PatientID FROM healthcare.Encounters
                         EXCEPT
                         SELECT PatientID FROM healthcare.Encounters WHERE Status = 'Pending') AS x) AS ExceptRows,
  (SELECT COUNT(*) FROM healthcare.Encounters AS e
   WHERE NOT EXISTS (SELECT 1 FROM healthcare.Encounters AS e2
                     WHERE e2.PatientID = e.PatientID AND e2.Status = 'Pending')) AS NotExistsRows;''',
  'EXCEPT removes duplicates, so it returns each patient once. NOT EXISTS keeps every encounter row of those patients. Choose based on whether you need distinct values or the full rows.')
