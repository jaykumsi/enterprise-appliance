# Retail Logistics: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## RETAIL_LOGISTICS-REPORT-01: Master activity

Return each Customers ID and name, including masters with no Shipments, with the count of related events and total known FreightCharge. Order by master ID.

## RETAIL_LOGISTICS-REPORT-02: No activity

Return Customers with no related Shipments using NOT EXISTS.

## RETAIL_LOGISTICS-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest FreightCharge event for each active master. Break ties by ShipmentID ascending.

## RETAIL_LOGISTICS-REPORT-04: Latest package location

Show every package, its shipment ID, customer name, carrier name, latest tracking status and scan time. Join all five tables, choosing the latest scan by ScanTime descending then TrackingEventID descending. Keep packages with no scan.

## RETAIL_LOGISTICS-REPORT-05: Delivered late

Find packages whose first Delivered scan occurred on a calendar date after PromisedDate. Show package ID, promised date and first delivery time. A package without a Delivered scan must not be labeled delivered late.

## RETAIL_LOGISTICS-REPORT-06: Freight and package reconciliation

Return all shipments with recorded freight charge, declared package count and actual package count. Pre-aggregate package rows; do not join raw tracking scans into monetary totals.
