# Retail Manufacturing: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_MANUFACTURING-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.ProductID, p.ProductName, COUNT(f.ProductionOrderID) AS EventCount, SUM(f.PlannedCost) AS TotalAmount FROM [retail_manufacturing].[Products] p LEFT JOIN [retail_manufacturing].[ProductionOrders] f ON p.ProductID=f.ProductID GROUP BY p.ProductID, p.ProductName ORDER BY p.ProductID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### RETAIL_MANUFACTURING-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.ProductID, p.ProductName FROM [retail_manufacturing].[Products] p WHERE NOT EXISTS (SELECT 1 FROM [retail_manufacturing].[ProductionOrders] f WHERE f.ProductID=p.ProductID) ORDER BY p.ProductID;
```

**Check and explain:** Only master ID 5.

### RETAIL_MANUFACTURING-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT ProductionOrderID,ProductID,PlannedCost,ROW_NUMBER() OVER(PARTITION BY ProductID ORDER BY PlannedCost DESC,ProductionOrderID) AS rn FROM [retail_manufacturing].[ProductionOrders]) SELECT ProductionOrderID,ProductID,PlannedCost FROM Ranked WHERE rn=1 ORDER BY ProductID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### RETAIL_MANUFACTURING-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT u.UsageID,o.ProductionReference,p.ProductName,m.MaterialName,u.QuantityUsed,b.QuantityPerUnit FROM retail_manufacturing.MaterialUsage u JOIN retail_manufacturing.ProductionOrders o ON o.ProductionOrderID=u.ProductionOrderID JOIN retail_manufacturing.Products p ON p.ProductID=o.ProductID JOIN retail_manufacturing.Materials m ON m.MaterialID=u.MaterialID LEFT JOIN retail_manufacturing.BillOfMaterials b ON b.ProductID=o.ProductID AND b.MaterialID=u.MaterialID ORDER BY u.UsageID;
```

**Check and explain:** 6 rows. Usage 3 is 4.5 units of Fabric for a product requiring 2 units of Fabric per finished unit.

### RETAIL_MANUFACTURING-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Used AS (SELECT ProductionOrderID,MaterialID,SUM(QuantityUsed) AS ActualQuantity FROM retail_manufacturing.MaterialUsage GROUP BY ProductionOrderID,MaterialID) SELECT o.ProductionOrderID,b.MaterialID,o.PlannedUnits,o.PlannedUnits*b.QuantityPerUnit AS RequiredQuantity,COALESCE(u.ActualQuantity,0) AS ActualQuantity,COALESCE(u.ActualQuantity,0)-o.PlannedUnits*b.QuantityPerUnit AS ActualMinusRequired FROM retail_manufacturing.ProductionOrders o JOIN retail_manufacturing.BillOfMaterials b ON b.ProductID=o.ProductID LEFT JOIN Used u ON u.ProductionOrderID=o.ProductionOrderID AND u.MaterialID=b.MaterialID ORDER BY o.ProductionOrderID,b.MaterialID;
```

**Check and explain:** 18 rows. Order 2/material 1: planned units=2, required=4, actual=4.5, difference=0.5. Negative values on unstarted orders indicate unrecorded consumption, not necessarily a favorable completed-production variance.

### RETAIL_MANUFACTURING-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT m.MaterialID,m.MaterialName FROM retail_manufacturing.Materials m WHERE NOT EXISTS(SELECT 1 FROM retail_manufacturing.BillOfMaterials b WHERE b.MaterialID=m.MaterialID) ORDER BY m.MaterialID;
```

**Check and explain:** Material 5 only. Material 4 is in a recipe even though no actual usage is recorded.
