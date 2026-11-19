# E-commerce: DATABASE SCHEMA USER — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DATABASE_SCHEMA_USER.md)

## Teaching and troubleshooting

Separate database, schema and user responsibilities. Check the active database and permissions before diagnosing a syntax error. Run administrative batches independently.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DATABASE_SCHEMA_USER-01-28 — Database

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
USE master;
GO
CREATE DATABASE [EcommerceAssignmentLab];
GO
SELECT name FROM sys.databases WHERE name=N'EcommerceAssignmentLab';
```

**Check and explain:** One matching name after creation. Start with this name unused; do not run in a transaction.

### DATABASE_SCHEMA_USER-01-32 — Database

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
SELECT DB_NAME() AS DatabaseName, DB_ID() AS DatabaseID, DATABASEPROPERTYEX(DB_NAME(),'Collation') AS Collation;
```

**Check and explain:** Values describe the selected training database.

### DATABASE_SCHEMA_USER-01-36 — Database

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
SELECT name, state_desc, recovery_model_desc FROM sys.databases ORDER BY name;
```

**Check and explain:** Results depend on permissions and the server; one row per visible database.

### DATABASE_SCHEMA_USER-01-40 — Database

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
SELECT name, type_desc, size*8.0/1024 AS SizeMB FROM sys.database_files ORDER BY file_id;
```

**Check and explain:** size is stored in 8-KB pages; this reports allocated file size, not used space.

### DATABASE_SCHEMA_USER-01-44 — Database

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
SELECT name, compatibility_level FROM sys.databases WHERE database_id=DB_ID();
```

**Check and explain:** An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

### DATABASE_SCHEMA_USER-02-28 — Schema

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'ecommerceAssignmentSchema') IS NOT NULL THROW 51000, 'Use an unused schema name', 1;
BEGIN TRANSACTION;
BEGIN TRY
EXEC(N'CREATE SCHEMA [ecommerceAssignmentSchema] AUTHORIZATION dbo;');
SELECT name, USER_NAME(principal_id) AS OwnerName FROM sys.schemas WHERE name=N'ecommerceAssignmentSchema';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** OwnerName=dbo. DDL requires appropriate database permissions.

### DATABASE_SCHEMA_USER-02-32 — Schema

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'ecommerceAssignmentSchema') IS NOT NULL THROW 51000, 'Use an unused schema name', 1;
BEGIN TRANSACTION;
BEGIN TRY
EXEC(N'CREATE SCHEMA [ecommerceAssignmentSchema] AUTHORIZATION dbo;');
CREATE TABLE [ecommerceAssignmentSchema].Records(ID int);
SELECT SCHEMA_NAME(schema_id) AS SchemaName, name FROM sys.tables WHERE object_id=OBJECT_ID(N'ecommerceAssignmentSchema.Records');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** The table belongs to the new schema. DDL requires appropriate database permissions.

### DATABASE_SCHEMA_USER-02-36 — Schema

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
SELECT name FROM sys.tables WHERE schema_id=SCHEMA_ID(N'ecommerce') ORDER BY name;
```

**Check and explain:** Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

### DATABASE_SCHEMA_USER-02-40 — Schema

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'ecommerceAssignmentSchema') IS NOT NULL THROW 51000, 'Use an unused schema name', 1;
IF OBJECT_ID(N'dbo.TransferLab') IS NOT NULL THROW 51000, 'Use an unused scratch table name', 1;
BEGIN TRANSACTION;
BEGIN TRY
EXEC(N'CREATE SCHEMA [ecommerceAssignmentSchema] AUTHORIZATION dbo;');
CREATE TABLE dbo.TransferLab(ID int);
ALTER SCHEMA [ecommerceAssignmentSchema] TRANSFER dbo.TransferLab;
SELECT OBJECT_ID(N'ecommerceAssignmentSchema.TransferLab') AS TransferredObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

