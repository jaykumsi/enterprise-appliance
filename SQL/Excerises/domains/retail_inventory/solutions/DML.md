# Retail Inventory: DML — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DML.md)

## Teaching and troubleshooting

Preview the target rows with SELECT using the same WHERE condition. Compare affected-row counts and unchanged rows. Reset the fixture between independent exercises.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DML-01-28 — Insert

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Region) VALUES
(100,N'Warehouses Alpha',N'NEW-100',N'North');
SELECT @@ROWCOUNT AS InsertedRows;
SELECT * FROM [retail_inventory].[Warehouses] WHERE WarehouseID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

### DML-02-28 — Update

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [retail_inventory].[Warehouses] WHERE WarehouseID=1;
UPDATE [retail_inventory].[Warehouses] SET WarehouseName=N'Revised name' WHERE WarehouseID=1;
SELECT @@ROWCOUNT AS UpdatedRows;
SELECT * FROM [retail_inventory].[Warehouses] WHERE WarehouseID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

### DML-03-28 — Delete

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Region) VALUES
(100,N'Warehouses Alpha',N'NEW-100',N'North');
DELETE FROM [retail_inventory].[Warehouses] WHERE WarehouseID=100;
SELECT @@ROWCOUNT AS DeletedRows;
SELECT COUNT(*) AS OriginalRowCount FROM [retail_inventory].[Warehouses];
SELECT * FROM [retail_inventory].[Warehouses] WHERE WarehouseID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

### DML-01-32 — Insert

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Products] (ProductID, ProductName, SKU, UnitCost) VALUES
(100,N'Inventory product 1',N'NEW-100',10);
SELECT @@ROWCOUNT AS InsertedRows;
SELECT * FROM [retail_inventory].[Products] WHERE ProductID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

### DML-02-32 — Update

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [retail_inventory].[Products] WHERE ProductID=1;
UPDATE [retail_inventory].[Products] SET UnitCost=UnitCost+1 WHERE ProductID=1;
SELECT @@ROWCOUNT AS UpdatedRows;
SELECT * FROM [retail_inventory].[Products] WHERE ProductID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

### DML-03-32 — Delete

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Products] (ProductID, ProductName, SKU, UnitCost) VALUES
(100,N'Inventory product 1',N'NEW-100',10);
DELETE FROM [retail_inventory].[Products] WHERE ProductID=100;
SELECT @@ROWCOUNT AS DeletedRows;
SELECT COUNT(*) AS OriginalRowCount FROM [retail_inventory].[Products];
SELECT * FROM [retail_inventory].[Products] WHERE ProductID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

### DML-01-36 — Insert

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Suppliers] (SupplierID, SupplierName, SupplierCode, LeadTimeDays) VALUES
(100,N'Inventory supplier 1',N'NEW-100',2);
SELECT @@ROWCOUNT AS InsertedRows;
SELECT * FROM [retail_inventory].[Suppliers] WHERE SupplierID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

### DML-02-36 — Update

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [retail_inventory].[Suppliers] WHERE SupplierID=1;
UPDATE [retail_inventory].[Suppliers] SET LeadTimeDays=LeadTimeDays+1 WHERE SupplierID=1;
SELECT @@ROWCOUNT AS UpdatedRows;
SELECT * FROM [retail_inventory].[Suppliers] WHERE SupplierID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

### DML-03-36 — Delete

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Suppliers] (SupplierID, SupplierName, SupplierCode, LeadTimeDays) VALUES
(100,N'Inventory supplier 1',N'NEW-100',2);
DELETE FROM [retail_inventory].[Suppliers] WHERE SupplierID=100;
SELECT @@ROWCOUNT AS DeletedRows;
SELECT COUNT(*) AS OriginalRowCount FROM [retail_inventory].[Suppliers];
SELECT * FROM [retail_inventory].[Suppliers] WHERE SupplierID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

### DML-01-40 — Insert

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[StockMovements] (MovementID, WarehouseID, MovementReference, MovementCategory, Status, MovementValue, MovedUnits, MovementDate, MovedAt, RecordedAt, Note, BackupNote, ParentMovementID, ProductID, SupplierID, Direction) VALUES
(100,1,N'NEW-100',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,1,N'IN');
SELECT @@ROWCOUNT AS InsertedRows;
SELECT * FROM [retail_inventory].[StockMovements] WHERE MovementID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

### DML-02-40 — Update

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [retail_inventory].[StockMovements] WHERE MovementID=1;
UPDATE [retail_inventory].[StockMovements] SET MovementValue=MovementValue+1 WHERE MovementID=1;
SELECT @@ROWCOUNT AS UpdatedRows;
SELECT * FROM [retail_inventory].[StockMovements] WHERE MovementID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

### DML-03-40 — Delete

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[StockMovements] (MovementID, WarehouseID, MovementReference, MovementCategory, Status, MovementValue, MovedUnits, MovementDate, MovedAt, RecordedAt, Note, BackupNote, ParentMovementID, ProductID, SupplierID, Direction) VALUES
(100,1,N'NEW-100',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,1,N'IN');
DELETE FROM [retail_inventory].[StockMovements] WHERE MovementID=100;
SELECT @@ROWCOUNT AS DeletedRows;
SELECT COUNT(*) AS OriginalRowCount FROM [retail_inventory].[StockMovements];
SELECT * FROM [retail_inventory].[StockMovements] WHERE MovementID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

