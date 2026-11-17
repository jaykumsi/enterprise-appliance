# Healthcare — CONSTRAINTS

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

## Not Null

### CONSTRAINTS-01-04

**Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-09

**Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-14

**Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-19

**Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-01-24

**Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Unique

### CONSTRAINTS-02-04

**Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-09

**Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-14

**Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-19

**Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-02-24

**Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Check

### CONSTRAINTS-03-04

**Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-09

**Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-14

**Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-19

**Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-03-24

**Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Primary key

### CONSTRAINTS-04-04

**Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-09

**Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-14

**Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-19

**Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-04-24

**Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

## Foreign key

### CONSTRAINTS-05-04

**Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-09

**Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-14

**Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-19

**Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

### CONSTRAINTS-05-24

**Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Not Null: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-01-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values. In the supplied sample data, `PatientName` is `Patients Alpha`.
2. Try to change `PatientName` to `NULL` in the row where `PatientID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Patients` have a value for `PatientName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values. In the supplied sample data, `DoctorName` is `Doctor 1`.
2. Try to change `DoctorName` to `NULL` in the row where `DoctorID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Doctors` have a value for `DoctorName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values. In the supplied sample data, `MedicationName` is `Training medication 1`.
2. Try to change `MedicationName` to `NULL` in the row where `MedicationID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Medications` have a value for `MedicationName`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values. In the supplied sample data, `PatientID` is `1`.
2. Try to change `PatientID` to `NULL` in the row where `EncounterID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Encounters` have a value for `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-01-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice NOT NULL on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values. In the supplied sample data, `EncounterID` is `1`.
2. Try to change `EncounterID` to `NULL` in the row where `PrescriptionID = 1`. NULL means no value; it is different from an empty text value.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why should every row in `Prescriptions` have a value for `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Unique: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-02-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PatientID` to `100`. Leave the other values the same. The UNIQUE rule on `PatientNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PatientID` value not enough when `PatientNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add a copy of row 1, but change only `DoctorID` to `100`. Leave the other values the same. The UNIQUE rule on `LicenseNumber` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `DoctorID` value not enough when `LicenseNumber` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add a copy of row 1, but change only `MedicationID` to `100`. Leave the other values the same. The UNIQUE rule on `MedicationCode` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `MedicationID` value not enough when `MedicationCode` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add a copy of row 1, but change only `EncounterID` to `100`. Leave the other values the same. The UNIQUE rule on `EncounterReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `EncounterID` value not enough when `EncounterReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-02-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice UNIQUE on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add a copy of row 1, but change only `PrescriptionID` to `100`. Leave the other values the same. The UNIQUE rule on `PrescriptionReference` does not allow those values to be repeated.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why is a new `PrescriptionID` value not enough when `PrescriptionReference` must also be unique?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Check: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-03-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(PatientName))) > 0`. Try to change `PatientName` to `N'   '` in the row where `PatientID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. This table has the rule `LEN(LTRIM(RTRIM(DoctorName))) > 0`. Try to change `DoctorName` to `N'   '` in the row where `DoctorID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. This table has the rule `UnitCost >= 0`. Try to change `UnitCost` to `-1` in the row where `MedicationID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. This table has the rule `EncounterType IN ('A','B','C')`. Try to change `EncounterType` to `'INVALID'` in the row where `EncounterID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-03-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice CHECK on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. This table has the rule `Quantity > 0`. Try to change `Quantity` to `-1` in the row where `PrescriptionID = 1`.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Primary key: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-04-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Patients**

**Before you start:** Use `[healthcare].[Patients]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PatientID = 1` and note its values.
2. Try to add another copy of the row where `PatientID = 1`. Keep the same `PatientID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Doctors**

**Before you start:** Use `[healthcare].[Doctors]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `DoctorID = 1` and note its values.
2. Try to add another copy of the row where `DoctorID = 1`. Keep the same `DoctorID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Medications**

**Before you start:** Use `[healthcare].[Medications]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `MedicationID = 1` and note its values.
2. Try to add another copy of the row where `MedicationID = 1`. Keep the same `MedicationID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to add another copy of the row where `EncounterID = 1`. Keep the same `EncounterID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-04-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice PRIMARY KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to add another copy of the row where `PrescriptionID = 1`. Keep the same `PrescriptionID` value in the new row.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why can two rows not have the same primary key value in `PrescriptionID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

### Foreign key: progression

**Beginner:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-B01

