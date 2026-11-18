# Retail Supply Chain: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## RETAIL_SUPPLY_CHAIN-REPORT-01: Master activity

Return each Warehouses ID and name, including masters with no StockMovements, with the count of related events and total known MovementValue. Order by master ID.

## RETAIL_SUPPLY_CHAIN-REPORT-02: No activity

Return Warehouses with no related StockMovements using NOT EXISTS.

## RETAIL_SUPPLY_CHAIN-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest MovementValue event for each active master. Break ties by MovementID ascending.

## RETAIL_SUPPLY_CHAIN-REPORT-04: Movement provenance

Show every stock movement with warehouse, product, sourcing, originating supplier, direction, moved units and the matching current on-hand balance using five tables. Join balances on BOTH warehouse and product.

## RETAIL_SUPPLY_CHAIN-REPORT-05: Factory to shelf

For every production order show its reference, product name, status, planned units, required material units (recipe quantity times PlannedUnits), material units used and units received into stock (IN movements that point to the order). Aggregate the recipe, the usage and the receipts separately before joining; missing values count as zero.

## RETAIL_SUPPLY_CHAIN-REPORT-06: Ledger reconciliation

For each warehouse/product snapshot, show opening quantity, signed net movement (IN positive, OUT negative), expected on-hand, stored on-hand and stored-minus-expected discrepancy. Include snapshots with no movements. All supplied movements are after the opening snapshot.
