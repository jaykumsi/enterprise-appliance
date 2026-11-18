-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [retail].[Customers] (CustomerID, CustomerName, CustomerCode, Region) VALUES
(1,N'Customers Alpha',N'CUS-1',N'North'),
(2,N'Customers Beta',N'CUS-2',N'South'),
(3,N'Customers Gamma',N'CUS-3',N'North'),
(4,N'Customers Delta',N'CUS-4',N'West'),
(5,N'Customers Unused',N'CUS-5',N'East');
INSERT INTO [retail].[Products] (ProductID, ProductName, SKU, UnitPrice, StockQuantity) VALUES
(1,N'Notebook',N'SKU-1',25,20),
(2,N'Pen set',N'SKU-2',10,30),
(3,N'Backpack',N'SKU-3',50,10),
(4,N'Desk lamp',N'SKU-4',40,5),
(5,N'Unused product',N'SKU-5',15,0);
INSERT INTO [retail].[Orders] (OrderID, CustomerID, OrderReference, SalesChannel, OrderStatus, OrderTotal, PackageCount, OrderDate, PlacedAt, RecordedAt, Note, BackupNote, ParentOrderID) VALUES
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
INSERT INTO [retail].[OrderItems] (OrderItemID, OrderID, ProductID, Quantity, UnitPrice) VALUES
(1,1,1,2,25),
(2,1,2,5,10),
(3,2,3,4,50),
(4,3,3,4,50),
(5,5,1,2,25),
(6,6,3,6,50);
INSERT INTO [retail].[Payments] (PaymentID, OrderID, PaymentReference, PaidAmount, PaymentDate) VALUES
(1,1,N'PAY-1',60,N'20240102'),
(2,1,N'PAY-2',40,N'20240103'),
(3,2,N'PAY-3',200,N'20240103'),
(4,3,N'PAY-4',100,N'20240104'),
(5,6,N'PAY-5',300,N'20240211');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
