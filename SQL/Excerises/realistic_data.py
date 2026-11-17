"""Deterministic fictional business fixtures; no network or personal data sources.

Run large_data_setup.py to regenerate SQL, guides and validation counts.
The original small answer-key fixtures are intentionally independent.
"""
from copy import deepcopy
from datetime import datetime, timedelta
from random import Random

FIRST = 'Olivia Liam Emma Noah Amelia Elijah Sophia James Charlotte Lucas Isabella Mason Mia Ethan Evelyn Henry Harper Benjamin Sofia Alexander Avery Daniel Ella Samuel Scarlett Joseph Grace David Chloe Leo'.split()
LAST = 'Bennett Patel Rivera Kim Morgan Chen Brooks Shah Reed Nguyen Carter Singh Foster Garcia Hughes Lewis Ahmed Parker Wilson Davis Robinson Turner Martinez Clark Walker'.split()
CITIES = ['Chicago', 'Dallas', 'Seattle', 'Boston', 'Atlanta', 'Denver', 'Phoenix', 'Portland', 'Austin', 'Miami', 'Detroit', 'Columbus', 'Nashville', 'Charlotte', 'Tampa', 'Raleigh', 'Madison', 'Boise', 'Omaha', 'Tulsa', 'Wichita', 'Richmond', 'Sacramento', 'Baltimore', 'Pittsburgh']
REGIONS = ['North', 'South', 'West', 'East', 'South', 'West', 'West', 'West', 'South', 'South', 'North', 'North', 'South', 'South', 'South', 'South', 'North', 'West', 'North', 'South', 'North', 'East', 'West', 'East', 'East']
BRANDS = ['Cedar Grove', 'Northstar', 'Riverbend', 'Summit Ridge', 'Oak Harbor', 'Prairie Creek', 'Blue Heron', 'Willow Brook', 'Granite Peak', 'Meadow Glen', 'Silver Birch', 'Clearwater', 'Maple Ridge', 'Copper Trail', 'Stonebridge', 'Pine Valley', 'Harbor Point', 'Juniper Hill', 'Aspen Crest', 'Laurel Creek', 'Redwood', 'Elm Grove', 'Lakeview', 'Sage Valley', 'Birch Hollow']
GOODS = [('Cotton Bath Towel', 18.50), ('Insulated Water Bottle 750ml', 24.95), ('Canvas Daypack 20L', 49.95), ('Ceramic Coffee Mug 350ml', 12.50), ('Linen Cushion Cover 45cm', 16.95), ('LED Desk Lamp', 39.95), ('A5 Hardcover Notebook', 9.95), ('Yoga Mat 6mm', 29.95), ('Fleece Throw 150cm', 34.50), ('Lunch Tote 8L', 22.95), ('Cotton Apron', 19.50), ('Travel Organizer', 17.95), ('Woven Storage Basket', 26.95), ('Silicone Spatula Set', 14.95), ('Laptop Sleeve 14in', 28.50), ('Garden Tool Pouch', 21.95), ('Microfiber Cleaning Cloth Set', 8.95), ('Reusable Shopping Bag', 6.50), ('Pet Travel Bowl', 11.95), ('Cotton Table Runner', 23.50)]
COLORS = ['Navy', 'Sage', 'Sand', 'Slate', 'Terracotta']
# Name, two marketed strengths, illustrative unit acquisition costs.
MEDS = [('Acetaminophen', '325mg', '500mg', .08), ('Ibuprofen', '200mg', '400mg', .10), ('Cetirizine', '5mg', '10mg', .18), ('Loratadine', '5mg', '10mg', .16), ('Omeprazole', '10mg', '20mg', .24), ('Famotidine', '10mg', '20mg', .20), ('Vitamin D3', '1000IU', '2000IU', .09), ('Vitamin C', '250mg', '500mg', .07), ('Calcium Carbonate', '500mg', '750mg', .12), ('Melatonin', '1mg', '3mg', .11), ('Metformin', '500mg', '850mg', .09), ('Amlodipine', '2.5mg', '5mg', .08), ('Lisinopril', '5mg', '10mg', .07), ('Losartan', '25mg', '50mg', .12), ('Atorvastatin', '10mg', '20mg', .15), ('Rosuvastatin', '5mg', '10mg', .18), ('Levothyroxine', '25mcg', '50mcg', .19), ('Sertraline', '25mg', '50mg', .14), ('Escitalopram', '5mg', '10mg', .16), ('Montelukast', '5mg', '10mg', .20), ('Folic Acid', '400mcg', '800mcg', .06), ('Vitamin B12', '500mcg', '1000mcg', .10), ('Naproxen', '250mg', '500mg', .13), ('Pantoprazole', '20mg', '40mg', .21), ('Pravastatin', '20mg', '40mg', .17)]