### DATABASE_SCHEMA_USER-02-44 — Schema

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'ecommerceAssignmentSchema') IS NOT NULL THROW 51000, 'Use an unused schema name', 1;
BEGIN TRANSACTION;
BEGIN TRY
EXEC(N'CREATE SCHEMA [ecommerceAssignmentSchema];');
ALTER AUTHORIZATION ON SCHEMA::[ecommerceAssignmentSchema] TO dbo;
SELECT USER_NAME(principal_id) AS OwnerName FROM sys.schemas WHERE name=N'ecommerceAssignmentSchema';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** OwnerName=dbo. DDL requires appropriate database permissions.

### DATABASE_SCHEMA_USER-03-28 — User

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF DATABASE_PRINCIPAL_ID(N'ecommerceLabReader') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'ecommerceLabReaderRole') IS NOT NULL THROW 51000, 'Use unused principal names', 1;
BEGIN TRANSACTION;
BEGIN TRY
CREATE USER [ecommerceLabReader] WITHOUT LOGIN;
SELECT name, authentication_type_desc FROM sys.database_principals WHERE name=N'ecommerceLabReader';
SELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'ecommerceLabReader');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

### DATABASE_SCHEMA_USER-03-32 — User

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF DATABASE_PRINCIPAL_ID(N'ecommerceLabReader') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'ecommerceLabReaderRole') IS NOT NULL THROW 51000, 'Use unused principal names', 1;
BEGIN TRANSACTION;
BEGIN TRY
CREATE USER [ecommerceLabReader] WITHOUT LOGIN;
GRANT SELECT ON SCHEMA::[ecommerce] TO [ecommerceLabReader];
SELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'ecommerceLabReader');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

### DATABASE_SCHEMA_USER-03-36 — User

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF DATABASE_PRINCIPAL_ID(N'ecommerceLabReader') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'ecommerceLabReaderRole') IS NOT NULL THROW 51000, 'Use unused principal names', 1;
BEGIN TRANSACTION;
BEGIN TRY
CREATE USER [ecommerceLabReader] WITHOUT LOGIN;
GRANT SELECT ON SCHEMA::[ecommerce] TO [ecommerceLabReader];
REVOKE SELECT ON SCHEMA::[ecommerce] FROM [ecommerceLabReader];
SELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'ecommerceLabReader');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

### DATABASE_SCHEMA_USER-03-40 — User

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF DATABASE_PRINCIPAL_ID(N'ecommerceLabReader') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'ecommerceLabReaderRole') IS NOT NULL THROW 51000, 'Use unused principal names', 1;
BEGIN TRANSACTION;
BEGIN TRY
CREATE USER [ecommerceLabReader] WITHOUT LOGIN;
ALTER USER [ecommerceLabReader] WITH DEFAULT_SCHEMA=[ecommerce];
SELECT name, default_schema_name FROM sys.database_principals WHERE name=N'ecommerceLabReader';
SELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'ecommerceLabReader');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

### DATABASE_SCHEMA_USER-03-44 — User

**Question**

[Canonical questions](../questions/DATABASE_SCHEMA_USER.md)

**Reference answer**

