# Pharma: connected SQL Server project

Track product batches from suppliers to warehouse stock. Identify unstocked batches and zero-stock locations.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Suppliers ||--o{ Batches : "SupplierID"
    Batches |o--o{ Batches : "ParentBatchID"
    Products ||--o{ Batches : "ProductID"
    Batches ||--o{ Inventory : "BatchID"
    Warehouses ||--o{ Inventory : "WarehouseID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Suppliers → Products → Warehouses → Batches → Inventory**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Suppliers

**Suppliers** — Each supplier can supply multiple batches.

| Column | Type | Requirement |
|---|---|---|
| SupplierID | int | NOT NULL |
| SupplierName | nvarchar(80) | NOT NULL |
| SupplierCode | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **SupplierID**.
Unique business key: **SupplierCode**.
Business rule: `LEN(LTRIM(RTRIM(SupplierName))) > 0`.

### Products

**Products** — A product can be manufactured in many batches.

| Column | Type | Requirement |
|---|---|---|
| ProductID | int | NOT NULL |
| ProductName | nvarchar(80) | NOT NULL |
| ProductCode | varchar(20) | NOT NULL |
| StandardCost | decimal(12,2) | NOT NULL |

Primary key: **ProductID**.
Unique business key: **ProductCode**.
Business rule: `StandardCost >= 0`.
Business rule: `LEN(LTRIM(RTRIM(ProductName))) > 0`.

### Warehouses

**Warehouses** — Locations holding stock from several batches.

| Column | Type | Requirement |
|---|---|---|
| WarehouseID | int | NOT NULL |
| WarehouseName | nvarchar(80) | NOT NULL |
| WarehouseCode | varchar(20) | NOT NULL |
| Capacity | int | NOT NULL |

Primary key: **WarehouseID**.
Unique business key: **WarehouseCode**.
Business rule: `Capacity > 0`.
Business rule: `LEN(LTRIM(RTRIM(WarehouseName))) > 0`.

### Batches

**Batches** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| BatchID | int | NOT NULL |
| SupplierID | int | NOT NULL |
| BatchCode | nvarchar(80) | NOT NULL |
| BatchType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| BatchCost | decimal(12,2) | NULL |
| PackCount | int | NOT NULL |
| ManufactureDate | date | NOT NULL |
| ProducedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentBatchID | int | NULL |
| ProductID | int | NOT NULL |

Primary key: **BatchID**.
Unique business key: **BatchCode**.
Business rule: `BatchType IN ('A','B','C')`.
Business rule: `Status IN ('Open','Closed','Pending')`.
Business rule: `BatchCost >= 0`.
Business rule: `PackCount > 0`.
Business rule: `ParentBatchID IS NULL OR ParentBatchID <> BatchID`.
Business rule: `LEN(LTRIM(RTRIM(BatchCode))) > 0`.
Foreign key: **Batches.SupplierID → Suppliers.SupplierID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Batches.ParentBatchID → Batches.BatchID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Batches.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.

### Inventory

**Inventory** — Bridge between batches and warehouses; one row per batch/location.

| Column | Type | Requirement |
|---|---|---|
| InventoryID | int | NOT NULL |
| BatchID | int | NOT NULL |
| WarehouseID | int | NOT NULL |
| QuantityOnHand | int | NOT NULL |
| LastCountDate | date | NOT NULL |

Primary key: **InventoryID**.
Unique business key: **BatchID, WarehouseID**.
Business rule: `QuantityOnHand >= 0`.
Foreign key: **Inventory.BatchID → Batches.BatchID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Inventory.WarehouseID → Warehouses.WarehouseID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** five tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Suppliers

| SupplierID | SupplierName | SupplierCode | Region |
|---|---|---|---|
| `1` | `Suppliers Alpha` | `SUP-1` | `North` |
| `2` | `Suppliers Beta` | `SUP-2` | `South` |
| `3` | `Suppliers Gamma` | `SUP-3` | `North` |
| `4` | `Suppliers Delta` | `SUP-4` | `West` |
| `5` | `Suppliers Unused` | `SUP-5` | `East` |

### Sample rows: Products

| ProductID | ProductName | ProductCode | StandardCost |
|---|---|---|---|
| `1` | `Compound 1` | `PR-1` | `10` |
| `2` | `Compound 2` | `PR-2` | `20` |
| `3` | `Compound 3` | `PR-3` | `30` |
| `4` | `Compound 4` | `PR-4` | `40` |
| `5` | `Compound 5` | `PR-5` | `50` |

### Sample rows: Warehouses

| WarehouseID | WarehouseName | WarehouseCode | Capacity |
|---|---|---|---|
| `1` | `Warehouse 1` | `WH-1` | `100` |
| `2` | `Warehouse 2` | `WH-2` | `200` |
| `3` | `Warehouse 3` | `WH-3` | `300` |
| `4` | `Warehouse 4` | `WH-4` | `400` |
| `5` | `Warehouse 5` | `WH-5` | `500` |

### Sample rows: Batches

| BatchID | SupplierID | BatchCode | BatchType | Status | BatchCost | PackCount | ManufactureDate | ProducedAt | RecordedAt | Note | BackupNote | ParentBatchID | ProductID |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `1` | `1` | `  Alpha-One  ` | `A` | `Open` | `100` | `1` | `20240101` | `2024-01-01T12:30:45.123` | `2024-01-01T12:30:45.123+00:00` | NULL | `backup` | NULL | `1` |
| `2` | `1` | `beta-Two` | `B` | `Closed` | `200` | `2` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | NULL | `1` | `2` |
| `3` | `2` | `Gamma-Three ` | `C` | `Pending` | `200` | `3` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | `backup` | `1` | `3` |
| `4` | `2` | ` Delta-Four` | `A` | `Open` | NULL | `4` | `20240103` | `2024-01-03T12:30:45.123` | `2024-01-03T12:30:45.123+00:00` | NULL | NULL | `2` | `4` |
| `5` | `3` | `Echo-Five` | `B` | `Closed` | `50` | `1` | `20240201` | `2024-02-01T12:30:45.123` | `2024-02-01T12:30:45.123+00:00` | `confirmed` | `backup` | `2` | `1` |
| `6` | `3` | `ALPHA-Six` | `C` | `Pending` | `300` | `2` | `20240210` | `2024-02-10T12:30:45.123` | `2024-02-10T12:30:45.123+00:00` | `confirmed` | NULL | `3` | `2` |
| `7` | `4` | `Zero-Seven` | `A` | `Open` | `0` | `3` | `20240229` | `2024-02-29T12:30:45.123` | `2024-02-29T12:30:45.123+00:00` | NULL | `backup` | `3` | `3` |
| `8` | `4` | `Review-Eight` | `B` | `Closed` | `150` | `4` | `20240301` | `2024-03-01T12:30:45.123` | `2024-03-01T12:30:45.123+00:00` | `confirmed` | NULL | `4` | `4` |
| `9` | `4` | `Zulu-Nine` | `C` | `Pending` | `300` | `1` | `20240310` | `2024-03-10T12:30:45.123` | `2024-03-10T12:30:45.123+00:00` | `confirmed` | `backup` | `4` | `1` |
| `10` | `4` | `Iota-Ten` | `A` | `Open` | `80` | `2` | `20241103` | `2024-11-03T12:30:45.123` | `2024-11-03T12:30:45.123+00:00` | NULL | NULL | `5` | `2` |
| `11` | `1` | `Kappa-Eleven` | `B` | `Closed` | `120` | `3` | `20241231` | `2024-12-31T12:30:45.123` | `2024-12-31T12:30:45.123+00:00` | `confirmed` | `backup` | `5` | `3` |
| `12` | `2` | `Last-Twelve` | `C` | `Pending` | `200` | `4` | `20250101` | `2025-01-01T12:30:45.123` | `2025-01-01T12:30:45.123+00:00` | `confirmed` | NULL | `6` | `4` |

### Sample rows: Inventory

| InventoryID | BatchID | WarehouseID | QuantityOnHand | LastCountDate |
|---|---|---|---|---|
| `1` | `1` | `1` | `20` | `20240105` |
| `2` | `1` | `2` | `30` | `20240105` |
| `3` | `2` | `1` | `40` | `20240105` |
| `4` | `3` | `3` | `10` | `20240106` |
| `5` | `5` | `4` | `0` | `20240205` |
| `6` | `6` | `2` | `50` | `20240212` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-03, DDL-01-08, DDL-01-13, DDL-01-18, DDL-01-23 |
| [DDL](DDL.md) | Alter | DDL-02-03, DDL-02-08, DDL-02-13, DDL-02-18, DDL-02-23 |
| [DDL](DDL.md) | Drop | DDL-03-03, DDL-03-08, DDL-03-13, DDL-03-18, DDL-03-23 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-03, DATA_SETUP-01-08, DATA_SETUP-01-13, DATA_SETUP-01-18, DATA_SETUP-01-23 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-03, DATA_SETUP-02-08, DATA_SETUP-02-13, DATA_SETUP-02-18, DATA_SETUP-02-23 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-03, CONSTRAINTS-01-08, CONSTRAINTS-01-13, CONSTRAINTS-01-18, CONSTRAINTS-01-23 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-03, CONSTRAINTS-02-08, CONSTRAINTS-02-13, CONSTRAINTS-02-18, CONSTRAINTS-02-23 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-03, CONSTRAINTS-03-08, CONSTRAINTS-03-13, CONSTRAINTS-03-18, CONSTRAINTS-03-23 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-03, CONSTRAINTS-04-08, CONSTRAINTS-04-13, CONSTRAINTS-04-18, CONSTRAINTS-04-23 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-03, CONSTRAINTS-05-08, CONSTRAINTS-05-13, CONSTRAINTS-05-18, CONSTRAINTS-05-23 |
| [DML](DML.md) | Insert | DML-01-03, DML-01-08, DML-01-13, DML-01-18, DML-01-23 |
| [DML](DML.md) | Update | DML-02-03, DML-02-08, DML-02-13, DML-02-18, DML-02-23 |
| [DML](DML.md) | Delete | DML-03-03, DML-03-08, DML-03-13, DML-03-18, DML-03-23 |
| [DQL](DQL.md) | Select | DQL-01-03, DQL-01-08, DQL-01-13, DQL-01-18, DQL-01-23 |
| [DQL](DQL.md) | Where | DQL-02-03, DQL-02-08, DQL-02-13, DQL-02-18, DQL-02-23 |
| [DQL](DQL.md) | Group By | DQL-03-03, DQL-03-08, DQL-03-13, DQL-03-18, DQL-03-23 |
| [DQL](DQL.md) | Having | DQL-04-03, DQL-04-08, DQL-04-13, DQL-04-18, DQL-04-23 |
| [DQL](DQL.md) | Order By | DQL-05-03, DQL-05-08, DQL-05-13, DQL-05-18, DQL-05-23 |
| [DQL](DQL.md) | Top | DQL-06-03, DQL-06-08, DQL-06-13, DQL-06-18, DQL-06-23 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-03, OPERATORS-01-08, OPERATORS-01-13, OPERATORS-01-18, OPERATORS-01-23 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-03, OPERATORS-02-08, OPERATORS-02-13, OPERATORS-02-18, OPERATORS-02-23 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-03, OPERATORS-03-08, OPERATORS-03-13, OPERATORS-03-18, OPERATORS-03-23 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-03, OPERATORS-04-08, OPERATORS-04-13, OPERATORS-04-18, OPERATORS-04-23 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-03, OPERATORS-05-08, OPERATORS-05-13, OPERATORS-05-18, OPERATORS-05-23 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-03, OPERATORS-06-08, OPERATORS-06-13, OPERATORS-06-18, OPERATORS-06-23 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-03, OPERATORS-07-08, OPERATORS-07-13, OPERATORS-07-18, OPERATORS-07-23 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-03, OPERATORS-08-08, OPERATORS-08-13, OPERATORS-08-18, OPERATORS-08-23 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-03, OPERATORS-09-08, OPERATORS-09-13, OPERATORS-09-18, OPERATORS-09-23 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-03, OPERATORS-10-08, OPERATORS-10-13, OPERATORS-10-18, OPERATORS-10-23 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-03, OPERATORS-11-08, OPERATORS-11-13, OPERATORS-11-18, OPERATORS-11-23 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-03, OPERATORS-12-08, OPERATORS-12-13, OPERATORS-12-18, OPERATORS-12-23 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-03, OPERATORS-13-08, OPERATORS-13-13, OPERATORS-13-18, OPERATORS-13-23 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-03, JOINS-01-08, JOINS-01-13, JOINS-01-18, JOINS-01-23 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-03, JOINS-02-08, JOINS-02-13, JOINS-02-18, JOINS-02-23 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-03, JOINS-03-08, JOINS-03-13, JOINS-03-18, JOINS-03-23 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-03, JOINS-04-08, JOINS-04-13, JOINS-04-18, JOINS-04-23 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-03, JOINS-05-08, JOINS-05-13, JOINS-05-18, JOINS-05-23 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-03, SET_OPERATIONS-01-08, SET_OPERATIONS-01-13, SET_OPERATIONS-01-18, SET_OPERATIONS-01-23 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-03, SET_OPERATIONS-02-08, SET_OPERATIONS-02-13, SET_OPERATIONS-02-18, SET_OPERATIONS-02-23 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-03, SET_OPERATIONS-03-08, SET_OPERATIONS-03-13, SET_OPERATIONS-03-18, SET_OPERATIONS-03-23 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-03, SET_OPERATIONS-04-08, SET_OPERATIONS-04-13, SET_OPERATIONS-04-18, SET_OPERATIONS-04-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-03, STRING_FUNCTIONS-01-08, STRING_FUNCTIONS-01-13, STRING_FUNCTIONS-01-18, STRING_FUNCTIONS-01-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-03, STRING_FUNCTIONS-02-08, STRING_FUNCTIONS-02-13, STRING_FUNCTIONS-02-18, STRING_FUNCTIONS-02-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-03, STRING_FUNCTIONS-03-08, STRING_FUNCTIONS-03-13, STRING_FUNCTIONS-03-18, STRING_FUNCTIONS-03-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-03, STRING_FUNCTIONS-04-08, STRING_FUNCTIONS-04-13, STRING_FUNCTIONS-04-18, STRING_FUNCTIONS-04-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-03, STRING_FUNCTIONS-05-08, STRING_FUNCTIONS-05-13, STRING_FUNCTIONS-05-18, STRING_FUNCTIONS-05-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-03, STRING_FUNCTIONS-06-08, STRING_FUNCTIONS-06-13, STRING_FUNCTIONS-06-18, STRING_FUNCTIONS-06-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-03, STRING_FUNCTIONS-07-08, STRING_FUNCTIONS-07-13, STRING_FUNCTIONS-07-18, STRING_FUNCTIONS-07-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-03, STRING_FUNCTIONS-08-08, STRING_FUNCTIONS-08-13, STRING_FUNCTIONS-08-18, STRING_FUNCTIONS-08-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-03, STRING_FUNCTIONS-09-08, STRING_FUNCTIONS-09-13, STRING_FUNCTIONS-09-18, STRING_FUNCTIONS-09-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-03, STRING_FUNCTIONS-10-08, STRING_FUNCTIONS-10-13, STRING_FUNCTIONS-10-18, STRING_FUNCTIONS-10-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-03, STRING_FUNCTIONS-11-08, STRING_FUNCTIONS-11-13, STRING_FUNCTIONS-11-18, STRING_FUNCTIONS-11-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-03, STRING_FUNCTIONS-12-08, STRING_FUNCTIONS-12-13, STRING_FUNCTIONS-12-18, STRING_FUNCTIONS-12-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-03, STRING_FUNCTIONS-13-08, STRING_FUNCTIONS-13-13, STRING_FUNCTIONS-13-18, STRING_FUNCTIONS-13-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-03, STRING_FUNCTIONS-14-08, STRING_FUNCTIONS-14-13, STRING_FUNCTIONS-14-18, STRING_FUNCTIONS-14-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-03, STRING_FUNCTIONS-15-08, STRING_FUNCTIONS-15-13, STRING_FUNCTIONS-15-18, STRING_FUNCTIONS-15-23 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-03, STRING_FUNCTIONS-16-08, STRING_FUNCTIONS-16-13, STRING_FUNCTIONS-16-18, STRING_FUNCTIONS-16-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-03, DATE_FUNCTIONS-01-08, DATE_FUNCTIONS-01-13, DATE_FUNCTIONS-01-18, DATE_FUNCTIONS-01-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-03, DATE_FUNCTIONS-02-08, DATE_FUNCTIONS-02-13, DATE_FUNCTIONS-02-18, DATE_FUNCTIONS-02-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-03, DATE_FUNCTIONS-03-08, DATE_FUNCTIONS-03-13, DATE_FUNCTIONS-03-18, DATE_FUNCTIONS-03-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-03, DATE_FUNCTIONS-04-08, DATE_FUNCTIONS-04-13, DATE_FUNCTIONS-04-18, DATE_FUNCTIONS-04-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-03, DATE_FUNCTIONS-05-08, DATE_FUNCTIONS-05-13, DATE_FUNCTIONS-05-18, DATE_FUNCTIONS-05-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-03, DATE_FUNCTIONS-06-08, DATE_FUNCTIONS-06-13, DATE_FUNCTIONS-06-18, DATE_FUNCTIONS-06-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-03, DATE_FUNCTIONS-07-08, DATE_FUNCTIONS-07-13, DATE_FUNCTIONS-07-18, DATE_FUNCTIONS-07-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-03, DATE_FUNCTIONS-08-08, DATE_FUNCTIONS-08-13, DATE_FUNCTIONS-08-18, DATE_FUNCTIONS-08-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-03, DATE_FUNCTIONS-09-08, DATE_FUNCTIONS-09-13, DATE_FUNCTIONS-09-18, DATE_FUNCTIONS-09-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-03, DATE_FUNCTIONS-10-08, DATE_FUNCTIONS-10-13, DATE_FUNCTIONS-10-18, DATE_FUNCTIONS-10-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-03, DATE_FUNCTIONS-11-08, DATE_FUNCTIONS-11-13, DATE_FUNCTIONS-11-18, DATE_FUNCTIONS-11-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-03, DATE_FUNCTIONS-12-08, DATE_FUNCTIONS-12-13, DATE_FUNCTIONS-12-18, DATE_FUNCTIONS-12-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-03, DATE_FUNCTIONS-13-08, DATE_FUNCTIONS-13-13, DATE_FUNCTIONS-13-18, DATE_FUNCTIONS-13-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-03, DATE_FUNCTIONS-14-08, DATE_FUNCTIONS-14-13, DATE_FUNCTIONS-14-18, DATE_FUNCTIONS-14-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-03, DATE_FUNCTIONS-15-08, DATE_FUNCTIONS-15-13, DATE_FUNCTIONS-15-18, DATE_FUNCTIONS-15-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-03, DATE_FUNCTIONS-16-08, DATE_FUNCTIONS-16-13, DATE_FUNCTIONS-16-18, DATE_FUNCTIONS-16-23 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-03, DATE_FUNCTIONS-17-08, DATE_FUNCTIONS-17-13, DATE_FUNCTIONS-17-18, DATE_FUNCTIONS-17-23 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-03, AGGREGATES-01-08, AGGREGATES-01-13, AGGREGATES-01-18, AGGREGATES-01-23 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-03, AGGREGATES-02-08, AGGREGATES-02-13, AGGREGATES-02-18, AGGREGATES-02-23 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-03, AGGREGATES-03-08, AGGREGATES-03-13, AGGREGATES-03-18, AGGREGATES-03-23 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-03, AGGREGATES-04-08, AGGREGATES-04-13, AGGREGATES-04-18, AGGREGATES-04-23 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-03, AGGREGATES-05-08, AGGREGATES-05-13, AGGREGATES-05-18, AGGREGATES-05-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-03, ANALYTICAL_FUNCTIONS-01-08, ANALYTICAL_FUNCTIONS-01-13, ANALYTICAL_FUNCTIONS-01-18, ANALYTICAL_FUNCTIONS-01-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-03, ANALYTICAL_FUNCTIONS-02-08, ANALYTICAL_FUNCTIONS-02-13, ANALYTICAL_FUNCTIONS-02-18, ANALYTICAL_FUNCTIONS-02-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-03, ANALYTICAL_FUNCTIONS-03-08, ANALYTICAL_FUNCTIONS-03-13, ANALYTICAL_FUNCTIONS-03-18, ANALYTICAL_FUNCTIONS-03-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-03, ANALYTICAL_FUNCTIONS-04-08, ANALYTICAL_FUNCTIONS-04-13, ANALYTICAL_FUNCTIONS-04-18, ANALYTICAL_FUNCTIONS-04-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-03, ANALYTICAL_FUNCTIONS-05-08, ANALYTICAL_FUNCTIONS-05-13, ANALYTICAL_FUNCTIONS-05-18, ANALYTICAL_FUNCTIONS-05-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-03, ANALYTICAL_FUNCTIONS-06-08, ANALYTICAL_FUNCTIONS-06-13, ANALYTICAL_FUNCTIONS-06-18, ANALYTICAL_FUNCTIONS-06-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-03, ANALYTICAL_FUNCTIONS-07-08, ANALYTICAL_FUNCTIONS-07-13, ANALYTICAL_FUNCTIONS-07-18, ANALYTICAL_FUNCTIONS-07-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-03, ANALYTICAL_FUNCTIONS-08-08, ANALYTICAL_FUNCTIONS-08-13, ANALYTICAL_FUNCTIONS-08-18, ANALYTICAL_FUNCTIONS-08-23 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-03, ANALYTICAL_FUNCTIONS-09-08, ANALYTICAL_FUNCTIONS-09-13, ANALYTICAL_FUNCTIONS-09-18, ANALYTICAL_FUNCTIONS-09-23 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-03, CTE-01-08, CTE-01-13, CTE-01-18, CTE-01-23 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-03, CTE-02-08, CTE-02-13, CTE-02-18, CTE-02-23 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-03, CTE-03-08, CTE-03-13, CTE-03-18, CTE-03-23 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-03, CTE-04-08, CTE-04-13, CTE-04-18, CTE-04-23 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-03, CTE-05-08, CTE-05-13, CTE-05-18, CTE-05-23 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-03, DATATYPES-01-08, DATATYPES-01-13, DATATYPES-01-18, DATATYPES-01-23 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-03, DATATYPES-02-08, DATATYPES-02-13, DATATYPES-02-18, DATATYPES-02-23 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-03, DATATYPES-03-08, DATATYPES-03-13, DATATYPES-03-18, DATATYPES-03-23 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-03, DATATYPES-04-08, DATATYPES-04-13, DATATYPES-04-18, DATATYPES-04-23 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-03, DATATYPES-05-08, DATATYPES-05-13, DATATYPES-05-18, DATATYPES-05-23 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-03, DATATYPES-06-08, DATATYPES-06-13, DATATYPES-06-18, DATATYPES-06-23 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-03, DATATYPES-07-08, DATATYPES-07-13, DATATYPES-07-18, DATATYPES-07-23 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-03, DATATYPES-08-08, DATATYPES-08-13, DATATYPES-08-18, DATATYPES-08-23 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-03, DATATYPES-09-08, DATATYPES-09-13, DATATYPES-09-18, DATATYPES-09-23 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-03, DATATYPES-10-08, DATATYPES-10-13, DATATYPES-10-18, DATATYPES-10-23 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-03, DATATYPES-11-08, DATATYPES-11-13, DATATYPES-11-18, DATATYPES-11-23 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-03, DATATYPES-12-08, DATATYPES-12-13, DATATYPES-12-18, DATATYPES-12-23 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-03, DATATYPES-13-08, DATATYPES-13-13, DATATYPES-13-18, DATATYPES-13-23 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-03, DATATYPES-14-08, DATATYPES-14-13, DATATYPES-14-18, DATATYPES-14-23 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-03, DATATYPES-15-08, DATATYPES-15-13, DATATYPES-15-18, DATATYPES-15-23 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-03, DATATYPES-16-08, DATATYPES-16-13, DATATYPES-16-18, DATATYPES-16-23 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-03, DATATYPES-17-08, DATATYPES-17-13, DATATYPES-17-18, DATATYPES-17-23 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-03, DATATYPES-18-08, DATATYPES-18-13, DATATYPES-18-18, DATATYPES-18-23 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-03, DATATYPES-19-08, DATATYPES-19-13, DATATYPES-19-18, DATATYPES-19-23 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-03, DATATYPES-20-08, DATATYPES-20-13, DATATYPES-20-18, DATATYPES-20-23 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-03, DATATYPES-21-08, DATATYPES-21-13, DATATYPES-21-18, DATATYPES-21-23 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-03, DATATYPES-22-08, DATATYPES-22-13, DATATYPES-22-18, DATATYPES-22-23 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-03, DATATYPES-23-08, DATATYPES-23-13, DATATYPES-23-18, DATATYPES-23-23 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-03, DATATYPES-24-08, DATATYPES-24-13, DATATYPES-24-18, DATATYPES-24-23 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-03, DATATYPES-25-08, DATATYPES-25-13, DATATYPES-25-18, DATATYPES-25-23 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-03, DATATYPES-26-08, DATATYPES-26-13, DATATYPES-26-18, DATATYPES-26-23 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-03, DATABASE_SCHEMA_USER-01-08, DATABASE_SCHEMA_USER-01-13, DATABASE_SCHEMA_USER-01-18, DATABASE_SCHEMA_USER-01-23 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-03, DATABASE_SCHEMA_USER-02-08, DATABASE_SCHEMA_USER-02-13, DATABASE_SCHEMA_USER-02-18, DATABASE_SCHEMA_USER-02-23 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-03, DATABASE_SCHEMA_USER-03-08, DATABASE_SCHEMA_USER-03-13, DATABASE_SCHEMA_USER-03-18, DATABASE_SCHEMA_USER-03-23 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-03, INTRODUCTION-01-08, INTRODUCTION-01-13, INTRODUCTION-01-18, INTRODUCTION-01-23 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-03, INTRODUCTION-02-08, INTRODUCTION-02-13, INTRODUCTION-02-18, INTRODUCTION-02-23 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-03, INTRODUCTION-03-08, INTRODUCTION-03-13, INTRODUCTION-03-18, INTRODUCTION-03-23 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-03, INTRODUCTION-04-08, INTRODUCTION-04-13, INTRODUCTION-04-18, INTRODUCTION-04-23 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-03, INTRODUCTION-05-08, INTRODUCTION-05-13, INTRODUCTION-05-18, INTRODUCTION-05-23 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-03, INTRODUCTION-06-08, INTRODUCTION-06-13, INTRODUCTION-06-18, INTRODUCTION-06-23 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-03, INTRODUCTION-07-08, INTRODUCTION-07-13, INTRODUCTION-07-18, INTRODUCTION-07-23 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-03, INTRODUCTION-08-08, INTRODUCTION-08-13, INTRODUCTION-08-18, INTRODUCTION-08-23 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-03, INTRODUCTION-09-08, INTRODUCTION-09-13, INTRODUCTION-09-18, INTRODUCTION-09-23 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-03, INTRODUCTION-10-08, INTRODUCTION-10-13, INTRODUCTION-10-18, INTRODUCTION-10-23 |

## 5. Integrate all five tables

Complete [REPORTING_ASSIGNMENTS.md](REPORTING_ASSIGNMENTS.md) after joins, aggregates and CTEs. These reports follow the domain workflow and include reconciliations that fail when joins multiply rows.

## 6. Confidence checkpoint and final project

Using a fresh database and this specification, without copying the solution:

1. Draw and explain all five tables and relationship row counts.
2. Re-create the schema in the order shown in your domain guide, including every PK, FK, UNIQUE, CHECK and default.
3. Load valid sample data; demonstrate rejection of a duplicate PK, duplicate business key, NULL required field, invalid CHECK value and nonexistent parent.
4. Demonstrate that deleting a referenced parent fails; explain a child-first deletion plan. Use a practice database with the supplied sample rows and keep the foreign keys enabled.
5. Perform a correct insert, targeted update and targeted delete, checking the number of changed rows. Ask your instructor to reset the practice tables afterwards.
6. Complete all six domain reports and compare and check their row counts and control totals.
7. Add one new valid business record with related details, rerun the reports and explain exactly which results changed. Ask your instructor to reset the practice tables afterwards.
8. Explain NULL handling, INNER versus LEFT JOIN, WHERE versus HAVING, duplicate multiplication and deterministic ranking.

**Ready to progress:** all integrity tests pass, all six reports compare and check, and you can explain each relationship and fix a deliberately incorrect join without an answer key. If a checkpoint fails, revisit that section instead of advancing by a calendar date.