NOTES = {
    'retail': 'SalesChannel A=web, B=store, C=phone. Totals equal line values before tax/shipping; Closed orders are fully paid, Open partially paid, Pending unpaid.',
    'banking': 'TransactionType A=credit, B=debit, C=fee. Amounts are unsigned; UnitCount is one posting. Related postings share an account; loans use the account owner.',
    'pharma': 'BatchType A=scheduled run, B=contract run, C=small run. Costs and inventory use 30-tablet packs. Inventory is a 2025-01-10 snapshot; held batches have no released stock.',
    'healthcare': 'EncounterType A=office visit, B=follow-up, C=telehealth. All doctors practice Family Medicine. Medication rows and quantities are illustrative, not prescribing instructions.',
    'oil': 'ShipmentType A=contract delivery, B=spot delivery, C=terminal transfer. Products are packaged lubricants; quantity is containers and value equals item extensions.',
    'retail_manufacturing': 'ProductionCategory A=standard run, B=replenishment, C=small run. Materials use meters for fabric/thread and pieces for zippers. Planned cost is BOM material cost; actual usage includes small waste variances.',
    'retail_logistics': 'ShipmentCategory A=standard, B=express, C=freight. Declared packages match package rows. Closed shipments are delivered, Open in transit, Pending picked up awaiting linehaul.',
    'retail_inventory': 'MovementCategory A=receipt, B=dispatch, C=return. Only Closed movements affect balances. Opening plus signed completed movements equals quantity on hand; SupplierID identifies product source.',
    'brokerage': 'RoutingCategory A=market, B=limit, C=scheduled. All orders are Buy per the schema. Securities and prices are fictional; Closed orders fully fill, Open partially fill, Pending have no executions.',
}


def person(i):
    return f'{FIRST[(i - 1) % len(FIRST)]} {LAST[((i - 1) * 7 + (i - 1) // len(FIRST)) % len(LAST)]}'


def stamp(d):
    return d.isoformat(timespec='milliseconds')


