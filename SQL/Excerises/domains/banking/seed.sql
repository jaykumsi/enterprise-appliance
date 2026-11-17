-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
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
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
