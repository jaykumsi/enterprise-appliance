# Healthcare: DDL — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DDL.md)

## Teaching and troubleshooting

Compare column names, types and nullability first, then keys and constraints. Create parent tables before children. A table with the correct columns can still be missing required constraints.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DDL-01-04 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'healthcare') IS NULL EXEC(N'CREATE SCHEMA [healthcare] AUTHORIZATION dbo;');
CREATE TABLE [healthcare].[Patients] (
    [PatientID] int NOT NULL,
    [PatientName] nvarchar(80) NOT NULL,
    [PatientNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Patients] PRIMARY KEY ([PatientID]),
    CONSTRAINT [UQ_Patients_1] UNIQUE (PatientNumber),
    CONSTRAINT [CK_Patients_1] CHECK (LEN(LTRIM(RTRIM(PatientName))) > 0)
);
```

**Check and explain:** Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-04 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Patients] ADD ContactPhone varchar(30) NULL;
EXEC sys.sp_help N'healthcare.Patients';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-04 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Encounters] DROP CONSTRAINT [FK_Encounters_PatientID];
DROP TABLE [healthcare].[Patients];
SELECT OBJECT_ID(N'healthcare.Patients') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-09 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [healthcare].[Doctors] (
    [DoctorID] int NOT NULL,
    [DoctorName] nvarchar(80) NOT NULL,
    [LicenseNumber] varchar(20) NOT NULL,
    [Specialty] varchar(30) NOT NULL,
    CONSTRAINT [PK_Doctors] PRIMARY KEY ([DoctorID]),
    CONSTRAINT [UQ_Doctors_1] UNIQUE (LicenseNumber),
    CONSTRAINT [CK_Doctors_1] CHECK (LEN(LTRIM(RTRIM(DoctorName))) > 0)
);
```

**Check and explain:** Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-09 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Doctors] DROP CONSTRAINT [CK_Doctors_1];
ALTER TABLE [healthcare].[Doctors] ALTER COLUMN DoctorName nvarchar(120) NOT NULL;
ALTER TABLE [healthcare].[Doctors] WITH CHECK ADD CONSTRAINT [CK_Doctors_1] CHECK (LEN(LTRIM(RTRIM(DoctorName))) > 0);
EXEC sys.sp_help N'healthcare.Doctors';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-09 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Encounters] DROP CONSTRAINT [FK_Encounters_DoctorID];
DROP TABLE [healthcare].[Doctors];
SELECT OBJECT_ID(N'healthcare.Doctors') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-14 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [healthcare].[Medications] (
    [MedicationID] int NOT NULL,
    [MedicationName] nvarchar(80) NOT NULL,
    [MedicationCode] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Medications] PRIMARY KEY ([MedicationID]),
    CONSTRAINT [UQ_Medications_1] UNIQUE (MedicationCode),
    CONSTRAINT [CK_Medications_1] CHECK (UnitCost >= 0),
    CONSTRAINT [CK_Medications_2] CHECK (LEN(LTRIM(RTRIM(MedicationName))) > 0)
);
```

**Check and explain:** Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-14 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Medications] ADD AuditNote nvarchar(200) NULL;
EXEC sys.sp_help N'healthcare.Medications';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-14 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Prescriptions] DROP CONSTRAINT [FK_Prescriptions_MedicationID];
DROP TABLE [healthcare].[Medications];
SELECT OBJECT_ID(N'healthcare.Medications') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-19 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [healthcare].[Encounters] (
    [EncounterID] int NOT NULL,
    [PatientID] int NOT NULL,
    [EncounterReference] nvarchar(80) NOT NULL,
    [EncounterType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [Charge] decimal(12,2) NULL,
    [ServiceUnits] int NOT NULL,
    [EncounterDate] date NOT NULL,
    [StartedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentEncounterID] int NULL,
    [DoctorID] int NOT NULL,
    CONSTRAINT [PK_Encounters] PRIMARY KEY ([EncounterID]),
    CONSTRAINT [UQ_Encounters_1] UNIQUE (EncounterReference),
    CONSTRAINT [CK_Encounters_1] CHECK (EncounterType IN ('A','B','C')),
    CONSTRAINT [CK_Encounters_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Encounters_3] CHECK (Charge >= 0),
    CONSTRAINT [CK_Encounters_4] CHECK (ServiceUnits > 0),
    CONSTRAINT [CK_Encounters_5] CHECK (ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID),
    CONSTRAINT [CK_Encounters_6] CHECK (LEN(LTRIM(RTRIM(EncounterReference))) > 0),
    CONSTRAINT [FK_Encounters_PatientID] FOREIGN KEY ([PatientID]) REFERENCES [healthcare].[Patients] ([PatientID]),
    CONSTRAINT [FK_Encounters_ParentEncounterID] FOREIGN KEY ([ParentEncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Encounters_DoctorID] FOREIGN KEY ([DoctorID]) REFERENCES [healthcare].[Doctors] ([DoctorID])
);
```

