"""Replacement items for workbook questions that need tables or data a domain does not have.

Written once in AmeriMed (healthcare) vocabulary using ONLY Encounters and Patients, then translated to each domain by
translate.Translator exactly like the original items. Each replacement keeps the topic, level and SQL skill of the
original. {{XC}} / {{XV}} expand to the extra NOT NULL columns/values a domain's event table needs on INSERT.
"""

FB = {}


def F(i, title, q, sql, how):
    FB[i] = dict(title=title, q=q, sql=sql.strip('\n'), how=how)


# ---------------- AGGREGATES ----------------
F('AGGREGATES-B10', 'Average service units',
  'What is the average number of ServiceUnits per encounter, rounded to 2 decimals?',
  '''SELECT ROUND(AVG(CAST(ServiceUnits AS decimal(10,2))), 2) AS AvgServiceUnits
FROM healthcare.Encounters;''',
  'ROUND(value, 2) rounds to 2 decimal places. ServiceUnits is an int, so cast it first: AVG of an int column returns an int and drops the decimals.')
F('AGGREGATES-I04', 'Average with decimals',
  'On average, how many encounters does a patient with at least one encounter have? Show the answer with decimals.',
  '''SELECT CAST(COUNT(*) AS decimal(10,2)) / COUNT(DISTINCT PatientID) AS AvgPerPatient
FROM healthcare.Encounters;''',
  'Dividing two integers in SQL Server drops the decimals (7 / 2 = 3). Casting one side to decimal keeps them.')
F('AGGREGATES-I05', 'Charge by encounter type and status',
  'For each encounter type, show the number of encounters, the total ServiceUnits and the total charge. Highest total charge first.',
  '''SELECT EncounterType,
       COUNT(*)          AS Encounters,
       SUM(ServiceUnits) AS TotalUnits,
       SUM(Charge)       AS TotalCharge
FROM healthcare.Encounters
GROUP BY EncounterType
ORDER BY TotalCharge DESC;''',
  'Several aggregates can share one GROUP BY. Each one is calculated over the same group of rows.')
F('AGGREGATES-A10', 'Patients above their region\'s average',
  'For each patient, compare their total charge with the average patient total in the same region. Show only patients above their region\'s average.',
  '''WITH t AS (
    SELECT p.Region, e.PatientID, SUM(e.Charge) AS PatientTotal
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
    GROUP BY p.Region, e.PatientID
)
SELECT Region, PatientID, PatientTotal,
       CAST(RegionAvg AS decimal(10,2)) AS RegionAvg
FROM (SELECT *, AVG(PatientTotal) OVER (PARTITION BY Region) AS RegionAvg FROM t) AS x
WHERE PatientTotal > RegionAvg
ORDER BY Region, PatientTotal DESC;''',
  'Aggregate per patient, then AVG() OVER (PARTITION BY Region) puts the region average on each row so you can compare. Window results cannot go in WHERE directly, so wrap them in a subquery.')

# ---------------- ANALYTICAL_FUNCTIONS ----------------
F('ANALYTICAL_FUNCTIONS-B05', 'ROW_NUMBER vs RANK vs DENSE_RANK',
  'Show the three ranking functions side by side for encounters ordered by charge (highest first). Show the 10 highest rows.',
  '''SELECT TOP (10) EncounterID, Charge,
       ROW_NUMBER() OVER (ORDER BY Charge DESC) AS RowNum,
       RANK()       OVER (ORDER BY Charge DESC) AS Rnk,
       DENSE_RANK() OVER (ORDER BY Charge DESC) AS DenseRnk
FROM healthcare.Encounters
ORDER BY Charge DESC, EncounterID;''',
  'On ties: ROW_NUMBER always gives unique numbers, RANK leaves gaps, DENSE_RANK does not. Be ready to explain this in interviews.')
F('ANALYTICAL_FUNCTIONS-B10', 'Split into quartiles',
  'Split patients into 4 equal bands by their total charge (1 = highest) using NTILE.',
  '''SELECT PatientID, SUM(Charge) AS TotalCharge,
       NTILE(4) OVER (ORDER BY SUM(Charge) DESC) AS ChargeBand
FROM healthcare.Encounters
GROUP BY PatientID
ORDER BY ChargeBand, TotalCharge DESC;''',
  'NTILE(n) divides the ordered rows into n groups that are as equal in size as possible. It can rank an aggregate because window functions run after GROUP BY.')
