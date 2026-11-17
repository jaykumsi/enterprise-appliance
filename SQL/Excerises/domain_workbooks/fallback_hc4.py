"""Replacement items, part 4: STRING_FUNCTIONS, SUBQUERIES (see fallback_hc.py)."""
from fallback_hc import F

# ---------------- STRING_FUNCTIONS ----------------
F('STRING_FUNCTIONS-B01', 'Length of text',
  'Show each patient name and how many characters it has.',
  '''SELECT PatientName, LEN(PatientName) AS NameLength
FROM healthcare.Patients
ORDER BY PatientID;''',
  'LEN counts characters, ignoring trailing spaces. DATALENGTH counts bytes (2 per character for nvarchar).')
F('STRING_FUNCTIONS-B02', 'Upper and lower case',
  'Show each patient\'s name in UPPER case and in lower case.',
  '''SELECT PatientName, UPPER(PatientName) AS Upper, LOWER(PatientName) AS Lower
FROM healthcare.Patients
ORDER BY PatientID;''',
  'UPPER and LOWER change letter case. They are often used to compare text regardless of case.')
F('STRING_FUNCTIONS-B03', 'First characters',
  'Show the first 3 characters of each encounter reference.',
  '''SELECT EncounterReference, LEFT(EncounterReference, 3) AS Prefix
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'LEFT(text, n) returns the first n characters; RIGHT returns the last n.')
F('STRING_FUNCTIONS-B07', 'Replace text',
  'Show each encounter reference with the dashes replaced by slashes.',
  '''SELECT EncounterReference, REPLACE(EncounterReference, '-', '/') AS WithSlashes
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'REPLACE(text, find, with) swaps every occurrence of find.')
F('STRING_FUNCTIONS-B10', 'Reverse text',
  'Show each patient number written backwards.',
  '''SELECT PatientNumber, REVERSE(PatientNumber) AS Backwards
FROM healthcare.Patients
ORDER BY PatientID;''',
  'REVERSE flips the characters. On its own it is rarely useful, but it is the trick behind "find the last occurrence" problems.')
F('STRING_FUNCTIONS-I03', 'Number from a code',
  'Turn the sequence number at the end of each encounter reference (the part after the last dash) into an integer.',
  '''SELECT EncounterReference,
       CAST(RIGHT(EncounterReference, CHARINDEX('-', REVERSE(EncounterReference)) - 1) AS int) AS SeqNo
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'REVERSE + CHARINDEX finds the last dash; RIGHT takes what follows; CAST turns the text into a number, dropping leading zeros.')
F('STRING_FUNCTIONS-I05', 'Date inside a reference',
  'Extract the date part (the 8 digits between the dashes) from each encounter reference and convert it to a date.',
  '''SELECT EncounterReference,
       CONVERT(date, SUBSTRING(EncounterReference, CHARINDEX('-', EncounterReference) + 1, 8), 112) AS RefDate
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'SUBSTRING(text, start, length) cuts out a piece; CHARINDEX finds where it starts. CONVERT style 112 reads yyyymmdd.')
F('STRING_FUNCTIONS-I06', 'Count a character',
  'Count how many spaces are in each patient name.',
  '''SELECT PatientName,
       LEN(PatientName) - LEN(REPLACE(PatientName, ' ', '')) AS Spaces
FROM healthcare.Patients
ORDER BY PatientID;''',
  'Remove the character and compare the lengths: the difference is how many times it appeared.')
F('STRING_FUNCTIONS-I08', 'Case-insensitive search',
  'Find patients whose name contains \'AN\' regardless of case, and show the position where it starts.',
  '''SELECT PatientName, CHARINDEX('an', LOWER(PatientName)) AS StartsAt
FROM healthcare.Patients
WHERE CHARINDEX('an', LOWER(PatientName)) > 0
ORDER BY PatientName;''',
  'CHARINDEX returns the position of the first match, or 0 if there is none. Lowering both sides makes it case-insensitive.')
F('STRING_FUNCTIONS-I09', 'STRING_AGG',
  'For each region, list the encounter references from December 2024 in one comma-separated cell.',
  '''SELECT p.Region,
       STRING_AGG(e.EncounterReference, ', ') WITHIN GROUP (ORDER BY e.EncounterReference) AS RefList
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
WHERE e.EncounterDate >= '2024-12-01'
GROUP BY p.Region
ORDER BY p.Region;''',
  'STRING_AGG joins text values from a group with a separator. WITHIN GROUP sets the order of the items.')
F('STRING_FUNCTIONS-A01', 'Last word of a name',
  'Return the last word of each patient name, using REVERSE.',
  '''SELECT PatientName,
       RIGHT(PatientName, CHARINDEX(' ', REVERSE(PatientName) + ' ') - 1) AS LastWord
FROM healthcare.Patients
ORDER BY PatientID;''',
  'REVERSE turns "last space" into "first space", which CHARINDEX can find. Adding a space protects names with no space at all.')
