-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
