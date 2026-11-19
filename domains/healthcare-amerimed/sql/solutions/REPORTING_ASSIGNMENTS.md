# Healthcare: REPORTING ASSIGNMENTS — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/REPORTING_ASSIGNMENTS.md)

## Teaching and troubleshooting

State what one output row represents. Aggregate independent child tables before joining them to avoid multiplying totals. Compare row counts and totals to the source tables, including parents with no children.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### HEALTHCARE-REPORT-01

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.PatientID, p.PatientName, COUNT(f.EncounterID) AS EventCount, SUM(f.Charge) AS TotalAmount FROM [healthcare].[Patients] p LEFT JOIN [healthcare].[Encounters] f ON p.PatientID=f.PatientID GROUP BY p.PatientID, p.PatientName ORDER BY p.PatientID;
```

**Check and explain:** Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.

### HEALTHCARE-REPORT-02

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT p.PatientID, p.PatientName FROM [healthcare].[Patients] p WHERE NOT EXISTS (SELECT 1 FROM [healthcare].[Encounters] f WHERE f.PatientID=p.PatientID) ORDER BY p.PatientID;
```

**Check and explain:** Only master ID 5.

### HEALTHCARE-REPORT-03

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Ranked AS (SELECT EncounterID,PatientID,Charge,ROW_NUMBER() OVER(PARTITION BY PatientID ORDER BY Charge DESC,EncounterID) AS rn FROM [healthcare].[Encounters]) SELECT EncounterID,PatientID,Charge FROM Ranked WHERE rn=1 ORDER BY PatientID;
```

**Check and explain:** Master/event IDs: 1/2, 2/3, 3/6, 4/9.

### HEALTHCARE-REPORT-04

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT r.PrescriptionReference,p.PatientName,d.DoctorName,e.EncounterID,m.MedicationName,r.Quantity FROM healthcare.Prescriptions r JOIN healthcare.Encounters e ON e.EncounterID=r.EncounterID JOIN healthcare.Patients p ON p.PatientID=e.PatientID JOIN healthcare.Doctors d ON d.DoctorID=e.DoctorID JOIN healthcare.Medications m ON m.MedicationID=r.MedicationID ORDER BY r.PrescriptionID;
```

**Check and explain:** 5 rows; no real clinical instructions are implied.

### HEALTHCARE-REPORT-05

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
;WITH Rx AS (SELECT EncounterID,COUNT(*) AS PrescriptionCount FROM healthcare.Prescriptions GROUP BY EncounterID) SELECT e.EncounterID,p.PatientName,e.Charge,COALESCE(r.PrescriptionCount,0) AS PrescriptionCount FROM healthcare.Encounters e JOIN healthcare.Patients p ON p.PatientID=e.PatientID LEFT JOIN Rx r ON r.EncounterID=e.EncounterID ORDER BY e.EncounterID;
```

**Check and explain:** 12 rows. Encounter 1 charge=100 and prescription count=2. Encounter 4 charge=NULL and count=0. Known charges total 1700.

### HEALTHCARE-REPORT-06

**Question**

[Canonical questions](../questions/REPORTING_ASSIGNMENTS.md)

**Reference answer**

```sql
SELECT m.MedicationID,m.MedicationName FROM healthcare.Medications m WHERE NOT EXISTS(SELECT 1 FROM healthcare.Prescriptions p WHERE p.MedicationID=m.MedicationID) ORDER BY m.MedicationID;
```

**Check and explain:** Medication 5 only.