F('ANALYTICAL_FUNCTIONS-I10', 'Percentile rank',
  'Show each encounter\'s charge and its percentile rank (0 = lowest, 1 = highest). Order by charge.',
  '''SELECT EncounterID, Charge,
       CAST(PERCENT_RANK() OVER (ORDER BY Charge) AS decimal(4,2)) AS PctRank
FROM healthcare.Encounters
ORDER BY Charge, EncounterID;''',
  'PERCENT_RANK shows where a row sits in the range: (rank - 1) / (rows - 1).')
F('ANALYTICAL_FUNCTIONS-A01', 'Top 2 encounters per region',
  'For each patient region, show the 2 highest-charge encounters. If charges tie, keep all tied rows.',
  '''WITH r AS (
    SELECT p.Region, e.EncounterID, e.Charge,
           DENSE_RANK() OVER (PARTITION BY p.Region ORDER BY e.Charge DESC) AS rnk
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
)
SELECT Region, EncounterID, Charge, rnk
FROM r
WHERE rnk <= 2
ORDER BY Region, rnk, EncounterID;''',
  'Top-N per group is the most common window-function interview question. Choose ROW_NUMBER for exactly N rows, or RANK/DENSE_RANK to keep ties, and say why.')
F('ANALYTICAL_FUNCTIONS-A02', 'Delete duplicates, keep one',
  'Interview classic: copy Encounters into #Enc and add a duplicate of every encounter of patient 1 (same PatientID, date and charge, new ID). Then keep only the first row of each duplicate group and delete the rest. Show how many rows remain.',
  '''SELECT EncounterID, PatientID, EncounterDate, Charge
INTO #Enc
FROM healthcare.Encounters;

INSERT INTO #Enc (EncounterID, PatientID, EncounterDate, Charge)
SELECT EncounterID + 10000, PatientID, EncounterDate, Charge
FROM healthcare.Encounters
WHERE PatientID = 1;

WITH d AS (
    SELECT EncounterID,
           ROW_NUMBER() OVER (PARTITION BY PatientID, EncounterDate, Charge
                              ORDER BY EncounterID) AS rn
    FROM #Enc
)
DELETE FROM d WHERE rn > 1;

SELECT COUNT(*) AS RemainingRows FROM #Enc;

DROP TABLE #Enc;''',
  'ROW_NUMBER numbers the copies inside each duplicate group. Rows with rn > 1 are the repeats, so deleting them keeps one per group. You can DELETE directly through a CTE that reads one table. Always run the SELECT part first to check what will be deleted.')
F('ANALYTICAL_FUNCTIONS-A09', 'Monthly rank of regions',
  'For each month, rank patient regions by their total charge that month and show only the top region (ties included).',
  '''WITH m AS (
    SELECT MONTH(e.EncounterDate) AS MonthNo, p.Region, SUM(e.Charge) AS Total,
           RANK() OVER (PARTITION BY MONTH(e.EncounterDate) ORDER BY SUM(e.Charge) DESC) AS rnk
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
    GROUP BY MONTH(e.EncounterDate), p.Region
)
SELECT MonthNo, Region, Total
FROM m
WHERE rnk = 1
ORDER BY MonthNo;''',
  'Join + GROUP BY + RANK partitioned by month. The window function runs after GROUP BY, so it can rank aggregated totals.')
F('ANALYTICAL_FUNCTIONS-A10', 'Repeat encounters within N days',
  'Find encounters that happened within @Days days of the same patient\'s previous encounter. Use @Days = 145. Show patient, previous date, current date and gap.',
  '''DECLARE @Days int = 145;

WITH v AS (
    SELECT PatientID, EncounterID, EncounterDate,
           LAG(EncounterDate) OVER (PARTITION BY PatientID ORDER BY EncounterDate, EncounterID) AS PrevDate
    FROM healthcare.Encounters
)
SELECT PatientID, PrevDate, EncounterDate,
       DATEDIFF(day, PrevDate, EncounterDate) AS GapDays
FROM v
WHERE PrevDate IS NOT NULL
  AND DATEDIFF(day, PrevDate, EncounterDate) <= @Days
ORDER BY PatientID, EncounterDate;''',
  'LAG finds the previous encounter and DATEDIFF measures the gap. A variable makes the window easy to change. Repeat-activity checks like this are a common interview question.')