**Check and explain:** Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-19 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Encounters] ADD Reviewed bit NOT NULL DEFAULT(0) WITH VALUES;
EXEC sys.sp_help N'healthcare.Encounters';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-19 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Prescriptions] DROP CONSTRAINT [FK_Prescriptions_EncounterID];
DROP TABLE [healthcare].[Encounters];
SELECT OBJECT_ID(N'healthcare.Encounters') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-24 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [healthcare].[Prescriptions] (
    [PrescriptionID] int NOT NULL,
    [EncounterID] int NOT NULL,
    [MedicationID] int NOT NULL,
    [PrescriptionReference] varchar(20) NOT NULL,
    [Quantity] int NOT NULL,
    CONSTRAINT [PK_Prescriptions] PRIMARY KEY ([PrescriptionID]),
    CONSTRAINT [UQ_Prescriptions_1] UNIQUE (PrescriptionReference),
    CONSTRAINT [CK_Prescriptions_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_Prescriptions_2] CHECK (LEN(LTRIM(RTRIM(PrescriptionReference))) > 0),
    CONSTRAINT [FK_Prescriptions_EncounterID] FOREIGN KEY ([EncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Prescriptions_MedicationID] FOREIGN KEY ([MedicationID]) REFERENCES [healthcare].[Medications] ([MedicationID])
);
```

**Check and explain:** Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-24 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [healthcare].[Prescriptions] ADD ExternalReference varchar(30) NULL;
ALTER TABLE [healthcare].[Prescriptions] ALTER COLUMN ExternalReference varchar(60) NULL;
ALTER TABLE [healthcare].[Prescriptions] DROP COLUMN ExternalReference;
EXEC sys.sp_help N'healthcare.Prescriptions';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-24 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY

DROP TABLE [healthcare].[Prescriptions];
SELECT OBJECT_ID(N'healthcare.Prescriptions') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Create: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-01-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B02

**Missing input**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B09

**Dependency order**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B14

**Empty state**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I04

**Drift before change**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I05

**Application bypass**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I08

**Reference membership**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-DDL-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Patients exists with PK PatientID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Doctors exists with PK DoctorID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Medications exists with PK MedicationID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Encounters exists with PK EncounterID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-01-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#healthcare-ddl-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Prescriptions exists with PK PrescriptionID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Alter: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-02-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B02

**Missing input**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B09

**Dependency order**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B14

**Empty state**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I04

**Drift before change**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I05

**Application bypass**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I08

**Reference membership**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-DDL-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-02-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#healthcare-ddl-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Drop: progression

**Beginner:15 questions**

#### HEALTHCARE-DDL-03-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B02

**Missing input**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B09

**Dependency order**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B14

**Empty state**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-DDL-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I04

**Drift before change**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I05

**Application bypass**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I08

**Reference membership**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-DDL-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-DDL-03-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#healthcare-ddl-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied answer key

Historical references require instructor review on the large fixture. These are not newly validated levelled references. [Selection audit](EXERCISE_SELECTION.md).

##### DDL-I04: Create an index

[Question](../questions/DDL.md)

```sql
CREATE NONCLUSTERED INDEX IX_Encounters_Patient_Date
ON healthcare.Encounters (PatientID, EncounterDate);

SELECT name, type_desc
FROM sys.indexes
WHERE object_id = OBJECT_ID('healthcare.Encounters') AND name = 'IX_Encounters_Patient_Date';
```

**How it works:** An index lets SQL Server find rows without reading the whole table. Put the column you filter on with = first, then the one you sort or range on.

**Expected result:** 1 row

| name | type_desc |
|---|---|
| IX\_Encounters\_Patient\_Date | NONCLUSTERED |

##### DDL-I05: Covering index with INCLUDE

[Question](../questions/DDL.md)

```sql
CREATE NONCLUSTERED INDEX IX_Encounters_Status
ON healthcare.Encounters (Status)
INCLUDE (Charge);

SELECT Status, SUM(Charge) AS TotalCharge
FROM healthcare.Encounters
GROUP BY Status;
```

**How it works:** INCLUDE stores extra columns in the index leaf level without making them part of the key. A query that needs only key + included columns is "covered".

**Expected result:** 3 rows

| Status | TotalCharge |
|---|---|
| Closed | 31537 |
| Open | 3326 |
| Pending | 1800 |

##### DDL-I10: Schema-bound view

[Question](../questions/DDL.md)

```sql
CREATE VIEW healthcare.vMedPrices WITH SCHEMABINDING AS
SELECT MedicationID, MedicationName, UnitCost FROM healthcare.Medications;
GO
SELECT OBJECTPROPERTY(OBJECT_ID('healthcare.vMedPrices'), 'IsSchemaBound') AS IsSchemaBound;
```

**How it works:** SCHEMABINDING ties the view to its tables. After this, `ALTER TABLE healthcare.Medications DROP COLUMN UnitCost` fails with error 5074 because the view depends on it. Schema binding is also required for indexed views. A schema-bound view must use two-part names (schema.table) and cannot use SELECT *.

**Expected result:** 1 row

| IsSchemaBound |
|---|
| 1 |

##### DDL-A02: Filtered index

[Question](../questions/DDL.md)

```sql
CREATE NONCLUSTERED INDEX IX_Encounters_Open
ON healthcare.Encounters (EncounterDate)
WHERE Status = 'Open';

SELECT name, filter_definition
FROM sys.indexes
WHERE name = 'IX_Encounters_Open';
```

**How it works:** A filtered index is smaller and cheaper to maintain when queries target a small subset (here 24 of 240 rows).

**Expected result:** 1 row

| name | filter_definition |
|---|---|
| IX\_Encounters\_Open | ([Status]='Open') |

##### DDL-A04: Temporal (history) table

[Question](../questions/DDL.md)

```sql
CREATE TABLE healthcare.PriceList (
    MedicationID int NOT NULL PRIMARY KEY,
    Price        decimal(12,2) NOT NULL,
    ValidFrom datetime2 GENERATED ALWAYS AS ROW START NOT NULL,
    ValidTo   datetime2 GENERATED ALWAYS AS ROW END   NOT NULL,
    PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)
)
WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = healthcare.PriceListHistory));

