# Pharma: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### PHARMA-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.SupplierID, p.SupplierName, COUNT(f.BatchID) AS EventCount, SUM(f.BatchCost) AS TotalAmount FROM [pharma].[Suppliers] p LEFT JOIN [pharma].[Batches] f ON p.SupplierID=f.SupplierID GROUP BY p.SupplierID, p.SupplierName ORDER BY p.SupplierID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### PHARMA-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.SupplierID, p.SupplierName FROM [pharma].[Suppliers] p WHERE NOT EXISTS (SELECT 1 FROM [pharma].[Batches] f WHERE f.SupplierID=p.SupplierID) ORDER BY p.SupplierID;
```

**Check and explain:** Only master ID 5.

### PHARMA-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT BatchID,SupplierID,BatchCost,ROW_NUMBER() OVER(PARTITION BY SupplierID ORDER BY BatchCost DESC,BatchID) AS rn FROM [pharma].[Batches]) SELECT BatchID,SupplierID,BatchCost FROM Ranked WHERE rn=1 ORDER BY SupplierID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### PHARMA-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT i.InventoryID,b.BatchCode,s.SupplierName,p.ProductName,w.WarehouseName,i.QuantityOnHand FROM pharma.Inventory i JOIN pharma.Batches b ON b.BatchID=i.BatchID JOIN pharma.Suppliers s ON s.SupplierID=b.SupplierID JOIN pharma.Products p ON p.ProductID=b.ProductID JOIN pharma.Warehouses w ON w.WarehouseID=i.WarehouseID ORDER BY i.InventoryID;
```

**Check and explain:** 6 inventory rows; quantity total=150.

### PHARMA-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Stock AS (SELECT BatchID,SUM(QuantityOnHand) AS Units FROM pharma.Inventory GROUP BY BatchID) SELECT b.BatchID,s.SupplierName,b.BatchCost,COALESCE(x.Units,0) AS StockUnits FROM pharma.Batches b JOIN pharma.Suppliers s ON s.SupplierID=b.SupplierID LEFT JOIN Stock x ON x.BatchID=b.BatchID ORDER BY b.BatchID;
```

**Check and explain:** 12 rows. Batch 1 has 50 units and cost 100 once. Batch 4 has zero stock and unknown cost.

### PHARMA-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT w.WarehouseID,w.WarehouseName FROM pharma.Warehouses w WHERE NOT EXISTS(SELECT 1 FROM pharma.Inventory i WHERE i.WarehouseID=w.WarehouseID) ORDER BY w.WarehouseID;
```

**Check and explain:** Warehouse 5 only. Warehouse 4 has an inventory row with zero quantity and is not returned.
