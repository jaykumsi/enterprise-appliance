# Brokerage: DATA SETUP — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/DATA_SETUP.md)

## Teaching and troubleshooting

Load parents before children and compare the listed column order with each value list. Duplicate-key errors often mean the data was already loaded. Do not rerun inserts blindly.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### DATA_SETUP-01-29 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'brokerage.Clients') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'brokerage.Clients');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-29 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [brokerage].[Clients] (ClientID, ClientName, ClientReference, Email) VALUES
(1,N'Investor 1',N'CLIENT-1',N'investor1@example.test'),
(2,N'Investor 2',N'CLIENT-2',N'investor2@example.test'),
(3,N'Investor 3',N'CLIENT-3',N'investor3@example.test'),
(4,N'Investor 4',N'CLIENT-4',N'investor4@example.test'),
(5,N'Investor 5',N'CLIENT-5',N'investor5@example.test');
SELECT COUNT(*) AS LoadedRows FROM [brokerage].[Clients];
SELECT * FROM [brokerage].[Clients] ORDER BY ClientID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-33 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'brokerage.Securities') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'brokerage.Securities');
```

**Check and explain:** 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-33 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [brokerage].[Securities] (SecurityID, SecurityName, Symbol, AssetClass) VALUES
(1,N'Training Equity Alpha',N'DEMO-A',N'Stock'),
(2,N'Training Equity Beta',N'DEMO-B',N'Stock'),
(3,N'Training Fund Gamma',N'DEMO-C',N'ETF'),
(4,N'Training Fund Delta',N'DEMO-D',N'ETF'),
(5,N'Unused Training Equity',N'DEMO-E',N'Stock');
SELECT COUNT(*) AS LoadedRows FROM [brokerage].[Securities];
SELECT * FROM [brokerage].[Securities] ORDER BY SecurityID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-37 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'brokerage.BrokerageAccounts') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'brokerage.BrokerageAccounts');
```

**Check and explain:** 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-37 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [brokerage].[BrokerageAccounts] (AccountID, AccountName, AccountNumber, Region, ClientID) VALUES
(1,N'BrokerageAccounts Alpha',N'ACC-1',N'North',1),
(2,N'BrokerageAccounts Beta',N'ACC-2',N'South',2),
(3,N'BrokerageAccounts Gamma',N'ACC-3',N'North',3),
(4,N'BrokerageAccounts Delta',N'ACC-4',N'West',4),
(5,N'BrokerageAccounts Unused',N'ACC-5',N'East',5);
SELECT COUNT(*) AS LoadedRows FROM [brokerage].[BrokerageAccounts];
SELECT * FROM [brokerage].[BrokerageAccounts] ORDER BY AccountID;
```

**Check and explain:** LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-41 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'brokerage.TradeOrders') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'brokerage.TradeOrders');
```

**Check and explain:** 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-41 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [brokerage].[TradeOrders] (OrderID, AccountID, OrderReference, RoutingCategory, WorkflowStatus, EstimatedValue, RequestedQuantity, OrderDate, SubmittedAt, RecordedAt, Note, BackupNote, ParentOrderID, SecurityID, Side) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,N'Buy'),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,N'Buy'),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,N'Buy'),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,N'Buy'),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,N'Buy'),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,N'Buy'),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,N'Buy'),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,N'Buy'),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,N'Buy'),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,N'Buy'),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,N'Buy'),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,N'Buy');
SELECT COUNT(*) AS LoadedRows FROM [brokerage].[TradeOrders];
SELECT * FROM [brokerage].[TradeOrders] ORDER BY OrderID;
```

**Check and explain:** LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

### DATA_SETUP-01-45 — Create tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'brokerage.Executions') ORDER BY c.column_id;
SELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'brokerage.Executions');
```

**Check and explain:** 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

### DATA_SETUP-02-45 — Insert data into the tables

**Question**

[Canonical questions](../questions/DATA_SETUP.md)

**Reference answer**

```sql
INSERT INTO [brokerage].[Executions] (ExecutionID, OrderID, ExecutionReference, ExecutedQuantity, ExecutionPrice, ExecutedAt) VALUES
(1,1,N'FILL-1',0.4,100,N'2024-01-01T12:31:00'),
(2,1,N'FILL-2',0.6,101,N'2024-01-01T12:32:00'),
(3,2,N'FILL-3',1,99,N'2024-01-02T12:31:00'),
(4,2,N'FILL-4',0.5,100,N'2024-01-02T12:32:00'),
(5,3,N'FILL-5',3,101,N'2024-01-02T12:33:00'),
(6,6,N'FILL-6',1,150,N'2024-02-10T12:31:00');
SELECT COUNT(*) AS LoadedRows FROM [brokerage].[Executions];
SELECT * FROM [brokerage].[Executions] ORDER BY ExecutionID;
```

**Check and explain:** LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Create tables: progression

**Beginner:15 questions**

#### BROKERAGE-DATA_SETUP-01-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### BROKERAGE-DATA_SETUP-01-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### BROKERAGE-DATA_SETUP-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: 4 columns, 0 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: 5 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: 15 columns, 3 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-01-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: 6 columns, 1 foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.

**Core reference:** Find `DATA_SETUP-01-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Insert data into the tables: progression

**Beginner:15 questions**

#### BROKERAGE-DATA_SETUP-02-B01

**Valid baseline**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B02

**Missing input**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B03

**Exact boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B04

**Two independent rows**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B05

**Duplicate proposal**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B06

**Metadata evidence**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B07

**Unknown versus zero**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B08

**Wrong type input**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B09

**Dependency order**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B10

**Rejected request preserves state**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B11

**Deterministic presentation**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B12

**Least sufficient permission**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B13

**Name and scope collision**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B14

**Empty state**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-B15

**Independent acceptance check**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### BROKERAGE-DATA_SETUP-02-I01

**Batch with mixed validity**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I02

**Lossless round trip**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I03

**All conflicting keys**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I04

**Drift before change**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I05

**Application bypass**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I06

**Partial input correction**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I07

**Idempotency decision**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I08

**Reference membership**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I09

**Schema version precondition**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I10

**Before-image restoration**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I14

**Two independent implementations**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-I15

**Auditable decision table**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### BROKERAGE-DATA_SETUP-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A03

**Crash after accepted effect**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A07

**Restartable chunked repair**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A08

**Stale authorization at execution**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A10

**Atomic publication boundary**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A11

**Type or scope spoofing**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-29` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A12

**Nonunique history correction**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-33` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A13

**Owner failure and fencing**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: LoadedRows=5. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-37` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A14

**Independent corruption detector**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: LoadedRows=12. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-41` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### BROKERAGE-DATA_SETUP-02-A15

**Adversarial native case study**

[Canonical question](../questions/DATA_SETUP.md#brokerage-data_setup-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: LoadedRows=6. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.

**Core reference:** Find `DATA_SETUP-02-45` in this topic's earlier foundation answers. Also require the case-specific evidence above.

