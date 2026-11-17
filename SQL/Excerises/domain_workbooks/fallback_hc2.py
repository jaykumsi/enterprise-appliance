"""Replacement items, part 2: DDL, DML, DQL, INTRODUCTION (see fallback_hc.py)."""
from fallback_hc import F

# ---------------- DDL ----------------
F('DDL-B04', 'Add a column with a default',
  'Add a column IsActive (bit, not null) to healthcare.Patients with a default value of 1.',
  '''ALTER TABLE healthcare.Patients
ADD IsActive bit NOT NULL CONSTRAINT DF_Patients_IsActive DEFAULT (1);
GO
SELECT IsActive, COUNT(*) AS Patients FROM healthcare.Patients GROUP BY IsActive;''',
  'Adding a NOT NULL column to a table that has rows needs a DEFAULT, so SQL Server can fill the existing rows.')
F('DDL-B06', 'Drop a column',
  'Add a temporary column TempNote to Patients, then drop it.',
  '''ALTER TABLE healthcare.Patients ADD TempNote varchar(50) NULL;
ALTER TABLE healthcare.Patients DROP COLUMN TempNote;

SELECT COUNT(*) AS TempNoteColumns
FROM sys.columns
WHERE object_id = OBJECT_ID('healthcare.Patients') AND name = 'TempNote';''',
  'DROP COLUMN removes the column and its data. It fails if a constraint or index still uses the column, so drop those first.')
F('DDL-B09', 'TRUNCATE vs DELETE',
  'Copy Encounters into a temp table #Enc, then remove all rows from the copy with TRUNCATE and check the count.',
  '''SELECT * INTO #Enc FROM healthcare.Encounters;

TRUNCATE TABLE #Enc;

SELECT COUNT(*) AS RowsLeft FROM #Enc;
DROP TABLE #Enc;''',
  'TRUNCATE removes all rows quickly by deallocating pages and resets IDENTITY. It cannot have a WHERE clause and is not allowed on a table referenced by a foreign key. DELETE removes rows one by one and can filter.')
F('DDL-I02', 'Computed column',
  'Add a computed column ChargePerUnit to a copy of Encounters that equals Charge / ServiceUnits. Show the first 3 rows.',
  '''SELECT EncounterID, Charge, ServiceUnits INTO #Enc FROM healthcare.Encounters;

ALTER TABLE #Enc ADD ChargePerUnit AS CAST(Charge / ServiceUnits AS decimal(12,2));

SELECT TOP (3) EncounterID, ServiceUnits, ChargePerUnit FROM #Enc ORDER BY EncounterID;
DROP TABLE #Enc;''',
  'A computed column is calculated from other columns when you read it. Add PERSISTED to store it, which also lets you index it.')
F('DDL-I03', 'Create a view',
  'Create a view healthcare.vEncounterDetails showing encounter ID, date, patient name, region and charge.',
  '''CREATE VIEW healthcare.vEncounterDetails AS
SELECT e.EncounterID, e.EncounterDate, p.PatientName, p.Region, e.Charge
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID;
GO
SELECT TOP (3) * FROM healthcare.vEncounterDetails ORDER BY EncounterID;''',
  'A view is a saved query that behaves like a table. CREATE VIEW must be the only statement in its batch, which is why GO comes after it.')
F('DDL-I10', 'Schema-bound view',
  'Create a view WITH SCHEMABINDING over Patients and confirm it is schema-bound.',
  '''CREATE VIEW healthcare.vPatientNames
WITH SCHEMABINDING
AS
SELECT PatientID, PatientName, Region
FROM healthcare.Patients;
GO
SELECT OBJECTPROPERTY(OBJECT_ID('healthcare.vPatientNames'), 'IsSchemaBound') AS IsSchemaBound;''',
  'SCHEMABINDING stops anyone changing or dropping the columns the view uses. It needs two-part names (schema.table) and no SELECT *. Indexed views require it.')
