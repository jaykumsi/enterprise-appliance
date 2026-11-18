# SUBQUERIES

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied answer key

Historical references require instructor review on the large fixture. These are not newly validated levelled references. [Selection audit](EXERCISE_SELECTION.md).

##### SUBQUERIES-I07: ANY / ALL

[Question](../questions/SUBQUERIES.md)

```sql
SELECT MedicationName, UnitCost
FROM healthcare.Medications
WHERE UnitCost > ALL (SELECT UnitCost
                      FROM healthcare.Medications
                      WHERE MedicationName LIKE 'Ibuprofen%')
ORDER BY UnitCost;
```

**How it works:** `> ALL` means greater than every value in the list, the same as greater than the MAX. `> ANY` means greater than at least one, the same as greater than the MIN.

**Expected result:** 28 rows, first 6 shown

| MedicationName | UnitCost |
|---|---|
| Melatonin 3mg tablet | 0.14 |
| Sertraline 25mg tablet | 0.14 |
| Atorvastatin 10mg tablet | 0.15 |
| Losartan 50mg tablet | 0.16 |
| Loratadine 5mg tablet | 0.16 |
| Escitalopram 5mg tablet | 0.16 |

##### SUBQUERIES-A01: NOT IN and the NULL trap

[Question](../questions/SUBQUERIES.md)

```sql
SELECT
  (SELECT COUNT(*) FROM healthcare.Encounters AS e
   WHERE e.EncounterID NOT IN (SELECT ParentEncounterID
                               FROM healthcare.Encounters)) AS NotIn_Wrong,
  (SELECT COUNT(*) FROM healthcare.Encounters AS e
   WHERE NOT EXISTS (SELECT 1 FROM healthcare.Encounters AS c
                     WHERE c.ParentEncounterID = e.EncounterID)) AS NotExists_Right;
```

**How it works:** ParentEncounterID contains NULLs. `x NOT IN (..., NULL)` is never true, so NOT IN returns 0. NOT EXISTS ignores the NULLs and returns the correct count. You can also fix NOT IN by adding `WHERE ParentEncounterID IS NOT NULL` inside the subquery.

**Expected result:** 1 row

| NotIn_Wrong | NotExists_Right |
|---|---|
| 0 | 95 |

##### SUBQUERIES-A03: Repeated prescribing without deleting history

[Question](../questions/SUBQUERIES.md)

```sql
SELECT p.PatientID, p.PatientName
FROM healthcare.Patients AS p
WHERE EXISTS (SELECT 1
                  FROM healthcare.Encounters AS e
                  JOIN healthcare.Prescriptions AS rx ON rx.EncounterID = e.EncounterID
                  WHERE e.PatientID = p.PatientID
                  GROUP BY rx.MedicationID
                  HAVING COUNT(*) > 1)
ORDER BY p.PatientID;
```

**How it works:** Inside EXISTS, the patient's prescriptions are grouped by medication and HAVING keeps groups with more than one row. If any such group exists, the patient has repeated prescribing for that medication; this alone does not establish a refill or a duplicate record. Swap to NOT EXISTS to find patients with no refills.

**Expected result:** 76 rows, first 6 shown

| PatientID | PatientName |
|---|---|
| 1 | Olivia Bennett |
| 2 | Liam Shah |
| 3 | Emma Hughes |
| 4 | Noah Turner |
| 6 | Elijah Carter |
| 7 | Sophia Parker |
