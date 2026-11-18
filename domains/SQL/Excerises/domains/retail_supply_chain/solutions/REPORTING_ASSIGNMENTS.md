# Retail Supply Chain: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_SUPPLY_CHAIN-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.WarehouseID, p.WarehouseName, COUNT(f.MovementID) AS EventCount, SUM(f.MovementValue) AS TotalAmount FROM [retail_supply_chain].[Warehouses] p LEFT JOIN [retail_supply_chain].[StockMovements] f ON p.WarehouseID=f.WarehouseID GROUP BY p.WarehouseID, p.WarehouseName ORDER BY p.WarehouseID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### RETAIL_SUPPLY_CHAIN-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.WarehouseID, p.WarehouseName FROM [retail_supply_chain].[Warehouses] p WHERE NOT EXISTS (SELECT 1 FROM [retail_supply_chain].[StockMovements] f WHERE f.WarehouseID=p.WarehouseID) ORDER BY p.WarehouseID;
```

**Check and explain:** Only master ID 5.

### RETAIL_SUPPLY_CHAIN-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT MovementID,WarehouseID,MovementValue,ROW_NUMBER() OVER(PARTITION BY WarehouseID ORDER BY MovementValue DESC,MovementID) AS rn FROM [retail_supply_chain].[StockMovements]) SELECT MovementID,WarehouseID,MovementValue FROM Ranked WHERE rn=1 ORDER BY WarehouseID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### RETAIL_SUPPLY_CHAIN-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT m.MovementID,w.WarehouseName,p.ProductName,p.Sourcing,s.SupplierName,m.Direction,m.MovedUnits,b.QuantityOnHand FROM retail_supply_chain.StockMovements m JOIN retail_supply_chain.Warehouses w ON w.WarehouseID=m.WarehouseID JOIN retail_supply_chain.Products p ON p.ProductID=m.ProductID JOIN retail_supply_chain.Suppliers s ON s.SupplierID=m.SupplierID LEFT JOIN retail_supply_chain.StockBalances b ON b.WarehouseID=m.WarehouseID AND b.ProductID=m.ProductID ORDER BY m.MovementID;
```

**Check and explain:** 12 rows; every seed movement resolves to one warehouse/product snapshot. Movements 3, 4, 7, 8, 11 and 12 are Made products supplied by the Private Label Plant. A warehouse-only join to StockBalances would multiply rows.

### RETAIL_SUPPLY_CHAIN-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Recipe AS (SELECT o.ProductionOrderID,SUM(o.PlannedUnits*b.QuantityPerUnit) AS RequiredUnits FROM retail_supply_chain.ProductionOrders o JOIN retail_supply_chain.BillOfMaterials b ON b.ProductID=o.ProductID GROUP BY o.ProductionOrderID), Used AS (SELECT ProductionOrderID,SUM(QuantityUsed) AS UsedUnits FROM retail_supply_chain.MaterialUsage GROUP BY ProductionOrderID), Received AS (SELECT ProductionOrderID,SUM(MovedUnits) AS ReceivedUnits FROM retail_supply_chain.StockMovements WHERE Direction='IN' AND ProductionOrderID IS NOT NULL GROUP BY ProductionOrderID) SELECT o.ProductionReference,p.ProductName,o.ProductionStatus,o.PlannedUnits,COALESCE(r.RequiredUnits,0) AS RequiredUnits,COALESCE(u.UsedUnits,0) AS UsedUnits,COALESCE(x.ReceivedUnits,0) AS ReceivedUnits FROM retail_supply_chain.ProductionOrders o JOIN retail_supply_chain.Products p ON p.ProductID=o.ProductID LEFT JOIN Recipe r ON r.ProductionOrderID=o.ProductionOrderID LEFT JOIN Used u ON u.ProductionOrderID=o.ProductionOrderID LEFT JOIN Received x ON x.ProductionOrderID=o.ProductionOrderID ORDER BY o.ProductionOrderID;
```

**Check and explain:** 4 rows. PO-1: required 30, used 30.5 (0.5 over the recipe) and 3 units received so far. PO-2 is Completed but nothing is received yet. PO-3 has used 8 of 24 required units; PO-4 is Planned with no usage. Joining recipe, usage and receipts before aggregating would multiply the totals.

### RETAIL_SUPPLY_CHAIN-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Net AS (SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM retail_supply_chain.StockMovements GROUP BY WarehouseID,ProductID) SELECT b.WarehouseID,b.ProductID,b.OpeningQuantity,COALESCE(n.NetUnits,0) AS NetUnits,b.OpeningQuantity+COALESCE(n.NetUnits,0) AS ExpectedOnHand,b.QuantityOnHand,b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0)) AS Discrepancy FROM retail_supply_chain.StockBalances b LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID ORDER BY b.WarehouseID,b.ProductID;
```

**Check and explain:** 12 rows; all discrepancies=0. Warehouse 2/product 4: opening=10, net=8, on-hand=18. Warehouse 1/product 5 has no movements (net 0). Total opening=120 and total on-hand=130.
