# Banking / Finance: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### BANKING-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.AccountID, p.AccountName, COUNT(f.TransactionID) AS EventCount, SUM(f.Amount) AS TotalAmount FROM [banking].[Accounts] p LEFT JOIN [banking].[Transactions] f ON p.AccountID=f.AccountID GROUP BY p.AccountID, p.AccountName ORDER BY p.AccountID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### BANKING-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.AccountID, p.AccountName FROM [banking].[Accounts] p WHERE NOT EXISTS (SELECT 1 FROM [banking].[Transactions] f WHERE f.AccountID=p.AccountID) ORDER BY p.AccountID;
```

**Check and explain:** Only master ID 5.

### BANKING-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT TransactionID,AccountID,Amount,ROW_NUMBER() OVER(PARTITION BY AccountID ORDER BY Amount DESC,TransactionID) AS rn FROM [banking].[Transactions]) SELECT TransactionID,AccountID,Amount FROM Ranked WHERE rn=1 ORDER BY AccountID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### BANKING-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT t.TransactionID,a.AccountName,c.CustomerName,b.BranchName,t.Amount FROM banking.Transactions t JOIN banking.Accounts a ON a.AccountID=t.AccountID JOIN banking.Customers c ON c.CustomerID=a.CustomerID JOIN banking.Branches b ON b.BranchID=a.BranchID ORDER BY t.TransactionID;
```

**Check and explain:** 12 rows; every transaction has a valid account, customer and branch.

### BANKING-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Activity AS (SELECT a.CustomerID,SUM(t.Amount) AS TransactionTotal FROM banking.Accounts a JOIN banking.Transactions t ON t.AccountID=a.AccountID GROUP BY a.CustomerID), Lending AS (SELECT CustomerID,SUM(Principal) AS PrincipalTotal FROM banking.Loans GROUP BY CustomerID) SELECT c.CustomerID,COALESCE(a.TransactionTotal,0) AS TransactionTotal,COALESCE(l.PrincipalTotal,0) AS PrincipalTotal FROM banking.Customers c LEFT JOIN Activity a ON a.CustomerID=c.CustomerID LEFT JOIN Lending l ON l.CustomerID=c.CustomerID ORDER BY c.CustomerID;
```

**Check and explain:** 5 rows. Customer 1: transaction total 420, principal 15000. Principal totals sum to 58000, not multiplied by transaction count.

### BANKING-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT b.BranchID,b.BranchName,COUNT(a.AccountID) AS AccountCount FROM banking.Branches b LEFT JOIN banking.Accounts a ON a.BranchID=b.BranchID GROUP BY b.BranchID,b.BranchName ORDER BY b.BranchID;
```

**Check and explain:** Five branches, one account each. An account with no transactions still counts.
