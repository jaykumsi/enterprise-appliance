# Retail — DATABASE SCHEMA USER

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

## Database

### DATABASE_SCHEMA_USER-01-01

Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

### DATABASE_SCHEMA_USER-01-06

Retail: Report the current database name, ID and collation.

### DATABASE_SCHEMA_USER-01-11

Retail: List visible databases and their state and recovery model.

### DATABASE_SCHEMA_USER-01-16

Retail: List the current database data/log file logical names, types and allocated sizes in MB.

### DATABASE_SCHEMA_USER-01-21

Retail: Report current database compatibility level and explain how an instance, database and schema differ.

## Schema

### DATABASE_SCHEMA_USER-02-01

Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

### DATABASE_SCHEMA_USER-02-06

Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

### DATABASE_SCHEMA_USER-02-11

Retail: List the tables belonging to the existing domain schema. Use a practice database.

### DATABASE_SCHEMA_USER-02-16

Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

### DATABASE_SCHEMA_USER-02-21

Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

## User

### DATABASE_SCHEMA_USER-03-01

Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

### DATABASE_SCHEMA_USER-03-06

Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

### DATABASE_SCHEMA_USER-03-11

Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

### DATABASE_SCHEMA_USER-03-16

Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

### DATABASE_SCHEMA_USER-03-21

Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Database: progression

**Beginner:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-01-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-01-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-01-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Write a script to create an empty database named RetailAssignmentLab. Run separately with instructor-authorized CREATE DATABASE permission.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report the current database name, ID and collation.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List visible databases and their state and recovery model.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the current database data/log file logical names, types and allocated sizes in MB.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-01-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Report current database compatibility level and explain how an instance, database and schema differ.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Schema: progression

**Beginner:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-02-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-02-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-02-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema owned by dbo, inspect its owner, then remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and a table Records(ID int); show its two-part name, then drop the table followed by the schema. Use a practice database.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: List the tables belonging to the existing domain schema. Use a practice database.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema and transfer a new scratch table dbo.TransferLab into it; drop the practice table followed by the schema. Use a practice database.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-02-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create schema retailAssignmentSchema, explicitly set its owner to dbo, then inspect ownership and remove the schema using DROP SCHEMA. Use a practice database.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### User: progression

**Beginner:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-03-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-03-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### RETAIL-DATABASE_SCHEMA_USER-03-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create database user retailLabReader WITHOUT LOGIN and show its authentication type. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant retailLabReader SELECT on schema retail and inspect the explicit permission. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Grant then revoke SELECT on schema retail for retailLabReader. Explain why REVOKE is not DENY. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Set retailLabReader's default schema to retail; inspect it. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### RETAIL-DATABASE_SCHEMA_USER-03-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** Retail: Create role retailLabReaderRole, grant it schema SELECT, add retailLabReader to the role and inspect membership. Use a new database connection with instructor-authorized principal-management permissions.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Retained earlier SQL draft exercises

Unique earlier draft contracts are consolidated here rather than kept in a second SQL bank. They supplement the15/15/15 levelled set;their new extensions were not supplied with complete validated solutions. Use the domain guide for table requirements.

##### SQL-DATABASE-SCHEMA-USER-01-B01

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B02

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B03

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B04

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B05

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B06

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B07

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B08

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B09

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B10

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Return the core's dependency/resource graph and validate every referenced node exists.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B11

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B12

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Produce a dry-run plan describing observable actions with no external mutation calls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B13

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B14

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-B15

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I01

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I02

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I03

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I04

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I05

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I06

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I07

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I08

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I09

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I10

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I11

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I12

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I13

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I14

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-I15

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A01

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A02

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A03

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A04

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A05

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A06

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A07

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A08

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A09

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A10

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A11

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A12

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A13

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A14

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-01-A15

Implement a local provision planner for database names matching Lab_[A-Za-z0-9_]{1,32}. Given existing [Lab_A],request Lab_A -> ALREADY_EXISTS and Lab_B -> CREATE_REQUIRED. Return no real CREATE DATABASE action unless using an instructor-provided disposable SQL Server instance. Supply SQL catalog verification for a native demonstration.

**Extension:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B01

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B02

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B03

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B04

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B05

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B06

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B07

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B08

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B09

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B10

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Return the core's dependency/resource graph and validate every referenced node exists.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B11

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B12

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Produce a dry-run plan describing observable actions with no external mutation calls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B13

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B14

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-B15

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I01

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I02

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I03

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I04

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I05

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I06

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I07

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I08

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I09

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I10

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I11

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I12

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I13

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I14

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-I15

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A01

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A02

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A03

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A04

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A05

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A06

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A07

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A08

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A09

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A10

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A11

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A12

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A13

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A14

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-02-A15

In an instructor-provided disposable SQL Server database,design schemas ingest and report,each with an Orders table. Write fully qualified SQL proving same table names do not mix rows. Supply a metadata check for schema ownership; a name alone is not an authorization grant.

**Extension:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B01

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B02

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B03

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B04

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B05

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B06

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B07

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B08

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B09

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B10

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Return the core's dependency/resource graph and validate every referenced node exists.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B11

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B12

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Produce a dry-run plan describing observable actions with no external mutation calls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B13

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B14

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-B15

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I01

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I02

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I03

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I04

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I05

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I06

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I07

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I08

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I09

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I10

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I11

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I12

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I13

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I14

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-I15

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A01

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A02

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A03

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A04

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A05

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A06

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A07

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A08

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A09

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A10

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A11

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A12

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A13

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A14

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.

##### SQL-DATABASE-SCHEMA-USER-03-A15

In a disposable SQL Server database,design a WITHOUT LOGIN reader principal with SELECT on a report view only. Show allowed view read and rejected base-table update using an execution-context test. A grant on one object must not authorize another. Also provide a local finite actor/action/object decision table.

**Extension:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql) and its exact baseline rows. Derive the complete expected result independently; legacy core references are instructor-only and do not answer the extension.
