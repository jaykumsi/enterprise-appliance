# Healthcare: CONSTRAINTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/CONSTRAINTS.md)

## Teaching and troubleshooting

These exercises deliberately attempt invalid writes. An expected constraint error means the rule worked. Confirm the original rows remain unchanged; do not remove the constraint to make the write succeed.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### CONSTRAINTS-01-04 — Not Null

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
BEGIN TRY
 UPDATE [healthcare].[Patients] SET PatientName=NULL WHERE PatientID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>515 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-01-09 — Not Null

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
BEGIN TRY
 UPDATE [healthcare].[Doctors] SET DoctorName=NULL WHERE DoctorID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>515 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-01-14 — Not Null

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
BEGIN TRY
 UPDATE [healthcare].[Medications] SET MedicationName=NULL WHERE MedicationID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>515 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-01-19 — Not Null

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 UPDATE [healthcare].[Encounters] SET PatientID=NULL WHERE EncounterID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>515 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-01-24 — Not Null

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 UPDATE [healthcare].[Prescriptions] SET EncounterID=NULL WHERE PrescriptionID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>515 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-02-04 — Unique

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Patients] (PatientID, PatientName, PatientNumber, Region) VALUES
(100,N'Patients Alpha',N'PAT-1',N'North');
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-02-09 — Unique

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Doctors] (DoctorID, DoctorName, LicenseNumber, Specialty) VALUES
(100,N'Doctor 1',N'LIC-1',N'General');
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-02-14 — Unique

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Medications] (MedicationID, MedicationName, MedicationCode, UnitCost) VALUES
(100,N'Training medication 1',N'MED-1',5);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-02-19 — Unique

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Encounters] (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge, ServiceUnits, EncounterDate, StartedAt, RecordedAt, Note, BackupNote, ParentEncounterID, DoctorID) VALUES
(100,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-02-24 — Unique

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Prescriptions] (PrescriptionID, EncounterID, MedicationID, PrescriptionReference, Quantity) VALUES
(100,1,1,N'RX-1',2);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-03-04 — Check

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
BEGIN TRY
 UPDATE [healthcare].[Patients] SET PatientName=N'   ' WHERE PatientID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-03-09 — Check

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
BEGIN TRY
 UPDATE [healthcare].[Doctors] SET DoctorName=N'   ' WHERE DoctorID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-03-14 — Check

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
BEGIN TRY
 UPDATE [healthcare].[Medications] SET UnitCost=-1 WHERE MedicationID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-03-19 — Check

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 UPDATE [healthcare].[Encounters] SET EncounterType='INVALID' WHERE EncounterID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-03-24 — Check

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 UPDATE [healthcare].[Prescriptions] SET Quantity=-1 WHERE PrescriptionID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-04-04 — Primary key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Patients] (PatientID, PatientName, PatientNumber, Region) VALUES
(1,N'Patients Alpha',N'PAT-1',N'North');
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Patients] WHERE PatientID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-04-09 — Primary key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Doctors] (DoctorID, DoctorName, LicenseNumber, Specialty) VALUES
(1,N'Doctor 1',N'LIC-1',N'General');
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Doctors] WHERE DoctorID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-04-14 — Primary key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Medications] (MedicationID, MedicationName, MedicationCode, UnitCost) VALUES
(1,N'Training medication 1',N'MED-1',5);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Medications] WHERE MedicationID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-04-19 — Primary key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Encounters] (EncounterID, PatientID, EncounterReference, EncounterType, Status, Charge, ServiceUnits, EncounterDate, StartedAt, RecordedAt, Note, BackupNote, ParentEncounterID, DoctorID) VALUES
(1,1,N'  Alpha-One  ',N'A',N'Open',100,1,N'20240101',N'2024-01-01T12:30:45.123',N'2024-01-01T12:30:45.123+00:00',NULL,N'backup',NULL,1);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-04-24 — Primary key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 INSERT INTO [healthcare].[Prescriptions] (PrescriptionID, EncounterID, MedicationID, PrescriptionReference, Quantity) VALUES
(1,1,1,N'RX-1',2);
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>2627 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-05-04 — Foreign key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 UPDATE [healthcare].[Encounters] SET PatientID=999 WHERE EncounterID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-05-09 — Foreign key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 UPDATE [healthcare].[Encounters] SET ParentEncounterID=999 WHERE EncounterID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-05-14 — Foreign key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
BEGIN TRY
 UPDATE [healthcare].[Encounters] SET DoctorID=999 WHERE EncounterID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Encounters] WHERE EncounterID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-05-19 — Foreign key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 UPDATE [healthcare].[Prescriptions] SET EncounterID=999 WHERE PrescriptionID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

