"""Large practice data for the Retail Supply Chain and E-commerce domains (deterministic, fictional).

realistic_data.build calls large_rows(slug); each generator returns {table name: [row dicts]} that match the
domain model in domain_projects.py. Everyday Bazaar (E-commerce) has about 32,000 orders in 2024 with daily and
seasonal peaks; Maple & Main Supply Chain combines bought and private label (made) products.
"""
from datetime import datetime, timedelta
from random import Random

from realistic_data import BRANDS, CITIES, COLORS, GOODS, REGIONS, stamp

EVENT_PURPOSE = ''
def col(name, typ, rule='NOT NULL'):
    return dict(name=name, type=typ, rule=rule, sample=None)


def table(name, key, columns, unique=(), checks=(), fks=(), purpose=''):
    return dict(name=name, key=key, columns=[col(*c) for c in columns], unique=list(unique), checks=list(checks),
                fks=[dict(column=c, parent=p, key=k) for c, p, k in fks], purpose=purpose, rows=[])


def event_columns(id_, party, label, cat, status, amt, qty, date, time, parent):
    return [(id_, 'int'), (party, 'int'), (label, 'nvarchar(80)'), (cat, 'varchar(10)'),
            (status, 'varchar(10)', "NOT NULL DEFAULT ('Open')"), (amt, 'decimal(12,2)', 'NULL'), (qty, 'int'),
            (date, 'date'), (time, 'datetime2(3)'), ('RecordedAt', 'datetimeoffset(3)'), ('Note', 'nvarchar(100)', 'NULL'),
            ('BackupNote', 'nvarchar(100)', 'NULL'), (parent, 'int', 'NULL')]


def event_checks(id_, label, cat, status, amt, qty, parent):
    return [f"{cat} IN ('A','B','C')", f"{status} IN ('Open','Closed','Pending')", f'{amt} >= 0', f'{qty} > 0',
            f'{parent} IS NULL OR {parent} <> {id_}', f'LEN(LTRIM(RTRIM({label}))) > 0']


def money(v):
    return round(v + 1e-8, 2)


def location(i):
    return CITIES[(i - 1) % 25], REGIONS[(i - 1) % 25]