# ---------------- CONSTRAINTS ----------------
F('CONSTRAINTS-B03', 'NOT NULL rejects missing values',
  'Try to insert a patient without a PatientName.',
  '''BEGIN TRY
    INSERT INTO healthcare.Patients (PatientID, PatientNumber, Region)
    VALUES (999, 'PT-0000999', 'North');
    SELECT 'Inserted' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'PatientName is NOT NULL, so leaving it out (it has no default) fails with error 515.')
F('CONSTRAINTS-B04', 'UNIQUE constraint',
  'Try to insert a new patient with a PatientNumber that already exists (the number of patient 1).',
  '''BEGIN TRY
    INSERT INTO healthcare.Patients (PatientID, PatientName, PatientNumber, Region)
    SELECT 999, N'Test Patient', PatientNumber, 'North'
    FROM healthcare.Patients
    WHERE PatientID = 1;
    SELECT 'Inserted' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'UNIQUE stops two rows having the same value. Unlike a primary key, a table can have many UNIQUE constraints, and a UNIQUE column can hold one NULL.')
F('CONSTRAINTS-B05', 'CHECK constraint',
  'Try to set encounter 1\'s Charge to -5.',
  '''BEGIN TRY
    UPDATE healthcare.Encounters SET Charge = -5 WHERE EncounterID = 1;
    SELECT 'Updated' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'CHECK (Charge >= 0) rejects negative amounts. Error 547 covers CHECK and FOREIGN KEY violations.')
F('CONSTRAINTS-B06', 'FOREIGN KEY rejects orphans',
  'Try to add an encounter for PatientID 5000, which does not exist.',
  '''BEGIN TRY
    INSERT INTO healthcare.Encounters
        (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge,
         ServiceUnits, EncounterDate, StartedAt, RecordedAt{{XC}})
    VALUES (9001, 5000, N'HEA-TEST-1', 'A', 'Open', 100, 1,
            '2025-01-02', '2025-01-02 09:00', '2025-01-02 09:01 +00:00'{{XV}});
    SELECT 'Inserted' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'The foreign key Encounters.PatientID -> Patients.PatientID makes sure every encounter belongs to a real patient.')
F('CONSTRAINTS-B07', 'DEFAULT fills a value',
  'Insert an encounter without giving a Status, then check which Status it got.',
  '''INSERT INTO healthcare.Encounters
    (EncounterID, PatientID, EncounterReference, EncounterType, Charge,
     ServiceUnits, EncounterDate, StartedAt, RecordedAt{{XC}})
VALUES (9002, 1, N'HEA-TEST-2', 'A', 120, 1,
        '2025-01-02', '2025-01-02 10:00', '2025-01-02 10:01 +00:00'{{XV}});

SELECT EncounterID, Status FROM healthcare.Encounters WHERE EncounterID = 9002;''',
  'Status has DEFAULT (\'Open\'), so SQL Server fills it when the INSERT leaves the column out.')
F('CONSTRAINTS-B09', 'Add a UNIQUE constraint',
  'Make sure no two encounters share the same EncounterReference and EncounterDate by adding a UNIQUE constraint on the pair.',
  '''ALTER TABLE healthcare.Encounters
ADD CONSTRAINT UQ_Encounters_RefDate UNIQUE (EncounterReference, EncounterDate);

SELECT name, type_desc FROM sys.key_constraints WHERE name = 'UQ_Encounters_RefDate';''',
  'SQL Server creates a unique index behind every UNIQUE constraint. It fails if duplicates already exist.')
F('CONSTRAINTS-B10', 'Drop a constraint',
  'Add a CHECK that ServiceUnits is at most 100000 on Encounters, then drop it.',
  '''ALTER TABLE healthcare.Encounters ADD CONSTRAINT CK_Enc_MaxUnits CHECK (ServiceUnits <= 100000);
ALTER TABLE healthcare.Encounters DROP CONSTRAINT CK_Enc_MaxUnits;

SELECT COUNT(*) AS Remaining FROM sys.check_constraints WHERE name = 'CK_Enc_MaxUnits';''',
  'Constraints are dropped by name. That is why naming constraints yourself is good practice; system-generated names are random.')
