# Retail: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../SQL/Excerises/BEGINNER_GUIDE.md).

## RETAIL-REPORT-01: Master activity

Return each Customers ID and name, including masters with no Orders, with the count of related events and total known OrderTotal. Order by master ID.

## RETAIL-REPORT-02: No activity

Return Customers with no related Orders using NOT EXISTS.

## RETAIL-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest OrderTotal event for each active master. Break ties by OrderID ascending.

## RETAIL-REPORT-04: Order detail

Show order ID, customer name, product name, quantity, historical line price and line total for every order line.

## RETAIL-REPORT-05: Payment reconciliation

For all orders, return OrderID, OrderTotal, line total, paid total and outstanding amount. Aggregate lines and payments separately before joining. Preserve unknown OrderTotal; missing lines/payments count as zero.

## RETAIL-REPORT-06: Unused products

Return product ID and name for products never used on an order line.
