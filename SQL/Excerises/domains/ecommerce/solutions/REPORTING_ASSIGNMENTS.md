# E-commerce: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### ECOMMERCE-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName, COUNT(f.OrderID) AS EventCount, SUM(f.OrderTotal) AS TotalAmount FROM [ecommerce].[Customers] p LEFT JOIN [ecommerce].[Orders] f ON p.CustomerID=f.CustomerID GROUP BY p.CustomerID, p.CustomerName ORDER BY p.CustomerID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### ECOMMERCE-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName FROM [ecommerce].[Customers] p WHERE NOT EXISTS (SELECT 1 FROM [ecommerce].[Orders] f WHERE f.CustomerID=p.CustomerID) ORDER BY p.CustomerID;
```

**Check and explain:** Only master ID 5.

### ECOMMERCE-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT OrderID,CustomerID,OrderTotal,ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY OrderTotal DESC,OrderID) AS rn FROM [ecommerce].[Orders]) SELECT OrderID,CustomerID,OrderTotal FROM Ranked WHERE rn=1 ORDER BY CustomerID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### ECOMMERCE-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT o.OrderID,c.CustomerName,s.SellerName,p.ProductName,i.Quantity,i.UnitPrice,i.Quantity*i.UnitPrice AS LineTotal FROM ecommerce.Orders o JOIN ecommerce.Customers c ON c.CustomerID=o.CustomerID JOIN ecommerce.Sellers s ON s.SellerID=o.SellerID JOIN ecommerce.OrderItems i ON i.OrderID=o.OrderID JOIN ecommerce.Products p ON p.ProductID=i.ProductID ORDER BY o.OrderID,i.OrderItemID;
```

**Check and explain:** 6 rows; line totals sum to 850. Orders 1 and 5 are Seller 1 (Electronics); the charged UnitPrice is used, not the catalog price.

### ECOMMERCE-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Lines AS (SELECT OrderID,SUM(Quantity*UnitPrice) AS LineTotal FROM ecommerce.OrderItems GROUP BY OrderID), Paid AS (SELECT OrderID,SUM(PaidAmount) AS PaidTotal FROM ecommerce.Payments GROUP BY OrderID) SELECT o.OrderID,o.OrderTotal,COALESCE(l.LineTotal,0) AS LineTotal,COALESCE(p.PaidTotal,0) AS PaidTotal,o.OrderTotal-COALESCE(p.PaidTotal,0) AS Outstanding FROM ecommerce.Orders o LEFT JOIN Lines l ON l.OrderID=o.OrderID LEFT JOIN Paid p ON p.OrderID=o.OrderID ORDER BY o.OrderID;
```

**Check and explain:** 12 rows. Order 1 is split between a gift card (40) and a card (60): paid 100, outstanding 0. Order 3 outstanding=100, order 5 is unpaid (outstanding 50) and order 4 keeps NULL outstanding because its OrderTotal is unknown.

### ECOMMERCE-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT s.SellerID,s.SellerName,s.Department,COUNT(o.OrderID) AS OrderCount,COALESCE(SUM(o.OrderTotal),0) AS Revenue,COUNT(DISTINCT o.CustomerID) AS DistinctCustomers FROM ecommerce.Sellers s LEFT JOIN ecommerce.Orders o ON o.SellerID=s.SellerID GROUP BY s.SellerID,s.SellerName,s.Department ORDER BY s.SellerID;
```

**Check and explain:** 5 rows. Seller 2 has the highest revenue (580); Seller 4 has 3 orders from 2 distinct customers; the unused seller shows zero orders and zero revenue.