SELECT name, temporal_type_desc
FROM sys.tables
WHERE schema_id = SCHEMA_ID('healthcare') AND name IN ('PriceList','PriceListHistory')
ORDER BY name;
```

**How it works:** Temporal tables keep every old version of a row in a history table, which you can query with FOR SYSTEM_TIME AS OF. Useful for audit requirements in healthcare.

**Expected result:** 2 rows

| name | temporal_type_desc |
|---|---|
| PriceList | SYSTEM\_VERSIONED\_TEMPORAL\_TABLE |
| PriceListHistory | HISTORY\_TABLE |

##### DDL-A09: Change a column type with data

[Question](../questions/DDL.md)

```sql
ALTER TABLE healthcare.Medications DROP CONSTRAINT CK_Medications_1;
ALTER TABLE healthcare.Medications ALTER COLUMN UnitCost decimal(12,4) NOT NULL;
ALTER TABLE healthcare.Medications ADD CONSTRAINT CK_Medications_1 CHECK (UnitCost >= 0);

SELECT TOP (3) MedicationID, UnitCost FROM healthcare.Medications ORDER BY MedicationID;
```

**How it works:** A column used by a constraint cannot be altered until the constraint is dropped. Drop it, change the type, recreate it. In production, do this in one transaction.

**Expected result:** 3 rows

| MedicationID | UnitCost |
|---|---|
| 1 | 0.0800 |
| 2 | 0.1000 |
| 3 | 0.1000 |

##### DDL-A10: SEQUENCE vs IDENTITY

[Question](../questions/DDL.md)

```sql
CREATE SEQUENCE healthcare.seqInvoice AS int START WITH 5000 INCREMENT BY 10;
GO
SELECT n, NEXT VALUE FOR healthcare.seqInvoice OVER (ORDER BY n) AS InvoiceNo
FROM (VALUES (1), (2), (3)) AS v(n)
ORDER BY n;
```

**How it works:** A SEQUENCE is a separate object that hands out numbers, so several tables can share it and you can get a number before inserting. IDENTITY belongs to one column of one table. NEXT VALUE FOR gives each row a new number: 5000, 5010, 5020.

**Expected result:** 3 rows

| n | InvoiceNo |
|---|---|
| 1 | 5000 |
| 2 | 5010 |
| 3 | 5020 |
