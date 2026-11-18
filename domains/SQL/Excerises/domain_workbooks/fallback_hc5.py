"""Replacement items, part 5: questions whose original depends on healthcare-only data values (see fallback_hc.py)."""
from fallback_hc import F

F('CONSTRAINTS-I03', 'ON DELETE CASCADE',
  'Create healthcare.PatientContacts with a foreign key to Patients that deletes contacts automatically when the patient is deleted. Test it with a new patient 999 who has no encounters.',
  '''INSERT INTO healthcare.Patients (PatientID, PatientName, PatientNumber, Region)
VALUES (999, N'Test Patient', 'PT-0000999', 'North');

CREATE TABLE healthcare.PatientContacts (
    ContactID int NOT NULL PRIMARY KEY,
    PatientID int NOT NULL,
    Phone     varchar(20) NOT NULL,
    CONSTRAINT FK_Contacts_Patients FOREIGN KEY (PatientID)
        REFERENCES healthcare.Patients (PatientID) ON DELETE CASCADE
);
INSERT INTO healthcare.PatientContacts VALUES (1, 999, '555-0100'), (2, 999, '555-0101');

DELETE FROM healthcare.Patients WHERE PatientID = 999;

SELECT COUNT(*) AS ContactsLeft FROM healthcare.PatientContacts;''',
  'ON DELETE CASCADE deletes child rows with the parent. Use it carefully: one delete can remove a lot of data.')

F('DML-A08', 'Delete parents and children in order',
  'Add a test patient 999 with two encounters (IDs 9101 and 9102). Then delete the patient and everything that depends on them in the right order, and confirm nothing is left.',
  '''INSERT INTO healthcare.Patients (PatientID, PatientName, PatientNumber, Region)
VALUES (999, N'Test Patient', 'PT-0000999', 'North');
INSERT INTO healthcare.Encounters
    (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge,
     ServiceUnits, EncounterDate, StartedAt, RecordedAt{{XC}})
VALUES (9101, 999, N'HEA-TEST-9101', 'A', 'Open', 100, 1, '2025-01-02', '2025-01-02 09:00', '2025-01-02 09:01 +00:00'{{XV}}),
       (9102, 999, N'HEA-TEST-9102', 'A', 'Open', 100, 1, '2025-01-03', '2025-01-03 09:00', '2025-01-03 09:01 +00:00'{{XV}});

DECLARE @PatientID int = 999;
DELETE FROM healthcare.Encounters WHERE PatientID = @PatientID;   -- children first
DELETE FROM healthcare.Patients   WHERE PatientID = @PatientID;   -- then the parent

SELECT (SELECT COUNT(*) FROM healthcare.Patients   WHERE PatientID = @PatientID) AS PatientLeft,
       (SELECT COUNT(*) FROM healthcare.Encounters WHERE PatientID = @PatientID) AS EncountersLeft;''',
  'Delete from the bottom of the foreign key chain upward: first the child rows (encounters), then the parent (the patient). In the other order the foreign key blocks the delete. Real rows are often referenced by more tables, so list every child table before deleting.')

F('DML-B06', 'Delete rows',
  'Copy Patients into #Pt, then delete from the copy the patients that have never had an encounter. Show how many remain.',
  '''SELECT * INTO #Pt FROM healthcare.Patients;

DELETE FROM #Pt
WHERE PatientID NOT IN (SELECT PatientID FROM healthcare.Encounters);

SELECT COUNT(*) AS PatientsLeft FROM #Pt;
DROP TABLE #Pt;''',
  'A subquery in WHERE picks the rows to delete. On the real table, other tables that reference a patient would block the delete, which is why this practises on a copy.')

F('CTE-B03', 'CTE with GROUP BY',
  'Use a CTE to count encounters per patient, then show the patients with 3 or more encounters.',
  '''WITH Counts AS (
    SELECT PatientID, COUNT(*) AS EncounterCount
    FROM healthcare.Encounters
    GROUP BY PatientID
)
SELECT PatientID, EncounterCount
FROM Counts
WHERE EncounterCount >= 3
ORDER BY EncounterCount DESC, PatientID;''',
  'Put the aggregation in the CTE and the filter outside. This reads more naturally than HAVING for many people.')

F('SUBQUERIES-B08', 'Derived table',
  'Use a subquery in FROM that counts encounters per patient, then show patients with 3 or more encounters.',
  '''SELECT PatientID, EncounterCount
FROM (SELECT PatientID, COUNT(*) AS EncounterCount
      FROM healthcare.Encounters
      GROUP BY PatientID) AS v
WHERE EncounterCount >= 3
ORDER BY EncounterCount DESC, PatientID;''',
  'A subquery in FROM (a derived table) must have an alias. Its columns can then be filtered like a normal table.')

F('DATATYPES-A03', 'Find values that would not fit',
  'Before changing Encounters.Note from nvarchar(100) to nvarchar(20), find the rows that would not fit.',
  '''SELECT EncounterID, LEN(Note) AS NoteLength
FROM healthcare.Encounters
WHERE LEN(Note) > 20
ORDER BY NoteLength DESC, EncounterID;''',
  'Check the data before shrinking a column. If any value is too long, ALTER COLUMN fails (or, with some settings, the text is cut). An empty result means it is safe.')

F('JOINS-A09', 'Patients active in the same month',
  'Find pairs of different patients who had an encounter in the same month of 2024. Show the month and both patient IDs, each pair once.',
  '''SELECT DISTINCT MONTH(a.EncounterDate) AS MonthNo, a.PatientID AS Patient1, b.PatientID AS Patient2
FROM healthcare.Encounters AS a
JOIN healthcare.Encounters AS b
  ON MONTH(b.EncounterDate) = MONTH(a.EncounterDate)
 AND YEAR(b.EncounterDate) = YEAR(a.EncounterDate)
 AND b.PatientID > a.PatientID
ORDER BY MonthNo, Patient1, Patient2;''',
  'The condition b.PatientID > a.PatientID removes self-pairs and keeps each pair once (A,B but not B,A).')
