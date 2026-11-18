# Retail Logistics: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### RETAIL_LOGISTICS-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName, COUNT(f.ShipmentID) AS EventCount, SUM(f.FreightCharge) AS TotalAmount FROM [retail_logistics].[Customers] p LEFT JOIN [retail_logistics].[Shipments] f ON p.CustomerID=f.CustomerID GROUP BY p.CustomerID, p.CustomerName ORDER BY p.CustomerID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### RETAIL_LOGISTICS-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.CustomerID, p.CustomerName FROM [retail_logistics].[Customers] p WHERE NOT EXISTS (SELECT 1 FROM [retail_logistics].[Shipments] f WHERE f.CustomerID=p.CustomerID) ORDER BY p.CustomerID;
```

**Check and explain:** Only master ID 5.

### RETAIL_LOGISTICS-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT ShipmentID,CustomerID,FreightCharge,ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY FreightCharge DESC,ShipmentID) AS rn FROM [retail_logistics].[Shipments]) SELECT ShipmentID,CustomerID,FreightCharge FROM Ranked WHERE rn=1 ORDER BY CustomerID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### RETAIL_LOGISTICS-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Latest AS (SELECT PackageID,EventStatus,ScanTime,ROW_NUMBER() OVER(PARTITION BY PackageID ORDER BY ScanTime DESC,TrackingEventID DESC) AS rn FROM retail_logistics.TrackingEvents) SELECT p.PackageID,h.ShipmentID,c.CustomerName,r.CarrierName,l.EventStatus,l.ScanTime FROM retail_logistics.ShipmentPackages p JOIN retail_logistics.Shipments h ON h.ShipmentID=p.ShipmentID JOIN retail_logistics.Customers c ON c.CustomerID=h.CustomerID JOIN retail_logistics.Carriers r ON r.CarrierID=h.CarrierID LEFT JOIN Latest l ON l.PackageID=p.PackageID AND l.rn=1 ORDER BY p.PackageID;
```

**Check and explain:** 5 rows. Package 1 is Delivered; package 2 is InTransit; package 5 has NULL status/time.

### RETAIL_LOGISTICS-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Delivered AS (SELECT PackageID,MIN(ScanTime) AS DeliveredAt FROM retail_logistics.TrackingEvents WHERE EventStatus='Delivered' GROUP BY PackageID) SELECT p.PackageID,p.PromisedDate,d.DeliveredAt FROM retail_logistics.ShipmentPackages p JOIN Delivered d ON d.PackageID=p.PackageID WHERE CONVERT(date,d.DeliveredAt)>p.PromisedDate ORDER BY p.PackageID;
```

**Check and explain:** Package 3 only: promised 2024-01-04, first delivered 2024-01-05. Package 1 was delivered on its promised date.

### RETAIL_LOGISTICS-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Packages AS (SELECT ShipmentID,COUNT(*) AS ActualPackages FROM retail_logistics.ShipmentPackages GROUP BY ShipmentID) SELECT s.ShipmentID,s.FreightCharge,s.DeclaredPackages,COALESCE(p.ActualPackages,0) AS ActualPackages FROM retail_logistics.Shipments s LEFT JOIN Packages p ON p.ShipmentID=s.ShipmentID ORDER BY s.ShipmentID;
```

**Check and explain:** 12 rows; known freight charges total 1700 once each. Shipment 1 declares 1 package but has 2 recorded packages: flag the mismatch rather than changing the seed.
