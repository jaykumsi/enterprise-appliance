# E-commerce: reporting assignments

Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](DOMAIN_GUIDE.md). [Help with SQL terms](../../../BEGINNER_GUIDE.md).

## ECOMMERCE-REPORT-01: Master activity

Return each Customers ID and name, including masters with no Orders, with the count of related events and total known OrderTotal. Order by master ID.

## ECOMMERCE-REPORT-02: No activity

Return Customers with no related Orders using NOT EXISTS.

## ECOMMERCE-REPORT-03: Highest value per master

Use ROW_NUMBER to select the highest OrderTotal event for each active master. Break ties by OrderID ascending.

## ECOMMERCE-REPORT-04: Order detail

Show order ID, customer name, seller name, product name, quantity, charged unit price and line total for every order line.

## ECOMMERCE-REPORT-05: Settlement check

For all orders, return OrderID, OrderTotal, line total, paid total and outstanding amount. An order can be split between a gift card and a card, so aggregate lines and payments separately before joining. Preserve unknown OrderTotal; missing lines/payments count as zero.

## ECOMMERCE-REPORT-06: Seller activity

Return every seller with its department, order count, known order revenue and distinct customers, including sellers with no orders (zero counts, zero revenue).
