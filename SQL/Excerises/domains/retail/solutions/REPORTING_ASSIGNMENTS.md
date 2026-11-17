# Retail: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName, COUNT(f.OrderID) AS EventCount, SUM(f.OrderTotal) AS TotalAmount FROM [retail].[Customers] p LEFT JOIN [retail].[Orders] f ON p.CustomerID=f.CustomerID GROUP BY p.CustomerID, p.CustomerName ORDER BY p.CustomerID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### RETAIL-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName FROM [retail].[Customers] p WHERE NOT EXISTS (SELECT 1 FROM [retail].[Orders] f WHERE f.CustomerID=p.CustomerID) ORDER BY p.CustomerID;
```

**Check and explain:** Only master ID 5.

### RETAIL-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT OrderID,CustomerID,OrderTotal,ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY OrderTotal DESC,OrderID) AS rn FROM [retail].[Orders]) SELECT OrderID,CustomerID,OrderTotal FROM Ranked WHERE rn=1 ORDER BY CustomerID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### RETAIL-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT o.OrderID,c.CustomerName,p.ProductName,i.Quantity,i.UnitPrice,i.Quantity*i.UnitPrice AS LineTotal FROM [retail].[Orders] o JOIN [retail].[Customers] c ON c.CustomerID=o.CustomerID JOIN [retail].[OrderItems] i ON i.OrderID=o.OrderID JOIN [retail].[Products] p ON p.ProductID=i.ProductID ORDER BY o.OrderID,i.OrderItemID;
```

**Check and explain:** 6 rows; line totals sum to 850. Product catalog prices are not substituted for historical line prices.

### RETAIL-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Lines AS (SELECT OrderID,SUM(Quantity*UnitPrice) AS LineTotal FROM retail.OrderItems GROUP BY OrderID), Paid AS (SELECT OrderID,SUM(PaidAmount) AS PaidTotal FROM retail.Payments GROUP BY OrderID) SELECT o.OrderID,o.OrderTotal,COALESCE(l.LineTotal,0) AS LineTotal,COALESCE(p.PaidTotal,0) AS PaidTotal,o.OrderTotal-COALESCE(p.PaidTotal,0) AS Outstanding FROM retail.Orders o LEFT JOIN Lines l ON l.OrderID=o.OrderID LEFT JOIN Paid p ON p.OrderID=o.OrderID ORDER BY o.OrderID;
```

**Check and explain:** 12 rows. Order 1 has line total 100, paid 100, outstanding 0 despite having two lines and two payments. Order 3 outstanding=100. Order 4 outstanding=NULL.

### RETAIL-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.ProductID,p.ProductName FROM retail.Products p WHERE NOT EXISTS(SELECT 1 FROM retail.OrderItems i WHERE i.ProductID=p.ProductID) ORDER BY p.ProductID;
```

**Check and explain:** Products 4 and 5.
