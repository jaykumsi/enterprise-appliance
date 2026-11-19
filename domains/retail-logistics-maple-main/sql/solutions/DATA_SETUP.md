# Retail Logistics: DATA SETUP — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DATA_SETUP.md)

## Teaching and troubleshooting

Load parents before children and compare the listed column order with each value list. Duplicate-key errors often mean the data was already loaded. Do not rerun inserts blindly.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DATA_SETUP-01-27 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_logistics.Customers') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_logistics.Customers');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-27 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_logistics].[Customers] (CustomerID, CustomerName, CustomerCode, Region) VALUES
(1,N'Customers Alpha',N'CUS-1',N'North'),
(2,N'Customers Beta',N'CUS-2',N'South'),
(3,N'Customers Gamma',N'CUS-3',N'North'),
(4,N'Customers Delta',N'CUS-4',N'West'),
(5,N'Customers Unused',N'CUS-5',N'East');
SELECT COUNT(*) AS LoadedRows FROM [retail_logistics].[Customers];
SELECT * FROM [retail_logistics].[Customers] ORDER BY CustomerID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-31 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_logistics.Carriers') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_logistics.Carriers');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-31 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_logistics].[Carriers] (CarrierID, CarrierName, CarrierCode, ServiceLevel) VALUES
(1,N'Logistics carrier 1',N'LOG-1',N'Express'),
(2,N'Logistics carrier 2',N'LOG-2',N'Standard'),
(3,N'Logistics carrier 3',N'LOG-3',N'Express'),
(4,N'Logistics carrier 4',N'LOG-4',N'Standard'),
(5,N'Logistics carrier 5',N'LOG-5',N'Express');
SELECT COUNT(*) AS LoadedRows FROM [retail_logistics].[Carriers];
SELECT * FROM [retail_logistics].[Carriers] ORDER BY CarrierID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-35 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_logistics.Shipments') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_logistics.Shipments');
```

**Check and explain:** 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-35 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_logistics].[Shipments] (ShipmentID, CustomerID, ShipmentReference, ShipmentCategory, Status, FreightCharge, DeclaredPackages, ShipDate, DispatchedAt, RecordedAt, Note, BackupNote, ParentShipmentID, CarrierID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4);
SELECT COUNT(*) AS LoadedRows FROM [retail_logistics].[Shipments];
SELECT * FROM [retail_logistics].[Shipments] ORDER BY ShipmentID;
```

**Check and explain:** LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-39 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_logistics.ShipmentPackages') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_logistics.ShipmentPackages');
```

**Check and explain:** 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-39 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_logistics].[ShipmentPackages] (PackageID, ShipmentID, TrackingNumber, WeightKg, PromisedDate) VALUES
(1,1,N'TRK-1',2,N'20240103'),
(2,1,N'TRK-2',3,N'20240103'),
(3,2,N'TRK-3',1,N'20240104'),
(4,3,N'TRK-4',4,N'20240104'),
(5,6,N'TRK-5',2,N'20240212');
SELECT COUNT(*) AS LoadedRows FROM [retail_logistics].[ShipmentPackages];
SELECT * FROM [retail_logistics].[ShipmentPackages] ORDER BY PackageID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-43 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'retail_logistics.TrackingEvents') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'retail_logistics.TrackingEvents');
```

**Check and explain:** 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-43 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [retail_logistics].[TrackingEvents] (TrackingEventID, PackageID, ScanReference, EventStatus, ScanTime, LocationName) VALUES
(1,1,N'SCAN-1',N'PickedUp',N'2024-01-01T13:00:00',N'Origin hub'),
(2,1,N'SCAN-2',N'Delivered',N'2024-01-03T10:00:00',N'Customer address'),
(3,2,N'SCAN-3',N'InTransit',N'2024-01-02T09:00:00',N'Regional hub'),
(4,3,N'SCAN-4',N'Delivered',N'2024-01-05T11:00:00',N'Customer address'),
(5,4,N'SCAN-5',N'PickedUp',N'2024-01-03T08:00:00',N'Origin hub');
SELECT COUNT(*) AS LoadedRows FROM [retail_logistics].[TrackingEvents];
SELECT * FROM [retail_logistics].[TrackingEvents] ORDER BY TrackingEventID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Create tables: progression

**Beginner:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-01-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: 14 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-01-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Insert data into the tables: progression

**Beginner:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-02-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### RETAIL_LOGISTICS-DATA_SETUP-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-27` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-31` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-35` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-39` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### RETAIL_LOGISTICS-DATA_SETUP-02-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#retail_logistics-data_setup-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-43` in this topic's earlier foundation answers. Also require the case-specific evidence above.

