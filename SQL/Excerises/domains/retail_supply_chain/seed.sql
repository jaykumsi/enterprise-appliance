-- Load only AFTER all nine tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail_supply_chain].[Warehouses] (WarehouseID, WarehouseName, WarehouseCode, Region) VALUES
(1,N'Warehouses Alpha',N'WAR-1',N'North'),
(2,N'Warehouses Beta',N'WAR-2',N'South'),
(3,N'Warehouses Gamma',N'WAR-3',N'North'),
(4,N'Warehouses Delta',N'WAR-4',N'West'),
(5,N'Warehouses Unused',N'WAR-5',N'East');
INSERT INTO [retail_supply_chain].[Suppliers] (SupplierID, SupplierName, SupplierCode, LeadTimeDays) VALUES
(1,N'Supply chain supplier 1',N'SC-SUP-1',2),
(2,N'Supply chain supplier 2',N'SC-SUP-2',3),
(3,N'Supply chain supplier 3',N'SC-SUP-3',4),
(4,N'Private Label Plant',N'SC-SUP-4',1),
(5,N'Unused supplier',N'SC-SUP-5',6);
INSERT INTO [retail_supply_chain].[Products] (ProductID, ProductName, SKU, UnitCost, Sourcing) VALUES
(1,N'Notebook',N'SC-SKU-1',10,N'Bought'),
(2,N'Pen set',N'SC-SKU-2',4,N'Bought'),
(3,N'Canvas tote',N'SC-SKU-3',15,N'Made'),
(4,N'Travel pouch',N'SC-SKU-4',16,N'Made'),
(5,N'Unused product',N'SC-SKU-5',8,N'Bought');
INSERT INTO [retail_supply_chain].[Materials] (MaterialID, MaterialName, MaterialCode, UnitCost) VALUES
(1,N'Fabric',N'SC-MAT-1',5),
(2,N'Thread',N'SC-MAT-2',1),
(3,N'Zipper',N'SC-MAT-3',2),
(4,N'Packaging',N'SC-MAT-4',3),
(5,N'Unused trim',N'SC-MAT-5',4);
INSERT INTO [retail_supply_chain].[BillOfMaterials] (BOMID, ProductID, MaterialID, QuantityPerUnit) VALUES
(1,3,1,2),
(2,3,2,1),
(3,4,1,1),
(4,4,3,2),
(5,4,4,1);
INSERT INTO [retail_supply_chain].[ProductionOrders] (ProductionOrderID, ProductID, WarehouseID, ProductionReference, ProductionStatus, PlannedUnits, PlannedCost, StartDate, CompletedDate) VALUES
(1,3,2,N'PO-1',N'Completed',10,110,N'20231220',N'20231230'),
(2,4,1,N'PO-2',N'Completed',5,60,N'20231222',N'20231229'),
(3,3,3,N'PO-3',N'InProgress',8,88,N'20240201',NULL),
(4,4,4,N'PO-4',N'Planned',6,72,N'20240301',NULL);
INSERT INTO [retail_supply_chain].[MaterialUsage] (UsageID, ProductionOrderID, MaterialID, QuantityUsed, UsageDate) VALUES
(1,1,1,20,N'20231221'),
(2,1,2,10.5,N'20231221'),
(3,2,1,5,N'20231223'),
(4,2,3,10,N'20231223'),
(5,2,4,5,N'20231223'),
(6,3,1,8,N'20240202');
INSERT INTO [retail_supply_chain].[StockMovements] (MovementID, WarehouseID, MovementReference, MovementCategory, Status, MovementValue, MovedUnits, MovementDate, MovedAt, RecordedAt, Note, BackupNote, ParentMovementID, ProductID, SupplierID, Direction, ProductionOrderID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,1,N'IN',NULL),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,2,N'OUT',NULL),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,4,N'IN',1),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,4,N'IN',NULL),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,1,N'OUT',NULL),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,2,N'IN',NULL),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,4,N'IN',NULL),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,4,N'OUT',NULL),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,1,N'IN',NULL),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,2,N'IN',NULL),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,4,N'OUT',NULL),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,4,N'IN',NULL);
INSERT INTO [retail_supply_chain].[StockBalances] (BalanceID, WarehouseID, ProductID, OpeningQuantity, QuantityOnHand, ReorderLevel) VALUES
(1,1,1,10,11,10),
(2,1,2,10,8,10),
(3,1,3,10,7,10),
(4,2,3,10,13,10),
(5,2,4,10,18,10),
(6,3,1,10,9,10),
(7,3,2,10,12,10),
(8,4,1,10,11,10),
(9,4,2,10,12,10),
(10,4,3,10,13,10),
(11,4,4,10,6,10),
(12,1,5,10,10,10);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
