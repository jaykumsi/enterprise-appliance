-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_logistics].[Customers] (CustomerID, CustomerName, CustomerCode, Region) VALUES
(1,N'Customers Alpha',N'CUS-1',N'North'),
(2,N'Customers Beta',N'CUS-2',N'South'),
(3,N'Customers Gamma',N'CUS-3',N'North'),
(4,N'Customers Delta',N'CUS-4',N'West'),
(5,N'Customers Unused',N'CUS-5',N'East');
INSERT INTO [retail_logistics].[Carriers] (CarrierID, CarrierName, CarrierCode, ServiceLevel) VALUES
(1,N'Logistics carrier 1',N'LOG-1',N'Express'),
(2,N'Logistics carrier 2',N'LOG-2',N'Standard'),
(3,N'Logistics carrier 3',N'LOG-3',N'Express'),
(4,N'Logistics carrier 4',N'LOG-4',N'Standard'),
(5,N'Logistics carrier 5',N'LOG-5',N'Express');
INSERT INTO [retail_logistics].[Shipments] (ShipmentID, CustomerID, ShipmentReference, ShipmentCategory, Status, FreightCharge, DeclaredPackages, ShipDate, DispatchedAt, RecordedAt, Note, BackupNote, ParentShipmentID, CarrierID) VALUES
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
INSERT INTO [retail_logistics].[ShipmentPackages] (PackageID, ShipmentID, TrackingNumber, WeightKg, PromisedDate) VALUES
(1,1,N'TRK-1',2,N'20240103'),
(2,1,N'TRK-2',3,N'20240103'),
(3,2,N'TRK-3',1,N'20240104'),
(4,3,N'TRK-4',4,N'20240104'),
(5,6,N'TRK-5',2,N'20240212');
INSERT INTO [retail_logistics].[TrackingEvents] (TrackingEventID, PackageID, ScanReference, EventStatus, ScanTime, LocationName) VALUES
(1,1,N'SCAN-1',N'PickedUp',N'2024-01-01T13:00:00',N'Origin hub'),
(2,1,N'SCAN-2',N'Delivered',N'2024-01-03T10:00:00',N'Customer address'),
(3,2,N'SCAN-3',N'InTransit',N'2024-01-02T09:00:00',N'Regional hub'),
(4,3,N'SCAN-4',N'Delivered',N'2024-01-05T11:00:00',N'Customer address'),
(5,4,N'SCAN-5',N'PickedUp',N'2024-01-03T08:00:00',N'Origin hub');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
