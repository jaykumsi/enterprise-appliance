-- Instructor schema answer. Execute in an empty training database.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
IF SCHEMA_ID(N'healthcare') IS NULL EXEC(N'CREATE SCHEMA [healthcare] AUTHORIZATION dbo;');
IF OBJECT_ID(N'healthcare.Patients') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Doctors') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Medications') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Encounters') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
IF OBJECT_ID(N'healthcare.Prescriptions') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;
CREATE TABLE [healthcare].[Patients] (
    [PatientID] int NOT NULL,
    [PatientName] nvarchar(80) NOT NULL,
    [PatientNumber] varchar(20) NOT NULL,
    [Region] varchar(10) NOT NULL,
    CONSTRAINT [PK_Patients] PRIMARY KEY ([PatientID]),
    CONSTRAINT [UQ_Patients_1] UNIQUE (PatientNumber),
    CONSTRAINT [CK_Patients_1] CHECK (LEN(LTRIM(RTRIM(PatientName))) > 0)
);
CREATE TABLE [healthcare].[Doctors] (
    [DoctorID] int NOT NULL,
    [DoctorName] nvarchar(80) NOT NULL,
    [LicenseNumber] varchar(20) NOT NULL,
    [Specialty] varchar(30) NOT NULL,
    CONSTRAINT [PK_Doctors] PRIMARY KEY ([DoctorID]),
    CONSTRAINT [UQ_Doctors_1] UNIQUE (LicenseNumber),
    CONSTRAINT [CK_Doctors_1] CHECK (LEN(LTRIM(RTRIM(DoctorName))) > 0)
);
CREATE TABLE [healthcare].[Medications] (
    [MedicationID] int NOT NULL,
    [MedicationName] nvarchar(80) NOT NULL,
    [MedicationCode] varchar(20) NOT NULL,
    [UnitCost] decimal(12,2) NOT NULL,
    CONSTRAINT [PK_Medications] PRIMARY KEY ([MedicationID]),
    CONSTRAINT [UQ_Medications_1] UNIQUE (MedicationCode),
    CONSTRAINT [CK_Medications_1] CHECK (UnitCost >= 0),
    CONSTRAINT [CK_Medications_2] CHECK (LEN(LTRIM(RTRIM(MedicationName))) > 0)
);
CREATE TABLE [healthcare].[Encounters] (
    [EncounterID] int NOT NULL,
    [PatientID] int NOT NULL,
    [EncounterReference] nvarchar(80) NOT NULL,
    [EncounterType] varchar(10) NOT NULL,
    [Status] varchar(10) NOT NULL DEFAULT ('Open'),
    [Charge] decimal(12,2) NULL,
    [ServiceUnits] int NOT NULL,
    [EncounterDate] date NOT NULL,
    [StartedAt] datetime2(3) NOT NULL,
    [RecordedAt] datetimeoffset(3) NOT NULL,
    [Note] nvarchar(100) NULL,
    [BackupNote] nvarchar(100) NULL,
    [ParentEncounterID] int NULL,
    [DoctorID] int NOT NULL,
    CONSTRAINT [PK_Encounters] PRIMARY KEY ([EncounterID]),
    CONSTRAINT [UQ_Encounters_1] UNIQUE (EncounterReference),
    CONSTRAINT [CK_Encounters_1] CHECK (EncounterType IN ('A','B','C')),
    CONSTRAINT [CK_Encounters_2] CHECK (Status IN ('Open','Closed','Pending')),
    CONSTRAINT [CK_Encounters_3] CHECK (Charge >= 0),
    CONSTRAINT [CK_Encounters_4] CHECK (ServiceUnits > 0),
    CONSTRAINT [CK_Encounters_5] CHECK (ParentEncounterID IS NULL OR ParentEncounterID <> EncounterID),
    CONSTRAINT [CK_Encounters_6] CHECK (LEN(LTRIM(RTRIM(EncounterReference))) > 0),
    CONSTRAINT [FK_Encounters_PatientID] FOREIGN KEY ([PatientID]) REFERENCES [healthcare].[Patients] ([PatientID]),
    CONSTRAINT [FK_Encounters_ParentEncounterID] FOREIGN KEY ([ParentEncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Encounters_DoctorID] FOREIGN KEY ([DoctorID]) REFERENCES [healthcare].[Doctors] ([DoctorID])
);
CREATE TABLE [healthcare].[Prescriptions] (
    [PrescriptionID] int NOT NULL,
    [EncounterID] int NOT NULL,
    [MedicationID] int NOT NULL,
    [PrescriptionReference] varchar(20) NOT NULL,
    [Quantity] int NOT NULL,
    CONSTRAINT [PK_Prescriptions] PRIMARY KEY ([PrescriptionID]),
    CONSTRAINT [UQ_Prescriptions_1] UNIQUE (PrescriptionReference),
    CONSTRAINT [CK_Prescriptions_1] CHECK (Quantity > 0),
    CONSTRAINT [CK_Prescriptions_2] CHECK (LEN(LTRIM(RTRIM(PrescriptionReference))) > 0),
    CONSTRAINT [FK_Prescriptions_EncounterID] FOREIGN KEY ([EncounterID]) REFERENCES [healthcare].[Encounters] ([EncounterID]),
    CONSTRAINT [FK_Prescriptions_MedicationID] FOREIGN KEY ([MedicationID]) REFERENCES [healthcare].[Medications] ([MedicationID])
);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