F('DDL-A04', 'Temporal (history) table',
  'Create a system-versioned table healthcare.RegionTargets that automatically keeps the history of target changes.',
  '''CREATE TABLE healthcare.RegionTargets (
    Region    varchar(10) NOT NULL PRIMARY KEY,
    Target    decimal(12,2) NOT NULL,
    ValidFrom datetime2 GENERATED ALWAYS AS ROW START NOT NULL,
    ValidTo   datetime2 GENERATED ALWAYS AS ROW END   NOT NULL,
    PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = healthcare.RegionTargetsHistory));

SELECT name, temporal_type_desc
FROM sys.tables
WHERE name LIKE 'RegionTargets%';''',
  'Temporal tables keep every old version of a row in a history table, which you can query with FOR SYSTEM_TIME AS OF. Useful for audit requirements.')
F('DDL-A07', 'Rebuild an index and check fragmentation',
  'Create an index on Encounters(EncounterType, EncounterDate), rebuild it, and show its fragmentation percentage.',
  '''CREATE INDEX IX_Encounters_TypeDate ON healthcare.Encounters (EncounterType, EncounterDate);
ALTER INDEX IX_Encounters_TypeDate ON healthcare.Encounters REBUILD;

SELECT i.name, CAST(ps.avg_fragmentation_in_percent AS decimal(5,1)) AS FragPct
FROM sys.dm_db_index_physical_stats(DB_ID(), OBJECT_ID('healthcare.Encounters'), NULL, NULL, 'LIMITED') AS ps
JOIN sys.indexes AS i ON i.object_id = ps.object_id AND i.index_id = ps.index_id
WHERE i.name = 'IX_Encounters_TypeDate';''',
  'REBUILD recreates the index from scratch, removing fragmentation. A common rule of thumb: reorganize at 5-30% fragmentation, rebuild above 30%.')
F('DDL-A09', 'Change a column type with data',
  'Copy Encounters into #Enc, change the copy\'s Charge from decimal(12,2) to decimal(14,4), and confirm the values are kept.',
  '''SELECT EncounterID, Charge INTO #Enc FROM healthcare.Encounters;
DECLARE @Before decimal(18,2) = (SELECT SUM(Charge) FROM #Enc);

ALTER TABLE #Enc ALTER COLUMN Charge decimal(14,4) NULL;

SELECT @Before AS TotalBefore,
       (SELECT SUM(Charge) FROM #Enc) AS TotalAfter,
       (SELECT scale FROM tempdb.sys.columns
        WHERE object_id = OBJECT_ID('tempdb..#Enc') AND name = 'Charge') AS NewScale;
DROP TABLE #Enc;''',
  'Widening a decimal keeps the values. Narrowing it can fail or round. On the real table, ALTER COLUMN also fails while a CHECK, index or view depends on the column, so those must be dropped first; practising on a copy avoids that.')

# ---------------- DML ----------------
F('DML-B02', 'Insert several rows',
  'Add two patients in one statement: IDs 201 and 202, names \'Maya Ross\' and \'Owen Hart\', numbers PT-0000201 and PT-0000202, both in the West region.',
  '''INSERT INTO healthcare.Patients (PatientID, PatientName, PatientNumber, Region)
VALUES (201, N'Maya Ross', 'PT-0000201', 'West'),
       (202, N'Owen Hart', 'PT-0000202', 'West');

SELECT PatientID, PatientName, PatientNumber, Region
FROM healthcare.Patients
WHERE PatientID IN (201, 202);''',
  'One INSERT can add several rows: separate each row\'s values with a comma.')
F('DML-B05', 'Update with a calculation',
  'Increase the charge of all Pending encounters by 10%. Show the new total of Pending charges.',
  '''UPDATE healthcare.Encounters
SET Charge = Charge * 1.10
WHERE Status = 'Pending';

SELECT SUM(Charge) AS PendingTotal FROM healthcare.Encounters WHERE Status = 'Pending';''',
  'UPDATE can set a column from an expression that uses its current value. Always include WHERE, or every row changes.')