### DML-01-44 — Insert

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[StockBalances] (BalanceID, WarehouseID, ProductID, OpeningQuantity, QuantityOnHand, ReorderLevel) VALUES
(100,1,5,10,11,10);
SELECT @@ROWCOUNT AS InsertedRows;
SELECT * FROM [retail_inventory].[StockBalances] WHERE BalanceID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

### DML-02-44 — Update

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [retail_inventory].[StockBalances] WHERE BalanceID=1;
UPDATE [retail_inventory].[StockBalances] SET OpeningQuantity=OpeningQuantity+1 WHERE BalanceID=1;
SELECT @@ROWCOUNT AS UpdatedRows;
SELECT * FROM [retail_inventory].[StockBalances] WHERE BalanceID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

### DML-03-44 — Delete

**Question**

[Canonical questions](../questions/DML.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[StockBalances] (BalanceID, WarehouseID, ProductID, OpeningQuantity, QuantityOnHand, ReorderLevel) VALUES
(100,1,5,10,11,10);
DELETE FROM [retail_inventory].[StockBalances] WHERE BalanceID=100;
SELECT @@ROWCOUNT AS DeletedRows;
SELECT COUNT(*) AS OriginalRowCount FROM [retail_inventory].[StockBalances];
SELECT * FROM [retail_inventory].[StockBalances] WHERE BalanceID=100;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Insert: progression

**Beginner:15 questions**

#### RETAIL_INVENTORY-DML-01-B01

**Valid baseline**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B02

**Missing input**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B03

**Exact boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B04

**Two independent rows**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B05

**Duplicate proposal**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B06

**Metadata evidence**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B07

**Unknown versus zero**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B08

**Wrong type input**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B09

**Dependency order**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B11

**Deterministic presentation**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B12

**Least sufficient permission**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B13

**Name and scope collision**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B14

**Empty state**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-B15

**Independent acceptance check**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_INVENTORY-DML-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I02

**Lossless round trip**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I03

**All conflicting keys**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I04

**Drift before change**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I05

**Application bypass**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I06

**Partial input correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I07

**Idempotency decision**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I08

**Reference membership**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I09

**Schema version precondition**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I10

**Before-image restoration**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I14

**Two independent implementations**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-I15

**Auditable decision table**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_INVENTORY-DML-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A12

**Nonunique history correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A14

**Independent corruption detector**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-01-A15

**Adversarial native case study**

[Canonical question](../questions/DML.md#retail_inventory-dml-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.

**Core reference:** Find `DML-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Update: progression

**Beginner:15 questions**

#### RETAIL_INVENTORY-DML-02-B01

**Valid baseline**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B02

**Missing input**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B03

**Exact boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B04

**Two independent rows**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B05

**Duplicate proposal**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B06

**Metadata evidence**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B07

**Unknown versus zero**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B08

**Wrong type input**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B09

**Dependency order**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B11

**Deterministic presentation**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B12

**Least sufficient permission**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B13

**Name and scope collision**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B14

**Empty state**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-B15

**Independent acceptance check**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_INVENTORY-DML-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I02

**Lossless round trip**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I03

**All conflicting keys**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I04

**Drift before change**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I05

**Application bypass**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I06

**Partial input correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I07

**Idempotency decision**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I08

**Reference membership**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I09

**Schema version precondition**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I10

**Before-image restoration**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I14

**Two independent implementations**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-I15

**Auditable decision table**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_INVENTORY-DML-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A12

**Nonunique history correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A14

**Independent corruption detector**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-02-A15

**Adversarial native case study**

[Canonical question](../questions/DML.md#retail_inventory-dml-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.

**Core reference:** Find `DML-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Delete: progression

**Beginner:15 questions**

#### RETAIL_INVENTORY-DML-03-B01

**Valid baseline**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B02

**Missing input**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B03

**Exact boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B04

**Two independent rows**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B05

**Duplicate proposal**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B06

**Metadata evidence**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B07

**Unknown versus zero**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B08

**Wrong type input**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B09

**Dependency order**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B10

**Rejected request preserves state**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B11

**Deterministic presentation**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B12

**Least sufficient permission**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B13

**Name and scope collision**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B14

**Empty state**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-B15

**Independent acceptance check**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_INVENTORY-DML-03-I01

**Batch with mixed validity**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I02

**Lossless round trip**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I03

**All conflicting keys**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I04

**Drift before change**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I05

**Application bypass**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I06

**Partial input correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I07

**Idempotency decision**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I08

**Reference membership**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I09

**Schema version precondition**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I10

**Before-image restoration**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I14

**Two independent implementations**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-I15

**Auditable decision table**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_INVENTORY-DML-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A03

**Crash after accepted effect**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A07

**Restartable chunked repair**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A08

**Stale authorization at execution**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A10

**Atomic publication boundary**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A11

**Type or scope spoofing**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A12

**Nonunique history correction**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A13

**Owner failure and fencing**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: DeletedRows=1; original count=5; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A14

**Independent corruption detector**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: DeletedRows=1; original count=12; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DML-03-A15

**Adversarial native case study**

[Canonical question](../questions/DML.md#retail_inventory-dml-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: DeletedRows=1; original count=11; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.

**Core reference:** Find `DML-03-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

