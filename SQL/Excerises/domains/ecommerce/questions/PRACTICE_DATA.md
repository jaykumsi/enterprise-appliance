# E-commerce: large practice data

1. Select a new practice database in SQL Server Management Studio.
2. For CREATE practice, complete the Create section of DDL.md first. Leave the tables empty.
3. Ask your instructor to load the large dataset. The setup can also create any missing tables.
4. Check the row counts below, then practice SELECT, joins, GROUP BY, date functions and parent-child queries.

The setup stops if any domain table already contains rows. To repeat the lesson, use another empty practice database. Ask the instructor to reload after exercises that change data or tables.

| Table | Role | Rows |
|---|---|---:|
| Customers | Master | 2000 |
| Sellers | Master | 80 |
| Products | Master | 400 |
| Orders | Transaction / detail | 31973 |
| OrderItems | Transaction / detail | 58025 |
| Payments | Transaction / detail | 32171 |

Fictional, realistic business records with varied dates, quantities, prices and activity. Contact emails use example.com. Timestamps are UTC. Amounts are illustrative training values, not market quotes or clinical guidance.

SalesChannel A=mobile app, B=website, C=voice assistant. About 32,000 orders in 2024 with evening and weekend peaks, a Bazaar Days sale on 16-17 July and a holiday rush. Closed orders are delivered and paid, Open orders are in progress (cash-on-delivery ones are unpaid until delivery), Pending orders await payment. OrderTotal equals the sum of its items.

This is an additional practice dataset. The small sample rows and fixed expected results in existing assignments still refer to the original dataset; totals and row counts will differ here.
