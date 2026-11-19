-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
