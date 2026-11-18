# Brokerage: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### BROKERAGE-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.AccountID, p.AccountName, COUNT(f.OrderID) AS EventCount, SUM(f.EstimatedValue) AS TotalAmount FROM [brokerage].[BrokerageAccounts] p LEFT JOIN [brokerage].[TradeOrders] f ON p.AccountID=f.AccountID GROUP BY p.AccountID, p.AccountName ORDER BY p.AccountID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### BROKERAGE-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.AccountID, p.AccountName FROM [brokerage].[BrokerageAccounts] p WHERE NOT EXISTS (SELECT 1 FROM [brokerage].[TradeOrders] f WHERE f.AccountID=p.AccountID) ORDER BY p.AccountID;
```

**Check and explain:** Only master ID 5.

### BROKERAGE-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT OrderID,AccountID,EstimatedValue,ROW_NUMBER() OVER(PARTITION BY AccountID ORDER BY EstimatedValue DESC,OrderID) AS rn FROM [brokerage].[TradeOrders]) SELECT OrderID,AccountID,EstimatedValue FROM Ranked WHERE rn=1 ORDER BY AccountID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### BROKERAGE-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT e.ExecutionReference,c.ClientName,a.AccountNumber,s.Symbol,o.OrderID,e.ExecutedQuantity,e.ExecutionPrice,e.ExecutedQuantity*e.ExecutionPrice AS GrossValue FROM brokerage.Executions e JOIN brokerage.TradeOrders o ON o.OrderID=e.OrderID JOIN brokerage.BrokerageAccounts a ON a.AccountID=o.AccountID JOIN brokerage.Clients c ON c.ClientID=a.ClientID JOIN brokerage.Securities s ON s.SecurityID=o.SecurityID ORDER BY e.ExecutionID;
```

**Check and explain:** 6 fills; gross executed values total 702.60. All clients and securities are fictitious.

### BROKERAGE-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Fills AS (SELECT OrderID,SUM(ExecutedQuantity) AS FilledQuantity,SUM(ExecutedQuantity*ExecutionPrice) AS GrossValue FROM brokerage.Executions GROUP BY OrderID) SELECT o.OrderID,o.RequestedQuantity,COALESCE(f.FilledQuantity,0) AS FilledQuantity,o.RequestedQuantity-COALESCE(f.FilledQuantity,0) AS RemainingQuantity,COALESCE(f.GrossValue,0) AS GrossValue,f.GrossValue/NULLIF(f.FilledQuantity,0) AS AverageExecutionPrice FROM brokerage.TradeOrders o LEFT JOIN Fills f ON f.OrderID=o.OrderID ORDER BY o.OrderID;
```

**Check and explain:** 12 orders. Order 1: filled=1, remaining=0, gross=100.60, average=100.60. Order 2: filled=1.5, remaining=0.5, gross=149, average approximately 99.333333. Order 4 has NULL average. No order is overfilled.

### BROKERAGE-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Activity AS (SELECT a.ClientID,SUM(e.ExecutedQuantity*e.ExecutionPrice) AS GrossValue,COUNT(e.ExecutionID) AS FillCount FROM brokerage.BrokerageAccounts a JOIN brokerage.TradeOrders o ON o.AccountID=a.AccountID JOIN brokerage.Executions e ON e.OrderID=o.OrderID GROUP BY a.ClientID) SELECT c.ClientID,c.ClientName,COALESCE(a.GrossValue,0) AS GrossValue,COALESCE(a.FillCount,0) AS FillCount FROM brokerage.Clients c LEFT JOIN Activity a ON a.ClientID=c.ClientID ORDER BY c.ClientID;
```

**Check and explain:** 5 clients. Client 1: gross 249.60 and 4 fills; client 2: 303 and 1 fill; client 3: 150 and 1 fill; clients 4 and 5: zero. These are executed notionals, not balances or profits.