F('CONSTRAINTS-I01', 'Composite primary key',
  'Create a table healthcare.PatientCalendar with a primary key on (PatientID, CalendarDate), and show that the same patient cannot be booked twice on one date.',
  '''CREATE TABLE healthcare.PatientCalendar (
    PatientID    int  NOT NULL REFERENCES healthcare.Patients (PatientID),
    CalendarDate date NOT NULL,
    Slot         varchar(10) NOT NULL,
    CONSTRAINT PK_PatientCalendar PRIMARY KEY (PatientID, CalendarDate)
);

INSERT INTO healthcare.PatientCalendar VALUES (1, '2025-01-06', 'Morning');
BEGIN TRY
    INSERT INTO healthcare.PatientCalendar VALUES (1, '2025-01-06', 'Evening');
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'A composite key makes the combination of columns unique. Each column alone can repeat.')
F('CONSTRAINTS-I05', 'Load order from foreign keys',
  'Why must Patients be loaded before Encounters? Show it by deleting a patient who has encounters.',
  '''BEGIN TRY
    DELETE FROM healthcare.Patients WHERE PatientID = 1;
    SELECT 'Deleted' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'Parents must exist before children are inserted, and children must be deleted before parents (unless CASCADE is set). The error shows the REFERENCE constraint blocking the delete.')
F('CONSTRAINTS-I06', 'Disable and re-enable a constraint',
  'Find the CHECK on Encounters that tests Charge >= 0. Disable it, set one charge to -1, then re-enable the CHECK WITH CHECK and see what happens.',
  '''DECLARE @ck sysname = (SELECT name FROM sys.check_constraints
                       WHERE parent_object_id = OBJECT_ID('healthcare.Encounters')
                         AND definition LIKE '%Charge%>=%0%');
DECLARE @sql nvarchar(400);

SET @sql = N'ALTER TABLE healthcare.Encounters NOCHECK CONSTRAINT ' + QUOTENAME(@ck);
EXEC (@sql);
UPDATE healthcare.Encounters SET Charge = -1 WHERE EncounterID = 1;

BEGIN TRY
    SET @sql = N'ALTER TABLE healthcare.Encounters WITH CHECK CHECK CONSTRAINT ' + QUOTENAME(@ck);
    EXEC (@sql);
    SELECT 'Re-enabled' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'NOCHECK lets bad data in. Re-enabling WITH CHECK validates existing rows and fails on the bad one. Re-enabling without WITH CHECK leaves the constraint "not trusted", and the optimizer then ignores it. The constraint name is looked up first because system-generated names differ between databases.')
F('CONSTRAINTS-I10', 'Default from a function',
  'Add a CreatedOn column to Patients that defaults to today\'s date.',
  '''ALTER TABLE healthcare.Patients
ADD CreatedOn date NOT NULL CONSTRAINT DF_Patients_CreatedOn DEFAULT (CAST(GETDATE() AS date));
GO
SELECT COUNT(DISTINCT CreatedOn) AS DistinctDates FROM healthcare.Patients;''',
  'A DEFAULT can call a function. Every existing row gets today\'s date because the column is NOT NULL.')
F('CONSTRAINTS-A03', 'Self-referencing foreign key',
  'Encounters.ParentEncounterID references Encounters.EncounterID. Try to point encounter 2 to a parent that does not exist, and try to point encounter 2 to itself.',
  '''BEGIN TRY
    UPDATE healthcare.Encounters SET ParentEncounterID = 99999 WHERE EncounterID = 2;
END TRY
BEGIN CATCH
    SELECT 'Missing parent' AS Test, ERROR_NUMBER() AS ErrorNo;
END CATCH;

BEGIN TRY
    UPDATE healthcare.Encounters SET ParentEncounterID = 2 WHERE EncounterID = 2;
END TRY
BEGIN CATCH
    SELECT 'Self parent' AS Test, ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'The self-referencing FK blocks missing parents. The CHECK `ParentEncounterID <> EncounterID` blocks a row being its own parent. The result shows the second test. In this data set the parent column is empty for every row, but the rules still apply.')
