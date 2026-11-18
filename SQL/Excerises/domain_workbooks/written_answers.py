"""Hand-written questions and model answers for the design questions whose AmeriMed wording does not translate.

Q[domain][id]   replaces the question text on the student and instructor pages.
A[domain][id]   is the model answer in the instructor solution guide.
"""

Q = {
    'banking': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a banking example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Harborstone wants to store scheduled payments (standing orders) that '
                            'create transactions when they run. How would you model it?',
    },
    'brokerage': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a brokerage example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Ridgeline wants to store recurring investment plans that create trade '
                            'orders on a schedule. How would you model it?',
    },
    'oil': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give an energy shipping example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Permian Ridge wants to store booked pickup slots that become shipments. '
                            'How would you model it?',
    },
    'pharma': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a pharmaceutical example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Novacrest wants to store planned production runs that become batches. '
                            'How would you model it?',
    },
    'retail': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a retail example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Maple & Main wants to store subscriptions (repeat orders on a schedule) '
                            'that become orders. How would you model it?',
    },
    'retail_inventory': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a warehouse stock example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Maple & Main Merchandising wants to store expected deliveries from '
                            'suppliers that become stock movements when they arrive. How would you model it?',
    },
    'retail_logistics': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a delivery network example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Maple & Main Distribution wants to store booked pickups that become '
                            'shipments. How would you model it?',
    },
    'retail_manufacturing': {
        'INTRODUCTION-I03': 'What does ACID stand for? Give a factory example for each letter.',
        'INTRODUCTION-A10': 'Interview design question: Maple & Main Private Label wants to store a production schedule whose '
                            'slots become production orders. How would you model it?',
    },
}

_DUR = ('Durability: once committed, the data survives a crash or power loss (SQL Server writes it to the transaction log first).')
_ISO = 'Isolation: two sessions working at the same time do not see each other\'s half-finished changes'

