# Retail Manufacturing: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## RETAIL_MANUFACTURING-REPORT-01: Master activity

Return each Products ID and name, including masters with no ProductionOrders, with the count of related events and total known PlannedCost. Order by master ID.

## RETAIL_MANUFACTURING-REPORT-02: No activity

Return Products with no related ProductionOrders using NOT EXISTS.

## RETAIL_MANUFACTURING-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest PlannedCost event for each active master. Break ties by ProductionOrderID ascending.

## RETAIL_MANUFACTURING-REPORT-04: Production consumption trace

For each material-usage row, show production reference, product name, material name, actual quantity and recipe quantity per unit. Join all five tables; keep usage with no matching recipe using a LEFT JOIN to BillOfMaterials.

## RETAIL_MANUFACTURING-REPORT-05: Recipe versus actual

For every production order and recipe material, show planned units, required material quantity, actual usage (zero when missing) and ActualMinusRequired. Multiply recipe quantity by PlannedUnits; aggregate usage for each order and material pair before joining.

## RETAIL_MANUFACTURING-REPORT-06: Materials outside recipes

Return materials not used in any bill of materials. Explain how this differs from a recipe material that has not yet been consumed.