F('DML-B06', 'Delete rows',
  'Delete patients that have never had an encounter. Show how many patients remain.',
  '''DELETE FROM healthcare.Patients
WHERE PatientID NOT IN (SELECT PatientID FROM healthcare.Encounters);

SELECT COUNT(*) AS PatientsLeft FROM healthcare.Patients;''',
  'A subquery in WHERE picks the rows to delete. Patients with encounters cannot be deleted anyway, because the foreign key protects them. If every patient has encounters, nothing is deleted.')
F('DML-B07', 'Preview before you change',
  'Before deleting Pending encounters with a charge below the average charge, preview how many rows would be affected.',
  '''SELECT COUNT(*) AS RowsToDelete
FROM healthcare.Encounters
WHERE Status = 'Pending'
  AND Charge < (SELECT AVG(Charge) FROM healthcare.Encounters);''',
  'Write the WHERE clause as a SELECT first. When the count looks right, change SELECT COUNT(*) to DELETE.')
F('DML-I02', 'Delete using a join',
  'Copy Encounters into #Enc, then delete from the copy the encounters of patients in the East region, using a join. Show how many rows remain.',
  '''SELECT EncounterID, PatientID INTO #Enc FROM healthcare.Encounters;

DELETE c
FROM #Enc AS c
JOIN healthcare.Patients AS p ON p.PatientID = c.PatientID
WHERE p.Region = 'East';

SELECT COUNT(*) AS RowsLeft FROM #Enc;
DROP TABLE #Enc;''',
  'DELETE alias FROM table JOIN other ... deletes rows from the first table based on data in the joined table. Name the alias right after DELETE.')
F('DML-I06', 'Conditional update with CASE',
  'Re-price Open encounters: below the average charge add 5%, otherwise add 2%. First show how many Open encounters fall in each band.',
  '''DECLARE @Avg decimal(12,2) = (SELECT AVG(Charge) FROM healthcare.Encounters);

SELECT CASE WHEN Charge < @Avg THEN '5%' ELSE '2%' END AS Increase,
       COUNT(*) AS Encounters
FROM healthcare.Encounters
WHERE Status = 'Open'
GROUP BY CASE WHEN Charge < @Avg THEN '5%' ELSE '2%' END
ORDER BY Increase;

UPDATE healthcare.Encounters
SET Charge = Charge * CASE WHEN Charge < @Avg THEN 1.05 ELSE 1.02 END
WHERE Status = 'Open';''',
  'A CASE expression inside SET gives each row its own change in one UPDATE. Preview the bands with the same CASE in a SELECT before running the UPDATE. The average goes into a variable so it does not change while rows are updated.')
F('DML-I08', 'Delete the oldest rows in batches',
  'Copy Encounters into #Enc, then delete the Closed rows from the copy in batches of 50, and report how many batches it took.',
  '''SELECT EncounterID, Status INTO #Enc FROM healthcare.Encounters;
DECLARE @Batches int = 0;

WHILE 1 = 1
BEGIN
    DELETE TOP (50) FROM #Enc WHERE Status = 'Closed';
    IF @@ROWCOUNT = 0 BREAK;
    SET @Batches += 1;
END;

SELECT @Batches AS Batches, (SELECT COUNT(*) FROM #Enc) AS RowsLeft;
DROP TABLE #Enc;''',
  'Deleting in small batches keeps locks and the transaction log small on big tables. @@ROWCOUNT tells you when nothing is left.')
