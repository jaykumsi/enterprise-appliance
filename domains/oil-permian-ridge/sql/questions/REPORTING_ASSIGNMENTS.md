# Oil: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../SQL/Excerises/BEGINNER_GUIDE.md).

## OIL-REPORT-01: Master activity

Return each Sites ID and name, including masters with no Shipments, with the count of related events and total known ShipmentValue. Order by master ID.

## OIL-REPORT-02: No activity

Return Sites with no related Shipments using NOT EXISTS.

## OIL-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest ShipmentValue event for each active master. Break ties by ShipmentID ascending.

## OIL-REPORT-04: Shipment trace

Show each shipment line with site name, carrier name, product name, quantity and historical price per unit using all five tables.

## OIL-REPORT-05: Shipment reconciliation

List every shipment, site name, carrier name, recorded shipment value and total of quantity times historical price. Include missing detail as zero; return recorded value minus line total as Difference.

## OIL-REPORT-06: Unused carriers

List carriers never assigned to any shipment, including their Active flag.
