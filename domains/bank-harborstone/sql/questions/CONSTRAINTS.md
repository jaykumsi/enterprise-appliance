# Banking / Finance — CONSTRAINTS

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

## Not Null

### CONSTRAINTS-01-02

**Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-07

**Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-12

**Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-17

**Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-22

**Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Unique

### CONSTRAINTS-02-02

**Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-07

**Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-12

**Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-17

**Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-22

**Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Check

### CONSTRAINTS-03-02

**Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-07

**Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-12

**Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-17

**Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-22

**Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Primary key

### CONSTRAINTS-04-02

**Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-07

**Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-12

**Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-17

**Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-22

**Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Foreign key

### CONSTRAINTS-05-02

**Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-07

**Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-12

**Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-17

**Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-22

**Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Not Null: progression

**Beginner:15 questions**

#### BANKING-CONSTRAINTS-01-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### BANKING-CONSTRAINTS-01-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### BANKING-CONSTRAINTS-01-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values. In the supplied sample data, `BranchName` is `Branch 1`.
2. Try to change `BranchName` to `NULL` in the row where `BranchID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Branches` have a value for `BranchName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values. In the supplied sample data, `CustomerName` is `Client 1`.
2. Try to change `CustomerName` to `NULL` in the row where `CustomerID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Customers` have a value for `CustomerName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values. In the supplied sample data, `AccountName` is `Accounts Alpha`.
2. Try to change `AccountName` to `NULL` in the row where `AccountID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Accounts` have a value for `AccountName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values. In the supplied sample data, `AccountID` is `1`.
2. Try to change `AccountID` to `NULL` in the row where `TransactionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Transactions` have a value for `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-01-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice NOT NULL on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values. In the supplied sample data, `CustomerID` is `1`.
2. Try to change `CustomerID` to `NULL` in the row where `LoanID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Loans` have a value for `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Unique: progression

**Beginner:15 questions**

#### BANKING-CONSTRAINTS-02-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### BANKING-CONSTRAINTS-02-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### BANKING-CONSTRAINTS-02-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add a copy of row 1, but change only `BranchID` to `100`. Leave the other values the same. The UNIQUE rule on `BranchCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `BranchID` value not enough when `BranchCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add a copy of row 1, but change only `CustomerID` to `100`. Leave the other values the same. The UNIQUE rule on `Email` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `CustomerID` value not enough when `Email` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add a copy of row 1, but change only `AccountID` to `100`. Leave the other values the same. The UNIQUE rule on `AccountNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `AccountID` value not enough when `AccountNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `TransactionID` to `100`. Leave the other values the same. The UNIQUE rule on `Reference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `TransactionID` value not enough when `Reference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-02-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice UNIQUE on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add a copy of row 1, but change only `LoanID` to `100`. Leave the other values the same. The UNIQUE rule on `LoanReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `LoanID` value not enough when `LoanReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Check: progression

**Beginner:15 questions**

#### BANKING-CONSTRAINTS-03-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### BANKING-CONSTRAINTS-03-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### BANKING-CONSTRAINTS-03-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(BranchName))) > 0`. Try to change `BranchName` to `N'   '` in the row where `BranchID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(CustomerName))) > 0`. Try to change `CustomerName` to `N'   '` in the row where `CustomerID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(AccountName))) > 0`. Try to change `AccountName` to `N'   '` in the row where `AccountID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. This table has the rule `TransactionType IN ('A','B','C')`. Try to change `TransactionType` to `'INVALID'` in the row where `TransactionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-03-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice CHECK on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. This table has the rule `Principal > 0`. Try to change `Principal` to `-1` in the row where `LoanID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Primary key: progression

**Beginner:15 questions**

#### BANKING-CONSTRAINTS-04-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### BANKING-CONSTRAINTS-04-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### BANKING-CONSTRAINTS-04-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Branches**

**Before you start:** Use `[banking].[Branches]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `BranchID = 1` and note its values.
2. Try to add another copy of the row where `BranchID = 1`. Keep the same `BranchID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Customers**

**Before you start:** Use `[banking].[Customers]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `CustomerID = 1` and note its values.
2. Try to add another copy of the row where `CustomerID = 1`. Keep the same `CustomerID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to add another copy of the row where `AccountID = 1`. Keep the same `AccountID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to add another copy of the row where `TransactionID = 1`. Keep the same `TransactionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-04-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice PRIMARY KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to add another copy of the row where `LoanID = 1`. Keep the same `LoanID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `LoanID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Foreign key: progression

**Beginner:15 questions**

#### BANKING-CONSTRAINTS-05-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### BANKING-CONSTRAINTS-05-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### BANKING-CONSTRAINTS-05-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `AccountID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Accounts**

**Before you start:** Use `[banking].[Accounts]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `AccountID = 1` and note its values.
2. Try to change `BranchID` to `999` in the row where `AccountID = 1`. There is no row with `BranchID = 999` in `Branches`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `BranchID` match a value in `Branches.BranchID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `AccountID` to `999` in the row where `TransactionID = 1`. There is no row with `AccountID = 999` in `Accounts`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `AccountID` match a value in `Accounts.AccountID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Transactions**

**Before you start:** Use `[banking].[Transactions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `TransactionID = 1` and note its values.
2. Try to change `ParentTransactionID` to `999` in the row where `TransactionID = 1`. There is no row with `TransactionID = 999` in `Transactions`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentTransactionID` match a value in `Transactions.TransactionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### BANKING-CONSTRAINTS-05-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Banking / Finance: Practice FOREIGN KEY on Loans**

**Before you start:** Use `[banking].[Loans]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `LoanID = 1` and note its values.
2. Try to change `CustomerID` to `999` in the row where `LoanID = 1`. There is no row with `CustomerID = 999` in `Customers`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `CustomerID` match a value in `Customers.CustomerID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

