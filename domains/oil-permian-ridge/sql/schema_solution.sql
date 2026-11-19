-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