def build(original):
    model = deepcopy(original)
    slug = model['slug']
    rng = Random(202410 + sum(map(ord, slug)))
    tables = {t['name']: t for t in model['tables']}
    rows = {name: [] for name in tables}
    model['fixture_notes'] = NOTES[slug]

    def add(table, **values):
        values[tables[table]['key']] = len(rows[table]) + 1
        rows[table].append(values)
        return values

    def money(v):
        return round(v + 1e-8, 2)

    def master(table, count, make):
        for i in range(1, count + 1):
            add(table, **make(i))

    def location(i):
        return CITIES[(i - 1) % 25], REGIONS[(i - 1) % 25]

    def contact(i, label):
        return {label: person(i), 'Email': person(i).lower().replace(' ', '.') + '@example.com'}

    def catalog(i):
        name, cost = GOODS[(i - 1) // 5]
        return f'{name} - {COLORS[(i - 1) % 5]}', cost

    def medication(i):
        name, a, b, cost = MEDS[(i - 1) // 2]
        return f'{name} {a if i % 2 else b} tablet', money(cost * (1 if i % 2 else 1.3))

    def event(i, party, category, value, units, note, status=None, **extra):
        # Stable chronology covers a full leap year with varied business-hour times.
        day = datetime(2024, 1, 1) + timedelta(days=(i - 1) * 365 // 239, hours=rng.randrange(8, 18), minutes=rng.randrange(60), seconds=rng.randrange(60))
        vals = dict(RecordID=i, PartyID=party, Label=f'{slug[:3].upper()}-{day:%Y%m%d}-{i:05}', Category=category,
                    Status=status or ('Closed' if i <= 204 else 'Open' if i <= 228 else 'Pending'),
                    Amount=value, Quantity=units, EventDate=day.strftime('%Y%m%d'), EventTime=stamp(day),
                    RecordedAt=stamp(day + timedelta(seconds=rng.randrange(2, 91))) + '+00:00',
                    Note=note, BackupNote='Reviewed by operations' if i % 17 == 0 else None, ParentID=None)
        mapped = {model['map'][k]: v for k, v in vals.items()}
        mapped.update(extra)
        return add(model['base'][0], **mapped), day

    if slug == 'banking':
        master('Branches', 50, lambda i: dict(BranchName=f'{location(i)[0]} {"Downtown" if i <= 25 else "Westside"}', BranchCode=f'BR-{i:04}', City=location(i)[0]))
        master('Customers', 100, lambda i: contact(i, 'CustomerName'))
        master('Accounts', 100, lambda i: dict(AccountName=f'{person(i)} - {"Checking" if i % 3 else "Savings"}', AccountNumber=f'7102{i:010}', Region=location((i - 1) % 50 + 1)[1], CustomerID=i, BranchID=(i - 1) % 50 + 1))
        for i in range(1, 241):
            account = rng.randrange(1, 96)
            cat = rng.choices('ABC', [35, 60, 5])[0]
            amount = money(rng.uniform(1800, 6200) if cat == 'A' else rng.uniform(8, 650) if cat == 'B' else rng.choice([2.5, 5, 12, 15]))
            event(i, account, cat, amount, 1, rng.choice(['Payroll direct deposit', 'ACH transfer received']) if cat == 'A' else rng.choice(['Grocery card purchase', 'Utility bill payment', 'Insurance premium', 'Online purchase']) if cat == 'B' else 'Monthly account service fee')
        master('Loans', 100, lambda i: dict(CustomerID=(i - 1) % 85 + 1, AccountID=(i - 1) % 85 + 1, LoanReference=f'LN-2024-{i:06}', Principal=rng.randrange(20, 601) * 500, AnnualRate=money(rng.uniform(4.75, 12.5))))

    elif slug in ('retail', 'retail_inventory'):
        master('Products', 100, lambda i: dict(ProductName=catalog(i)[0], SKU=f'HOME-{i:05}', **({'UnitPrice': catalog(i)[1], 'StockQuantity': rng.randrange(0, 240)} if slug == 'retail' else {'UnitCost': money(catalog(i)[1] * .58)})))
        if slug == 'retail':
            master('Customers', 100, lambda i: dict(CustomerName=person(i), CustomerCode=f'CUS-{i:06}', Region=location(i)[1]))
            for i in range(1, 241):
                total = 0
                for product in rng.sample(range(1, 101), rng.choices([1, 2, 3, 4], [30, 40, 20, 10])[0]):
                    qty = rng.choices([1, 2, 3, 4], [65, 25, 7, 3])[0]
                    price = money(catalog(product)[1] * rng.choice([1, 1, 1, .9]))
                    add('OrderItems', OrderID=i, ProductID=product, Quantity=qty, UnitPrice=price)
                    total += qty * price
                order, day = event(i, rng.randrange(1, 96), rng.choices('ABC', [60, 30, 10])[0], money(total), rng.choice([1, 1, 1, 2]), 'Customer order; prices include any promotional discount')
                if i <= 228:
                    paid = money(total if i <= 204 else total * .5)
                    amounts = [money(paid * .4), money(paid - money(paid * .4))] if i % 7 == 0 else [paid]
                    for offset, amount in enumerate(amounts):
                        add('Payments', OrderID=i, PaymentReference=f'PAY-{i:06}-{offset + 1}', PaidAmount=amount, PaymentDate=(day + timedelta(days=offset + 1)).strftime('%Y%m%d'))
        else:
            master('Warehouses', 50, lambda i: dict(WarehouseName=f'{location(i)[0]} {"Fulfillment Center" if i <= 25 else "Store Replenishment Depot"}', WarehouseCode=f'WH-{i:04}', Region=location(i)[1]))
            master('Suppliers', 50, lambda i: dict(SupplierName=f'{BRANDS[(i - 1) % 25]} {"Home Goods" if i <= 25 else "Retail Supply"}', SupplierCode=f'SUP-{i:04}', LeadTimeDays=rng.choice([3, 5, 7, 10, 14, 21])))
            # Two products per location, each with a replenishment and later dispatch.
            for i in range(1, 241):
                pair = (i - 1) % 100
                product, warehouse = pair + 1, pair % 50 + 1
                direction = 'IN' if i <= 100 or i > 200 else 'OUT'
                units = rng.randrange(24, 97) if direction == 'IN' else rng.randrange(5, 41)
                event(i, warehouse, 'A' if i <= 100 else 'B' if i <= 200 else 'C', money(units * rows['Products'][product - 1]['UnitCost']), units, 'Supplier replenishment' if i <= 100 else 'Store allocation dispatch' if i <= 200 else 'Resalable customer returns', ProductID=product, SupplierID=(product - 1) % 50 + 1, Direction=direction)
            for p in range(1, 101):
                opening = rng.randrange(50, 180)
                movement = sum((r['MovedUnits'] if r['Direction'] == 'IN' else -r['MovedUnits']) for r in rows['StockMovements'] if r['ProductID'] == p and r['Status'] == 'Closed')
                add('StockBalances', WarehouseID=(p - 1) % 50 + 1, ProductID=p, OpeningQuantity=opening, QuantityOnHand=opening + movement, ReorderLevel=rng.choice([60, 100, 150]))

    elif slug in ('pharma', 'healthcare'):
        table = 'Products' if slug == 'pharma' else 'Medications'
        master(table, 50, lambda i: dict(ProductName=medication(i)[0] + ' - 30 count', ProductCode=f'PH-{i:05}', StandardCost=money(medication(i)[1] * 30)) if slug == 'pharma' else dict(MedicationName=medication(i)[0], MedicationCode=f'MED-{i:05}', UnitCost=medication(i)[1]))
        if slug == 'pharma':
            master('Suppliers', 50, lambda i: dict(SupplierName=f'{BRANDS[(i - 1) % 25]} {"Pharmaceuticals" if i <= 25 else "Health Distribution"}', SupplierCode=f'PS-{i:04}', Region=location(i)[1]))
            master('Warehouses', 50, lambda i: dict(WarehouseName=f'{location(i)[0]} {"Pharma Distribution" if i <= 25 else "Regional Medicine Depot"}', WarehouseCode=f'PW-{i:04}', Capacity=rng.randrange(20, 61) * 1000))
            for i in range(1, 241):
                product = (i - 1) % 50 + 1
                packs = rng.choice([240, 480, 720, 960, 1200, 1440])
                event(i, product, rng.choice('AAB'), money(packs * rows['Products'][product - 1]['StandardCost']), packs, 'Quality release complete' if i <= 204 else 'Quality review in progress', ProductID=product)
                if i <= 204:
                    remaining = rng.randrange(0, packs + 1)
                    first = remaining // 2
                    for warehouse, qty in [((i - 1) % 50 + 1, first), (i % 50 + 1, remaining - first)]:
                        add('Inventory', BatchID=i, WarehouseID=warehouse, QuantityOnHand=qty, LastCountDate='20250110')
        else:
            master('Patients', 100, lambda i: dict(PatientName=person(i), PatientNumber=f'PT-{i:07}', Region=location(i)[1]))
            master('Doctors', 50, lambda i: dict(DoctorName='Dr. ' + person(i + 150), LicenseNumber=f'MD-SIM-{i:06}', Specialty='Family Medicine'))
            for i in range(1, 241):
                patient = (i - 1) % 95 + 1
                category = rng.choice('AABC')
                enc, _ = event(i, patient, category, money(rng.randrange(85, 251) if category != 'C' else rng.randrange(65, 121)), 1, 'Routine primary care review', DoctorID=(patient - 1) % 50 + 1)
                if i > 95:
                    enc['ParentEncounterID'] = i - 95
                    enc['EncounterType'] = 'B'
                    enc['Note'] = 'Follow-up with established primary care physician'
                if i <= 204 and i % 5:
                    add('Prescriptions', EncounterID=i, MedicationID=(patient - 1) % 50 + 1, PrescriptionReference=f'RX-2024-{i:06}', Quantity=rng.choice([30, 60, 90]))

    elif slug == 'oil':
        master('Sites', 50, lambda i: dict(SiteName=f'{location(i)[0]} {"Lubricants Terminal" if i <= 25 else "Bulk Distribution Depot"}', SiteCode=f'TERM-{i:04}', Region=location(i)[1]))
        master('Carriers', 50, lambda i: dict(CarrierName=f'{BRANDS[(i - 1) % 25]} {"Bulk Transport" if i <= 25 else "Industrial Freight"}', CarrierCode=f'OC-{i:04}', Active=0 if i > 47 else 1))
        oils = [('Hydraulic Oil ISO 32', 3.4), ('Hydraulic Oil ISO 46', 3.6), ('Hydraulic Oil ISO 68', 3.8), ('Gear Oil ISO 150', 5.2), ('Gear Oil ISO 220', 5.5), ('Compressor Oil ISO 46', 6.2), ('Turbine Oil ISO 32', 5.8), ('Engine Oil SAE 15W-40', 4.9), ('Engine Oil SAE 10W-30', 5.1), ('Transmission Fluid Dex III', 5.6)]
        sizes = [1, 5, 20, 60, 205]
        master('Products', 50, lambda i: dict(ProductName=f'{oils[(i - 1) // 5][0]} - {sizes[(i - 1) % 5]}L', ProductCode=f'LUBE-{i:05}', PricePerUnit=money(oils[(i - 1) // 5][1] * sizes[(i - 1) % 5])))
        for i in range(1, 241):
            total, units = 0, 0
            for product in rng.sample(range(1, 51), rng.choice([1, 2, 3])):
                qty = rng.randrange(4, 49)
                price = money(rows['Products'][product - 1]['PricePerUnit'] * rng.choice([.95, 1, 1.02]))
                add('ShipmentItems', ShipmentID=i, ProductID=product, Quantity=qty, PricePerUnit=price)
                total += qty * price
                units += qty
            event(i, rng.randrange(1, 51), rng.choice('AABC'), money(total), units, 'Packaged lubricant consignment; sealed containers', CarrierID=rng.randrange(1, 48))

    elif slug == 'retail_manufacturing':
        # 50 textile SKUs, each with a matched fabric, thread and zipper recipe.
        textiles = ['Canvas Tote', 'Travel Pouch', 'Cushion Cover', 'Laptop Sleeve', 'Laundry Bag', 'Tool Roll', 'Lunch Bag', 'Garment Bag', 'Toiletry Bag', 'Storage Cube']
        master('Products', 50, lambda i: dict(ProductName=f'{textiles[(i - 1) // 5]} - {COLORS[(i - 1) % 5]}', ProductCode=f'TEXT-{i:05}', Region=location(i)[1]))
        for kind, cost in [('Cotton Canvas', 7.4), ('Lining Fabric', 3.2), ('Polyester Thread', .08), ('Coil Zipper 30cm', .85)]:
            for color in COLORS:
                for grade in ['Standard', 'Heavy Duty', 'Recycled']:
                    add('Materials', MaterialName=f'{color} {kind} - {grade}', MaterialCode=f'MAT-{len(rows["Materials"]) + 1:05}', UnitCost=money(cost * {'Standard': 1, 'Heavy Duty': 1.25, 'Recycled': 1.12}[grade]))
        for p in range(1, 51):
            color = (p - 1) % 5
            grade = (p - 1) // 5 % 3
            for material, qty in [(color * 3 + grade + 1, money(.35 + ((p - 1) // 5) * .12)), (15 + color * 3 + grade + 1, .30), (30 + color * 3 + grade + 1, 3.50), (45 + color * 3 + grade + 1, 1)]:
                add('BillOfMaterials', ProductID=p, MaterialID=material, QuantityPerUnit=qty)
        for i in range(1, 241):
            product = (i - 1) % 50 + 1
            units = rng.choice([40, 60, 80, 120, 180, 240])
            recipe = [r for r in rows['BillOfMaterials'] if r['ProductID'] == product]
            cost = money(sum(r['QuantityPerUnit'] * rows['Materials'][r['MaterialID'] - 1]['UnitCost'] * units for r in recipe))
            _, day = event(i, product, rng.choice('AABC'), cost, units, 'Cut-and-sew production; material-only cost')
            if i <= 228:
                for r in recipe:
                    used = r['QuantityPerUnit'] * units * (1 if r['MaterialID'] > 45 else rng.choice([1, 1.01, 1.02, 1.04])) * (1 if i <= 204 else .5)
                    add('MaterialUsage', ProductionOrderID=i, MaterialID=r['MaterialID'], QuantityUsed=money(used), UsageDate=(day + timedelta(days=1)).strftime('%Y%m%d'))

    elif slug == 'retail_logistics':
        master('Customers', 100, lambda i: dict(CustomerName=person(i), CustomerCode=f'LC-{i:06}', Region=location(i)[1]))
        master('Carriers', 50, lambda i: dict(CarrierName=f'{BRANDS[(i - 1) % 25]} {"Parcel Services" if i <= 25 else "Freight Lines"}', CarrierCode=f'CR-{i:04}', ServiceLevel='Ground' if i <= 20 else 'Express' if i <= 25 else 'Freight'))
        for i in range(1, 241):
            carrier = rng.randrange(1, 51)
            category = 'A' if carrier <= 20 else 'B' if carrier <= 25 else 'C'
            count = rng.choice([1, 1, 2, 3])
            weights = [money(rng.uniform(12, 90) if category == 'C' else rng.uniform(.3, 12)) for _ in range(count)]
            value = money((8 if category == 'A' else 18 if category == 'B' else 45) * count + sum(weights) * 1.15)
            _, day = event(i, rng.randrange(1, 96), category, value, count, 'Customer delivery; standard packaging', CarrierID=carrier)
            for weight in weights:
                package = add('ShipmentPackages', ShipmentID=i, TrackingNumber=f'TRK24{len(rows["ShipmentPackages"]) + 1:012}', WeightKg=weight, PromisedDate=(day + timedelta(days=1 if category == 'B' else 4)).strftime('%Y%m%d'))
                statuses = ['PickedUp', 'InTransit', 'Delivered'] if i <= 204 else ['PickedUp', 'InTransit'] if i <= 228 else ['PickedUp']
                for step, status in enumerate(statuses):
                    scan = day + timedelta(hours=1 if step == 0 else 8 if step == 1 else (24 if category == 'B' else rng.choice([48, 72, 120])))
                    add('TrackingEvents', PackageID=package['PackageID'], ScanReference=f'SCN-{len(rows["TrackingEvents"]) + 1:010}', EventStatus=status, ScanTime=stamp(scan), LocationName='Recipient address' if step == 2 else f'{CITIES[(carrier - 1) % 25]} {"pickup station" if step == 0 else "sorting hub"}')

    elif slug == 'brokerage':
        master('Clients', 100, lambda i: dict(**contact(i, 'ClientName'), ClientReference=f'CL-{i:06}'))
        master('Securities', 50, lambda i: dict(SecurityName=f'{BRANDS[(i - 1) % 25]} {"Industries" if i <= 25 else "Diversified Equity ETF"}', Symbol=f'SIM{i:03}', AssetClass='Stock' if i <= 25 else 'ETF'))
        master('BrokerageAccounts', 100, lambda i: dict(AccountName=f'{person(i)} - {"Individual" if i % 3 else "Retirement"}', AccountNumber=f'8201{i:010}', Region=location(i)[1], ClientID=i))
        prices = {i: money(rng.uniform(15, 250)) for i in range(1, 51)}
        for i in range(1, 241):
            security = rng.randrange(1, 51)
            quantity = rng.choice([5, 10, 20, 25, 50, 100, 200])
            price = money(prices[security] * rng.uniform(.94, 1.06))
            _, day = event(i, rng.randrange(1, 96), rng.choice('AABC'), money(quantity * price), quantity, 'Buy allocation; execution prices exclude fees', SecurityID=security, Side='Buy')
            if i <= 228:
                filled = quantity if i <= 204 else max(1, quantity // 2)
                fills = [filled // 2, filled - filled // 2] if i % 3 == 0 and filled > 1 else [filled]
                for part, qty in enumerate(fills):
                    add('Executions', OrderID=i, ExecutionReference=f'EX-{i:06}-{part + 1}', ExecutedQuantity=qty, ExecutionPrice=price, ExecutedAt=stamp(day + timedelta(seconds=95 + part * 30)))
    else:
        raise ValueError(slug)

    validate_business(slug, rows)
    for name, table in tables.items():
        table['rows'] = [[r[c['name']] for c in table['columns']] for r in rows[name]]
    return model


def validate_business(slug, rows):
    """Cross-table checks beyond foreign keys and column CHECK constraints."""
    def close(a, b):
        assert abs(a - b) < .011, (slug, a, b)

    if slug in ('retail', 'oil'):
        parent, detail, key, total, price = ('Orders', 'OrderItems', 'OrderID', 'OrderTotal', 'UnitPrice') if slug == 'retail' else ('Shipments', 'ShipmentItems', 'ShipmentID', 'ShipmentValue', 'PricePerUnit')
        for r in rows[parent]:
            items = [x for x in rows[detail] if x[key] == r[key]]
            close(r[total], sum(x['Quantity'] * x[price] for x in items))
            if slug == 'oil':
                assert r['UnitCount'] == sum(x['Quantity'] for x in items)
                assert rows['Carriers'][r['CarrierID'] - 1]['Active'] == 1
            else:
                payments = [x for x in rows['Payments'] if x[key] == r[key]]
                paid = sum(x['PaidAmount'] for x in payments)
                assert paid <= r[total] + .001
                if r['OrderStatus'] == 'Closed':
                    close(paid, r[total])
                assert all(x['PaymentDate'] >= r['OrderDate'] for x in payments)
    if slug == 'banking':
        assert all(r['CustomerID'] == rows['Accounts'][r['AccountID'] - 1]['CustomerID'] for r in rows['Loans'])
    if slug == 'pharma':
        for batch in rows['Batches']:
            close(batch['BatchCost'], batch['PackCount'] * rows['Products'][batch['ProductID'] - 1]['StandardCost'])
            stock = [r for r in rows['Inventory'] if r['BatchID'] == batch['BatchID']]
            assert sum(r['QuantityOnHand'] for r in stock) <= batch['PackCount']
            assert all(r['LastCountDate'] >= batch['ManufactureDate'] for r in stock)
        assert all(sum(r['QuantityOnHand'] for r in rows['Inventory'] if r['WarehouseID'] == w['WarehouseID']) <= w['Capacity'] for w in rows['Warehouses'])
    if slug == 'retail_inventory':
        for balance in rows['StockBalances']:
            movement = [r for r in rows['StockMovements'] if r['WarehouseID'] == balance['WarehouseID'] and r['ProductID'] == balance['ProductID']]
            onhand = balance['OpeningQuantity']
            for r in movement:
                close(r['MovementValue'], r['MovedUnits'] * rows['Products'][r['ProductID'] - 1]['UnitCost'])
                if r['Status'] == 'Closed':
                    onhand += r['MovedUnits'] * (1 if r['Direction'] == 'IN' else -1)
                    assert onhand >= 0
            assert onhand == balance['QuantityOnHand']
    if slug == 'retail_manufacturing':
        for order in rows['ProductionOrders']:
            recipe = {r['MaterialID']: r['QuantityPerUnit'] for r in rows['BillOfMaterials'] if r['ProductID'] == order['ProductID']}
            close(order['PlannedCost'], sum(q * rows['Materials'][m - 1]['UnitCost'] * order['PlannedUnits'] for m, q in recipe.items()))
            for usage in (r for r in rows['MaterialUsage'] if r['ProductionOrderID'] == order['ProductionOrderID']):
                assert usage['MaterialID'] in recipe and usage['UsageDate'] >= order['ProductionDate']
    if slug == 'retail_logistics':
        for shipment in rows['Shipments']:
            packages = [r for r in rows['ShipmentPackages'] if r['ShipmentID'] == shipment['ShipmentID']]
            assert shipment['DeclaredPackages'] == len(packages)
            for package in packages:
                assert package['PromisedDate'] >= shipment['ShipDate']
                events = [r for r in rows['TrackingEvents'] if r['PackageID'] == package['PackageID']]
                times = [e['ScanTime'] for e in events]
                assert times == sorted(times) and times[0] >= shipment['DispatchedAt']
                assert (events[-1]['EventStatus'] == 'Delivered') == (shipment['Status'] == 'Closed')
    if slug == 'brokerage':
        for order in rows['TradeOrders']:
            fills = [r for r in rows['Executions'] if r['OrderID'] == order['OrderID']]
            qty = sum(r['ExecutedQuantity'] for r in fills)
            assert qty <= order['RequestedQuantity']
            if order['WorkflowStatus'] == 'Closed':
                assert qty == order['RequestedQuantity']
            assert all(r['ExecutedAt'] >= order['SubmittedAt'] for r in fills)
    if slug == 'healthcare':
        for enc in rows['Encounters']:
            if enc['ParentEncounterID']:
                parent = rows['Encounters'][enc['ParentEncounterID'] - 1]
                assert parent['PatientID'] == enc['PatientID'] and parent['DoctorID'] == enc['DoctorID']
                assert parent['StartedAt'] < enc['StartedAt']
