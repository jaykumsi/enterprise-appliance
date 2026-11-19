-- Load only AFTER all five tables are created; run once.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
INSERT INTO [healthcare].[Patients] (PatientID, PatientName, PatientNumber, Region) VALUES
(1,N'Patients Alpha',N'PAT-1',N'North'),
(2,N'Patients Beta',N'PAT-2',N'South'),
(3,N'Patients Gamma',N'PAT-3',N'North'),
(4,N'Patients Delta',N'PAT-4',N'West'),
(5,N'Patients Unused',N'PAT-5',N'East');
INSERT INTO [healthcare].[Doctors] (DoctorID, DoctorName, LicenseNumber, Specialty) VALUES
(1,N'Doctor 1',N'LIC-1',N'General'),
(2,N'Doctor 2',N'LIC-2',N'Cardiology'),
(3,N'Doctor 3',N'LIC-3',N'General'),
(4,N'Doctor 4',N'LIC-4',N'Dermatology'),
(5,N'Doctor 5',N'LIC-5',N'Neurology');
INSERT INTO [healthcare].[Medications] (MedicationID, MedicationName, MedicationCode, UnitCost) VALUES
(1,N'Training medication 1',N'MED-1',5),
(2,N'Training medication 2',N'MED-2',10),
(3,N'Training medication 3',N'MED-3',15),
(4,N'Training medication 4',N'MED-4',20),
(5,N'Training medication 5',N'MED-5',25);
INSERT INTO [healthcare].[Encounters] (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge, ServiceUnits, EncounterDate, StartedAt, RecordedAt, Note, BackupNote, ParentEncounterID, DoctorID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1),
(2,1,N'beta-Two',N'B',N'Closed',200,2,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',NULL,1,2),
(3,2,N'Gamma-Three ',N'C',N'Pending',200,3,N'20240102',N'2024-01-02T12:30:45.123',N'2024-01-02T12:30:45.123+00:00',N'confirmed',N'backup',1,3),
(4,2,N' Delta-Four',N'A',N'Open',NULL,4,N'20240103',N'2024-01-03T12:30:45.123',N'2024-01-03T12:30:45.123+00:00',NULL,NULL,2,4),
(5,3,N'Echo-Five',N'B',N'Closed',50,1,N'20240201',N'2024-02-01T12:30:45.123',N'2024-02-01T12:30:45.123+00:00',N'confirmed',N'backup',2,1),
(6,3,N'ALPHA-Six',N'C',N'Pending',300,2,N'20240210',N'2024-02-10T12:30:45.123',N'2024-02-10T12:30:45.123+00:00',N'confirmed',NULL,3,2),
(7,4,N'Zero-Seven',N'A',N'Open',0,3,N'20240229',N'2024-02-29T12:30:45.123',N'2024-02-29T12:30:45.123+00:00',NULL,N'backup',3,3),
(8,4,N'Review-Eight',N'B',N'Closed',150,4,N'20240301',N'2024-03-01T12:30:45.123',N'2024-03-01T12:30:45.123+00:00',N'confirmed',NULL,4,4),
(9,4,N'Zulu-Nine',N'C',N'Pending',300,1,N'20240310',N'2024-03-10T12:30:45.123',N'2024-03-10T12:30:45.123+00:00',N'confirmed',N'backup',4,1),
(10,4,N'Iota-Ten',N'A',N'Open',80,2,N'20241103',N'2024-11-03T12:30:45.123',N'2024-11-03T12:30:45.123+00:00',NULL,NULL,5,2),
(11,1,N'Kappa-Eleven',N'B',N'Closed',120,3,N'20241231',N'2024-12-31T12:30:45.123',N'2024-12-31T12:30:45.123+00:00',N'confirmed',N'backup',5,3),
(12,2,N'Last-Twelve',N'C',N'Pending',200,4,N'20250101',N'2025-01-01T12:30:45.123',N'2025-01-01T12:30:45.123+00:00',N'confirmed',NULL,6,4);
INSERT INTO [healthcare].[Prescriptions] (PrescriptionID, EncounterID, MedicationID, PrescriptionReference, Quantity) VALUES
(1,1,1,N'RX-1',2),
(2,1,2,N'RX-2',3),
(3,2,3,N'RX-3',1),
(4,3,1,N'RX-4',2),
(5,6,4,N'RX-5',4);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