F('DML-A01', 'MERGE: sync a staging table',
  'Sync patient regions from a staging list: update regions that changed, insert new patients, and report each action.',
  '''DECLARE @Stage TABLE (PatientID int, PatientName nvarchar(80), PatientNumber varchar(20), Region varchar(10));
INSERT INTO @Stage
SELECT PatientID, PatientName, PatientNumber, CASE WHEN Region = 'East' THEN 'West' ELSE 'East' END
FROM healthcare.Patients WHERE PatientID = 1          -- region change
UNION ALL
SELECT PatientID, PatientName, PatientNumber, Region
FROM healthcare.Patients WHERE PatientID = 2          -- no change
UNION ALL
SELECT 301, N'New Patient', 'PT-0000301', 'North';     -- new

MERGE healthcare.Patients AS t
USING @Stage AS s
   ON t.PatientID = s.PatientID
WHEN MATCHED AND t.Region <> s.Region THEN
    UPDATE SET t.Region = s.Region
WHEN NOT MATCHED BY TARGET THEN
    INSERT (PatientID, PatientName, PatientNumber, Region)
    VALUES (s.PatientID, s.PatientName, s.PatientNumber, s.Region)
OUTPUT $action AS ActionTaken, inserted.PatientID, deleted.Region AS OldRegion, inserted.Region AS NewRegion;''',
  'MERGE does insert, update and (optionally) delete in one statement. The extra `AND t.Region <> s.Region` skips rows that did not change. $action in OUTPUT reports what happened to each row.')
F('DML-A02', 'Audit trail with OUTPUT INTO',
  'Raise the charge of every Pending encounter by 1% and write the old and new charges into an audit table in the same statement. Show the first 5 audit rows.',
  '''CREATE TABLE #ChargeAudit (EncounterID int, OldCharge decimal(12,2), NewCharge decimal(12,2), ChangedAt datetime2(0));

UPDATE healthcare.Encounters
SET Charge = Charge * 1.01
OUTPUT inserted.EncounterID, deleted.Charge, inserted.Charge, SYSDATETIME()
INTO #ChargeAudit (EncounterID, OldCharge, NewCharge, ChangedAt)
WHERE Status = 'Pending';

SELECT TOP (5) EncounterID, OldCharge, NewCharge FROM #ChargeAudit ORDER BY EncounterID;
DROP TABLE #ChargeAudit;''',
  'OUTPUT ... INTO writes the change history atomically with the update, so the audit can never miss a change.')
F('DML-A04', 'Soft delete',
  'Instead of deleting patients, mark them inactive. Add IsDeleted (bit, default 0), soft-delete patient 3, and show the active patients count.',
  '''ALTER TABLE healthcare.Patients ADD IsDeleted bit NOT NULL CONSTRAINT DF_Patients_IsDeleted DEFAULT (0);
GO
UPDATE healthcare.Patients SET IsDeleted = 1 WHERE PatientID = 3;

SELECT COUNT(*) AS ActivePatients FROM healthcare.Patients WHERE IsDeleted = 0;''',
  'A soft delete keeps the row (and its history and foreign keys) but hides it from normal queries. Every query must then filter IsDeleted = 0, often through a view.')
F('DML-A06', 'Error handling in a data change',
  'Move encounter 1 to patient 5000 (which does not exist) inside TRY/CATCH, and report the error and the encounter\'s PatientID afterwards.',
  '''BEGIN TRY
    UPDATE healthcare.Encounters SET PatientID = 5000 WHERE EncounterID = 1;
    SELECT 'Updated' AS Result;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNo,
           (SELECT PatientID FROM healthcare.Encounters WHERE EncounterID = 1) AS PatientIDNow;
END CATCH;''',
  'If the statement fails inside TRY, control jumps to CATCH and the row is unchanged. ERROR_NUMBER() tells you what went wrong; here 547, the foreign key.')