### CONSTRAINTS-05-24 — Foreign key

**Question**

[Canonical questions](../questions/CONSTRAINTS.md)

**Reference answer**

```sql
SET XACT_ABORT OFF;
IF @@TRANCOUNT <> 0 THROW 51000, 'Use a fresh session with no open transaction', 1;
BEGIN TRANSACTION;
BEGIN TRY
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
BEGIN TRY
 UPDATE [healthcare].[Prescriptions] SET MedicationID=999 WHERE PrescriptionID=1;
 THROW 51001, 'Invalid value was unexpectedly accepted', 1;
END TRY
BEGIN CATCH
 IF ERROR_NUMBER()<>547 THROW;
 SELECT ERROR_NUMBER() AS ExpectedError;
END CATCH;
SELECT * FROM [healthcare].[Prescriptions] WHERE PrescriptionID=1;
ROLLBACK TRANSACTION;
END TRY
BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 THROW;
END CATCH;
```

**Check and explain:** SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Not Null: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-B01

**Valid baseline**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B02

**Missing input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B03

**Exact boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B04

**Two independent rows**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B05

**Duplicate proposal**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B06

**Metadata evidence**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B07

**Unknown versus zero**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B08

**Wrong type input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B09

**Dependency order**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B10

**Rejected request preserves state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B11

**Deterministic presentation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B12

**Least sufficient permission**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B13

**Name and scope collision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B14

**Empty state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-B15

**Independent acceptance check**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-I01

**Batch with mixed validity**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I02

**Lossless round trip**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I03

**All conflicting keys**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I04

**Drift before change**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I05

**Application bypass**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I06

**Partial input correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I07

**Idempotency decision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I08

**Reference membership**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I09

**Schema version precondition**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I10

**Before-image restoration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I14

**Two independent implementations**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-I15

**Auditable decision table**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A03

**Crash after accepted effect**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A07

**Restartable chunked repair**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A08

**Stale authorization at execution**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A10

**Atomic publication boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A11

**Type or scope spoofing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A12

**Nonunique history correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A13

**Owner failure and fencing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A14

**Independent corruption detector**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-01-A15

**Adversarial native case study**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SQL Server should show error 515. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Unique: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-B01

**Valid baseline**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B02

**Missing input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B03

**Exact boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B04

**Two independent rows**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B05

**Duplicate proposal**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B06

**Metadata evidence**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B07

**Unknown versus zero**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B08

**Wrong type input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B09

**Dependency order**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B10

**Rejected request preserves state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B11

**Deterministic presentation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B12

**Least sufficient permission**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B13

**Name and scope collision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B14

**Empty state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-B15

**Independent acceptance check**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-I01

**Batch with mixed validity**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I02

**Lossless round trip**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I03

**All conflicting keys**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I04

**Drift before change**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I05

**Application bypass**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I06

**Partial input correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I07

**Idempotency decision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I08

**Reference membership**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I09

**Schema version precondition**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I10

**Before-image restoration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I14

**Two independent implementations**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-I15

**Auditable decision table**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A03

**Crash after accepted effect**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A07

**Restartable chunked repair**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A08

**Stale authorization at execution**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A10

**Atomic publication boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A11

**Type or scope spoofing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A12

**Nonunique history correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A13

**Owner failure and fencing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A14

**Independent corruption detector**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-02-A15

**Adversarial native case study**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Check: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-B01

**Valid baseline**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B02

**Missing input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B03

**Exact boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B04

**Two independent rows**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B05

**Duplicate proposal**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B06

**Metadata evidence**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B07

**Unknown versus zero**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B08

**Wrong type input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B09

**Dependency order**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B10

**Rejected request preserves state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B11

**Deterministic presentation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B12

**Least sufficient permission**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B13

