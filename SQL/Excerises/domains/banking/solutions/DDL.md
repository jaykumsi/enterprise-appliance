# Banking / Finance: DDL — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DDL.md)

## Teaching and troubleshooting

Compare column names, types and nullability first, then keys and constraints. Create parent tables before children. A table with the correct columns can still be missing required constraints.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DDL-01-02 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'banking') IS NULL EXEC(N'CREATE SCHEMA [banking] AUTHORIZATION dbo;');
CREATE TABLE [banking].[Branches] (
    [BranchID] int NOT NULL,
    [BranchName] nvarchar(80) NOT NULL,
    [BranchCode] varchar(20) NOT NULL,
    [City] nvarchar(50) NOT NULL,
    CONSTRAINT [PK_Branches] PRIMARY KEY ([BranchID]),
    CONSTRAINT [UQ_Branches_1] UNIQUE (BranchCode),
    CONSTRAINT [CK_Branches_1] CHECK (LEN(LTRIM(RTRIM(BranchName))) > 0)
);
```

**Check and explain:** Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-02 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Branches] ADD ContactPhone varchar(30) NULL;
EXEC sys.sp_help N'banking.Branches';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-02 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Accounts] DROP CONSTRAINT [FK_Accounts_BranchID];
DROP TABLE [banking].[Branches];
SELECT OBJECT_ID(N'banking.Branches') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-07 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [banking].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [Email] varchar(100) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (Email),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
```

**Check and explain:** Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-07 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Customers] DROP CONSTRAINT [CK_Customers_1];
ALTER TABLE [banking].[Customers] ALTER COLUMN CustomerName nvarchar(120) NOT NULL;
ALTER TABLE [banking].[Customers] WITH CHECK ADD CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0);
EXEC sys.sp_help N'banking.Customers';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-07 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Accounts] DROP CONSTRAINT [FK_Accounts_CustomerID];
ALTER TABLE [banking].[Loans] DROP CONSTRAINT [FK_Loans_CustomerID];
DROP TABLE [banking].[Customers];
SELECT OBJECT_ID(N'banking.Customers') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-12 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [banking].[Accounts] (
    [AccountID] int NOT NULL,
    [AccountName] nvarchar(80) NOT NULL,
    [AccountNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    [CustomerID] int NOT NULL,
    [BranchID] int NOT NULL,
    CONSTRAINT [PK_Accounts] PRIMARY KEY ([AccountID]),
    CONSTRAINT [UQ_Accounts_1] UNIQUE (AccountNumber),
    CONSTRAINT [CK_Accounts_1] CHECK (LEN(LTRIM(RTRIM(AccountName))) > 0),
    CONSTRAINT [FK_Accounts_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [banking].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Accounts_BranchID] FOREIGN KEY ([BranchID]) REFERENCES [banking].[Branches] ([BranchID])
);
```

**Check and explain:** Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-12 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Accounts] ADD AuditNote nvarchar(200) NULL;
EXEC sys.sp_help N'banking.Accounts';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-12 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Transactions] DROP CONSTRAINT [FK_Transactions_AccountID];
ALTER TABLE [banking].[Loans] DROP CONSTRAINT [FK_Loans_AccountID];
DROP TABLE [banking].[Accounts];
SELECT OBJECT_ID(N'banking.Accounts') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-17 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [banking].[Transactions] (
    [TransactionID] int NOT NULL,
    [AccountID] int NOT NULL,
    [Reference] nvarchar(80) NOT NULL,
    [TransactionType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [Amount] decimal(12,2) NULL,
    [UnitCount] int NOT NULL,
    [TransactionDate] date NOT NULL,
    [PostedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentTransactionID] int NULL,
    CONSTRAINT [PK_Transactions] PRIMARY KEY ([TransactionID]),
    CONSTRAINT [UQ_Transactions_1] UNIQUE (Reference),
    CONSTRAINT [CK_Transactions_1] CHECK (TransactionType IN ('A','B','C')),
    CONSTRAINT [CK_Transactions_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Transactions_3] CHECK (Amount >= 0),
    CONSTRAINT [CK_Transactions_4] CHECK (UnitCount > 0),
    CONSTRAINT [CK_Transactions_5] CHECK (ParentTransactionID IS NULL OR ParentTransactionID <> TransactionID),
    CONSTRAINT [CK_Transactions_6] CHECK (LEN(LTRIM(RTRIM(Reference))) > 0),
    CONSTRAINT [FK_Transactions_AccountID] FOREIGN KEY ([AccountID]) REFERENCES [banking].[Accounts] ([AccountID]),
    CONSTRAINT [FK_Transactions_ParentTransactionID] FOREIGN KEY ([ParentTransactionID]) REFERENCES [banking].[Transactions] ([TransactionID])
);
```

**Check and explain:** Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-17 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Transactions] ADD Reviewed bit NOT NULL DEFAULT(0) WITH VALUES;
EXEC sys.sp_help N'banking.Transactions';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-17 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY

DROP TABLE [banking].[Transactions];
SELECT OBJECT_ID(N'banking.Transactions') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-22 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [banking].[Loans] (
    [LoanID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [AccountID] int NOT NULL,
    [LoanReference] varchar(20) NOT NULL,
    [Principal] decimal(12,2) NOT NULL,
    [AnnualRate] decimal(5,2) NOT NULL,
    CONSTRAINT [PK_Loans] PRIMARY KEY ([LoanID]),
    CONSTRAINT [UQ_Loans_1] UNIQUE (LoanReference),
    CONSTRAINT [CK_Loans_1] CHECK (Principal > 0),
    CONSTRAINT [CK_Loans_2] CHECK (AnnualRate BETWEEN 0 AND 100),
    CONSTRAINT [CK_Loans_3] CHECK (LEN(LTRIM(RTRIM(LoanReference))) > 0),
    CONSTRAINT [FK_Loans_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [banking].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Loans_AccountID] FOREIGN KEY ([AccountID]) REFERENCES [banking].[Accounts] ([AccountID])
);
```

**Check and explain:** Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-22 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [banking].[Loans] ADD ExternalReference varchar(30) NULL;
ALTER TABLE [banking].[Loans] ALTER COLUMN ExternalReference varchar(60) NULL;
ALTER TABLE [banking].[Loans] DROP COLUMN ExternalReference;
EXEC sys.sp_help N'banking.Loans';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-22 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY

DROP TABLE [banking].[Loans];
SELECT OBJECT_ID(N'banking.Loans') AS RemovedObjectID;
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

#### BANKING-DDL-01-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#banking-ddl-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B02

**Missing input**

[Canonical question](../questions/DDL.md#banking-ddl-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#banking-ddl-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#banking-ddl-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#banking-ddl-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#banking-ddl-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#banking-ddl-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#banking-ddl-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B09

**Dependency order**

[Canonical question](../questions/DDL.md#banking-ddl-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#banking-ddl-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#banking-ddl-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#banking-ddl-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#banking-ddl-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B14

**Empty state**

[Canonical question](../questions/DDL.md#banking-ddl-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#banking-ddl-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### BANKING-DDL-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#banking-ddl-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#banking-ddl-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#banking-ddl-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I04

**Drift before change**

[Canonical question](../questions/DDL.md#banking-ddl-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I05

**Application bypass**

[Canonical question](../questions/DDL.md#banking-ddl-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#banking-ddl-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#banking-ddl-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I08

**Reference membership**

[Canonical question](../questions/DDL.md#banking-ddl-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#banking-ddl-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#banking-ddl-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#banking-ddl-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#banking-ddl-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#banking-ddl-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#banking-ddl-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#banking-ddl-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### BANKING-DDL-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#banking-ddl-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#banking-ddl-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#banking-ddl-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#banking-ddl-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#banking-ddl-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#banking-ddl-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#banking-ddl-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#banking-ddl-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#banking-ddl-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#banking-ddl-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#banking-ddl-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Branches exists with PK BranchID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#banking-ddl-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#banking-ddl-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Accounts exists with PK AccountID, 2 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#banking-ddl-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Transactions exists with PK TransactionID, 2 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-01-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#banking-ddl-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Loans exists with PK LoanID, 2 FK(s), 1 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Alter: progression

**Beginner:15 questions**

#### BANKING-DDL-02-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#banking-ddl-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B02

**Missing input**

[Canonical question](../questions/DDL.md#banking-ddl-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#banking-ddl-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#banking-ddl-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#banking-ddl-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#banking-ddl-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#banking-ddl-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#banking-ddl-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B09

**Dependency order**

[Canonical question](../questions/DDL.md#banking-ddl-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#banking-ddl-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#banking-ddl-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#banking-ddl-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#banking-ddl-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B14

**Empty state**

[Canonical question](../questions/DDL.md#banking-ddl-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#banking-ddl-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### BANKING-DDL-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#banking-ddl-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#banking-ddl-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#banking-ddl-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I04

**Drift before change**

[Canonical question](../questions/DDL.md#banking-ddl-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I05

**Application bypass**

[Canonical question](../questions/DDL.md#banking-ddl-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#banking-ddl-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#banking-ddl-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I08

**Reference membership**

[Canonical question](../questions/DDL.md#banking-ddl-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#banking-ddl-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#banking-ddl-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#banking-ddl-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#banking-ddl-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#banking-ddl-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#banking-ddl-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#banking-ddl-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### BANKING-DDL-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#banking-ddl-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#banking-ddl-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#banking-ddl-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#banking-ddl-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#banking-ddl-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#banking-ddl-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#banking-ddl-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#banking-ddl-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#banking-ddl-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#banking-ddl-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#banking-ddl-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#banking-ddl-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#banking-ddl-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#banking-ddl-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-02-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#banking-ddl-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Drop: progression

**Beginner:15 questions**

#### BANKING-DDL-03-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#banking-ddl-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B02

**Missing input**

[Canonical question](../questions/DDL.md#banking-ddl-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#banking-ddl-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#banking-ddl-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#banking-ddl-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#banking-ddl-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#banking-ddl-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#banking-ddl-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B09

**Dependency order**

[Canonical question](../questions/DDL.md#banking-ddl-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#banking-ddl-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#banking-ddl-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#banking-ddl-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#banking-ddl-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B14

**Empty state**

[Canonical question](../questions/DDL.md#banking-ddl-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#banking-ddl-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### BANKING-DDL-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#banking-ddl-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#banking-ddl-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#banking-ddl-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I04

**Drift before change**

[Canonical question](../questions/DDL.md#banking-ddl-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I05

**Application bypass**

[Canonical question](../questions/DDL.md#banking-ddl-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#banking-ddl-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#banking-ddl-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I08

**Reference membership**

[Canonical question](../questions/DDL.md#banking-ddl-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#banking-ddl-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#banking-ddl-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#banking-ddl-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#banking-ddl-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#banking-ddl-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#banking-ddl-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#banking-ddl-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### BANKING-DDL-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#banking-ddl-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#banking-ddl-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#banking-ddl-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#banking-ddl-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#banking-ddl-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#banking-ddl-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#banking-ddl-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#banking-ddl-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#banking-ddl-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#banking-ddl-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#banking-ddl-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-02` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#banking-ddl-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-07` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#banking-ddl-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-12` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#banking-ddl-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-17` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BANKING-DDL-03-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#banking-ddl-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-22` in this topic's earlier foundation answers. Also require the case-specific evidence above.

