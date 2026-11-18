-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