**Name and scope collision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B14

**Empty state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-B15

**Independent acceptance check**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-I01

**Batch with mixed validity**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I02

**Lossless round trip**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I03

**All conflicting keys**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I04

**Drift before change**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I05

**Application bypass**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I06

**Partial input correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I07

**Idempotency decision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I08

**Reference membership**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I09

**Schema version precondition**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I10

**Before-image restoration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I14

**Two independent implementations**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-I15

**Auditable decision table**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A03

**Crash after accepted effect**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A07

**Restartable chunked repair**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A08

**Stale authorization at execution**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A10

**Atomic publication boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A11

**Type or scope spoofing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A12

**Nonunique history correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A13

**Owner failure and fencing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A14

**Independent corruption detector**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-03-A15

**Adversarial native case study**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Primary key: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-B01

**Valid baseline**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B02

**Missing input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B03

**Exact boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B04

**Two independent rows**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B05

**Duplicate proposal**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B06

**Metadata evidence**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B07

**Unknown versus zero**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B08

**Wrong type input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B09

**Dependency order**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B10

**Rejected request preserves state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B11

**Deterministic presentation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B12

**Least sufficient permission**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B13

**Name and scope collision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B14

**Empty state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-B15

**Independent acceptance check**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-I01

**Batch with mixed validity**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I02

**Lossless round trip**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I03

**All conflicting keys**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I04

**Drift before change**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I05

**Application bypass**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I06

**Partial input correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I07

**Idempotency decision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I08

**Reference membership**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I09

**Schema version precondition**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I10

**Before-image restoration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I11

**Representation-aware reconciliation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I12

**Safe dynamic identifier**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I13

**Precision and aggregate boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I14

**Two independent implementations**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-I15

**Auditable decision table**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-A01

**Zero-loss representation migration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A02

**Conflicting concurrent actors**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A03

**Crash after accepted effect**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A04

**Dependency graph rebuild**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A05

**Collation and canonicalization trap**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A07

**Restartable chunked repair**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A08

**Stale authorization at execution**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A10

**Atomic publication boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A11

**Type or scope spoofing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A12

**Nonunique history correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A13

**Owner failure and fencing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A14

**Independent corruption detector**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-04-A15

**Adversarial native case study**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-04-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SQL Server should show error 2627. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Foreign key: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-B01

**Valid baseline**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B02

**Missing input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B03

**Exact boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B04

**Two independent rows**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B05

**Duplicate proposal**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B06

**Metadata evidence**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B07

**Unknown versus zero**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B08

**Wrong type input**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B09

**Dependency order**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B10

**Rejected request preserves state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B11

**Deterministic presentation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B12

**Least sufficient permission**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B13

**Name and scope collision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B14

**Empty state**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-B15

**Independent acceptance check**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-I01

**Batch with mixed validity**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I02

**Lossless round trip**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I03

**All conflicting keys**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I04

**Drift before change**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I05

**Application bypass**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I06

**Partial input correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I07

**Idempotency decision**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I08

**Reference membership**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I09

**Schema version precondition**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I10

**Before-image restoration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I11

**Representation-aware reconciliation**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I12

**Safe dynamic identifier**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I13

**Precision and aggregate boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I14

**Two independent implementations**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-I15

**Auditable decision table**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-A01

**Zero-loss representation migration**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A02

**Conflicting concurrent actors**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A03

**Crash after accepted effect**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A04

**Dependency graph rebuild**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A05

**Collation and canonicalization trap**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A07

**Restartable chunked repair**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A08

**Stale authorization at execution**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A10

**Atomic publication boundary**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A11

**Type or scope spoofing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A12

**Nonunique history correction**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A13

**Owner failure and fencing**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A14

**Independent corruption detector**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-CONSTRAINTS-05-A15

**Adversarial native case study**