F('CONSTRAINTS-A04', 'Cascade risks with self-references',
  'Explain why ON DELETE CASCADE cannot be added to the self-referencing key on Encounters. Try it.',
  '''DECLARE @fk sysname = (SELECT name FROM sys.foreign_keys
                       WHERE parent_object_id = OBJECT_ID('healthcare.Encounters')
                         AND referenced_object_id = OBJECT_ID('healthcare.Encounters'));
DECLARE @sql nvarchar(400) = N'ALTER TABLE healthcare.Encounters DROP CONSTRAINT ' + QUOTENAME(@fk);
EXEC (@sql);

BEGIN TRY
    ALTER TABLE healthcare.Encounters
    ADD CONSTRAINT FK_Encounters_Parent_Cascade FOREIGN KEY (ParentEncounterID)
        REFERENCES healthcare.Encounters (EncounterID) ON DELETE CASCADE;
    SELECT 'Added' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'SQL Server does not allow cascading actions that could loop (cycles or multiple cascade paths). It raises error 1785 and then 1750 ("Could not create constraint"); CATCH shows the last one. Delete child rows first, or use a recursive CTE to remove a whole chain.')
F('CONSTRAINTS-A05', 'Business rule across tables',
  'A CHECK cannot look at other tables. Write a trigger that stops new encounters being added for patients in the East region, then test it.',
  '''CREATE TRIGGER healthcare.trg_Enc_NoEast
ON healthcare.Encounters
AFTER INSERT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted AS i
               JOIN healthcare.Patients AS p ON p.PatientID = i.PatientID
               WHERE p.Region = 'East')
        THROW 50001, 'New encounters are not allowed for East patients.', 1;
END;
GO
DECLARE @east int = (SELECT MIN(PatientID) FROM healthcare.Patients WHERE Region = 'East');
BEGIN TRY
    INSERT INTO healthcare.Encounters
        (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge,
         ServiceUnits, EncounterDate, StartedAt, RecordedAt{{XC}})
    VALUES (9003, @east, N'HEA-TEST-3', 'A', 'Open', 100, 1,
            '2025-01-02', '2025-01-02 09:00', '2025-01-02 09:01 +00:00'{{XV}});
    SELECT 'Inserted' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo, ERROR_MESSAGE() AS Message;
END CATCH;''',
  'Rules that need data from other tables are enforced with triggers (or in the application). `inserted` holds the new rows. The patient is in the East region, so the insert is rejected.')
F('CONSTRAINTS-A07', 'Find orphans before adding a FK',
  'A copy of Encounters has a row pointing to a missing patient. Find the orphan rows before adding a foreign key.',
  '''SELECT EncounterID, PatientID INTO #EncCopy FROM healthcare.Encounters;
INSERT INTO #EncCopy VALUES (9999, 7777);

SELECT c.EncounterID, c.PatientID
FROM #EncCopy AS c
LEFT JOIN healthcare.Patients AS p ON p.PatientID = c.PatientID
WHERE p.PatientID IS NULL;

DROP TABLE #EncCopy;''',
  'Adding a FK to data with orphans fails. Find them with an anti-join, then fix or remove them first. This is common during data migrations.')
F('CONSTRAINTS-A08', 'Cascade an update',
  'Create a small parent/child pair (Teams, TeamMembers) with ON UPDATE CASCADE, change a team code, and show the members follow.',
  '''CREATE TABLE healthcare.Teams (TeamCode varchar(5) PRIMARY KEY);
CREATE TABLE healthcare.TeamMembers (
    MemberID int PRIMARY KEY,
    TeamCode varchar(5) NOT NULL
        REFERENCES healthcare.Teams (TeamCode) ON UPDATE CASCADE
);
INSERT INTO healthcare.Teams VALUES ('T1');
INSERT INTO healthcare.TeamMembers VALUES (1, 'T1'), (2, 'T1');

UPDATE healthcare.Teams SET TeamCode = 'OPS' WHERE TeamCode = 'T1';

SELECT MemberID, TeamCode FROM healthcare.TeamMembers;''',
  'ON UPDATE CASCADE changes child keys when the parent key changes. This is only needed with natural keys; surrogate (ID) keys never change, which is one reason they are preferred.')
