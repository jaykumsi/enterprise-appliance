# Retail Supply Chain: connected SQL Server project

Buy or make products, move stock through warehouses, and compare and check production, receipts, dispatches and balances.

**Goal:** build and explain nine related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Products ||--o{ BillOfMaterials : "ProductID"
    Materials ||--o{ BillOfMaterials : "MaterialID"
    Products ||--o{ ProductionOrders : "ProductID"
    Warehouses ||--o{ ProductionOrders : "WarehouseID"
    ProductionOrders ||--o{ MaterialUsage : "ProductionOrderID"
    Materials ||--o{ MaterialUsage : "MaterialID"
    Warehouses ||--o{ StockMovements : "WarehouseID"
    StockMovements |o--o{ StockMovements : "ParentMovementID"
    Products ||--o{ StockMovements : "ProductID"
    Suppliers ||--o{ StockMovements : "SupplierID"
    ProductionOrders |o--o{ StockMovements : "ProductionOrderID"
    Warehouses ||--o{ StockBalances : "WarehouseID"
    Products ||--o{ StockBalances : "ProductID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the nine tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Warehouses → Suppliers → Products → Materials → BillOfMaterials → ProductionOrders → MaterialUsage → StockMovements → StockBalances**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Warehouses

**Warehouses** — Fulfillment centers and store depots; each warehouse has stock movements and balances and receives private label production.

| Column | Type | Requirement |
|---|---|---|
| WarehouseID | int | NOT NULL |
| WarehouseName | nvarchar(80) | NOT NULL |
| WarehouseCode | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **WarehouseID**.
Unique business key: **WarehouseCode**.
Business rule: `LEN(LTRIM(RTRIM(WarehouseName))) > 0`.

### Suppliers

**Suppliers** — Where stock comes from. Supplier 4 is the in-house Private Label plant, the source of every Made product.

| Column | Type | Requirement |
|---|---|---|
| SupplierID | int | NOT NULL |
| SupplierName | nvarchar(80) | NOT NULL |
| SupplierCode | varchar(20) | NOT NULL |
| LeadTimeDays | int | NOT NULL |

Primary key: **SupplierID**.
Unique business key: **SupplierCode**.
Business rule: `LeadTimeDays >= 0`.
Business rule: `LEN(LTRIM(RTRIM(SupplierName))) > 0`.

### Products

**Products** — One catalog: Bought products come from outside suppliers; Made products are produced in the Private Label plant from a recipe.

| Column | Type | Requirement |
|---|---|---|
| ProductID | int | NOT NULL |
| ProductName | nvarchar(80) | NOT NULL |
| SKU | varchar(20) | NOT NULL |
| UnitCost | decimal(12,2) | NOT NULL |
| Sourcing | varchar(10) | NOT NULL DEFAULT ('Bought') |

Primary key: **ProductID**.
Unique business key: **SKU**.
Business rule: `UnitCost > 0`.
Business rule: `Sourcing IN ('Bought','Made')`.
Business rule: `LEN(LTRIM(RTRIM(ProductName))) > 0`.

### Materials

**Materials** — Raw materials for Made products. Quantities are in the material-specific unit.

| Column | Type | Requirement |
|---|---|---|
| MaterialID | int | NOT NULL |
| MaterialName | nvarchar(80) | NOT NULL |
| MaterialCode | varchar(20) | NOT NULL |
| UnitCost | decimal(12,2) | NOT NULL |

Primary key: **MaterialID**.
Unique business key: **MaterialCode**.
Business rule: `UnitCost > 0`.
Business rule: `LEN(LTRIM(RTRIM(MaterialName))) > 0`.

### BillOfMaterials

**BillOfMaterials** — Recipe bridge: one row per Made product and required material, per unit produced.

| Column | Type | Requirement |
|---|---|---|
| BOMID | int | NOT NULL |
| ProductID | int | NOT NULL |
| MaterialID | int | NOT NULL |
| QuantityPerUnit | decimal(12,2) | NOT NULL |

Primary key: **BOMID**.
Unique business key: **ProductID, MaterialID**.
Business rule: `QuantityPerUnit > 0`.
Foreign key: **BillOfMaterials.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **BillOfMaterials.MaterialID → Materials.MaterialID**. Use NO ACTION on delete/update; do not disable checking.

### ProductionOrders

**ProductionOrders** — Factory runs for Made products. PlannedCost is the recipe material cost; finished units are received into WarehouseID.

| Column | Type | Requirement |
|---|---|---|
| ProductionOrderID | int | NOT NULL |
| ProductID | int | NOT NULL |
| WarehouseID | int | NOT NULL |
| ProductionReference | varchar(20) | NOT NULL |
| ProductionStatus | varchar(12) | NOT NULL |
| PlannedUnits | int | NOT NULL |
| PlannedCost | decimal(12,2) | NOT NULL |
| StartDate | date | NOT NULL |
| CompletedDate | date | NULL |

Primary key: **ProductionOrderID**.
Unique business key: **ProductionReference**.
Business rule: `ProductionStatus IN ('Planned','InProgress','Completed')`.
Business rule: `PlannedUnits > 0`.
Business rule: `PlannedCost >= 0`.
Business rule: `CompletedDate IS NULL OR CompletedDate >= StartDate`.
Business rule: `LEN(LTRIM(RTRIM(ProductionReference))) > 0`.
Foreign key: **ProductionOrders.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **ProductionOrders.WarehouseID → Warehouses.WarehouseID**. Use NO ACTION on delete/update; do not disable checking.

### MaterialUsage

**MaterialUsage** — Actual material consumed per production order and material; compare it with the recipe.

| Column | Type | Requirement |
|---|---|---|
| UsageID | int | NOT NULL |
| ProductionOrderID | int | NOT NULL |
| MaterialID | int | NOT NULL |
| QuantityUsed | decimal(12,2) | NOT NULL |
| UsageDate | date | NOT NULL |

Primary key: **UsageID**.
Unique business key: **ProductionOrderID, MaterialID**.
Business rule: `QuantityUsed > 0`.
Foreign key: **MaterialUsage.ProductionOrderID → ProductionOrders.ProductionOrderID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **MaterialUsage.MaterialID → Materials.MaterialID**. Use NO ACTION on delete/update; do not disable checking.

### StockMovements

**StockMovements** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| MovementID | int | NOT NULL |
| WarehouseID | int | NOT NULL |
| MovementReference | nvarchar(80) | NOT NULL |
| MovementCategory | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| MovementValue | decimal(12,2) | NULL |
| MovedUnits | int | NOT NULL |
| MovementDate | date | NOT NULL |
| MovedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentMovementID | int | NULL |
| ProductID | int | NOT NULL |
| SupplierID | int | NOT NULL |
| Direction | varchar(3) | NOT NULL |
| ProductionOrderID | int | NULL |

Primary key: **MovementID**.
Unique business key: **MovementReference**.
Business rule: `MovementCategory IN ('A','B','C')`.
Business rule: `Status IN ('Open','Closed','Pending')`.
Business rule: `MovementValue >= 0`.
Business rule: `MovedUnits > 0`.
Business rule: `ParentMovementID IS NULL OR ParentMovementID <> MovementID`.
Business rule: `Direction IN ('IN','OUT')`.
Business rule: `LEN(LTRIM(RTRIM(MovementReference))) > 0`.
Foreign key: **StockMovements.WarehouseID → Warehouses.WarehouseID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **StockMovements.ParentMovementID → StockMovements.MovementID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **StockMovements.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **StockMovements.SupplierID → Suppliers.SupplierID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **StockMovements.ProductionOrderID → ProductionOrders.ProductionOrderID**. Use NO ACTION on delete/update; do not disable checking.

### StockBalances

**StockBalances** — One snapshot per warehouse and product: opening stock plus the signed seed movements equals QuantityOnHand. No trigger updates it automatically.

| Column | Type | Requirement |
|---|---|---|
| BalanceID | int | NOT NULL |
| WarehouseID | int | NOT NULL |
| ProductID | int | NOT NULL |
| OpeningQuantity | int | NOT NULL |
| QuantityOnHand | int | NOT NULL |
| ReorderLevel | int | NOT NULL |

Primary key: **BalanceID**.
Unique business key: **WarehouseID, ProductID**.
Business rule: `OpeningQuantity >= 0`.
Business rule: `QuantityOnHand >= 0`.
Business rule: `ReorderLevel >= 0`.
Foreign key: **StockBalances.WarehouseID → Warehouses.WarehouseID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **StockBalances.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** nine tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Warehouses

| WarehouseID | WarehouseName | WarehouseCode | Region |
|---|---|---|---|
| `1` | `Warehouses Alpha` | `WAR-1` | `North` |
| `2` | `Warehouses Beta` | `WAR-2` | `South` |
| `3` | `Warehouses Gamma` | `WAR-3` | `North` |
| `4` | `Warehouses Delta` | `WAR-4` | `West` |
| `5` | `Warehouses Unused` | `WAR-5` | `East` |

### Sample rows: Suppliers

| SupplierID | SupplierName | SupplierCode | LeadTimeDays |
|---|---|---|---|
| `1` | `Supply chain supplier 1` | `SC-SUP-1` | `2` |
| `2` | `Supply chain supplier 2` | `SC-SUP-2` | `3` |
| `3` | `Supply chain supplier 3` | `SC-SUP-3` | `4` |
| `4` | `Private Label Plant` | `SC-SUP-4` | `1` |
| `5` | `Unused supplier` | `SC-SUP-5` | `6` |

### Sample rows: Products

| ProductID | ProductName | SKU | UnitCost | Sourcing |
|---|---|---|---|---|
| `1` | `Notebook` | `SC-SKU-1` | `10` | `Bought` |
| `2` | `Pen set` | `SC-SKU-2` | `4` | `Bought` |
| `3` | `Canvas tote` | `SC-SKU-3` | `15` | `Made` |
| `4` | `Travel pouch` | `SC-SKU-4` | `16` | `Made` |
| `5` | `Unused product` | `SC-SKU-5` | `8` | `Bought` |

### Sample rows: Materials

| MaterialID | MaterialName | MaterialCode | UnitCost |
|---|---|---|---|
| `1` | `Fabric` | `SC-MAT-1` | `5` |
| `2` | `Thread` | `SC-MAT-2` | `1` |
| `3` | `Zipper` | `SC-MAT-3` | `2` |
| `4` | `Packaging` | `SC-MAT-4` | `3` |
| `5` | `Unused trim` | `SC-MAT-5` | `4` |

### Sample rows: BillOfMaterials

| BOMID | ProductID | MaterialID | QuantityPerUnit |
|---|---|---|---|
| `1` | `3` | `1` | `2` |
| `2` | `3` | `2` | `1` |
| `3` | `4` | `1` | `1` |
| `4` | `4` | `3` | `2` |
| `5` | `4` | `4` | `1` |

### Sample rows: ProductionOrders

| ProductionOrderID | ProductID | WarehouseID | ProductionReference | ProductionStatus | PlannedUnits | PlannedCost | StartDate | CompletedDate |
|---|---|---|---|---|---|---|---|---|
| `1` | `3` | `2` | `PO-1` | `Completed` | `10` | `110` | `20231220` | `20231230` |
| `2` | `4` | `1` | `PO-2` | `Completed` | `5` | `60` | `20231222` | `20231229` |
| `3` | `3` | `3` | `PO-3` | `InProgress` | `8` | `88` | `20240201` | NULL |
| `4` | `4` | `4` | `PO-4` | `Planned` | `6` | `72` | `20240301` | NULL |

### Sample rows: MaterialUsage

| UsageID | ProductionOrderID | MaterialID | QuantityUsed | UsageDate |
|---|---|---|---|---|
| `1` | `1` | `1` | `20` | `20231221` |
| `2` | `1` | `2` | `10.5` | `20231221` |
| `3` | `2` | `1` | `5` | `20231223` |
| `4` | `2` | `3` | `10` | `20231223` |
| `5` | `2` | `4` | `5` | `20231223` |
| `6` | `3` | `1` | `8` | `20240202` |

### Sample rows: StockMovements

| MovementID | WarehouseID | MovementReference | MovementCategory | Status | MovementValue | MovedUnits | MovementDate | MovedAt | RecordedAt | Note | BackupNote | ParentMovementID | ProductID | SupplierID | Direction | ProductionOrderID |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `1` | `1` | `  Alpha-One  ` | `A` | `Open` | `100` | `1` | `20240101` | `2024-01-01T12:30:45.123` | `2024-01-01T12:30:45.123+00:00` | NULL | `backup` | NULL | `1` | `1` | `IN` | NULL |
| `2` | `1` | `beta-Two` | `B` | `Closed` | `200` | `2` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | NULL | `1` | `2` | `2` | `OUT` | NULL |
| `3` | `2` | `Gamma-Three ` | `C` | `Pending` | `200` | `3` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | `backup` | `1` | `3` | `4` | `IN` | `1` |
| `4` | `2` | ` Delta-Four` | `A` | `Open` | NULL | `4` | `20240103` | `2024-01-03T12:30:45.123` | `2024-01-03T12:30:45.123+00:00` | NULL | NULL | `2` | `4` | `4` | `IN` | NULL |
| `5` | `3` | `Echo-Five` | `B` | `Closed` | `50` | `1` | `20240201` | `2024-02-01T12:30:45.123` | `2024-02-01T12:30:45.123+00:00` | `confirmed` | `backup` | `2` | `1` | `1` | `OUT` | NULL |
| `6` | `3` | `ALPHA-Six` | `C` | `Pending` | `300` | `2` | `20240210` | `2024-02-10T12:30:45.123` | `2024-02-10T12:30:45.123+00:00` | `confirmed` | NULL | `3` | `2` | `2` | `IN` | NULL |
| `7` | `4` | `Zero-Seven` | `A` | `Open` | `0` | `3` | `20240229` | `2024-02-29T12:30:45.123` | `2024-02-29T12:30:45.123+00:00` | NULL | `backup` | `3` | `3` | `4` | `IN` | NULL |
| `8` | `4` | `Review-Eight` | `B` | `Closed` | `150` | `4` | `20240301` | `2024-03-01T12:30:45.123` | `2024-03-01T12:30:45.123+00:00` | `confirmed` | NULL | `4` | `4` | `4` | `OUT` | NULL |
| `9` | `4` | `Zulu-Nine` | `C` | `Pending` | `300` | `1` | `20240310` | `2024-03-10T12:30:45.123` | `2024-03-10T12:30:45.123+00:00` | `confirmed` | `backup` | `4` | `1` | `1` | `IN` | NULL |
| `10` | `4` | `Iota-Ten` | `A` | `Open` | `80` | `2` | `20241103` | `2024-11-03T12:30:45.123` | `2024-11-03T12:30:45.123+00:00` | NULL | NULL | `5` | `2` | `2` | `IN` | NULL |
| `11` | `1` | `Kappa-Eleven` | `B` | `Closed` | `120` | `3` | `20241231` | `2024-12-31T12:30:45.123` | `2024-12-31T12:30:45.123+00:00` | `confirmed` | `backup` | `5` | `3` | `4` | `OUT` | NULL |
| `12` | `2` | `Last-Twelve` | `C` | `Pending` | `200` | `4` | `20250101` | `2025-01-01T12:30:45.123` | `2025-01-01T12:30:45.123+00:00` | `confirmed` | NULL | `6` | `4` | `4` | `IN` | NULL |

### Sample rows: StockBalances

| BalanceID | WarehouseID | ProductID | OpeningQuantity | QuantityOnHand | ReorderLevel |
|---|---|---|---|---|---|
| `1` | `1` | `1` | `10` | `11` | `10` |
| `2` | `1` | `2` | `10` | `8` | `10` |
| `3` | `1` | `3` | `10` | `7` | `10` |
| `4` | `2` | `3` | `10` | `13` | `10` |
| `5` | `2` | `4` | `10` | `18` | `10` |
| `6` | `3` | `1` | `10` | `9` | `10` |
| `7` | `3` | `2` | `10` | `12` | `10` |
| `8` | `4` | `1` | `10` | `11` | `10` |
| `9` | `4` | `2` | `10` | `12` | `10` |
| `10` | `4` | `3` | `10` | `13` | `10` |
| `11` | `4` | `4` | `10` | `6` | `10` |
| `12` | `1` | `5` | `10` | `10` | `10` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-26, DDL-01-30, DDL-01-34, DDL-01-38, DDL-01-42 |
| [DDL](DDL.md) | Alter | DDL-02-26, DDL-02-30, DDL-02-34, DDL-02-38, DDL-02-42 |
| [DDL](DDL.md) | Drop | DDL-03-26, DDL-03-30, DDL-03-34, DDL-03-38, DDL-03-42 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-26, DATA_SETUP-01-30, DATA_SETUP-01-34, DATA_SETUP-01-38, DATA_SETUP-01-42 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-26, DATA_SETUP-02-30, DATA_SETUP-02-34, DATA_SETUP-02-38, DATA_SETUP-02-42 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-26, CONSTRAINTS-01-30, CONSTRAINTS-01-34, CONSTRAINTS-01-38, CONSTRAINTS-01-42 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-26, CONSTRAINTS-02-30, CONSTRAINTS-02-34, CONSTRAINTS-02-38, CONSTRAINTS-02-42 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-26, CONSTRAINTS-03-30, CONSTRAINTS-03-34, CONSTRAINTS-03-38, CONSTRAINTS-03-42 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-26, CONSTRAINTS-04-30, CONSTRAINTS-04-34, CONSTRAINTS-04-38, CONSTRAINTS-04-42 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-26, CONSTRAINTS-05-30, CONSTRAINTS-05-34, CONSTRAINTS-05-38, CONSTRAINTS-05-42 |
| [DML](DML.md) | Insert | DML-01-26, DML-01-30, DML-01-34, DML-01-38, DML-01-42 |
| [DML](DML.md) | Update | DML-02-26, DML-02-30, DML-02-34, DML-02-38, DML-02-42 |
| [DML](DML.md) | Delete | DML-03-26, DML-03-30, DML-03-34, DML-03-38, DML-03-42 |
| [DQL](DQL.md) | Select | DQL-01-26, DQL-01-30, DQL-01-34, DQL-01-38, DQL-01-42 |
| [DQL](DQL.md) | Where | DQL-02-26, DQL-02-30, DQL-02-34, DQL-02-38, DQL-02-42 |
| [DQL](DQL.md) | Group By | DQL-03-26, DQL-03-30, DQL-03-34, DQL-03-38, DQL-03-42 |
| [DQL](DQL.md) | Having | DQL-04-26, DQL-04-30, DQL-04-34, DQL-04-38, DQL-04-42 |
| [DQL](DQL.md) | Order By | DQL-05-26, DQL-05-30, DQL-05-34, DQL-05-38, DQL-05-42 |
| [DQL](DQL.md) | Top | DQL-06-26, DQL-06-30, DQL-06-34, DQL-06-38, DQL-06-42 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-26, OPERATORS-01-30, OPERATORS-01-34, OPERATORS-01-38, OPERATORS-01-42 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-26, OPERATORS-02-30, OPERATORS-02-34, OPERATORS-02-38, OPERATORS-02-42 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-26, OPERATORS-03-30, OPERATORS-03-34, OPERATORS-03-38, OPERATORS-03-42 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-26, OPERATORS-04-30, OPERATORS-04-34, OPERATORS-04-38, OPERATORS-04-42 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-26, OPERATORS-05-30, OPERATORS-05-34, OPERATORS-05-38, OPERATORS-05-42 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-26, OPERATORS-06-30, OPERATORS-06-34, OPERATORS-06-38, OPERATORS-06-42 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-26, OPERATORS-07-30, OPERATORS-07-34, OPERATORS-07-38, OPERATORS-07-42 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-26, OPERATORS-08-30, OPERATORS-08-34, OPERATORS-08-38, OPERATORS-08-42 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-26, OPERATORS-09-30, OPERATORS-09-34, OPERATORS-09-38, OPERATORS-09-42 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-26, OPERATORS-10-30, OPERATORS-10-34, OPERATORS-10-38, OPERATORS-10-42 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-26, OPERATORS-11-30, OPERATORS-11-34, OPERATORS-11-38, OPERATORS-11-42 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-26, OPERATORS-12-30, OPERATORS-12-34, OPERATORS-12-38, OPERATORS-12-42 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-26, OPERATORS-13-30, OPERATORS-13-34, OPERATORS-13-38, OPERATORS-13-42 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-26, JOINS-01-30, JOINS-01-34, JOINS-01-38, JOINS-01-42 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-26, JOINS-02-30, JOINS-02-34, JOINS-02-38, JOINS-02-42 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-26, JOINS-03-30, JOINS-03-34, JOINS-03-38, JOINS-03-42 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-26, JOINS-04-30, JOINS-04-34, JOINS-04-38, JOINS-04-42 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-26, JOINS-05-30, JOINS-05-34, JOINS-05-38, JOINS-05-42 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-26, SET_OPERATIONS-01-30, SET_OPERATIONS-01-34, SET_OPERATIONS-01-38, SET_OPERATIONS-01-42 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-26, SET_OPERATIONS-02-30, SET_OPERATIONS-02-34, SET_OPERATIONS-02-38, SET_OPERATIONS-02-42 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-26, SET_OPERATIONS-03-30, SET_OPERATIONS-03-34, SET_OPERATIONS-03-38, SET_OPERATIONS-03-42 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-26, SET_OPERATIONS-04-30, SET_OPERATIONS-04-34, SET_OPERATIONS-04-38, SET_OPERATIONS-04-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-26, STRING_FUNCTIONS-01-30, STRING_FUNCTIONS-01-34, STRING_FUNCTIONS-01-38, STRING_FUNCTIONS-01-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-26, STRING_FUNCTIONS-02-30, STRING_FUNCTIONS-02-34, STRING_FUNCTIONS-02-38, STRING_FUNCTIONS-02-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-26, STRING_FUNCTIONS-03-30, STRING_FUNCTIONS-03-34, STRING_FUNCTIONS-03-38, STRING_FUNCTIONS-03-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-26, STRING_FUNCTIONS-04-30, STRING_FUNCTIONS-04-34, STRING_FUNCTIONS-04-38, STRING_FUNCTIONS-04-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-26, STRING_FUNCTIONS-05-30, STRING_FUNCTIONS-05-34, STRING_FUNCTIONS-05-38, STRING_FUNCTIONS-05-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-26, STRING_FUNCTIONS-06-30, STRING_FUNCTIONS-06-34, STRING_FUNCTIONS-06-38, STRING_FUNCTIONS-06-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-26, STRING_FUNCTIONS-07-30, STRING_FUNCTIONS-07-34, STRING_FUNCTIONS-07-38, STRING_FUNCTIONS-07-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-26, STRING_FUNCTIONS-08-30, STRING_FUNCTIONS-08-34, STRING_FUNCTIONS-08-38, STRING_FUNCTIONS-08-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-26, STRING_FUNCTIONS-09-30, STRING_FUNCTIONS-09-34, STRING_FUNCTIONS-09-38, STRING_FUNCTIONS-09-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-26, STRING_FUNCTIONS-10-30, STRING_FUNCTIONS-10-34, STRING_FUNCTIONS-10-38, STRING_FUNCTIONS-10-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-26, STRING_FUNCTIONS-11-30, STRING_FUNCTIONS-11-34, STRING_FUNCTIONS-11-38, STRING_FUNCTIONS-11-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-26, STRING_FUNCTIONS-12-30, STRING_FUNCTIONS-12-34, STRING_FUNCTIONS-12-38, STRING_FUNCTIONS-12-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-26, STRING_FUNCTIONS-13-30, STRING_FUNCTIONS-13-34, STRING_FUNCTIONS-13-38, STRING_FUNCTIONS-13-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-26, STRING_FUNCTIONS-14-30, STRING_FUNCTIONS-14-34, STRING_FUNCTIONS-14-38, STRING_FUNCTIONS-14-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-26, STRING_FUNCTIONS-15-30, STRING_FUNCTIONS-15-34, STRING_FUNCTIONS-15-38, STRING_FUNCTIONS-15-42 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-26, STRING_FUNCTIONS-16-30, STRING_FUNCTIONS-16-34, STRING_FUNCTIONS-16-38, STRING_FUNCTIONS-16-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-26, DATE_FUNCTIONS-01-30, DATE_FUNCTIONS-01-34, DATE_FUNCTIONS-01-38, DATE_FUNCTIONS-01-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-26, DATE_FUNCTIONS-02-30, DATE_FUNCTIONS-02-34, DATE_FUNCTIONS-02-38, DATE_FUNCTIONS-02-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-26, DATE_FUNCTIONS-03-30, DATE_FUNCTIONS-03-34, DATE_FUNCTIONS-03-38, DATE_FUNCTIONS-03-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-26, DATE_FUNCTIONS-04-30, DATE_FUNCTIONS-04-34, DATE_FUNCTIONS-04-38, DATE_FUNCTIONS-04-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-26, DATE_FUNCTIONS-05-30, DATE_FUNCTIONS-05-34, DATE_FUNCTIONS-05-38, DATE_FUNCTIONS-05-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-26, DATE_FUNCTIONS-06-30, DATE_FUNCTIONS-06-34, DATE_FUNCTIONS-06-38, DATE_FUNCTIONS-06-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-26, DATE_FUNCTIONS-07-30, DATE_FUNCTIONS-07-34, DATE_FUNCTIONS-07-38, DATE_FUNCTIONS-07-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-26, DATE_FUNCTIONS-08-30, DATE_FUNCTIONS-08-34, DATE_FUNCTIONS-08-38, DATE_FUNCTIONS-08-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-26, DATE_FUNCTIONS-09-30, DATE_FUNCTIONS-09-34, DATE_FUNCTIONS-09-38, DATE_FUNCTIONS-09-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-26, DATE_FUNCTIONS-10-30, DATE_FUNCTIONS-10-34, DATE_FUNCTIONS-10-38, DATE_FUNCTIONS-10-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-26, DATE_FUNCTIONS-11-30, DATE_FUNCTIONS-11-34, DATE_FUNCTIONS-11-38, DATE_FUNCTIONS-11-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-26, DATE_FUNCTIONS-12-30, DATE_FUNCTIONS-12-34, DATE_FUNCTIONS-12-38, DATE_FUNCTIONS-12-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-26, DATE_FUNCTIONS-13-30, DATE_FUNCTIONS-13-34, DATE_FUNCTIONS-13-38, DATE_FUNCTIONS-13-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-26, DATE_FUNCTIONS-14-30, DATE_FUNCTIONS-14-34, DATE_FUNCTIONS-14-38, DATE_FUNCTIONS-14-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-26, DATE_FUNCTIONS-15-30, DATE_FUNCTIONS-15-34, DATE_FUNCTIONS-15-38, DATE_FUNCTIONS-15-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-26, DATE_FUNCTIONS-16-30, DATE_FUNCTIONS-16-34, DATE_FUNCTIONS-16-38, DATE_FUNCTIONS-16-42 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-26, DATE_FUNCTIONS-17-30, DATE_FUNCTIONS-17-34, DATE_FUNCTIONS-17-38, DATE_FUNCTIONS-17-42 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-26, AGGREGATES-01-30, AGGREGATES-01-34, AGGREGATES-01-38, AGGREGATES-01-42 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-26, AGGREGATES-02-30, AGGREGATES-02-34, AGGREGATES-02-38, AGGREGATES-02-42 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-26, AGGREGATES-03-30, AGGREGATES-03-34, AGGREGATES-03-38, AGGREGATES-03-42 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-26, AGGREGATES-04-30, AGGREGATES-04-34, AGGREGATES-04-38, AGGREGATES-04-42 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-26, AGGREGATES-05-30, AGGREGATES-05-34, AGGREGATES-05-38, AGGREGATES-05-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-26, ANALYTICAL_FUNCTIONS-01-30, ANALYTICAL_FUNCTIONS-01-34, ANALYTICAL_FUNCTIONS-01-38, ANALYTICAL_FUNCTIONS-01-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-26, ANALYTICAL_FUNCTIONS-02-30, ANALYTICAL_FUNCTIONS-02-34, ANALYTICAL_FUNCTIONS-02-38, ANALYTICAL_FUNCTIONS-02-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-26, ANALYTICAL_FUNCTIONS-03-30, ANALYTICAL_FUNCTIONS-03-34, ANALYTICAL_FUNCTIONS-03-38, ANALYTICAL_FUNCTIONS-03-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-26, ANALYTICAL_FUNCTIONS-04-30, ANALYTICAL_FUNCTIONS-04-34, ANALYTICAL_FUNCTIONS-04-38, ANALYTICAL_FUNCTIONS-04-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-26, ANALYTICAL_FUNCTIONS-05-30, ANALYTICAL_FUNCTIONS-05-34, ANALYTICAL_FUNCTIONS-05-38, ANALYTICAL_FUNCTIONS-05-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-26, ANALYTICAL_FUNCTIONS-06-30, ANALYTICAL_FUNCTIONS-06-34, ANALYTICAL_FUNCTIONS-06-38, ANALYTICAL_FUNCTIONS-06-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-26, ANALYTICAL_FUNCTIONS-07-30, ANALYTICAL_FUNCTIONS-07-34, ANALYTICAL_FUNCTIONS-07-38, ANALYTICAL_FUNCTIONS-07-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-26, ANALYTICAL_FUNCTIONS-08-30, ANALYTICAL_FUNCTIONS-08-34, ANALYTICAL_FUNCTIONS-08-38, ANALYTICAL_FUNCTIONS-08-42 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-26, ANALYTICAL_FUNCTIONS-09-30, ANALYTICAL_FUNCTIONS-09-34, ANALYTICAL_FUNCTIONS-09-38, ANALYTICAL_FUNCTIONS-09-42 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-26, CTE-01-30, CTE-01-34, CTE-01-38, CTE-01-42 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-26, CTE-02-30, CTE-02-34, CTE-02-38, CTE-02-42 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-26, CTE-03-30, CTE-03-34, CTE-03-38, CTE-03-42 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-26, CTE-04-30, CTE-04-34, CTE-04-38, CTE-04-42 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-26, CTE-05-30, CTE-05-34, CTE-05-38, CTE-05-42 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-26, DATATYPES-01-30, DATATYPES-01-34, DATATYPES-01-38, DATATYPES-01-42 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-26, DATATYPES-02-30, DATATYPES-02-34, DATATYPES-02-38, DATATYPES-02-42 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-26, DATATYPES-03-30, DATATYPES-03-34, DATATYPES-03-38, DATATYPES-03-42 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-26, DATATYPES-04-30, DATATYPES-04-34, DATATYPES-04-38, DATATYPES-04-42 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-26, DATATYPES-05-30, DATATYPES-05-34, DATATYPES-05-38, DATATYPES-05-42 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-26, DATATYPES-06-30, DATATYPES-06-34, DATATYPES-06-38, DATATYPES-06-42 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-26, DATATYPES-07-30, DATATYPES-07-34, DATATYPES-07-38, DATATYPES-07-42 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-26, DATATYPES-08-30, DATATYPES-08-34, DATATYPES-08-38, DATATYPES-08-42 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-26, DATATYPES-09-30, DATATYPES-09-34, DATATYPES-09-38, DATATYPES-09-42 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-26, DATATYPES-10-30, DATATYPES-10-34, DATATYPES-10-38, DATATYPES-10-42 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-26, DATATYPES-11-30, DATATYPES-11-34, DATATYPES-11-38, DATATYPES-11-42 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-26, DATATYPES-12-30, DATATYPES-12-34, DATATYPES-12-38, DATATYPES-12-42 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-26, DATATYPES-13-30, DATATYPES-13-34, DATATYPES-13-38, DATATYPES-13-42 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-26, DATATYPES-14-30, DATATYPES-14-34, DATATYPES-14-38, DATATYPES-14-42 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-26, DATATYPES-15-30, DATATYPES-15-34, DATATYPES-15-38, DATATYPES-15-42 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-26, DATATYPES-16-30, DATATYPES-16-34, DATATYPES-16-38, DATATYPES-16-42 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-26, DATATYPES-17-30, DATATYPES-17-34, DATATYPES-17-38, DATATYPES-17-42 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-26, DATATYPES-18-30, DATATYPES-18-34, DATATYPES-18-38, DATATYPES-18-42 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-26, DATATYPES-19-30, DATATYPES-19-34, DATATYPES-19-38, DATATYPES-19-42 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-26, DATATYPES-20-30, DATATYPES-20-34, DATATYPES-20-38, DATATYPES-20-42 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-26, DATATYPES-21-30, DATATYPES-21-34, DATATYPES-21-38, DATATYPES-21-42 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-26, DATATYPES-22-30, DATATYPES-22-34, DATATYPES-22-38, DATATYPES-22-42 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-26, DATATYPES-23-30, DATATYPES-23-34, DATATYPES-23-38, DATATYPES-23-42 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-26, DATATYPES-24-30, DATATYPES-24-34, DATATYPES-24-38, DATATYPES-24-42 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-26, DATATYPES-25-30, DATATYPES-25-34, DATATYPES-25-38, DATATYPES-25-42 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-26, DATATYPES-26-30, DATATYPES-26-34, DATATYPES-26-38, DATATYPES-26-42 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-26, DATABASE_SCHEMA_USER-01-30, DATABASE_SCHEMA_USER-01-34, DATABASE_SCHEMA_USER-01-38, DATABASE_SCHEMA_USER-01-42 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-26, DATABASE_SCHEMA_USER-02-30, DATABASE_SCHEMA_USER-02-34, DATABASE_SCHEMA_USER-02-38, DATABASE_SCHEMA_USER-02-42 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-26, DATABASE_SCHEMA_USER-03-30, DATABASE_SCHEMA_USER-03-34, DATABASE_SCHEMA_USER-03-38, DATABASE_SCHEMA_USER-03-42 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-26, INTRODUCTION-01-30, INTRODUCTION-01-34, INTRODUCTION-01-38, INTRODUCTION-01-42 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-26, INTRODUCTION-02-30, INTRODUCTION-02-34, INTRODUCTION-02-38, INTRODUCTION-02-42 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-26, INTRODUCTION-03-30, INTRODUCTION-03-34, INTRODUCTION-03-38, INTRODUCTION-03-42 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-26, INTRODUCTION-04-30, INTRODUCTION-04-34, INTRODUCTION-04-38, INTRODUCTION-04-42 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-26, INTRODUCTION-05-30, INTRODUCTION-05-34, INTRODUCTION-05-38, INTRODUCTION-05-42 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-26, INTRODUCTION-06-30, INTRODUCTION-06-34, INTRODUCTION-06-38, INTRODUCTION-06-42 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-26, INTRODUCTION-07-30, INTRODUCTION-07-34, INTRODUCTION-07-38, INTRODUCTION-07-42 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-26, INTRODUCTION-08-30, INTRODUCTION-08-34, INTRODUCTION-08-38, INTRODUCTION-08-42 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-26, INTRODUCTION-09-30, INTRODUCTION-09-34, INTRODUCTION-09-38, INTRODUCTION-09-42 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-26, INTRODUCTION-10-30, INTRODUCTION-10-34, INTRODUCTION-10-38, INTRODUCTION-10-42 |

## 5. Integrate all nine tables

Complete [REPORTING_ASSIGNMENTS.md](REPORTING_ASSIGNMENTS.md) after joins, aggregates and CTEs. These reports follow the domain workflow and include reconciliations that fail when joins multiply rows.

## 6. Confidence checkpoint and final project

Using a fresh database and this specification, without copying the solution:

1. Draw and explain all nine tables and relationship row counts.
2. Re-create the schema in the order shown in your domain guide, including every PK, FK, UNIQUE, CHECK and default.
3. Load valid sample data; demonstrate rejection of a duplicate PK, duplicate business key, NULL required field, invalid CHECK value and nonexistent parent.
4. Demonstrate that deleting a referenced parent fails; explain a child-first deletion plan. Use a practice database with the supplied sample rows and keep the foreign keys enabled.
5. Perform a correct insert, targeted update and targeted delete, checking the number of changed rows. Ask your instructor to reset the practice tables afterwards.
6. Complete all six domain reports and compare and check their row counts and control totals.
7. Add one new valid business record with related details, rerun the reports and explain exactly which results changed. Ask your instructor to reset the practice tables afterwards.
8. Explain NULL handling, INNER versus LEFT JOIN, WHERE versus HAVING, duplicate multiplication and deterministic ranking.

**Ready to progress:** all integrity tests pass, all six reports compare and check, and you can explain each relationship and fix a deliberately incorrect join without an answer key. If a checkpoint fails, revisit that section instead of advancing by a calendar date.
