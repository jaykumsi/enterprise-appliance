# Healthcare: connected SQL Server project

Follow patients through encounters with doctors and medications prescribed. Report encounters without prescriptions and avoid repeated encounter charges.

**Goal:** build and explain five related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.

## 1. Understand the relationships

A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.

```mermaid
erDiagram
    Patients ||--o{ Encounters : "PatientID"
    Encounters |o--o{ Encounters : "ParentEncounterID"
    Doctors ||--o{ Encounters : "DoctorID"
    Encounters ||--o{ Prescriptions : "EncounterID"
    Medications ||--o{ Prescriptions : "MedicationID"
```

Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.

## 2. Build the five tables

Start in a new disposable SQL Server 2017+ database. Work in this order: **Patients → Doctors → Medications → Encounters → Prescriptions**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.

### Patients

**Patients** — Synthetic patients; one patient may have several encounters.

| Column | Type | Requirement |
|---|---|---|
| PatientID | int | NOT NULL |
| PatientName | nvarchar(80) | NOT NULL |
| PatientNumber | varchar(20) | NOT NULL |
| Region | varchar(10) | NOT NULL |

Primary key: **PatientID**.
Unique business key: **PatientNumber**.
Business rule: `LEN(LTRIM(RTRIM(PatientName))) > 0`.

### Doctors

**Doctors** — One doctor is assigned to each encounter in this simplified teaching model.

| Column | Type | Requirement |
|---|---|---|
| DoctorID | int | NOT NULL |
| DoctorName | nvarchar(80) | NOT NULL |
| LicenseNumber | varchar(20) | NOT NULL |
| Specialty | varchar(30) | NOT NULL |

Primary key: **DoctorID**.
Unique business key: **LicenseNumber**.
Business rule: `LEN(LTRIM(RTRIM(DoctorName))) > 0`.

### Medications

**Medications** — Synthetic catalog for relational practice; no clinical dosing guidance.

| Column | Type | Requirement |
|---|---|---|
| MedicationID | int | NOT NULL |
| MedicationName | nvarchar(80) | NOT NULL |
| MedicationCode | varchar(20) | NOT NULL |
| UnitCost | decimal(12,2) | NOT NULL |

Primary key: **MedicationID**.
Unique business key: **MedicationCode**.
Business rule: `UnitCost >= 0`.
Business rule: `LEN(LTRIM(RTRIM(MedicationName))) > 0`.

### Encounters

**Encounters** — The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.

| Column | Type | Requirement |
|---|---|---|
| EncounterID | int | NOT NULL |
| PatientID | int | NOT NULL |
| EncounterReference | nvarchar(80) | NOT NULL |
| EncounterType | varchar(10) | NOT NULL |
| Status | varchar(10) | NOT NULL DEFAULT ('Open') |
| Charge | decimal(12,2) | NULL |
| ServiceUnits | int | NOT NULL |
| EncounterDate | date | NOT NULL |
| StartedAt | datetime2(3) | NOT NULL |
| RecordedAt | datetimeoffset(3) | NOT NULL |
| Note | nvarchar(100) | NULL |
| BackupNote | nvarchar(100) | NULL |
| ParentEncounterID | int | NULL |
| DoctorID | int | NOT NULL |

Primary key: **EncounterID**.
Unique business key: **EncounterReference**.
Business rule: `EncounterType IN ('A','B','C')`.
Business rule: `Status IN ('Open','Closed','Pending')`.
Business rule: `Charge >= 0`.
Business rule: `ServiceUnits > 0`.
Business rule: `ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID`.
Business rule: `LEN(LTRIM(RTRIM(EncounterReference))) > 0`.
Foreign key: **Encounters.PatientID → Patients.PatientID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Encounters.ParentEncounterID → Encounters.EncounterID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Encounters.DoctorID → Doctors.DoctorID**. Use NO ACTION on delete/update; do not disable checking.

### Prescriptions

**Prescriptions** — A prescription links one encounter to one medication; multiple prescriptions may belong to an encounter.

| Column | Type | Requirement |
|---|---|---|
| PrescriptionID | int | NOT NULL |
| EncounterID | int | NOT NULL |
| MedicationID | int | NOT NULL |
| PrescriptionReference | varchar(20) | NOT NULL |
| Quantity | int | NOT NULL |

Primary key: **PrescriptionID**.
Unique business key: **PrescriptionReference**.
Business rule: `Quantity > 0`.
Business rule: `LEN(LTRIM(RTRIM(PrescriptionReference))) > 0`.
Foreign key: **Prescriptions.EncounterID → Encounters.EncounterID**. Use NO ACTION on delete/update; do not disable checking.
Foreign key: **Prescriptions.MedicationID → Medications.MedicationID**. Use NO ACTION on delete/update; do not disable checking.

