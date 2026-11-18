-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [brokerage].[Clients] (ClientID, ClientName, ClientReference, Email) VALUES
(1,N'Investor 1',N'CLIENT-1',N'investor1@example.test'),
(2,N'Investor 2',N'CLIENT-2',N'investor2@example.test'),
(3,N'Investor 3',N'CLIENT-3',N'investor3@example.test'),
(4,N'Investor 4',N'CLIENT-4',N'investor4@example.test'),
(5,N'Investor 5',N'CLIENT-5',N'investor5@example.test');
INSERT INTO [brokerage].[Securities] (SecurityID, SecurityName, Symbol, AssetClass) VALUES
(1,N'Training Equity Alpha',N'DEMO-A',N'Stock'),
(2,N'Training Equity Beta',N'DEMO-B',N'Stock'),
(3,N'Training Fund Gamma',N'DEMO-C',N'ETF'),
(4,N'Training Fund Delta',N'DEMO-D',N'ETF'),
(5,N'Unused Training Equity',N'DEMO-E',N'Stock');
INSERT INTO [brokerage].[BrokerageAccounts] (AccountID, AccountName, AccountNumber, Region, ClientID) VALUES
(1,N'BrokerageAccounts Alpha',N'ACC-1',N'North',1),
(2,N'BrokerageAccounts Beta',N'ACC-2',N'South',2),
(3,N'BrokerageAccounts Gamma',N'ACC-3',N'North',3),
(4,N'BrokerageAccounts Delta',N'ACC-4',N'West',4),
(5,N'BrokerageAccounts Unused',N'ACC-5',N'East',5);
INSERT INTO [brokerage].[TradeOrders] (OrderID, AccountID, OrderReference, RoutingCategory, WorkflowStatus, EstimatedValue, RequestedQuantity, OrderDate, SubmittedAt, RecordedAt, Note, BackupNote, ParentOrderID, SecurityID, Side) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1,N'Buy'),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2,N'Buy'),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3,N'Buy'),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4,N'Buy'),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1,N'Buy'),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2,N'Buy'),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3,N'Buy'),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4,N'Buy'),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1,N'Buy'),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2,N'Buy'),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3,N'Buy'),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4,N'Buy');
INSERT INTO [brokerage].[Executions] (ExecutionID, OrderID, ExecutionReference, ExecutedQuantity, ExecutionPrice, ExecutedAt) VALUES
(1,1,N'FILL-1',0.4,100,N'2024-01-01T12:31:00'),
(2,1,N'FILL-2',0.6,101,N'2024-01-01T12:32:00'),
(3,2,N'FILL-3',1,99,N'2024-01-02T12:31:00'),
(4,2,N'FILL-4',0.5,100,N'2024-01-02T12:32:00'),
(5,3,N'FILL-5',3,101,N'2024-01-02T12:33:00'),
(6,6,N'FILL-6',1,150,N'2024-02-10T12:31:00');
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
