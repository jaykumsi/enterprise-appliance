# Banking / Finance: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## BANKING-REPORT-01: Master activity

Return each Accounts ID and name, including masters with no Transactions, with the count of related events and total known Amount. Order by master ID.

## BANKING-REPORT-02: No activity

Return Accounts with no related Transactions using NOT EXISTS.

## BANKING-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest Amount event for each active master. Break ties by TransactionID ascending.

## BANKING-REPORT-04: Transaction trace

Show every transaction ID, account name, customer name, branch name and amount.

## BANKING-REPORT-05: Customer exposure

Return each customer with transaction amount total through their accounts and principal total through their loans. Aggregate the two measures independently; use zero for no activity.

## BANKING-REPORT-06: Branch activity

Show all branches and their account counts, including branches without activity; count accounts rather than transactions.
