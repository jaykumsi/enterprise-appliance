# Brokerage: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## BROKERAGE-REPORT-01: Master activity

Return each BrokerageAccounts ID and name, including masters with no TradeOrders, with the count of related events and total known EstimatedValue. Order by master ID.

## BROKERAGE-REPORT-02: No activity

Return BrokerageAccounts with no related TradeOrders using NOT EXISTS.

## BROKERAGE-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest EstimatedValue event for each active master. Break ties by OrderID ascending.

## BROKERAGE-REPORT-04: Client-to-execution audit

Join all five tables to show execution reference, client name, account number, security symbol, order ID, executed quantity, price and gross executed value.

## BROKERAGE-REPORT-05: Fill reconciliation

For all orders, return requested, filled and remaining quantities, gross executed value and quantity-weighted average execution price. Use zero filled/gross for unfilled orders, but NULL average. Identify any overfills.

## BROKERAGE-REPORT-06: Client execution totals

Return all clients with gross executed value and number of fills through their accounts, including clients without executions. Avoid multiplying order estimates by fill counts.
