# SUBQUERIES

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied practice

Selected cases supplement the assessed levelled bank. B/I/A in these older IDs are historical labels, not current difficulty ratings. [Practice route](BEST_EXERCISES.md). Historical self-checks use the large fixture and are outside the native report-validation claim. Use a fresh large-fixture practice copy for each case that changes data or permissions; changes persist.

<a id="legacy-subqueries-i07"></a>

##### SUBQUERIES-I07: ANY / ALL

List medications that cost more than ALL Ibuprofen medications.

**Expected result:** 28 rows, first 6 shown

| MedicationName | UnitCost |
|---|---|
| Melatonin 3mg tablet | 0.14 |
| Sertraline 25mg tablet | 0.14 |
| Atorvastatin 10mg tablet | 0.15 |
| Losartan 50mg tablet | 0.16 |
| Loratadine 5mg tablet | 0.16 |
| Escitalopram 5mg tablet | 0.16 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-subqueries-a01"></a>

##### SUBQUERIES-A01: NOT IN and the NULL trap

Interview trap: show why NOT IN fails when the list contains NULL. Find encounters that are not a parent of any other encounter, first with NOT IN (wrong), then with NOT EXISTS (right).

**Expected result:** 1 row

| NotIn_Wrong | NotExists_Right |
|---|---|
| 0 | 95 |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._

<a id="legacy-subqueries-a03"></a>

##### SUBQUERIES-A03: Repeated prescribing without deleting history

Return PatientID and PatientName for patients with more than one prescription row for the same MedicationID across their encounters. Use EXISTS and return each patient once, ordered by PatientID. Repeated prescribing may include refills; do not infer clinical duplication or delete prescriptions. Source columns: Patients.PatientID, Patients.PatientName, Encounters.PatientID, Encounters.EncounterID, Prescriptions.EncounterID, Prescriptions.MedicationID.

**Expected result:** 76 rows, first 6 shown

| PatientID | PatientName |
|---|---|
| 1 | Olivia Bennett |
| 2 | Liam Shah |
| 3 | Emma Hughes |
| 4 | Noah Turner |
| 6 | Elijah Carter |
| 7 | Sophia Parker |


_Your query may be written differently and still be correct. Compare the number of rows and the values; if the question has no ORDER BY, your rows may come back in a different order._