```sql
IF DATABASE_PRINCIPAL_ID(N'ecommerceLabReader') IS NOT NULL OR DATABASE_PRINCIPAL_ID(N'ecommerceLabReaderRole') IS NOT NULL THROW 51000, 'Use unused principal names', 1;
BEGIN TRANSACTION;
BEGIN TRY
CREATE USER [ecommerceLabReader] WITHOUT LOGIN;
CREATE ROLE [ecommerceLabReaderRole];
GRANT SELECT ON SCHEMA::[ecommerce] TO [ecommerceLabReaderRole];
ALTER ROLE [ecommerceLabReaderRole] ADD MEMBER [ecommerceLabReader];
SELECT USER_NAME(role_principal_id) AS RoleName, USER_NAME(member_principal_id) AS MemberName FROM sys.database_role_members WHERE member_principal_id=USER_ID(N'ecommerceLabReader');
SELECT permission_name, state_desc FROM sys.database_permissions WHERE grantee_principal_id=USER_ID(N'ecommerceLabReader');
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Database: progression

**Beginner:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B01

**Valid baseline**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B02

**Missing input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B03

**Exact boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B04

**Two independent rows**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B05

**Duplicate proposal**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B06

**Metadata evidence**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B07

**Unknown versus zero**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B08

**Wrong type input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B09

**Dependency order**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B11

**Deterministic presentation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B12

**Least sufficient permission**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B13

**Name and scope collision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B14

**Empty state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-B15

**Independent acceptance check**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I02

**Lossless round trip**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I03

**All conflicting keys**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I04

**Drift before change**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I05

**Application bypass**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I06

**Partial input correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I07

**Idempotency decision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I08

**Reference membership**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I09

**Schema version precondition**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I10

**Before-image restoration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I14

**Two independent implementations**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-I15

**Auditable decision table**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: One matching name after creation. Start with this name unused; do not run in a transaction.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A12

**Nonunique history correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Values describe the selected training database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Results depend on permissions and the server; one row per visible database.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A14

**Independent corruption detector**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: size is stored in 8-KB pages; this reports allocated file size, not used space.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-01-A15

**Adversarial native case study**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: An instance hosts databases; each database has schemas containing objects. Compatibility level influences database behavior and is not the server version.

**Core reference:** Find `DATABASE_SCHEMA_USER-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Schema: progression

**Beginner:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B01

**Valid baseline**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B02

**Missing input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B03

**Exact boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B04

**Two independent rows**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B05

**Duplicate proposal**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B06

**Metadata evidence**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B07

**Unknown versus zero**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B08

**Wrong type input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B09

**Dependency order**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B11

**Deterministic presentation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B12

**Least sufficient permission**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B13

**Name and scope collision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B14

**Empty state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-B15

**Independent acceptance check**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I02

**Lossless round trip**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I03

**All conflicting keys**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I04

**Drift before change**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I05

**Application bypass**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I06

**Partial input correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I07

**Idempotency decision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I08

**Reference membership**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I09

**Schema version precondition**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I10

**Before-image restoration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I14

**Two independent implementations**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-I15

**Auditable decision table**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A12

**Nonunique history correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: The table belongs to the new schema. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Tables: Customers, Sellers, Products, Orders, OrderItems, Payments.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A14

**Independent corruption detector**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: The object resolves under the new schema; choose an unused dbo.TransferLab name. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-02-A15

**Adversarial native case study**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: OwnerName=dbo. DDL requires appropriate database permissions.

**Core reference:** Find `DATABASE_SCHEMA_USER-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### User: progression

**Beginner:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B01

**Valid baseline**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B02

**Missing input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B03

**Exact boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B04

**Two independent rows**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B05

**Duplicate proposal**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B06

**Metadata evidence**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B07

**Unknown versus zero**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B08

**Wrong type input**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B09

**Dependency order**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B11

**Deterministic presentation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B12

**Least sufficient permission**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B13

**Name and scope collision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B14

**Empty state**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-B15

**Independent acceptance check**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I02

**Lossless round trip**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I03

**All conflicting keys**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I04

**Drift before change**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I05

**Application bypass**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I06

**Partial input correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I07

**Idempotency decision**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I08

**Reference membership**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I09

**Schema version precondition**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I10

**Before-image restoration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I14

**Two independent implementations**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-I15

**Auditable decision table**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Authentication type is NONE; this user cannot log in independently. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A12

**Nonunique history correction**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: An explicit schema-level SELECT grant appears. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: No explicit SELECT grant remains. Other roles/grants can still provide access; REVOKE removes this grant only. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A14

**Independent corruption detector**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Default schema=ecommerce; default schema does not grant permissions. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DATABASE_SCHEMA_USER-03-A15

**Adversarial native case study**

[Canonical question](../questions/DATABASE_SCHEMA_USER.md#ecommerce-database_schema_user-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Membership shows the new reader role and user. Database users and server logins are distinct. These labs need no password or server configuration change.

**Core reference:** Find `DATABASE_SCHEMA_USER-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