F('CONSTRAINTS-A09', 'Validate before insert',
  'Insert three new patient notes from a staging list into a new table healthcare.PatientNotes, but only those whose PatientID exists, so no FK error is raised. Show how many were inserted.',
  '''CREATE TABLE healthcare.PatientNotes (
    NoteID    int NOT NULL PRIMARY KEY,
    PatientID int NOT NULL REFERENCES healthcare.Patients (PatientID),
    NoteText  nvarchar(100) NOT NULL
);

DECLARE @Staging TABLE (NoteID int, PatientID int, NoteText nvarchar(100));
INSERT INTO @Staging VALUES
    (1, 5,    N'Called back'),
    (2, 9999, N'Unknown patient'),   -- bad patient
    (3, 6,    N'Address checked');

INSERT INTO healthcare.PatientNotes (NoteID, PatientID, NoteText)
SELECT s.NoteID, s.PatientID, s.NoteText
FROM @Staging AS s
WHERE EXISTS (SELECT 1 FROM healthcare.Patients AS p WHERE p.PatientID = s.PatientID);

SELECT COUNT(*) AS Inserted FROM healthcare.PatientNotes;''',
  'Filtering staging rows with EXISTS keeps good rows and skips bad ones without failing the whole batch. In ETL jobs, the rejected rows usually go to an error table.')

# ---------------- CTE ----------------
F('CTE-B02', 'CTE with a calculation',
  'Use a CTE to calculate the charge per service unit (Charge / ServiceUnits) for each encounter, then list the 10 encounters with the highest charge per unit.',
  '''WITH PerUnit AS (
    SELECT EncounterID, Charge, ServiceUnits,
           CAST(Charge / ServiceUnits AS decimal(12,2)) AS ChargePerUnit
    FROM healthcare.Encounters
)
SELECT TOP (10) EncounterID, Charge, ServiceUnits, ChargePerUnit
FROM PerUnit
ORDER BY ChargePerUnit DESC, EncounterID;''',
  'A CTE lets you filter or sort on a calculated column (ChargePerUnit) without repeating the formula.')
F('CTE-B06', 'Readable column names',
  'Write a CTE with a column list (ID, Name) over Patients, and select from it.',
  '''WITH Pt (ID, Name) AS (
    SELECT PatientID, PatientName
    FROM healthcare.Patients
)
SELECT ID, Name
FROM Pt
ORDER BY Name;''',
  'You can name the CTE\'s columns in brackets after its name instead of using aliases inside.')
F('CTE-B10', 'Encounters with names via CTE',
  'Use a CTE that joins Encounters to Patients, then return the 5 highest charges with the patient names.',
  '''WITH Enc AS (
    SELECT e.EncounterReference, p.PatientName, e.Charge
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
)
SELECT TOP (5) EncounterReference, PatientName, Charge
FROM Enc
ORDER BY Charge DESC, EncounterReference;''',
  'Hide the joins in the CTE, then keep the final query short.')
F('CTE-I06', 'Encounter chain for one patient',
  'Starting from patient 1\'s first encounter, use a recursive CTE to walk forward through that patient\'s encounters in date order, with a step number.',
  '''WITH Ordered AS (
    SELECT EncounterID, EncounterDate,
           ROW_NUMBER() OVER (ORDER BY EncounterDate, EncounterID) AS rn
    FROM healthcare.Encounters
    WHERE PatientID = 1
), Chain AS (
    SELECT EncounterID, EncounterDate, rn, 0 AS Step
    FROM Ordered
    WHERE rn = 1
    UNION ALL
    SELECT o.EncounterID, o.EncounterDate, o.rn, c.Step + 1
    FROM Ordered AS o
    JOIN Chain AS c ON o.rn = c.rn + 1
)
SELECT EncounterID, EncounterDate, Step
FROM Chain
ORDER BY Step;''',
  'The anchor picks the starting row. The recursive part finds the next row (rn + 1) one step at a time. The same shape walks hierarchies such as org charts or bills of materials.')