**Valid baseline** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core in a fresh practice copy. Return the requested result and a before/after object or value snapshot. Explain which business rule it establishes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B02

**Missing input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Propose one missing required input from the core and one explicitly allowed missing input. Execute both where supported,or prove that the second case is not supported. Return accepted/rejected with the exact field or object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B03

**Exact boundary** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Find a real boundary of this core:representable value,width,nullability,valid identifier or object dependency. Demonstrate the boundary and its nearest invalid neighbor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B04

**Two independent rows** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Run two independent valid instances of the core with different keys or values. Return both outcomes and prove changing one cannot overwrite the other. For a scalar construct,use separate values rather than inventing persistent columns.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B05

**Duplicate proposal** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repeat an identical core request. Determine whether it is a legal repeat,a duplicate-key conflict,or a second independent value. Return the observed result without suppressing the rejection.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B06

**Metadata evidence** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return a compact specification of the core's actual output/object type,nullability,key membership or scope. Obtain evidence from SQL Server metadata or a native demonstrator,not a guessed type name.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B07

**Unknown versus zero** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Create the smallest core-related example separating missing data,known zero and absent row/object. Return three labelled outcomes;reject a representation unsupported by this construct.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B08

**Wrong type input** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Supply an input of the wrong declared type and a correctly typed equivalent. Show whether SQL Server rejects,converts,rounds or truncates it,and return the resulting value/error category.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B09

**Dependency order** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** List the core's real prerequisites,then execute one deliberately incorrect order in a practice copy and the correct order. Return the failing dependency and the final valid state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B10

**Rejected request preserves state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core request that must be rejected under a stated rule. Capture the relevant state before and after;prove no prohibited value/object survives.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B11

**Deterministic presentation** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Return the core result with exact column names and a deterministic order where rows exist. Demonstrate a tied/identical-value case using different valid keys.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B12

**Least sufficient permission** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Identify the minimum permission needed for the core and demonstrate an allowed and denied action under instructor-provided principals. A local decision table is acceptable until a native principal is available.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B13

**Name and scope collision** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct two legal scopes/keys with the same display name or similar identifier. Prove the core resolves the intended one using actual identifiers.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B14

**Empty state** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Execute the core with an empty source or absent target as appropriate. Return a legal empty result,required creation,or precise precondition failure.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-B15

**Independent acceptance check** · Beginner · Suggested coding time:15 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core and an independent assertion derived from its business rule. Introduce one wrong value/object definition in a practice copy and show the assertion catches it.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Intermediate:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-I01

**Batch with mixed validity** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Prepare five core-related requests:two valid,one missing-required,one conflicting key/object and one representation error. Validate all before applying accepted requests individually;return one disposition per input position.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I02

**Lossless round trip** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Move a valid core value/object specification through a second declared representation and back. Return full equality evidence and a counterexample where a superficially similar conversion loses information.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I03

**All conflicting keys** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a candidate batch containing repeated keys under the real equality/collation rules. Return every member of each conflict group;do not select an arbitrary survivor.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I04

**Drift before change** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Change one existing type,nullability,key,scope or prerequisite relative to the core contract. Write a preflight that reports the exact difference and prevents an incompatible operation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I05

**Application bypass** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core rule at the application/input layer and at the authoritative database/native boundary. Show a direct bypass attempt and its observable rejection or a precise limit of database enforcement.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I06

**Partial input correction** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Load or model three good and two bad core-related inputs. Return a corrected plan only for the bad inputs while preserving the good keys/values. Do not silently change unknown values to zero.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I07

**Idempotency decision** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add a durable request identity to a repeatable core operation or an external operation journal where the construct itself is not stateful. Identical repeat returns prior outcome;different payload under the same ID is CONFLICT.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I08

**Reference membership** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Add one valid and one missing parent/reference/scope dependency to a core example. Return all missing dependencies before proceeding;do not disable constraints to make the case pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I09

**Schema version precondition** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Declare schema/contract version1,plan the core change,then change to version2 before execution. Reject the stale plan and regenerate it against version2.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I10

**Before-image restoration** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Capture enough evidence to reconstruct the original practice state after the core. Demonstrate a separate explicit repair/reset plan,without claiming that an ordinary failed request undoes prior committed changes.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I11

**Representation-aware reconciliation** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Compare two core-related datasets/specifications with matching counts but different complete values. Return missing,extra and changed items using stable keys or full-row multiplicity.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I12

