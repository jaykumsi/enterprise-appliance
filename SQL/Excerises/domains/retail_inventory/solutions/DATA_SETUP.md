# Retail Inventory: DATA SETUP — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DATA_SETUP.md)

## Teaching and troubleshooting

Load parents before children and compare the listed column order with each value list. Duplicate-key errors often mean the data was already loaded. Do not rerun inserts blindly.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DATA_SETUP-01-28 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_inventory.Warehouses') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_inventory.Warehouses');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-28 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_inventory].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Region) VALUES
(1,N'Warehouses Alpha',N'WAR-1',N'North'),
(2,N'Warehouses Beta',N'WAR-2',N'South'),
(3,N'Warehouses Gamma',N'WAR-3',N'North'),
(4,N'Warehouses Delta',N'WAR-4',N'West'),
(5,N'Warehouses Unused',N'WAR-5',N'East');
SELECT COUNT(*) AS LoadedRows FROM [retail_inventory].[Warehouses];
SELECT * FROM [retail_inventory].[Warehouses] ORDER BY WarehouseID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-32 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_inventory.Products') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_inventory.Products');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-32 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_inventory].[Products] (ProductID, ProductName, SKU, UnitCost) VALUES
(1,N'Inventory product 1',N'INV-SKU-1',10),
(2,N'Inventory product 2',N'INV-SKU-2',20),
(3,N'Inventory product 3',N'INV-SKU-3',30),
(4,N'Inventory product 4',N'INV-SKU-4',40),
(5,N'Inventory product 5',N'INV-SKU-5',50);
SELECT COUNT(*) AS LoadedRows FROM [retail_inventory].[Products];
SELECT * FROM [retail_inventory].[Products] ORDER BY ProductID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-36 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_inventory.Suppliers') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_inventory.Suppliers');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-36 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_inventory].[Suppliers] (SupplierID, SupplierName, SupplierCode, LeadTimeDays) VALUES
(1,N'Inventory supplier 1',N'INV-SUP-1',2),
(2,N'Inventory supplier 2',N'INV-SUP-2',3),
(3,N'Inventory supplier 3',N'INV-SUP-3',4),
(4,N'Inventory supplier 4',N'INV-SUP-4',5),
(5,N'Inventory supplier 5',N'INV-SUP-5',6);
SELECT COUNT(*) AS LoadedRows FROM [retail_inventory].[Suppliers];
SELECT * FROM [retail_inventory].[Suppliers] ORDER BY SupplierID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-40 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_inventory.StockMovements') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_inventory.StockMovements');
```

**Check and explain:** 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-40 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_inventory].[StockMovements] (MovementID, WarehouseID, MovementReference, MovementCategory, Status, MovementValue, MovedUnits, MovementDate, MovedAt, RecordedAt, Note, BackupNote, ParentMovementID, ProductID, SupplierID, Direction) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,1,N'IN'),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,2,N'OUT'),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,3,N'IN'),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,4,N'IN'),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,1,N'OUT'),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,2,N'IN'),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,3,N'IN'),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,4,N'OUT'),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,1,N'IN'),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,2,N'IN'),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,3,N'OUT'),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,4,N'IN');
SELECT COUNT(*) AS LoadedRows FROM [retail_inventory].[StockMovements];
SELECT * FROM [retail_inventory].[StockMovements] ORDER BY MovementID;
```

**Check and explain:** LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-44 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_inventory.StockBalances') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_inventory.StockBalances');
```

**Check and explain:** 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-44 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_inventory].[StockBalances] (BalanceID, WarehouseID, ProductID, OpeningQuantity, QuantityOnHand, ReorderLevel) VALUES
(1,1,1,10,11,10),
(2,1,2,10,8,10),
(3,1,3,10,7,10),
(4,2,3,10,13,10),
(5,2,4,10,18,10),
(6,3,1,10,9,10),
(7,3,2,10,12,10),
(8,4,3,10,13,10),
(9,4,4,10,6,10),
(10,4,1,10,11,10),
(11,4,2,10,12,10);
SELECT COUNT(*) AS LoadedRows FROM [retail_inventory].[StockBalances];
SELECT * FROM [retail_inventory].[StockBalances] ORDER BY BalanceID;
```

**Check and explain:** LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Create tables: progression

**Beginner:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-01-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: 16 columns, 4 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-01-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: 6 columns, 2 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Insert data into the tables: progression

**Beginner:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-02-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_INVENTORY-DATA_SETUP-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-28` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-32` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-36` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-40` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_INVENTORY-DATA_SETUP-02-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#retail_inventory-data_setup-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: LoadedRows=11. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-44` in this topic's earlier foundation answers. Also require the case-specific evidence above.

