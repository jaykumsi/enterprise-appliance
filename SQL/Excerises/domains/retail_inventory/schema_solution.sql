-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
IF SCHEMA_ID(N'retail_inventory') IS NULL EXEC(N'CREATE SCHEMA [retail_inventory] AUTHORIZATION dbo;');
IF OBJECT_ID(N'retail_inventory.Warehouses') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_inventory.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_inventory.Suppliers') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_inventory.StockMovements') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_inventory.StockBalances') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [retail_inventory].[Warehouses] (
    [WarehouseID] int NOT NULL,
    [WarehouseName] nvarchar(80) NOT NULL,
    [WarehouseCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Warehouses] PRIMARY KEY ([WarehouseID]),
    CONSTRAINT [UQ_Warehouses_1] UNIQUE (WarehouseCode),
    CONSTRAINT [CK_Warehouses_1] CHECK (LEN(LTRIM(RTRIM(WarehouseName))) > 0)
);
CREATE TABLE [retail_inventory].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [SKU] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (SKU),
    CONSTRAINT [CK_Products_1] CHECK (UnitCost > 0),
    CONSTRAINT [CK_Products_2] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [retail_inventory].[Suppliers] (
    [SupplierID] int NOT NULL,
    [SupplierName] nvarchar(80) NOT NULL,
    [SupplierCode] varchar(20) NOT NULL,
    [LeadTimeDays] int NOT NULL,
    CONSTRAINT [PK_Suppliers] PRIMARY KEY ([SupplierID]),
    CONSTRAINT [UQ_Suppliers_1] UNIQUE (SupplierCode),
    CONSTRAINT [CK_Suppliers_1] CHECK (LeadTimeDays >= 0),
    CONSTRAINT [CK_Suppliers_2] CHECK (LEN(LTRIM(RTRIM(SupplierName))) > 0)
);
CREATE TABLE [retail_inventory].[StockMovements] (
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
    CONSTRAINT [PK_StockMovements] PRIMARY KEY ([MovementID]),
    CONSTRAINT [UQ_StockMovements_1] UNIQUE (MovementReference),
    CONSTRAINT [CK_StockMovements_1] CHECK (MovementCategory IN ('A','B','C')),
    CONSTRAINT [CK_StockMovements_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_StockMovements_3] CHECK (MovementValue >= 0),
    CONSTRAINT [CK_StockMovements_4] CHECK (MovedUnits > 0),
    CONSTRAINT [CK_StockMovements_5] CHECK (ParentMovementID IS NULL OR ParentMovementID <> MovementID),
    CONSTRAINT [CK_StockMovements_6] CHECK (Direction IN ('IN','OUT')),
    CONSTRAINT [CK_StockMovements_7] CHECK (LEN(LTRIM(RTRIM(MovementReference))) > 0),
    CONSTRAINT [FK_StockMovements_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [retail_inventory].[Warehouses] ([WarehouseID]),
    CONSTRAINT [FK_StockMovements_ParentMovementID] FOREIGN KEY ([ParentMovementID]) REFERENCES [retail_inventory].[StockMovements] ([MovementID]),
    CONSTRAINT [FK_StockMovements_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_inventory].[Products] ([ProductID]),
    CONSTRAINT [FK_StockMovements_SupplierID] FOREIGN KEY ([SupplierID]) REFERENCES [retail_inventory].[Suppliers] ([SupplierID])
);
CREATE TABLE [retail_inventory].[StockBalances] (
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
    CONSTRAINT [FK_StockBalances_WarehouseID] FOREIGN KEY ([WarehouseID]) REFERENCES [retail_inventory].[Warehouses] ([WarehouseID]),
    CONSTRAINT [FK_StockBalances_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_inventory].[Products] ([ProductID])
);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