A = {
    'banking': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Harborstone, Customers, Branches and Accounts are separate tables; each account stores the '
                            'CustomerID and BranchID it belongs to, and each row in Transactions stores its AccountID. SQL is the '
                            'language used to define, read and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per transaction, not '
                            '"T1, T2, T3" in one cell of Accounts). 2NF: in a table with a composite key every column depends on '
                            'the whole key (if a table were keyed by AccountID + CustomerID, the customer\'s name would depend on '
                            'only part of it, so it belongs in Customers). 3NF: no column depends on another non-key column (the '
                            'branch city depends on BranchID, so it lives in Branches, not repeated on every account).',
        'INTRODUCTION-I03': 'Atomicity: a transfer debits one account and credits another, and either both rows are saved or '
                            'neither is. Consistency: constraints always hold (no transaction for an AccountID that does not '
                            f'exist). {_ISO} (a balance report never sees only the debit half of a transfer). {_DUR}',
        'INTRODUCTION-A10': 'Create StandingOrders (StandingOrderID PK, AccountID FK, Amount decimal(12,2) CHECK (Amount > 0), '
                            'Frequency CHECK IN (\'Weekly\',\'Monthly\',\'Yearly\'), NextRunDate date, EndDate date NULL, Status CHECK '
                            'IN (\'Active\',\'Paused\',\'Cancelled\'), CreatedAt DEFAULT SYSDATETIME()). Add a nullable StandingOrderID FK '
                            'on Transactions so every transaction a schedule creates points back to it. Index (Status, NextRunDate) '
                            'so the nightly job finds what is due, and add a unique index on (StandingOrderID, TransactionDate) so '
                            'one run cannot post twice.',
    },
    'brokerage': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Ridgeline, Clients, Securities and BrokerageAccounts are separate tables; each trade order '
                            'stores its AccountID and SecurityID, and each execution stores the OrderID it filled. SQL is the '
                            'language used to define, read and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per execution, not a '
                            'list of fills in one cell of TradeOrders). 2NF: in a table with a composite key every column depends on '
                            'the whole key (in a table keyed by OrderID + SecurityID, the security\'s Symbol depends only on '
                            'SecurityID, so it belongs in Securities). 3NF: no column depends on another non-key column (the client\'s '
                            'name depends on ClientID, so it lives in Clients, not repeated on every account or order).',
        'INTRODUCTION-I03': 'Atomicity: an execution row and the update to its order\'s status are saved together or not at all. '
                            'Consistency: constraints always hold (no execution for an OrderID that does not exist, Side is only Buy '
                            f'or Sell). {_ISO} (a position report never sees a fill without its order update). {_DUR}',
        'INTRODUCTION-A10': 'Create InvestmentPlans (PlanID PK, AccountID FK, SecurityID FK, Amount decimal(14,2) CHECK (Amount > 0), '
                            'Frequency CHECK IN (\'Weekly\',\'Monthly\'), NextRunDate date, Status CHECK IN (\'Active\',\'Paused\','
                            '\'Cancelled\'), CreatedAt DEFAULT SYSDATETIME()). Add a nullable PlanID FK on TradeOrders so each order '
                            'a plan creates points back to it. Index (Status, NextRunDate) for the job that places due orders, and '
                            'a unique index on (PlanID, OrderDate) so a plan cannot place two orders for the same run.',
    },
    'oil': {
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per shipment item, not '
                            '"Crude, Diesel" in one cell of Shipments). 2NF: in a table with a composite key every column depends on '
                            'the whole key (in ShipmentItems keyed by ShipmentID + ProductID, the product name depends only on '
                            'ProductID, so it belongs in Products). 3NF: no column depends on another non-key column (the site\'s '
                            'region depends on SiteID, so it lives in Sites, not repeated on every shipment).',
        'INTRODUCTION-I03': 'Atomicity: a shipment and its shipment items are saved together or not at all. Consistency: '
                            f'constraints always hold (no shipment item for a product that does not exist). {_ISO}. {_DUR}',
        'INTRODUCTION-A10': 'Create PickupSlots (SlotID PK, SiteID FK, CarrierID FK, ScheduledAt datetime2, Status CHECK IN '
                            '(\'Booked\',\'Cancelled\',\'Completed\',\'Missed\'), CreatedAt DEFAULT SYSDATETIME()). Add a nullable SlotID '
                            'FK on Shipments (unique when not NULL) so each shipment points to the slot it came from. Add a unique '
                            'index on (CarrierID, ScheduledAt) to stop double booking a carrier, and an index on (SiteID, '
                            'ScheduledAt) for site lookups.',
    },
    'pharma': {
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one inventory row per batch and '
                            'warehouse, not "W1, W2" in one cell of Batches). 2NF: in a table with a composite key every column '
                            'depends on the whole key (in Inventory keyed by BatchID + WarehouseID, the warehouse capacity depends '
                            'only on WarehouseID, so it belongs in Warehouses). 3NF: no column depends on another non-key column '
                            '(the supplier\'s region depends on SupplierID, so it lives in Suppliers, not repeated on every batch).',
        'INTRODUCTION-I03': 'Atomicity: a batch and its inventory rows are saved together or not at all. Consistency: constraints '
                            f'always hold (no inventory row for a warehouse that does not exist). {_ISO}. {_DUR}',
        'INTRODUCTION-A10': 'Create ProductionPlans (PlanID PK, ProductID FK, SupplierID FK, PlannedDate date, PlannedPacks int '
                            'CHECK (PlannedPacks > 0), Status CHECK IN (\'Planned\',\'Cancelled\',\'Produced\'), CreatedAt DEFAULT '
                            'SYSDATETIME()). Add a nullable PlanID FK on Batches (unique when not NULL) so each batch points to the '
                            'plan it fulfilled. Index (Status, PlannedDate) to list upcoming runs and (ProductID, PlannedDate) for '
                            'product lookups.',
    },
    'retail': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Maple & Main, Customers and Products are separate tables; each order stores its CustomerID, '
                            'each order item stores its OrderID and ProductID, and each payment stores its OrderID. SQL is the '
                            'language used to define, read and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per order item, not '
                            '"Mug, Lamp" in one cell of Orders). 2NF: in a table with a composite key every column depends on the '
                            'whole key (in OrderItems keyed by OrderID + ProductID, the product name depends only on ProductID, so it '
                            'belongs in Products). 3NF: no column depends on another non-key column (the customer\'s region depends '
                            'on CustomerID, so it lives in Customers, not repeated on every order).',
        'INTRODUCTION-I03': 'Atomicity: an order, its order items and its payment are saved together or not at all. Consistency: '
                            f'constraints always hold (no order item for a product that does not exist). {_ISO} (two shoppers '
                            f'cannot both buy the last unit of a product). {_DUR}',
        'INTRODUCTION-A10': 'Create Subscriptions (SubscriptionID PK, CustomerID FK, ProductID FK, Quantity int CHECK (Quantity > 0), '
                            'Frequency CHECK IN (\'Weekly\',\'Monthly\'), NextOrderDate date, Status CHECK IN (\'Active\',\'Paused\','
                            '\'Cancelled\'), CreatedAt DEFAULT SYSDATETIME()). Add a nullable SubscriptionID FK on Orders so each order '
                            'a subscription creates points back to it. Index (Status, NextOrderDate) for the job that places due '
                            'orders, and a unique index on (SubscriptionID, OrderDate) so one run cannot create two orders.',
    },
    'retail_inventory': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Maple & Main Merchandising, Warehouses, Products and Suppliers are separate tables; each stock '
                            'movement stores its WarehouseID, ProductID and SupplierID, and StockBalances holds one row per warehouse '
                            'and product. SQL is the language used to define, read and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one stock movement per row, not '
                            'a list of movements in one cell). 2NF: in a table with a composite key every column depends on the whole '
                            'key (in StockBalances keyed by WarehouseID + ProductID, the product\'s UnitCost depends only on ProductID, '
                            'so it belongs in Products). 3NF: no column depends on another non-key column (a supplier\'s LeadTimeDays '
                            'depends on SupplierID, so it lives in Suppliers, not repeated on every movement).',
        'INTRODUCTION-I03': 'Atomicity: a stock movement and the matching change to StockBalances.QuantityOnHand are saved together '
                            'or not at all. Consistency: constraints always hold (no movement for a warehouse that does not exist). '
                            f'{_ISO} (two pickers cannot both take the last unit). {_DUR}',
        'INTRODUCTION-A10': 'Create ExpectedDeliveries (DeliveryID PK, SupplierID FK, WarehouseID FK, ProductID FK, ExpectedDate '
                            'date, ExpectedUnits int CHECK (ExpectedUnits > 0), Status CHECK IN (\'Expected\',\'Received\',\'Cancelled\'), '
                            'CreatedAt DEFAULT SYSDATETIME()). Add a nullable DeliveryID FK on StockMovements so the IN movement '
                            'created on arrival points to the delivery it fulfilled. Index (Status, ExpectedDate) for the receiving '
                            'dock\'s daily list and (WarehouseID, ProductID) for stock planning.',
    },
    'retail_logistics': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Maple & Main Distribution, Customers and Carriers are separate tables; each shipment stores '
                            'its CustomerID and CarrierID, each package stores its ShipmentID, and each tracking event stores its '
                            'PackageID. SQL is the language used to define, read and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per package, not a list '
                            'of tracking numbers in one cell of Shipments). 2NF: in a table with a composite key every column depends '
                            'on the whole key (in a table keyed by ShipmentID + CarrierID, the carrier\'s ServiceLevel depends only on '
                            'CarrierID, so it belongs in Carriers). 3NF: no column depends on another non-key column (the customer\'s '
                            'region depends on CustomerID, so it lives in Customers, not repeated on every shipment).',
        'INTRODUCTION-I03': 'Atomicity: a shipment and its packages are saved together or not at all. Consistency: constraints '
                            f'always hold (no tracking event for a package that does not exist). {_ISO}. {_DUR}',
        'INTRODUCTION-A10': 'Create Pickups (PickupID PK, CustomerID FK, CarrierID FK, ScheduledAt datetime2, Status CHECK IN '
                            '(\'Booked\',\'Cancelled\',\'Collected\',\'Missed\'), CreatedAt DEFAULT SYSDATETIME()). Add a nullable PickupID '
                            'FK on Shipments (unique when not NULL) so each shipment points to the pickup it came from. Add a unique '
                            'index on (CarrierID, ScheduledAt) to stop double booking, and an index on (CustomerID, ScheduledAt) '
                            'for customer lookups.',
    },
    'retail_manufacturing': {
        'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key '
                            'values. At Maple & Main Private Label, Products and Materials are separate tables; BillOfMaterials links '
                            'them (which materials go into each product), each production order stores its ProductID, and each '
                            'MaterialUsage row stores its ProductionOrderID and MaterialID. SQL is the language used to define, read '
                            'and change that data.',
        'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one BillOfMaterials row per '
                            'product and material, not "Flour, Sugar" in one cell of Products). 2NF: in a table with a composite key '
                            'every column depends on the whole key (in BillOfMaterials keyed by ProductID + MaterialID, the material\'s '
                            'UnitCost depends only on MaterialID, so it belongs in Materials). 3NF: no column depends on another '
                            'non-key column (the product\'s region depends on ProductID, so it lives in Products, not repeated on '
                            'every production order).',
        'INTRODUCTION-I03': 'Atomicity: a production order and its MaterialUsage rows are saved together or not at all. '
                            f'Consistency: constraints always hold (no usage row for a material that does not exist). {_ISO}. {_DUR}',
        'INTRODUCTION-A10': 'Create ProductionSchedule (SlotID PK, ProductID FK, PlannedDate date, PlannedUnits int CHECK '
                            '(PlannedUnits > 0), Line varchar(20), Status CHECK IN (\'Planned\',\'Cancelled\',\'Produced\'), CreatedAt '
                            'DEFAULT SYSDATETIME()). Add a nullable SlotID FK on ProductionOrders (unique when not NULL) so each order '
                            'points to the slot it fulfilled. Add a unique index on (Line, PlannedDate) so a line is not booked twice, '
                            'and an index on (ProductID, PlannedDate) for product lookups.',
    },
}

