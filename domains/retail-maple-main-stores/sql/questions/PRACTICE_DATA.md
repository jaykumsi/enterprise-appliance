# Retail: large practice data

1. Select a new practice database in SQL Server Management Studio.
2. For CREATE practice, complete the Create section of DDL.md first. Leave the tables empty.
3. Ask your instructor to load the large dataset. The setup can also create any missing tables.
4. Check the row counts below, then practice SELECT, joins, GROUP BY, date functions and parent-child queries.

The setup stops if any domain table already contains rows. To repeat the lesson, use another empty practice database. Ask the instructor to reload after exercises that change data or tables.

| Table | Role | Rows |
|---|---|---:|
| Customers | Master | 100 |
| Products | Master | 100 |
| Orders | Transaction / detail | 240 |
| OrderItems | Transaction / detail | 524 |
| Payments | Transaction / detail | 260 |

Fictional, realistic business records with varied dates, quantities, prices and activity. Contact emails use example.com. Timestamps are UTC. Amounts are illustrative training values, not market quotes or clinical guidance.

SalesChannel A=web, B=store, C=phone. Totals equal line values before tax/shipping; Closed orders are fully paid, Open partially paid, Pending unpaid.

This is an additional practice dataset. The small sample rows and fixed expected results in existing assignments still refer to the original dataset; totals and row counts will differ here.
