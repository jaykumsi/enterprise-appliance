# Retail Inventory: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## RETAIL_INVENTORY-REPORT-01: Master activity

Return each Warehouses ID and name, including masters with no StockMovements, with the count of related events and total known MovementValue. Order by master ID.

## RETAIL_INVENTORY-REPORT-02: No activity

Return Warehouses with no related StockMovements using NOT EXISTS.

## RETAIL_INVENTORY-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest MovementValue event for each active master. Break ties by MovementID ascending.

## RETAIL_INVENTORY-REPORT-04: Movement provenance

Show every stock movement with warehouse, product, originating supplier, direction, moved units and the matching current on-hand balance using all five tables. Join balances on BOTH warehouse and product.

## RETAIL_INVENTORY-REPORT-05: Ledger reconciliation

For each warehouse/product snapshot, show opening quantity, signed net movement (IN positive, OUT negative), expected on-hand, stored on-hand and stored-minus-expected discrepancy. Include snapshots with no movements. All supplied movements are after the opening snapshot.

## RETAIL_INVENTORY-REPORT-06: Replenishment and stock value

Find warehouse/product balances below ReorderLevel. Show warehouse ID, product name, on-hand units, reorder level, units needed to reach that level and current stock value at the product UnitCost.
