-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_inventory].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Region) VALUES
(1,N'Warehouses Alpha',N'WAR-1',N'North'),
(2,N'Warehouses Beta',N'WAR-2',N'South'),
(3,N'Warehouses Gamma',N'WAR-3',N'North'),
(4,N'Warehouses Delta',N'WAR-4',N'West'),
(5,N'Warehouses Unused',N'WAR-5',N'East');
INSERT INTO [retail_inventory].[Products] (ProductID, ProductName, SKU, UnitCost) VALUES
(1,N'Inventory product 1',N'INV-SKU-1',10),
(2,N'Inventory product 2',N'INV-SKU-2',20),
(3,N'Inventory product 3',N'INV-SKU-3',30),
(4,N'Inventory product 4',N'INV-SKU-4',40),
(5,N'Inventory product 5',N'INV-SKU-5',50);
INSERT INTO [retail_inventory].[Suppliers] (SupplierID, SupplierName, SupplierCode, LeadTimeDays) VALUES
(1,N'Inventory supplier 1',N'INV-SUP-1',2),
(2,N'Inventory supplier 2',N'INV-SUP-2',3),
(3,N'Inventory supplier 3',N'INV-SUP-3',4),
(4,N'Inventory supplier 4',N'INV-SUP-4',5),
(5,N'Inventory supplier 5',N'INV-SUP-5',6);
INSERT INTO [retail_inventory].[StockMovements] (MovementID, WarehouseID, MovementReference, MovementCategory, Status, MovementValue, MovedUnits, MovementDate, MovedAt, RecordedAt, Note, BackupNote, ParentMovementID, ProductID, SupplierID, Direction) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,1,N'IN'),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,2,N'OUT'),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,3,N'IN'),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,4,N'IN'),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,1,N'OUT'),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,2,N'IN'),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,3,N'IN'),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,4,N'OUT'),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,1,N'IN'),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,2,N'IN'),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,3,N'OUT'),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,4,N'IN');
INSERT INTO [retail_inventory].[StockBalances] (BalanceID, WarehouseID, ProductID, OpeningQuantity, QuantityOnHand, ReorderLevel) VALUES
(1,1,1,10,11,10),
(2,1,2,10,8,10),
(3,1,3,10,7,10),
(4,2,3,10,13,10),
(5,2,4,10,18,10),
(6,3,1,10,9,10),
(7,3,2,10,12,10),
(8,4,3,10,13,10),
(9,4,4,10,6,10),
(10,4,1,10,11,10),
(11,4,2,10,12,10);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
