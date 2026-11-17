-- Instructor schema answer. Execute in an empty training database.
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
