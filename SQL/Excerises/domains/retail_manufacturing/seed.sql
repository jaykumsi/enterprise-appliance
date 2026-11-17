-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_manufacturing].[Products] (ProductID, ProductName, ProductCode, Region) VALUES
(1,N'Products Alpha',N'PRO-1',N'North'),
(2,N'Products Beta',N'PRO-2',N'South'),
(3,N'Products Gamma',N'PRO-3',N'North'),
(4,N'Products Delta',N'PRO-4',N'West'),
(5,N'Products Unused',N'PRO-5',N'East');
INSERT INTO [retail_manufacturing].[Materials] (MaterialID, MaterialName, MaterialCode, UnitCost) VALUES
(1,N'Fabric',N'MAT-1',5),
(2,N'Thread',N'MAT-2',1),
(3,N'Zipper',N'MAT-3',2),
(4,N'Packaging',N'MAT-4',3),
(5,N'Unused trim',N'MAT-5',4);
INSERT INTO [retail_manufacturing].[ProductionOrders] (ProductionOrderID, ProductID, ProductionReference, ProductionCategory, Status, PlannedCost, PlannedUnits, ProductionDate, StartedAt, RecordedAt, Note, BackupNote, ParentProductionOrderID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6);
INSERT INTO [retail_manufacturing].[BillOfMaterials] (BOMID, ProductID, MaterialID, QuantityPerUnit) VALUES
(1,1,1,2),
(2,1,2,1),
(3,2,1,1),
(4,2,3,2),
(5,3,4,1),
(6,4,2,3);
INSERT INTO [retail_manufacturing].[MaterialUsage] (UsageID, ProductionOrderID, MaterialID, QuantityUsed, UsageDate) VALUES
(1,1,1,2,N'20240101'),
(2,1,2,1,N'20240101'),
(3,2,1,4.5,N'20240102'),
(4,2,2,2,N'20240102'),
(5,3,1,3,N'20240102'),
(6,3,3,7,N'20240102');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