F('CTE-I09', 'Patient summary in steps',
  'Build a summary per patient: number of encounters, total charge and number of Open encounters, using one CTE per measure. Include patients with no encounters.',
  '''WITH V AS (
    SELECT PatientID, COUNT(*) AS Encounters, SUM(Charge) AS TotalCharge
    FROM healthcare.Encounters GROUP BY PatientID
), O AS (
    SELECT PatientID, COUNT(*) AS OpenEncounters
    FROM healthcare.Encounters
    WHERE Status = 'Open'
    GROUP BY PatientID
)
SELECT p.PatientName, ISNULL(V.Encounters, 0) AS Encounters,
       ISNULL(V.TotalCharge, 0) AS TotalCharge, ISNULL(O.OpenEncounters, 0) AS OpenEncounters
FROM healthcare.Patients AS p
LEFT JOIN V ON V.PatientID = p.PatientID
LEFT JOIN O ON O.PatientID = p.PatientID
ORDER BY TotalCharge DESC, p.PatientName;''',
  'Aggregating each measure in its own CTE and then LEFT JOINing keeps patients with no rows and avoids double counting.')
F('CTE-A01', 'Top 3 patients by charge per region',
  'For each region, show the 3 patients with the highest total charge.',
  '''WITH Spend AS (
    SELECT p.Region, p.PatientName, SUM(e.Charge) AS TotalCharge
    FROM healthcare.Encounters AS e
    JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
    GROUP BY p.Region, p.PatientID, p.PatientName
), Ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY Region ORDER BY TotalCharge DESC, PatientName) AS rn
    FROM Spend
)
SELECT Region, PatientName, TotalCharge
FROM Ranked
WHERE rn <= 3
ORDER BY Region, rn;''',
  'CTE 1 joins and aggregates, CTE 2 ranks, the final SELECT filters. This 3-step shape solves most "top N per group" interview questions.')
F('CTE-A03', 'Org-chart style hierarchy with path',
  'Build a small hierarchy in a table variable (region head > team > patient) and list it with a recursive CTE, showing each level and a path like Head > North > Olivia.',
  '''DECLARE @Org TABLE (NodeID int, ParentID int NULL, NodeName nvarchar(100));
INSERT INTO @Org VALUES (0, NULL, N'Head');
INSERT INTO @Org
SELECT DENSE_RANK() OVER (ORDER BY Region), 0, Region
FROM healthcare.Patients
GROUP BY Region;
INSERT INTO @Org
SELECT 100 + p.PatientID, r.NodeID, p.PatientName
FROM healthcare.Patients AS p
JOIN @Org AS r ON r.NodeName = p.Region
WHERE p.PatientID <= 6;

WITH Tree AS (
    SELECT NodeID, NodeName, 0 AS Lvl, CAST(NodeName AS nvarchar(400)) AS PathText
    FROM @Org
    WHERE ParentID IS NULL
    UNION ALL
    SELECT o.NodeID, o.NodeName, t.Lvl + 1,
           CAST(t.PathText + N' > ' + o.NodeName AS nvarchar(400))
    FROM @Org AS o
    JOIN Tree AS t ON o.ParentID = t.NodeID
)
SELECT NodeID, Lvl, PathText
FROM Tree
ORDER BY PathText;''',
  'Building a path string in the recursion shows the full lineage. The CAST to the same type and size in both parts is required, or SQL Server raises a type-mismatch error.')
F('CTE-A04', 'Deepest level in a hierarchy',
  'Using a parent/child list in a table variable, find how deep the deepest branch goes and which leaf nodes are at that depth.',
  '''DECLARE @Tree TABLE (NodeID int, ParentID int NULL);
INSERT INTO @Tree VALUES (1, NULL), (2, 1), (3, 1), (4, 2), (5, 4), (6, 3), (7, 5);

WITH Walk AS (
    SELECT NodeID, 0 AS Lvl FROM @Tree WHERE ParentID IS NULL
    UNION ALL
    SELECT t.NodeID, w.Lvl + 1
    FROM @Tree AS t
    JOIN Walk AS w ON t.ParentID = w.NodeID
)
SELECT TOP (1) WITH TIES NodeID, Lvl AS Depth
FROM Walk
ORDER BY Lvl DESC;''',
  'Carry the level down through the recursion. TOP (1) WITH TIES returns every node that shares the greatest depth.')