**Safe dynamic identifier** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Accept a requested core object identifier only from a declared allowlist. Demonstrate a valid identifier and a crafted separator/quote attack;the rejected input must never become executable SQL.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I13

**Precision and aggregate boundary** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Choose a core-related value where individual rows fit but a derived aggregate/combined representation may not. Demonstrate the risk and an explicit safe representation,or prove why this construct cannot be aggregated.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I14

**Two independent implementations** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Implement the core business rule with two independent supported strategies. Compare complete outcomes on normal,empty,boundary and invalid cases. Where only one native construct is possible,use an independent validation model for the second.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-I15

**Auditable decision table** · Intermediate · Suggested coding time:30 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver a finite table of core-related input states and expected accepted/rejected/converted outcomes,then execute it. Include one context/type/dependency interaction that an isolated happy-path check misses.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

**Advanced:15 questions**

#### HEALTHCARE-CONSTRAINTS-05-A01

**Zero-loss representation migration** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Design and demonstrate an expand/validate/switch migration of the core's representation or object contract with old/new consumers active. Include a nonrepresentable input and prove it is quarantined before switch. Return compatibility and full-value reconciliation evidence.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A02

**Conflicting concurrent actors** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two sessions or a deterministic native/local interleaving attempting incompatible core-related changes after reading the same old state. Implement a commit-time version/ownership precondition and show exactly one wins.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A03

**Crash after accepted effect** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model the core operation accepting its database effect but the caller missing the response. Use durable action identity to discover the accepted outcome before retrying. Include a conflicting replay payload.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A04

**Dependency graph rebuild** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Rebuild a core-related graph of objects/records with one self-reference and a cross-table dependency. Return a valid staged execution order and an explicit diagnosis for a cycle that cannot be created in one simple pass.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A05

**Collation and canonicalization trap** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct distinct source keys/representations that collapse under a proposed normalization,collation or conversion used by the core. Build a pre-migration collision report and a deterministic reject/remap plan with lineage.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A06

**Intermediate overflow or precision loss** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct values that individually satisfy the core but break an intermediate computation or derived representation. Supply the corrected native expression/schema and an independent exact-value check. For nonnumeric constructs,use a concrete length/encoding/structural-loss boundary.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A07

**Restartable chunked repair** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Repair a large core-related dataset in stable-key chunks with a durable journal. Stop after an accepted chunk and before acknowledgment,then resume without skipping or applying a business correction twice. Return the final reconciliation.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A08

**Stale authorization at execution** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Authorize a core-related object/action,then revoke or change its ownership before execution. Demonstrate a fresh authorization/version check at the actual action boundary and show the old plan cannot leak data or modify the object.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A09

**Mixed-version import with tombstones** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model versioned core-related records arriving out of order with deletes. Highest version wins;equal-version different content is CONFLICT. Show a delayed older row cannot resurrect a deleted key and return complete final state.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A10

**Atomic publication boundary** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build a new validated core-related representation in scratch state and publish it through a single versioned current pointer or equivalent native boundary. Inject failure before and after publication;readers must see a complete old or new contract.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A11

**Type or scope spoofing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `PatientID` to `999` in the row where `EncounterID = 1`. There is no row with `PatientID = 999` in `Patients`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `PatientID` match a value in `Patients.PatientID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Construct an untrusted input that passes a superficial text/type/name check but targets the wrong object or changes meaning after implicit conversion. Implement a typed,fully qualified validation boundary and prove both the attack and a valid request are classified correctly.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A12

**Nonunique history correction** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `ParentEncounterID` to `999` in the row where `EncounterID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `ParentEncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Model two corrections for the same business key/effective time plus a later correction. Produce a deterministic CONFLICT for contradictory equal-version input,retain prior valid history and show the later input does not erase evidence of the unresolved conflict.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A13

**Owner failure and fencing** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Encounters**

**Before you start:** Use `[healthcare].[Encounters]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `EncounterID = 1` and note its values.
2. Try to change `DoctorID` to `999` in the row where `EncounterID = 1`. There is no row with `DoctorID = 999` in `Doctors`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `DoctorID` match a value in `Doctors.DoctorID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Give two simulated/native workers performing the core-related migration/import. The first loses its lease but finishes late. Use a monotonically increasing fencing token at publication so its stale result cannot overwrite the new owner.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A14

**Independent corruption detector** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `EncounterID` to `999` in the row where `PrescriptionID = 1`. There is no row with `EncounterID = 999` in `Encounters`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `EncounterID` match a value in `Encounters.EncounterID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Build an independent scanner for the core invariant across existing rows/objects,including one orphan/missing dependency,one representation mismatch and one duplicate/version conflict where supported. Seed all three and show complete diagnostics even when global counts/totals still match.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

