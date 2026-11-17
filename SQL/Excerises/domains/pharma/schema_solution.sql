-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