F('CTE-A06', 'Find missing IDs',
  'Interview classic: find missing numbers in an ID column. Copy the encounter IDs into #Ids, delete IDs 5 and 10 as setup, then find every missing ID between 1 and the highest ID.',
  '''SELECT EncounterID INTO #Ids FROM healthcare.Encounters;
DELETE FROM #Ids WHERE EncounterID IN (5, 10);   -- setup

DECLARE @MaxID int = (SELECT MAX(EncounterID) FROM #Ids);

WITH N AS (
    SELECT 1 AS id
    UNION ALL
    SELECT id + 1 FROM N WHERE id < @MaxID
)
SELECT n.id AS MissingID
FROM N AS n
LEFT JOIN #Ids AS i ON i.EncounterID = n.id
WHERE i.EncounterID IS NULL
OPTION (MAXRECURSION 1000);

DROP TABLE #Ids;''',
  'Generate every expected number, then anti-join to find those not present. The maximum goes into a variable first, because the recursive part of a CTE cannot contain an aggregate.')

# ---------------- DATABASE_SCHEMA_USER ----------------
F('DATABASE_SCHEMA_USER-I04', 'Database roles',
  'Create a role ops_reader, give it SELECT on Encounters and Patients, and add report_reader to it.',
  '''CREATE ROLE ops_reader;
GRANT SELECT ON healthcare.Encounters TO ops_reader;
GRANT SELECT ON healthcare.Patients   TO ops_reader;

CREATE USER report_reader WITHOUT LOGIN;
ALTER ROLE ops_reader ADD MEMBER report_reader;

SELECT r.name AS RoleName, m.name AS MemberName
FROM sys.database_role_members AS rm
JOIN sys.database_principals AS r ON r.principal_id = rm.role_principal_id
JOIN sys.database_principals AS m ON m.principal_id = rm.member_principal_id
WHERE r.name = 'ops_reader';''',
  'Grant permissions to roles, then add users to roles. Managing roles is much easier than managing many individual users.')

# ---------------- DATATYPES ----------------
F('DATATYPES-B04', 'Decimal precision and scale',
  'What do the numbers in decimal(12,2) mean? Show the precision and scale of Encounters.Charge.',
  '''SELECT name, TYPE_NAME(user_type_id) AS DataType, precision, scale
FROM sys.columns
WHERE object_id = OBJECT_ID('healthcare.Encounters') AND name = 'Charge';''',
  'Precision is the total number of digits (12) and scale is how many of them come after the decimal point (2).')
F('DATATYPES-I08', 'Money calculation with the right scale',
  'Calculate each encounter\'s charge per service unit and show it as decimal(10,2). Show the first 10 encounters.',
  '''SELECT TOP (10) EncounterID, Charge, ServiceUnits,
       CAST(Charge / ServiceUnits AS decimal(10,2)) AS ChargePerUnit
FROM healthcare.Encounters
ORDER BY EncounterID;''',
  'Dividing decimals can give many decimal places. CAST to decimal(10,2) rounds the result to cents.')
F('DATATYPES-A08', 'sql_variant and type checking',
  'Show the base type, precision and scale of Charge, Charge * ServiceUnits, and AVG(Charge).',
  '''SELECT 'Charge' AS Expr,
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge), 'BaseType') AS varchar(20))  AS BaseType,
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge), 'Precision') AS varchar(20)) AS Prec,
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge), 'Scale') AS varchar(20))     AS Scale
FROM healthcare.Encounters
UNION ALL
SELECT 'Charge * ServiceUnits',
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge * ServiceUnits), 'BaseType') AS varchar(20)),
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge * ServiceUnits), 'Precision') AS varchar(20)),
       CAST(SQL_VARIANT_PROPERTY(MAX(Charge * ServiceUnits), 'Scale') AS varchar(20))
FROM healthcare.Encounters
UNION ALL
SELECT 'AVG(Charge)',
       CAST(SQL_VARIANT_PROPERTY(AVG(Charge), 'BaseType') AS varchar(20)),
       CAST(SQL_VARIANT_PROPERTY(AVG(Charge), 'Precision') AS varchar(20)),
       CAST(SQL_VARIANT_PROPERTY(AVG(Charge), 'Scale') AS varchar(20))
FROM healthcare.Encounters;''',
  'SQL Server works out the result type of every expression. Multiplying a decimal by an int keeps the decimal scale; AVG of decimal(12,2) returns decimal(38,6). SQL_VARIANT_PROPERTY shows the type it chose.')
