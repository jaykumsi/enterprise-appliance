# E-commerce: DDL — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DDL.md)

## Teaching and troubleshooting

Compare column names, types and nullability first, then keys and constraints. Create parent tables before children. A table with the correct columns can still be missing required constraints.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DDL-01-28 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
IF SCHEMA_ID(N'ecommerce') IS NULL EXEC(N'CREATE SCHEMA [ecommerce] AUTHORIZATION dbo;');
CREATE TABLE [ecommerce].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [CustomerCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (CustomerCode),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
CREATE TABLE [ecommerce].[Sellers] (
    [SellerID] int NOT NULL,
    [SellerName] nvarchar(80) NOT NULL,
    [SellerCode] varchar(20) NOT NULL,
    [Department] varchar(20) NOT NULL,
    CONSTRAINT [PK_Sellers] PRIMARY KEY ([SellerID]),
    CONSTRAINT [UQ_Sellers_1] UNIQUE (SellerCode),
    CONSTRAINT [CK_Sellers_1] CHECK (LEN(LTRIM(RTRIM(SellerName))) > 0)
);
```

**Check and explain:** Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-28 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Customers] ADD ContactPhone varchar(30) NULL;
EXEC sys.sp_help N'ecommerce.Customers';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-28 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Orders] DROP CONSTRAINT [FK_Orders_CustomerID];
DROP TABLE [ecommerce].[Customers];
SELECT OBJECT_ID(N'ecommerce.Customers') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-32 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [ecommerce].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [SKU] varchar(20) NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    [Department] varchar(20) NOT NULL DEFAULT ('General'),
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (SKU),
    CONSTRAINT [CK_Products_1] CHECK (UnitPrice > 0),
    CONSTRAINT [CK_Products_2] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
```

**Check and explain:** Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-32 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Sellers] DROP CONSTRAINT [CK_Sellers_1];
ALTER TABLE [ecommerce].[Sellers] ALTER COLUMN SellerName nvarchar(120) NOT NULL;
ALTER TABLE [ecommerce].[Sellers] WITH CHECK ADD CONSTRAINT [CK_Sellers_1] CHECK (LEN(LTRIM(RTRIM(SellerName))) > 0);
EXEC sys.sp_help N'ecommerce.Sellers';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-32 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Orders] DROP CONSTRAINT [FK_Orders_SellerID];
DROP TABLE [ecommerce].[Sellers];
SELECT OBJECT_ID(N'ecommerce.Sellers') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-36 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [ecommerce].[Orders] (
    [OrderID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [OrderReference] nvarchar(80) NOT NULL,
    [SalesChannel] varchar(10) NOT NULL,
    [OrderStatus] varchar(10) NOT NULL DEFAULT ('Open'),
    [OrderTotal] decimal(12,2) NULL,
    [ItemCount] int NOT NULL,
    [OrderDate] date NOT NULL,
    [PlacedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentOrderID] int NULL,
    [SellerID] int NOT NULL,
    CONSTRAINT [PK_Orders] PRIMARY KEY ([OrderID]),
    CONSTRAINT [UQ_Orders_1] UNIQUE (OrderReference),
    CONSTRAINT [CK_Orders_1] CHECK (SalesChannel IN ('A','B','C')),
    CONSTRAINT [CK_Orders_2] CHECK (OrderStatus IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Orders_3] CHECK (OrderTotal >= 0),
    CONSTRAINT [CK_Orders_4] CHECK (ItemCount > 0),
    CONSTRAINT [CK_Orders_5] CHECK (ParentOrderID IS NULL OR ParentOrderID <> OrderID),
    CONSTRAINT [CK_Orders_6] CHECK (LEN(LTRIM(RTRIM(OrderReference))) > 0),
    CONSTRAINT [FK_Orders_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [ecommerce].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Orders_ParentOrderID] FOREIGN KEY ([ParentOrderID]) REFERENCES [ecommerce].[Orders] ([OrderID]),
    CONSTRAINT [FK_Orders_SellerID] FOREIGN KEY ([SellerID]) REFERENCES [ecommerce].[Sellers] ([SellerID])
);
```

**Check and explain:** Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-36 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Products] ADD AuditNote nvarchar(200) NULL;
EXEC sys.sp_help N'ecommerce.Products';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-36 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[OrderItems] DROP CONSTRAINT [FK_OrderItems_ProductID];
DROP TABLE [ecommerce].[Products];
SELECT OBJECT_ID(N'ecommerce.Products') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-40 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [ecommerce].[OrderItems] (
    [OrderItemID] int NOT NULL,
    [OrderID] int NOT NULL,
    [ProductID] int NOT NULL,
    [Quantity] int NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_OrderItems] PRIMARY KEY ([OrderItemID]),
    CONSTRAINT [UQ_OrderItems_1] UNIQUE (OrderID, ProductID),
    CONSTRAINT [CK_OrderItems_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_OrderItems_2] CHECK (UnitPrice >= 0),
    CONSTRAINT [FK_OrderItems_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [ecommerce].[Orders] ([OrderID]),
    CONSTRAINT [FK_OrderItems_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [ecommerce].[Products] ([ProductID])
);
```

**Check and explain:** OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-40 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[Orders] ADD Reviewed bit NOT NULL DEFAULT(0) WITH VALUES;
EXEC sys.sp_help N'ecommerce.Orders';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-40 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[OrderItems] DROP CONSTRAINT [FK_OrderItems_OrderID];
ALTER TABLE [ecommerce].[Payments] DROP CONSTRAINT [FK_Payments_OrderID];
DROP TABLE [ecommerce].[Orders];
SELECT OBJECT_ID(N'ecommerce.Orders') AS RemovedObjectID;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

### DDL-01-44 — Create

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
CREATE TABLE [ecommerce].[Payments] (
    [PaymentID] int NOT NULL,
    [OrderID] int NOT NULL,
    [PaymentMethod] varchar(10) NOT NULL,
    [PaidAmount] decimal(12,2) NOT NULL,
    [PaidAt] datetime2(3) NOT NULL,
    CONSTRAINT [PK_Payments] PRIMARY KEY ([PaymentID]),
    CONSTRAINT [CK_Payments_1] CHECK (PaymentMethod IN ('Card','Wallet','GiftCard','COD')),
    CONSTRAINT [CK_Payments_2] CHECK (PaidAmount > 0),
    CONSTRAINT [CK_Payments_3] CHECK (LEN(LTRIM(RTRIM(PaymentMethod))) > 0),
    CONSTRAINT [FK_Payments_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [ecommerce].[Orders] ([OrderID])
);
```

**Check and explain:** Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

### DDL-02-44 — Alter

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
ALTER TABLE [ecommerce].[OrderItems] ADD ExternalReference varchar(30) NULL;
ALTER TABLE [ecommerce].[OrderItems] ALTER COLUMN ExternalReference varchar(60) NULL;
ALTER TABLE [ecommerce].[OrderItems] DROP COLUMN ExternalReference;
EXEC sys.sp_help N'ecommerce.OrderItems';
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

### DDL-03-44 — Drop

**Question**

[Canonical questions](../questions/DDL.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY

DROP TABLE [ecommerce].[OrderItems];
SELECT OBJECT_ID(N'ecommerce.OrderItems') AS RemovedObjectID;
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

#### ECOMMERCE-DDL-01-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B02

**Missing input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B09

**Dependency order**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B14

**Empty state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DDL-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I04

**Drift before change**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I05

**Application bypass**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I08

**Reference membership**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DDL-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Customers exists with PK CustomerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Sellers exists with PK SellerID, 0 FK(s), 1 UNIQUE rule(s) and 1 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Products exists with PK ProductID, 0 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Orders exists with PK OrderID, 3 FK(s), 1 UNIQUE rule(s) and 6 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: OrderItems exists with PK OrderItemID, 2 FK(s), 1 UNIQUE rule(s) and 2 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-01-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#ecommerce-ddl-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Payments exists with PK PaymentID, 1 FK(s), 0 UNIQUE rule(s) and 3 CHECK rule(s). Use the metadata checks in the project brief; matching column names alone is insufficient.

**Core reference:** Find `DDL-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Alter: progression

**Beginner:15 questions**

#### ECOMMERCE-DDL-02-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B02

**Missing input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B09

**Dependency order**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B14

**Empty state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DDL-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I04

**Drift before change**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I05

**Application bypass**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I08

**Reference membership**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DDL-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-02-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#ecommerce-ddl-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.

**Core reference:** Find `DDL-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Drop: progression

**Beginner:15 questions**

#### ECOMMERCE-DDL-03-B01

**Valid baseline**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B02

**Missing input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B03

**Exact boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B04

**Two independent rows**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B05

**Duplicate proposal**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B06

**Metadata evidence**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B07

**Unknown versus zero**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B08

**Wrong type input**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B09

**Dependency order**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B11

**Deterministic presentation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B12

**Least sufficient permission**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B13

**Name and scope collision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B14

**Empty state**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-B15

**Independent acceptance check**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### ECOMMERCE-DDL-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I02

**Lossless round trip**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I03

**All conflicting keys**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I04

**Drift before change**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I05

**Application bypass**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I06

**Partial input correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I07

**Idempotency decision**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I08

**Reference membership**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I09

**Schema version precondition**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I10

**Before-image restoration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I14

**Two independent implementations**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-I15

**Auditable decision table**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### ECOMMERCE-DDL-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A12

**Nonunique history correction**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=1. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A14

**Independent corruption detector**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=2. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### ECOMMERCE-DDL-03-A15

**Adversarial native case study**

[Canonical question](../questions/DDL.md#ecommerce-ddl-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: RemovedObjectID is NULL inside the transaction. Incoming FK count=0. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.

**Core reference:** Find `DDL-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