#### HEALTHCARE-CONSTRAINTS-05-A15

**Adversarial native case study** · Advanced · Suggested coding time:60 minutes

**Core task:** **Healthcare: Practice FOREIGN KEY on Prescriptions**

**Before you start:** Use `[healthcare].[Prescriptions]` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](DOMAIN_GUIDE.md).

1. Display the row where `PrescriptionID = 1` and note its values.
2. Try to change `MedicationID` to `999` in the row where `PrescriptionID = 1`. There is no row with `MedicationID = 999` in `Medications`. Keep the foreign key rule turned on.
3. Write down the error message SQL Server shows. An error is expected in this exercise.
4. Display the original row again. Check that its values have not changed.

**Explain:** Why must `MedicationID` match a value in `Medications.MedicationID`?

**Submit:** Your SQL, the error message, and the row shown before and after the attempt.

**Interview case:** Deliver the core plus one multi-step failure case combining three applicable hazards from precision,duplicates,scope,dependency,concurrency,encoding or unknown outcome. Provide native SQL or a precisely bounded local simulator,expected states and a recovery trace.

**Required evidence:** Return a request/disposition table(InputOrdinal,Decision,Reason),a keyed before/after state or value table,and an assertion table(CheckName,Expected,Actual,Passed). For a design choice left open,declare it before implementation and test it. Unsupported operations/types must be rejected explicitly rather than silently simulated as native SQL features.

**Environment:** Use a separate practice copy;changes persist. Ask the instructor to reset the original schema/data between independent cases. No transaction/rollback commands are required prerequisites. Principal/database provisioning needs an instructor-provided disposable environment;until then,use a clearly labelled finite local model.

**Grading boundary:** This is a practical design/native-demonstration exercise,not a single-output automatic test. An explanation without the concrete case,implementation and observed evidence is incomplete.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied practice

Selected cases supplement the assessed levelled bank. B/I/A in these older IDs are historical labels, not current difficulty ratings. [Practice route](BEST_EXERCISES.md). Historical self-checks use the large fixture and are outside the native report-validation claim. Use a fresh large-fixture practice copy for each case that changes data or permissions; changes persist.

<a id="legacy-constraints-i02"></a>

##### CONSTRAINTS-I02: Multi-column CHECK

Add a rule to Encounters: when Status is 'Closed', Charge must not be NULL.

**Expected result:** 1 row

| name | definition |
|---|---|
| CK\_Encounters\_ClosedHasCharge | ([Status]<>'Closed' OR [Charge] IS NOT NULL) |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-constraints-i04"></a>

##### CONSTRAINTS-I04: Find foreign keys

List every foreign key in the healthcare schema: child table, child column, parent table, parent column.

**Expected result:** 5 rows

| ForeignKey | ChildTable | ChildColumn | ParentTable | ParentColumn |
|---|---|---|---|---|
| FK\_Encounters\_DoctorID | Encounters | DoctorID | Doctors | DoctorID |
| FK\_Encounters\_ParentEncounterID | Encounters | ParentEncounterID | Encounters | EncounterID |
| FK\_Encounters\_PatientID | Encounters | PatientID | Patients | PatientID |
| FK\_Prescriptions\_EncounterID | Prescriptions | EncounterID | Encounters | EncounterID |
| FK\_Prescriptions\_MedicationID | Prescriptions | MedicationID | Medications | MedicationID |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-constraints-i07"></a>

##### CONSTRAINTS-I07: Untrusted constraints

Find any CHECK or FOREIGN KEY constraints that are disabled or not trusted.

**Expected result:** 0 rows (an empty result is the correct answer here).

_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-constraints-i08"></a>

##### CONSTRAINTS-I08: Unique but allow many NULLs

Add an optional NationalID column to Patients that must be unique when it has a value, while many patients can leave it NULL.

**Expected result:** 1 row

| PatientsWithNullID |
|---|
| 99 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-constraints-a02"></a>

##### CONSTRAINTS-A02: CHECK passes on NULL

Show that CHECK (Charge >= 0) allows NULL: set encounter 1's Charge to NULL and read it back.

**Expected result:** 1 row

| EncounterID | Charge |
|---|---|
| 1 | NULL |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._