**Checkpoint:** five tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.

## 3. Load and inspect sample data

Use the Data Setup insert exercises in the same parent-before-child order. Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.

The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.

### Sample rows: Patients

| PatientID | PatientName | PatientNumber | Region |
|---|---|---|---|
| `1` | `Patients Alpha` | `PAT-1` | `North` |
| `2` | `Patients Beta` | `PAT-2` | `South` |
| `3` | `Patients Gamma` | `PAT-3` | `North` |
| `4` | `Patients Delta` | `PAT-4` | `West` |
| `5` | `Patients Unused` | `PAT-5` | `East` |

### Sample rows: Doctors

| DoctorID | DoctorName | LicenseNumber | Specialty |
|---|---|---|---|
| `1` | `Doctor 1` | `LIC-1` | `General` |
| `2` | `Doctor 2` | `LIC-2` | `Cardiology` |
| `3` | `Doctor 3` | `LIC-3` | `General` |
| `4` | `Doctor 4` | `LIC-4` | `Dermatology` |
| `5` | `Doctor 5` | `LIC-5` | `Neurology` |

### Sample rows: Medications

| MedicationID | MedicationName | MedicationCode | UnitCost |
|---|---|---|---|
| `1` | `Training medication 1` | `MED-1` | `5` |
| `2` | `Training medication 2` | `MED-2` | `10` |
| `3` | `Training medication 3` | `MED-3` | `15` |
| `4` | `Training medication 4` | `MED-4` | `20` |
| `5` | `Training medication 5` | `MED-5` | `25` |

### Sample rows: Encounters

| EncounterID | PatientID | EncounterReference | EncounterType | Status | Charge | ServiceUnits | EncounterDate | StartedAt | RecordedAt | Note | BackupNote | ParentEncounterID | DoctorID |
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

### Sample rows: Prescriptions

| PrescriptionID | EncounterID | MedicationID | PrescriptionReference | Quantity |
|---|---|---|---|---|
| `1` | `1` | `1` | `RX-1` | `2` |
| `2` | `1` | `2` | `RX-2` | `3` |
| `3` | `2` | `3` | `RX-3` | `1` |
| `4` | `3` | `1` | `RX-4` | `2` |
| `5` | `6` | `4` | `RX-5` | `4` |

**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.

## 4. Prove the rules and practice changes

Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../../BEGINNER_GUIDE.md) if these terms are new.

## Assignment navigation

IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](README.md) to see all topics.

