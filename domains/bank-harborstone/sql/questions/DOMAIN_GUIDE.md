# Banking / Finance: connected SQL Server project

Trace transactions to accounts, customers and branches, then summarize lending exposure without multiplying loan balances by transaction counts.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Customers ||--o{ Accounts : "CustomerID"
    Branches ||--o{ Accounts : "BranchID"
    Accounts ||--o{ Transactions : "AccountID"
    Transactions |o--o{ Transactions : "ParentTransactionID"
    Customers ||--o{ Loans : "CustomerID"
    Accounts ||--o{ Loans : "AccountID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Branches → Customers → Accounts → Transactions → Loans**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Branches

**Branches** — A branch services many accounts.

| Column | Type | Requirement |
|---|---|---|
| BranchID | int | NOT NULL |
| BranchName | nvarchar(80) | NOT NULL |
| BranchCode | varchar(20) | NOT NULL |
| City | nvarchar(50) | NOT NULL |

Primary key: **BranchID**.
Unique business key: **BranchCode**.
Business rule: `LEN(LTRIM(RTRIM(BranchName))) > 0`.

### Customers

**Customers** — A customer may own several accounts and loans.

| Column | Type | Requirement |
|---|---|---|
| CustomerID | int | NOT NULL |
| CustomerName | nvarchar(80) | NOT NULL |
| Email | varchar(100) | NOT NULL |

Primary key: **CustomerID**.
Unique business key: **Email**.
Business rule: `LEN(LTRIM(RTRIM(CustomerName))) > 0`.

### Accounts

**Accounts** — Account-level servicing identity; each account belongs to one customer and branch.

| Column | Type | Requirement |
|---|---|---|
| AccountID | int | NOT NULL |
| AccountName | nvarchar(80) | NOT NULL |
| AccountNumber | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |
| CustomerID | int | NOT NULL |
| BranchID | int | NOT NULL |

Primary key: **AccountID**.
Unique business key: **AccountNumber**.
Business rule: `LEN(LTRIM(RTRIM(AccountName))) > 0`.
Foreign key: **Accounts.CustomerID → Customers.CustomerID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Accounts.BranchID → Branches.BranchID**. Use NO ACTION on delete/update; do not disable checking.

### Transactions

**Transactions** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| TransactionID | int | NOT NULL |
| AccountID | int | NOT NULL |
| Reference | nvarchar(80) | NOT NULL |
| TransactionType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Amount | decimal(12,2) | NULL |
| UnitCount | int | NOT NULL |
| TransactionDate | date | NOT NULL |
| PostedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentTransactionID | int | NULL |

Primary key: **TransactionID**.
Unique business key: **Reference**.
Business rule: `TransactionType IN ('A','B','C')`.
Business rule: `Status IN ('Open','Closed','Pending')`.
Business rule: `Amount >= 0`.
Business rule: `UnitCount > 0`.
Business rule: `ParentTransactionID IS NULL OR ParentTransactionID <> TransactionID`.
Business rule: `LEN(LTRIM(RTRIM(Reference))) > 0`.
Foreign key: **Transactions.AccountID → Accounts.AccountID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Transactions.ParentTransactionID → Transactions.TransactionID**. Use NO ACTION on delete/update; do not disable checking.

### Loans

**Loans** — Loans reference a borrower and a servicing account; the simplified model permits a different servicing-account owner.

| Column | Type | Requirement |
|---|---|---|
| LoanID | int | NOT NULL |
| CustomerID | int | NOT NULL |
| AccountID | int | NOT NULL |
| LoanReference | varchar(20) | NOT NULL |
| Principal | decimal(12,2) | NOT NULL |
| AnnualRate | decimal(5,2) | NOT NULL |

Primary key: **LoanID**.
Unique business key: **LoanReference**.
Business rule: `Principal > 0`.
Business rule: `AnnualRate BETWEEN 0 AND 100`.
Business rule: `LEN(LTRIM(RTRIM(LoanReference))) > 0`.
Foreign key: **Loans.CustomerID → Customers.CustomerID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Loans.AccountID → Accounts.AccountID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** five tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Branches

| BranchID | BranchName | BranchCode | City |
|---|---|---|---|
| `1` | `Branch 1` | `BR-1` | `Chicago` |
| `2` | `Branch 2` | `BR-2` | `Austin` |
| `3` | `Branch 3` | `BR-3` | `Boston` |
| `4` | `Branch 4` | `BR-4` | `Denver` |
| `5` | `Branch 5` | `BR-5` | `Seattle` |

### Sample rows: Customers

| CustomerID | CustomerName | Email |
|---|---|---|
| `1` | `Client 1` | `client1@example.test` |
| `2` | `Client 2` | `client2@example.test` |
| `3` | `Client 3` | `client3@example.test` |
| `4` | `Client 4` | `client4@example.test` |
| `5` | `Client 5` | `client5@example.test` |

### Sample rows: Accounts

| AccountID | AccountName | AccountNumber | Region | CustomerID | BranchID |
|---|---|---|---|---|---|
| `1` | `Accounts Alpha` | `ACC-1` | `North` | `1` | `1` |
| `2` | `Accounts Beta` | `ACC-2` | `South` | `2` | `2` |
| `3` | `Accounts Gamma` | `ACC-3` | `North` | `3` | `3` |
| `4` | `Accounts Delta` | `ACC-4` | `West` | `4` | `4` |
| `5` | `Accounts Unused` | `ACC-5` | `East` | `5` | `5` |

### Sample rows: Transactions

| TransactionID | AccountID | Reference | TransactionType | Status | Amount | UnitCount | TransactionDate | PostedAt | RecordedAt | Note | BackupNote | ParentTransactionID |
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

### Sample rows: Loans

| LoanID | CustomerID | AccountID | LoanReference | Principal | AnnualRate |
|---|---|---|---|---|---|
| `1` | `1` | `1` | `LN-1` | `10000` | `5` |
| `2` | `1` | `1` | `LN-2` | `5000` | `6` |
| `3` | `2` | `2` | `LN-3` | `20000` | `4` |
| `4` | `3` | `3` | `LN-4` | `15000` | `7` |
| `5` | `4` | `4` | `LN-5` | `8000` | `8` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../SQL/Excerises/BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-02, DDL-01-07, DDL-01-12, DDL-01-17, DDL-01-22 |
| [DDL](DDL.md) | Alter | DDL-02-02, DDL-02-07, DDL-02-12, DDL-02-17, DDL-02-22 |
| [DDL](DDL.md) | Drop | DDL-03-02, DDL-03-07, DDL-03-12, DDL-03-17, DDL-03-22 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-02, DATA_SETUP-01-07, DATA_SETUP-01-12, DATA_SETUP-01-17, DATA_SETUP-01-22 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-02, DATA_SETUP-02-07, DATA_SETUP-02-12, DATA_SETUP-02-17, DATA_SETUP-02-22 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-02, CONSTRAINTS-01-07, CONSTRAINTS-01-12, CONSTRAINTS-01-17, CONSTRAINTS-01-22 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-02, CONSTRAINTS-02-07, CONSTRAINTS-02-12, CONSTRAINTS-02-17, CONSTRAINTS-02-22 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-02, CONSTRAINTS-03-07, CONSTRAINTS-03-12, CONSTRAINTS-03-17, CONSTRAINTS-03-22 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-02, CONSTRAINTS-04-07, CONSTRAINTS-04-12, CONSTRAINTS-04-17, CONSTRAINTS-04-22 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-02, CONSTRAINTS-05-07, CONSTRAINTS-05-12, CONSTRAINTS-05-17, CONSTRAINTS-05-22 |
| [DML](DML.md) | Insert | DML-01-02, DML-01-07, DML-01-12, DML-01-17, DML-01-22 |
| [DML](DML.md) | Update | DML-02-02, DML-02-07, DML-02-12, DML-02-17, DML-02-22 |
| [DML](DML.md) | Delete | DML-03-02, DML-03-07, DML-03-12, DML-03-17, DML-03-22 |
| [DQL](DQL.md) | Select | DQL-01-02, DQL-01-07, DQL-01-12, DQL-01-17, DQL-01-22 |
| [DQL](DQL.md) | Where | DQL-02-02, DQL-02-07, DQL-02-12, DQL-02-17, DQL-02-22 |
| [DQL](DQL.md) | Group By | DQL-03-02, DQL-03-07, DQL-03-12, DQL-03-17, DQL-03-22 |
| [DQL](DQL.md) | Having | DQL-04-02, DQL-04-07, DQL-04-12, DQL-04-17, DQL-04-22 |
| [DQL](DQL.md) | Order By | DQL-05-02, DQL-05-07, DQL-05-12, DQL-05-17, DQL-05-22 |
| [DQL](DQL.md) | Top | DQL-06-02, DQL-06-07, DQL-06-12, DQL-06-17, DQL-06-22 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-02, OPERATORS-01-07, OPERATORS-01-12, OPERATORS-01-17, OPERATORS-01-22 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-02, OPERATORS-02-07, OPERATORS-02-12, OPERATORS-02-17, OPERATORS-02-22 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-02, OPERATORS-03-07, OPERATORS-03-12, OPERATORS-03-17, OPERATORS-03-22 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-02, OPERATORS-04-07, OPERATORS-04-12, OPERATORS-04-17, OPERATORS-04-22 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-02, OPERATORS-05-07, OPERATORS-05-12, OPERATORS-05-17, OPERATORS-05-22 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-02, OPERATORS-06-07, OPERATORS-06-12, OPERATORS-06-17, OPERATORS-06-22 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-02, OPERATORS-07-07, OPERATORS-07-12, OPERATORS-07-17, OPERATORS-07-22 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-02, OPERATORS-08-07, OPERATORS-08-12, OPERATORS-08-17, OPERATORS-08-22 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-02, OPERATORS-09-07, OPERATORS-09-12, OPERATORS-09-17, OPERATORS-09-22 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-02, OPERATORS-10-07, OPERATORS-10-12, OPERATORS-10-17, OPERATORS-10-22 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-02, OPERATORS-11-07, OPERATORS-11-12, OPERATORS-11-17, OPERATORS-11-22 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-02, OPERATORS-12-07, OPERATORS-12-12, OPERATORS-12-17, OPERATORS-12-22 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-02, OPERATORS-13-07, OPERATORS-13-12, OPERATORS-13-17, OPERATORS-13-22 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-02, JOINS-01-07, JOINS-01-12, JOINS-01-17, JOINS-01-22 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-02, JOINS-02-07, JOINS-02-12, JOINS-02-17, JOINS-02-22 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-02, JOINS-03-07, JOINS-03-12, JOINS-03-17, JOINS-03-22 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-02, JOINS-04-07, JOINS-04-12, JOINS-04-17, JOINS-04-22 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-02, JOINS-05-07, JOINS-05-12, JOINS-05-17, JOINS-05-22 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-02, SET_OPERATIONS-01-07, SET_OPERATIONS-01-12, SET_OPERATIONS-01-17, SET_OPERATIONS-01-22 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-02, SET_OPERATIONS-02-07, SET_OPERATIONS-02-12, SET_OPERATIONS-02-17, SET_OPERATIONS-02-22 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-02, SET_OPERATIONS-03-07, SET_OPERATIONS-03-12, SET_OPERATIONS-03-17, SET_OPERATIONS-03-22 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-02, SET_OPERATIONS-04-07, SET_OPERATIONS-04-12, SET_OPERATIONS-04-17, SET_OPERATIONS-04-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-02, STRING_FUNCTIONS-01-07, STRING_FUNCTIONS-01-12, STRING_FUNCTIONS-01-17, STRING_FUNCTIONS-01-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-02, STRING_FUNCTIONS-02-07, STRING_FUNCTIONS-02-12, STRING_FUNCTIONS-02-17, STRING_FUNCTIONS-02-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-02, STRING_FUNCTIONS-03-07, STRING_FUNCTIONS-03-12, STRING_FUNCTIONS-03-17, STRING_FUNCTIONS-03-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-02, STRING_FUNCTIONS-04-07, STRING_FUNCTIONS-04-12, STRING_FUNCTIONS-04-17, STRING_FUNCTIONS-04-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-02, STRING_FUNCTIONS-05-07, STRING_FUNCTIONS-05-12, STRING_FUNCTIONS-05-17, STRING_FUNCTIONS-05-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-02, STRING_FUNCTIONS-06-07, STRING_FUNCTIONS-06-12, STRING_FUNCTIONS-06-17, STRING_FUNCTIONS-06-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-02, STRING_FUNCTIONS-07-07, STRING_FUNCTIONS-07-12, STRING_FUNCTIONS-07-17, STRING_FUNCTIONS-07-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-02, STRING_FUNCTIONS-08-07, STRING_FUNCTIONS-08-12, STRING_FUNCTIONS-08-17, STRING_FUNCTIONS-08-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-02, STRING_FUNCTIONS-09-07, STRING_FUNCTIONS-09-12, STRING_FUNCTIONS-09-17, STRING_FUNCTIONS-09-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-02, STRING_FUNCTIONS-10-07, STRING_FUNCTIONS-10-12, STRING_FUNCTIONS-10-17, STRING_FUNCTIONS-10-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-02, STRING_FUNCTIONS-11-07, STRING_FUNCTIONS-11-12, STRING_FUNCTIONS-11-17, STRING_FUNCTIONS-11-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-02, STRING_FUNCTIONS-12-07, STRING_FUNCTIONS-12-12, STRING_FUNCTIONS-12-17, STRING_FUNCTIONS-12-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-02, STRING_FUNCTIONS-13-07, STRING_FUNCTIONS-13-12, STRING_FUNCTIONS-13-17, STRING_FUNCTIONS-13-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-02, STRING_FUNCTIONS-14-07, STRING_FUNCTIONS-14-12, STRING_FUNCTIONS-14-17, STRING_FUNCTIONS-14-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-02, STRING_FUNCTIONS-15-07, STRING_FUNCTIONS-15-12, STRING_FUNCTIONS-15-17, STRING_FUNCTIONS-15-22 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-02, STRING_FUNCTIONS-16-07, STRING_FUNCTIONS-16-12, STRING_FUNCTIONS-16-17, STRING_FUNCTIONS-16-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-02, DATE_FUNCTIONS-01-07, DATE_FUNCTIONS-01-12, DATE_FUNCTIONS-01-17, DATE_FUNCTIONS-01-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-02, DATE_FUNCTIONS-02-07, DATE_FUNCTIONS-02-12, DATE_FUNCTIONS-02-17, DATE_FUNCTIONS-02-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-02, DATE_FUNCTIONS-03-07, DATE_FUNCTIONS-03-12, DATE_FUNCTIONS-03-17, DATE_FUNCTIONS-03-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-02, DATE_FUNCTIONS-04-07, DATE_FUNCTIONS-04-12, DATE_FUNCTIONS-04-17, DATE_FUNCTIONS-04-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-02, DATE_FUNCTIONS-05-07, DATE_FUNCTIONS-05-12, DATE_FUNCTIONS-05-17, DATE_FUNCTIONS-05-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-02, DATE_FUNCTIONS-06-07, DATE_FUNCTIONS-06-12, DATE_FUNCTIONS-06-17, DATE_FUNCTIONS-06-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-02, DATE_FUNCTIONS-07-07, DATE_FUNCTIONS-07-12, DATE_FUNCTIONS-07-17, DATE_FUNCTIONS-07-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-02, DATE_FUNCTIONS-08-07, DATE_FUNCTIONS-08-12, DATE_FUNCTIONS-08-17, DATE_FUNCTIONS-08-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-02, DATE_FUNCTIONS-09-07, DATE_FUNCTIONS-09-12, DATE_FUNCTIONS-09-17, DATE_FUNCTIONS-09-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-02, DATE_FUNCTIONS-10-07, DATE_FUNCTIONS-10-12, DATE_FUNCTIONS-10-17, DATE_FUNCTIONS-10-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-02, DATE_FUNCTIONS-11-07, DATE_FUNCTIONS-11-12, DATE_FUNCTIONS-11-17, DATE_FUNCTIONS-11-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-02, DATE_FUNCTIONS-12-07, DATE_FUNCTIONS-12-12, DATE_FUNCTIONS-12-17, DATE_FUNCTIONS-12-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-02, DATE_FUNCTIONS-13-07, DATE_FUNCTIONS-13-12, DATE_FUNCTIONS-13-17, DATE_FUNCTIONS-13-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-02, DATE_FUNCTIONS-14-07, DATE_FUNCTIONS-14-12, DATE_FUNCTIONS-14-17, DATE_FUNCTIONS-14-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-02, DATE_FUNCTIONS-15-07, DATE_FUNCTIONS-15-12, DATE_FUNCTIONS-15-17, DATE_FUNCTIONS-15-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-02, DATE_FUNCTIONS-16-07, DATE_FUNCTIONS-16-12, DATE_FUNCTIONS-16-17, DATE_FUNCTIONS-16-22 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-02, DATE_FUNCTIONS-17-07, DATE_FUNCTIONS-17-12, DATE_FUNCTIONS-17-17, DATE_FUNCTIONS-17-22 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-02, AGGREGATES-01-07, AGGREGATES-01-12, AGGREGATES-01-17, AGGREGATES-01-22 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-02, AGGREGATES-02-07, AGGREGATES-02-12, AGGREGATES-02-17, AGGREGATES-02-22 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-02, AGGREGATES-03-07, AGGREGATES-03-12, AGGREGATES-03-17, AGGREGATES-03-22 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-02, AGGREGATES-04-07, AGGREGATES-04-12, AGGREGATES-04-17, AGGREGATES-04-22 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-02, AGGREGATES-05-07, AGGREGATES-05-12, AGGREGATES-05-17, AGGREGATES-05-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-02, ANALYTICAL_FUNCTIONS-01-07, ANALYTICAL_FUNCTIONS-01-12, ANALYTICAL_FUNCTIONS-01-17, ANALYTICAL_FUNCTIONS-01-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-02, ANALYTICAL_FUNCTIONS-02-07, ANALYTICAL_FUNCTIONS-02-12, ANALYTICAL_FUNCTIONS-02-17, ANALYTICAL_FUNCTIONS-02-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-02, ANALYTICAL_FUNCTIONS-03-07, ANALYTICAL_FUNCTIONS-03-12, ANALYTICAL_FUNCTIONS-03-17, ANALYTICAL_FUNCTIONS-03-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-02, ANALYTICAL_FUNCTIONS-04-07, ANALYTICAL_FUNCTIONS-04-12, ANALYTICAL_FUNCTIONS-04-17, ANALYTICAL_FUNCTIONS-04-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-02, ANALYTICAL_FUNCTIONS-05-07, ANALYTICAL_FUNCTIONS-05-12, ANALYTICAL_FUNCTIONS-05-17, ANALYTICAL_FUNCTIONS-05-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-02, ANALYTICAL_FUNCTIONS-06-07, ANALYTICAL_FUNCTIONS-06-12, ANALYTICAL_FUNCTIONS-06-17, ANALYTICAL_FUNCTIONS-06-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-02, ANALYTICAL_FUNCTIONS-07-07, ANALYTICAL_FUNCTIONS-07-12, ANALYTICAL_FUNCTIONS-07-17, ANALYTICAL_FUNCTIONS-07-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-02, ANALYTICAL_FUNCTIONS-08-07, ANALYTICAL_FUNCTIONS-08-12, ANALYTICAL_FUNCTIONS-08-17, ANALYTICAL_FUNCTIONS-08-22 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-02, ANALYTICAL_FUNCTIONS-09-07, ANALYTICAL_FUNCTIONS-09-12, ANALYTICAL_FUNCTIONS-09-17, ANALYTICAL_FUNCTIONS-09-22 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-02, CTE-01-07, CTE-01-12, CTE-01-17, CTE-01-22 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-02, CTE-02-07, CTE-02-12, CTE-02-17, CTE-02-22 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-02, CTE-03-07, CTE-03-12, CTE-03-17, CTE-03-22 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-02, CTE-04-07, CTE-04-12, CTE-04-17, CTE-04-22 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-02, CTE-05-07, CTE-05-12, CTE-05-17, CTE-05-22 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-02, DATATYPES-01-07, DATATYPES-01-12, DATATYPES-01-17, DATATYPES-01-22 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-02, DATATYPES-02-07, DATATYPES-02-12, DATATYPES-02-17, DATATYPES-02-22 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-02, DATATYPES-03-07, DATATYPES-03-12, DATATYPES-03-17, DATATYPES-03-22 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-02, DATATYPES-04-07, DATATYPES-04-12, DATATYPES-04-17, DATATYPES-04-22 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-02, DATATYPES-05-07, DATATYPES-05-12, DATATYPES-05-17, DATATYPES-05-22 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-02, DATATYPES-06-07, DATATYPES-06-12, DATATYPES-06-17, DATATYPES-06-22 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-02, DATATYPES-07-07, DATATYPES-07-12, DATATYPES-07-17, DATATYPES-07-22 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-02, DATATYPES-08-07, DATATYPES-08-12, DATATYPES-08-17, DATATYPES-08-22 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-02, DATATYPES-09-07, DATATYPES-09-12, DATATYPES-09-17, DATATYPES-09-22 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-02, DATATYPES-10-07, DATATYPES-10-12, DATATYPES-10-17, DATATYPES-10-22 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-02, DATATYPES-11-07, DATATYPES-11-12, DATATYPES-11-17, DATATYPES-11-22 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-02, DATATYPES-12-07, DATATYPES-12-12, DATATYPES-12-17, DATATYPES-12-22 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-02, DATATYPES-13-07, DATATYPES-13-12, DATATYPES-13-17, DATATYPES-13-22 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-02, DATATYPES-14-07, DATATYPES-14-12, DATATYPES-14-17, DATATYPES-14-22 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-02, DATATYPES-15-07, DATATYPES-15-12, DATATYPES-15-17, DATATYPES-15-22 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-02, DATATYPES-16-07, DATATYPES-16-12, DATATYPES-16-17, DATATYPES-16-22 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-02, DATATYPES-17-07, DATATYPES-17-12, DATATYPES-17-17, DATATYPES-17-22 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-02, DATATYPES-18-07, DATATYPES-18-12, DATATYPES-18-17, DATATYPES-18-22 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-02, DATATYPES-19-07, DATATYPES-19-12, DATATYPES-19-17, DATATYPES-19-22 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-02, DATATYPES-20-07, DATATYPES-20-12, DATATYPES-20-17, DATATYPES-20-22 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-02, DATATYPES-21-07, DATATYPES-21-12, DATATYPES-21-17, DATATYPES-21-22 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-02, DATATYPES-22-07, DATATYPES-22-12, DATATYPES-22-17, DATATYPES-22-22 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-02, DATATYPES-23-07, DATATYPES-23-12, DATATYPES-23-17, DATATYPES-23-22 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-02, DATATYPES-24-07, DATATYPES-24-12, DATATYPES-24-17, DATATYPES-24-22 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-02, DATATYPES-25-07, DATATYPES-25-12, DATATYPES-25-17, DATATYPES-25-22 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-02, DATATYPES-26-07, DATATYPES-26-12, DATATYPES-26-17, DATATYPES-26-22 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-02, DATABASE_SCHEMA_USER-01-07, DATABASE_SCHEMA_USER-01-12, DATABASE_SCHEMA_USER-01-17, DATABASE_SCHEMA_USER-01-22 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-02, DATABASE_SCHEMA_USER-02-07, DATABASE_SCHEMA_USER-02-12, DATABASE_SCHEMA_USER-02-17, DATABASE_SCHEMA_USER-02-22 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-02, DATABASE_SCHEMA_USER-03-07, DATABASE_SCHEMA_USER-03-12, DATABASE_SCHEMA_USER-03-17, DATABASE_SCHEMA_USER-03-22 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-02, INTRODUCTION-01-07, INTRODUCTION-01-12, INTRODUCTION-01-17, INTRODUCTION-01-22 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-02, INTRODUCTION-02-07, INTRODUCTION-02-12, INTRODUCTION-02-17, INTRODUCTION-02-22 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-02, INTRODUCTION-03-07, INTRODUCTION-03-12, INTRODUCTION-03-17, INTRODUCTION-03-22 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-02, INTRODUCTION-04-07, INTRODUCTION-04-12, INTRODUCTION-04-17, INTRODUCTION-04-22 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-02, INTRODUCTION-05-07, INTRODUCTION-05-12, INTRODUCTION-05-17, INTRODUCTION-05-22 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-02, INTRODUCTION-06-07, INTRODUCTION-06-12, INTRODUCTION-06-17, INTRODUCTION-06-22 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-02, INTRODUCTION-07-07, INTRODUCTION-07-12, INTRODUCTION-07-17, INTRODUCTION-07-22 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-02, INTRODUCTION-08-07, INTRODUCTION-08-12, INTRODUCTION-08-17, INTRODUCTION-08-22 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-02, INTRODUCTION-09-07, INTRODUCTION-09-12, INTRODUCTION-09-17, INTRODUCTION-09-22 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-02, INTRODUCTION-10-07, INTRODUCTION-10-12, INTRODUCTION-10-17, INTRODUCTION-10-22 |

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
