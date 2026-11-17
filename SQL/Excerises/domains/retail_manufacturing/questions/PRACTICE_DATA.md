# Retail Manufacturing: large practice data

1. Select a new practice database in SQL Server Management Studio.
2. For CREATE practice, complete the Create section of DDL.md first. Leave the tables empty.
3. Ask your instructor to load the large dataset. The setup can also create any missing tables.
4. Check the row counts below, then practice SELECT, joins, GROUP BY, date functions and parent-child queries.

The setup stops if any domain table already contains rows. To repeat the lesson, use another empty practice database. Ask the instructor to reload after exercises that change data or tables.

| Table | Role | Rows |
|---|---|---:|
| Products | Master | 50 |
| Materials | Master | 60 |
| ProductionOrders | Transaction / detail | 240 |
| BillOfMaterials | Transaction / detail | 200 |
| MaterialUsage | Transaction / detail | 912 |

Fictional, realistic business records with varied dates, quantities, prices and activity. Contact emails use example.com. Timestamps are UTC. Amounts are illustrative training values, not market quotes or clinical guidance.

ProductionCategory A=standard run, B=replenishment, C=small run. Materials use meters for fabric/thread and pieces for zippers. Planned cost is BOM material cost; actual usage includes small waste variances.

This is an additional practice dataset. The small sample rows and fixed expected results in existing assignments still refer to the original dataset; totals and row counts will differ here.
