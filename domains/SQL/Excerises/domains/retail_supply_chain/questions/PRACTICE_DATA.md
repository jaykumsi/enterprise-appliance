# Retail Supply Chain: large practice data

1. Select a new practice database in SQL Server Management Studio.
2. For CREATE practice, complete the Create section of DDL.md first. Leave the tables empty.
3. Ask your instructor to load the large dataset. The setup can also create any missing tables.
4. Check the row counts below, then practice SELECT, joins, GROUP BY, date functions and parent-child queries.

The setup stops if any domain table already contains rows. To repeat the lesson, use another empty practice database. Ask the instructor to reload after exercises that change data or tables.

| Table | Role | Rows |
|---|---|---:|
| Warehouses | Master | 50 |
| Suppliers | Master | 50 |
| Products | Master | 100 |
| Materials | Master | 60 |
| BillOfMaterials | Transaction / detail | 200 |
| ProductionOrders | Transaction / detail | 120 |
| MaterialUsage | Transaction / detail | 440 |
| StockMovements | Transaction / detail | 240 |
| StockBalances | Transaction / detail | 100 |

Fictional, realistic business records with varied dates, quantities, prices and activity. Contact emails use example.com. Timestamps are UTC. Amounts are illustrative training values, not market quotes or clinical guidance.

MovementCategory A=receipt, B=dispatch, C=return. Only Closed movements affect balances. Products 1-50 are Bought; 51-100 are Made in the Private Label plant (SupplierID 50) from BillOfMaterials recipes, and their receipts link to the production order. PlannedCost is recipe material cost; actual usage includes small waste variances.

This is an additional practice dataset. The small sample rows and fixed expected results in existing assignments still refer to the original dataset; totals and row counts will differ here.