F('STRING_FUNCTIONS-A02', 'Validate a code format',
  'Find encounter references that are NOT in the format PREFIX-yyyymmdd-nnnnn (letters, a dash, 8 digits, a dash, 5 digits).',
  '''SELECT EncounterReference
FROM healthcare.Encounters
WHERE EncounterReference NOT LIKE '[A-Z][A-Z][A-Z]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]';''',
  'LIKE with [0-9] and [A-Z] checks each position. An empty result means every reference is valid. Run this before adding a CHECK constraint.')
F('STRING_FUNCTIONS-A06', 'Group by the first word',
  'Group patients by the first word of their name and show how many patients share it and the list of their regions. Only first words used by 2 or more patients.',
  '''WITH f AS (
    SELECT LEFT(PatientName, CHARINDEX(' ', PatientName + ' ') - 1) AS FirstWord, Region
    FROM healthcare.Patients
)
SELECT FirstWord, COUNT(*) AS Patients,
       STRING_AGG(Region, ', ') WITHIN GROUP (ORDER BY Region) AS Regions
FROM f
GROUP BY FirstWord
HAVING COUNT(*) >= 2
ORDER BY Patients DESC, FirstWord;''',
  'Extract the group key with string functions in a CTE, then group by it like any column.')
F('STRING_FUNCTIONS-A10', 'Compare text ignoring spaces and case',
  'Someone typed patient 1\'s name in capitals with two spaces at both ends. Check whether that typed value matches any patient name when spaces at the ends and case are ignored.',
  '''DECLARE @typed nvarchar(100) = (SELECT N'  ' + UPPER(PatientName) + N'  ' FROM healthcare.Patients WHERE PatientID = 1);

SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE LOWER(LTRIM(RTRIM(PatientName))) = LOWER(LTRIM(RTRIM(@typed)));''',
  'LTRIM/RTRIM (or TRIM in SQL Server 2017+) remove spaces at the ends; LOWER makes the comparison case-insensitive. Clean typed input like this before matching.')

# ---------------- SUBQUERIES ----------------
F('SUBQUERIES-B02', 'Highest charge',
  'Show the encounter with the highest charge, using a subquery.',
  '''SELECT EncounterID, Charge
FROM healthcare.Encounters
WHERE Charge = (SELECT MAX(Charge) FROM healthcare.Encounters)
ORDER BY EncounterID;''',
  'The subquery returns one value (the maximum). The outer query finds the row(s) with that value; ties all appear.')
