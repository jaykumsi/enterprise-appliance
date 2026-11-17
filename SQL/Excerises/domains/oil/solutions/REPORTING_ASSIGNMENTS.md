# Oil: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### OIL-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.SiteID, p.SiteName, COUNT(f.ShipmentID) AS EventCount, SUM(f.ShipmentValue) AS TotalAmount FROM [oil].[Sites] p LEFT JOIN [oil].[Shipments] f ON p.SiteID=f.SiteID GROUP BY p.SiteID, p.SiteName ORDER BY p.SiteID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### OIL-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.SiteID, p.SiteName FROM [oil].[Sites] p WHERE NOT EXISTS (SELECT 1 FROM [oil].[Shipments] f WHERE f.SiteID=p.SiteID) ORDER BY p.SiteID;
```

**Check and explain:** Only master ID 5.

### OIL-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT ShipmentID,SiteID,ShipmentValue,ROW_NUMBER() OVER(PARTITION BY SiteID ORDER BY ShipmentValue DESC,ShipmentID) AS rn FROM [oil].[Shipments]) SELECT ShipmentID,SiteID,ShipmentValue FROM Ranked WHERE rn=1 ORDER BY SiteID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### OIL-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT i.ShipmentItemID,s.SiteName,c.CarrierName,p.ProductName,i.Quantity,i.PricePerUnit FROM oil.ShipmentItems i JOIN oil.Shipments h ON h.ShipmentID=i.ShipmentID JOIN oil.Sites s ON s.SiteID=h.SiteID JOIN oil.Carriers c ON c.CarrierID=h.CarrierID JOIN oil.Products p ON p.ProductID=i.ProductID ORDER BY i.ShipmentItemID;
```

**Check and explain:** 5 line rows; each resolves to a site, carrier and product.

### OIL-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Lines AS (SELECT ShipmentID,SUM(Quantity*PricePerUnit) AS LineTotal FROM oil.ShipmentItems GROUP BY ShipmentID) SELECT h.ShipmentID,s.SiteName,c.CarrierName,h.ShipmentValue,COALESCE(l.LineTotal,0) AS LineTotal,h.ShipmentValue-COALESCE(l.LineTotal,0) AS Difference FROM oil.Shipments h JOIN oil.Sites s ON s.SiteID=h.SiteID JOIN oil.Carriers c ON c.CarrierID=h.CarrierID LEFT JOIN Lines l ON l.ShipmentID=h.ShipmentID ORDER BY h.ShipmentID;
```

**Check and explain:** 12 shipments; shipment 1 line total=100 and Difference=0. Shipment 4 Difference=NULL. All known recorded values sum to 1700.

### OIL-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT c.CarrierID,c.CarrierName,c.Active FROM oil.Carriers c WHERE NOT EXISTS(SELECT 1 FROM oil.Shipments s WHERE s.CarrierID=c.CarrierID) ORDER BY c.CarrierID;
```

**Check and explain:** Carrier 5, Active=0.
