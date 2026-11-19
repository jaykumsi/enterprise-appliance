# Retail: connected SQL Server project

Track customers, products, orders, line items and payments. Reconcile line totals and payments without double-counting.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Customers ||--o{ Orders : "CustomerID"
    Orders |o--o{ Orders : "ParentOrderID"
    Orders ||--o{ OrderItems : "OrderID"
    Products ||--o{ OrderItems : "ProductID"
    Orders ||--o{ Payments : "OrderID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Customers → Products → Orders → OrderItems → Payments**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Customers

**Customers** — One customer can place many orders.

| Column | Type | Requirement |
|---|---|---|
| CustomerID | int | NOT NULL |
| CustomerName | nvarchar(80) | NOT NULL |
| CustomerCode | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **CustomerID**.
Unique business key: **CustomerCode**.
Business rule: `LEN(LTRIM(RTRIM(CustomerName))) > 0`.

### Products

**Products** — Product catalog and current selling price; order lines retain their historical price.

| Column | Type | Requirement |
|---|---|---|
| ProductID | int | NOT NULL |
| ProductName | nvarchar(80) | NOT NULL |
| SKU | varchar(20) | NOT NULL |
| UnitPrice | decimal(12,2) | NOT NULL |
| StockQuantity | int | NOT NULL |

Primary key: **ProductID**.
Unique business key: **SKU**.
Business rule: `UnitPrice >= 0`.
Business rule: `StockQuantity >= 0`.
Business rule: `LEN(LTRIM(RTRIM(ProductName))) > 0`.

### Orders

**Orders** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| OrderID | int | NOT NULL |
| CustomerID | int | NOT NULL |
| OrderReference | nvarchar(80) | NOT NULL |
| SalesChannel | varchar(10) | NOT NULL |
| OrderStatus | varchar(10) | NOT NULL DEFAULT ('Open') |
| OrderTotal | decimal(12,2) | NULL |
| PackageCount | int | NOT NULL |
| OrderDate | date | NOT NULL |
| PlacedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentOrderID | int | NULL |

Primary key: **OrderID**.
Unique business key: **OrderReference**.
Business rule: `SalesChannel IN ('A','B','C')`.
Business rule: `OrderStatus IN ('Open','Closed','Pending')`.
Business rule: `OrderTotal >= 0`.
Business rule: `PackageCount > 0`.
Business rule: `ParentOrderID IS NULL OR ParentOrderID <> OrderID`.
Business rule: `LEN(LTRIM(RTRIM(OrderReference))) > 0`.
Foreign key: **Orders.CustomerID → Customers.CustomerID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Orders.ParentOrderID → Orders.OrderID**. Use NO ACTION on delete/update; do not disable checking.

### OrderItems

**OrderItems** — Bridge between orders and products; an order can have multiple lines.

| Column | Type | Requirement |
|---|---|---|
| OrderItemID | int | NOT NULL |
| OrderID | int | NOT NULL |
| ProductID | int | NOT NULL |
| Quantity | int | NOT NULL |
| UnitPrice | decimal(12,2) | NOT NULL |

Primary key: **OrderItemID**.
Unique business key: **OrderID, ProductID**.
Business rule: `Quantity > 0`.
Business rule: `UnitPrice >= 0`.
Foreign key: **OrderItems.OrderID → Orders.OrderID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **OrderItems.ProductID → Products.ProductID**. Use NO ACTION on delete/update; do not disable checking.

### Payments

**Payments** — One order can have several payments, or none.

| Column | Type | Requirement |
|---|---|---|
| PaymentID | int | NOT NULL |
| OrderID | int | NOT NULL |
| PaymentReference | varchar(20) | NOT NULL |
| PaidAmount | decimal(12,2) | NOT NULL |
| PaymentDate | date | NOT NULL |

Primary key: **PaymentID**.
Unique business key: **PaymentReference**.
Business rule: `PaidAmount > 0`.
Business rule: `LEN(LTRIM(RTRIM(PaymentReference))) > 0`.
Foreign key: **Payments.OrderID → Orders.OrderID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** five tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Customers

| CustomerID | CustomerName | CustomerCode | Region |
|---|---|---|---|
| `1` | `Customers Alpha` | `CUS-1` | `North` |
| `2` | `Customers Beta` | `CUS-2` | `South` |
| `3` | `Customers Gamma` | `CUS-3` | `North` |
| `4` | `Customers Delta` | `CUS-4` | `West` |
| `5` | `Customers Unused` | `CUS-5` | `East` |

### Sample rows: Products

| ProductID | ProductName | SKU | UnitPrice | StockQuantity |
|---|---|---|---|---|
| `1` | `Notebook` | `SKU-1` | `25` | `20` |
| `2` | `Pen set` | `SKU-2` | `10` | `30` |
| `3` | `Backpack` | `SKU-3` | `50` | `10` |
| `4` | `Desk lamp` | `SKU-4` | `40` | `5` |
| `5` | `Unused product` | `SKU-5` | `15` | `0` |

### Sample rows: Orders

| OrderID | CustomerID | OrderReference | SalesChannel | OrderStatus | OrderTotal | PackageCount | OrderDate | PlacedAt | RecordedAt | Note | BackupNote | ParentOrderID |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `1` | `1` | `  Alpha-One  ` | `A` | `Open` | `100` | `1` | `20240101` | `2024-01-01T12:30:45.123` | `2024-01-01T12:30:45.123+00:00` | NULL | `backup` | NULL |
| `2` | `1` | `beta-Two` | `B` | `Closed` | `200` | `2` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | NULL | `1` |
| `3` | `2` | `Gamma-Three ` | `C` | `Pending` | `200` | `3` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | `backup` | `1` |
| `4` | `2` | ` Delta-Four` | `A` | `Open` | NULL | `4` | `20240103` | `2024-01-03T12:30:45.123` | `2024-01-03T12:30:45.123+00:00` | NULL | NULL | `2` |
| `5` | `3` | `Echo-Five` | `B` | `Closed` | `50` | `1` | `20240201` | `2024-02-01T12:30:45.123` | `2024-02-01T12:30:45.123+00:00` | `confirmed` | `backup` | `2` |
| `6` | `3` | `ALPHA-Six` | `C` | `Pending` | `300` | `2` | `20240210` | `2024-02-10T12:30:45.123` | `2024-02-10T12:30:45.123+00:00` | `confirmed` | NULL | `3` |
| `7` | `4` | `Zero-Seven` | `A` | `Open` | `0` | `3` | `20240229` | `2024-02-29T12:30:45.123` | `2024-02-29T12:30:45.123+00:00` | NULL | `backup` | `3` |
| `8` | `4` | `Review-Eight` | `B` | `Closed` | `150` | `4` | `20240301` | `2024-03-01T12:30:45.123` | `2024-03-01T12:30:45.123+00:00` | `confirmed` | NULL | `4` |
| `9` | `4` | `Zulu-Nine` | `C` | `Pending` | `300` | `1` | `20240310` | `2024-03-10T12:30:45.123` | `2024-03-10T12:30:45.123+00:00` | `confirmed` | `backup` | `4` |
| `10` | `4` | `Iota-Ten` | `A` | `Open` | `80` | `2` | `20241103` | `2024-11-03T12:30:45.123` | `2024-11-03T12:30:45.123+00:00` | NULL | NULL | `5` |
| `11` | `1` | `Kappa-Eleven` | `B` | `Closed` | `120` | `3` | `20241231` | `2024-12-31T12:30:45.123` | `2024-12-31T12:30:45.123+00:00` | `confirmed` | `backup` | `5` |
| `12` | `2` | `Last-Twelve` | `C` | `Pending` | `200` | `4` | `20250101` | `2025-01-01T12:30:45.123` | `2025-01-01T12:30:45.123+00:00` | `confirmed` | NULL | `6` |

### Sample rows: OrderItems

| OrderItemID | OrderID | ProductID | Quantity | UnitPrice |
|---|---|---|---|---|
| `1` | `1` | `1` | `2` | `25` |
| `2` | `1` | `2` | `5` | `10` |
| `3` | `2` | `3` | `4` | `50` |
| `4` | `3` | `3` | `4` | `50` |
| `5` | `5` | `1` | `2` | `25` |
| `6` | `6` | `3` | `6` | `50` |

### Sample rows: Payments

| PaymentID | OrderID | PaymentReference | PaidAmount | PaymentDate |
|---|---|---|---|---|
| `1` | `1` | `PAY-1` | `60` | `20240102` |
| `2` | `1` | `PAY-2` | `40` | `20240103` |
| `3` | `2` | `PAY-3` | `200` | `20240103` |
| `4` | `3` | `PAY-4` | `100` | `20240104` |
| `5` | `6` | `PAY-5` | `300` | `20240211` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../SQL/Excerises/BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-01, DDL-01-06, DDL-01-11, DDL-01-16, DDL-01-21 |
| [DDL](DDL.md) | Alter | DDL-02-01, DDL-02-06, DDL-02-11, DDL-02-16, DDL-02-21 |
| [DDL](DDL.md) | Drop | DDL-03-01, DDL-03-06, DDL-03-11, DDL-03-16, DDL-03-21 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-01, DATA_SETUP-01-06, DATA_SETUP-01-11, DATA_SETUP-01-16, DATA_SETUP-01-21 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-01, DATA_SETUP-02-06, DATA_SETUP-02-11, DATA_SETUP-02-16, DATA_SETUP-02-21 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-01, CONSTRAINTS-01-06, CONSTRAINTS-01-11, CONSTRAINTS-01-16, CONSTRAINTS-01-21 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-01, CONSTRAINTS-02-06, CONSTRAINTS-02-11, CONSTRAINTS-02-16, CONSTRAINTS-02-21 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-01, CONSTRAINTS-03-06, CONSTRAINTS-03-11, CONSTRAINTS-03-16, CONSTRAINTS-03-21 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-01, CONSTRAINTS-04-06, CONSTRAINTS-04-11, CONSTRAINTS-04-16, CONSTRAINTS-04-21 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-01, CONSTRAINTS-05-06, CONSTRAINTS-05-11, CONSTRAINTS-05-16, CONSTRAINTS-05-21 |
| [DML](DML.md) | Insert | DML-01-01, DML-01-06, DML-01-11, DML-01-16, DML-01-21 |
| [DML](DML.md) | Update | DML-02-01, DML-02-06, DML-02-11, DML-02-16, DML-02-21 |
| [DML](DML.md) | Delete | DML-03-01, DML-03-06, DML-03-11, DML-03-16, DML-03-21 |
| [DQL](DQL.md) | Select | DQL-01-01, DQL-01-06, DQL-01-11, DQL-01-16, DQL-01-21 |
| [DQL](DQL.md) | Where | DQL-02-01, DQL-02-06, DQL-02-11, DQL-02-16, DQL-02-21 |
| [DQL](DQL.md) | Group By | DQL-03-01, DQL-03-06, DQL-03-11, DQL-03-16, DQL-03-21 |
| [DQL](DQL.md) | Having | DQL-04-01, DQL-04-06, DQL-04-11, DQL-04-16, DQL-04-21 |
| [DQL](DQL.md) | Order By | DQL-05-01, DQL-05-06, DQL-05-11, DQL-05-16, DQL-05-21 |
| [DQL](DQL.md) | Top | DQL-06-01, DQL-06-06, DQL-06-11, DQL-06-16, DQL-06-21 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-01, OPERATORS-01-06, OPERATORS-01-11, OPERATORS-01-16, OPERATORS-01-21 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-01, OPERATORS-02-06, OPERATORS-02-11, OPERATORS-02-16, OPERATORS-02-21 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-01, OPERATORS-03-06, OPERATORS-03-11, OPERATORS-03-16, OPERATORS-03-21 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-01, OPERATORS-04-06, OPERATORS-04-11, OPERATORS-04-16, OPERATORS-04-21 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-01, OPERATORS-05-06, OPERATORS-05-11, OPERATORS-05-16, OPERATORS-05-21 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-01, OPERATORS-06-06, OPERATORS-06-11, OPERATORS-06-16, OPERATORS-06-21 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-01, OPERATORS-07-06, OPERATORS-07-11, OPERATORS-07-16, OPERATORS-07-21 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-01, OPERATORS-08-06, OPERATORS-08-11, OPERATORS-08-16, OPERATORS-08-21 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-01, OPERATORS-09-06, OPERATORS-09-11, OPERATORS-09-16, OPERATORS-09-21 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-01, OPERATORS-10-06, OPERATORS-10-11, OPERATORS-10-16, OPERATORS-10-21 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-01, OPERATORS-11-06, OPERATORS-11-11, OPERATORS-11-16, OPERATORS-11-21 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-01, OPERATORS-12-06, OPERATORS-12-11, OPERATORS-12-16, OPERATORS-12-21 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-01, OPERATORS-13-06, OPERATORS-13-11, OPERATORS-13-16, OPERATORS-13-21 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-01, JOINS-01-06, JOINS-01-11, JOINS-01-16, JOINS-01-21 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-01, JOINS-02-06, JOINS-02-11, JOINS-02-16, JOINS-02-21 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-01, JOINS-03-06, JOINS-03-11, JOINS-03-16, JOINS-03-21 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-01, JOINS-04-06, JOINS-04-11, JOINS-04-16, JOINS-04-21 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-01, JOINS-05-06, JOINS-05-11, JOINS-05-16, JOINS-05-21 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-01, SET_OPERATIONS-01-06, SET_OPERATIONS-01-11, SET_OPERATIONS-01-16, SET_OPERATIONS-01-21 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-01, SET_OPERATIONS-02-06, SET_OPERATIONS-02-11, SET_OPERATIONS-02-16, SET_OPERATIONS-02-21 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-01, SET_OPERATIONS-03-06, SET_OPERATIONS-03-11, SET_OPERATIONS-03-16, SET_OPERATIONS-03-21 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-01, SET_OPERATIONS-04-06, SET_OPERATIONS-04-11, SET_OPERATIONS-04-16, SET_OPERATIONS-04-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-01, STRING_FUNCTIONS-01-06, STRING_FUNCTIONS-01-11, STRING_FUNCTIONS-01-16, STRING_FUNCTIONS-01-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-01, STRING_FUNCTIONS-02-06, STRING_FUNCTIONS-02-11, STRING_FUNCTIONS-02-16, STRING_FUNCTIONS-02-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-01, STRING_FUNCTIONS-03-06, STRING_FUNCTIONS-03-11, STRING_FUNCTIONS-03-16, STRING_FUNCTIONS-03-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-01, STRING_FUNCTIONS-04-06, STRING_FUNCTIONS-04-11, STRING_FUNCTIONS-04-16, STRING_FUNCTIONS-04-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-01, STRING_FUNCTIONS-05-06, STRING_FUNCTIONS-05-11, STRING_FUNCTIONS-05-16, STRING_FUNCTIONS-05-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-01, STRING_FUNCTIONS-06-06, STRING_FUNCTIONS-06-11, STRING_FUNCTIONS-06-16, STRING_FUNCTIONS-06-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-01, STRING_FUNCTIONS-07-06, STRING_FUNCTIONS-07-11, STRING_FUNCTIONS-07-16, STRING_FUNCTIONS-07-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-01, STRING_FUNCTIONS-08-06, STRING_FUNCTIONS-08-11, STRING_FUNCTIONS-08-16, STRING_FUNCTIONS-08-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-01, STRING_FUNCTIONS-09-06, STRING_FUNCTIONS-09-11, STRING_FUNCTIONS-09-16, STRING_FUNCTIONS-09-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-01, STRING_FUNCTIONS-10-06, STRING_FUNCTIONS-10-11, STRING_FUNCTIONS-10-16, STRING_FUNCTIONS-10-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-01, STRING_FUNCTIONS-11-06, STRING_FUNCTIONS-11-11, STRING_FUNCTIONS-11-16, STRING_FUNCTIONS-11-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-01, STRING_FUNCTIONS-12-06, STRING_FUNCTIONS-12-11, STRING_FUNCTIONS-12-16, STRING_FUNCTIONS-12-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-01, STRING_FUNCTIONS-13-06, STRING_FUNCTIONS-13-11, STRING_FUNCTIONS-13-16, STRING_FUNCTIONS-13-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-01, STRING_FUNCTIONS-14-06, STRING_FUNCTIONS-14-11, STRING_FUNCTIONS-14-16, STRING_FUNCTIONS-14-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-01, STRING_FUNCTIONS-15-06, STRING_FUNCTIONS-15-11, STRING_FUNCTIONS-15-16, STRING_FUNCTIONS-15-21 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-01, STRING_FUNCTIONS-16-06, STRING_FUNCTIONS-16-11, STRING_FUNCTIONS-16-16, STRING_FUNCTIONS-16-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-01, DATE_FUNCTIONS-01-06, DATE_FUNCTIONS-01-11, DATE_FUNCTIONS-01-16, DATE_FUNCTIONS-01-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-01, DATE_FUNCTIONS-02-06, DATE_FUNCTIONS-02-11, DATE_FUNCTIONS-02-16, DATE_FUNCTIONS-02-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-01, DATE_FUNCTIONS-03-06, DATE_FUNCTIONS-03-11, DATE_FUNCTIONS-03-16, DATE_FUNCTIONS-03-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-01, DATE_FUNCTIONS-04-06, DATE_FUNCTIONS-04-11, DATE_FUNCTIONS-04-16, DATE_FUNCTIONS-04-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-01, DATE_FUNCTIONS-05-06, DATE_FUNCTIONS-05-11, DATE_FUNCTIONS-05-16, DATE_FUNCTIONS-05-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-01, DATE_FUNCTIONS-06-06, DATE_FUNCTIONS-06-11, DATE_FUNCTIONS-06-16, DATE_FUNCTIONS-06-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-01, DATE_FUNCTIONS-07-06, DATE_FUNCTIONS-07-11, DATE_FUNCTIONS-07-16, DATE_FUNCTIONS-07-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-01, DATE_FUNCTIONS-08-06, DATE_FUNCTIONS-08-11, DATE_FUNCTIONS-08-16, DATE_FUNCTIONS-08-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-01, DATE_FUNCTIONS-09-06, DATE_FUNCTIONS-09-11, DATE_FUNCTIONS-09-16, DATE_FUNCTIONS-09-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-01, DATE_FUNCTIONS-10-06, DATE_FUNCTIONS-10-11, DATE_FUNCTIONS-10-16, DATE_FUNCTIONS-10-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-01, DATE_FUNCTIONS-11-06, DATE_FUNCTIONS-11-11, DATE_FUNCTIONS-11-16, DATE_FUNCTIONS-11-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-01, DATE_FUNCTIONS-12-06, DATE_FUNCTIONS-12-11, DATE_FUNCTIONS-12-16, DATE_FUNCTIONS-12-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-01, DATE_FUNCTIONS-13-06, DATE_FUNCTIONS-13-11, DATE_FUNCTIONS-13-16, DATE_FUNCTIONS-13-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-01, DATE_FUNCTIONS-14-06, DATE_FUNCTIONS-14-11, DATE_FUNCTIONS-14-16, DATE_FUNCTIONS-14-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-01, DATE_FUNCTIONS-15-06, DATE_FUNCTIONS-15-11, DATE_FUNCTIONS-15-16, DATE_FUNCTIONS-15-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-01, DATE_FUNCTIONS-16-06, DATE_FUNCTIONS-16-11, DATE_FUNCTIONS-16-16, DATE_FUNCTIONS-16-21 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-01, DATE_FUNCTIONS-17-06, DATE_FUNCTIONS-17-11, DATE_FUNCTIONS-17-16, DATE_FUNCTIONS-17-21 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-01, AGGREGATES-01-06, AGGREGATES-01-11, AGGREGATES-01-16, AGGREGATES-01-21 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-01, AGGREGATES-02-06, AGGREGATES-02-11, AGGREGATES-02-16, AGGREGATES-02-21 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-01, AGGREGATES-03-06, AGGREGATES-03-11, AGGREGATES-03-16, AGGREGATES-03-21 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-01, AGGREGATES-04-06, AGGREGATES-04-11, AGGREGATES-04-16, AGGREGATES-04-21 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-01, AGGREGATES-05-06, AGGREGATES-05-11, AGGREGATES-05-16, AGGREGATES-05-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-01, ANALYTICAL_FUNCTIONS-01-06, ANALYTICAL_FUNCTIONS-01-11, ANALYTICAL_FUNCTIONS-01-16, ANALYTICAL_FUNCTIONS-01-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-01, ANALYTICAL_FUNCTIONS-02-06, ANALYTICAL_FUNCTIONS-02-11, ANALYTICAL_FUNCTIONS-02-16, ANALYTICAL_FUNCTIONS-02-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-01, ANALYTICAL_FUNCTIONS-03-06, ANALYTICAL_FUNCTIONS-03-11, ANALYTICAL_FUNCTIONS-03-16, ANALYTICAL_FUNCTIONS-03-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-01, ANALYTICAL_FUNCTIONS-04-06, ANALYTICAL_FUNCTIONS-04-11, ANALYTICAL_FUNCTIONS-04-16, ANALYTICAL_FUNCTIONS-04-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-01, ANALYTICAL_FUNCTIONS-05-06, ANALYTICAL_FUNCTIONS-05-11, ANALYTICAL_FUNCTIONS-05-16, ANALYTICAL_FUNCTIONS-05-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-01, ANALYTICAL_FUNCTIONS-06-06, ANALYTICAL_FUNCTIONS-06-11, ANALYTICAL_FUNCTIONS-06-16, ANALYTICAL_FUNCTIONS-06-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-01, ANALYTICAL_FUNCTIONS-07-06, ANALYTICAL_FUNCTIONS-07-11, ANALYTICAL_FUNCTIONS-07-16, ANALYTICAL_FUNCTIONS-07-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-01, ANALYTICAL_FUNCTIONS-08-06, ANALYTICAL_FUNCTIONS-08-11, ANALYTICAL_FUNCTIONS-08-16, ANALYTICAL_FUNCTIONS-08-21 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-01, ANALYTICAL_FUNCTIONS-09-06, ANALYTICAL_FUNCTIONS-09-11, ANALYTICAL_FUNCTIONS-09-16, ANALYTICAL_FUNCTIONS-09-21 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-01, CTE-01-06, CTE-01-11, CTE-01-16, CTE-01-21 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-01, CTE-02-06, CTE-02-11, CTE-02-16, CTE-02-21 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-01, CTE-03-06, CTE-03-11, CTE-03-16, CTE-03-21 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-01, CTE-04-06, CTE-04-11, CTE-04-16, CTE-04-21 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-01, CTE-05-06, CTE-05-11, CTE-05-16, CTE-05-21 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-01, DATATYPES-01-06, DATATYPES-01-11, DATATYPES-01-16, DATATYPES-01-21 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-01, DATATYPES-02-06, DATATYPES-02-11, DATATYPES-02-16, DATATYPES-02-21 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-01, DATATYPES-03-06, DATATYPES-03-11, DATATYPES-03-16, DATATYPES-03-21 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-01, DATATYPES-04-06, DATATYPES-04-11, DATATYPES-04-16, DATATYPES-04-21 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-01, DATATYPES-05-06, DATATYPES-05-11, DATATYPES-05-16, DATATYPES-05-21 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-01, DATATYPES-06-06, DATATYPES-06-11, DATATYPES-06-16, DATATYPES-06-21 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-01, DATATYPES-07-06, DATATYPES-07-11, DATATYPES-07-16, DATATYPES-07-21 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-01, DATATYPES-08-06, DATATYPES-08-11, DATATYPES-08-16, DATATYPES-08-21 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-01, DATATYPES-09-06, DATATYPES-09-11, DATATYPES-09-16, DATATYPES-09-21 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-01, DATATYPES-10-06, DATATYPES-10-11, DATATYPES-10-16, DATATYPES-10-21 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-01, DATATYPES-11-06, DATATYPES-11-11, DATATYPES-11-16, DATATYPES-11-21 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-01, DATATYPES-12-06, DATATYPES-12-11, DATATYPES-12-16, DATATYPES-12-21 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-01, DATATYPES-13-06, DATATYPES-13-11, DATATYPES-13-16, DATATYPES-13-21 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-01, DATATYPES-14-06, DATATYPES-14-11, DATATYPES-14-16, DATATYPES-14-21 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-01, DATATYPES-15-06, DATATYPES-15-11, DATATYPES-15-16, DATATYPES-15-21 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-01, DATATYPES-16-06, DATATYPES-16-11, DATATYPES-16-16, DATATYPES-16-21 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-01, DATATYPES-17-06, DATATYPES-17-11, DATATYPES-17-16, DATATYPES-17-21 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-01, DATATYPES-18-06, DATATYPES-18-11, DATATYPES-18-16, DATATYPES-18-21 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-01, DATATYPES-19-06, DATATYPES-19-11, DATATYPES-19-16, DATATYPES-19-21 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-01, DATATYPES-20-06, DATATYPES-20-11, DATATYPES-20-16, DATATYPES-20-21 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-01, DATATYPES-21-06, DATATYPES-21-11, DATATYPES-21-16, DATATYPES-21-21 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-01, DATATYPES-22-06, DATATYPES-22-11, DATATYPES-22-16, DATATYPES-22-21 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-01, DATATYPES-23-06, DATATYPES-23-11, DATATYPES-23-16, DATATYPES-23-21 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-01, DATATYPES-24-06, DATATYPES-24-11, DATATYPES-24-16, DATATYPES-24-21 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-01, DATATYPES-25-06, DATATYPES-25-11, DATATYPES-25-16, DATATYPES-25-21 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-01, DATATYPES-26-06, DATATYPES-26-11, DATATYPES-26-16, DATATYPES-26-21 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-01, DATABASE_SCHEMA_USER-01-06, DATABASE_SCHEMA_USER-01-11, DATABASE_SCHEMA_USER-01-16, DATABASE_SCHEMA_USER-01-21 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-01, DATABASE_SCHEMA_USER-02-06, DATABASE_SCHEMA_USER-02-11, DATABASE_SCHEMA_USER-02-16, DATABASE_SCHEMA_USER-02-21 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-01, DATABASE_SCHEMA_USER-03-06, DATABASE_SCHEMA_USER-03-11, DATABASE_SCHEMA_USER-03-16, DATABASE_SCHEMA_USER-03-21 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-01, INTRODUCTION-01-06, INTRODUCTION-01-11, INTRODUCTION-01-16, INTRODUCTION-01-21 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-01, INTRODUCTION-02-06, INTRODUCTION-02-11, INTRODUCTION-02-16, INTRODUCTION-02-21 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-01, INTRODUCTION-03-06, INTRODUCTION-03-11, INTRODUCTION-03-16, INTRODUCTION-03-21 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-01, INTRODUCTION-04-06, INTRODUCTION-04-11, INTRODUCTION-04-16, INTRODUCTION-04-21 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-01, INTRODUCTION-05-06, INTRODUCTION-05-11, INTRODUCTION-05-16, INTRODUCTION-05-21 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-01, INTRODUCTION-06-06, INTRODUCTION-06-11, INTRODUCTION-06-16, INTRODUCTION-06-21 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-01, INTRODUCTION-07-06, INTRODUCTION-07-11, INTRODUCTION-07-16, INTRODUCTION-07-21 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-01, INTRODUCTION-08-06, INTRODUCTION-08-11, INTRODUCTION-08-16, INTRODUCTION-08-21 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-01, INTRODUCTION-09-06, INTRODUCTION-09-11, INTRODUCTION-09-16, INTRODUCTION-09-21 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-01, INTRODUCTION-10-06, INTRODUCTION-10-11, INTRODUCTION-10-16, INTRODUCTION-10-21 |

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
