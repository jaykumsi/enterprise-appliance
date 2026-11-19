# Healthcare — DDL

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

After the Create exercises, use [Large practice data](PRACTICE_DATA.md) for a dataset with at least 50 rows per master and 100 per detail table.

## Create

### DDL-01-04

Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

### DDL-01-09

Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

### DDL-01-14

Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

### DDL-01-19

Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

### DDL-01-24

Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

## Alter

### DDL-02-04

**Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

### DDL-02-09

**Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

### DDL-02-14

**Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

### DDL-02-19

**Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

### DDL-02-24

**Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

## Drop

### DDL-03-04

**Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

### DDL-03-09

**Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

### DDL-03-14

**Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

### DDL-03-19

**Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

### DDL-03-24

**Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Create: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-01-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-01-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-DDL-01-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Patients]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PatientID | int | NOT NULL; PRIMARY KEY |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL; UNIQUE |
| Region | varchar(10) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(PatientName))) > 0`).

Before creating this table, create the `healthcare` schema if it does not exist. A schema groups related tables.

Table 1 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Doctors]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| DoctorID | int | NOT NULL; PRIMARY KEY |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL; UNIQUE |
| Specialty | varchar(30) | NOT NULL |

Add these constraints:

1. Add CHECK (`LEN(LTRIM(RTRIM(DoctorName))) > 0`).

Table 2 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Medications]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| MedicationID | int | NOT NULL; PRIMARY KEY |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL; UNIQUE |
| UnitCost | decimal(12,2) | NOT NULL |

Add these constraints:

1. Add CHECK (`UnitCost >= 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(MedicationName))) > 0`).

Table 3 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Encounters]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| EncounterID | int | NOT NULL; PRIMARY KEY |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL; UNIQUE |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Add these constraints:

1. Add CHECK (`EncounterType IN ('A','B','C')`).
2. Add CHECK (`Status IN ('Open','Closed','Pending')`).
3. Add CHECK (`Charge >= 0`).
4. Add CHECK (`ServiceUnits > 0`).
5. Add CHECK (`ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`).
6. Add CHECK (`LEN(LTRIM(RTRIM(EncounterReference))) > 0`).
7. Add a FOREIGN KEY from `PatientID` to `[healthcare].[Patients](PatientID)`.
8. Add a FOREIGN KEY from `ParentEncounterID` to `[healthcare].[Encounters](EncounterID)`.
9. Add a FOREIGN KEY from `DoctorID` to `[healthcare].[Doctors](DoctorID)`.

For foreign keys, use NO ACTION on delete and update.

Table 4 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-01-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Create the `[healthcare].[Prescriptions]` table with these columns:

| Column | Data type | Constraints |
|---|---|---|
| PrescriptionID | int | NOT NULL; PRIMARY KEY |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL; UNIQUE |
| Quantity | int | NOT NULL |

Add these constraints:

1. Add CHECK (`Quantity > 0`).
2. Add CHECK (`LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`).
3. Add a FOREIGN KEY from `EncounterID` to `[healthcare].[Encounters](EncounterID)`.
4. Add a FOREIGN KEY from `MedicationID` to `[healthcare].[Medications](MedicationID)`.

For foreign keys, use NO ACTION on delete and update.

Table 5 of 5. Create the tables in the order listed. Keep them for the next exercises.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Alter: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-02-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-02-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-DDL-02-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Patients table**

Use `[healthcare].[Patients]` and the sample rows you added earlier.

1. Make this change: add nullable ContactPhone varchar(30).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Doctors table**

Use `[healthcare].[Doctors]` and the sample rows you added earlier.

1. Make this change: widen DoctorName to nvarchar(120), keeping NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Medications table**

Use `[healthcare].[Medications]` and the sample rows you added earlier.

1. Make this change: add nullable AuditNote nvarchar(200).
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Encounters table**

Use `[healthcare].[Encounters]` and the sample rows you added earlier.

1. Make this change: add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-02-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Change the Prescriptions table**

Use `[healthcare].[Prescriptions]` and the sample rows you added earlier.

1. Make this change: add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column.
2. Check the column settings and rows. You can use `sp_help` to see the table settings.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Drop: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-03-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-03-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-DDL-03-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Patients table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Patients]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Patients]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Doctors table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Doctors]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Doctors]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Medications table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Medications]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Medications]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Encounters table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Encounters]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Encounters]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-DDL-03-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice removing the Prescriptions table**

Use a separate practice copy of the tables and sample rows for this exercise.

1. Find the foreign keys in other tables that point to `[healthcare].[Prescriptions]`. Remove those links, but keep the other tables.
2. Use DROP TABLE to remove only `[healthcare].[Prescriptions]`. Check that it no longer exists.

**Explain:** How is removing a table different from deleting rows inside it?

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied practice

Selected cases supplement the assessed levelled bank. B/I/A in these older IDs are historical labels, not current difficulty ratings. [Practice route](BEST_EXERCISES.md). Historical self-checks use the large fixture and are outside the native report-validation claim. Use a fresh large-fixture practice copy for each case that changes data or permissions; changes persist.

<a id="legacy-ddl-i04"></a>

##### DDL-I04: Create an index

Create a nonclustered index on Encounters(PatientID, EncounterDate) to speed up "visits of a patient" queries.

**Expected result:** 1 row

| name | type_desc |
|---|---|
| IX\_Encounters\_Patient\_Date | NONCLUSTERED |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-i05"></a>

##### DDL-I05: Covering index with INCLUDE

Create an index on Encounters(Status) that also includes Charge, so 'total charge by status' can be answered from the index alone.

**Expected result:** 3 rows

| Status | TotalCharge |
|---|---|
| Closed | 31537 |
| Open | 3326 |
| Pending | 1800 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-i10"></a>

##### DDL-I10: Schema-bound view

Create a view WITH SCHEMABINDING over Medications and confirm it is schema-bound.

**Expected result:** 1 row

| IsSchemaBound |
|---|
| 1 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-a02"></a>

##### DDL-A02: Filtered index

Create an index that only covers Open encounters, sorted by EncounterDate.

**Expected result:** 1 row

| name | filter_definition |
|---|---|
| IX\_Encounters\_Open | ([Status]='Open') |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-a04"></a>

##### DDL-A04: Temporal (history) table

Create system-versioned healthcare.PriceList with MedicationID int NOT NULL PRIMARY KEY, Price decimal(12,2) NOT NULL, ValidFrom datetime2(7) GENERATED ALWAYS AS ROW START NOT NULL and ValidTo datetime2(7) GENERATED ALWAYS AS ROW END NOT NULL. Define PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo), enable SYSTEM_VERSIONING, and name the history table healthcare.PriceListHistory. No foreign key or additional default is required. Return name and temporal_type_desc for the two tables from sys.tables, in name order.

**Expected result:** 2 rows

| name | temporal_type_desc |
|---|---|
| PriceList | SYSTEM\_VERSIONED\_TEMPORAL\_TABLE |
| PriceListHistory | HISTORY\_TABLE |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-a09"></a>

##### DDL-A09: Change a column type with data

Change Medications.UnitCost from decimal(12,2) to decimal(12,4) and confirm the values are kept.

**Expected result:** 3 rows

| MedicationID | UnitCost |
|---|---|
| 1 | 0.0800 |
| 2 | 0.1000 |
| 3 | 0.1000 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-ddl-a10"></a>

##### DDL-A10: SEQUENCE vs IDENTITY

Create healthcare.seqInvoice AS int starting at 5000 and incrementing by 10. For input n = 1, 2, 3, allocate sequence values in n order and return n, InvoiceNo ordered by n. Use a fresh sequence; explain why gaps are allowed and why this differs from a table IDENTITY.

**Expected result:** 3 rows

| n | InvoiceNo |
|---|---|
| 1 | 5000 |
| 2 | 5010 |
| 3 | 5020 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._
