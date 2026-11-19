# Retail Logistics: connected SQL Server project

Follow customer shipments through carriers, parcels and tracking events. Find missing scans and late deliveries without multiplying freight charges.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Customers ||--o{ Shipments : "CustomerID"
    Shipments |o--o{ Shipments : "ParentShipmentID"
    Carriers ||--o{ Shipments : "CarrierID"
    Shipments ||--o{ ShipmentPackages : "ShipmentID"
    ShipmentPackages ||--o{ TrackingEvents : "PackageID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Customers → Carriers → Shipments → ShipmentPackages → TrackingEvents**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Customers

**Customers** — Customers request retail deliveries; one customer may have many shipments.

| Column | Type | Requirement |
|---|---|---|
| CustomerID | int | NOT NULL |
| CustomerName | nvarchar(80) | NOT NULL |
| CustomerCode | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **CustomerID**.
Unique business key: **CustomerCode**.
Business rule: `LEN(LTRIM(RTRIM(CustomerName))) > 0`.

### Carriers

**Carriers** — Delivery partners; each shipment is assigned to one carrier.

| Column | Type | Requirement |
|---|---|---|
| CarrierID | int | NOT NULL |
| CarrierName | nvarchar(80) | NOT NULL |
| CarrierCode | varchar(20) | NOT NULL |
| ServiceLevel | varchar(20) | NOT NULL |

Primary key: **CarrierID**.
Unique business key: **CarrierCode**.
Business rule: `LEN(LTRIM(RTRIM(CarrierName))) > 0`.

### Shipments

**Shipments** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| ShipmentID | int | NOT NULL |
| CustomerID | int | NOT NULL |
| ShipmentReference | nvarchar(80) | NOT NULL |
| ShipmentCategory | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| FreightCharge | decimal(12,2) | NULL |
| DeclaredPackages | int | NOT NULL |
| ShipDate | date | NOT NULL |
| DispatchedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentShipmentID | int | NULL |
| CarrierID | int | NOT NULL |

Primary key: **ShipmentID**.
Unique business key: **ShipmentReference**.
Business rule: `ShipmentCategory IN ('A','B','C')`.
Business rule: `Status IN ('Open','Closed','Pending')`.
Business rule: `FreightCharge >= 0`.
Business rule: `DeclaredPackages > 0`.
Business rule: `ParentShipmentID IS NULL OR ParentShipmentID <> ShipmentID`.
Business rule: `LEN(LTRIM(RTRIM(ShipmentReference))) > 0`.
Foreign key: **Shipments.CustomerID → Customers.CustomerID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Shipments.ParentShipmentID → Shipments.ShipmentID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Shipments.CarrierID → Carriers.CarrierID**. Use NO ACTION on delete/update; do not disable checking.

### ShipmentPackages

**ShipmentPackages** — Physical parcels with individual tracking numbers and promised delivery dates.

| Column | Type | Requirement |
|---|---|---|
| PackageID | int | NOT NULL |
| ShipmentID | int | NOT NULL |
| TrackingNumber | varchar(20) | NOT NULL |
| WeightKg | decimal(12,2) | NOT NULL |
| PromisedDate | date | NOT NULL |

Primary key: **PackageID**.
Unique business key: **TrackingNumber**.
Business rule: `WeightKg > 0`.
Business rule: `LEN(LTRIM(RTRIM(TrackingNumber))) > 0`.
Foreign key: **ShipmentPackages.ShipmentID → Shipments.ShipmentID**. Use NO ACTION on delete/update; do not disable checking.

### TrackingEvents

**TrackingEvents** — Append-only package scan history; select the latest scan rather than counting it as another package.

| Column | Type | Requirement |
|---|---|---|
| TrackingEventID | int | NOT NULL |
| PackageID | int | NOT NULL |
| ScanReference | varchar(20) | NOT NULL |
| EventStatus | varchar(20) | NOT NULL |
| ScanTime | datetime2(3) | NOT NULL |
| LocationName | nvarchar(80) | NOT NULL |

Primary key: **TrackingEventID**.
Unique business key: **ScanReference**.
Business rule: `EventStatus IN ('PickedUp','InTransit','Delivered')`.
Business rule: `LEN(LTRIM(RTRIM(ScanReference))) > 0`.
Foreign key: **TrackingEvents.PackageID → ShipmentPackages.PackageID**. Use NO ACTION on delete/update; do not disable checking.

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

### Sample rows: Carriers

| CarrierID | CarrierName | CarrierCode | ServiceLevel |
|---|---|---|---|
| `1` | `Logistics carrier 1` | `LOG-1` | `Express` |
| `2` | `Logistics carrier 2` | `LOG-2` | `Standard` |
| `3` | `Logistics carrier 3` | `LOG-3` | `Express` |
| `4` | `Logistics carrier 4` | `LOG-4` | `Standard` |
| `5` | `Logistics carrier 5` | `LOG-5` | `Express` |

### Sample rows: Shipments

| ShipmentID | CustomerID | ShipmentReference | ShipmentCategory | Status | FreightCharge | DeclaredPackages | ShipDate | DispatchedAt | RecordedAt | Note | BackupNote | ParentShipmentID | CarrierID |
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

### Sample rows: ShipmentPackages

| PackageID | ShipmentID | TrackingNumber | WeightKg | PromisedDate |
|---|---|---|---|---|
| `1` | `1` | `TRK-1` | `2` | `20240103` |
| `2` | `1` | `TRK-2` | `3` | `20240103` |
| `3` | `2` | `TRK-3` | `1` | `20240104` |
| `4` | `3` | `TRK-4` | `4` | `20240104` |
| `5` | `6` | `TRK-5` | `2` | `20240212` |

### Sample rows: TrackingEvents

| TrackingEventID | PackageID | ScanReference | EventStatus | ScanTime | LocationName |
|---|---|---|---|---|---|
| `1` | `1` | `SCAN-1` | `PickedUp` | `2024-01-01T13:00:00` | `Origin hub` |
| `2` | `1` | `SCAN-2` | `Delivered` | `2024-01-03T10:00:00` | `Customer address` |
| `3` | `2` | `SCAN-3` | `InTransit` | `2024-01-02T09:00:00` | `Regional hub` |
| `4` | `3` | `SCAN-4` | `Delivered` | `2024-01-05T11:00:00` | `Customer address` |
| `5` | `4` | `SCAN-5` | `PickedUp` | `2024-01-03T08:00:00` | `Origin hub` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../SQL/Excerises/BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-27, DDL-01-31, DDL-01-35, DDL-01-39, DDL-01-43 |
| [DDL](DDL.md) | Alter | DDL-02-27, DDL-02-31, DDL-02-35, DDL-02-39, DDL-02-43 |
| [DDL](DDL.md) | Drop | DDL-03-27, DDL-03-31, DDL-03-35, DDL-03-39, DDL-03-43 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-27, DATA_SETUP-01-31, DATA_SETUP-01-35, DATA_SETUP-01-39, DATA_SETUP-01-43 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-27, DATA_SETUP-02-31, DATA_SETUP-02-35, DATA_SETUP-02-39, DATA_SETUP-02-43 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-27, CONSTRAINTS-01-31, CONSTRAINTS-01-35, CONSTRAINTS-01-39, CONSTRAINTS-01-43 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-27, CONSTRAINTS-02-31, CONSTRAINTS-02-35, CONSTRAINTS-02-39, CONSTRAINTS-02-43 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-27, CONSTRAINTS-03-31, CONSTRAINTS-03-35, CONSTRAINTS-03-39, CONSTRAINTS-03-43 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-27, CONSTRAINTS-04-31, CONSTRAINTS-04-35, CONSTRAINTS-04-39, CONSTRAINTS-04-43 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-27, CONSTRAINTS-05-31, CONSTRAINTS-05-35, CONSTRAINTS-05-39, CONSTRAINTS-05-43 |
| [DML](DML.md) | Insert | DML-01-27, DML-01-31, DML-01-35, DML-01-39, DML-01-43 |
| [DML](DML.md) | Update | DML-02-27, DML-02-31, DML-02-35, DML-02-39, DML-02-43 |
| [DML](DML.md) | Delete | DML-03-27, DML-03-31, DML-03-35, DML-03-39, DML-03-43 |
| [DQL](DQL.md) | Select | DQL-01-27, DQL-01-31, DQL-01-35, DQL-01-39, DQL-01-43 |
| [DQL](DQL.md) | Where | DQL-02-27, DQL-02-31, DQL-02-35, DQL-02-39, DQL-02-43 |
| [DQL](DQL.md) | Group By | DQL-03-27, DQL-03-31, DQL-03-35, DQL-03-39, DQL-03-43 |
| [DQL](DQL.md) | Having | DQL-04-27, DQL-04-31, DQL-04-35, DQL-04-39, DQL-04-43 |
| [DQL](DQL.md) | Order By | DQL-05-27, DQL-05-31, DQL-05-35, DQL-05-39, DQL-05-43 |
| [DQL](DQL.md) | Top | DQL-06-27, DQL-06-31, DQL-06-35, DQL-06-39, DQL-06-43 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-27, OPERATORS-01-31, OPERATORS-01-35, OPERATORS-01-39, OPERATORS-01-43 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-27, OPERATORS-02-31, OPERATORS-02-35, OPERATORS-02-39, OPERATORS-02-43 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-27, OPERATORS-03-31, OPERATORS-03-35, OPERATORS-03-39, OPERATORS-03-43 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-27, OPERATORS-04-31, OPERATORS-04-35, OPERATORS-04-39, OPERATORS-04-43 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-27, OPERATORS-05-31, OPERATORS-05-35, OPERATORS-05-39, OPERATORS-05-43 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-27, OPERATORS-06-31, OPERATORS-06-35, OPERATORS-06-39, OPERATORS-06-43 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-27, OPERATORS-07-31, OPERATORS-07-35, OPERATORS-07-39, OPERATORS-07-43 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-27, OPERATORS-08-31, OPERATORS-08-35, OPERATORS-08-39, OPERATORS-08-43 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-27, OPERATORS-09-31, OPERATORS-09-35, OPERATORS-09-39, OPERATORS-09-43 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-27, OPERATORS-10-31, OPERATORS-10-35, OPERATORS-10-39, OPERATORS-10-43 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-27, OPERATORS-11-31, OPERATORS-11-35, OPERATORS-11-39, OPERATORS-11-43 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-27, OPERATORS-12-31, OPERATORS-12-35, OPERATORS-12-39, OPERATORS-12-43 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-27, OPERATORS-13-31, OPERATORS-13-35, OPERATORS-13-39, OPERATORS-13-43 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-27, JOINS-01-31, JOINS-01-35, JOINS-01-39, JOINS-01-43 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-27, JOINS-02-31, JOINS-02-35, JOINS-02-39, JOINS-02-43 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-27, JOINS-03-31, JOINS-03-35, JOINS-03-39, JOINS-03-43 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-27, JOINS-04-31, JOINS-04-35, JOINS-04-39, JOINS-04-43 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-27, JOINS-05-31, JOINS-05-35, JOINS-05-39, JOINS-05-43 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-27, SET_OPERATIONS-01-31, SET_OPERATIONS-01-35, SET_OPERATIONS-01-39, SET_OPERATIONS-01-43 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-27, SET_OPERATIONS-02-31, SET_OPERATIONS-02-35, SET_OPERATIONS-02-39, SET_OPERATIONS-02-43 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-27, SET_OPERATIONS-03-31, SET_OPERATIONS-03-35, SET_OPERATIONS-03-39, SET_OPERATIONS-03-43 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-27, SET_OPERATIONS-04-31, SET_OPERATIONS-04-35, SET_OPERATIONS-04-39, SET_OPERATIONS-04-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-27, STRING_FUNCTIONS-01-31, STRING_FUNCTIONS-01-35, STRING_FUNCTIONS-01-39, STRING_FUNCTIONS-01-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-27, STRING_FUNCTIONS-02-31, STRING_FUNCTIONS-02-35, STRING_FUNCTIONS-02-39, STRING_FUNCTIONS-02-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-27, STRING_FUNCTIONS-03-31, STRING_FUNCTIONS-03-35, STRING_FUNCTIONS-03-39, STRING_FUNCTIONS-03-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-27, STRING_FUNCTIONS-04-31, STRING_FUNCTIONS-04-35, STRING_FUNCTIONS-04-39, STRING_FUNCTIONS-04-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-27, STRING_FUNCTIONS-05-31, STRING_FUNCTIONS-05-35, STRING_FUNCTIONS-05-39, STRING_FUNCTIONS-05-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-27, STRING_FUNCTIONS-06-31, STRING_FUNCTIONS-06-35, STRING_FUNCTIONS-06-39, STRING_FUNCTIONS-06-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-27, STRING_FUNCTIONS-07-31, STRING_FUNCTIONS-07-35, STRING_FUNCTIONS-07-39, STRING_FUNCTIONS-07-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-27, STRING_FUNCTIONS-08-31, STRING_FUNCTIONS-08-35, STRING_FUNCTIONS-08-39, STRING_FUNCTIONS-08-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-27, STRING_FUNCTIONS-09-31, STRING_FUNCTIONS-09-35, STRING_FUNCTIONS-09-39, STRING_FUNCTIONS-09-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-27, STRING_FUNCTIONS-10-31, STRING_FUNCTIONS-10-35, STRING_FUNCTIONS-10-39, STRING_FUNCTIONS-10-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-27, STRING_FUNCTIONS-11-31, STRING_FUNCTIONS-11-35, STRING_FUNCTIONS-11-39, STRING_FUNCTIONS-11-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-27, STRING_FUNCTIONS-12-31, STRING_FUNCTIONS-12-35, STRING_FUNCTIONS-12-39, STRING_FUNCTIONS-12-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-27, STRING_FUNCTIONS-13-31, STRING_FUNCTIONS-13-35, STRING_FUNCTIONS-13-39, STRING_FUNCTIONS-13-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-27, STRING_FUNCTIONS-14-31, STRING_FUNCTIONS-14-35, STRING_FUNCTIONS-14-39, STRING_FUNCTIONS-14-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-27, STRING_FUNCTIONS-15-31, STRING_FUNCTIONS-15-35, STRING_FUNCTIONS-15-39, STRING_FUNCTIONS-15-43 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-27, STRING_FUNCTIONS-16-31, STRING_FUNCTIONS-16-35, STRING_FUNCTIONS-16-39, STRING_FUNCTIONS-16-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-27, DATE_FUNCTIONS-01-31, DATE_FUNCTIONS-01-35, DATE_FUNCTIONS-01-39, DATE_FUNCTIONS-01-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-27, DATE_FUNCTIONS-02-31, DATE_FUNCTIONS-02-35, DATE_FUNCTIONS-02-39, DATE_FUNCTIONS-02-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-27, DATE_FUNCTIONS-03-31, DATE_FUNCTIONS-03-35, DATE_FUNCTIONS-03-39, DATE_FUNCTIONS-03-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-27, DATE_FUNCTIONS-04-31, DATE_FUNCTIONS-04-35, DATE_FUNCTIONS-04-39, DATE_FUNCTIONS-04-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-27, DATE_FUNCTIONS-05-31, DATE_FUNCTIONS-05-35, DATE_FUNCTIONS-05-39, DATE_FUNCTIONS-05-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-27, DATE_FUNCTIONS-06-31, DATE_FUNCTIONS-06-35, DATE_FUNCTIONS-06-39, DATE_FUNCTIONS-06-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-27, DATE_FUNCTIONS-07-31, DATE_FUNCTIONS-07-35, DATE_FUNCTIONS-07-39, DATE_FUNCTIONS-07-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-27, DATE_FUNCTIONS-08-31, DATE_FUNCTIONS-08-35, DATE_FUNCTIONS-08-39, DATE_FUNCTIONS-08-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-27, DATE_FUNCTIONS-09-31, DATE_FUNCTIONS-09-35, DATE_FUNCTIONS-09-39, DATE_FUNCTIONS-09-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-27, DATE_FUNCTIONS-10-31, DATE_FUNCTIONS-10-35, DATE_FUNCTIONS-10-39, DATE_FUNCTIONS-10-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-27, DATE_FUNCTIONS-11-31, DATE_FUNCTIONS-11-35, DATE_FUNCTIONS-11-39, DATE_FUNCTIONS-11-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-27, DATE_FUNCTIONS-12-31, DATE_FUNCTIONS-12-35, DATE_FUNCTIONS-12-39, DATE_FUNCTIONS-12-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-27, DATE_FUNCTIONS-13-31, DATE_FUNCTIONS-13-35, DATE_FUNCTIONS-13-39, DATE_FUNCTIONS-13-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-27, DATE_FUNCTIONS-14-31, DATE_FUNCTIONS-14-35, DATE_FUNCTIONS-14-39, DATE_FUNCTIONS-14-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-27, DATE_FUNCTIONS-15-31, DATE_FUNCTIONS-15-35, DATE_FUNCTIONS-15-39, DATE_FUNCTIONS-15-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-27, DATE_FUNCTIONS-16-31, DATE_FUNCTIONS-16-35, DATE_FUNCTIONS-16-39, DATE_FUNCTIONS-16-43 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-27, DATE_FUNCTIONS-17-31, DATE_FUNCTIONS-17-35, DATE_FUNCTIONS-17-39, DATE_FUNCTIONS-17-43 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-27, AGGREGATES-01-31, AGGREGATES-01-35, AGGREGATES-01-39, AGGREGATES-01-43 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-27, AGGREGATES-02-31, AGGREGATES-02-35, AGGREGATES-02-39, AGGREGATES-02-43 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-27, AGGREGATES-03-31, AGGREGATES-03-35, AGGREGATES-03-39, AGGREGATES-03-43 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-27, AGGREGATES-04-31, AGGREGATES-04-35, AGGREGATES-04-39, AGGREGATES-04-43 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-27, AGGREGATES-05-31, AGGREGATES-05-35, AGGREGATES-05-39, AGGREGATES-05-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-27, ANALYTICAL_FUNCTIONS-01-31, ANALYTICAL_FUNCTIONS-01-35, ANALYTICAL_FUNCTIONS-01-39, ANALYTICAL_FUNCTIONS-01-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-27, ANALYTICAL_FUNCTIONS-02-31, ANALYTICAL_FUNCTIONS-02-35, ANALYTICAL_FUNCTIONS-02-39, ANALYTICAL_FUNCTIONS-02-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-27, ANALYTICAL_FUNCTIONS-03-31, ANALYTICAL_FUNCTIONS-03-35, ANALYTICAL_FUNCTIONS-03-39, ANALYTICAL_FUNCTIONS-03-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-27, ANALYTICAL_FUNCTIONS-04-31, ANALYTICAL_FUNCTIONS-04-35, ANALYTICAL_FUNCTIONS-04-39, ANALYTICAL_FUNCTIONS-04-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-27, ANALYTICAL_FUNCTIONS-05-31, ANALYTICAL_FUNCTIONS-05-35, ANALYTICAL_FUNCTIONS-05-39, ANALYTICAL_FUNCTIONS-05-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-27, ANALYTICAL_FUNCTIONS-06-31, ANALYTICAL_FUNCTIONS-06-35, ANALYTICAL_FUNCTIONS-06-39, ANALYTICAL_FUNCTIONS-06-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-27, ANALYTICAL_FUNCTIONS-07-31, ANALYTICAL_FUNCTIONS-07-35, ANALYTICAL_FUNCTIONS-07-39, ANALYTICAL_FUNCTIONS-07-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-27, ANALYTICAL_FUNCTIONS-08-31, ANALYTICAL_FUNCTIONS-08-35, ANALYTICAL_FUNCTIONS-08-39, ANALYTICAL_FUNCTIONS-08-43 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-27, ANALYTICAL_FUNCTIONS-09-31, ANALYTICAL_FUNCTIONS-09-35, ANALYTICAL_FUNCTIONS-09-39, ANALYTICAL_FUNCTIONS-09-43 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-27, CTE-01-31, CTE-01-35, CTE-01-39, CTE-01-43 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-27, CTE-02-31, CTE-02-35, CTE-02-39, CTE-02-43 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-27, CTE-03-31, CTE-03-35, CTE-03-39, CTE-03-43 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-27, CTE-04-31, CTE-04-35, CTE-04-39, CTE-04-43 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-27, CTE-05-31, CTE-05-35, CTE-05-39, CTE-05-43 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-27, DATATYPES-01-31, DATATYPES-01-35, DATATYPES-01-39, DATATYPES-01-43 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-27, DATATYPES-02-31, DATATYPES-02-35, DATATYPES-02-39, DATATYPES-02-43 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-27, DATATYPES-03-31, DATATYPES-03-35, DATATYPES-03-39, DATATYPES-03-43 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-27, DATATYPES-04-31, DATATYPES-04-35, DATATYPES-04-39, DATATYPES-04-43 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-27, DATATYPES-05-31, DATATYPES-05-35, DATATYPES-05-39, DATATYPES-05-43 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-27, DATATYPES-06-31, DATATYPES-06-35, DATATYPES-06-39, DATATYPES-06-43 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-27, DATATYPES-07-31, DATATYPES-07-35, DATATYPES-07-39, DATATYPES-07-43 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-27, DATATYPES-08-31, DATATYPES-08-35, DATATYPES-08-39, DATATYPES-08-43 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-27, DATATYPES-09-31, DATATYPES-09-35, DATATYPES-09-39, DATATYPES-09-43 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-27, DATATYPES-10-31, DATATYPES-10-35, DATATYPES-10-39, DATATYPES-10-43 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-27, DATATYPES-11-31, DATATYPES-11-35, DATATYPES-11-39, DATATYPES-11-43 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-27, DATATYPES-12-31, DATATYPES-12-35, DATATYPES-12-39, DATATYPES-12-43 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-27, DATATYPES-13-31, DATATYPES-13-35, DATATYPES-13-39, DATATYPES-13-43 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-27, DATATYPES-14-31, DATATYPES-14-35, DATATYPES-14-39, DATATYPES-14-43 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-27, DATATYPES-15-31, DATATYPES-15-35, DATATYPES-15-39, DATATYPES-15-43 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-27, DATATYPES-16-31, DATATYPES-16-35, DATATYPES-16-39, DATATYPES-16-43 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-27, DATATYPES-17-31, DATATYPES-17-35, DATATYPES-17-39, DATATYPES-17-43 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-27, DATATYPES-18-31, DATATYPES-18-35, DATATYPES-18-39, DATATYPES-18-43 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-27, DATATYPES-19-31, DATATYPES-19-35, DATATYPES-19-39, DATATYPES-19-43 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-27, DATATYPES-20-31, DATATYPES-20-35, DATATYPES-20-39, DATATYPES-20-43 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-27, DATATYPES-21-31, DATATYPES-21-35, DATATYPES-21-39, DATATYPES-21-43 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-27, DATATYPES-22-31, DATATYPES-22-35, DATATYPES-22-39, DATATYPES-22-43 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-27, DATATYPES-23-31, DATATYPES-23-35, DATATYPES-23-39, DATATYPES-23-43 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-27, DATATYPES-24-31, DATATYPES-24-35, DATATYPES-24-39, DATATYPES-24-43 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-27, DATATYPES-25-31, DATATYPES-25-35, DATATYPES-25-39, DATATYPES-25-43 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-27, DATATYPES-26-31, DATATYPES-26-35, DATATYPES-26-39, DATATYPES-26-43 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-27, DATABASE_SCHEMA_USER-01-31, DATABASE_SCHEMA_USER-01-35, DATABASE_SCHEMA_USER-01-39, DATABASE_SCHEMA_USER-01-43 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-27, DATABASE_SCHEMA_USER-02-31, DATABASE_SCHEMA_USER-02-35, DATABASE_SCHEMA_USER-02-39, DATABASE_SCHEMA_USER-02-43 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-27, DATABASE_SCHEMA_USER-03-31, DATABASE_SCHEMA_USER-03-35, DATABASE_SCHEMA_USER-03-39, DATABASE_SCHEMA_USER-03-43 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-27, INTRODUCTION-01-31, INTRODUCTION-01-35, INTRODUCTION-01-39, INTRODUCTION-01-43 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-27, INTRODUCTION-02-31, INTRODUCTION-02-35, INTRODUCTION-02-39, INTRODUCTION-02-43 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-27, INTRODUCTION-03-31, INTRODUCTION-03-35, INTRODUCTION-03-39, INTRODUCTION-03-43 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-27, INTRODUCTION-04-31, INTRODUCTION-04-35, INTRODUCTION-04-39, INTRODUCTION-04-43 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-27, INTRODUCTION-05-31, INTRODUCTION-05-35, INTRODUCTION-05-39, INTRODUCTION-05-43 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-27, INTRODUCTION-06-31, INTRODUCTION-06-35, INTRODUCTION-06-39, INTRODUCTION-06-43 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-27, INTRODUCTION-07-31, INTRODUCTION-07-35, INTRODUCTION-07-39, INTRODUCTION-07-43 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-27, INTRODUCTION-08-31, INTRODUCTION-08-35, INTRODUCTION-08-39, INTRODUCTION-08-43 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-27, INTRODUCTION-09-31, INTRODUCTION-09-35, INTRODUCTION-09-39, INTRODUCTION-09-43 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-27, INTRODUCTION-10-31, INTRODUCTION-10-35, INTRODUCTION-10-39, INTRODUCTION-10-43 |

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
