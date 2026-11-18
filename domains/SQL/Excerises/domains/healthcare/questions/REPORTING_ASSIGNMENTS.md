# Healthcare: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## HEALTHCARE-REPORT-01: Master activity

Return each Patients ID and name, including masters with no Encounters, with the count of related events and total known Charge. Order by master ID.

## HEALTHCARE-REPORT-02: No activity

Return Patients with no related Encounters using NOT EXISTS.

## HEALTHCARE-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest Charge event for each active master. Break ties by EncounterID ascending.

## HEALTHCARE-REPORT-04: Prescription trace

Show prescription reference, patient name, doctor name, encounter ID, medication name and prescribed quantity by joining all five tables.

## HEALTHCARE-REPORT-05: Encounter billing

Return every encounter, patient name, charge and prescription count. Count prescriptions before joining, so charges appear only once per encounter.

## HEALTHCARE-REPORT-06: Unprescribed medications

Find medication IDs and names never referenced by a prescription.
