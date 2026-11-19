# Brokerage: connected SQL Server project

Trace clients and accounts through securities, trade orders and partial executions. Reconcile filled quantities and weighted average execution prices.

An independent, synthetic brokerage training model. Scope: buy orders for fictitious stocks and ETFs, including partial fills. Settlement, cash ledgers, positions, margin, taxes and options are outside this five-table model. WorkflowStatus is an administrative practice flag; derive fill status from requested and executed quantities.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Clients ||--o{ BrokerageAccounts : "ClientID"
    BrokerageAccounts ||--o{ TradeOrders : "AccountID"
    TradeOrders |o--o{ TradeOrders : "ParentOrderID"
    Securities ||--o{ TradeOrders : "SecurityID"
    TradeOrders ||--o{ Executions : "OrderID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Clients → Securities → BrokerageAccounts → TradeOrders → Executions**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Clients

**Clients** — Synthetic individual brokerage clients; each can hold multiple accounts.

| Column | Type | Requirement |
|---|---|---|
| ClientID | int | NOT NULL |
| ClientName | nvarchar(80) | NOT NULL |
| ClientReference | varchar(20) | NOT NULL |
| Email | varchar(100) | NOT NULL |

Primary key: **ClientID**.
Unique business key: **ClientReference**.
Unique business key: **Email**.
Business rule: `LEN(LTRIM(RTRIM(ClientName))) > 0`.

### Securities

**Securities** — Fictitious stock and ETF instruments with unique symbols.

| Column | Type | Requirement |
|---|---|---|
| SecurityID | int | NOT NULL |
| SecurityName | nvarchar(80) | NOT NULL |
| Symbol | varchar(20) | NOT NULL |
| AssetClass | varchar(10) | NOT NULL |

Primary key: **SecurityID**.
Unique business key: **Symbol**.
Business rule: `AssetClass IN ('Stock','ETF')`.
Business rule: `LEN(LTRIM(RTRIM(SecurityName))) > 0`.

### BrokerageAccounts

**BrokerageAccounts** — Each brokerage account belongs to one client; Region is the servicing region.

| Column | Type | Requirement |
|---|---|---|
| AccountID | int | NOT NULL |
| AccountName | nvarchar(80) | NOT NULL |
| AccountNumber | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |
| ClientID | int | NOT NULL |

Primary key: **AccountID**.
Unique business key: **AccountNumber**.
Business rule: `LEN(LTRIM(RTRIM(AccountName))) > 0`.
Foreign key: **BrokerageAccounts.ClientID → Clients.ClientID**. Use NO ACTION on delete/update; do not disable checking.

### TradeOrders

**TradeOrders** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| OrderID | int | NOT NULL |
| AccountID | int | NOT NULL |
| OrderReference | nvarchar(80) | NOT NULL |
| RoutingCategory | varchar(10) | NOT NULL |
| WorkflowStatus | varchar(10) | NOT NULL DEFAULT ('Open') |
| EstimatedValue | decimal(12,2) | NULL |
| RequestedQuantity | int | NOT NULL |
| OrderDate | date | NOT NULL |
| SubmittedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentOrderID | int | NULL |
| SecurityID | int | NOT NULL |
| Side | varchar(3) | NOT NULL DEFAULT ('Buy') |

Primary key: **OrderID**.
Unique business key: **OrderReference**.
Business rule: `RoutingCategory IN ('A','B','C')`.
Business rule: `WorkflowStatus IN ('Open','Closed','Pending')`.
Business rule: `EstimatedValue >= 0`.
Business rule: `RequestedQuantity > 0`.
Business rule: `ParentOrderID IS NULL OR ParentOrderID <> OrderID`.
Business rule: `Side = 'Buy'`.
Business rule: `LEN(LTRIM(RTRIM(OrderReference))) > 0`.
Foreign key: **TradeOrders.AccountID → BrokerageAccounts.AccountID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **TradeOrders.ParentOrderID → TradeOrders.OrderID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **TradeOrders.SecurityID → Securities.SecurityID**. Use NO ACTION on delete/update; do not disable checking.

### Executions

**Executions** — Individual partial fills. Total fills must not exceed the requested order quantity; this cross-row rule is validated by reconciliation.

| Column | Type | Requirement |
|---|---|---|
| ExecutionID | int | NOT NULL |
| OrderID | int | NOT NULL |
| ExecutionReference | varchar(20) | NOT NULL |
| ExecutedQuantity | decimal(12,4) | NOT NULL |
| ExecutionPrice | decimal(12,4) | NOT NULL |
| ExecutedAt | datetime2(3) | NOT NULL |

Primary key: **ExecutionID**.
Unique business key: **ExecutionReference**.
Business rule: `ExecutedQuantity > 0`.
Business rule: `ExecutionPrice > 0`.
Business rule: `LEN(LTRIM(RTRIM(ExecutionReference))) > 0`.
Foreign key: **Executions.OrderID → TradeOrders.OrderID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** five tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Clients

| ClientID | ClientName | ClientReference | Email |
|---|---|---|---|
| `1` | `Investor 1` | `CLIENT-1` | `investor1@example.test` |
| `2` | `Investor 2` | `CLIENT-2` | `investor2@example.test` |
| `3` | `Investor 3` | `CLIENT-3` | `investor3@example.test` |
| `4` | `Investor 4` | `CLIENT-4` | `investor4@example.test` |
| `5` | `Investor 5` | `CLIENT-5` | `investor5@example.test` |

### Sample rows: Securities

| SecurityID | SecurityName | Symbol | AssetClass |
|---|---|---|---|
| `1` | `Training Equity Alpha` | `DEMO-A` | `Stock` |
| `2` | `Training Equity Beta` | `DEMO-B` | `Stock` |
| `3` | `Training Fund Gamma` | `DEMO-C` | `ETF` |
| `4` | `Training Fund Delta` | `DEMO-D` | `ETF` |
| `5` | `Unused Training Equity` | `DEMO-E` | `Stock` |

### Sample rows: BrokerageAccounts

| AccountID | AccountName | AccountNumber | Region | ClientID |
|---|---|---|---|---|
| `1` | `BrokerageAccounts Alpha` | `ACC-1` | `North` | `1` |
| `2` | `BrokerageAccounts Beta` | `ACC-2` | `South` | `2` |
| `3` | `BrokerageAccounts Gamma` | `ACC-3` | `North` | `3` |
| `4` | `BrokerageAccounts Delta` | `ACC-4` | `West` | `4` |
| `5` | `BrokerageAccounts Unused` | `ACC-5` | `East` | `5` |

### Sample rows: TradeOrders

| OrderID | AccountID | OrderReference | RoutingCategory | WorkflowStatus | EstimatedValue | RequestedQuantity | OrderDate | SubmittedAt | RecordedAt | Note | BackupNote | ParentOrderID | SecurityID | Side |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `1` | `1` | `  Alpha-One  ` | `A` | `Open` | `100` | `1` | `20240101` | `2024-01-01T12:30:45.123` | `2024-01-01T12:30:45.123+00:00` | NULL | `backup` | NULL | `1` | `Buy` |
| `2` | `1` | `beta-Two` | `B` | `Closed` | `200` | `2` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | NULL | `1` | `2` | `Buy` |
| `3` | `2` | `Gamma-Three ` | `C` | `Pending` | `200` | `3` | `20240102` | `2024-01-02T12:30:45.123` | `2024-01-02T12:30:45.123+00:00` | `confirmed` | `backup` | `1` | `3` | `Buy` |
| `4` | `2` | ` Delta-Four` | `A` | `Open` | NULL | `4` | `20240103` | `2024-01-03T12:30:45.123` | `2024-01-03T12:30:45.123+00:00` | NULL | NULL | `2` | `4` | `Buy` |
| `5` | `3` | `Echo-Five` | `B` | `Closed` | `50` | `1` | `20240201` | `2024-02-01T12:30:45.123` | `2024-02-01T12:30:45.123+00:00` | `confirmed` | `backup` | `2` | `1` | `Buy` |
| `6` | `3` | `ALPHA-Six` | `C` | `Pending` | `300` | `2` | `20240210` | `2024-02-10T12:30:45.123` | `2024-02-10T12:30:45.123+00:00` | `confirmed` | NULL | `3` | `2` | `Buy` |
| `7` | `4` | `Zero-Seven` | `A` | `Open` | `0` | `3` | `20240229` | `2024-02-29T12:30:45.123` | `2024-02-29T12:30:45.123+00:00` | NULL | `backup` | `3` | `3` | `Buy` |
| `8` | `4` | `Review-Eight` | `B` | `Closed` | `150` | `4` | `20240301` | `2024-03-01T12:30:45.123` | `2024-03-01T12:30:45.123+00:00` | `confirmed` | NULL | `4` | `4` | `Buy` |
| `9` | `4` | `Zulu-Nine` | `C` | `Pending` | `300` | `1` | `20240310` | `2024-03-10T12:30:45.123` | `2024-03-10T12:30:45.123+00:00` | `confirmed` | `backup` | `4` | `1` | `Buy` |
| `10` | `4` | `Iota-Ten` | `A` | `Open` | `80` | `2` | `20241103` | `2024-11-03T12:30:45.123` | `2024-11-03T12:30:45.123+00:00` | NULL | NULL | `5` | `2` | `Buy` |
| `11` | `1` | `Kappa-Eleven` | `B` | `Closed` | `120` | `3` | `20241231` | `2024-12-31T12:30:45.123` | `2024-12-31T12:30:45.123+00:00` | `confirmed` | `backup` | `5` | `3` | `Buy` |
| `12` | `2` | `Last-Twelve` | `C` | `Pending` | `200` | `4` | `20250101` | `2025-01-01T12:30:45.123` | `2025-01-01T12:30:45.123+00:00` | `confirmed` | NULL | `6` | `4` | `Buy` |

### Sample rows: Executions

| ExecutionID | OrderID | ExecutionReference | ExecutedQuantity | ExecutionPrice | ExecutedAt |
|---|---|---|---|---|---|
| `1` | `1` | `FILL-1` | `0.4` | `100` | `2024-01-01T12:31:00` |
| `2` | `1` | `FILL-2` | `0.6` | `101` | `2024-01-01T12:32:00` |
| `3` | `2` | `FILL-3` | `1` | `99` | `2024-01-02T12:31:00` |
| `4` | `2` | `FILL-4` | `0.5` | `100` | `2024-01-02T12:32:00` |
| `5` | `3` | `FILL-5` | `3` | `101` | `2024-01-02T12:33:00` |
| `6` | `6` | `FILL-6` | `1` | `150` | `2024-02-10T12:31:00` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../SQL/Excerises/BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-29, DDL-01-33, DDL-01-37, DDL-01-41, DDL-01-45 |
| [DDL](DDL.md) | Alter | DDL-02-29, DDL-02-33, DDL-02-37, DDL-02-41, DDL-02-45 |
| [DDL](DDL.md) | Drop | DDL-03-29, DDL-03-33, DDL-03-37, DDL-03-41, DDL-03-45 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-29, DATA_SETUP-01-33, DATA_SETUP-01-37, DATA_SETUP-01-41, DATA_SETUP-01-45 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-29, DATA_SETUP-02-33, DATA_SETUP-02-37, DATA_SETUP-02-41, DATA_SETUP-02-45 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-29, CONSTRAINTS-01-33, CONSTRAINTS-01-37, CONSTRAINTS-01-41, CONSTRAINTS-01-45 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-29, CONSTRAINTS-02-33, CONSTRAINTS-02-37, CONSTRAINTS-02-41, CONSTRAINTS-02-45 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-29, CONSTRAINTS-03-33, CONSTRAINTS-03-37, CONSTRAINTS-03-41, CONSTRAINTS-03-45 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-29, CONSTRAINTS-04-33, CONSTRAINTS-04-37, CONSTRAINTS-04-41, CONSTRAINTS-04-45 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-29, CONSTRAINTS-05-33, CONSTRAINTS-05-37, CONSTRAINTS-05-41, CONSTRAINTS-05-45 |
| [DML](DML.md) | Insert | DML-01-29, DML-01-33, DML-01-37, DML-01-41, DML-01-45 |
| [DML](DML.md) | Update | DML-02-29, DML-02-33, DML-02-37, DML-02-41, DML-02-45 |
| [DML](DML.md) | Delete | DML-03-29, DML-03-33, DML-03-37, DML-03-41, DML-03-45 |
| [DQL](DQL.md) | Select | DQL-01-29, DQL-01-33, DQL-01-37, DQL-01-41, DQL-01-45 |
| [DQL](DQL.md) | Where | DQL-02-29, DQL-02-33, DQL-02-37, DQL-02-41, DQL-02-45 |
| [DQL](DQL.md) | Group By | DQL-03-29, DQL-03-33, DQL-03-37, DQL-03-41, DQL-03-45 |
| [DQL](DQL.md) | Having | DQL-04-29, DQL-04-33, DQL-04-37, DQL-04-41, DQL-04-45 |
| [DQL](DQL.md) | Order By | DQL-05-29, DQL-05-33, DQL-05-37, DQL-05-41, DQL-05-45 |
| [DQL](DQL.md) | Top | DQL-06-29, DQL-06-33, DQL-06-37, DQL-06-41, DQL-06-45 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-29, OPERATORS-01-33, OPERATORS-01-37, OPERATORS-01-41, OPERATORS-01-45 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-29, OPERATORS-02-33, OPERATORS-02-37, OPERATORS-02-41, OPERATORS-02-45 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-29, OPERATORS-03-33, OPERATORS-03-37, OPERATORS-03-41, OPERATORS-03-45 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-29, OPERATORS-04-33, OPERATORS-04-37, OPERATORS-04-41, OPERATORS-04-45 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-29, OPERATORS-05-33, OPERATORS-05-37, OPERATORS-05-41, OPERATORS-05-45 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-29, OPERATORS-06-33, OPERATORS-06-37, OPERATORS-06-41, OPERATORS-06-45 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-29, OPERATORS-07-33, OPERATORS-07-37, OPERATORS-07-41, OPERATORS-07-45 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-29, OPERATORS-08-33, OPERATORS-08-37, OPERATORS-08-41, OPERATORS-08-45 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-29, OPERATORS-09-33, OPERATORS-09-37, OPERATORS-09-41, OPERATORS-09-45 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-29, OPERATORS-10-33, OPERATORS-10-37, OPERATORS-10-41, OPERATORS-10-45 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-29, OPERATORS-11-33, OPERATORS-11-37, OPERATORS-11-41, OPERATORS-11-45 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-29, OPERATORS-12-33, OPERATORS-12-37, OPERATORS-12-41, OPERATORS-12-45 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-29, OPERATORS-13-33, OPERATORS-13-37, OPERATORS-13-41, OPERATORS-13-45 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-29, JOINS-01-33, JOINS-01-37, JOINS-01-41, JOINS-01-45 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-29, JOINS-02-33, JOINS-02-37, JOINS-02-41, JOINS-02-45 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-29, JOINS-03-33, JOINS-03-37, JOINS-03-41, JOINS-03-45 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-29, JOINS-04-33, JOINS-04-37, JOINS-04-41, JOINS-04-45 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-29, JOINS-05-33, JOINS-05-37, JOINS-05-41, JOINS-05-45 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-29, SET_OPERATIONS-01-33, SET_OPERATIONS-01-37, SET_OPERATIONS-01-41, SET_OPERATIONS-01-45 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-29, SET_OPERATIONS-02-33, SET_OPERATIONS-02-37, SET_OPERATIONS-02-41, SET_OPERATIONS-02-45 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-29, SET_OPERATIONS-03-33, SET_OPERATIONS-03-37, SET_OPERATIONS-03-41, SET_OPERATIONS-03-45 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-29, SET_OPERATIONS-04-33, SET_OPERATIONS-04-37, SET_OPERATIONS-04-41, SET_OPERATIONS-04-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-29, STRING_FUNCTIONS-01-33, STRING_FUNCTIONS-01-37, STRING_FUNCTIONS-01-41, STRING_FUNCTIONS-01-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-29, STRING_FUNCTIONS-02-33, STRING_FUNCTIONS-02-37, STRING_FUNCTIONS-02-41, STRING_FUNCTIONS-02-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-29, STRING_FUNCTIONS-03-33, STRING_FUNCTIONS-03-37, STRING_FUNCTIONS-03-41, STRING_FUNCTIONS-03-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-29, STRING_FUNCTIONS-04-33, STRING_FUNCTIONS-04-37, STRING_FUNCTIONS-04-41, STRING_FUNCTIONS-04-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-29, STRING_FUNCTIONS-05-33, STRING_FUNCTIONS-05-37, STRING_FUNCTIONS-05-41, STRING_FUNCTIONS-05-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-29, STRING_FUNCTIONS-06-33, STRING_FUNCTIONS-06-37, STRING_FUNCTIONS-06-41, STRING_FUNCTIONS-06-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-29, STRING_FUNCTIONS-07-33, STRING_FUNCTIONS-07-37, STRING_FUNCTIONS-07-41, STRING_FUNCTIONS-07-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-29, STRING_FUNCTIONS-08-33, STRING_FUNCTIONS-08-37, STRING_FUNCTIONS-08-41, STRING_FUNCTIONS-08-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-29, STRING_FUNCTIONS-09-33, STRING_FUNCTIONS-09-37, STRING_FUNCTIONS-09-41, STRING_FUNCTIONS-09-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-29, STRING_FUNCTIONS-10-33, STRING_FUNCTIONS-10-37, STRING_FUNCTIONS-10-41, STRING_FUNCTIONS-10-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-29, STRING_FUNCTIONS-11-33, STRING_FUNCTIONS-11-37, STRING_FUNCTIONS-11-41, STRING_FUNCTIONS-11-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-29, STRING_FUNCTIONS-12-33, STRING_FUNCTIONS-12-37, STRING_FUNCTIONS-12-41, STRING_FUNCTIONS-12-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-29, STRING_FUNCTIONS-13-33, STRING_FUNCTIONS-13-37, STRING_FUNCTIONS-13-41, STRING_FUNCTIONS-13-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-29, STRING_FUNCTIONS-14-33, STRING_FUNCTIONS-14-37, STRING_FUNCTIONS-14-41, STRING_FUNCTIONS-14-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-29, STRING_FUNCTIONS-15-33, STRING_FUNCTIONS-15-37, STRING_FUNCTIONS-15-41, STRING_FUNCTIONS-15-45 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-29, STRING_FUNCTIONS-16-33, STRING_FUNCTIONS-16-37, STRING_FUNCTIONS-16-41, STRING_FUNCTIONS-16-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-29, DATE_FUNCTIONS-01-33, DATE_FUNCTIONS-01-37, DATE_FUNCTIONS-01-41, DATE_FUNCTIONS-01-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-29, DATE_FUNCTIONS-02-33, DATE_FUNCTIONS-02-37, DATE_FUNCTIONS-02-41, DATE_FUNCTIONS-02-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-29, DATE_FUNCTIONS-03-33, DATE_FUNCTIONS-03-37, DATE_FUNCTIONS-03-41, DATE_FUNCTIONS-03-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-29, DATE_FUNCTIONS-04-33, DATE_FUNCTIONS-04-37, DATE_FUNCTIONS-04-41, DATE_FUNCTIONS-04-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-29, DATE_FUNCTIONS-05-33, DATE_FUNCTIONS-05-37, DATE_FUNCTIONS-05-41, DATE_FUNCTIONS-05-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-29, DATE_FUNCTIONS-06-33, DATE_FUNCTIONS-06-37, DATE_FUNCTIONS-06-41, DATE_FUNCTIONS-06-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-29, DATE_FUNCTIONS-07-33, DATE_FUNCTIONS-07-37, DATE_FUNCTIONS-07-41, DATE_FUNCTIONS-07-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-29, DATE_FUNCTIONS-08-33, DATE_FUNCTIONS-08-37, DATE_FUNCTIONS-08-41, DATE_FUNCTIONS-08-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-29, DATE_FUNCTIONS-09-33, DATE_FUNCTIONS-09-37, DATE_FUNCTIONS-09-41, DATE_FUNCTIONS-09-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-29, DATE_FUNCTIONS-10-33, DATE_FUNCTIONS-10-37, DATE_FUNCTIONS-10-41, DATE_FUNCTIONS-10-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-29, DATE_FUNCTIONS-11-33, DATE_FUNCTIONS-11-37, DATE_FUNCTIONS-11-41, DATE_FUNCTIONS-11-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-29, DATE_FUNCTIONS-12-33, DATE_FUNCTIONS-12-37, DATE_FUNCTIONS-12-41, DATE_FUNCTIONS-12-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-29, DATE_FUNCTIONS-13-33, DATE_FUNCTIONS-13-37, DATE_FUNCTIONS-13-41, DATE_FUNCTIONS-13-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-29, DATE_FUNCTIONS-14-33, DATE_FUNCTIONS-14-37, DATE_FUNCTIONS-14-41, DATE_FUNCTIONS-14-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-29, DATE_FUNCTIONS-15-33, DATE_FUNCTIONS-15-37, DATE_FUNCTIONS-15-41, DATE_FUNCTIONS-15-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-29, DATE_FUNCTIONS-16-33, DATE_FUNCTIONS-16-37, DATE_FUNCTIONS-16-41, DATE_FUNCTIONS-16-45 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-29, DATE_FUNCTIONS-17-33, DATE_FUNCTIONS-17-37, DATE_FUNCTIONS-17-41, DATE_FUNCTIONS-17-45 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-29, AGGREGATES-01-33, AGGREGATES-01-37, AGGREGATES-01-41, AGGREGATES-01-45 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-29, AGGREGATES-02-33, AGGREGATES-02-37, AGGREGATES-02-41, AGGREGATES-02-45 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-29, AGGREGATES-03-33, AGGREGATES-03-37, AGGREGATES-03-41, AGGREGATES-03-45 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-29, AGGREGATES-04-33, AGGREGATES-04-37, AGGREGATES-04-41, AGGREGATES-04-45 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-29, AGGREGATES-05-33, AGGREGATES-05-37, AGGREGATES-05-41, AGGREGATES-05-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-29, ANALYTICAL_FUNCTIONS-01-33, ANALYTICAL_FUNCTIONS-01-37, ANALYTICAL_FUNCTIONS-01-41, ANALYTICAL_FUNCTIONS-01-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-29, ANALYTICAL_FUNCTIONS-02-33, ANALYTICAL_FUNCTIONS-02-37, ANALYTICAL_FUNCTIONS-02-41, ANALYTICAL_FUNCTIONS-02-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-29, ANALYTICAL_FUNCTIONS-03-33, ANALYTICAL_FUNCTIONS-03-37, ANALYTICAL_FUNCTIONS-03-41, ANALYTICAL_FUNCTIONS-03-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-29, ANALYTICAL_FUNCTIONS-04-33, ANALYTICAL_FUNCTIONS-04-37, ANALYTICAL_FUNCTIONS-04-41, ANALYTICAL_FUNCTIONS-04-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-29, ANALYTICAL_FUNCTIONS-05-33, ANALYTICAL_FUNCTIONS-05-37, ANALYTICAL_FUNCTIONS-05-41, ANALYTICAL_FUNCTIONS-05-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-29, ANALYTICAL_FUNCTIONS-06-33, ANALYTICAL_FUNCTIONS-06-37, ANALYTICAL_FUNCTIONS-06-41, ANALYTICAL_FUNCTIONS-06-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-29, ANALYTICAL_FUNCTIONS-07-33, ANALYTICAL_FUNCTIONS-07-37, ANALYTICAL_FUNCTIONS-07-41, ANALYTICAL_FUNCTIONS-07-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-29, ANALYTICAL_FUNCTIONS-08-33, ANALYTICAL_FUNCTIONS-08-37, ANALYTICAL_FUNCTIONS-08-41, ANALYTICAL_FUNCTIONS-08-45 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-29, ANALYTICAL_FUNCTIONS-09-33, ANALYTICAL_FUNCTIONS-09-37, ANALYTICAL_FUNCTIONS-09-41, ANALYTICAL_FUNCTIONS-09-45 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-29, CTE-01-33, CTE-01-37, CTE-01-41, CTE-01-45 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-29, CTE-02-33, CTE-02-37, CTE-02-41, CTE-02-45 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-29, CTE-03-33, CTE-03-37, CTE-03-41, CTE-03-45 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-29, CTE-04-33, CTE-04-37, CTE-04-41, CTE-04-45 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-29, CTE-05-33, CTE-05-37, CTE-05-41, CTE-05-45 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-29, DATATYPES-01-33, DATATYPES-01-37, DATATYPES-01-41, DATATYPES-01-45 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-29, DATATYPES-02-33, DATATYPES-02-37, DATATYPES-02-41, DATATYPES-02-45 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-29, DATATYPES-03-33, DATATYPES-03-37, DATATYPES-03-41, DATATYPES-03-45 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-29, DATATYPES-04-33, DATATYPES-04-37, DATATYPES-04-41, DATATYPES-04-45 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-29, DATATYPES-05-33, DATATYPES-05-37, DATATYPES-05-41, DATATYPES-05-45 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-29, DATATYPES-06-33, DATATYPES-06-37, DATATYPES-06-41, DATATYPES-06-45 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-29, DATATYPES-07-33, DATATYPES-07-37, DATATYPES-07-41, DATATYPES-07-45 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-29, DATATYPES-08-33, DATATYPES-08-37, DATATYPES-08-41, DATATYPES-08-45 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-29, DATATYPES-09-33, DATATYPES-09-37, DATATYPES-09-41, DATATYPES-09-45 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-29, DATATYPES-10-33, DATATYPES-10-37, DATATYPES-10-41, DATATYPES-10-45 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-29, DATATYPES-11-33, DATATYPES-11-37, DATATYPES-11-41, DATATYPES-11-45 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-29, DATATYPES-12-33, DATATYPES-12-37, DATATYPES-12-41, DATATYPES-12-45 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-29, DATATYPES-13-33, DATATYPES-13-37, DATATYPES-13-41, DATATYPES-13-45 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-29, DATATYPES-14-33, DATATYPES-14-37, DATATYPES-14-41, DATATYPES-14-45 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-29, DATATYPES-15-33, DATATYPES-15-37, DATATYPES-15-41, DATATYPES-15-45 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-29, DATATYPES-16-33, DATATYPES-16-37, DATATYPES-16-41, DATATYPES-16-45 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-29, DATATYPES-17-33, DATATYPES-17-37, DATATYPES-17-41, DATATYPES-17-45 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-29, DATATYPES-18-33, DATATYPES-18-37, DATATYPES-18-41, DATATYPES-18-45 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-29, DATATYPES-19-33, DATATYPES-19-37, DATATYPES-19-41, DATATYPES-19-45 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-29, DATATYPES-20-33, DATATYPES-20-37, DATATYPES-20-41, DATATYPES-20-45 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-29, DATATYPES-21-33, DATATYPES-21-37, DATATYPES-21-41, DATATYPES-21-45 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-29, DATATYPES-22-33, DATATYPES-22-37, DATATYPES-22-41, DATATYPES-22-45 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-29, DATATYPES-23-33, DATATYPES-23-37, DATATYPES-23-41, DATATYPES-23-45 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-29, DATATYPES-24-33, DATATYPES-24-37, DATATYPES-24-41, DATATYPES-24-45 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-29, DATATYPES-25-33, DATATYPES-25-37, DATATYPES-25-41, DATATYPES-25-45 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-29, DATATYPES-26-33, DATATYPES-26-37, DATATYPES-26-41, DATATYPES-26-45 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-29, DATABASE_SCHEMA_USER-01-33, DATABASE_SCHEMA_USER-01-37, DATABASE_SCHEMA_USER-01-41, DATABASE_SCHEMA_USER-01-45 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-29, DATABASE_SCHEMA_USER-02-33, DATABASE_SCHEMA_USER-02-37, DATABASE_SCHEMA_USER-02-41, DATABASE_SCHEMA_USER-02-45 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-29, DATABASE_SCHEMA_USER-03-33, DATABASE_SCHEMA_USER-03-37, DATABASE_SCHEMA_USER-03-41, DATABASE_SCHEMA_USER-03-45 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-29, INTRODUCTION-01-33, INTRODUCTION-01-37, INTRODUCTION-01-41, INTRODUCTION-01-45 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-29, INTRODUCTION-02-33, INTRODUCTION-02-37, INTRODUCTION-02-41, INTRODUCTION-02-45 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-29, INTRODUCTION-03-33, INTRODUCTION-03-37, INTRODUCTION-03-41, INTRODUCTION-03-45 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-29, INTRODUCTION-04-33, INTRODUCTION-04-37, INTRODUCTION-04-41, INTRODUCTION-04-45 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-29, INTRODUCTION-05-33, INTRODUCTION-05-37, INTRODUCTION-05-41, INTRODUCTION-05-45 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-29, INTRODUCTION-06-33, INTRODUCTION-06-37, INTRODUCTION-06-41, INTRODUCTION-06-45 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-29, INTRODUCTION-07-33, INTRODUCTION-07-37, INTRODUCTION-07-41, INTRODUCTION-07-45 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-29, INTRODUCTION-08-33, INTRODUCTION-08-37, INTRODUCTION-08-41, INTRODUCTION-08-45 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-29, INTRODUCTION-09-33, INTRODUCTION-09-37, INTRODUCTION-09-41, INTRODUCTION-09-45 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-29, INTRODUCTION-10-33, INTRODUCTION-10-37, INTRODUCTION-10-41, INTRODUCTION-10-45 |

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
