-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
IF SCHEMA_ID(N'retail_manufacturing') IS NULL EXEC(N'CREATE SCHEMA [retail_manufacturing] AUTHORIZATION dbo;');
IF OBJECT_ID(N'retail_manufacturing.Products') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_manufacturing.Materials') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_manufacturing.ProductionOrders') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_manufacturing.BillOfMaterials') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'retail_manufacturing.MaterialUsage') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [retail_manufacturing].[Products] (
    [ProductID] int NOT NULL,
    [ProductName] nvarchar(80) NOT NULL,
    [ProductCode] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Products] PRIMARY KEY ([ProductID]),
    CONSTRAINT [UQ_Products_1] UNIQUE (ProductCode),
    CONSTRAINT [CK_Products_1] CHECK (LEN(LTRIM(RTRIM(ProductName))) > 0)
);
CREATE TABLE [retail_manufacturing].[Materials] (
    [MaterialID] int NOT NULL,
    [MaterialName] nvarchar(80) NOT NULL,
    [MaterialCode] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Materials] PRIMARY KEY ([MaterialID]),
    CONSTRAINT [UQ_Materials_1] UNIQUE (MaterialCode),
    CONSTRAINT [CK_Materials_1] CHECK (UnitCost > 0),
    CONSTRAINT [CK_Materials_2] CHECK (LEN(LTRIM(RTRIM(MaterialName))) > 0)
);
CREATE TABLE [retail_manufacturing].[ProductionOrders] (
    [ProductionOrderID] int NOT NULL,
    [ProductID] int NOT NULL,
    [ProductionReference] nvarchar(80) NOT NULL,
    [ProductionCategory] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [PlannedCost] decimal(12,2) NULL,
    [PlannedUnits] int NOT NULL,
    [ProductionDate] date NOT NULL,
    [StartedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentProductionOrderID] int NULL,
    CONSTRAINT [PK_ProductionOrders] PRIMARY KEY ([ProductionOrderID]),
    CONSTRAINT [UQ_ProductionOrders_1] UNIQUE (ProductionReference),
    CONSTRAINT [CK_ProductionOrders_1] CHECK (ProductionCategory IN ('A','B','C')),
    CONSTRAINT [CK_ProductionOrders_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_ProductionOrders_3] CHECK (PlannedCost >= 0),
    CONSTRAINT [CK_ProductionOrders_4] CHECK (PlannedUnits > 0),
    CONSTRAINT [CK_ProductionOrders_5] CHECK (ParentProductionOrderID IS NULL OR ParentProductionOrderID <> ProductionOrderID),
    CONSTRAINT [CK_ProductionOrders_6] CHECK (LEN(LTRIM(RTRIM(ProductionReference))) > 0),
    CONSTRAINT [FK_ProductionOrders_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_manufacturing].[Products] ([ProductID]),
    CONSTRAINT [FK_ProductionOrders_ParentProductionOrderID] FOREIGN KEY ([ParentProductionOrderID]) REFERENCES [retail_manufacturing].[ProductionOrders] ([ProductionOrderID])
);
CREATE TABLE [retail_manufacturing].[BillOfMaterials] (
    [BOMID] int NOT NULL,
    [ProductID] int NOT NULL,
    [MaterialID] int NOT NULL,
    [QuantityPerUnit] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_BillOfMaterials] PRIMARY KEY ([BOMID]),
    CONSTRAINT [UQ_BillOfMaterials_1] UNIQUE (ProductID, MaterialID),
    CONSTRAINT [CK_BillOfMaterials_1] CHECK (QuantityPerUnit > 0),
    CONSTRAINT [FK_BillOfMaterials_ProductID] FOREIGN KEY ([ProductID]) REFERENCES [retail_manufacturing].[Products] ([ProductID]),
    CONSTRAINT [FK_BillOfMaterials_MaterialID] FOREIGN KEY ([MaterialID]) REFERENCES [retail_manufacturing].[Materials] ([MaterialID])
);
CREATE TABLE [retail_manufacturing].[MaterialUsage] (
    [UsageID] int NOT NULL,
    [ProductionOrderID] int NOT NULL,
    [MaterialID] int NOT NULL,
    [QuantityUsed] decimal(12,2) NOT NULL,
    [UsageDate] date NOT NULL,
    CONSTRAINT [PK_MaterialUsage] PRIMARY KEY ([UsageID]),
    CONSTRAINT [UQ_MaterialUsage_1] UNIQUE (ProductionOrderID, MaterialID),
    CONSTRAINT [CK_MaterialUsage_1] CHECK (QuantityUsed > 0),
    CONSTRAINT [FK_MaterialUsage_ProductionOrderID] FOREIGN KEY ([ProductionOrderID]) REFERENCES [retail_manufacturing].[ProductionOrders] ([ProductionOrderID]),
    CONSTRAINT [FK_MaterialUsage_MaterialID] FOREIGN KEY ([MaterialID]) REFERENCES [retail_manufacturing].[Materials] ([MaterialID])
);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