F('SUBQUERIES-B06', 'Subquery in SELECT',
  'Show each encounter with the overall average charge next to it.',
  '''SELECT EncounterID, Charge,
       (SELECT AVG(Charge) FROM healthcare.Encounters) AS AvgCharge
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'A subquery in SELECT that returns one value is repeated on every row.')
F('SUBQUERIES-B07', 'Patients that have encounters',
  'List the patients that appear in at least one encounter, using IN.',
  '''SELECT PatientID, PatientName
FROM healthcare.Patients
WHERE PatientID IN (SELECT PatientID FROM healthcare.Encounters)
ORDER BY PatientID;''',
  'IN (subquery) keeps rows whose value is in the list the subquery returns.')
F('SUBQUERIES-B10', 'Below a given encounter',
  'List encounters with a charge lower than encounter 1\'s charge.',
  '''SELECT EncounterID, Charge
FROM healthcare.Encounters
WHERE Charge < (SELECT Charge FROM healthcare.Encounters WHERE EncounterID = 1)
ORDER BY Charge DESC, EncounterID;''',
  'The subquery must return exactly one value when used with <, >, or =. Otherwise SQL Server raises an error.')
F('SUBQUERIES-I02', 'NOT EXISTS',
  'List patients that never had a Pending encounter, using NOT EXISTS.',
  '''SELECT p.PatientID, p.PatientName
FROM healthcare.Patients AS p
WHERE NOT EXISTS (SELECT 1 FROM healthcare.Encounters AS e
                  WHERE e.PatientID = p.PatientID AND e.Status = 'Pending')
ORDER BY p.PatientID;''',
  'NOT EXISTS is true when the correlated subquery finds no row. It is safe with NULLs, unlike NOT IN.')
F('SUBQUERIES-I04', 'Count in a SELECT subquery',
  'Show each patient with the number of encounters they had, using a subquery in SELECT.',
  '''SELECT p.PatientID, p.PatientName,
       (SELECT COUNT(*) FROM healthcare.Encounters AS e WHERE e.PatientID = p.PatientID) AS Encounters
FROM healthcare.Patients AS p
ORDER BY Encounters DESC, p.PatientID;''',
  'A correlated subquery runs once per outer row, using that row\'s PatientID. Patients with none get 0, not NULL, because COUNT(*) of no rows is 0.')
F('SUBQUERIES-I07', 'ANY / ALL',
  'List encounters whose charge is higher than ALL charges of type C encounters.',
  '''SELECT EncounterID, EncounterType, Charge
FROM healthcare.Encounters
WHERE Charge > ALL (SELECT Charge FROM healthcare.Encounters WHERE EncounterType = 'C')
ORDER BY Charge DESC, EncounterID;''',
  '> ALL means "greater than the largest value"; > ANY means "greater than the smallest". If the list is empty, ALL is true for every row.')
F('SUBQUERIES-I10', 'Encounters of the top patient',
  'List the encounters of the patient with the highest total charge.',
  '''SELECT EncounterID, EncounterDate, Charge
FROM healthcare.Encounters
WHERE PatientID = (SELECT TOP (1) PatientID
                   FROM healthcare.Encounters
                   GROUP BY PatientID
                   ORDER BY SUM(Charge) DESC, PatientID)
ORDER BY EncounterDate;''',
  'A subquery can contain GROUP BY and ORDER BY with TOP. TOP (1) makes sure it returns a single value for the = comparison.')
F('SUBQUERIES-A01', 'NOT IN and the NULL trap',
  'Interview trap: show why NOT IN fails when the list contains NULL. Find encounters that are not a parent of any other encounter, first with NOT IN (wrong), then with NOT EXISTS (right).',
  '''SELECT
  (SELECT COUNT(*) FROM healthcare.Encounters AS e
   WHERE e.EncounterID NOT IN (SELECT ParentEncounterID
                               FROM healthcare.Encounters)) AS NotIn_Wrong,
  (SELECT COUNT(*) FROM healthcare.Encounters AS e
   WHERE NOT EXISTS (SELECT 1 FROM healthcare.Encounters AS c
                     WHERE c.ParentEncounterID = e.EncounterID)) AS NotExists_Right;''',
  'ParentEncounterID is NULL on every row here. `x NOT IN (..., NULL)` is never true, so NOT IN returns 0. NOT EXISTS ignores the NULLs and correctly finds that no encounter is a parent. You can also fix NOT IN by adding `WHERE ParentEncounterID IS NOT NULL` inside the subquery.')
F('SUBQUERIES-A03', 'Patients with repeat types',
  'Find patients who had the same encounter type more than once, using EXISTS.',
  '''SELECT p.PatientID, p.PatientName
FROM healthcare.Patients AS p
WHERE EXISTS (SELECT 1
              FROM healthcare.Encounters AS e
              WHERE e.PatientID = p.PatientID
              GROUP BY e.EncounterType
              HAVING COUNT(*) > 1)
ORDER BY p.PatientID;''',
  'The correlated subquery groups one patient\'s encounters by type; EXISTS is true if any type appears more than once.')
F('SUBQUERIES-A05', 'Patients whose every encounter is Closed',
  'List patients who have encounters and all of them are Closed.',
  '''SELECT p.PatientID, p.PatientName
FROM healthcare.Patients AS p
WHERE EXISTS (SELECT 1 FROM healthcare.Encounters AS e WHERE e.PatientID = p.PatientID)
  AND NOT EXISTS (SELECT 1 FROM healthcare.Encounters AS e
                  WHERE e.PatientID = p.PatientID AND e.Status <> 'Closed')
ORDER BY p.PatientID;''',
  '"All are X" is written as "has some, and none are not X". Without the first EXISTS, patients with no encounters would also qualify.')
F('SUBQUERIES-A06', 'Rank without window functions',
  'Rank the 10 highest charges (1 = highest) using a correlated subquery instead of RANK().',
  '''SELECT TOP (10) e.EncounterID, e.Charge,
       (SELECT COUNT(*) FROM healthcare.Encounters AS x WHERE x.Charge > e.Charge) + 1 AS ChargeRank
FROM healthcare.Encounters AS e
ORDER BY ChargeRank, e.EncounterID;''',
  'Counting how many rows are higher, plus 1, gives the same result as RANK(). It is slower on large tables, but interviewers ask it to test understanding.')
F('SUBQUERIES-A08', 'Encounters after a patient\'s first Pending one',
  'For each patient who has a Pending encounter, count how many of their encounters happened after their first Pending encounter.',
  '''SELECT p.PatientID,
       (SELECT COUNT(*) FROM healthcare.Encounters AS e
        WHERE e.PatientID = p.PatientID
          AND e.EncounterDate > (SELECT MIN(e2.EncounterDate) FROM healthcare.Encounters AS e2
                                 WHERE e2.PatientID = p.PatientID AND e2.Status = 'Pending')) AS LaterEncounters
FROM healthcare.Patients AS p
WHERE EXISTS (SELECT 1 FROM healthcare.Encounters AS e WHERE e.PatientID = p.PatientID AND e.Status = 'Pending')
ORDER BY LaterEncounters DESC, p.PatientID;''',
  'Subqueries can be nested: the inner one finds each patient\'s first Pending date, the middle one counts encounters after it.')
F('SUBQUERIES-A10', 'Above their group\'s average',
  'List encounters whose charge is more than the average charge of their own encounter type.',
  '''SELECT e.EncounterID, e.EncounterType, e.Charge
FROM healthcare.Encounters AS e
WHERE e.Charge > (SELECT AVG(x.Charge) FROM healthcare.Encounters AS x
                  WHERE x.EncounterType = e.EncounterType)
ORDER BY e.EncounterType, e.Charge DESC, e.EncounterID;''',
  'The correlated subquery calculates the average for the current row\'s type. AVG() OVER (PARTITION BY ...) is the window-function alternative.')