| Topic | Subtopic | Your assignment IDs |
|---|---|---|
| [DDL](DDL.md) | Create | DDL-01-04, DDL-01-09, DDL-01-14, DDL-01-19, DDL-01-24 |
| [DDL](DDL.md) | Alter | DDL-02-04, DDL-02-09, DDL-02-14, DDL-02-19, DDL-02-24 |
| [DDL](DDL.md) | Drop | DDL-03-04, DDL-03-09, DDL-03-14, DDL-03-19, DDL-03-24 |
| [DATA_SETUP](DATA_SETUP.md) | Create tables | DATA_SETUP-01-04, DATA_SETUP-01-09, DATA_SETUP-01-14, DATA_SETUP-01-19, DATA_SETUP-01-24 |
| [DATA_SETUP](DATA_SETUP.md) | Insert data into the tables | DATA_SETUP-02-04, DATA_SETUP-02-09, DATA_SETUP-02-14, DATA_SETUP-02-19, DATA_SETUP-02-24 |
| [CONSTRAINTS](CONSTRAINTS.md) | Not Null | CONSTRAINTS-01-04, CONSTRAINTS-01-09, CONSTRAINTS-01-14, CONSTRAINTS-01-19, CONSTRAINTS-01-24 |
| [CONSTRAINTS](CONSTRAINTS.md) | Unique | CONSTRAINTS-02-04, CONSTRAINTS-02-09, CONSTRAINTS-02-14, CONSTRAINTS-02-19, CONSTRAINTS-02-24 |
| [CONSTRAINTS](CONSTRAINTS.md) | Check | CONSTRAINTS-03-04, CONSTRAINTS-03-09, CONSTRAINTS-03-14, CONSTRAINTS-03-19, CONSTRAINTS-03-24 |
| [CONSTRAINTS](CONSTRAINTS.md) | Primary key | CONSTRAINTS-04-04, CONSTRAINTS-04-09, CONSTRAINTS-04-14, CONSTRAINTS-04-19, CONSTRAINTS-04-24 |
| [CONSTRAINTS](CONSTRAINTS.md) | Foreign key | CONSTRAINTS-05-04, CONSTRAINTS-05-09, CONSTRAINTS-05-14, CONSTRAINTS-05-19, CONSTRAINTS-05-24 |
| [DML](DML.md) | Insert | DML-01-04, DML-01-09, DML-01-14, DML-01-19, DML-01-24 |
| [DML](DML.md) | Update | DML-02-04, DML-02-09, DML-02-14, DML-02-19, DML-02-24 |
| [DML](DML.md) | Delete | DML-03-04, DML-03-09, DML-03-14, DML-03-19, DML-03-24 |
| [DQL](DQL.md) | Select | DQL-01-04, DQL-01-09, DQL-01-14, DQL-01-19, DQL-01-24 |
| [DQL](DQL.md) | Where | DQL-02-04, DQL-02-09, DQL-02-14, DQL-02-19, DQL-02-24 |
| [DQL](DQL.md) | Group By | DQL-03-04, DQL-03-09, DQL-03-14, DQL-03-19, DQL-03-24 |
| [DQL](DQL.md) | Having | DQL-04-04, DQL-04-09, DQL-04-14, DQL-04-19, DQL-04-24 |
| [DQL](DQL.md) | Order By | DQL-05-04, DQL-05-09, DQL-05-14, DQL-05-19, DQL-05-24 |
| [DQL](DQL.md) | Top | DQL-06-04, DQL-06-09, DQL-06-14, DQL-06-19, DQL-06-24 |
| [OPERATORS](OPERATORS.md) | Equality Operator (=) | OPERATORS-01-04, OPERATORS-01-09, OPERATORS-01-14, OPERATORS-01-19, OPERATORS-01-24 |
| [OPERATORS](OPERATORS.md) | Inequality Operator (<>) | OPERATORS-02-04, OPERATORS-02-09, OPERATORS-02-14, OPERATORS-02-19, OPERATORS-02-24 |
| [OPERATORS](OPERATORS.md) | Greater Than (>) | OPERATORS-03-04, OPERATORS-03-09, OPERATORS-03-14, OPERATORS-03-19, OPERATORS-03-24 |
| [OPERATORS](OPERATORS.md) | Greater Than or Equal To (>=) | OPERATORS-04-04, OPERATORS-04-09, OPERATORS-04-14, OPERATORS-04-19, OPERATORS-04-24 |
| [OPERATORS](OPERATORS.md) | Less Than (<) | OPERATORS-05-04, OPERATORS-05-09, OPERATORS-05-14, OPERATORS-05-19, OPERATORS-05-24 |
| [OPERATORS](OPERATORS.md) | Less Than or Equal To (<=) | OPERATORS-06-04, OPERATORS-06-09, OPERATORS-06-14, OPERATORS-06-19, OPERATORS-06-24 |
| [OPERATORS](OPERATORS.md) | IN Operator | OPERATORS-07-04, OPERATORS-07-09, OPERATORS-07-14, OPERATORS-07-19, OPERATORS-07-24 |
| [OPERATORS](OPERATORS.md) | NOT IN Operator | OPERATORS-08-04, OPERATORS-08-09, OPERATORS-08-14, OPERATORS-08-19, OPERATORS-08-24 |
| [OPERATORS](OPERATORS.md) | LIKE Operator | OPERATORS-09-04, OPERATORS-09-09, OPERATORS-09-14, OPERATORS-09-19, OPERATORS-09-24 |
| [OPERATORS](OPERATORS.md) | NOT LIKE Operator | OPERATORS-10-04, OPERATORS-10-09, OPERATORS-10-14, OPERATORS-10-19, OPERATORS-10-24 |
| [OPERATORS](OPERATORS.md) | BETWEEN Operator | OPERATORS-11-04, OPERATORS-11-09, OPERATORS-11-14, OPERATORS-11-19, OPERATORS-11-24 |
| [OPERATORS](OPERATORS.md) | EXISTS Operator | OPERATORS-12-04, OPERATORS-12-09, OPERATORS-12-14, OPERATORS-12-19, OPERATORS-12-24 |
| [OPERATORS](OPERATORS.md) | NOT EXISTS Operator | OPERATORS-13-04, OPERATORS-13-09, OPERATORS-13-14, OPERATORS-13-19, OPERATORS-13-24 |
| [JOINS](JOINS.md) | Inner Join | JOINS-01-04, JOINS-01-09, JOINS-01-14, JOINS-01-19, JOINS-01-24 |
| [JOINS](JOINS.md) | Left Join | JOINS-02-04, JOINS-02-09, JOINS-02-14, JOINS-02-19, JOINS-02-24 |
| [JOINS](JOINS.md) | Right Join | JOINS-03-04, JOINS-03-09, JOINS-03-14, JOINS-03-19, JOINS-03-24 |
| [JOINS](JOINS.md) | Full Join | JOINS-04-04, JOINS-04-09, JOINS-04-14, JOINS-04-19, JOINS-04-24 |
| [JOINS](JOINS.md) | Cross Join | JOINS-05-04, JOINS-05-09, JOINS-05-14, JOINS-05-19, JOINS-05-24 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union | SET_OPERATIONS-01-04, SET_OPERATIONS-01-09, SET_OPERATIONS-01-14, SET_OPERATIONS-01-19, SET_OPERATIONS-01-24 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Union All | SET_OPERATIONS-02-04, SET_OPERATIONS-02-09, SET_OPERATIONS-02-14, SET_OPERATIONS-02-19, SET_OPERATIONS-02-24 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Intersect | SET_OPERATIONS-03-04, SET_OPERATIONS-03-09, SET_OPERATIONS-03-14, SET_OPERATIONS-03-19, SET_OPERATIONS-03-24 |
| [SET_OPERATIONS](SET_OPERATIONS.md) | Except | SET_OPERATIONS-04-04, SET_OPERATIONS-04-09, SET_OPERATIONS-04-14, SET_OPERATIONS-04-19, SET_OPERATIONS-04-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Length Function (LEN) | STRING_FUNCTIONS-01-04, STRING_FUNCTIONS-01-09, STRING_FUNCTIONS-01-14, STRING_FUNCTIONS-01-19, STRING_FUNCTIONS-01-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Substring Function (SUBSTRING) | STRING_FUNCTIONS-02-04, STRING_FUNCTIONS-02-09, STRING_FUNCTIONS-02-14, STRING_FUNCTIONS-02-19, STRING_FUNCTIONS-02-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Concatenation Operator (+) | STRING_FUNCTIONS-03-04, STRING_FUNCTIONS-03-09, STRING_FUNCTIONS-03-14, STRING_FUNCTIONS-03-19, STRING_FUNCTIONS-03-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Lower Function (LOWER) | STRING_FUNCTIONS-04-04, STRING_FUNCTIONS-04-09, STRING_FUNCTIONS-04-14, STRING_FUNCTIONS-04-19, STRING_FUNCTIONS-04-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Upper Function (UPPER) | STRING_FUNCTIONS-05-04, STRING_FUNCTIONS-05-09, STRING_FUNCTIONS-05-14, STRING_FUNCTIONS-05-19, STRING_FUNCTIONS-05-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Trim Function (TRIM) | STRING_FUNCTIONS-06-04, STRING_FUNCTIONS-06-09, STRING_FUNCTIONS-06-14, STRING_FUNCTIONS-06-19, STRING_FUNCTIONS-06-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Ltrim Function (LTRIM) | STRING_FUNCTIONS-07-04, STRING_FUNCTIONS-07-09, STRING_FUNCTIONS-07-14, STRING_FUNCTIONS-07-19, STRING_FUNCTIONS-07-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Rtrim Function (RTRIM) | STRING_FUNCTIONS-08-04, STRING_FUNCTIONS-08-09, STRING_FUNCTIONS-08-14, STRING_FUNCTIONS-08-19, STRING_FUNCTIONS-08-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Charindex Function (CHARINDEX) | STRING_FUNCTIONS-09-04, STRING_FUNCTIONS-09-09, STRING_FUNCTIONS-09-14, STRING_FUNCTIONS-09-19, STRING_FUNCTIONS-09-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Left Function (LEFT) | STRING_FUNCTIONS-10-04, STRING_FUNCTIONS-10-09, STRING_FUNCTIONS-10-14, STRING_FUNCTIONS-10-19, STRING_FUNCTIONS-10-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Right Function (RIGHT) | STRING_FUNCTIONS-11-04, STRING_FUNCTIONS-11-09, STRING_FUNCTIONS-11-14, STRING_FUNCTIONS-11-19, STRING_FUNCTIONS-11-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Reverse Function (REVERSE) | STRING_FUNCTIONS-12-04, STRING_FUNCTIONS-12-09, STRING_FUNCTIONS-12-14, STRING_FUNCTIONS-12-19, STRING_FUNCTIONS-12-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Replace Function (REPLACE) | STRING_FUNCTIONS-13-04, STRING_FUNCTIONS-13-09, STRING_FUNCTIONS-13-14, STRING_FUNCTIONS-13-19, STRING_FUNCTIONS-13-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Case Statement (CASE) | STRING_FUNCTIONS-14-04, STRING_FUNCTIONS-14-09, STRING_FUNCTIONS-14-14, STRING_FUNCTIONS-14-19, STRING_FUNCTIONS-14-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | ISNULL Function (ISNULL) | STRING_FUNCTIONS-15-04, STRING_FUNCTIONS-15-09, STRING_FUNCTIONS-15-14, STRING_FUNCTIONS-15-19, STRING_FUNCTIONS-15-24 |
| [STRING_FUNCTIONS](STRING_FUNCTIONS.md) | Coalesce Function (COALESCE) | STRING_FUNCTIONS-16-04, STRING_FUNCTIONS-16-09, STRING_FUNCTIONS-16-14, STRING_FUNCTIONS-16-19, STRING_FUNCTIONS-16-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Current Date and time (GETDATE) | DATE_FUNCTIONS-01-04, DATE_FUNCTIONS-01-09, DATE_FUNCTIONS-01-14, DATE_FUNCTIONS-01-19, DATE_FUNCTIONS-01-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Part Function (DATEPART) | DATE_FUNCTIONS-02-04, DATE_FUNCTIONS-02-09, DATE_FUNCTIONS-02-14, DATE_FUNCTIONS-02-19, DATE_FUNCTIONS-02-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Difference Function (DATEDIFF) | DATE_FUNCTIONS-03-04, DATE_FUNCTIONS-03-09, DATE_FUNCTIONS-03-14, DATE_FUNCTIONS-03-19, DATE_FUNCTIONS-03-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Addition/Subtraction | DATE_FUNCTIONS-04-04, DATE_FUNCTIONS-04-09, DATE_FUNCTIONS-04-14, DATE_FUNCTIONS-04-19, DATE_FUNCTIONS-04-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date Formatting (FORMAT) | DATE_FUNCTIONS-05-04, DATE_FUNCTIONS-05-09, DATE_FUNCTIONS-05-14, DATE_FUNCTIONS-05-19, DATE_FUNCTIONS-05-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Weekday Function (DATEPART) | DATE_FUNCTIONS-06-04, DATE_FUNCTIONS-06-09, DATE_FUNCTIONS-06-14, DATE_FUNCTIONS-06-19, DATE_FUNCTIONS-06-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date to String (Various formats) | DATE_FUNCTIONS-07-04, DATE_FUNCTIONS-07-09, DATE_FUNCTIONS-07-14, DATE_FUNCTIONS-07-19, DATE_FUNCTIONS-07-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | DateTime to String (Various formats) | DATE_FUNCTIONS-08-04, DATE_FUNCTIONS-08-09, DATE_FUNCTIONS-08-14, DATE_FUNCTIONS-08-19, DATE_FUNCTIONS-08-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to Date (Various formats) | DATE_FUNCTIONS-09-04, DATE_FUNCTIONS-09-09, DATE_FUNCTIONS-09-14, DATE_FUNCTIONS-09-19, DATE_FUNCTIONS-09-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | String to DateTime (Various formats) | DATE_FUNCTIONS-10-04, DATE_FUNCTIONS-10-09, DATE_FUNCTIONS-10-14, DATE_FUNCTIONS-10-19, DATE_FUNCTIONS-10-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Date and Time | DATE_FUNCTIONS-11-04, DATE_FUNCTIONS-11-09, DATE_FUNCTIONS-11-14, DATE_FUNCTIONS-11-19, DATE_FUNCTIONS-11-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Timezones | DATE_FUNCTIONS-12-04, DATE_FUNCTIONS-12-09, DATE_FUNCTIONS-12-14, DATE_FUNCTIONS-12-19, DATE_FUNCTIONS-12-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | UTC | DATE_FUNCTIONS-13-04, DATE_FUNCTIONS-13-09, DATE_FUNCTIONS-13-14, DATE_FUNCTIONS-13-19, DATE_FUNCTIONS-13-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Offsets | DATE_FUNCTIONS-14-04, DATE_FUNCTIONS-14-09, DATE_FUNCTIONS-14-14, DATE_FUNCTIONS-14-19, DATE_FUNCTIONS-14-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Applying an Offset to a Date Datatype Column | DATE_FUNCTIONS-15-04, DATE_FUNCTIONS-15-09, DATE_FUNCTIONS-15-14, DATE_FUNCTIONS-15-19, DATE_FUNCTIONS-15-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime to DateTime with Timezone (in UTC, EST and IST TimeZones) | DATE_FUNCTIONS-16-04, DATE_FUNCTIONS-16-09, DATE_FUNCTIONS-16-14, DATE_FUNCTIONS-16-19, DATE_FUNCTIONS-16-24 |
| [DATE_FUNCTIONS](DATE_FUNCTIONS.md) | Cast a DateTime Timezone to another TimeZone | DATE_FUNCTIONS-17-04, DATE_FUNCTIONS-17-09, DATE_FUNCTIONS-17-14, DATE_FUNCTIONS-17-19, DATE_FUNCTIONS-17-24 |
| [AGGREGATES](AGGREGATES.md) | Count | AGGREGATES-01-04, AGGREGATES-01-09, AGGREGATES-01-14, AGGREGATES-01-19, AGGREGATES-01-24 |
| [AGGREGATES](AGGREGATES.md) | Sum | AGGREGATES-02-04, AGGREGATES-02-09, AGGREGATES-02-14, AGGREGATES-02-19, AGGREGATES-02-24 |
| [AGGREGATES](AGGREGATES.md) | Avg | AGGREGATES-03-04, AGGREGATES-03-09, AGGREGATES-03-14, AGGREGATES-03-19, AGGREGATES-03-24 |
| [AGGREGATES](AGGREGATES.md) | Max | AGGREGATES-04-04, AGGREGATES-04-09, AGGREGATES-04-14, AGGREGATES-04-19, AGGREGATES-04-24 |
| [AGGREGATES](AGGREGATES.md) | Min | AGGREGATES-05-04, AGGREGATES-05-09, AGGREGATES-05-14, AGGREGATES-05-19, AGGREGATES-05-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | Aggregate Functions | ANALYTICAL_FUNCTIONS-01-04, ANALYTICAL_FUNCTIONS-01-09, ANALYTICAL_FUNCTIONS-01-14, ANALYTICAL_FUNCTIONS-01-19, ANALYTICAL_FUNCTIONS-01-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | ROW_NUMBER() | ANALYTICAL_FUNCTIONS-02-04, ANALYTICAL_FUNCTIONS-02-09, ANALYTICAL_FUNCTIONS-02-14, ANALYTICAL_FUNCTIONS-02-19, ANALYTICAL_FUNCTIONS-02-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | RANK() | ANALYTICAL_FUNCTIONS-03-04, ANALYTICAL_FUNCTIONS-03-09, ANALYTICAL_FUNCTIONS-03-14, ANALYTICAL_FUNCTIONS-03-19, ANALYTICAL_FUNCTIONS-03-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | DENSE_RANK() | ANALYTICAL_FUNCTIONS-04-04, ANALYTICAL_FUNCTIONS-04-09, ANALYTICAL_FUNCTIONS-04-14, ANALYTICAL_FUNCTIONS-04-19, ANALYTICAL_FUNCTIONS-04-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | NTILE(n) | ANALYTICAL_FUNCTIONS-05-04, ANALYTICAL_FUNCTIONS-05-09, ANALYTICAL_FUNCTIONS-05-14, ANALYTICAL_FUNCTIONS-05-19, ANALYTICAL_FUNCTIONS-05-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAG() | ANALYTICAL_FUNCTIONS-06-04, ANALYTICAL_FUNCTIONS-06-09, ANALYTICAL_FUNCTIONS-06-14, ANALYTICAL_FUNCTIONS-06-19, ANALYTICAL_FUNCTIONS-06-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LEAD() | ANALYTICAL_FUNCTIONS-07-04, ANALYTICAL_FUNCTIONS-07-09, ANALYTICAL_FUNCTIONS-07-14, ANALYTICAL_FUNCTIONS-07-19, ANALYTICAL_FUNCTIONS-07-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | FIRST_VALUE() | ANALYTICAL_FUNCTIONS-08-04, ANALYTICAL_FUNCTIONS-08-09, ANALYTICAL_FUNCTIONS-08-14, ANALYTICAL_FUNCTIONS-08-19, ANALYTICAL_FUNCTIONS-08-24 |
| [ANALYTICAL_FUNCTIONS](ANALYTICAL_FUNCTIONS.md) | LAST_VALUE() | ANALYTICAL_FUNCTIONS-09-04, ANALYTICAL_FUNCTIONS-09-09, ANALYTICAL_FUNCTIONS-09-14, ANALYTICAL_FUNCTIONS-09-19, ANALYTICAL_FUNCTIONS-09-24 |
| [CTE](CTE.md) | Creating a CTE | CTE-01-04, CTE-01-09, CTE-01-14, CTE-01-19, CTE-01-24 |
| [CTE](CTE.md) | Using Multiple CTEs | CTE-02-04, CTE-02-09, CTE-02-14, CTE-02-19, CTE-02-24 |
| [CTE](CTE.md) | Recursive CTEs | CTE-03-04, CTE-03-09, CTE-03-14, CTE-03-19, CTE-03-24 |
| [CTE](CTE.md) | Common Use Cases for CTEs | CTE-04-04, CTE-04-09, CTE-04-14, CTE-04-19, CTE-04-24 |
| [CTE](CTE.md) | Benefits of Using CTEs | CTE-05-04, CTE-05-09, CTE-05-14, CTE-05-19, CTE-05-24 |
| [DATATYPES](DATATYPES.md) | INT | DATATYPES-01-04, DATATYPES-01-09, DATATYPES-01-14, DATATYPES-01-19, DATATYPES-01-24 |
| [DATATYPES](DATATYPES.md) | BIGINT | DATATYPES-02-04, DATATYPES-02-09, DATATYPES-02-14, DATATYPES-02-19, DATATYPES-02-24 |
| [DATATYPES](DATATYPES.md) | DECIMAL | DATATYPES-03-04, DATATYPES-03-09, DATATYPES-03-14, DATATYPES-03-19, DATATYPES-03-24 |
| [DATATYPES](DATATYPES.md) | NUMERIC | DATATYPES-04-04, DATATYPES-04-09, DATATYPES-04-14, DATATYPES-04-19, DATATYPES-04-24 |
| [DATATYPES](DATATYPES.md) | FLOAT | DATATYPES-05-04, DATATYPES-05-09, DATATYPES-05-14, DATATYPES-05-19, DATATYPES-05-24 |
| [DATATYPES](DATATYPES.md) | DATE | DATATYPES-06-04, DATATYPES-06-09, DATATYPES-06-14, DATATYPES-06-19, DATATYPES-06-24 |
| [DATATYPES](DATATYPES.md) | DATETIME | DATATYPES-07-04, DATATYPES-07-09, DATATYPES-07-14, DATATYPES-07-19, DATATYPES-07-24 |
| [DATATYPES](DATATYPES.md) | SMALLDATETIME | DATATYPES-08-04, DATATYPES-08-09, DATATYPES-08-14, DATATYPES-08-19, DATATYPES-08-24 |
| [DATATYPES](DATATYPES.md) | DATETIMEOFFSET | DATATYPES-09-04, DATATYPES-09-09, DATATYPES-09-14, DATATYPES-09-19, DATATYPES-09-24 |
| [DATATYPES](DATATYPES.md) | TIME | DATATYPES-10-04, DATATYPES-10-09, DATATYPES-10-14, DATATYPES-10-19, DATATYPES-10-24 |
| [DATATYPES](DATATYPES.md) | DATETIME2 | DATATYPES-11-04, DATATYPES-11-09, DATATYPES-11-14, DATATYPES-11-19, DATATYPES-11-24 |
| [DATATYPES](DATATYPES.md) | CHAR(n) | DATATYPES-12-04, DATATYPES-12-09, DATATYPES-12-14, DATATYPES-12-19, DATATYPES-12-24 |
| [DATATYPES](DATATYPES.md) | VARCHAR(n) | DATATYPES-13-04, DATATYPES-13-09, DATATYPES-13-14, DATATYPES-13-19, DATATYPES-13-24 |
| [DATATYPES](DATATYPES.md) | BINARY | DATATYPES-14-04, DATATYPES-14-09, DATATYPES-14-14, DATATYPES-14-19, DATATYPES-14-24 |
| [DATATYPES](DATATYPES.md) | VARBINARY | DATATYPES-15-04, DATATYPES-15-09, DATATYPES-15-14, DATATYPES-15-19, DATATYPES-15-24 |
| [DATATYPES](DATATYPES.md) | UNIQUEIDENTIFIER | DATATYPES-16-04, DATATYPES-16-09, DATATYPES-16-14, DATATYPES-16-19, DATATYPES-16-24 |
| [DATATYPES](DATATYPES.md) | BIT | DATATYPES-17-04, DATATYPES-17-09, DATATYPES-17-14, DATATYPES-17-19, DATATYPES-17-24 |
| [DATATYPES](DATATYPES.md) | MONEY | DATATYPES-18-04, DATATYPES-18-09, DATATYPES-18-14, DATATYPES-18-19, DATATYPES-18-24 |
| [DATATYPES](DATATYPES.md) | SMALLMONEY | DATATYPES-19-04, DATATYPES-19-09, DATATYPES-19-14, DATATYPES-19-19, DATATYPES-19-24 |
| [DATATYPES](DATATYPES.md) | TEXT | DATATYPES-20-04, DATATYPES-20-09, DATATYPES-20-14, DATATYPES-20-19, DATATYPES-20-24 |
| [DATATYPES](DATATYPES.md) | XML | DATATYPES-21-04, DATATYPES-21-09, DATATYPES-21-14, DATATYPES-21-19, DATATYPES-21-24 |
| [DATATYPES](DATATYPES.md) | GEOGRAPHY | DATATYPES-22-04, DATATYPES-22-09, DATATYPES-22-14, DATATYPES-22-19, DATATYPES-22-24 |
| [DATATYPES](DATATYPES.md) | GEOMETRY | DATATYPES-23-04, DATATYPES-23-09, DATATYPES-23-14, DATATYPES-23-19, DATATYPES-23-24 |
| [DATATYPES](DATATYPES.md) | HIERARCHYID | DATATYPES-24-04, DATATYPES-24-09, DATATYPES-24-14, DATATYPES-24-19, DATATYPES-24-24 |
| [DATATYPES](DATATYPES.md) | ROWVERSION | DATATYPES-25-04, DATATYPES-25-09, DATATYPES-25-14, DATATYPES-25-19, DATATYPES-25-24 |
| [DATATYPES](DATATYPES.md) | CURSOR | DATATYPES-26-04, DATATYPES-26-09, DATATYPES-26-14, DATATYPES-26-19, DATATYPES-26-24 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Database | DATABASE_SCHEMA_USER-01-04, DATABASE_SCHEMA_USER-01-09, DATABASE_SCHEMA_USER-01-14, DATABASE_SCHEMA_USER-01-19, DATABASE_SCHEMA_USER-01-24 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | Schema | DATABASE_SCHEMA_USER-02-04, DATABASE_SCHEMA_USER-02-09, DATABASE_SCHEMA_USER-02-14, DATABASE_SCHEMA_USER-02-19, DATABASE_SCHEMA_USER-02-24 |
| [DATABASE_SCHEMA_USER](DATABASE_SCHEMA_USER.md) | User | DATABASE_SCHEMA_USER-03-04, DATABASE_SCHEMA_USER-03-09, DATABASE_SCHEMA_USER-03-14, DATABASE_SCHEMA_USER-03-19, DATABASE_SCHEMA_USER-03-24 |
| [INTRODUCTION](INTRODUCTION.md) | Relational database fundamentals | INTRODUCTION-01-04, INTRODUCTION-01-09, INTRODUCTION-01-14, INTRODUCTION-01-19, INTRODUCTION-01-24 |
| [INTRODUCTION](INTRODUCTION.md) | Structured Data Storage and Control | INTRODUCTION-02-04, INTRODUCTION-02-09, INTRODUCTION-02-14, INTRODUCTION-02-19, INTRODUCTION-02-24 |
| [INTRODUCTION](INTRODUCTION.md) | Advanced Querying and Data Operations | INTRODUCTION-03-04, INTRODUCTION-03-09, INTRODUCTION-03-14, INTRODUCTION-03-19, INTRODUCTION-03-24 |
| [INTRODUCTION](INTRODUCTION.md) | Security and Regulatory Support | INTRODUCTION-04-04, INTRODUCTION-04-09, INTRODUCTION-04-14, INTRODUCTION-04-19, INTRODUCTION-04-24 |
| [INTRODUCTION](INTRODUCTION.md) | Performance and Scalability | INTRODUCTION-05-04, INTRODUCTION-05-09, INTRODUCTION-05-14, INTRODUCTION-05-19, INTRODUCTION-05-24 |
| [INTRODUCTION](INTRODUCTION.md) | Analytics and Business Intelligence | INTRODUCTION-06-04, INTRODUCTION-06-09, INTRODUCTION-06-14, INTRODUCTION-06-19, INTRODUCTION-06-24 |
| [INTRODUCTION](INTRODUCTION.md) | Transactional Workloads | INTRODUCTION-07-04, INTRODUCTION-07-09, INTRODUCTION-07-14, INTRODUCTION-07-19, INTRODUCTION-07-24 |
| [INTRODUCTION](INTRODUCTION.md) | Data Warehousing and BI | INTRODUCTION-08-04, INTRODUCTION-08-09, INTRODUCTION-08-14, INTRODUCTION-08-19, INTRODUCTION-08-24 |
| [INTRODUCTION](INTRODUCTION.md) | Digital Content Management | INTRODUCTION-09-04, INTRODUCTION-09-09, INTRODUCTION-09-14, INTRODUCTION-09-19, INTRODUCTION-09-24 |
| [INTRODUCTION](INTRODUCTION.md) | Enterprise Applications | INTRODUCTION-10-04, INTRODUCTION-10-09, INTRODUCTION-10-14, INTRODUCTION-10-19, INTRODUCTION-10-24 |

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