F('DML-A08', 'Delete parents and children in order',
  'Delete patient 4 and everything that depends on them (their encounters) in the right order.',
  '''DECLARE @PatientID int = 4;

DELETE FROM healthcare.Encounters WHERE PatientID = @PatientID;
DELETE FROM healthcare.Patients   WHERE PatientID = @PatientID;

SELECT (SELECT COUNT(*) FROM healthcare.Patients   WHERE PatientID = @PatientID) AS PatientLeft,
       (SELECT COUNT(*) FROM healthcare.Encounters WHERE PatientID = @PatientID) AS EncountersLeft;''',
  'Delete from the bottom of the foreign key chain upward: first the child rows (encounters), then the parent (the patient). In the other order the foreign key blocks the delete.')
F('DML-A09', 'Generate test rows with a set',
  'Insert 20 test encounters for patient 1 in one statement, one per day starting 2025-01-01, with IDs 1001-1020.',
  '''WITH N AS (
    SELECT TOP (20) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects
)
INSERT INTO healthcare.Encounters
    (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge,
     ServiceUnits, EncounterDate, StartedAt, RecordedAt{{XC}})
SELECT 1000 + n, 1, CONCAT(N'HEA-TEST-', n), 'A', 'Open', 100, 1,
       DATEADD(day, n - 1, CAST('2025-01-01' AS date)),
       DATEADD(day, n - 1, CAST('2025-01-01 09:00' AS datetime2(3))),
       DATEADD(day, n - 1, CAST('2025-01-01 09:01 +00:00' AS datetimeoffset(3))){{XV}}
FROM N;

SELECT COUNT(*) AS TestRows, MIN(EncounterDate) AS FirstDate, MAX(EncounterDate) AS LastDate
FROM healthcare.Encounters
WHERE EncounterID BETWEEN 1001 AND 1020;''',
  'Generate numbers with ROW_NUMBER over any large table, then build each row from n. One set-based INSERT is much faster than a loop of 20 inserts.')
F('DML-A10', 'Lock-friendly update pattern',
  'Update only rows that really change: set Note to \'Reviewed\' for type B encounters, skipping rows that already have that note. Report how many rows changed.',
  '''UPDATE healthcare.Encounters
SET Note = N'Reviewed'
WHERE EncounterType = 'B'
  AND (Note <> N'Reviewed' OR Note IS NULL);

SELECT @@ROWCOUNT AS RowsChanged;''',
  'Skipping rows that already have the value avoids needless locks and log writes. The `OR Note IS NULL` is needed because NULL <> \'Reviewed\' is UNKNOWN, not TRUE.')

# ---------------- DQL ----------------
F('DQL-B04', 'Sort the result',
  'List all patients sorted by name from A to Z.',
  '''SELECT PatientID, PatientName
FROM healthcare.Patients
ORDER BY PatientName ASC;''',
  'ORDER BY sorts the result. ASC (A to Z, smallest first) is the default; DESC reverses it.')
F('DQL-B05', 'Highest charges',
  'Show the 5 encounters with the highest charge.',
  '''SELECT TOP (5) EncounterID, Charge
FROM healthcare.Encounters
ORDER BY Charge DESC, EncounterID;''',
  'TOP (n) with ORDER BY ... DESC returns the n largest values. Without ORDER BY, TOP returns any n rows.')
F('DQL-B07', 'Rename columns with aliases',
  'List patient names and regions, but show the column headings as Name and Area.',
  '''SELECT PatientName AS Name, Region AS Area
FROM healthcare.Patients;''',
  'AS gives a column a new heading in the result. The table itself does not change.')
F('DQL-B08', 'Calculated column',
  'For every encounter show the charge and the charge with 8% tax added. Call the new column ChargeWithTax.',
  '''SELECT EncounterID, Charge,
       Charge * 1.08 AS ChargeWithTax
FROM healthcare.Encounters;''',
  'You can calculate new columns in SELECT. They exist only in the result.')
F('DQL-I03', 'Translate codes into words',
  'EncounterType A means Standard, B means Priority, C means Special. Show each encounter ID with the readable type.',
  '''SELECT EncounterID, EncounterType,
       CASE EncounterType
            WHEN 'A' THEN 'Standard'
            WHEN 'B' THEN 'Priority'
            WHEN 'C' THEN 'Special'
            ELSE 'Unknown'
       END AS TypeName
FROM healthcare.Encounters;''',
  'A simple CASE compares one value against a list. ELSE catches anything not listed.')
