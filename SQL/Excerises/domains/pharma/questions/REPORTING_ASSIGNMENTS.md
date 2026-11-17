# Pharma: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## PHARMA-REPORT-01: Master activity

Return each Suppliers ID and name, including masters with no Batches, with the count of related events and total known BatchCost. Order by master ID.

## PHARMA-REPORT-02: No activity

Return Suppliers with no related Batches using NOT EXISTS.

## PHARMA-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest BatchCost event for each active master. Break ties by BatchID ascending.

## PHARMA-REPORT-04: Batch location trace

Show inventory ID, batch code, supplier name, product name, warehouse name and quantity on hand by joining all five tables.

## PHARMA-REPORT-05: Batch stock

List every batch with supplier name, batch cost and total stock across warehouses. Include unstocked batches with zero units; do not multiply batch cost by location count.

## PHARMA-REPORT-06: Empty warehouses

Return warehouses with no inventory rows; distinguish this from a warehouse holding a zero-quantity inventory row.