# ---- workbook-only domains (extra_domains.py) ----
Q['retail_supply_chain'] = {
    'INTRODUCTION-I03': 'What does ACID stand for? Give a supply chain example for each letter.',
    'INTRODUCTION-A10': 'Interview design question: Maple & Main Supply Chain wants to store expected deliveries from suppliers '
                        'that become stock movements when they arrive. How would you model it?',
}
Q['ecommerce'] = {
    'INTRODUCTION-I03': 'What does ACID stand for? Give an online marketplace example for each letter.',
    'INTRODUCTION-A10': 'Interview design question: Everyday Bazaar wants to store shopping carts that become orders at checkout. '
                        'How would you model it?',
}
A['retail_supply_chain'] = {
    'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key values. '
                        'At Maple & Main Supply Chain, Warehouses, Suppliers, Products and Materials are separate tables; each stock '
                        'movement stores its WarehouseID, ProductID and SupplierID, each production order stores its ProductID and '
                        'WarehouseID, and BillOfMaterials links products to materials. SQL is the language used to define, read and '
                        'change that data.',
    'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one recipe line per row in '
                        'BillOfMaterials, not "fabric, thread, zipper" in one cell of Products). 2NF: in a table with a composite key '
                        'every column depends on the whole key (in BillOfMaterials keyed by ProductID + MaterialID, the material\'s '
                        'UnitCost depends only on MaterialID, so it belongs in Materials). 3NF: no column depends on another non-key '
                        'column (a supplier\'s LeadTimeDays depends on SupplierID, so it lives in Suppliers, not on every movement).',
    'INTRODUCTION-I03': 'Atomicity: completing a production order, its MaterialUsage rows and the IN stock movement for the '
                        'finished units are saved together or not at all. Consistency: constraints always hold (no movement for a '
                        f'product that does not exist). {_ISO} (two pickers cannot both take the last unit). {_DUR}',
    'INTRODUCTION-A10': A['retail_inventory']['INTRODUCTION-A10'],
}
A['ecommerce'] = {
    'INTRODUCTION-B01': 'A relational database stores data in tables (rows and columns) and links them through shared key values. '
                        'At Everyday Bazaar, Customers, Sellers and Products are separate tables; each order stores its CustomerID '
                        'and SellerID, each order item stores its OrderID and ProductID, and each payment stores its OrderID. SQL is '
                        'the language used to define, read and change that data.',
    'INTRODUCTION-I01': '1NF: every column holds one value and there are no repeating groups (one row per order item, not '
                        '"Earbuds, Charger" in one cell of Orders). 2NF: in a table with a composite key every column depends on the '
                        'whole key (in OrderItems keyed by OrderID + ProductID, the product name depends only on ProductID, so it '
                        'belongs in Products). 3NF: no column depends on another non-key column (a seller\'s Department depends on '
                        'SellerID, so it lives in Sellers, not repeated on every order).',
    'INTRODUCTION-I03': 'Atomicity: an order, its order items and its payment are saved together or not at all, even with '
                        'hundreds of checkouts a minute. Consistency: constraints always hold (no order item for a product that does '
                        f'not exist). {_ISO} (two shoppers in a flash sale cannot both buy the last unit). {_DUR}',
    'INTRODUCTION-A10': 'Create Carts (CartID PK, CustomerID FK, CreatedAt DEFAULT SYSDATETIME(), Status CHECK IN (\'Open\','
                        '\'CheckedOut\',\'Abandoned\')) and CartItems (CartID FK, ProductID FK, Quantity CHECK (Quantity > 0), AddedAt, '
                        'PRIMARY KEY (CartID, ProductID)). Add a nullable CartID FK on Orders (unique when not NULL) so the order '
                        'created at checkout points to its cart. Index Carts (Status, CreatedAt) for the abandoned-cart job and '
                        'Carts (CustomerID) to find a shopper\'s open cart quickly.',
}