[Canonical question](../questions/CONSTRAINTS.md#healthcare-constraints-05-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: SQL Server should show error 547. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.

**Core reference:** Find `CONSTRAINTS-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied answer key

Historical references require instructor review on the large fixture. These are not newly validated levelled references. [Selection audit](EXERCISE_SELECTION.md).

##### CONSTRAINTS-I02: Multi-column CHECK

[Question](../questions/CONSTRAINTS.md)

```sql
ALTER TABLE healthcare.Encounters
ADD CONSTRAINT CK_Encounters_ClosedHasCharge
CHECK (Status <> 'Closed' OR Charge IS NOT NULL);

SELECT name, definition FROM sys.check_constraints WHERE name = 'CK_Encounters_ClosedHasCharge';
```

**How it works:** "If A then B" is written as `NOT A OR B`. A table-level CHECK can compare several columns of the same row.

**Expected result:** 1 row

| name | definition |
|---|---|
| CK\_Encounters\_ClosedHasCharge | ([Status]<>'Closed' OR [Charge] IS NOT NULL) |

##### CONSTRAINTS-I04: Find foreign keys

[Question](../questions/CONSTRAINTS.md)

```sql
SELECT fk.name AS ForeignKey,
       OBJECT_NAME(fkc.parent_object_id)  AS ChildTable,
       COL_NAME(fkc.parent_object_id, fkc.parent_column_id)         AS ChildColumn,
       OBJECT_NAME(fkc.referenced_object_id) AS ParentTable,
       COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS ParentColumn
FROM sys.foreign_keys AS fk
JOIN sys.foreign_key_columns AS fkc ON fkc.constraint_object_id = fk.object_id
WHERE SCHEMA_NAME(fk.schema_id) = 'healthcare'
ORDER BY ChildTable, ForeignKey;
```

**How it works:** These system views describe the relationships, which is useful for drawing an ER diagram or deciding load order.

**Expected result:** 5 rows

| ForeignKey | ChildTable | ChildColumn | ParentTable | ParentColumn |
|---|---|---|---|---|
| FK\_Encounters\_DoctorID | Encounters | DoctorID | Doctors | DoctorID |
| FK\_Encounters\_ParentEncounterID | Encounters | ParentEncounterID | Encounters | EncounterID |
| FK\_Encounters\_PatientID | Encounters | PatientID | Patients | PatientID |
| FK\_Prescriptions\_EncounterID | Prescriptions | EncounterID | Encounters | EncounterID |
| FK\_Prescriptions\_MedicationID | Prescriptions | MedicationID | Medications | MedicationID |

##### CONSTRAINTS-I07: Untrusted constraints

[Question](../questions/CONSTRAINTS.md)

```sql
SELECT name, type_desc, is_disabled, is_not_trusted
FROM sys.check_constraints
WHERE is_disabled = 1 OR is_not_trusted = 1
UNION ALL
SELECT name, type_desc, is_disabled, is_not_trusted
FROM sys.foreign_keys
WHERE is_disabled = 1 OR is_not_trusted = 1;
```

**How it works:** An empty result is healthy. Untrusted constraints are a common hidden problem after bulk loads.

**Expected result:** 0 rows (an empty result is the correct answer here).

##### CONSTRAINTS-I08: Unique but allow many NULLs

[Question](../questions/CONSTRAINTS.md)

```sql
ALTER TABLE healthcare.Patients ADD NationalID varchar(20) NULL;
GO
CREATE UNIQUE INDEX UX_Patients_NationalID
ON healthcare.Patients (NationalID)
WHERE NationalID IS NOT NULL;

UPDATE healthcare.Patients SET NationalID = 'N-1' WHERE PatientID = 1;
SELECT COUNT(*) AS PatientsWithNullID FROM healthcare.Patients WHERE NationalID IS NULL;
```

**How it works:** A UNIQUE constraint allows only one NULL in SQL Server. A filtered unique index ignores NULLs, so it allows any number of them.

**Expected result:** 1 row

| PatientsWithNullID |
|---|
| 99 |

##### CONSTRAINTS-A02: CHECK passes on NULL

[Question](../questions/CONSTRAINTS.md)

```sql
UPDATE healthcare.Encounters SET Charge = NULL WHERE EncounterID = 1;

SELECT EncounterID, Charge FROM healthcare.Encounters WHERE EncounterID = 1;
```

**How it works:** A CHECK fails only when the condition is FALSE. NULL >= 0 is UNKNOWN, so it is allowed. Add NOT NULL if a value is required. A common interview question.

**Expected result:** 1 row

| EncounterID | Charge |
|---|---|
| 1 | NULL |
