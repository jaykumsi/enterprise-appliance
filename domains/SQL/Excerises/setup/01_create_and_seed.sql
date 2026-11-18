-- Revised five-table projects. Use a NEW disposable database, not the old two-table fixture.
SET NOCOUNT ON;
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
IF SCHEMA_ID(N'retail') IS NULL EXEC(N'CREATE SCHEMA [retail] AUTHORIZATION dbo;');
IF OBJECT_ID(N'retail.Customers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail.Orders') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail.OrderItems') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail.Payments') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [retail].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [CustomerCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (CustomerCode),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
CREATE TABLE [retail].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [SKU] varchar(20) NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    [StockQuantity] int NOT NULL,
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (SKU),
    CONSTRAINT [CK_Products_1] CHECK (UnitPrice >= 0),
    CONSTRAINT [CK_Products_2] CHECK (StockQuantity >= 0),
    CONSTRAINT [CK_Products_3] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [retail].[Orders] (
    [OrderID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [OrderReference] nvarchar(80) NOT NULL,
    [SalesChannel] varchar(10) NOT NULL,
    [OrderStatus] varchar(10) NOT NULL DEFAULT ('Open'),
    [OrderTotal] decimal(12,2) NULL,
    [PackageCount] int NOT NULL,
    [OrderDate] date NOT NULL,
    [PlacedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentOrderID] int NULL,
    CONSTRAINT [PK_Orders] PRIMARY KEY ([OrderID]),
    CONSTRAINT [UQ_Orders_1] UNIQUE (OrderReference),
    CONSTRAINT [CK_Orders_1] CHECK (SalesChannel IN ('A','B','C')),
    CONSTRAINT [CK_Orders_2] CHECK (OrderStatus IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Orders_3] CHECK (OrderTotal >= 0),
    CONSTRAINT [CK_Orders_4] CHECK (PackageCount > 0),
    CONSTRAINT [CK_Orders_5] CHECK (ParentOrderID IS NULL OR ParentOrderID <> OrderID),
    CONSTRAINT [CK_Orders_6] CHECK (LEN(LTRIM(RTRIM(OrderReference))) > 0),
    CONSTRAINT [FK_Orders_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [retail].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Orders_ParentOrderID] FOREIGN KEY ([ParentOrderID]) REFERENCES [retail].[Orders] ([OrderID])
);
CREATE TABLE [retail].[OrderItems] (
    [OrderItemID] int NOT NULL,
    [OrderID] int NOT NULL,
    [ProductID] int NOT NULL,
    [Quantity] int NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_OrderItems] PRIMARY KEY ([OrderItemID]),
    CONSTRAINT [UQ_OrderItems_1] UNIQUE (OrderID, ProductID),
    CONSTRAINT [CK_OrderItems_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_OrderItems_2] CHECK (UnitPrice >= 0),
    CONSTRAINT [FK_OrderItems_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [retail].[Orders] ([OrderID]),
    CONSTRAINT [FK_OrderItems_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail].[Products] ([ProductID])
);
CREATE TABLE [retail].[Payments] (
    [PaymentID] int NOT NULL,
    [OrderID] int NOT NULL,
    [PaymentReference] varchar(20) NOT NULL,
    [PaidAmount] decimal(12,2) NOT NULL,
    [PaymentDate] date NOT NULL,
    CONSTRAINT [PK_Payments] PRIMARY KEY ([PaymentID]),
    CONSTRAINT [UQ_Payments_1] UNIQUE (PaymentReference),
    CONSTRAINT [CK_Payments_1] CHECK (PaidAmount > 0),
    CONSTRAINT [CK_Payments_2] CHECK (LEN(LTRIM(RTRIM(PaymentReference))) > 0),
    CONSTRAINT [FK_Payments_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [retail].[Orders] ([OrderID])
);
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
IF SCHEMA_ID(N'banking') IS NULL EXEC(N'CREATE SCHEMA [banking] AUTHORIZATION dbo;');
IF OBJECT_ID(N'banking.Branches') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'banking.Customers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'banking.Accounts') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'banking.Transactions') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'banking.Loans') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [banking].[Branches] (
    [BranchID] int NOT NULL,
    [BranchName] nvarchar(80) NOT NULL,
    [BranchCode] varchar(20) NOT NULL,
    [City] nvarchar(50) NOT NULL,
    CONSTRAINT [PK_Branches] PRIMARY KEY ([BranchID]),
    CONSTRAINT [UQ_Branches_1] UNIQUE (BranchCode),
    CONSTRAINT [CK_Branches_1] CHECK (LEN(LTRIM(RTRIM(BranchName))) > 0)
);
CREATE TABLE [banking].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [Email] varchar(100) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (Email),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
CREATE TABLE [banking].[Accounts] (
    [AccountID] int NOT NULL,
    [AccountName] nvarchar(80) NOT NULL,
    [AccountNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    [CustomerID] int NOT NULL,
    [BranchID] int NOT NULL,
    CONSTRAINT [PK_Accounts] PRIMARY KEY ([AccountID]),
    CONSTRAINT [UQ_Accounts_1] UNIQUE (AccountNumber),
    CONSTRAINT [CK_Accounts_1] CHECK (LEN(LTRIM(RTRIM(AccountName))) > 0),
    CONSTRAINT [FK_Accounts_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [banking].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Accounts_BranchID] FOREIGN KEY ([BranchID]) REFERENCES [banking].[Branches] ([BranchID])
);
CREATE TABLE [banking].[Transactions] (
    [TransactionID] int NOT NULL,
    [AccountID] int NOT NULL,
    [Reference] nvarchar(80) NOT NULL,
    [TransactionType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [Amount] decimal(12,2) NULL,
    [UnitCount] int NOT NULL,
    [TransactionDate] date NOT NULL,
    [PostedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentTransactionID] int NULL,
    CONSTRAINT [PK_Transactions] PRIMARY KEY ([TransactionID]),
    CONSTRAINT [UQ_Transactions_1] UNIQUE (Reference),
    CONSTRAINT [CK_Transactions_1] CHECK (TransactionType IN ('A','B','C')),
    CONSTRAINT [CK_Transactions_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Transactions_3] CHECK (Amount >= 0),
    CONSTRAINT [CK_Transactions_4] CHECK (UnitCount > 0),
    CONSTRAINT [CK_Transactions_5] CHECK (ParentTransactionID IS NULL OR ParentTransactionID <> TransactionID),
    CONSTRAINT [CK_Transactions_6] CHECK (LEN(LTRIM(RTRIM(Reference))) > 0),
    CONSTRAINT [FK_Transactions_AccountID] FOREIGN KEY ([AccountID]) REFERENCES [banking].[Accounts] ([AccountID]),
    CONSTRAINT [FK_Transactions_ParentTransactionID] FOREIGN KEY ([ParentTransactionID]) REFERENCES [banking].[Transactions] ([TransactionID])
);
CREATE TABLE [banking].[Loans] (
    [LoanID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [AccountID] int NOT NULL,
    [LoanReference] varchar(20) NOT NULL,
    [Principal] decimal(12,2) NOT NULL,
    [AnnualRate] decimal(5,2) NOT NULL,
    CONSTRAINT [PK_Loans] PRIMARY KEY ([LoanID]),
    CONSTRAINT [UQ_Loans_1] UNIQUE (LoanReference),
    CONSTRAINT [CK_Loans_1] CHECK (Principal > 0),
    CONSTRAINT [CK_Loans_2] CHECK (AnnualRate BETWEEN 0 AND 100),
    CONSTRAINT [CK_Loans_3] CHECK (LEN(LTRIM(RTRIM(LoanReference))) > 0),
    CONSTRAINT [FK_Loans_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [banking].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Loans_AccountID] FOREIGN KEY ([AccountID]) REFERENCES [banking].[Accounts] ([AccountID])
);
INSERT INTO [banking].[Branches] (BranchID, BranchName, BranchCode, City) VALUES
(1,N'Branch 1',N'BR-1',N'Chicago'),
(2,N'Branch 2',N'BR-2',N'Austin'),
(3,N'Branch 3',N'BR-3',N'Boston'),
(4,N'Branch 4',N'BR-4',N'Denver'),
(5,N'Branch 5',N'BR-5',N'Seattle');
INSERT INTO [banking].[Customers] (CustomerID, CustomerName, Email) VALUES
(1,N'Client 1',N'client1@example.test'),
(2,N'Client 2',N'client2@example.test'),
(3,N'Client 3',N'client3@example.test'),
(4,N'Client 4',N'client4@example.test'),
(5,N'Client 5',N'client5@example.test');
INSERT INTO [banking].[Accounts] (AccountID, AccountName, AccountNumber, Region, CustomerID, BranchID) VALUES
(1,N'Accounts Alpha',N'ACC-1',N'North',1,1),
(2,N'Accounts Beta',N'ACC-2',N'South',2,2),
(3,N'Accounts Gamma',N'ACC-3',N'North',3,3),
(4,N'Accounts Delta',N'ACC-4',N'West',4,4),
(5,N'Accounts Unused',N'ACC-5',N'East',5,5);
INSERT INTO [banking].[Transactions] (TransactionID, AccountID, Reference, TransactionType, Status, Amount, UnitCount, TransactionDate, PostedAt, RecordedAt, Note, BackupNote, ParentTransactionID) VALUES
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
INSERT INTO [banking].[Loans] (LoanID, CustomerID, AccountID, LoanReference, Principal, AnnualRate) VALUES
(1,1,1,N'LN-1',10000,5),
(2,1,1,N'LN-2',5000,6),
(3,2,2,N'LN-3',20000,4),
(4,3,3,N'LN-4',15000,7),
(5,4,4,N'LN-5',8000,8);
IF SCHEMA_ID(N'pharma') IS NULL EXEC(N'CREATE SCHEMA [pharma] AUTHORIZATION dbo;');
IF OBJECT_ID(N'pharma.Suppliers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'pharma.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'pharma.Warehouses') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'pharma.Batches') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'pharma.Inventory') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [pharma].[Suppliers] (
    [SupplierID] int NOT NULL,
    [SupplierName] nvarchar(80) NOT NULL,
    [SupplierCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Suppliers] PRIMARY KEY ([SupplierID]),
    CONSTRAINT [UQ_Suppliers_1] UNIQUE (SupplierCode),
    CONSTRAINT [CK_Suppliers_1] CHECK (LEN(LTRIM(RTRIM(SupplierName))) > 0)
);
CREATE TABLE [pharma].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [ProductCode] varchar(20) NOT NULL,
    [StandardCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (ProductCode),
    CONSTRAINT [CK_Products_1] CHECK (StandardCost >= 0),
    CONSTRAINT [CK_Products_2] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [pharma].[Warehouses] (
    [WarehouseID] int NOT NULL,
    [WarehouseName] nvarchar(80) NOT NULL,
    [WarehouseCode] varchar(20) NOT NULL,
    [Capacity] int NOT NULL,
    CONSTRAINT [PK_Warehouses] PRIMARY KEY ([WarehouseID]),
    CONSTRAINT [UQ_Warehouses_1] UNIQUE (WarehouseCode),
    CONSTRAINT [CK_Warehouses_1] CHECK (Capacity > 0),
    CONSTRAINT [CK_Warehouses_2] CHECK (LEN(LTRIM(RTRIM(WarehouseName))) > 0)
);
CREATE TABLE [pharma].[Batches] (
    [BatchID] int NOT NULL,
    [SupplierID] int NOT NULL,
    [BatchCode] nvarchar(80) NOT NULL,
    [BatchType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [BatchCost] decimal(12,2) NULL,
    [PackCount] int NOT NULL,
    [ManufactureDate] date NOT NULL,
    [ProducedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentBatchID] int NULL,
    [ProductID] int NOT NULL,
    CONSTRAINT [PK_Batches] PRIMARY KEY ([BatchID]),
    CONSTRAINT [UQ_Batches_1] UNIQUE (BatchCode),
    CONSTRAINT [CK_Batches_1] CHECK (BatchType IN ('A','B','C')),
    CONSTRAINT [CK_Batches_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Batches_3] CHECK (BatchCost >= 0),
    CONSTRAINT [CK_Batches_4] CHECK (PackCount > 0),
    CONSTRAINT [CK_Batches_5] CHECK (ParentBatchID IS NULL OR ParentBatchID <> BatchID),
    CONSTRAINT [CK_Batches_6] CHECK (LEN(LTRIM(RTRIM(BatchCode))) > 0),
    CONSTRAINT [FK_Batches_SupplierID] FOREIGN KEY ([SupplierID]) REFERENCES [pharma].[Suppliers] ([SupplierID]),
    CONSTRAINT [FK_Batches_ParentBatchID] FOREIGN KEY ([ParentBatchID]) REFERENCES [pharma].[Batches] ([BatchID]),
    CONSTRAINT [FK_Batches_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [pharma].[Products] ([ProductID])
);
CREATE TABLE [pharma].[Inventory] (
    [InventoryID] int NOT NULL,
    [BatchID] int NOT NULL,
    [WarehouseID] int NOT NULL,
    [QuantityOnHand] int NOT NULL,
    [LastCountDate] date NOT NULL,
    CONSTRAINT [PK_Inventory] PRIMARY KEY ([InventoryID]),
    CONSTRAINT [UQ_Inventory_1] UNIQUE (BatchID, WarehouseID),
    CONSTRAINT [CK_Inventory_1] CHECK (QuantityOnHand >= 0),
    CONSTRAINT [FK_Inventory_BatchID] FOREIGN KEY ([BatchID]) REFERENCES [pharma].[Batches] ([BatchID]),
    CONSTRAINT [FK_Inventory_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [pharma].[Warehouses] ([WarehouseID])
);
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
IF SCHEMA_ID(N'healthcare') IS NULL EXEC(N'CREATE SCHEMA [healthcare] AUTHORIZATION dbo;');
IF OBJECT_ID(N'healthcare.Patients') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Doctors') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Medications') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Encounters') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Prescriptions') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [healthcare].[Patients] (
    [PatientID] int NOT NULL,
    [PatientName] nvarchar(80) NOT NULL,
    [PatientNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Patients] PRIMARY KEY ([PatientID]),
    CONSTRAINT [UQ_Patients_1] UNIQUE (PatientNumber),
    CONSTRAINT [CK_Patients_1] CHECK (LEN(LTRIM(RTRIM(PatientName))) > 0)
);
CREATE TABLE [healthcare].[Doctors] (
    [DoctorID] int NOT NULL,
    [DoctorName] nvarchar(80) NOT NULL,
    [LicenseNumber] varchar(20) NOT NULL,
    [Specialty] varchar(30) NOT NULL,
    CONSTRAINT [PK_Doctors] PRIMARY KEY ([DoctorID]),
    CONSTRAINT [UQ_Doctors_1] UNIQUE (LicenseNumber),
    CONSTRAINT [CK_Doctors_1] CHECK (LEN(LTRIM(RTRIM(DoctorName))) > 0)
);
CREATE TABLE [healthcare].[Medications] (
    [MedicationID] int NOT NULL,
    [MedicationName] nvarchar(80) NOT NULL,
    [MedicationCode] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Medications] PRIMARY KEY ([MedicationID]),
    CONSTRAINT [UQ_Medications_1] UNIQUE (MedicationCode),
    CONSTRAINT [CK_Medications_1] CHECK (UnitCost >= 0),
    CONSTRAINT [CK_Medications_2] CHECK (LEN(LTRIM(RTRIM(MedicationName))) > 0)
);
CREATE TABLE [healthcare].[Encounters] (
    [EncounterID] int NOT NULL,
    [PatientID] int NOT NULL,
    [EncounterReference] nvarchar(80) NOT NULL,
    [EncounterType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [Charge] decimal(12,2) NULL,
    [ServiceUnits] int NOT NULL,
    [EncounterDate] date NOT NULL,
    [StartedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentEncounterID] int NULL,
    [DoctorID] int NOT NULL,
    CONSTRAINT [PK_Encounters] PRIMARY KEY ([EncounterID]),
    CONSTRAINT [UQ_Encounters_1] UNIQUE (EncounterReference),
    CONSTRAINT [CK_Encounters_1] CHECK (EncounterType IN ('A','B','C')),
    CONSTRAINT [CK_Encounters_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Encounters_3] CHECK (Charge >= 0),
    CONSTRAINT [CK_Encounters_4] CHECK (ServiceUnits > 0),
    CONSTRAINT [CK_Encounters_5] CHECK (ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID),
    CONSTRAINT [CK_Encounters_6] CHECK (LEN(LTRIM(RTRIM(EncounterReference))) > 0),
    CONSTRAINT [FK_Encounters_PatientID] FOREIGN KEY ([PatientID]) REFERENCES [healthcare].[Patients] ([PatientID]),
    CONSTRAINT [FK_Encounters_ParentEncounterID] FOREIGN KEY ([ParentEncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Encounters_DoctorID] FOREIGN KEY ([DoctorID]) REFERENCES [healthcare].[Doctors] ([DoctorID])
);
CREATE TABLE [healthcare].[Prescriptions] (
    [PrescriptionID] int NOT NULL,
    [EncounterID] int NOT NULL,
    [MedicationID] int NOT NULL,
    [PrescriptionReference] varchar(20) NOT NULL,
    [Quantity] int NOT NULL,
    CONSTRAINT [PK_Prescriptions] PRIMARY KEY ([PrescriptionID]),
    CONSTRAINT [UQ_Prescriptions_1] UNIQUE (PrescriptionReference),
    CONSTRAINT [CK_Prescriptions_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_Prescriptions_2] CHECK (LEN(LTRIM(RTRIM(PrescriptionReference))) > 0),
    CONSTRAINT [FK_Prescriptions_EncounterID] FOREIGN KEY ([EncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Prescriptions_MedicationID] FOREIGN KEY ([MedicationID]) REFERENCES [healthcare].[Medications] ([MedicationID])
);
INSERT INTO [healthcare].[Patients] (PatientID, PatientName, PatientNumber, Region) VALUES
(1,N'Patients Alpha',N'PAT-1',N'North'),
(2,N'Patients Beta',N'PAT-2',N'South'),
(3,N'Patients Gamma',N'PAT-3',N'North'),
(4,N'Patients Delta',N'PAT-4',N'West'),
(5,N'Patients Unused',N'PAT-5',N'East');
INSERT INTO [healthcare].[Doctors] (DoctorID, DoctorName, LicenseNumber, Specialty) VALUES
(1,N'Doctor 1',N'LIC-1',N'General'),
(2,N'Doctor 2',N'LIC-2',N'Cardiology'),
(3,N'Doctor 3',N'LIC-3',N'General'),
(4,N'Doctor 4',N'LIC-4',N'Dermatology'),
(5,N'Doctor 5',N'LIC-5',N'Neurology');
INSERT INTO [healthcare].[Medications] (MedicationID, MedicationName, MedicationCode, UnitCost) VALUES
(1,N'Training medication 1',N'MED-1',5),
(2,N'Training medication 2',N'MED-2',10),
(3,N'Training medication 3',N'MED-3',15),
(4,N'Training medication 4',N'MED-4',20),
(5,N'Training medication 5',N'MED-5',25);
INSERT INTO [healthcare].[Encounters] (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge, ServiceUnits, EncounterDate, StartedAt, RecordedAt, Note, BackupNote, ParentEncounterID, DoctorID) VALUES
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
INSERT INTO [healthcare].[Prescriptions] (PrescriptionID, EncounterID, MedicationID, PrescriptionReference, Quantity) VALUES
(1,1,1,N'RX-1',2),
(2,1,2,N'RX-2',3),
(3,2,3,N'RX-3',1),
(4,3,1,N'RX-4',2),
(5,6,4,N'RX-5',4);
IF SCHEMA_ID(N'oil') IS NULL EXEC(N'CREATE SCHEMA [oil] AUTHORIZATION dbo;');
IF OBJECT_ID(N'oil.Sites') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'oil.Carriers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'oil.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'oil.Shipments') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'oil.ShipmentItems') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [oil].[Sites] (
    [SiteID] int NOT NULL,
    [SiteName] nvarchar(80) NOT NULL,
    [SiteCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Sites] PRIMARY KEY ([SiteID]),
    CONSTRAINT [UQ_Sites_1] UNIQUE (SiteCode),
    CONSTRAINT [CK_Sites_1] CHECK (LEN(LTRIM(RTRIM(SiteName))) > 0)
);
CREATE TABLE [oil].[Carriers] (
    [CarrierID] int NOT NULL,
    [CarrierName] nvarchar(80) NOT NULL,
    [CarrierCode] varchar(20) NOT NULL,
    [Active] bit NOT NULL DEFAULT (1),
    CONSTRAINT [PK_Carriers] PRIMARY KEY ([CarrierID]),
    CONSTRAINT [UQ_Carriers_1] UNIQUE (CarrierCode),
    CONSTRAINT [CK_Carriers_1] CHECK (LEN(LTRIM(RTRIM(CarrierName))) > 0)
);
CREATE TABLE [oil].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [ProductCode] varchar(20) NOT NULL,
    [PricePerUnit] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (ProductCode),
    CONSTRAINT [CK_Products_1] CHECK (PricePerUnit >= 0),
    CONSTRAINT [CK_Products_2] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [oil].[Shipments] (
    [ShipmentID] int NOT NULL,
    [SiteID] int NOT NULL,
    [ShipmentReference] nvarchar(80) NOT NULL,
    [ShipmentType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [ShipmentValue] decimal(12,2) NULL,
    [UnitCount] int NOT NULL,
    [ShipDate] date NOT NULL,
    [DispatchedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentShipmentID] int NULL,
    [CarrierID] int NOT NULL,
    CONSTRAINT [PK_Shipments] PRIMARY KEY ([ShipmentID]),
    CONSTRAINT [UQ_Shipments_1] UNIQUE (ShipmentReference),
    CONSTRAINT [CK_Shipments_1] CHECK (ShipmentType IN ('A','B','C')),
    CONSTRAINT [CK_Shipments_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Shipments_3] CHECK (ShipmentValue >= 0),
    CONSTRAINT [CK_Shipments_4] CHECK (UnitCount > 0),
    CONSTRAINT [CK_Shipments_5] CHECK (ParentShipmentID IS NULL OR ParentShipmentID <> ShipmentID),
    CONSTRAINT [CK_Shipments_6] CHECK (LEN(LTRIM(RTRIM(ShipmentReference))) > 0),
    CONSTRAINT [FK_Shipments_SiteID] FOREIGN KEY ([SiteID]) REFERENCES [oil].[Sites] ([SiteID]),
    CONSTRAINT [FK_Shipments_ParentShipmentID] FOREIGN KEY ([ParentShipmentID]) REFERENCES [oil].[Shipments] ([ShipmentID]),
    CONSTRAINT [FK_Shipments_CarrierID] FOREIGN KEY ([CarrierID]) REFERENCES [oil].[Carriers] ([CarrierID])
);
CREATE TABLE [oil].[ShipmentItems] (
    [ShipmentItemID] int NOT NULL,
    [ShipmentID] int NOT NULL,
    [ProductID] int NOT NULL,
    [Quantity] int NOT NULL,
    [PricePerUnit] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_ShipmentItems] PRIMARY KEY ([ShipmentItemID]),
    CONSTRAINT [UQ_ShipmentItems_1] UNIQUE (ShipmentID, ProductID),
    CONSTRAINT [CK_ShipmentItems_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_ShipmentItems_2] CHECK (PricePerUnit >= 0),
    CONSTRAINT [FK_ShipmentItems_ShipmentID] FOREIGN KEY ([ShipmentID]) REFERENCES [oil].[Shipments] ([ShipmentID]),
    CONSTRAINT [FK_ShipmentItems_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [oil].[Products] ([ProductID])
);
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
IF SCHEMA_ID(N'retail_supply_chain') IS NULL EXEC(N'CREATE SCHEMA [retail_supply_chain] AUTHORIZATION dbo;');
IF OBJECT_ID(N'retail_supply_chain.Warehouses') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.Suppliers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.Materials') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.BillOfMaterials') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.ProductionOrders') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.MaterialUsage') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.StockMovements') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_supply_chain.StockBalances') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [retail_supply_chain].[Warehouses] (
    [WarehouseID] int NOT NULL,
    [WarehouseName] nvarchar(80) NOT NULL,
    [WarehouseCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Warehouses] PRIMARY KEY ([WarehouseID]),
    CONSTRAINT [UQ_Warehouses_1] UNIQUE (WarehouseCode),
    CONSTRAINT [CK_Warehouses_1] CHECK (LEN(LTRIM(RTRIM(WarehouseName))) > 0)
);
CREATE TABLE [retail_supply_chain].[Suppliers] (
    [SupplierID] int NOT NULL,
    [SupplierName] nvarchar(80) NOT NULL,
    [SupplierCode] varchar(20) NOT NULL,
    [LeadTimeDays] int NOT NULL,
    CONSTRAINT [PK_Suppliers] PRIMARY KEY ([SupplierID]),
    CONSTRAINT [UQ_Suppliers_1] UNIQUE (SupplierCode),
    CONSTRAINT [CK_Suppliers_1] CHECK (LeadTimeDays >= 0),
    CONSTRAINT [CK_Suppliers_2] CHECK (LEN(LTRIM(RTRIM(SupplierName))) > 0)
);
CREATE TABLE [retail_supply_chain].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [SKU] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    [Sourcing] varchar(10) NOT NULL DEFAULT ('Bought'),
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (SKU),
    CONSTRAINT [CK_Products_1] CHECK (UnitCost > 0),
    CONSTRAINT [CK_Products_2] CHECK (Sourcing IN ('Bought','Made')),
    CONSTRAINT [CK_Products_3] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [retail_supply_chain].[Materials] (
    [MaterialID] int NOT NULL,
    [MaterialName] nvarchar(80) NOT NULL,
    [MaterialCode] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Materials] PRIMARY KEY ([MaterialID]),
    CONSTRAINT [UQ_Materials_1] UNIQUE (MaterialCode),
    CONSTRAINT [CK_Materials_1] CHECK (UnitCost > 0),
    CONSTRAINT [CK_Materials_2] CHECK (LEN(LTRIM(RTRIM(MaterialName))) > 0)
);
CREATE TABLE [retail_supply_chain].[BillOfMaterials] (
    [BOMID] int NOT NULL,
    [ProductID] int NOT NULL,
    [MaterialID] int NOT NULL,
    [QuantityPerUnit] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_BillOfMaterials] PRIMARY KEY ([BOMID]),
    CONSTRAINT [UQ_BillOfMaterials_1] UNIQUE (ProductID, MaterialID),
    CONSTRAINT [CK_BillOfMaterials_1] CHECK (QuantityPerUnit > 0),
    CONSTRAINT [FK_BillOfMaterials_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_supply_chain].[Products] ([ProductID]),
    CONSTRAINT [FK_BillOfMaterials_MaterialID] FOREIGN KEY ([MaterialID]) REFERENCES [retail_supply_chain].[Materials] ([MaterialID])
);
CREATE TABLE [retail_supply_chain].[ProductionOrders] (
    [ProductionOrderID] int NOT NULL,
    [ProductID] int NOT NULL,
    [WarehouseID] int NOT NULL,
    [ProductionReference] varchar(20) NOT NULL,
    [ProductionStatus] varchar(12) NOT NULL,
    [PlannedUnits] int NOT NULL,
    [PlannedCost] decimal(12,2) NOT NULL,
    [StartDate] date NOT NULL,
    [CompletedDate] date NULL,
    CONSTRAINT [PK_ProductionOrders] PRIMARY KEY ([ProductionOrderID]),
    CONSTRAINT [UQ_ProductionOrders_1] UNIQUE (ProductionReference),
    CONSTRAINT [CK_ProductionOrders_1] CHECK (ProductionStatus IN ('Planned','InProgress','Completed')),
    CONSTRAINT [CK_ProductionOrders_2] CHECK (PlannedUnits > 0),
    CONSTRAINT [CK_ProductionOrders_3] CHECK (PlannedCost >= 0),
    CONSTRAINT [CK_ProductionOrders_4] CHECK (CompletedDate IS NULL OR CompletedDate >= StartDate),
    CONSTRAINT [CK_ProductionOrders_5] CHECK (LEN(LTRIM(RTRIM(ProductionReference))) > 0),
    CONSTRAINT [FK_ProductionOrders_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_supply_chain].[Products] ([ProductID]),
    CONSTRAINT [FK_ProductionOrders_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [retail_supply_chain].[Warehouses] ([WarehouseID])
);
CREATE TABLE [retail_supply_chain].[MaterialUsage] (
    [UsageID] int NOT NULL,
    [ProductionOrderID] int NOT NULL,
    [MaterialID] int NOT NULL,
    [QuantityUsed] decimal(12,2) NOT NULL,
    [UsageDate] date NOT NULL,
    CONSTRAINT [PK_MaterialUsage] PRIMARY KEY ([UsageID]),
    CONSTRAINT [UQ_MaterialUsage_1] UNIQUE (ProductionOrderID, MaterialID),
    CONSTRAINT [CK_MaterialUsage_1] CHECK (QuantityUsed > 0),
    CONSTRAINT [FK_MaterialUsage_ProductionOrderID] FOREIGN KEY ([ProductionOrderID]) REFERENCES [retail_supply_chain].[ProductionOrders] ([ProductionOrderID]),
    CONSTRAINT [FK_MaterialUsage_MaterialID] FOREIGN KEY ([MaterialID]) REFERENCES [retail_supply_chain].[Materials] ([MaterialID])
);
CREATE TABLE [retail_supply_chain].[StockMovements] (
    [MovementID] int NOT NULL,
    [WarehouseID] int NOT NULL,
    [MovementReference] nvarchar(80) NOT NULL,
    [MovementCategory] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [MovementValue] decimal(12,2) NULL,
    [MovedUnits] int NOT NULL,
    [MovementDate] date NOT NULL,
    [MovedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentMovementID] int NULL,
    [ProductID] int NOT NULL,
    [SupplierID] int NOT NULL,
    [Direction] varchar(3) NOT NULL,
    [ProductionOrderID] int NULL,
    CONSTRAINT [PK_StockMovements] PRIMARY KEY ([MovementID]),
    CONSTRAINT [UQ_StockMovements_1] UNIQUE (MovementReference),
    CONSTRAINT [CK_StockMovements_1] CHECK (MovementCategory IN ('A','B','C')),
    CONSTRAINT [CK_StockMovements_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_StockMovements_3] CHECK (MovementValue >= 0),
    CONSTRAINT [CK_StockMovements_4] CHECK (MovedUnits > 0),
    CONSTRAINT [CK_StockMovements_5] CHECK (ParentMovementID IS NULL OR ParentMovementID <> MovementID),
    CONSTRAINT [CK_StockMovements_6] CHECK (Direction IN ('IN','OUT')),
    CONSTRAINT [CK_StockMovements_7] CHECK (LEN(LTRIM(RTRIM(MovementReference))) > 0),
    CONSTRAINT [FK_StockMovements_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [retail_supply_chain].[Warehouses] ([WarehouseID]),
    CONSTRAINT [FK_StockMovements_ParentMovementID] FOREIGN KEY ([ParentMovementID]) REFERENCES [retail_supply_chain].[StockMovements] ([MovementID]),
    CONSTRAINT [FK_StockMovements_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_supply_chain].[Products] ([ProductID]),
    CONSTRAINT [FK_StockMovements_SupplierID] FOREIGN KEY ([SupplierID]) REFERENCES [retail_supply_chain].[Suppliers] ([SupplierID]),
    CONSTRAINT [FK_StockMovements_ProductionOrderID] FOREIGN KEY ([ProductionOrderID]) REFERENCES [retail_supply_chain].[ProductionOrders] ([ProductionOrderID])
);
CREATE TABLE [retail_supply_chain].[StockBalances] (
    [BalanceID] int NOT NULL,
    [WarehouseID] int NOT NULL,
    [ProductID] int NOT NULL,
    [OpeningQuantity] int NOT NULL,
    [QuantityOnHand] int NOT NULL,
    [ReorderLevel] int NOT NULL,
    CONSTRAINT [PK_StockBalances] PRIMARY KEY ([BalanceID]),
    CONSTRAINT [UQ_StockBalances_1] UNIQUE (WarehouseID, ProductID),
    CONSTRAINT [CK_StockBalances_1] CHECK (OpeningQuantity >= 0),
    CONSTRAINT [CK_StockBalances_2] CHECK (QuantityOnHand >= 0),
    CONSTRAINT [CK_StockBalances_3] CHECK (ReorderLevel >= 0),
    CONSTRAINT [FK_StockBalances_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [retail_supply_chain].[Warehouses] ([WarehouseID]),
    CONSTRAINT [FK_StockBalances_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_supply_chain].[Products] ([ProductID])
);
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
IF SCHEMA_ID(N'retail_logistics') IS NULL EXEC(N'CREATE SCHEMA [retail_logistics] AUTHORIZATION dbo;');
IF OBJECT_ID(N'retail_logistics.Customers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_logistics.Carriers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_logistics.Shipments') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_logistics.ShipmentPackages') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_logistics.TrackingEvents') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [retail_logistics].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [CustomerCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (CustomerCode),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
CREATE TABLE [retail_logistics].[Carriers] (
    [CarrierID] int NOT NULL,
    [CarrierName] nvarchar(80) NOT NULL,
    [CarrierCode] varchar(20) NOT NULL,
    [ServiceLevel] varchar(20) NOT NULL,
    CONSTRAINT [PK_Carriers] PRIMARY KEY ([CarrierID]),
    CONSTRAINT [UQ_Carriers_1] UNIQUE (CarrierCode),
    CONSTRAINT [CK_Carriers_1] CHECK (LEN(LTRIM(RTRIM(CarrierName))) > 0)
);
CREATE TABLE [retail_logistics].[Shipments] (
    [ShipmentID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [ShipmentReference] nvarchar(80) NOT NULL,
    [ShipmentCategory] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [FreightCharge] decimal(12,2) NULL,
    [DeclaredPackages] int NOT NULL,
    [ShipDate] date NOT NULL,
    [DispatchedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentShipmentID] int NULL,
    [CarrierID] int NOT NULL,
    CONSTRAINT [PK_Shipments] PRIMARY KEY ([ShipmentID]),
    CONSTRAINT [UQ_Shipments_1] UNIQUE (ShipmentReference),
    CONSTRAINT [CK_Shipments_1] CHECK (ShipmentCategory IN ('A','B','C')),
    CONSTRAINT [CK_Shipments_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Shipments_3] CHECK (FreightCharge >= 0),
    CONSTRAINT [CK_Shipments_4] CHECK (DeclaredPackages > 0),
    CONSTRAINT [CK_Shipments_5] CHECK (ParentShipmentID IS NULL OR ParentShipmentID <> ShipmentID),
    CONSTRAINT [CK_Shipments_6] CHECK (LEN(LTRIM(RTRIM(ShipmentReference))) > 0),
    CONSTRAINT [FK_Shipments_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [retail_logistics].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Shipments_ParentShipmentID] FOREIGN KEY ([ParentShipmentID]) REFERENCES [retail_logistics].[Shipments] ([ShipmentID]),
    CONSTRAINT [FK_Shipments_CarrierID] FOREIGN KEY ([CarrierID]) REFERENCES [retail_logistics].[Carriers] ([CarrierID])
);
CREATE TABLE [retail_logistics].[ShipmentPackages] (
    [PackageID] int NOT NULL,
    [ShipmentID] int NOT NULL,
    [TrackingNumber] varchar(20) NOT NULL,
    [WeightKg] decimal(12,2) NOT NULL,
    [PromisedDate] date NOT NULL,
    CONSTRAINT [PK_ShipmentPackages] PRIMARY KEY ([PackageID]),
    CONSTRAINT [UQ_ShipmentPackages_1] UNIQUE (TrackingNumber),
    CONSTRAINT [CK_ShipmentPackages_1] CHECK (WeightKg > 0),
    CONSTRAINT [CK_ShipmentPackages_2] CHECK (LEN(LTRIM(RTRIM(TrackingNumber))) > 0),
    CONSTRAINT [FK_ShipmentPackages_ShipmentID] FOREIGN KEY ([ShipmentID]) REFERENCES [retail_logistics].[Shipments] ([ShipmentID])
);
CREATE TABLE [retail_logistics].[TrackingEvents] (
    [TrackingEventID] int NOT NULL,
    [PackageID] int NOT NULL,
    [ScanReference] varchar(20) NOT NULL,
    [EventStatus] varchar(20) NOT NULL,
    [ScanTime] datetime2(3) NOT NULL,
    [LocationName] nvarchar(80) NOT NULL,
    CONSTRAINT [PK_TrackingEvents] PRIMARY KEY ([TrackingEventID]),
    CONSTRAINT [UQ_TrackingEvents_1] UNIQUE (ScanReference),
    CONSTRAINT [CK_TrackingEvents_1] CHECK (EventStatus IN ('PickedUp','InTransit','Delivered')),
    CONSTRAINT [CK_TrackingEvents_2] CHECK (LEN(LTRIM(RTRIM(ScanReference))) > 0),
    CONSTRAINT [FK_TrackingEvents_PackageID] FOREIGN KEY ([PackageID]) REFERENCES [retail_logistics].[ShipmentPackages] ([PackageID])
);
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
IF SCHEMA_ID(N'ecommerce') IS NULL EXEC(N'CREATE SCHEMA [ecommerce] AUTHORIZATION dbo;');
IF OBJECT_ID(N'ecommerce.Customers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'ecommerce.Sellers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'ecommerce.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'ecommerce.Orders') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'ecommerce.OrderItems') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'ecommerce.Payments') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [ecommerce].[Customers] (
    [CustomerID] int NOT NULL,
    [CustomerName] nvarchar(80) NOT NULL,
    [CustomerCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Customers] PRIMARY KEY ([CustomerID]),
    CONSTRAINT [UQ_Customers_1] UNIQUE (CustomerCode),
    CONSTRAINT [CK_Customers_1] CHECK (LEN(LTRIM(RTRIM(CustomerName))) > 0)
);
CREATE TABLE [ecommerce].[Sellers] (
    [SellerID] int NOT NULL,
    [SellerName] nvarchar(80) NOT NULL,
    [SellerCode] varchar(20) NOT NULL,
    [Department] varchar(20) NOT NULL,
    CONSTRAINT [PK_Sellers] PRIMARY KEY ([SellerID]),
    CONSTRAINT [UQ_Sellers_1] UNIQUE (SellerCode),
    CONSTRAINT [CK_Sellers_1] CHECK (LEN(LTRIM(RTRIM(SellerName))) > 0)
);
CREATE TABLE [ecommerce].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [SKU] varchar(20) NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    [Department] varchar(20) NOT NULL DEFAULT ('General'),
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (SKU),
    CONSTRAINT [CK_Products_1] CHECK (UnitPrice > 0),
    CONSTRAINT [CK_Products_2] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [ecommerce].[Orders] (
    [OrderID] int NOT NULL,
    [CustomerID] int NOT NULL,
    [OrderReference] nvarchar(80) NOT NULL,
    [SalesChannel] varchar(10) NOT NULL,
    [OrderStatus] varchar(10) NOT NULL DEFAULT ('Open'),
    [OrderTotal] decimal(12,2) NULL,
    [ItemCount] int NOT NULL,
    [OrderDate] date NOT NULL,
    [PlacedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentOrderID] int NULL,
    [SellerID] int NOT NULL,
    CONSTRAINT [PK_Orders] PRIMARY KEY ([OrderID]),
    CONSTRAINT [UQ_Orders_1] UNIQUE (OrderReference),
    CONSTRAINT [CK_Orders_1] CHECK (SalesChannel IN ('A','B','C')),
    CONSTRAINT [CK_Orders_2] CHECK (OrderStatus IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Orders_3] CHECK (OrderTotal >= 0),
    CONSTRAINT [CK_Orders_4] CHECK (ItemCount > 0),
    CONSTRAINT [CK_Orders_5] CHECK (ParentOrderID IS NULL OR ParentOrderID <> OrderID),
    CONSTRAINT [CK_Orders_6] CHECK (LEN(LTRIM(RTRIM(OrderReference))) > 0),
    CONSTRAINT [FK_Orders_CustomerID] FOREIGN KEY ([CustomerID]) REFERENCES [ecommerce].[Customers] ([CustomerID]),
    CONSTRAINT [FK_Orders_ParentOrderID] FOREIGN KEY ([ParentOrderID]) REFERENCES [ecommerce].[Orders] ([OrderID]),
    CONSTRAINT [FK_Orders_SellerID] FOREIGN KEY ([SellerID]) REFERENCES [ecommerce].[Sellers] ([SellerID])
);
CREATE TABLE [ecommerce].[OrderItems] (
    [OrderItemID] int NOT NULL,
    [OrderID] int NOT NULL,
    [ProductID] int NOT NULL,
    [Quantity] int NOT NULL,
    [UnitPrice] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_OrderItems] PRIMARY KEY ([OrderItemID]),
    CONSTRAINT [UQ_OrderItems_1] UNIQUE (OrderID, ProductID),
    CONSTRAINT [CK_OrderItems_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_OrderItems_2] CHECK (UnitPrice >= 0),
    CONSTRAINT [FK_OrderItems_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [ecommerce].[Orders] ([OrderID]),
    CONSTRAINT [FK_OrderItems_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [ecommerce].[Products] ([ProductID])
);
CREATE TABLE [ecommerce].[Payments] (
    [PaymentID] int NOT NULL,
    [OrderID] int NOT NULL,
    [PaymentMethod] varchar(10) NOT NULL,
    [PaidAmount] decimal(12,2) NOT NULL,
    [PaidAt] datetime2(3) NOT NULL,
    CONSTRAINT [PK_Payments] PRIMARY KEY ([PaymentID]),
    CONSTRAINT [CK_Payments_1] CHECK (PaymentMethod IN ('Card','Wallet','GiftCard','COD')),
    CONSTRAINT [CK_Payments_2] CHECK (PaidAmount > 0),
    CONSTRAINT [CK_Payments_3] CHECK (LEN(LTRIM(RTRIM(PaymentMethod))) > 0),
    CONSTRAINT [FK_Payments_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [ecommerce].[Orders] ([OrderID])
);
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
IF SCHEMA_ID(N'brokerage') IS NULL EXEC(N'CREATE SCHEMA [brokerage] AUTHORIZATION dbo;');
IF OBJECT_ID(N'brokerage.Clients') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'brokerage.Securities') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'brokerage.BrokerageAccounts') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'brokerage.TradeOrders') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'brokerage.Executions') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [brokerage].[Clients] (
    [ClientID] int NOT NULL,
    [ClientName] nvarchar(80) NOT NULL,
    [ClientReference] varchar(20) NOT NULL,
    [Email] varchar(100) NOT NULL,
    CONSTRAINT [PK_Clients] PRIMARY KEY ([ClientID]),
    CONSTRAINT [UQ_Clients_1] UNIQUE (ClientReference),
    CONSTRAINT [UQ_Clients_2] UNIQUE (Email),
    CONSTRAINT [CK_Clients_1] CHECK (LEN(LTRIM(RTRIM(ClientName))) > 0)
);
CREATE TABLE [brokerage].[Securities] (
    [SecurityID] int NOT NULL,
    [SecurityName] nvarchar(80) NOT NULL,
    [Symbol] varchar(20) NOT NULL,
    [AssetClass] varchar(10) NOT NULL,
    CONSTRAINT [PK_Securities] PRIMARY KEY ([SecurityID]),
    CONSTRAINT [UQ_Securities_1] UNIQUE (Symbol),
    CONSTRAINT [CK_Securities_1] CHECK (AssetClass IN ('Stock','ETF')),
    CONSTRAINT [CK_Securities_2] CHECK (LEN(LTRIM(RTRIM(SecurityName))) > 0)
);
CREATE TABLE [brokerage].[BrokerageAccounts] (
    [AccountID] int NOT NULL,
    [AccountName] nvarchar(80) NOT NULL,
    [AccountNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    [ClientID] int NOT NULL,
    CONSTRAINT [PK_BrokerageAccounts] PRIMARY KEY ([AccountID]),
    CONSTRAINT [UQ_BrokerageAccounts_1] UNIQUE (AccountNumber),
    CONSTRAINT [CK_BrokerageAccounts_1] CHECK (LEN(LTRIM(RTRIM(AccountName))) > 0),
    CONSTRAINT [FK_BrokerageAccounts_ClientID] FOREIGN KEY ([ClientID]) REFERENCES [brokerage].[Clients] ([ClientID])
);
CREATE TABLE [brokerage].[TradeOrders] (
    [OrderID] int NOT NULL,
    [AccountID] int NOT NULL,
    [OrderReference] nvarchar(80) NOT NULL,
    [RoutingCategory] varchar(10) NOT NULL,
    [WorkflowStatus] varchar(10) NOT NULL DEFAULT ('Open'),
    [EstimatedValue] decimal(12,2) NULL,
    [RequestedQuantity] int NOT NULL,
    [OrderDate] date NOT NULL,
    [SubmittedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentOrderID] int NULL,
    [SecurityID] int NOT NULL,
    [Side] varchar(3) NOT NULL DEFAULT ('Buy'),
    CONSTRAINT [PK_TradeOrders] PRIMARY KEY ([OrderID]),
    CONSTRAINT [UQ_TradeOrders_1] UNIQUE (OrderReference),
    CONSTRAINT [CK_TradeOrders_1] CHECK (RoutingCategory IN ('A','B','C')),
    CONSTRAINT [CK_TradeOrders_2] CHECK (WorkflowStatus IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_TradeOrders_3] CHECK (EstimatedValue >= 0),
    CONSTRAINT [CK_TradeOrders_4] CHECK (RequestedQuantity > 0),
    CONSTRAINT [CK_TradeOrders_5] CHECK (ParentOrderID IS NULL OR ParentOrderID <> OrderID),
    CONSTRAINT [CK_TradeOrders_6] CHECK (Side = 'Buy'),
    CONSTRAINT [CK_TradeOrders_7] CHECK (LEN(LTRIM(RTRIM(OrderReference))) > 0),
    CONSTRAINT [FK_TradeOrders_AccountID] FOREIGN KEY ([AccountID]) REFERENCES [brokerage].[BrokerageAccounts] ([AccountID]),
    CONSTRAINT [FK_TradeOrders_ParentOrderID] FOREIGN KEY ([ParentOrderID]) REFERENCES [brokerage].[TradeOrders] ([OrderID]),
    CONSTRAINT [FK_TradeOrders_SecurityID] FOREIGN KEY ([SecurityID]) REFERENCES [brokerage].[Securities] ([SecurityID])
);
CREATE TABLE [brokerage].[Executions] (
    [ExecutionID] int NOT NULL,
    [OrderID] int NOT NULL,
    [ExecutionReference] varchar(20) NOT NULL,
    [ExecutedQuantity] decimal(12,4) NOT NULL,
    [ExecutionPrice] decimal(12,4) NOT NULL,
    [ExecutedAt] datetime2(3) NOT NULL,
    CONSTRAINT [PK_Executions] PRIMARY KEY ([ExecutionID]),
    CONSTRAINT [UQ_Executions_1] UNIQUE (ExecutionReference),
    CONSTRAINT [CK_Executions_1] CHECK (ExecutedQuantity > 0),
    CONSTRAINT [CK_Executions_2] CHECK (ExecutionPrice > 0),
    CONSTRAINT [CK_Executions_3] CHECK (LEN(LTRIM(RTRIM(ExecutionReference))) > 0),
    CONSTRAINT [FK_Executions_OrderID] FOREIGN KEY ([OrderID]) REFERENCES [brokerage].[TradeOrders] ([OrderID])
);
INSERT INTO [brokerage].[Clients] (ClientID, ClientName, ClientReference, Email) VALUES
(1,N'Investor 1',N'CLIENT-1',N'investor1@example.test'),
(2,N'Investor 2',N'CLIENT-2',N'investor2@example.test'),
(3,N'Investor 3',N'CLIENT-3',N'investor3@example.test'),
(4,N'Investor 4',N'CLIENT-4',N'investor4@example.test'),
(5,N'Investor 5',N'CLIENT-5',N'investor5@example.test');
INSERT INTO [brokerage].[Securities] (SecurityID, SecurityName, Symbol, AssetClass) VALUES
(1,N'Training Equity Alpha',N'DEMO-A',N'Stock'),
(2,N'Training Equity Beta',N'DEMO-B',N'Stock'),
(3,N'Training Fund Gamma',N'DEMO-C',N'ETF'),
(4,N'Training Fund Delta',N'DEMO-D',N'ETF'),
(5,N'Unused Training Equity',N'DEMO-E',N'Stock');
INSERT INTO [brokerage].[BrokerageAccounts] (AccountID, AccountName, AccountNumber, Region, ClientID) VALUES
(1,N'BrokerageAccounts Alpha',N'ACC-1',N'North',1),
(2,N'BrokerageAccounts Beta',N'ACC-2',N'South',2),
(3,N'BrokerageAccounts Gamma',N'ACC-3',N'North',3),
(4,N'BrokerageAccounts Delta',N'ACC-4',N'West',4),
(5,N'BrokerageAccounts Unused',N'ACC-5',N'East',5);
INSERT INTO [brokerage].[TradeOrders] (OrderID, AccountID, OrderReference, RoutingCategory, WorkflowStatus, EstimatedValue, RequestedQuantity, OrderDate, SubmittedAt, RecordedAt, Note, BackupNote, ParentOrderID, SecurityID, Side) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,N'Buy'),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,N'Buy'),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,N'Buy'),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,N'Buy'),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,N'Buy'),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,N'Buy'),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,N'Buy'),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,N'Buy'),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,N'Buy'),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,N'Buy'),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,N'Buy'),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,N'Buy');
INSERT INTO [brokerage].[Executions] (ExecutionID, OrderID, ExecutionReference, ExecutedQuantity, ExecutionPrice, ExecutedAt) VALUES
(1,1,N'FILL-1',0.4,100,N'2024-01-01T12:31:00'),
(2,1,N'FILL-2',0.6,101,N'2024-01-01T12:32:00'),
(3,2,N'FILL-3',1,99,N'2024-01-02T12:31:00'),
(4,2,N'FILL-4',0.5,100,N'2024-01-02T12:32:00'),
(5,3,N'FILL-5',3,101,N'2024-01-02T12:33:00'),
(6,6,N'FILL-6',1,150,N'2024-02-10T12:31:00');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
THROW;
END CATCH;
