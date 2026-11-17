-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [pharma].[Suppliers] (SupplierID, SupplierName, SupplierCode, Region) VALUES
(1,N'Suppliers Alpha',N'SUP-1',N'North'),
(2,N'Suppliers Beta',N'SUP-2',N'South'),
(3,N'Suppliers Gamma',N'SUP-3',N'North'),
(4,N'Suppliers Delta',N'SUP-4',N'West'),
(5,N'Suppliers Unused',N'SUP-5',N'East');
INSERT INTO [pharma].[Products] (ProductID, ProductName, ProductCode, StandardCost) VALUES
(1,N'Compound 1',N'PR-1',10),
(2,N'Compound 2',N'PR-2',20),
(3,N'Compound 3',N'PR-3',30),
(4,N'Compound 4',N'PR-4',40),
(5,N'Compound 5',N'PR-5',50);
INSERT INTO [pharma].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Capacity) VALUES
(1,N'Warehouse 1',N'WH-1',100),
(2,N'Warehouse 2',N'WH-2',200),
(3,N'Warehouse 3',N'WH-3',300),
(4,N'Warehouse 4',N'WH-4',400),
(5,N'Warehouse 5',N'WH-5',500);
INSERT INTO [pharma].[Batches] (BatchID, SupplierID, BatchCode, BatchType, Status, BatchCost, PackCount, ManufactureDate, ProducedAt, RecordedAt, Note, BackupNote, ParentBatchID, ProductID) VALUES
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
INSERT INTO [pharma].[Inventory] (InventoryID, BatchID, WarehouseID, QuantityOnHand, LastCountDate) VALUES
(1,1,1,20,N'20240105'),
(2,1,2,30,N'20240105'),
(3,2,1,40,N'20240105'),
(4,3,3,10,N'20240106'),
(5,5,4,0,N'20240205'),
(6,6,2,50,N'20240212');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
