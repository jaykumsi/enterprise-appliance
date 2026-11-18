# Preserved setup and capstone notes

Unique notes from the consolidated domain copies. File names refer to the selected domain.

**Domains:** banking, brokerage, ecommerce, healthcare, oil, pharma, retail, retail_logistics, retail_supply_chain

Use schema_solution.sql as the structural reference and seed.sql as the data reference. Inspect sys.key_constraints, sys.foreign_keys and sys.check_constraints; foreign keys/checks must be enabled and trusted. A correct PK/FK design should reject each invalid case with the expected SQL Server error (515 for NOT NULL, 2627 for PK/UNIQUE, 547 for CHECK/FK).

For the parent-deletion test, choose a master with existing events (ID 1), attempt its deletion in a transaction, catch 547 and roll back. For the new-record scenario, require valid parent IDs and unique business identifiers. Verify the expected increase in counts/totals, then roll back and rerun baseline checks.

Pass only when all structural and integrity checks pass and all six reports reconcile. Grade explanations and independent correction of a faulty many-to-many join, not memorized syntax alone.
