# Retail Inventory: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_INVENTORY-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.WarehouseID, p.WarehouseName, COUNT(f.MovementID) AS EventCount, SUM(f.MovementValue) AS TotalAmount FROM [retail_inventory].[Warehouses] p LEFT JOIN [retail_inventory].[StockMovements] f ON p.WarehouseID=f.WarehouseID GROUP BY p.WarehouseID, p.WarehouseName ORDER BY p.WarehouseID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### RETAIL_INVENTORY-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.WarehouseID, p.WarehouseName FROM [retail_inventory].[Warehouses] p WHERE NOT EXISTS (SELECT 1 FROM [retail_inventory].[StockMovements] f WHERE f.WarehouseID=p.WarehouseID) ORDER BY p.WarehouseID;
```

**Check and explain:** Only master ID 5.

### RETAIL_INVENTORY-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT MovementID,WarehouseID,MovementValue,ROW_NUMBER() OVER(PARTITION BY WarehouseID ORDER BY MovementValue DESC,MovementID) AS rn FROM [retail_inventory].[StockMovements]) SELECT MovementID,WarehouseID,MovementValue FROM Ranked WHERE rn=1 ORDER BY WarehouseID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### RETAIL_INVENTORY-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT m.MovementID,w.WarehouseName,p.ProductName,s.SupplierName,m.Direction,m.MovedUnits,b.QuantityOnHand FROM retail_inventory.StockMovements m JOIN retail_inventory.Warehouses w ON w.WarehouseID=m.WarehouseID JOIN retail_inventory.Products p ON p.ProductID=m.ProductID JOIN retail_inventory.Suppliers s ON s.SupplierID=m.SupplierID LEFT JOIN retail_inventory.StockBalances b ON b.WarehouseID=m.WarehouseID AND b.ProductID=m.ProductID ORDER BY m.MovementID;
```

**Check and explain:** 12 rows; every seed movement resolves to one warehouse/product snapshot. A warehouse-only join would multiply rows.

### RETAIL_INVENTORY-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Net AS (SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM retail_inventory.StockMovements GROUP BY WarehouseID,ProductID) SELECT b.WarehouseID,b.ProductID,b.OpeningQuantity,COALESCE(n.NetUnits,0) AS NetUnits,b.OpeningQuantity+COALESCE(n.NetUnits,0) AS ExpectedOnHand,b.QuantityOnHand,b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0)) AS Discrepancy FROM retail_inventory.StockBalances b LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID ORDER BY b.WarehouseID,b.ProductID;
```

**Check and explain:** 11 rows; all discrepancies=0. Warehouse 2/product 4: opening=10, net=8, on-hand=18. Total opening=110 and total on-hand=120.

### RETAIL_INVENTORY-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT b.WarehouseID,p.ProductName,b.QuantityOnHand,b.ReorderLevel,b.ReorderLevel-b.QuantityOnHand AS UnitsToReorder,b.QuantityOnHand*p.UnitCost AS StockValue FROM retail_inventory.StockBalances b JOIN retail_inventory.Products p ON p.ProductID=b.ProductID WHERE b.QuantityOnHand<b.ReorderLevel ORDER BY b.WarehouseID,b.ProductID;
```

**Check and explain:** 4 rows: (warehouse,product)=(1,2),(1,3),(3,1),(4,4). Units to reorder are 2,3,1,4 respectively.
