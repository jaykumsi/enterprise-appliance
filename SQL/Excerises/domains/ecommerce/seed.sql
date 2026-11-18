-- Load only AFTER all six tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [ecommerce].[Customers] (CustomerID, CustomerName, CustomerCode, Region) VALUES
(1,N'Customers Alpha',N'CUS-1',N'North'),
(2,N'Customers Beta',N'CUS-2',N'South'),
(3,N'Customers Gamma',N'CUS-3',N'North'),
(4,N'Customers Delta',N'CUS-4',N'West'),
(5,N'Customers Unused',N'CUS-5',N'East');
INSERT INTO [ecommerce].[Sellers] (SellerID, SellerName, SellerCode, Department) VALUES
(1,N'Seller 1',N'SEL-1',N'Electronics'),
(2,N'Seller 2',N'SEL-2',N'Home & Kitchen'),
(3,N'Seller 3',N'SEL-3',N'Fashion'),
(4,N'Seller 4',N'SEL-4',N'Books'),
(5,N'Unused seller',N'SEL-5',N'Toys & Games');
INSERT INTO [ecommerce].[Products] (ProductID, ProductName, SKU, UnitPrice, Department) VALUES
(1,N'Wireless earbuds',N'EB-SKU-1',25,N'Electronics'),
(2,N'USB-C charger',N'EB-SKU-2',10,N'Electronics'),
(3,N'French press',N'EB-SKU-3',50,N'Home & Kitchen'),
(4,N'Rain jacket',N'EB-SKU-4',40,N'Fashion'),
(5,N'Unused product',N'EB-SKU-5',15,N'Books');
INSERT INTO [ecommerce].[Orders] (OrderID, CustomerID, OrderReference, SalesChannel, OrderStatus, OrderTotal, ItemCount, OrderDate, PlacedAt, RecordedAt, Note, BackupNote, ParentOrderID, SellerID) VALUES
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
INSERT INTO [ecommerce].[OrderItems] (OrderItemID, OrderID, ProductID, Quantity, UnitPrice) VALUES
(1,1,1,2,25),
(2,1,2,5,10),
(3,2,3,4,50),
(4,3,4,5,40),
(5,5,1,2,25),
(6,6,3,6,50);
INSERT INTO [ecommerce].[Payments] (PaymentID, OrderID, PaymentMethod, PaidAmount, PaidAt) VALUES
(1,1,N'GiftCard',40,N'2024-01-01T12:31:00'),
(2,1,N'Card',60,N'2024-01-01T12:31:04'),
(3,2,N'Wallet',200,N'2024-01-02T12:31:00'),
(4,3,N'Card',100,N'2024-01-02T12:32:00'),
(5,6,N'COD',300,N'2024-02-13T10:00:00');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