F('DQL-I05', 'Missing values with IS NULL',
  'Find encounters that have no BackupNote (BackupNote is empty). Show how many there are.',
  '''SELECT COUNT(*) AS WithoutBackupNote
FROM healthcare.Encounters
WHERE BackupNote IS NULL;''',
  'Test for NULL with IS NULL. `= NULL` never matches anything, because NULL is unknown, not a value.')
F('DQL-I09', 'Sort by a calculated value',
  'List encounters by charge per service unit, highest first. Show the ID and the charge per unit (top 10).',
  '''SELECT TOP (10) EncounterID,
       CAST(Charge / ServiceUnits AS decimal(12,2)) AS ChargePerUnit
FROM healthcare.Encounters
ORDER BY ChargePerUnit DESC, EncounterID;''',
  'ORDER BY can use a column alias from SELECT, because ORDER BY runs after SELECT.')
F('DQL-A09', 'Percent of total in the same row',
  'Show each region\'s total charge and what percent it is of the total of all charges, rounded to 2 decimals. Highest first.',
  '''SELECT p.Region, SUM(e.Charge) AS RegionCharge,
       ROUND(100.0 * SUM(e.Charge) / (SELECT SUM(Charge) FROM healthcare.Encounters), 2) AS PctOfTotal
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
GROUP BY p.Region
ORDER BY RegionCharge DESC;''',
  'A subquery in SELECT gives the grand total for the percentage. Multiply by 100.0 (not 100) to avoid integer division.')

# ---------------- INTRODUCTION ----------------
F('INTRODUCTION-B06', 'What does NULL mean?',
  'What does NULL mean, and how many encounters have a NULL BackupNote?',
  '''SELECT COUNT(*) AS WithoutBackupNote
FROM healthcare.Encounters
WHERE BackupNote IS NULL;''',
  'NULL means "no value / unknown". It is not zero and not an empty string. Test it with IS NULL.')
F('INTRODUCTION-B08', 'Many-to-many relationship',
  'Patients and Encounters are one-to-many. Explain what a many-to-many relationship is, and how you would add one here (for example, encounters that involve several staff members).',
  '', '')
F('INTRODUCTION-I02', 'Why not store everything in one table?',
  'Show the problem with a denormalized design: how many times is each patient\'s name repeated if we put it on every encounter row? Show the 10 most repeated.',
  '''SELECT TOP (10) p.PatientName, COUNT(*) AS TimesRepeated
FROM healthcare.Encounters AS e
JOIN healthcare.Patients AS p ON p.PatientID = e.PatientID
GROUP BY p.PatientID, p.PatientName
ORDER BY TimesRepeated DESC, p.PatientName;''',
  'Repeating data wastes space and causes update anomalies: renaming a patient would mean changing many rows, and missing one leaves the data inconsistent. Normalization stores each fact once.')
F('INTRODUCTION-A04', 'Star schema from OLTP',
  'Sketch how the Amerimed OLTP tables would become a star schema for reporting. Then write the query that would load a FactEncounter table.',
  '''SELECT e.EncounterID,
       CONVERT(int, FORMAT(e.EncounterDate, 'yyyyMMdd')) AS DateKey,
       e.PatientID AS PatientKey,
       e.EncounterType,
       e.Status,
       e.Charge,
       e.ServiceUnits
FROM healthcare.Encounters AS e;''',
  'Fact table: FactEncounter (one row per encounter, with measures Charge and ServiceUnits). Dimensions: DimPatient (with Region), DimDate (DateKey = yyyymmdd) and a small DimType for the encounter type. Facts hold numbers and keys; dimensions hold the descriptions you filter and group by.')
