-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [oil].[Sites] (SiteID, SiteName, SiteCode, Region) VALUES
(1,N'Sites Alpha',N'SIT-1',N'North'),
(2,N'Sites Beta',N'SIT-2',N'South'),
(3,N'Sites Gamma',N'SIT-3',N'North'),
(4,N'Sites Delta',N'SIT-4',N'West'),
(5,N'Sites Unused',N'SIT-5',N'East');
INSERT INTO [oil].[Carriers] (CarrierID, CarrierName, CarrierCode, Active) VALUES
(1,N'Carrier 1',N'CR-1',1),
(2,N'Carrier 2',N'CR-2',1),
(3,N'Carrier 3',N'CR-3',1),
(4,N'Carrier 4',N'CR-4',1),
(5,N'Carrier 5',N'CR-5',0);
INSERT INTO [oil].[Products] (ProductID, ProductName, ProductCode, PricePerUnit) VALUES
(1,N'Grade 1',N'OIL-1',20),
(2,N'Grade 2',N'OIL-2',40),
(3,N'Grade 3',N'OIL-3',60),
(4,N'Grade 4',N'OIL-4',80),
(5,N'Grade 5',N'OIL-5',100);
INSERT INTO [oil].[Shipments] (ShipmentID, SiteID, ShipmentReference, ShipmentType, Status, ShipmentValue, UnitCount, ShipDate, DispatchedAt, RecordedAt, Note, BackupNote, ParentShipmentID, CarrierID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4);
INSERT INTO [oil].[ShipmentItems] (ShipmentItemID, ShipmentID, ProductID, Quantity, PricePerUnit) VALUES
(1,1,1,3,20),
(2,1,2,1,40),
(3,2,2,5,40),
(4,3,1,10,20),
(5,6,3,5,60);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
