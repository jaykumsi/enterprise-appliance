# Start here: simple SQL practice instructions

Choose one business area, such as Retail. You will create five related tables, add sample rows, and use those same tables for the exercises. You do not need to build all nine business areas before starting.

## What do I need before an exercise?

1. Ask your instructor to help you open your practice database.
2. Follow your domain guide to create its five tables in the order shown.
3. Add the sample rows from that guide. Your instructor may use `seed.sql` to add these rows for you. Do not add them a second time.
4. Start the assignments for that domain.

“Sample data” means the example rows supplied with the course. For example, the Retail Customers table contains a row with CustomerID 1 and CustomerName `Customers Alpha`. When an exercise says “use your earlier sample rows,” it means these rows.

## How do I read a table name?

`[retail].[Customers]` means the Customers table in the retail group of tables. This group is called a **schema**. The square brackets mark SQL names.

`CustomerID = 1` means “find the row whose CustomerID is 1.”

`CustomerName` is a column in that row. A column holds one kind of information, such as a name or a date.

## Words you will see

| SQL word | Simple meaning |
|---|---|
| Row | One record, such as one customer |
| Column | One piece of information, such as CustomerName |
| NULL | No value is stored; it is different from zero or an empty text value |
| NOT NULL | This column must have a value |
| Primary key | A value, or combination of values, that identifies one row and cannot be repeated |
| Foreign key | A link to a row in another table, or sometimes the same table |
| UNIQUE | The listed column values must not be repeated; SQL Server also has special rules for NULL values |
| CHECK | A rule that limits allowed values, such as Quantity greater than zero |
| DEFAULT | A value used when an insert leaves that column out |
| Constraint | A rule on a table, such as NOT NULL, UNIQUE, CHECK or a key |
| SELECT | Read and display data |
| INSERT | Add a row |
| UPDATE | Change values in existing rows |
| DELETE | Remove rows |
| ALTER TABLE | Change a table's columns or rules |
| DROP TABLE | Remove the whole table, including its rows |

## Practicing changes

Use a practice database. Changes are kept when you run INSERT, UPDATE, DELETE, ALTER TABLE or DROP TABLE.

Keep your initial tables and sample rows for later exercises. Ask your instructor to reset the practice tables before each exercise that changes them. Use a separate practice copy for DROP TABLE.

## Is an error always bad?

No. Some exercises ask you to try a value that breaks a table rule. SQL Server should show an error and refuse the change. This is how you check that the rule works.

For example, trying to put NULL into a NOT NULL column should fail. Save the error message, then display the row again to check that its original value is still there. If your SQL tool stops after the error, ask your instructor how to run the remaining statements. The separate answer uses TRY/CATCH to handle the expected error.

## Example: a customer must have a name

Use the Customers table and sample rows you created earlier.

1. Find the customer whose CustomerID is 1. Note the current CustomerName.
2. Try to change that customer's CustomerName to `NULL`.
3. Read and save the error message. SQL Server should refuse the change because CustomerName is NOT NULL.
4. Display the customer again. Check that the original name is still there.

Explain in one sentence why every customer needs a name. Submit your SQL, the error message, and the customer row shown before and after the attempt.