# ---------------------------------------------------------------------------------------------------------------
# Maple & Main Supply Chain
# ---------------------------------------------------------------------------------------------------------------
def supply_chain():
    slug = 'retail_supply_chain'
    rng = Random(20241118)
    E = ['MovementID', 'WarehouseID', 'MovementReference', 'MovementCategory', 'Status', 'MovementValue', 'MovedUnits',
         'MovementDate', 'MovedAt', 'ParentMovementID']
    T = [
        table('Warehouses', 'WarehouseID', [('WarehouseID', 'int'), ('WarehouseName', 'nvarchar(80)'), ('WarehouseCode', 'varchar(20)'),
                                            ('Region', 'varchar(10)')],
              ['WarehouseCode'], ['LEN(LTRIM(RTRIM(WarehouseName))) > 0'],
              purpose='Fulfillment centers and store depots; each has stock movements, stock balances and receives factory output.'),
        table('Suppliers', 'SupplierID', [('SupplierID', 'int'), ('SupplierName', 'nvarchar(80)'), ('SupplierCode', 'varchar(20)'),
                                          ('LeadTimeDays', 'int')],
              ['SupplierCode'], ['LeadTimeDays >= 0', 'LEN(LTRIM(RTRIM(SupplierName))) > 0'],
              purpose='Where stock comes from. SupplierID 50 is the in-house Private Label plant, the source of every Made product.'),
        table('Products', 'ProductID', [('ProductID', 'int'), ('ProductName', 'nvarchar(80)'), ('SKU', 'varchar(20)'),
                                        ('UnitCost', 'decimal(12,2)'), ('Sourcing', 'varchar(10)', "NOT NULL DEFAULT ('Bought')")],
              ['SKU'], ['UnitCost > 0', "Sourcing IN ('Bought','Made')", 'LEN(LTRIM(RTRIM(ProductName))) > 0'],
              purpose='One catalog: Bought products come from outside suppliers, Made products are produced in the Private Label plant.'),
        table('Materials', 'MaterialID', [('MaterialID', 'int'), ('MaterialName', 'nvarchar(80)'), ('MaterialCode', 'varchar(20)'),
                                          ('UnitCost', 'decimal(12,2)')],
              ['MaterialCode'], ['UnitCost > 0', 'LEN(LTRIM(RTRIM(MaterialName))) > 0'],
              purpose='Raw materials for Made products: fabric and lining in meters, thread in meters, zippers in pieces.'),
        table('BillOfMaterials', 'BOMID', [('BOMID', 'int'), ('ProductID', 'int'), ('MaterialID', 'int'), ('QuantityPerUnit', 'decimal(12,2)')],
              ['ProductID, MaterialID'], ['QuantityPerUnit > 0'],
              [('ProductID', 'Products', 'ProductID'), ('MaterialID', 'Materials', 'MaterialID')],
              purpose='Recipe: one row per Made product and the material it needs, per unit produced.'),
        table('ProductionOrders', 'ProductionOrderID',
              [('ProductionOrderID', 'int'), ('ProductID', 'int'), ('WarehouseID', 'int'), ('ProductionReference', 'varchar(20)'),
               ('ProductionStatus', 'varchar(12)'), ('PlannedUnits', 'int'), ('PlannedCost', 'decimal(12,2)'),
               ('StartDate', 'date'), ('CompletedDate', 'date', 'NULL')],
              ['ProductionReference'],
              ["ProductionStatus IN ('Planned','InProgress','Completed')", 'PlannedUnits > 0', 'PlannedCost >= 0',
               'CompletedDate IS NULL OR CompletedDate >= StartDate'],
              [('ProductID', 'Products', 'ProductID'), ('WarehouseID', 'Warehouses', 'WarehouseID')],
              purpose='Factory runs for Made products. PlannedCost is the recipe material cost; finished units go to WarehouseID.'),
        table('MaterialUsage', 'UsageID', [('UsageID', 'int'), ('ProductionOrderID', 'int'), ('MaterialID', 'int'),
                                           ('QuantityUsed', 'decimal(12,2)'), ('UsageDate', 'date')],
              ['ProductionOrderID, MaterialID'], ['QuantityUsed > 0'],
              [('ProductionOrderID', 'ProductionOrders', 'ProductionOrderID'), ('MaterialID', 'Materials', 'MaterialID')],
              purpose='Actual material consumed per production order and material; compare it with the recipe.'),
        table('StockMovements', 'MovementID',
              [tuple(c) for c in event_columns(*E)] + [('ProductID', 'int'), ('SupplierID', 'int'), ('Direction', 'varchar(3)'),
                                                       ('ProductionOrderID', 'int', 'NULL')],
              ['MovementReference'], event_checks(E[0], E[2], E[3], E[4], E[5], E[6], E[9]) + ["Direction IN ('IN','OUT')"],
              [('WarehouseID', 'Warehouses', 'WarehouseID'), ('ParentMovementID', 'StockMovements', 'MovementID'),
               ('ProductID', 'Products', 'ProductID'), ('SupplierID', 'Suppliers', 'SupplierID'),
               ('ProductionOrderID', 'ProductionOrders', 'ProductionOrderID')],
              purpose=EVENT_PURPOSE + ' Receipts of Made products point to the production order that made them.'),
        table('StockBalances', 'BalanceID', [('BalanceID', 'int'), ('WarehouseID', 'int'), ('ProductID', 'int'),
                                             ('OpeningQuantity', 'int'), ('QuantityOnHand', 'int'), ('ReorderLevel', 'int')],
              ['WarehouseID, ProductID'], ['OpeningQuantity >= 0', 'QuantityOnHand >= 0', 'ReorderLevel >= 0'],
              [('WarehouseID', 'Warehouses', 'WarehouseID'), ('ProductID', 'Products', 'ProductID')],
              purpose='One snapshot per warehouse and product: opening stock plus Closed movements equals QuantityOnHand.'),
    ]
    tb = {t['name']: t for t in T}
    rows = {t['name']: [] for t in T}

    def add(name, **v):
        v[tb[name]['key']] = len(rows[name]) + 1
        rows[name].append(v)
        return v

    for i in range(1, 51):
        add('Warehouses', WarehouseName=f'{location(i)[0]} {"Fulfillment Center" if i <= 25 else "Store Replenishment Depot"}',
            WarehouseCode=f'WH-{i:04}', Region=location(i)[1])
    for i in range(1, 50):
        add('Suppliers', SupplierName=f'{BRANDS[(i - 1) % 25]} {"Home Goods" if i <= 25 else "Retail Supply"}',
            SupplierCode=f'SUP-{i:04}', LeadTimeDays=rng.choice([3, 5, 7, 10, 14, 21]))
    add('Suppliers', SupplierName='Maple & Main Private Label Plant', SupplierCode='SUP-0050', LeadTimeDays=2)

    for kind, cost in [('Cotton Canvas', 7.4), ('Lining Fabric', 3.2), ('Polyester Thread', .08), ('Coil Zipper 30cm', .85)]:
        for color in COLORS:
            for grade in ['Standard', 'Heavy Duty', 'Recycled']:
                add('Materials', MaterialName=f'{color} {kind} - {grade}', MaterialCode=f'MAT-{len(rows["Materials"]) + 1:05}',
                    UnitCost=money(cost * {'Standard': 1, 'Heavy Duty': 1.25, 'Recycled': 1.12}[grade]))
    textiles = ['Canvas Tote', 'Travel Pouch', 'Cushion Cover', 'Laptop Sleeve', 'Laundry Bag', 'Tool Roll', 'Lunch Bag',
                'Garment Bag', 'Toiletry Bag', 'Storage Cube']
    recipes = {}
    for k in range(1, 51):                                   # products 51-100 are Made: recipe first, cost from recipe
        color, grade = (k - 1) % 5, (k - 1) // 5 % 3
        recipes[50 + k] = [(color * 3 + grade + 1, money(.35 + ((k - 1) // 5) * .12)), (15 + color * 3 + grade + 1, .30),
                           (30 + color * 3 + grade + 1, 3.50), (45 + color * 3 + grade + 1, 1)]
    for i in range(1, 101):
        if i <= 50:
            name, price = GOODS[(i - 1) // 5]
            add('Products', ProductName=f'{name} - {COLORS[(i - 1) % 5]}', SKU=f'HOME-{i:05}', UnitCost=money(price * .58), Sourcing='Bought')
        else:
            k = i - 50
            unit = sum(q * rows['Materials'][m - 1]['UnitCost'] for m, q in recipes[i])
            add('Products', ProductName=f'{textiles[(k - 1) // 5]} - {COLORS[(k - 1) % 5]}', SKU=f'PL-{k:05}',
                UnitCost=money(unit * 1.35), Sourcing='Made')
    for p, rec in recipes.items():
        for m, q in rec:
            add('BillOfMaterials', ProductID=p, MaterialID=m, QuantityPerUnit=q)

    def mday(i):
        return datetime(2024, 1, 1) + timedelta(days=(i - 1) * 365 // 239)

    # Production: order k (1-50) is the run behind the first receipt of product 50+k; later runs fill the rest of the year.
    for k in range(1, 121):
        p = 51 + (k - 1) % 50
        units = rng.choice([40, 60, 80, 120, 180, 240])
        if k <= 50:
            done = mday(p) - timedelta(days=rng.randrange(1, 5))
            start = done - timedelta(days=rng.randrange(3, 11))
            status = 'Completed'
        else:
            start = datetime(2024, 5, 1) + timedelta(days=(k - 51) * 230 // 70 + rng.randrange(0, 3))
            status = 'Completed' if k <= 96 else 'InProgress' if k <= 110 else 'Planned'
            done = start + timedelta(days=rng.randrange(4, 12)) if status == 'Completed' else None
        cost = money(sum(q * rows['Materials'][m - 1]['UnitCost'] * units for m, q in recipes[p]))
        add('ProductionOrders', ProductID=p, WarehouseID=(p - 1) % 50 + 1, ProductionReference=f'PO-2024-{k:05}',
            ProductionStatus=status, PlannedUnits=units, PlannedCost=cost, StartDate=start.strftime('%Y%m%d'),
            CompletedDate=done.strftime('%Y%m%d') if done else None)
        if status != 'Planned':
            for m, q in recipes[p]:
                used = q * units * (1 if m > 45 else rng.choice([1, 1, 1.01, 1.02, 1.04, 1.06])) * (1 if status == 'Completed' else .5)
                add('MaterialUsage', ProductionOrderID=k, MaterialID=m, QuantityUsed=money(used),
                    UsageDate=(start + timedelta(days=1)).strftime('%Y%m%d'))

    for i in range(1, 241):
        product = (i - 1) % 100 + 1
        warehouse = (product - 1) % 50 + 1
        made = product > 50
        direction = 'IN' if i <= 100 or i > 200 else 'OUT'
        cat = 'A' if i <= 100 else 'B' if i <= 200 else 'C'
        po = None
        if cat == 'A' and made:
            po = rows['ProductionOrders'][product - 51]
            units = po['PlannedUnits']
            note = 'Private label production receipt'
        else:
            units = rng.randrange(24, 97) if direction == 'IN' else rng.randrange(5, 41)
            note = 'Supplier replenishment' if cat == 'A' else 'Store allocation dispatch' if cat == 'B' else 'Resalable customer returns'
        day = mday(i) + timedelta(hours=rng.randrange(8, 18), minutes=rng.randrange(60), seconds=rng.randrange(60))
        add('StockMovements', WarehouseID=warehouse, MovementReference=f'RSC-{day:%Y%m%d}-{i:05}', MovementCategory=cat,
            Status='Closed' if i <= 204 else 'Open' if i <= 228 else 'Pending',
            MovementValue=money(units * rows['Products'][product - 1]['UnitCost']), MovedUnits=units,
            MovementDate=day.strftime('%Y%m%d'), MovedAt=stamp(day),
            RecordedAt=stamp(day + timedelta(seconds=rng.randrange(2, 91))) + '+00:00', Note=note,
            BackupNote='Reviewed by operations' if i % 17 == 0 else None, ParentMovementID=None,
            ProductID=product, SupplierID=50 if made else (product - 1) % 49 + 1, Direction=direction,
            ProductionOrderID=po['ProductionOrderID'] if po else None)
    for p in range(1, 101):
        opening = rng.randrange(50, 180)
        net = sum(r['MovedUnits'] if r['Direction'] == 'IN' else -r['MovedUnits'] for r in rows['StockMovements']
                  if r['ProductID'] == p and r['Status'] == 'Closed')
        add('StockBalances', WarehouseID=(p - 1) % 50 + 1, ProductID=p, OpeningQuantity=opening, QuantityOnHand=opening + net,
            ReorderLevel=rng.choice([60, 100, 150, 250]))

    # business consistency
    for r in rows['StockMovements']:
        if r['ProductionOrderID']:
            po = rows['ProductionOrders'][r['ProductionOrderID'] - 1]
            assert po['ProductionStatus'] == 'Completed' and po['CompletedDate'] <= r['MovementDate'] and po['ProductID'] == r['ProductID']
    model = dict(slug=slug, title='Retail Supply Chain',
                 map=dict(RecordID=E[0], PartyID=E[1], Label=E[2], Category=E[3], Status=E[4], Amount=E[5], Quantity=E[6],
                          EventDate=E[7], EventTime=E[8], RecordedAt='RecordedAt', Note='Note', BackupNote='BackupNote',
                          ParentID=E[9], PartyName='WarehouseName'),
                 base=['StockMovements', 'Warehouses', 'WarehouseName'],
                 business='Buy or make products, move stock through warehouses, and reconcile production, receipts, dispatches and balances.',
                 masters={'Warehouses', 'Suppliers', 'Products', 'Materials'},
                 notes='MovementCategory A=receipt, B=dispatch, C=return. Only Closed movements affect balances. Products 1-50 are Bought, '
                       '51-100 are Made in the Private Label plant (SupplierID 50); their receipts link to the production order.',
                 tables=T)
    return model, rows


# ---------------------------------------------------------------------------------------------------------------
# Everyday Bazaar (online marketplace, heavy daily volume)
# ---------------------------------------------------------------------------------------------------------------
FIRST = ('Olivia Liam Emma Noah Amelia Elijah Sophia James Charlotte Lucas Isabella Mason Mia Ethan Evelyn Henry Harper Benjamin '
         'Sofia Alexander Avery Daniel Ella Samuel Scarlett Joseph Grace David Chloe Leo Aria Owen Layla Wyatt Nora Caleb Zoe '
         'Isaac Hannah Julian').split()
LAST = ('Bennett Patel Rivera Kim Morgan Chen Brooks Shah Reed Nguyen Carter Singh Foster Garcia Hughes Lewis Ahmed Parker Wilson '
        'Davis Robinson Turner Martinez Clark Walker Lopez Young Allen King Wright Scott Green Baker Adams Nelson Hill Ramirez '
        'Campbell Mitchell Roberts Phillips Evans Edwards Collins Stewart Sanchez Morris Rogers Cook Bell').split()
DEPTS = {
    'Electronics': [('Wireless Earbuds', 59.99), ('USB-C Charger 65W', 34.99), ('Bluetooth Speaker', 44.99), ('Smart Plug 2-Pack', 24.99),
                    ('Portable Power Bank', 29.99), ('HD Webcam', 49.99), ('Wireless Mouse', 19.99), ('Mechanical Keyboard', 79.99),
                    ('HDMI Cable 2m', 9.99), ('Fitness Tracker Band', 39.99)],
    'Home & Kitchen': [('Nonstick Frying Pan 28cm', 32.99), ('Glass Food Containers', 27.99), ('Chef Knife 20cm', 24.99),
                       ('French Press 1L', 22.99), ('Bamboo Cutting Board', 18.99), ('Cotton Bath Towel', 15.99),
                       ('LED Desk Lamp', 29.99), ('Storage Basket', 21.99), ('Electric Kettle 1.7L', 34.99), ('Throw Blanket', 26.99)],
    'Fashion': [('Crew Neck T-Shirt', 14.99), ('Slim Fit Jeans', 39.99), ('Running Sneakers', 64.99), ('Rain Jacket', 54.99),
                ('Wool Beanie', 12.99), ('Leather Belt', 19.99), ('Canvas Backpack', 34.99), ('Ankle Socks 6-Pack', 11.99),
                ('Hooded Sweatshirt', 32.99), ('Sunglasses', 17.99)],
    'Beauty': [('Daily Moisturizer 50ml', 16.99), ('Vitamin C Serum 30ml', 21.99), ('Mineral Sunscreen SPF50', 14.99),
               ('Shampoo 400ml', 9.99), ('Lip Balm 3-Pack', 6.99), ('Hair Dryer 1800W', 44.99), ('Electric Toothbrush', 39.99),
               ('Body Wash 500ml', 8.99), ('Makeup Brush Set', 18.99), ('Hand Cream 75ml', 7.99)],
    'Toys & Games': [('Building Blocks 500pc', 29.99), ('Jigsaw Puzzle 1000pc', 16.99), ('Remote Control Car', 39.99),
                     ('Plush Bear 30cm', 14.99), ('Board Game Classic', 24.99), ('Art Set 80pc', 19.99), ('Card Game', 9.99),
                     ('Science Kit', 27.99), ('Toy Train Set', 34.99), ('Kids Scooter', 49.99)],
    'Grocery': [('Ground Coffee 500g', 11.99), ('Green Tea 100 Bags', 7.99), ('Almonds 1kg', 13.99), ('Olive Oil 1L', 12.99),
                ('Protein Bars 12-Pack', 19.99), ('Basmati Rice 5kg', 15.99), ('Dark Chocolate 6-Pack', 10.99),
                ('Pasta 6-Pack', 8.99), ('Maple Syrup 500ml', 9.99), ('Sparkling Water 24-Pack', 12.99)],
    'Books': [('Cookbook Paperback', 18.99), ('Mystery Novel', 14.99), ('Science Fiction Novel', 15.99), ('Kids Picture Book', 9.99),
              ('Travel Guide', 19.99), ('Biography Hardcover', 24.99), ('Self-Help Paperback', 13.99), ('Coloring Book', 7.99),
              ('History Hardcover', 27.99), ('Puzzle Book', 8.99)],
    'Sports & Outdoors': [('Yoga Mat 6mm', 24.99), ('Insulated Water Bottle', 21.99), ('Resistance Bands Set', 16.99),
                          ('Camping Lantern', 22.99), ('Adjustable Dumbbells', 89.99), ('Cycling Gloves', 14.99),
                          ('Hiking Daypack 20L', 44.99), ('Jump Rope', 9.99), ('Foam Roller', 19.99), ('Tent 2-Person', 99.99)],
}
VARIANTS = ['Black', 'White', 'Blue', 'Gray', 'Green']
SELLER_WORDS = ['Outlet', 'Direct', 'Supply Co', 'Goods', 'Market', 'Depot', 'Store', 'Traders', 'Shop', 'Hub']


def ecommerce():
    slug = 'ecommerce'
    rng = Random(20240716)
    E = ['OrderID', 'CustomerID', 'OrderReference', 'SalesChannel', 'OrderStatus', 'OrderTotal', 'ItemCount',
         'OrderDate', 'PlacedAt', 'ParentOrderID']
    T = [
        table('Customers', 'CustomerID', [('CustomerID', 'int'), ('CustomerName', 'nvarchar(80)'), ('CustomerCode', 'varchar(20)'),
                                          ('Region', 'varchar(10)')],
              ['CustomerCode'], ['LEN(LTRIM(RTRIM(CustomerName))) > 0'],
              purpose='Shoppers; a few heavy buyers order almost every week, most order a handful of times a year.'),
        table('Sellers', 'SellerID', [('SellerID', 'int'), ('SellerName', 'nvarchar(80)'), ('SellerCode', 'varchar(20)'),
                                      ('Department', 'varchar(20)')],
              ['SellerCode'], ['LEN(LTRIM(RTRIM(SellerName))) > 0'],
              purpose='Third-party sellers on the marketplace; each seller sells in one department and fulfils its own orders.'),
        table('Products', 'ProductID', [('ProductID', 'int'), ('ProductName', 'nvarchar(80)'), ('SKU', 'varchar(20)'),
                                        ('UnitPrice', 'decimal(12,2)'), ('Department', 'varchar(20)', "NOT NULL DEFAULT ('General')")],
              ['SKU'], ['UnitPrice > 0', 'LEN(LTRIM(RTRIM(ProductName))) > 0'],
              purpose='Catalog listing price; the price actually charged is stored on each order item.'),
        table('Orders', 'OrderID', [tuple(c) for c in event_columns(*E)] + [('SellerID', 'int')],
              ['OrderReference'], event_checks(E[0], E[2], E[3], E[4], E[5], E[6], E[9]),
              [('CustomerID', 'Customers', 'CustomerID'), ('ParentOrderID', 'Orders', 'OrderID'), ('SellerID', 'Sellers', 'SellerID')],
              purpose=EVENT_PURPOSE + ' One order is one checkout with one seller; OrderTotal equals the sum of its items.'),
        table('OrderItems', 'OrderItemID', [('OrderItemID', 'int'), ('OrderID', 'int'), ('ProductID', 'int'), ('Quantity', 'int'),
                                            ('UnitPrice', 'decimal(12,2)')],
              ['OrderID, ProductID'], ['Quantity > 0', 'UnitPrice >= 0'],
              [('OrderID', 'Orders', 'OrderID'), ('ProductID', 'Products', 'ProductID')],
              purpose='Lines of an order; UnitPrice is the price charged, after any deal discount.'),
        table('Payments', 'PaymentID', [('PaymentID', 'int'), ('OrderID', 'int'), ('PaymentMethod', 'varchar(10)'),
                                        ('PaidAmount', 'decimal(12,2)'), ('PaidAt', 'datetime2(3)')],
              [], ["PaymentMethod IN ('Card','Wallet','GiftCard','COD')", 'PaidAmount > 0'],
              [('OrderID', 'Orders', 'OrderID')],
              purpose='Payments per order; some orders are split between a gift card and a card. Pending orders are unpaid.'),
    ]
    tb = {t['name']: t for t in T}
    rows = {t['name']: [] for t in T}

    def add(name, **v):
        v[tb[name]['key']] = len(rows[name]) + 1
        rows[name].append(v)
        return v

    n_cust = 2000
    for i in range(1, n_cust + 1):
        add('Customers', CustomerName=f'{FIRST[(i - 1) % 40]} {LAST[((i - 1) // 40 + (i - 1) * 3) % 50]}',
            CustomerCode=f'EBC-{i:06}', Region=location(i)[1])
    depts = list(DEPTS)
    for i in range(1, 81):
        d = depts[(i - 1) % 8]
        add('Sellers', SellerName=f'{BRANDS[(i - 1) % 25]} {SELLER_WORDS[(i - 1) // 8 % 10]}', SellerCode=f'SEL-{i:04}', Department=d)
    by_dept = {d: [] for d in depts}
    for d in depts:
        for base, price in DEPTS[d]:
            for v in VARIANTS:
                p = add('Products', ProductName=f'{base} - {v}', SKU=f'EB-{len(rows["Products"]) + 1:05}',
                        UnitPrice=money(price * rng.choice([.9, 1, 1, 1.1])), Department=d)
                by_dept[d].append(p)
    sellers_by_dept = {d: [s for s in rows['Sellers'] if s['Department'] == d] for d in depts}
    seller_w = {s['SellerID']: 1 / (1 + (s['SellerID'] - 1) // 8) ** .9 for s in rows['Sellers']}    # bigger sellers first
    cust_w = [1 / (i ** .75) for i in range(1, n_cust + 1)]
    cust_ids = list(range(1, n_cust + 1))
    rng.shuffle(cust_ids)                                                                           # heavy buyers spread over IDs
    hour_w = [2, 1, 1, 1, 1, 2, 3, 5, 6, 7, 8, 9, 11, 10, 8, 8, 9, 10, 12, 15, 16, 14, 9, 5]

    def day_volume(d):
        n = 72 * (1.25 if d.weekday() >= 5 else 1) * (1 + .12 * (d.month - 1) / 11)
        if datetime(2024, 11, 25) <= d <= datetime(2024, 12, 22):
            n *= 1.85
        if d in (datetime(2024, 7, 16), datetime(2024, 7, 17)):                                     # Bazaar Days sale
            n *= 3.6
        if d in (datetime(2024, 12, 25), datetime(2024, 1, 1)):
            n *= .55
        return max(20, int(rng.gauss(n, n * .08)))

    oid = 0
    day = datetime(2024, 1, 1)
    while day.year == 2024:
        deal = day in (datetime(2024, 7, 16), datetime(2024, 7, 17)) or datetime(2024, 11, 29) <= day <= datetime(2024, 12, 2)
        times = sorted(day + timedelta(seconds=rng.randrange(3600)) + timedelta(hours=rng.choices(range(24), hour_w)[0])
                       for _ in range(day_volume(day)))
        for t in times:
            oid += 1
            dweights = [1.0] * 8
            if t.month == 12 or (t.month == 11 and t.day >= 25):
                dweights[depts.index('Toys & Games')] = 2.6
                dweights[depts.index('Electronics')] = 1.6
            if t.month in (6, 7, 8):
                dweights[depts.index('Sports & Outdoors')] = 1.7
            d = rng.choices(depts, dweights)[0]
            sl = sellers_by_dept[d]
            seller = rng.choices(sl, [seller_w[s['SellerID']] for s in sl])[0]
            customer = cust_ids[rng.choices(range(n_cust), cust_w)[0]]
            total, units = 0, 0
            for p in rng.sample(by_dept[d], rng.choices([1, 2, 3, 4, 5], [52, 27, 12, 6, 3])[0]):
                qty = rng.choices([1, 2, 3, 4], [72, 19, 6, 3])[0]
                price = money(p['UnitPrice'] * (rng.choice([.7, .75, .8]) if deal else rng.choice([1, 1, 1, 1, .9])))
                add('OrderItems', OrderID=oid, ProductID=p['ProductID'], Quantity=qty, UnitPrice=price)
                total += qty * price
                units += qty
            total = money(total)
            late = t >= datetime(2024, 12, 20)
            r = rng.random()
            status = 'Pending' if r < .035 else 'Open' if (late and r < .75) or r < .06 else 'Closed'
            channel = rng.choices('ABC', [58, 34, 8])[0]
            note = rng.choices([None, 'Standard delivery', 'Express delivery', 'Gift order', 'Locker pickup'], [30, 40, 18, 7, 5])[0]
            add('Orders', CustomerID=customer, OrderReference=f'EB-{t:%Y%m%d}-{oid:06}', SalesChannel=channel, OrderStatus=status,
                OrderTotal=total, ItemCount=units, OrderDate=t.strftime('%Y%m%d'), PlacedAt=stamp(t),
                RecordedAt=stamp(t + timedelta(seconds=rng.randrange(1, 46))) + '+00:00', Note=note,
                BackupNote='Flagged for fraud review' if oid % 97 == 0 else None, ParentOrderID=None, SellerID=seller['SellerID'])
            if status != 'Pending':
                paid_at = t + timedelta(seconds=rng.randrange(5, 120))
                if total > 40 and rng.random() < .08:
                    gift = money(min(total - 1, rng.choice([10, 20, 25, 50])))
                    add('Payments', OrderID=oid, PaymentMethod='GiftCard', PaidAmount=gift, PaidAt=stamp(paid_at))
                    add('Payments', OrderID=oid, PaymentMethod='Card', PaidAmount=money(total - gift), PaidAt=stamp(paid_at + timedelta(seconds=4)))
                else:
                    method = rng.choices(['Card', 'Wallet', 'COD'], [70, 24, 6])[0]
                    when = paid_at + timedelta(days=rng.randrange(2, 6)) if method == 'COD' else paid_at
                    if method == 'COD' and status == 'Open':
                        continue                                                                   # cash collected on delivery
                    add('Payments', OrderID=oid, PaymentMethod=method, PaidAmount=total, PaidAt=stamp(when))
        day += timedelta(days=1)

    for o in rows['Orders']:
        assert o['OrderTotal'] >= 0
    model = dict(slug=slug, title='E-commerce',
                 map=dict(RecordID=E[0], PartyID=E[1], Label=E[2], Category=E[3], Status=E[4], Amount=E[5], Quantity=E[6],
                          EventDate=E[7], EventTime=E[8], RecordedAt='RecordedAt', Note='Note', BackupNote='BackupNote',
                          ParentID=E[9], PartyName='CustomerName'),
                 base=['Orders', 'Customers', 'CustomerName'],
                 business='Run a marketplace with tens of thousands of orders: daily volume, peaks, repeat buyers, sellers and payments.',
                 masters={'Customers', 'Sellers', 'Products'},
                 notes='SalesChannel A=mobile app, B=website, C=voice assistant. Closed orders are delivered and paid, Open orders are '
                       'in progress (cash-on-delivery ones are unpaid until delivery), Pending orders await payment. Bazaar Days sale: 16-17 July 2024.',
                 tables=T)
    return model, rows




def large_rows(slug):
    return {'retail_supply_chain': supply_chain, 'ecommerce': ecommerce}[slug]()[1]
