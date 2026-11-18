-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
