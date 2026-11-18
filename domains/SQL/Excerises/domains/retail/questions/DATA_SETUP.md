# Retail — DATA SETUP

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

## Create tables

### DATA_SETUP-01-01

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

### DATA_SETUP-01-06

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

### DATA_SETUP-01-11

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

### DATA_SETUP-01-16

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

### DATA_SETUP-01-21

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

## Insert data into the tables

### DATA_SETUP-02-01

Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

### DATA_SETUP-02-06

Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

### DATA_SETUP-02-11

Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

### DATA_SETUP-02-16

Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

### DATA_SETUP-02-21

Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Create tables: progression

**Beginner:15 questions**

#### RETAIL-DATA_SETUP-01-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### RETAIL-DATA_SETUP-01-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### RETAIL-DATA_SETUP-01-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-01-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with [the Retail project brief](DOMAIN_GUIDE.md); identify its primary key and which tables need sample rows first.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Insert data into the tables: progression

**Beginner:15 questions**

#### RETAIL-DATA_SETUP-02-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### RETAIL-DATA_SETUP-02-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### RETAIL-DATA_SETUP-02-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Customers from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Products from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 12 sample rows for Orders from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 6 sample rows for OrderItems from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATA_SETUP-02-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Load the 5 sample rows for Payments from [the Retail project brief](DOMAIN_GUIDE.md) into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Retained earlier SQL draft exercises

Unique earlier draft contracts are consolidated here rather than kept in a second SQL bank. They supplement the15/15/15 levelled set;their new extensions were not supplied with complete validated solutions. Use the domain guide for table requirements.

##### SQL-DATA-SETUP-01-B01

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B02

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B03

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B04

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B05

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B06

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B07

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B08

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B09

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B10

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B11

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B12

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B13

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B14

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-B15

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I01

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I02

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I03

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I04

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I05

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I06

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I07

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I08

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I09

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I10

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I11

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I12

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I13

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I14

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-I15

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A01

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A02

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A03

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A04

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A05

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A06

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A07

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A08

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A09

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A10

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A11

Retail: After building Customers from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A12

Retail: After building Products from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A13

Retail: After building Orders from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A14

Retail: After building OrderItems from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-01-A15

Retail: After building Payments from the DDL Create assignment, verify its column types, which columns allow NULL, and foreign key settings using sys.columns and sys.foreign_keys. Compare with the Retail table contract supplied with this question; identify its primary key and which tables need sample rows first.

**Extension:** Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B01

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B02

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B03

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B04

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B05

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B06

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B07

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B08

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B09

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B10

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B11

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B12

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B13

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B14

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-B15

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I01

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I02

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I03

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I04

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I05

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I06

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I07

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I08

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I09

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I10

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I11

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I12

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I13

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I14

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-I15

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A01

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A02

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A03

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A04

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A05

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A06

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A07

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A08

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A09

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A10

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A11

Retail: Load the 5 sample rows for Customers from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A12

Retail: Load the 5 sample rows for Products from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A13

Retail: Load the 12 sample rows for Orders from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A14

Retail: Load the 6 sample rows for OrderItems from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.

##### SQL-DATA-SETUP-02-A15

Retail: Load the 5 sample rows for Payments from the Retail table contract supplied with this question into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the final project. Verify count and key values; do not run this if the complete seed script was already used.

**Extension:** Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.

**Acceptance example:** Use a fresh scratch database for table creation,or empty target tables with required parent rows already loaded for insert exercises. The core and Retail table contract supply the requirements. Do not preload solved INSERT answers.
