# E-commerce: connected SQL Server project

Run a marketplace with tens of thousands of orders a year: daily volume, sellers, order lines and split payments, reconciled without double-counting.

**Goal:** build and explain six related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Customers ||--o{ Orders : "CustomerID"
    Orders |o--o{ Orders : "ParentOrderID"
    Sellers ||--o{ Orders : "SellerID"
    Orders ||--o{ OrderItems : "OrderID"
    Products ||--o{ OrderItems : "ProductID"
    Orders ||--o{ Payments : "OrderID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the six tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Customers → Sellers → Products → Orders → OrderItems → Payments**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Customers

**Customers** — Shoppers; one customer can place many orders, and heavy buyers order almost every week.

| Column | Type | Requirement |
|---|---|---|
| CustomerID | int | NOT NULL |
| CustomerName | nvarchar(80) | NOT NULL |
| CustomerCode | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **CustomerID**.
Unique business key: **CustomerCode**.
Business rule: `LEN(LTRIM(RTRIM(CustomerName))) > 0`.

### Sellers

**Sellers** — Third-party sellers; each sells in one department and fulfils its own orders.

| Column | Type | Requirement |
|---|---|---|
| SellerID | int | NOT NULL |
| SellerName | nvarchar(80) | NOT NULL |
| SellerCode | varchar(20) | NOT NULL |
| Department | varchar(20) | NOT NULL |

Primary key: **SellerID**.
Unique business key: **SellerCode**.
Business rule: `LEN(LTRIM(RTRIM(SellerName))) > 0`.

### Products

**Products** — Catalog listing price; the price actually charged is kept on each order item.

| Column | Type | Requirement |
|---|---|---|
| ProductID | int | NOT NULL |
| ProductName | nvarchar(80) | NOT NULL |
| SKU | varchar(20) | NOT NULL |
| UnitPrice | decimal(12,2) | NOT NULL |
| Department | varchar(20) | NOT NULL DEFAULT ('General') |

Primary key: **ProductID**.
Unique business key: **SKU**.
Business rule: `UnitPrice > 0`.
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
| ItemCount | int | NOT NULL |
| OrderDate | date | NOT NULL |
| PlacedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentOrderID | int | NULL |
| SellerID | int | NOT NULL |

Primary key: **OrderID**.
Unique business key: **OrderReference**.
Business rule: `SalesChannel IN ('A','B','C')`.
Business rule: `OrderStatus IN ('Open','Closed','Pending')`.
Business rule: `OrderTotal >= 0`.
Business rule: `ItemCount > 0`.
Business rule: `ParentOrderID IS NULL OR ParentOrderID <> OrderID`.
Business rule: `LEN(LTRIM(RTRIM(OrderReference))) > 0`.
Foreign key: **Orders.CustomerID → Customers.CustomerID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Orders.ParentOrderID → Orders.OrderID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Orders.SellerID → Sellers.SellerID**. Use NO ACTION on delete/update; do not disable checking.

### OrderItems

**OrderItems** — Lines of an order; UnitPrice is the price charged, after any deal discount.

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

**Payments** — Payments per order: an order can be split between a gift card and a card, or be unpaid.

| Column | Type | Requirement |
|---|---|---|
| PaymentID | int | NOT NULL |
| OrderID | int | NOT NULL |
| PaymentMethod | varchar(10) | NOT NULL |
| PaidAmount | decimal(12,2) | NOT NULL |
| PaidAt | datetime2(3) | NOT NULL |

Primary key: **PaymentID**.
Business rule: `PaymentMethod IN ('Card','Wallet','GiftCard','COD')`.
Business rule: `PaidAmount > 0`.
Business rule: `LEN(LTRIM(RTRIM(PaymentMethod))) > 0`.
Foreign key: **Payments.OrderID → Orders.OrderID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** six tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

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

### Sample rows: Sellers

| SellerID | SellerName | SellerCode | Department |
|---|---|---|---|
| `1` | `Seller 1` | `SEL-1` | `Electronics` |
| `2` | `Seller 2` | `SEL-2` | `Home & Kitchen` |
| `3` | `Seller 3` | `SEL-3` | `Fashion` |
| `4` | `Seller 4` | `SEL-4` | `Books` |
| `5` | `Unused seller` | `SEL-5` | `Toys & Games` |

### Sample rows: Products

| ProductID | ProductName | SKU | UnitPrice | Department |
|---|---|---|---|---|
| `1` | `Wireless earbuds` | `EB-SKU-1` | `25` | `Electronics` |
| `2` | `USB-C charger` | `EB-SKU-2` | `10` | `Electronics` |
| `3` | `French press` | `EB-SKU-3` | `50` | `Home & Kitchen` |
| `4` | `Rain jacket` | `EB-SKU-4` | `40` | `Fashion` |
| `5` | `Unused product` | `EB-SKU-5` | `15` | `Books` |

### Sample rows: Orders

| OrderID | CustomerID | OrderReference | SalesChannel | OrderStatus | OrderTotal | ItemCount | OrderDate | PlacedAt | RecordedAt | Note | BackupNote | ParentOrderID | SellerID |
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

### Sample rows: OrderItems

| OrderItemID | OrderID | ProductID | Quantity | UnitPrice |
|---|---|---|---|---|
| `1` | `1` | `1` | `2` | `25` |
| `2` | `1` | `2` | `5` | `10` |
| `3` | `2` | `3` | `4` | `50` |
| `4` | `3` | `4` | `5` | `40` |
| `5` | `5` | `1` | `2` | `25` |
| `6` | `6` | `3` | `6` | `50` |

### Sample rows: Payments

| PaymentID | OrderID | PaymentMethod | PaidAmount | PaidAt |
|---|---|---|---|---|
| `1` | `1` | `GiftCard` | `40` | `2024-01-01T12:31:00` |
| `2` | `1` | `Card` | `60` | `2024-01-01T12:31:04` |
| `3` | `2` | `Wallet` | `200` | `2024-01-02T12:31:00` |
| `4` | `3` | `Card` | `100` | `2024-01-02T12:32:00` |
| `5` | `6` | `COD` | `300` | `2024-02-13T10:00:00` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-28, DDL-01-32, DDL-01-36, DDL-01-40, DDL-01-44 |
| [DDL](DDL.md) | Alter | DDL-02-28, DDL-02-32, DDL-02-36, DDL-02-40, DDL-02-44 |
| [DDL](DDL.md) | Drop | DDL-03-28, DDL-03-32, DDL-03-36, DDL-03-40, DDL-03-44 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-28, DATA_SETUP-01-32, DATA_SETUP-01-36, DATA_SETUP-01-40, DATA_SETUP-01-44 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-28, DATA_SETUP-02-32, DATA_SETUP-02-36, DATA_SETUP-02-40, DATA_SETUP-02-44 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-28, CONSTRAINTS-01-32, CONSTRAINTS-01-36, CONSTRAINTS-01-40, CONSTRAINTS-01-44 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-28, CONSTRAINTS-02-32, CONSTRAINTS-02-36, CONSTRAINTS-02-40, CONSTRAINTS-02-44 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-28, CONSTRAINTS-03-32, CONSTRAINTS-03-36, CONSTRAINTS-03-40, CONSTRAINTS-03-44 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-28, CONSTRAINTS-04-32, CONSTRAINTS-04-36, CONSTRAINTS-04-40, CONSTRAINTS-04-44 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-28, CONSTRAINTS-05-32, CONSTRAINTS-05-36, CONSTRAINTS-05-40, CONSTRAINTS-05-44 |
| [DML](DML.md) | Insert | DML-01-28, DML-01-32, DML-01-36, DML-01-40, DML-01-44 |
| [DML](DML.md) | Update | DML-02-28, DML-02-32, DML-02-36, DML-02-40, DML-02-44 |
| [DML](DML.md) | Delete | DML-03-28, DML-03-32, DML-03-36, DML-03-40, DML-03-44 |
| [DQL](DQL.md) | Select | DQL-01-28, DQL-01-32, DQL-01-36, DQL-01-40, DQL-01-44 |
| [DQL](DQL.md) | Where | DQL-02-28, DQL-02-32, DQL-02-36, DQL-02-40, DQL-02-44 |
| [DQL](DQL.md) | Group By | DQL-03-28, DQL-03-32, DQL-03-36, DQL-03-40, DQL-03-44 |
| [DQL](DQL.md) | Having | DQL-04-28, DQL-04-32, DQL-04-36, DQL-04-40, DQL-04-44 |
| [DQL](DQL.md) | Order By | DQL-05-28, DQL-05-32, DQL-05-36, DQL-05-40, DQL-05-44 |
| [DQL](DQL.md) | Top | DQL-06-28, DQL-06-32, DQL-06-36, DQL-06-40, DQL-06-44 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-28, OPERATORS-01-32, OPERATORS-01-36, OPERATORS-01-40, OPERATORS-01-44 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-28, OPERATORS-02-32, OPERATORS-02-36, OPERATORS-02-40, OPERATORS-02-44 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-28, OPERATORS-03-32, OPERATORS-03-36, OPERATORS-03-40, OPERATORS-03-44 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-28, OPERATORS-04-32, OPERATORS-04-36, OPERATORS-04-40, OPERATORS-04-44 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-28, OPERATORS-05-32, OPERATORS-05-36, OPERATORS-05-40, OPERATORS-05-44 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-28, OPERATORS-06-32, OPERATORS-06-36, OPERATORS-06-40, OPERATORS-06-44 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-28, OPERATORS-07-32, OPERATORS-07-36, OPERATORS-07-40, OPERATORS-07-44 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-28, OPERATORS-08-32, OPERATORS-08-36, OPERATORS-08-40, OPERATORS-08-44 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-28, OPERATORS-09-32, OPERATORS-09-36, OPERATORS-09-40, OPERATORS-09-44 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-28, OPERATORS-10-32, OPERATORS-10-36, OPERATORS-10-40, OPERATORS-10-44 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-28, OPERATORS-11-32, OPERATORS-11-36, OPERATORS-11-40, OPERATORS-11-44 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-28, OPERATORS-12-32, OPERATORS-12-36, OPERATORS-12-40, OPERATORS-12-44 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-28, OPERATORS-13-32, OPERATORS-13-36, OPERATORS-13-40, OPERATORS-13-44 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-28, JOINS-01-32, JOINS-01-36, JOINS-01-40, JOINS-01-44 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-28, JOINS-02-32, JOINS-02-36, JOINS-02-40, JOINS-02-44 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-28, JOINS-03-32, JOINS-03-36, JOINS-03-40, JOINS-03-44 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-28, JOINS-04-32, JOINS-04-36, JOINS-04-40, JOINS-04-44 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-28, JOINS-05-32, JOINS-05-36, JOINS-05-40, JOINS-05-44 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-28, SET_OPERATIONS-01-32, SET_OPERATIONS-01-36, SET_OPERATIONS-01-40, SET_OPERATIONS-01-44 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-28, SET_OPERATIONS-02-32, SET_OPERATIONS-02-36, SET_OPERATIONS-02-40, SET_OPERATIONS-02-44 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-28, SET_OPERATIONS-03-32, SET_OPERATIONS-03-36, SET_OPERATIONS-03-40, SET_OPERATIONS-03-44 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-28, SET_OPERATIONS-04-32, SET_OPERATIONS-04-36, SET_OPERATIONS-04-40, SET_OPERATIONS-04-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-28, STRING_FUNCTIONS-01-32, STRING_FUNCTIONS-01-36, STRING_FUNCTIONS-01-40, STRING_FUNCTIONS-01-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-28, STRING_FUNCTIONS-02-32, STRING_FUNCTIONS-02-36, STRING_FUNCTIONS-02-40, STRING_FUNCTIONS-02-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-28, STRING_FUNCTIONS-03-32, STRING_FUNCTIONS-03-36, STRING_FUNCTIONS-03-40, STRING_FUNCTIONS-03-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-28, STRING_FUNCTIONS-04-32, STRING_FUNCTIONS-04-36, STRING_FUNCTIONS-04-40, STRING_FUNCTIONS-04-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-28, STRING_FUNCTIONS-05-32, STRING_FUNCTIONS-05-36, STRING_FUNCTIONS-05-40, STRING_FUNCTIONS-05-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-28, STRING_FUNCTIONS-06-32, STRING_FUNCTIONS-06-36, STRING_FUNCTIONS-06-40, STRING_FUNCTIONS-06-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-28, STRING_FUNCTIONS-07-32, STRING_FUNCTIONS-07-36, STRING_FUNCTIONS-07-40, STRING_FUNCTIONS-07-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-28, STRING_FUNCTIONS-08-32, STRING_FUNCTIONS-08-36, STRING_FUNCTIONS-08-40, STRING_FUNCTIONS-08-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-28, STRING_FUNCTIONS-09-32, STRING_FUNCTIONS-09-36, STRING_FUNCTIONS-09-40, STRING_FUNCTIONS-09-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-28, STRING_FUNCTIONS-10-32, STRING_FUNCTIONS-10-36, STRING_FUNCTIONS-10-40, STRING_FUNCTIONS-10-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-28, STRING_FUNCTIONS-11-32, STRING_FUNCTIONS-11-36, STRING_FUNCTIONS-11-40, STRING_FUNCTIONS-11-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-28, STRING_FUNCTIONS-12-32, STRING_FUNCTIONS-12-36, STRING_FUNCTIONS-12-40, STRING_FUNCTIONS-12-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-28, STRING_FUNCTIONS-13-32, STRING_FUNCTIONS-13-36, STRING_FUNCTIONS-13-40, STRING_FUNCTIONS-13-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-28, STRING_FUNCTIONS-14-32, STRING_FUNCTIONS-14-36, STRING_FUNCTIONS-14-40, STRING_FUNCTIONS-14-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-28, STRING_FUNCTIONS-15-32, STRING_FUNCTIONS-15-36, STRING_FUNCTIONS-15-40, STRING_FUNCTIONS-15-44 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-28, STRING_FUNCTIONS-16-32, STRING_FUNCTIONS-16-36, STRING_FUNCTIONS-16-40, STRING_FUNCTIONS-16-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-28, DATE_FUNCTIONS-01-32, DATE_FUNCTIONS-01-36, DATE_FUNCTIONS-01-40, DATE_FUNCTIONS-01-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-28, DATE_FUNCTIONS-02-32, DATE_FUNCTIONS-02-36, DATE_FUNCTIONS-02-40, DATE_FUNCTIONS-02-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-28, DATE_FUNCTIONS-03-32, DATE_FUNCTIONS-03-36, DATE_FUNCTIONS-03-40, DATE_FUNCTIONS-03-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-28, DATE_FUNCTIONS-04-32, DATE_FUNCTIONS-04-36, DATE_FUNCTIONS-04-40, DATE_FUNCTIONS-04-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-28, DATE_FUNCTIONS-05-32, DATE_FUNCTIONS-05-36, DATE_FUNCTIONS-05-40, DATE_FUNCTIONS-05-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-28, DATE_FUNCTIONS-06-32, DATE_FUNCTIONS-06-36, DATE_FUNCTIONS-06-40, DATE_FUNCTIONS-06-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-28, DATE_FUNCTIONS-07-32, DATE_FUNCTIONS-07-36, DATE_FUNCTIONS-07-40, DATE_FUNCTIONS-07-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-28, DATE_FUNCTIONS-08-32, DATE_FUNCTIONS-08-36, DATE_FUNCTIONS-08-40, DATE_FUNCTIONS-08-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-28, DATE_FUNCTIONS-09-32, DATE_FUNCTIONS-09-36, DATE_FUNCTIONS-09-40, DATE_FUNCTIONS-09-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-28, DATE_FUNCTIONS-10-32, DATE_FUNCTIONS-10-36, DATE_FUNCTIONS-10-40, DATE_FUNCTIONS-10-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-28, DATE_FUNCTIONS-11-32, DATE_FUNCTIONS-11-36, DATE_FUNCTIONS-11-40, DATE_FUNCTIONS-11-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-28, DATE_FUNCTIONS-12-32, DATE_FUNCTIONS-12-36, DATE_FUNCTIONS-12-40, DATE_FUNCTIONS-12-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-28, DATE_FUNCTIONS-13-32, DATE_FUNCTIONS-13-36, DATE_FUNCTIONS-13-40, DATE_FUNCTIONS-13-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-28, DATE_FUNCTIONS-14-32, DATE_FUNCTIONS-14-36, DATE_FUNCTIONS-14-40, DATE_FUNCTIONS-14-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-28, DATE_FUNCTIONS-15-32, DATE_FUNCTIONS-15-36, DATE_FUNCTIONS-15-40, DATE_FUNCTIONS-15-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-28, DATE_FUNCTIONS-16-32, DATE_FUNCTIONS-16-36, DATE_FUNCTIONS-16-40, DATE_FUNCTIONS-16-44 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-28, DATE_FUNCTIONS-17-32, DATE_FUNCTIONS-17-36, DATE_FUNCTIONS-17-40, DATE_FUNCTIONS-17-44 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-28, AGGREGATES-01-32, AGGREGATES-01-36, AGGREGATES-01-40, AGGREGATES-01-44 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-28, AGGREGATES-02-32, AGGREGATES-02-36, AGGREGATES-02-40, AGGREGATES-02-44 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-28, AGGREGATES-03-32, AGGREGATES-03-36, AGGREGATES-03-40, AGGREGATES-03-44 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-28, AGGREGATES-04-32, AGGREGATES-04-36, AGGREGATES-04-40, AGGREGATES-04-44 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-28, AGGREGATES-05-32, AGGREGATES-05-36, AGGREGATES-05-40, AGGREGATES-05-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-28, ANALYTICAL_FUNCTIONS-01-32, ANALYTICAL_FUNCTIONS-01-36, ANALYTICAL_FUNCTIONS-01-40, ANALYTICAL_FUNCTIONS-01-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-28, ANALYTICAL_FUNCTIONS-02-32, ANALYTICAL_FUNCTIONS-02-36, ANALYTICAL_FUNCTIONS-02-40, ANALYTICAL_FUNCTIONS-02-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-28, ANALYTICAL_FUNCTIONS-03-32, ANALYTICAL_FUNCTIONS-03-36, ANALYTICAL_FUNCTIONS-03-40, ANALYTICAL_FUNCTIONS-03-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-28, ANALYTICAL_FUNCTIONS-04-32, ANALYTICAL_FUNCTIONS-04-36, ANALYTICAL_FUNCTIONS-04-40, ANALYTICAL_FUNCTIONS-04-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-28, ANALYTICAL_FUNCTIONS-05-32, ANALYTICAL_FUNCTIONS-05-36, ANALYTICAL_FUNCTIONS-05-40, ANALYTICAL_FUNCTIONS-05-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-28, ANALYTICAL_FUNCTIONS-06-32, ANALYTICAL_FUNCTIONS-06-36, ANALYTICAL_FUNCTIONS-06-40, ANALYTICAL_FUNCTIONS-06-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-28, ANALYTICAL_FUNCTIONS-07-32, ANALYTICAL_FUNCTIONS-07-36, ANALYTICAL_FUNCTIONS-07-40, ANALYTICAL_FUNCTIONS-07-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-28, ANALYTICAL_FUNCTIONS-08-32, ANALYTICAL_FUNCTIONS-08-36, ANALYTICAL_FUNCTIONS-08-40, ANALYTICAL_FUNCTIONS-08-44 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-28, ANALYTICAL_FUNCTIONS-09-32, ANALYTICAL_FUNCTIONS-09-36, ANALYTICAL_FUNCTIONS-09-40, ANALYTICAL_FUNCTIONS-09-44 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-28, CTE-01-32, CTE-01-36, CTE-01-40, CTE-01-44 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-28, CTE-02-32, CTE-02-36, CTE-02-40, CTE-02-44 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-28, CTE-03-32, CTE-03-36, CTE-03-40, CTE-03-44 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-28, CTE-04-32, CTE-04-36, CTE-04-40, CTE-04-44 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-28, CTE-05-32, CTE-05-36, CTE-05-40, CTE-05-44 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-28, DATATYPES-01-32, DATATYPES-01-36, DATATYPES-01-40, DATATYPES-01-44 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-28, DATATYPES-02-32, DATATYPES-02-36, DATATYPES-02-40, DATATYPES-02-44 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-28, DATATYPES-03-32, DATATYPES-03-36, DATATYPES-03-40, DATATYPES-03-44 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-28, DATATYPES-04-32, DATATYPES-04-36, DATATYPES-04-40, DATATYPES-04-44 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-28, DATATYPES-05-32, DATATYPES-05-36, DATATYPES-05-40, DATATYPES-05-44 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-28, DATATYPES-06-32, DATATYPES-06-36, DATATYPES-06-40, DATATYPES-06-44 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-28, DATATYPES-07-32, DATATYPES-07-36, DATATYPES-07-40, DATATYPES-07-44 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-28, DATATYPES-08-32, DATATYPES-08-36, DATATYPES-08-40, DATATYPES-08-44 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-28, DATATYPES-09-32, DATATYPES-09-36, DATATYPES-09-40, DATATYPES-09-44 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-28, DATATYPES-10-32, DATATYPES-10-36, DATATYPES-10-40, DATATYPES-10-44 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-28, DATATYPES-11-32, DATATYPES-11-36, DATATYPES-11-40, DATATYPES-11-44 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-28, DATATYPES-12-32, DATATYPES-12-36, DATATYPES-12-40, DATATYPES-12-44 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-28, DATATYPES-13-32, DATATYPES-13-36, DATATYPES-13-40, DATATYPES-13-44 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-28, DATATYPES-14-32, DATATYPES-14-36, DATATYPES-14-40, DATATYPES-14-44 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-28, DATATYPES-15-32, DATATYPES-15-36, DATATYPES-15-40, DATATYPES-15-44 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-28, DATATYPES-16-32, DATATYPES-16-36, DATATYPES-16-40, DATATYPES-16-44 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-28, DATATYPES-17-32, DATATYPES-17-36, DATATYPES-17-40, DATATYPES-17-44 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-28, DATATYPES-18-32, DATATYPES-18-36, DATATYPES-18-40, DATATYPES-18-44 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-28, DATATYPES-19-32, DATATYPES-19-36, DATATYPES-19-40, DATATYPES-19-44 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-28, DATATYPES-20-32, DATATYPES-20-36, DATATYPES-20-40, DATATYPES-20-44 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-28, DATATYPES-21-32, DATATYPES-21-36, DATATYPES-21-40, DATATYPES-21-44 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-28, DATATYPES-22-32, DATATYPES-22-36, DATATYPES-22-40, DATATYPES-22-44 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-28, DATATYPES-23-32, DATATYPES-23-36, DATATYPES-23-40, DATATYPES-23-44 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-28, DATATYPES-24-32, DATATYPES-24-36, DATATYPES-24-40, DATATYPES-24-44 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-28, DATATYPES-25-32, DATATYPES-25-36, DATATYPES-25-40, DATATYPES-25-44 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-28, DATATYPES-26-32, DATATYPES-26-36, DATATYPES-26-40, DATATYPES-26-44 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-28, DATABASE_SCHEMA_USER-01-32, DATABASE_SCHEMA_USER-01-36, DATABASE_SCHEMA_USER-01-40, DATABASE_SCHEMA_USER-01-44 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-28, DATABASE_SCHEMA_USER-02-32, DATABASE_SCHEMA_USER-02-36, DATABASE_SCHEMA_USER-02-40, DATABASE_SCHEMA_USER-02-44 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-28, DATABASE_SCHEMA_USER-03-32, DATABASE_SCHEMA_USER-03-36, DATABASE_SCHEMA_USER-03-40, DATABASE_SCHEMA_USER-03-44 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-28, INTRODUCTION-01-32, INTRODUCTION-01-36, INTRODUCTION-01-40, INTRODUCTION-01-44 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-28, INTRODUCTION-02-32, INTRODUCTION-02-36, INTRODUCTION-02-40, INTRODUCTION-02-44 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-28, INTRODUCTION-03-32, INTRODUCTION-03-36, INTRODUCTION-03-40, INTRODUCTION-03-44 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-28, INTRODUCTION-04-32, INTRODUCTION-04-36, INTRODUCTION-04-40, INTRODUCTION-04-44 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-28, INTRODUCTION-05-32, INTRODUCTION-05-36, INTRODUCTION-05-40, INTRODUCTION-05-44 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-28, INTRODUCTION-06-32, INTRODUCTION-06-36, INTRODUCTION-06-40, INTRODUCTION-06-44 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-28, INTRODUCTION-07-32, INTRODUCTION-07-36, INTRODUCTION-07-40, INTRODUCTION-07-44 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-28, INTRODUCTION-08-32, INTRODUCTION-08-36, INTRODUCTION-08-40, INTRODUCTION-08-44 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-28, INTRODUCTION-09-32, INTRODUCTION-09-36, INTRODUCTION-09-40, INTRODUCTION-09-44 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-28, INTRODUCTION-10-32, INTRODUCTION-10-36, INTRODUCTION-10-40, INTRODUCTION-10-44 |

## 5. Integrate all six tables

Complete [REPORTING_ASSIGNMENTS.md](REPORTING_ASSIGNMENTS.md) after joins, aggregates and CTEs. These reports follow the domain workflow and include reconciliations that fail when joins multiply rows.

## 6. Confidence checkpoint and final project

Using a fresh database and this specification, without copying the solution:

1. Draw and explain all six tables and relationship row counts.
2. Re-create the schema in the order shown in your domain guide, including every PK, FK, UNIQUE, CHECK and default.
3. Load valid sample data; demonstrate rejection of a duplicate PK, duplicate business key, NULL required field, invalid CHECK value and nonexistent parent.
4. Demonstrate that deleting a referenced parent fails; explain a child-first deletion plan. Use a practice database with the supplied sample rows and keep the foreign keys enabled.
5. Perform a correct insert, targeted update and targeted delete, checking the number of changed rows. Ask your instructor to reset the practice tables afterwards.
6. Complete all six domain reports and compare and check their row counts and control totals.
7. Add one new valid business record with related details, rerun the reports and explain exactly which results changed. Ask your instructor to reset the practice tables afterwards.
8. Explain NULL handling, INNER versus LEFT JOIN, WHERE versus HAVING, duplicate multiplication and deterministic ranking.

**Ready to progress:** all integrity tests pass, all six reports compare and check, and you can explain each relationship and fix a deliberately incorrect join without an answer key. If a checkpoint fails, revisit that section instead of advancing by a calendar date.
