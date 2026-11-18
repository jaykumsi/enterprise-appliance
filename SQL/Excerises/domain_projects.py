"""Connected five-table domain projects used by the curriculum generator."""
from pathlib import Path
import json
import re
from domain_question_wording import clarify_question

ROOT=Path(__file__).resolve().parent

def student_english(text):
    """Simplify directions, preserving SQL identifiers and code examples."""
    replacements={
        'seeded five-table project':'tables and sample rows you created earlier',
        'seed data':'sample rows',
        'dependency order':'the order shown in your domain guide',
        'restored baseline':'original tables and sample rows',
        'baseline':'original sample data',
        'fresh session with no open transaction':'new database connection with no unfinished transaction',
        'fresh session':'new database connection',
        'Inspect metadata':'Check the table settings',
        'column types/nullability and FK metadata':'column types, which columns allow NULL, and foreign key settings',
        'insert dependencies':'which tables need sample rows first',
        'predicate':'condition',
        'preserving':'keeping',
        'preserve':'keep',
        'cardinalities':'row counts',
        'cardinality':'number of matching rows',
        'at order/material grain':'for each order and material pair',
        'at the required grain':'so each row represents the right business item',
        'before/after evidence':'the results before and after your changes',
        'affected-row count':'number of changed rows',
        'reconcile':'compare and check',
        'capstone':'final project',
    }
    parts=re.split(r'(```[\s\S]*?```|`[^`]*`)',text)
    for i in range(0,len(parts),2):
        for old,new in replacements.items():
            parts[i]=re.sub(r'\b'+re.escape(old)+r'\b',new,parts[i])
    result=''.join(parts)
    number=0
    lines=[]
    for line in result.split('\n'):
        if re.match(r'^\d+\. ', line):
            number+=1
            line=re.sub(r'^\d+\. ', f'{number}. ', line)
        else:
            number=0
        lines.append(line)
    return '\n'.join(lines)

def col(name,typ,rule='',sample=None):
    return dict(name=name,type=typ,rule=rule,sample=sample)

def entity(name,key,columns,rows,unique=(),checks=(),fks=(),purpose=''):
    return dict(name=name,key=key,columns=[col(key,'int','NOT NULL')]+columns,rows=rows,
                unique=list(unique),checks=list(checks),fks=list(fks),purpose=purpose)

def ref(column,parent,key):
    return dict(column=column,parent=parent,key=key)

def master(name,key,label,purpose,extra=(),fks=()):
    code={'Customers':'CustomerCode','Accounts':'AccountNumber','Suppliers':'SupplierCode','Patients':'PatientNumber','Sites':'SiteCode','Products':'ProductCode','Warehouses':'WarehouseCode'}[name]
    columns=[col(label,'nvarchar(80)','NOT NULL'),col(code,'varchar(20)','NOT NULL'),col('Region','varchar(10)','NOT NULL')]+list(extra)
    rows=[[i,f'{name} {suffix}',f'{name[:3].upper()}-{i}',region]+[i for _ in extra] for i,suffix,region in [(1,'Alpha','North'),(2,'Beta','South'),(3,'Gamma','North'),(4,'Delta','West'),(5,'Unused','East')]]
    return entity(name,key,columns,rows,unique=[code],fks=fks,purpose=purpose)

def model(slug,title,names,base,tables,business):
    original=['RecordID','PartyID','Label','Category','Status','Amount','Quantity','EventDate','EventTime','RecordedAt','Note','BackupNote','ParentID']
    mapping=dict(zip(original,names))
    m=dict(slug=slug,title=title,map=mapping,base=base,tables=tables,business=business)
    return m

MODELS=[]
# Each table declares business columns, keys, sample rows and relationship targets.
retail_customer=master('Customers','CustomerID','CustomerName','One customer can place many orders.')
retail_product=entity('Products','ProductID',[col('ProductName','nvarchar(80)','NOT NULL'),col('SKU','varchar(20)','NOT NULL'),col('UnitPrice','decimal(12,2)','NOT NULL'),col('StockQuantity','int','NOT NULL')],[[1,'Notebook','SKU-1',25,20],[2,'Pen set','SKU-2',10,30],[3,'Backpack','SKU-3',50,10],[4,'Desk lamp','SKU-4',40,5],[5,'Unused product','SKU-5',15,0]],unique=['SKU'],checks=['UnitPrice >= 0','StockQuantity >= 0'],purpose='Product catalog and current selling price; order lines retain their historical price.')
retail_items=entity('OrderItems','OrderItemID',[col('OrderID','int','NOT NULL'),col('ProductID','int','NOT NULL'),col('Quantity','int','NOT NULL'),col('UnitPrice','decimal(12,2)','NOT NULL')],[[1,1,1,2,25],[2,1,2,5,10],[3,2,3,4,50],[4,3,3,4,50],[5,5,1,2,25],[6,6,3,6,50]],unique=['OrderID, ProductID'],checks=['Quantity > 0','UnitPrice >= 0'],fks=[ref('OrderID','Orders','OrderID'),ref('ProductID','Products','ProductID')],purpose='Bridge between orders and products; an order can have multiple lines.')
retail_payments=entity('Payments','PaymentID',[col('OrderID','int','NOT NULL'),col('PaymentReference','varchar(20)','NOT NULL'),col('PaidAmount','decimal(12,2)','NOT NULL'),col('PaymentDate','date','NOT NULL')],[[1,1,'PAY-1',60,'20240102'],[2,1,'PAY-2',40,'20240103'],[3,2,'PAY-3',200,'20240103'],[4,3,'PAY-4',100,'20240104'],[5,6,'PAY-5',300,'20240211']],unique=['PaymentReference'],checks=['PaidAmount > 0'],fks=[ref('OrderID','Orders','OrderID')],purpose='One order can have several payments, or none.')
MODELS.append(model('retail','Retail',['OrderID','CustomerID','OrderReference','SalesChannel','OrderStatus','OrderTotal','PackageCount','OrderDate','PlacedAt','RecordedAt','Note','BackupNote','ParentOrderID'],('Orders','Customers','CustomerName'),[retail_customer,retail_product,None,retail_items,retail_payments],'Track customers, products, orders, line items and payments. Reconcile line totals and payments without double-counting.'))

branches=entity('Branches','BranchID',[col('BranchName','nvarchar(80)','NOT NULL'),col('BranchCode','varchar(20)','NOT NULL'),col('City','nvarchar(50)','NOT NULL')],[[i,f'Branch {i}',f'BR-{i}',city] for i,city in enumerate(['Chicago','Austin','Boston','Denver','Seattle'],1)],unique=['BranchCode'],purpose='A branch services many accounts.')
bankcustomers=entity('Customers','CustomerID',[col('CustomerName','nvarchar(80)','NOT NULL'),col('Email','varchar(100)','NOT NULL')],[[i,f'Client {i}',f'client{i}@example.test'] for i in range(1,6)],unique=['Email'],purpose='A customer may own several accounts and loans.')
accounts=master('Accounts','AccountID','AccountName','Account-level servicing identity; each account belongs to one customer and branch.',extra=[col('CustomerID','int','NOT NULL'),col('BranchID','int','NOT NULL')],fks=[ref('CustomerID','Customers','CustomerID'),ref('BranchID','Branches','BranchID')])
loans=entity('Loans','LoanID',[col('CustomerID','int','NOT NULL'),col('AccountID','int','NOT NULL'),col('LoanReference','varchar(20)','NOT NULL'),col('Principal','decimal(12,2)','NOT NULL'),col('AnnualRate','decimal(5,2)','NOT NULL')],[[1,1,1,'LN-1',10000,5],[2,1,1,'LN-2',5000,6],[3,2,2,'LN-3',20000,4],[4,3,3,'LN-4',15000,7],[5,4,4,'LN-5',8000,8]],unique=['LoanReference'],checks=['Principal > 0','AnnualRate BETWEEN 0 AND 100'],fks=[ref('CustomerID','Customers','CustomerID'),ref('AccountID','Accounts','AccountID')],purpose='Loans reference a borrower and a servicing account; the simplified model permits a different servicing-account owner.')
MODELS.append(model('banking','Banking / Finance',['TransactionID','AccountID','Reference','TransactionType','Status','Amount','UnitCount','TransactionDate','PostedAt','RecordedAt','Note','BackupNote','ParentTransactionID'],('Transactions','Accounts','AccountName'),[branches,bankcustomers,accounts,None,loans],'Trace transactions to accounts, customers and branches, then summarize lending exposure without multiplying loan balances by transaction counts.'))

suppliers=master('Suppliers','SupplierID','SupplierName','Each supplier can supply multiple batches.')
phproducts=entity('Products','ProductID',[col('ProductName','nvarchar(80)','NOT NULL'),col('ProductCode','varchar(20)','NOT NULL'),col('StandardCost','decimal(12,2)','NOT NULL')],[[i,f'Compound {i}',f'PR-{i}',i*10] for i in range(1,6)],unique=['ProductCode'],checks=['StandardCost >= 0'],purpose='A product can be manufactured in many batches.')
warehouses=entity('Warehouses','WarehouseID',[col('WarehouseName','nvarchar(80)','NOT NULL'),col('WarehouseCode','varchar(20)','NOT NULL'),col('Capacity','int','NOT NULL')],[[i,f'Warehouse {i}',f'WH-{i}',100*i] for i in range(1,6)],unique=['WarehouseCode'],checks=['Capacity > 0'],purpose='Locations holding stock from several batches.')
inventory=entity('Inventory','InventoryID',[col('BatchID','int','NOT NULL'),col('WarehouseID','int','NOT NULL'),col('QuantityOnHand','int','NOT NULL'),col('LastCountDate','date','NOT NULL')],[[1,1,1,20,'20240105'],[2,1,2,30,'20240105'],[3,2,1,40,'20240105'],[4,3,3,10,'20240106'],[5,5,4,0,'20240205'],[6,6,2,50,'20240212']],unique=['BatchID, WarehouseID'],checks=['QuantityOnHand >= 0'],fks=[ref('BatchID','Batches','BatchID'),ref('WarehouseID','Warehouses','WarehouseID')],purpose='Bridge between batches and warehouses; one row per batch/location.')
MODELS.append(model('pharma','Pharma',['BatchID','SupplierID','BatchCode','BatchType','Status','BatchCost','PackCount','ManufactureDate','ProducedAt','RecordedAt','Note','BackupNote','ParentBatchID'],('Batches','Suppliers','SupplierName'),[suppliers,phproducts,warehouses,None,inventory],'Track product batches from suppliers to warehouse stock. Identify unstocked batches and zero-stock locations.'))

patients=master('Patients','PatientID','PatientName','Synthetic patients; one patient may have several encounters.')
doctors=entity('Doctors','DoctorID',[col('DoctorName','nvarchar(80)','NOT NULL'),col('LicenseNumber','varchar(20)','NOT NULL'),col('Specialty','varchar(30)','NOT NULL')],[[i,f'Doctor {i}',f'LIC-{i}',sp] for i,sp in enumerate(['General','Cardiology','General','Dermatology','Neurology'],1)],unique=['LicenseNumber'],purpose='One doctor is assigned to each encounter in this simplified teaching model.')
medications=entity('Medications','MedicationID',[col('MedicationName','nvarchar(80)','NOT NULL'),col('MedicationCode','varchar(20)','NOT NULL'),col('UnitCost','decimal(12,2)','NOT NULL')],[[i,f'Training medication {i}',f'MED-{i}',i*5] for i in range(1,6)],unique=['MedicationCode'],checks=['UnitCost >= 0'],purpose='Synthetic catalog for relational practice; no clinical dosing guidance.')
prescriptions=entity('Prescriptions','PrescriptionID',[col('EncounterID','int','NOT NULL'),col('MedicationID','int','NOT NULL'),col('PrescriptionReference','varchar(20)','NOT NULL'),col('Quantity','int','NOT NULL')],[[1,1,1,'RX-1',2],[2,1,2,'RX-2',3],[3,2,3,'RX-3',1],[4,3,1,'RX-4',2],[5,6,4,'RX-5',4]],unique=['PrescriptionReference'],checks=['Quantity > 0'],fks=[ref('EncounterID','Encounters','EncounterID'),ref('MedicationID','Medications','MedicationID')],purpose='A prescription links one encounter to one medication; multiple prescriptions may belong to an encounter.')
MODELS.append(model('healthcare','Healthcare',['EncounterID','PatientID','EncounterReference','EncounterType','Status','Charge','ServiceUnits','EncounterDate','StartedAt','RecordedAt','Note','BackupNote','ParentEncounterID'],('Encounters','Patients','PatientName'),[patients,doctors,medications,None,prescriptions],'Follow patients through encounters with doctors and medications prescribed. Report encounters without prescriptions and avoid repeated encounter charges.'))

sites=master('Sites','SiteID','SiteName','Origin sites dispatch many shipments.')
carriers=entity('Carriers','CarrierID',[col('CarrierName','nvarchar(80)','NOT NULL'),col('CarrierCode','varchar(20)','NOT NULL'),col('Active','bit','NOT NULL DEFAULT (1)')],[[i,f'Carrier {i}',f'CR-{i}',1 if i<5 else 0] for i in range(1,6)],unique=['CarrierCode'],purpose='Each shipment is assigned to one carrier.')
oilproducts=entity('Products','ProductID',[col('ProductName','nvarchar(80)','NOT NULL'),col('ProductCode','varchar(20)','NOT NULL'),col('PricePerUnit','decimal(12,2)','NOT NULL')],[[i,f'Grade {i}',f'OIL-{i}',i*20] for i in range(1,6)],unique=['ProductCode'],checks=['PricePerUnit >= 0'],purpose='Product catalog; shipment lines retain historical unit prices.')
shipmentitems=entity('ShipmentItems','ShipmentItemID',[col('ShipmentID','int','NOT NULL'),col('ProductID','int','NOT NULL'),col('Quantity','int','NOT NULL'),col('PricePerUnit','decimal(12,2)','NOT NULL')],[[1,1,1,3,20],[2,1,2,1,40],[3,2,2,5,40],[4,3,1,10,20],[5,6,3,5,60]],unique=['ShipmentID, ProductID'],checks=['Quantity > 0','PricePerUnit >= 0'],fks=[ref('ShipmentID','Shipments','ShipmentID'),ref('ProductID','Products','ProductID')],purpose='Bridge between shipments and oil products; one row per shipment/product combination.')
MODELS.append(model('oil','Oil',['ShipmentID','SiteID','ShipmentReference','ShipmentType','Status','ShipmentValue','UnitCount','ShipDate','DispatchedAt','RecordedAt','Note','BackupNote','ParentShipmentID'],('Shipments','Sites','SiteName'),[sites,carriers,oilproducts,None,shipmentitems],'Track origin sites, carriers, shipments and product lines; reconcile shipment values and identify missing detail.'))

# Retail supply chain (Maple & Main Supply Chain): buy or make products, move stock and reconcile balances.
# Replaces the former Retail Inventory and Retail Manufacturing projects; nine connected tables.
sc_warehouses=master('Warehouses','WarehouseID','WarehouseName','Fulfillment centers and store depots; each warehouse has stock movements and balances and receives private label production.')
sc_suppliers=entity('Suppliers','SupplierID',[col('SupplierName','nvarchar(80)','NOT NULL'),col('SupplierCode','varchar(20)','NOT NULL'),col('LeadTimeDays','int','NOT NULL')],[[1,'Supply chain supplier 1','SC-SUP-1',2],[2,'Supply chain supplier 2','SC-SUP-2',3],[3,'Supply chain supplier 3','SC-SUP-3',4],[4,'Private Label Plant','SC-SUP-4',1],[5,'Unused supplier','SC-SUP-5',6]],unique=['SupplierCode'],checks=['LeadTimeDays >= 0'],purpose='Where stock comes from. Supplier 4 is the in-house Private Label plant, the source of every Made product.')
sc_products=entity('Products','ProductID',[col('ProductName','nvarchar(80)','NOT NULL'),col('SKU','varchar(20)','NOT NULL'),col('UnitCost','decimal(12,2)','NOT NULL'),col('Sourcing','varchar(10)',"NOT NULL DEFAULT ('Bought')")],[[1,'Notebook','SC-SKU-1',10,'Bought'],[2,'Pen set','SC-SKU-2',4,'Bought'],[3,'Canvas tote','SC-SKU-3',15,'Made'],[4,'Travel pouch','SC-SKU-4',16,'Made'],[5,'Unused product','SC-SKU-5',8,'Bought']],unique=['SKU'],checks=['UnitCost > 0',"Sourcing IN ('Bought','Made')"],purpose='One catalog: Bought products come from outside suppliers; Made products are produced in the Private Label plant from a recipe.')
sc_materials=entity('Materials','MaterialID',[col('MaterialName','nvarchar(80)','NOT NULL'),col('MaterialCode','varchar(20)','NOT NULL'),col('UnitCost','decimal(12,2)','NOT NULL')],[[i,name,f'SC-MAT-{i}',cost] for i,name,cost in [(1,'Fabric',5),(2,'Thread',1),(3,'Zipper',2),(4,'Packaging',3),(5,'Unused trim',4)]],unique=['MaterialCode'],checks=['UnitCost > 0'],purpose='Raw materials for Made products. Quantities are in the material-specific unit.')
sc_bom=entity('BillOfMaterials','BOMID',[col('ProductID','int','NOT NULL'),col('MaterialID','int','NOT NULL'),col('QuantityPerUnit','decimal(12,2)','NOT NULL')],[[1,3,1,2],[2,3,2,1],[3,4,1,1],[4,4,3,2],[5,4,4,1]],unique=['ProductID, MaterialID'],checks=['QuantityPerUnit > 0'],fks=[ref('ProductID','Products','ProductID'),ref('MaterialID','Materials','MaterialID')],purpose='Recipe bridge: one row per Made product and required material, per unit produced.')
sc_production=entity('ProductionOrders','ProductionOrderID',[col('ProductID','int','NOT NULL'),col('WarehouseID','int','NOT NULL'),col('ProductionReference','varchar(20)','NOT NULL'),col('ProductionStatus','varchar(12)','NOT NULL'),col('PlannedUnits','int','NOT NULL'),col('PlannedCost','decimal(12,2)','NOT NULL'),col('StartDate','date','NOT NULL'),col('CompletedDate','date','NULL')],[[1,3,2,'PO-1','Completed',10,110,'20231220','20231230'],[2,4,1,'PO-2','Completed',5,60,'20231222','20231229'],[3,3,3,'PO-3','InProgress',8,88,'20240201',None],[4,4,4,'PO-4','Planned',6,72,'20240301',None]],unique=['ProductionReference'],checks=["ProductionStatus IN ('Planned','InProgress','Completed')",'PlannedUnits > 0','PlannedCost >= 0','CompletedDate IS NULL OR CompletedDate >= StartDate'],fks=[ref('ProductID','Products','ProductID'),ref('WarehouseID','Warehouses','WarehouseID')],purpose='Factory runs for Made products. PlannedCost is the recipe material cost; finished units are received into WarehouseID.')
sc_usage=entity('MaterialUsage','UsageID',[col('ProductionOrderID','int','NOT NULL'),col('MaterialID','int','NOT NULL'),col('QuantityUsed','decimal(12,2)','NOT NULL'),col('UsageDate','date','NOT NULL')],[[1,1,1,20,'20231221'],[2,1,2,10.5,'20231221'],[3,2,1,5,'20231223'],[4,2,3,10,'20231223'],[5,2,4,5,'20231223'],[6,3,1,8,'20240202']],unique=['ProductionOrderID, MaterialID'],checks=['QuantityUsed > 0'],fks=[ref('ProductionOrderID','ProductionOrders','ProductionOrderID'),ref('MaterialID','Materials','MaterialID')],purpose='Actual material consumed per production order and material; compare it with the recipe.')
sc_balances=entity('StockBalances','BalanceID',[col('WarehouseID','int','NOT NULL'),col('ProductID','int','NOT NULL'),col('OpeningQuantity','int','NOT NULL'),col('QuantityOnHand','int','NOT NULL'),col('ReorderLevel','int','NOT NULL')],[],unique=['WarehouseID, ProductID'],checks=['OpeningQuantity >= 0','QuantityOnHand >= 0','ReorderLevel >= 0'],fks=[ref('WarehouseID','Warehouses','WarehouseID'),ref('ProductID','Products','ProductID')],purpose='One snapshot per warehouse and product: opening stock plus the signed seed movements equals QuantityOnHand. No trigger updates it automatically.')
sc=model('retail_supply_chain','Retail Supply Chain',['MovementID','WarehouseID','MovementReference','MovementCategory','Status','MovementValue','MovedUnits','MovementDate','MovedAt','RecordedAt','Note','BackupNote','ParentMovementID'],('StockMovements','Warehouses','WarehouseName'),[sc_warehouses,sc_suppliers,sc_products,sc_materials,sc_bom,sc_production,sc_usage,None,sc_balances],'Buy or make products, move stock through warehouses, and reconcile production, receipts, dispatches and balances.')
sc['extra_fks']=[('ProductID','Products','ProductID'),('SupplierID','Suppliers','SupplierID')]
sc['focus']=['Warehouses','Products','ProductionOrders','StockMovements','StockBalances']
MODELS.append(sc)

# Retail logistics: customers, carriers, shipments, packages and scan history.
lg_customers=master('Customers','CustomerID','CustomerName','Customers request retail deliveries; one customer may have many shipments.')
lg_carriers=entity('Carriers','CarrierID',[col('CarrierName','nvarchar(80)','NOT NULL'),col('CarrierCode','varchar(20)','NOT NULL'),col('ServiceLevel','varchar(20)','NOT NULL')],[[i,f'Logistics carrier {i}',f'LOG-{i}','Express' if i%2 else 'Standard'] for i in range(1,6)],unique=['CarrierCode'],purpose='Delivery partners; each shipment is assigned to one carrier.')
packages=entity('ShipmentPackages','PackageID',[col('ShipmentID','int','NOT NULL'),col('TrackingNumber','varchar(20)','NOT NULL'),col('WeightKg','decimal(12,2)','NOT NULL'),col('PromisedDate','date','NOT NULL')],[[1,1,'TRK-1',2,'20240103'],[2,1,'TRK-2',3,'20240103'],[3,2,'TRK-3',1,'20240104'],[4,3,'TRK-4',4,'20240104'],[5,6,'TRK-5',2,'20240212']],unique=['TrackingNumber'],checks=['WeightKg > 0'],fks=[ref('ShipmentID','Shipments','ShipmentID')],purpose='Physical parcels with individual tracking numbers and promised delivery dates.')
tracking=entity('TrackingEvents','TrackingEventID',[col('PackageID','int','NOT NULL'),col('ScanReference','varchar(20)','NOT NULL'),col('EventStatus','varchar(20)','NOT NULL'),col('ScanTime','datetime2(3)','NOT NULL'),col('LocationName','nvarchar(80)','NOT NULL')],[[1,1,'SCAN-1','PickedUp','2024-01-01T13:00:00','Origin hub'],[2,1,'SCAN-2','Delivered','2024-01-03T10:00:00','Customer address'],[3,2,'SCAN-3','InTransit','2024-01-02T09:00:00','Regional hub'],[4,3,'SCAN-4','Delivered','2024-01-05T11:00:00','Customer address'],[5,4,'SCAN-5','PickedUp','2024-01-03T08:00:00','Origin hub']],unique=['ScanReference'],checks=["EventStatus IN ('PickedUp','InTransit','Delivered')"],fks=[ref('PackageID','ShipmentPackages','PackageID')],purpose='Append-only package scan history; select the latest scan rather than counting it as another package.')
lg=model('retail_logistics','Retail Logistics',['ShipmentID','CustomerID','ShipmentReference','ShipmentCategory','Status','FreightCharge','DeclaredPackages','ShipDate','DispatchedAt','RecordedAt','Note','BackupNote','ParentShipmentID'],('Shipments','Customers','CustomerName'),[lg_customers,lg_carriers,None,packages,tracking],'Follow customer shipments through carriers, parcels and tracking events. Find missing scans and late deliveries without multiplying freight charges.')
lg['extra_fks']=[('CarrierID','Carriers','CarrierID')]
MODELS.append(lg)

# E-commerce (Everyday Bazaar): a high-volume online marketplace; six connected tables.
ec_customers=master('Customers','CustomerID','CustomerName','Shoppers; one customer can place many orders, and heavy buyers order almost every week.')
ec_sellers=entity('Sellers','SellerID',[col('SellerName','nvarchar(80)','NOT NULL'),col('SellerCode','varchar(20)','NOT NULL'),col('Department','varchar(20)','NOT NULL')],[[1,'Seller 1','SEL-1','Electronics'],[2,'Seller 2','SEL-2','Home & Kitchen'],[3,'Seller 3','SEL-3','Fashion'],[4,'Seller 4','SEL-4','Books'],[5,'Unused seller','SEL-5','Toys & Games']],unique=['SellerCode'],purpose='Third-party sellers; each sells in one department and fulfils its own orders.')
ec_products=entity('Products','ProductID',[col('ProductName','nvarchar(80)','NOT NULL'),col('SKU','varchar(20)','NOT NULL'),col('UnitPrice','decimal(12,2)','NOT NULL'),col('Department','varchar(20)',"NOT NULL DEFAULT ('General')")],[[1,'Wireless earbuds','EB-SKU-1',25,'Electronics'],[2,'USB-C charger','EB-SKU-2',10,'Electronics'],[3,'French press','EB-SKU-3',50,'Home & Kitchen'],[4,'Rain jacket','EB-SKU-4',40,'Fashion'],[5,'Unused product','EB-SKU-5',15,'Books']],unique=['SKU'],checks=['UnitPrice > 0'],purpose='Catalog listing price; the price actually charged is kept on each order item.')
ec_items=entity('OrderItems','OrderItemID',[col('OrderID','int','NOT NULL'),col('ProductID','int','NOT NULL'),col('Quantity','int','NOT NULL'),col('UnitPrice','decimal(12,2)','NOT NULL')],[[1,1,1,2,25],[2,1,2,5,10],[3,2,3,4,50],[4,3,4,5,40],[5,5,1,2,25],[6,6,3,6,50]],unique=['OrderID, ProductID'],checks=['Quantity > 0','UnitPrice >= 0'],fks=[ref('OrderID','Orders','OrderID'),ref('ProductID','Products','ProductID')],purpose='Lines of an order; UnitPrice is the price charged, after any deal discount.')
ec_payments=entity('Payments','PaymentID',[col('OrderID','int','NOT NULL'),col('PaymentMethod','varchar(10)','NOT NULL'),col('PaidAmount','decimal(12,2)','NOT NULL'),col('PaidAt','datetime2(3)','NOT NULL')],[[1,1,'GiftCard',40,'2024-01-01T12:31:00'],[2,1,'Card',60,'2024-01-01T12:31:04'],[3,2,'Wallet',200,'2024-01-02T12:31:00'],[4,3,'Card',100,'2024-01-02T12:32:00'],[5,6,'COD',300,'2024-02-13T10:00:00']],checks=["PaymentMethod IN ('Card','Wallet','GiftCard','COD')",'PaidAmount > 0'],fks=[ref('OrderID','Orders','OrderID')],purpose='Payments per order: an order can be split between a gift card and a card, or be unpaid.')
ec=model('ecommerce','E-commerce',['OrderID','CustomerID','OrderReference','SalesChannel','OrderStatus','OrderTotal','ItemCount','OrderDate','PlacedAt','RecordedAt','Note','BackupNote','ParentOrderID'],('Orders','Customers','CustomerName'),[ec_customers,ec_sellers,ec_products,None,ec_items,ec_payments],'Run a marketplace with tens of thousands of orders a year: daily volume, sellers, order lines and split payments, reconciled without double-counting.')
ec['extra_fks']=[('SellerID','Sellers','SellerID')]
ec['focus']=['Customers','Sellers','Products','Orders','OrderItems']
MODELS.append(ec)

clients=entity('Clients','ClientID',[col('ClientName','nvarchar(80)','NOT NULL'),col('ClientReference','varchar(20)','NOT NULL'),col('Email','varchar(100)','NOT NULL')],[[i,f'Investor {i}',f'CLIENT-{i}',f'investor{i}@example.test'] for i in range(1,6)],unique=['ClientReference','Email'],purpose='Synthetic individual brokerage clients; each can hold multiple accounts.')
securities=entity('Securities','SecurityID',[col('SecurityName','nvarchar(80)','NOT NULL'),col('Symbol','varchar(20)','NOT NULL'),col('AssetClass','varchar(10)','NOT NULL')],[[1,'Training Equity Alpha','DEMO-A','Stock'],[2,'Training Equity Beta','DEMO-B','Stock'],[3,'Training Fund Gamma','DEMO-C','ETF'],[4,'Training Fund Delta','DEMO-D','ETF'],[5,'Unused Training Equity','DEMO-E','Stock']],unique=['Symbol'],checks=["AssetClass IN ('Stock','ETF')"],purpose='Fictitious stock and ETF instruments with unique symbols.')
br_accounts=entity('BrokerageAccounts','AccountID',[col('AccountName','nvarchar(80)','NOT NULL'),col('AccountNumber','varchar(20)','NOT NULL'),col('Region','varchar(10)','NOT NULL'),col('ClientID','int','NOT NULL')],[[i,f'BrokerageAccounts {name}',f'ACC-{i}',region,i] for i,name,region in [(1,'Alpha','North'),(2,'Beta','South'),(3,'Gamma','North'),(4,'Delta','West'),(5,'Unused','East')]],unique=['AccountNumber'],fks=[ref('ClientID','Clients','ClientID')],purpose='Each brokerage account belongs to one client; Region is the servicing region.')
executions=entity('Executions','ExecutionID',[col('OrderID','int','NOT NULL'),col('ExecutionReference','varchar(20)','NOT NULL'),col('ExecutedQuantity','decimal(12,4)','NOT NULL'),col('ExecutionPrice','decimal(12,4)','NOT NULL'),col('ExecutedAt','datetime2(3)','NOT NULL')],[[1,1,'FILL-1',0.4,100,'2024-01-01T12:31:00'],[2,1,'FILL-2',0.6,101,'2024-01-01T12:32:00'],[3,2,'FILL-3',1,99,'2024-01-02T12:31:00'],[4,2,'FILL-4',0.5,100,'2024-01-02T12:32:00'],[5,3,'FILL-5',3,101,'2024-01-02T12:33:00'],[6,6,'FILL-6',1,150,'2024-02-10T12:31:00']],unique=['ExecutionReference'],checks=['ExecutedQuantity > 0','ExecutionPrice > 0'],fks=[ref('OrderID','TradeOrders','OrderID')],purpose='Individual partial fills. Total fills must not exceed the requested order quantity; this cross-row rule is validated by reconciliation.')
br=model('brokerage','Brokerage',['OrderID','AccountID','OrderReference','RoutingCategory','WorkflowStatus','EstimatedValue','RequestedQuantity','OrderDate','SubmittedAt','RecordedAt','Note','BackupNote','ParentOrderID'],('TradeOrders','BrokerageAccounts','AccountName'),[clients,securities,br_accounts,None,executions],'Trace clients and accounts through securities, trade orders and partial executions. Reconcile filled quantities and weighted average execution prices.')
br['extra_fks']=[('SecurityID','Securities','SecurityID')]
br['source_note']='An independent, synthetic brokerage training model. Scope: buy orders for fictitious stocks and ETFs, including partial fills. Settlement, cash ledgers, positions, margin, taxes and options are outside this five-table model. WorkflowStatus is an administrative practice flag; derive fill status from requested and executed quantities.'
MODELS.append(br)

for m in MODELS:
    mp=m['map']; fact,party,pname=m['base']
    mp['PartyName']=pname
    types=['int','int','nvarchar(80)','varchar(10)','varchar(10)','decimal(12,2)','int','date','datetime2(3)','datetimeoffset(3)','nvarchar(100)','nvarchar(100)','int']
    logical=list(mp)[:13]
    columns=[col(mp[k],t,'NULL' if k in ['Amount','Note','BackupNote','ParentID'] else 'NOT NULL') for k,t in zip(logical,types)]
    rows=[]
    amounts=[100,200,200,None,50,300,0,150,300,80,120,200]
    parties=[1,1,2,2,3,3,4,4,4,4,1,2]
    dates=['20240101','20240102','20240102','20240103','20240201','20240210','20240229','20240301','20240310','20241103','20241231','20250101']
    labels=['  Alpha-One  ','beta-Two','Gamma-Three ',' Delta-Four','Echo-Five','ALPHA-Six','Zero-Seven','Review-Eight','Zulu-Nine','Iota-Ten','Kappa-Eleven','Last-Twelve']
    fks=[ref(mp['PartyID'],party,mp['PartyID']),ref(mp['ParentID'],fact,mp['RecordID'])]
    defaults={'pharma':[('ProductID','Products','ProductID')],'healthcare':[('DoctorID','Doctors','DoctorID')],'oil':[('CarrierID','Carriers','CarrierID')]}
    extras=m.get('extra_fks',defaults.get(m['slug'],[]))
    for extra in extras:
        columns.append(col(extra[0],'int','NOT NULL')); fks.append(ref(*extra))
    for i in range(12):
        iso=f'{dates[i][:4]}-{dates[i][4:6]}-{dates[i][6:]}'
        row=[i+1,parties[i],labels[i],['A','B','C'][i%3],['Open','Closed','Pending'][i%3],amounts[i],i%4+1,dates[i],iso+'T12:30:45.123',iso+'T12:30:45.123+00:00',None if i%3==0 else 'confirmed','backup' if i%2==0 else None,None if i==0 else (i+1)//2]
        for extra in extras: row.append(i%4+1)
        rows.append(row)
    facttable=entity(fact,mp['RecordID'],columns[1:],rows,unique=[mp['Label']],checks=[f"{mp['Category']} IN ('A','B','C')",f"{mp['Status']} IN ('Open','Closed','Pending')",f"{mp['Amount']} >= 0",f"{mp['Quantity']} > 0",f"{mp['ParentID']} IS NULL OR {mp['ParentID']} <> {mp['RecordID']}"],fks=fks,purpose='The main business event; linked to its master and optionally to a related earlier event. The parent link is for teaching hierarchy traversal, not a guarantee of an acyclic graph.')
    facttable['columns'][4]['rule']="NOT NULL DEFAULT ('Open')"
    m['tables'][m['tables'].index(None)]=facttable
    if m['slug']=='retail_supply_chain':
        facttable['columns'].append(col('Direction','varchar(3)','NOT NULL'))
        facttable['checks'].append("Direction IN ('IN','OUT')")
        for i,row in enumerate(facttable['rows']):row.append('OUT' if i%3==1 else 'IN')
        # Made products (3 and 4) come from the Private Label plant; movement 3 receives production order 1.
        names=[c['name'] for c in facttable['columns']]
        pi,si,di,qi=names.index('ProductID'),names.index('SupplierID'),names.index('Direction'),names.index(mp['Quantity'])
        for row in facttable['rows']:
            if row[pi] in (3,4):row[si]=4
        facttable['columns'].append(col('ProductionOrderID','int','NULL'))
        facttable['fks'].append(ref('ProductionOrderID','ProductionOrders','ProductionOrderID'))
        for row in facttable['rows']:row.append(1 if row[0]==3 else None)
        net={}
        for row in facttable['rows']:
            key=(row[1],row[pi]);net[key]=net.get(key,0)+(row[qi] if row[di]=='IN' else -row[qi])
        balances=next(t for t in m['tables'] if t['name']=='StockBalances')
        balances['rows']=[[i,w,p,10,10+n,10] for i,((w,p),n) in enumerate(sorted(net.items())+[((1,5),0)],1)]
    if m['slug']=='brokerage':
        facttable['columns'].append(col('Side','varchar(3)',"NOT NULL DEFAULT ('Buy')"))
        facttable['checks'].append("Side = 'Buy'")
        for row in facttable['rows']:row.append('Buy')
    for t in m['tables']:
        firsttext=next((c['name'] for c in t['columns'] if 'char' in c['type']),None)
        if firsttext:t['checks'].append(f'LEN(LTRIM(RTRIM({firsttext}))) > 0')

def qname(m,t): return f"[{m['slug']}].[{t if isinstance(t,str) else t['name']}]"
def literal(value):
    if value is None:return 'NULL'
    if isinstance(value,str): return "N'"+value.replace("'","''")+"'"
    return str(value)
def fkname(t,f):return f"FK_{t['name']}_{f['column']}"
def ddl(m,t):
    items=[f"[{c['name']}] {c['type']} {c['rule']}" for c in t['columns']]
    items.append(f"CONSTRAINT [PK_{t['name']}] PRIMARY KEY ([{t['key']}])")
    for i,u in enumerate(t['unique'],1):items.append(f"CONSTRAINT [UQ_{t['name']}_{i}] UNIQUE ({u})")
    for i,c in enumerate(t['checks'],1):items.append(f"CONSTRAINT [CK_{t['name']}_{i}] CHECK ({c})")
    for f in t['fks']:items.append(f"CONSTRAINT [{fkname(t,f)}] FOREIGN KEY ([{f['column']}]) REFERENCES {qname(m,f['parent'])} ([{f['key']}])")
    return f'CREATE TABLE {qname(m,t)} (\n    '+',\n    '.join(items)+'\n);'
def insert(m,t,rows=None):
    return f"INSERT INTO {qname(m,t)} ("+', '.join(c['name'] for c in t['columns'])+') VALUES\n'+',\n'.join('('+','.join(literal(v) for v in r)+')' for r in (rows or t['rows']))+';'
def transaction(body):
    return 'SET XACT_ABORT OFF;\nIF @@TRANCOUNT <> 0 THROW 51000, \'Use a fresh session with no open transaction\', 1;\nBEGIN TRANSACTION;\nBEGIN TRY\n'+body+'\nROLLBACK TRANSACTION;\nEND TRY\nBEGIN CATCH\n IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;\n THROW;\nEND CATCH;'

def table_brief(m,t):
    lines=[f"**{t['name']}** — {t['purpose']}",'','| Column | Type | Requirement |','|---|---|---|']
    for c in t['columns']:lines.append(f"| {c['name']} | {c['type']} | {c['rule'] or 'NULL allowed'} |")
    lines+=['',f"Primary key: **{t['key']}**."]
    for u in t['unique']:lines.append(f'Unique business key: **{u}**.')
    for c in t['checks']:lines.append(f'Business rule: `{c}`.')
    for f in t['fks']:lines.append(f"Foreign key: **{t['name']}.{f['column']} → {f['parent']}.{f['key']}**. Use NO ACTION on delete/update; do not disable checking.")
    return '\n'.join(lines)

def create_setup():
    (ROOT/'domains').mkdir(exist_ok=True)
    allsql=['-- Revised five-table projects. Use a NEW disposable database, not the old two-table fixture.', 'SET NOCOUNT ON;', 'SET XACT_ABORT ON;', 'BEGIN TRANSACTION;', 'BEGIN TRY']
    reset=[f'-- Drops only the {sum(len(m["tables"]) for m in MODELS)} named project tables. Deliberate reset in your training database only.', 'SET XACT_ABORT ON;','BEGIN TRANSACTION;','BEGIN TRY']
    verify=[f'-- Read-only baseline checks for the {sum(len(m["tables"]) for m in MODELS)}-table projects.', 'SET NOCOUNT ON;']
    for m in MODELS:
        s=m['slug']; directory=ROOT/'domains'/s;directory.mkdir(exist_ok=True)
        schema=f"IF SCHEMA_ID(N'{s}') IS NULL EXEC(N'CREATE SCHEMA [{s}] AUTHORIZATION dbo;');"
        guards=[f"IF OBJECT_ID(N'{s}.{t['name']}') IS NOT NULL THROW 51000, 'Project tables already exist: use a fresh database', 1;" for t in m['tables']]
        create=[ddl(m,t) for t in m['tables']]; seed=[insert(m,t) for t in m['tables']]
        allsql += [schema]+guards+create+seed
        (directory/'schema_solution.sql').write_text('-- Instructor schema answer. Execute in an empty training database.\nSET XACT_ABORT ON;\nBEGIN TRANSACTION;\nBEGIN TRY\n'+schema+'\n'+'\n'.join(guards+create)+'\nCOMMIT TRANSACTION;\nEND TRY\nBEGIN CATCH\n IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;\n THROW;\nEND CATCH;\n',encoding='utf-8')
        (directory/'seed.sql').write_text(f'-- Load only AFTER all {table_count(m)} tables are created; run once.\nSET XACT_ABORT ON;\nBEGIN TRANSACTION;\nBEGIN TRY\n'+'\n'.join(seed)+'\nCOMMIT TRANSACTION;\nEND TRY\nBEGIN CATCH\n IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;\n THROW;\nEND CATCH;\n',encoding='utf-8')
        for t in reversed(m['tables']): reset.append(f'DROP TABLE IF EXISTS {qname(m,t)};')
        for t in m['tables']:
            verify.append(f"IF (SELECT COUNT(*) FROM {qname(m,t)}) <> {len(t['rows'])} THROW 51000, '{s}.{t['name']}: row count mismatch', 1;")
            for f in t['fks']:
                verify.append(f"IF EXISTS (SELECT 1 FROM {qname(m,t)} c LEFT JOIN {qname(m,f['parent'])} p ON c.{f['column']}=p.{f['key']} WHERE c.{f['column']} IS NOT NULL AND p.{f['key']} IS NULL) THROW 51000, '{s}.{t['name']}: orphan reference', 1;")
        verify.append(f"IF EXISTS (SELECT 1 FROM sys.foreign_keys WHERE schema_id=SCHEMA_ID(N'{s}') AND (is_disabled=1 OR is_not_trusted=1)) THROW 51000, '{s}: untrusted foreign key', 1;")
        verify.append(f"IF (SELECT SUM({m['map']['Amount']}) FROM {qname(m,m['base'][0])}) <> 1700 THROW 51000, '{s}: amount total mismatch', 1;")
        verify.append(f"SELECT '{s}' AS Domain, 'PASS' AS FixtureCheck;")
    allsql+=['COMMIT TRANSACTION;','END TRY','BEGIN CATCH','IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;','THROW;','END CATCH;']
    reset+=['COMMIT TRANSACTION;','END TRY','BEGIN CATCH','IF @@TRANCOUNT>0 ROLLBACK TRANSACTION;','THROW;','END CATCH;']
    for name,lines in [('01_create_and_seed.sql',allsql),('02_reset_fixture.sql',reset),('03_verify_fixture.sql',verify)]:
        (ROOT/'setup'/name).write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (ROOT/'domain_models.json').write_text(json.dumps(MODELS,indent=2)+'\n',encoding='utf-8')

def fresh_row(t):
    values=list(t['rows'][0]);values[0]=100
    # Change non-FK business-key components; keep valid parent references.
    fkcols={f['column'] for f in t['fks']}
    for u in t['unique']:
        parts=[x.strip() for x in u.split(',')]
        chosen=next((x for x in parts if x not in fkcols),parts[-1])
        idx=next(i for i,c in enumerate(t['columns']) if c['name']==chosen)
        values[idx]='NEW-100' if isinstance(values[idx],str) else 5
    return values

NUMBER_WORDS={5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

def table_count(m):
    return NUMBER_WORDS.get(len(m['tables']),str(len(m['tables'])))

def build_steps(m):
    """Split every table into five dependency-ordered build steps (one table per step for five-table domains)."""
    n=len(m['tables']);sizes=[n//5+(1 if i<n%5 else 0) for i in range(5)];steps=[];start=0
    for size in sizes:
        steps.append(m['tables'][start:start+size]);start+=size
    return steps

def focus_tables(m):
    """The five tables used for per-table drills (Alter, Drop, DML and constraints)."""
    names=m.get('focus')
    return [t for t in m['tables'] if t['name'] in names] if names else list(m['tables'])

def create_prompt(m,t):
    qn=qname(m,t);key=t['key']
    lines=[f"Create the `{qn}` table with these columns:", '',
           '| Column | Data type | Constraints |', '|---|---|---|']
    for c in t['columns']:
        rules=[c['rule'] or 'NULL allowed']
        if c['name']==key: rules.append('PRIMARY KEY')
        if c['name'] in t['unique']: rules.append('UNIQUE')
        lines.append(f"| {c['name']} | {c['type']} | {'; '.join(rules)} |")
    rules=[]
    for u in t['unique']:
        if ',' in u: rules.append(f"Add UNIQUE on (`{u}`) together.")
    for check in t['checks']:
        rules.append(f"Add CHECK (`{check}`).")
    for fk in t['fks']:
        rules.append(f"Add a FOREIGN KEY from `{fk['column']}` to `[{m['slug']}].[{fk['parent']}]({fk['key']})`.")
    if rules:
        lines+=['', 'Add these constraints:', '']+[f'{i}. {rule}' for i,rule in enumerate(rules,1)]
    if t['fks']:
        lines+=['', 'For foreign keys, use NO ACTION on delete and update.']
    return lines

def relational_lessons(add,domains):
    for v in range(5):
        for d,m in zip(domains,MODELS):
            group=build_steps(m)[v]
            link=f"[the {m['title']} project brief](../domains/{m['slug']}/README.md)"
            lines=[]
            for t in group:
                if lines: lines+=['', '---', '']
                lines+=create_prompt(m,t)
            if v==0:
                lines+=['', f"Before creating {'this table' if len(group)==1 else 'these tables'}, create the `{m['slug']}` schema if it does not exist. A schema groups related tables."]
            if len(m['tables'])==5:
                lines+=['', f"Table {v+1} of 5. Create the tables in the order listed. Keep them for the next exercises."]
            else:
                lines+=['', f"Step {v+1} of 5 ({len(m['tables'])} tables in all). Create the tables in the order listed. Keep them for the next exercises."]
            prompt='\n'.join(lines)
            sql=(f"IF SCHEMA_ID(N'{m['slug']}') IS NULL EXEC(N'CREATE SCHEMA [{m['slug']}] AUTHORIZATION dbo;');\n" if v==0 else '')+'\n'.join(ddl(m,t) for t in group)
            check=' '.join(f"{t['name']} exists with PK {t['key']}, {len(t['fks'])} FK(s), {len(t['unique'])} UNIQUE rule(s) and {len(t['checks'])} CHECK rule(s)." for t in group)
            add('DDL','Create',d,v,prompt,sql,check[:-1]+'. Use the metadata checks in the project brief; matching column names alone is insufficient.')
            t=focus_tables(m)[v];qn=qname(m,t);key=t['key'];name=t['name']
            textcol=next((c for c in t['columns'] if 'char' in c['type']),t['columns'][1])
            changes=[('add nullable ContactPhone varchar(30)',f'ALTER TABLE {qn} ADD ContactPhone varchar(30) NULL;'),
                     (f"widen {textcol['name']} to nvarchar(120) while keeping NOT NULL",f"ALTER TABLE {qn} ALTER COLUMN {textcol['name']} nvarchar(120) NOT NULL;"),
                     ('add nullable AuditNote nvarchar(200)',f'ALTER TABLE {qn} ADD AuditNote nvarchar(200) NULL;'),
                     ('add Reviewed bit NOT NULL with DEFAULT(0), populating existing rows',f'ALTER TABLE {qn} ADD Reviewed bit NOT NULL DEFAULT(0) WITH VALUES;'),
                     ('add nullable ExternalReference varchar(30), widen it to varchar(60), then remove only that column',f'ALTER TABLE {qn} ADD ExternalReference varchar(30) NULL;\nALTER TABLE {qn} ALTER COLUMN ExternalReference varchar(60) NULL;\nALTER TABLE {qn} DROP COLUMN ExternalReference;')]
            change,alter=changes[v]
            # Widening a column used in UNIQUE/CHECK can be blocked; choose a non-key text column.
            if v==1:
                textcol=next(c for c in t['columns'] if 'char' in c['type'] and not any(c['name'] in u.split(', ') for u in t['unique']))
                related=[(i,c) for i,c in enumerate(t['checks'],1) if re.search(r'\b'+textcol['name']+r'\b',c)]
                prefix='\n'.join(f'ALTER TABLE {qn} DROP CONSTRAINT [CK_{name}_{i}];' for i,_ in related)
                suffix='\n'.join(f'ALTER TABLE {qn} WITH CHECK ADD CONSTRAINT [CK_{name}_{i}] CHECK ({c});' for i,c in related)
                change=f"widen {textcol['name']} to nvarchar(120), preserving NOT NULL and all its CHECK rules; temporarily drop and re-create dependent CHECK constraints if needed"
                alter=prefix+f'\nALTER TABLE {qn} ALTER COLUMN {textcol["name"]} nvarchar(120) NOT NULL;\n'+suffix
            add('DDL','Alter',d,v,f'**{m["title"]}: Change the {name} table**\n\nUse `{qn}` and the sample rows you added earlier.\n\n2. Make this change: {change}.\n3. Check the column settings and rows. You can use `sp_help` to see the table settings.',transaction(alter+f"\nEXEC sys.sp_help N'{m['slug']}.{name}';"),'Column definitions meet the change request; keys and foreign keys remain valid. Rollback restores the original schema and all rows.')
            incoming=[(other,f) for other in m['tables'] if other!=t for f in other['fks'] if f['parent']==name]
            drop='\n'.join(f'ALTER TABLE {qname(m,other)} DROP CONSTRAINT [{fkname(other,f)}];' for other,f in incoming)
            drop+=f"\nDROP TABLE {qn};\nSELECT OBJECT_ID(N'{m['slug']}.{name}') AS RemovedObjectID;"
            add('DDL','Drop',d,v,f'**{m["title"]}: Practice removing the {name} table**\n\nUse a separate practice copy of the tables and sample rows for this exercise.\n\n2. Find the foreign keys in other tables that point to `{qn}`. Remove those links, but keep the other tables.\n3. Use DROP TABLE to remove only `{qn}`. Check that it no longer exists.\n\n**Explain:** How is removing a table different from deleting rows inside it?',transaction(drop),f"RemovedObjectID is NULL inside the transaction. Incoming FK count={len(incoming)}. After rollback, the table, its data and all removed FKs exist again. Dropping a table also drops its own outgoing/self FK constraints.")
            vals=fresh_row(t)
            add('DML','Insert',d,v,f'**{m["title"]}: Add a row to {name}**\n\nUse `{qn}` and your earlier sample data.\n\n**Columns, in order:** `{", ".join(c["name"] for c in t["columns"])}`\n\n**Values, in the same order:** `{", ".join(literal(x) for x in vals)}`\n\n2. Insert the new row using the columns and values above.\n3. Immediately run `SELECT @@ROWCOUNT` to see how many rows were added.\n4. Display the new row where `{key} = 100`.\n\n**Explain:** For each foreign key, which existing row does the new row link to?',transaction(insert(m,t,[vals])+f'\nSELECT @@ROWCOUNT AS InsertedRows;\nSELECT * FROM {qn} WHERE {key}=100;'),'InsertedRows=1 and the new row matches every supplied value. The same insert must fail if repeated before rollback because the PK already exists.')
            candidate=next((c for c in t['columns'][1:] if c['type'] in ['int','decimal(12,2)'] and c['name'] not in {f['column'] for f in t['fks']}),textcol)
            field=candidate['name'];expr=f'{field}+1' if candidate['type'] in ['int','decimal(12,2)'] else "N'Revised name'"
            add('DML','Update',d,v,f'**{m["title"]}: Change one row in {name}**\n\nUse `{qn}` and your earlier sample data.\n\n1. Display the row where `{key} = 1`.\n3. Change only this row. Set `{field}` to `{expr}`.\n4. Immediately run `SELECT @@ROWCOUNT`. It should show 1 changed row.\n5. Display the row again to see the change.\n\n**Explain:** What could happen if you leave out the WHERE condition?',transaction(f'SELECT * FROM {qn} WHERE {key}=1;\nUPDATE {qn} SET {field}={expr} WHERE {key}=1;\nSELECT @@ROWCOUNT AS UpdatedRows;\nSELECT * FROM {qn} WHERE {key}=1;'),'UpdatedRows=1. Only the requested column changes and all constraints remain satisfied. Rollback restores the original value.')
            add('DML','Delete',d,v,f'**{m["title"]}: Delete a practice row from {name}**\n\nUse `{qn}` and your earlier sample data.\n\n**New row values:** `{", ".join(literal(x) for x in vals)}`. Use the column order in your domain guide.\n\n2. Insert the new row above with `{key} = 100`.\n3. Delete only that row. Keep the original sample rows.\n4. Immediately run `SELECT @@ROWCOUNT` to check that 1 row was deleted.\n5. Search for `{key} = 100` again. You should find no row. Check that the original {len(t["rows"])} rows are still there. Keep the foreign key rules turned on.',transaction(insert(m,t,[vals])+f'\nDELETE FROM {qn} WHERE {key}=100;\nSELECT @@ROWCOUNT AS DeletedRows;\nSELECT COUNT(*) AS OriginalRowCount FROM {qn};\nSELECT * FROM {qn} WHERE {key}=100;'),f'DeletedRows=1; original count={len(t["rows"])}; the final ID=100 query is empty. A referenced original parent would require a different deletion plan.')
            def inspect(t):
                return f"SELECT c.name, TYPE_NAME(c.user_type_id) AS TypeName, c.max_length, c.is_nullable FROM sys.columns c WHERE c.object_id=OBJECT_ID(N'{m['slug']}.{t['name']}') ORDER BY c.column_id;\nSELECT name, is_disabled, is_not_trusted FROM sys.foreign_keys WHERE parent_object_id=OBJECT_ID(N'{m['slug']}.{t['name']}');"
            names=' and '.join(t['name'] for t in group)
            if len(group)==1:
                t=group[0]
                add('DATA_SETUP','Create tables',d,v,f'{m["title"]}: After building {t["name"]} from the DDL Create assignment, verify its column types/nullability and FK metadata using sys.columns and sys.foreign_keys. Compare with {link}; identify its primary key and insert dependencies.',inspect(t),f'{len(t["columns"])} columns, {len(t["fks"])} foreign keys, all enabled and trusted. This verifies the already-created table; do not create a second copy.')
                add('DATA_SETUP','Insert data into the tables',d,v,f'{m["title"]}: Load the {len(t["rows"])} sample rows for {t["name"]} from {link} into the EMPTY table, after loading its parent tables. Use explicit column lists. Keep the data for DQL, joins and the capstone. Verify count and key values; do not run this if the complete seed script was already used.',insert(m,t)+f'\nSELECT COUNT(*) AS LoadedRows FROM {qname(m,t)};\nSELECT * FROM {qname(m,t)} ORDER BY {t["key"]};',f'LoadedRows={len(t["rows"])}. PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.')
            else:
                add('DATA_SETUP','Create tables',d,v,f'{m["title"]}: After building {names} from the DDL Create assignment, verify each table\'s column types/nullability and FK metadata using sys.columns and sys.foreign_keys. Compare with {link}; identify each primary key and insert dependencies.','\n'.join(inspect(t) for t in group),' '.join(f'{t["name"]}: {len(t["columns"])} columns, {len(t["fks"])} foreign keys.' for t in group)+' All foreign keys are enabled and trusted. This verifies the already-created tables; do not create second copies.')
                add('DATA_SETUP','Insert data into the tables',d,v,f'{m["title"]}: Load the sample rows for {names} ('+', '.join(f'{len(t["rows"])} rows' for t in group)+f') from {link} into the EMPTY tables, in that order and after loading their parent tables. Use explicit column lists. Keep the data for DQL, joins and the capstone. Verify counts and key values; do not run this if the complete seed script was already used.','\n'.join(insert(m,t)+f'\nSELECT COUNT(*) AS LoadedRows FROM {qname(m,t)};\nSELECT * FROM {qname(m,t)} ORDER BY {t["key"]};' for t in group),' '.join(f'{t["name"]} LoadedRows={len(t["rows"])}.' for t in group)+' PKs are unique and every non-NULL FK has a matching parent. A repeated load fails rather than silently duplicating data.')

def rejection(sql,error):
    return f"BEGIN TRY\n {sql}\n THROW 51001, 'Invalid value was unexpectedly accepted', 1;\nEND TRY\nBEGIN CATCH\n IF ERROR_NUMBER()<>{error} THROW;\n SELECT ERROR_NUMBER() AS ExpectedError;\nEND CATCH;"

def constraint_lessons(add,domains):
    for sub in ['Not Null','Unique','Check','Primary key','Foreign key']:
        for v in range(5):
            for d,m in zip(domains,MODELS):
                t=focus_tables(m)[v];qn=qname(m,t);key=t['key']
                if sub=='Foreign key':
                    edges=[(table,f) for table in m['tables'] for f in table['fks']]
                    t,f=edges[v];qn=qname(m,t);key=t['key'];column=f['column']
                    bad=f'UPDATE {qn} SET {column}=999 WHERE {key}=1;'
                    description=f"Try to change `{column}` to `999` in the row where `{key} = 1`. There is no row with `{f['key']} = 999` in `{f['parent']}`. Keep the foreign key rule turned on."
                    why=f"Why must `{column}` match a value in `{f['parent']}.{f['key']}`?"
                    err=547
                elif sub=='Not Null':
                    column=next(c['name'] for c in t['columns'][1:] if c['rule'].startswith('NOT NULL'))
                    bad=f'UPDATE {qn} SET {column}=NULL WHERE {key}=1;'
                    description=f'Try to change `{column}` to `NULL` in the row where `{key} = 1`. NULL means no value; it is different from an empty text value.';err=515
                    why=f'Why should every row in `{t["name"]}` have a value for `{column}`?'
                elif sub=='Primary key':
                    bad=insert(m,t,[list(t['rows'][0])]);err=2627
                    description=f'Try to add another copy of the row where `{key} = 1`. Keep the same `{key}` value in the new row.'
                    why=f'Why can two rows not have the same primary key value in `{key}`?'
                elif sub=='Unique':
                    values=list(t['rows'][0]);values[0]=100;bad=insert(m,t,[values]);err=2627
                    description=f"Try to add a copy of row 1, but change only `{key}` to `100`. Leave the other values the same. The UNIQUE rule on `{t['unique'][0]}` does not allow those values to be repeated."
                    why=f"Why is a new `{key}` value not enough when `{t['unique'][0]}` must also be unique?"
                else:
                    check=t['checks'][0]
                    if check.startswith('LEN('):
                        column=re.search(r'RTRIM\((\w+)\)',check)[1];value="N'   '"
                    else:
                        column=check.split()[0];value="'INVALID'" if ' IN ' in check else '-1'
                    bad=f'UPDATE {qn} SET {column}={value} WHERE {key}=1;';err=547
                    description=f'This table has the rule `{check}`. Try to change `{column}` to `{value}` in the row where `{key} = 1`.'
                    why='What does this CHECK rule allow? How is it different from NOT NULL, which requires a value?'
                before=f'SELECT * FROM {qn} WHERE {key}=1;'
                sql=transaction(before+'\n'+rejection(bad,err)+'\n'+before)
                original=''
                if sub=='Not Null':
                    idx=next(i for i,c in enumerate(t['columns']) if c['name']==column)
                    original=f" In the supplied sample data, `{column}` is `{t['rows'][0][idx]}`."
                prompt=f'**{m["title"]}: Practice {sub.upper()} on {t["name"]}**\n\n**Before you start:** Use `{qn}` and the sample rows you added earlier. If you have not added them yet, follow [your domain guide](../domains/{m["slug"]}/README.md).\n\n1. Display the row where `{key} = 1` and note its values.{original}\n3. {description}\n4. Write down the error message SQL Server shows. An error is expected in this exercise.\n5. Display the original row again. Check that its values have not changed.\n\n**Explain:** {why}\n\n**Submit:** Your SQL, the error message, and the row shown before and after the attempt.'
                add('CONSTRAINTS',sub,d,v,prompt,sql,f'SQL Server should show error {err}. The invalid value or extra row should not be saved. The original row should still have the same values. Explain the rule in your own words.')

def remap_library(records):
    """Give technique drills the same domain-specific columns as the projects."""
    for r in records:
        m=next(m for m in MODELS if m['title']==r['domain'])
        if r['topic'] in ['DDL','DML','CONSTRAINTS','DATA_SETUP']:continue
        mp=m['map']
        pattern=r'\b('+'|'.join(sorted(mp,key=len,reverse=True))+r')\b'
        for field in ['prompt','sql','check','answer']:
            r[field]=re.sub(pattern,lambda match:mp[match[0]],r[field])
        r['prompt'] = clarify_question(r, m)
        # Assertions affected by replacing invalid master references with enforced FKs.
        r['check']=r['check'].replace('INNER=10; LEFT=RIGHT=11','INNER=12; LEFT=RIGHT=13').replace('10 rows; equivalent','12 rows; equivalent')
        if r['topic']=='DATATYPES' and r['subtopic']=='CURSOR':
            r['check']=r['check'].replace('SetBasedCount = 1.', 'SetBasedCount = 0.') if 'IS NULL' in r['sql'] and mp['PartyID'] in r['sql'] else r['check']
        if r['topic']=='DATABASE_SCHEMA_USER' and r['subtopic']=='Schema' and 'List the tables' in r['prompt']:
            r['check']='Tables: '+', '.join(t['name'] for t in m['tables'])+'.'

def project_reports(m):
    s=m['slug'];mp=m['map'];fact,master,pname=m['base'];f=qname(m,fact);p=qname(m,master);pk=mp['RecordID'];fk=mp['PartyID'];amt=mp['Amount']
    reports=[
        ('Master activity',f'Return each {master} ID and name, including masters with no {fact}, with the count of related events and total known {amt}. Order by master ID.',f'SELECT p.{fk}, p.{pname}, COUNT(f.{pk}) AS EventCount, SUM(f.{amt}) AS TotalAmount FROM {p} p LEFT JOIN {f} f ON p.{fk}=f.{fk} GROUP BY p.{fk}, p.{pname} ORDER BY p.{fk};','Five master rows; master 5 has count 0 and NULL total; all counts sum to 12 and known totals sum to 1700.'),
        ('No activity',f'Return {master} with no related {fact} using NOT EXISTS.',f'SELECT p.{fk}, p.{pname} FROM {p} p WHERE NOT EXISTS (SELECT 1 FROM {f} f WHERE f.{fk}=p.{fk}) ORDER BY p.{fk};','Only master ID 5.'),
        ('Highest value per master',f'Use ROW_NUMBER to select the highest {amt} event for each active master. Break ties by {pk} ascending.',f';WITH Ranked AS (SELECT {pk},{fk},{amt},ROW_NUMBER() OVER(PARTITION BY {fk} ORDER BY {amt} DESC,{pk}) AS rn FROM {f}) SELECT {pk},{fk},{amt} FROM Ranked WHERE rn=1 ORDER BY {fk};','Master/event IDs: 1/2, 2/3, 3/6, 4/9.'),
    ]
    if s=='retail':
        reports += [
            ('Order detail','Show order ID, customer name, product name, quantity, historical line price and line total for every order line.',f'SELECT o.OrderID,c.CustomerName,p.ProductName,i.Quantity,i.UnitPrice,i.Quantity*i.UnitPrice AS LineTotal FROM {f} o JOIN [retail].[Customers] c ON c.CustomerID=o.CustomerID JOIN [retail].[OrderItems] i ON i.OrderID=o.OrderID JOIN [retail].[Products] p ON p.ProductID=i.ProductID ORDER BY o.OrderID,i.OrderItemID;','6 rows; line totals sum to 850. Product catalog prices are not substituted for historical line prices.'),
            ('Payment reconciliation','For all orders, return OrderID, OrderTotal, line total, paid total and outstanding amount. Aggregate lines and payments separately before joining. Preserve unknown OrderTotal; missing lines/payments count as zero.',";WITH Lines AS (SELECT OrderID,SUM(Quantity*UnitPrice) AS LineTotal FROM retail.OrderItems GROUP BY OrderID), Paid AS (SELECT OrderID,SUM(PaidAmount) AS PaidTotal FROM retail.Payments GROUP BY OrderID) SELECT o.OrderID,o.OrderTotal,COALESCE(l.LineTotal,0) AS LineTotal,COALESCE(p.PaidTotal,0) AS PaidTotal,o.OrderTotal-COALESCE(p.PaidTotal,0) AS Outstanding FROM retail.Orders o LEFT JOIN Lines l ON l.OrderID=o.OrderID LEFT JOIN Paid p ON p.OrderID=o.OrderID ORDER BY o.OrderID;",'12 rows. Order 1 has line total 100, paid 100, outstanding 0 despite having two lines and two payments. Order 3 outstanding=100. Order 4 outstanding=NULL.'),
            ('Unused products','Return product ID and name for products never used on an order line.',"SELECT p.ProductID,p.ProductName FROM retail.Products p WHERE NOT EXISTS(SELECT 1 FROM retail.OrderItems i WHERE i.ProductID=p.ProductID) ORDER BY p.ProductID;",'Products 4 and 5.')]
    elif s=='banking':
        reports += [
            ('Transaction trace','Show every transaction ID, account name, customer name, branch name and amount.',"SELECT t.TransactionID,a.AccountName,c.CustomerName,b.BranchName,t.Amount FROM banking.Transactions t JOIN banking.Accounts a ON a.AccountID=t.AccountID JOIN banking.Customers c ON c.CustomerID=a.CustomerID JOIN banking.Branches b ON b.BranchID=a.BranchID ORDER BY t.TransactionID;",'12 rows; every transaction has a valid account, customer and branch.'),
            ('Customer exposure','Return each customer with transaction amount total through their accounts and principal total through their loans. Aggregate the two measures independently; use zero for no activity.',";WITH Activity AS (SELECT a.CustomerID,SUM(t.Amount) AS TransactionTotal FROM banking.Accounts a JOIN banking.Transactions t ON t.AccountID=a.AccountID GROUP BY a.CustomerID), Lending AS (SELECT CustomerID,SUM(Principal) AS PrincipalTotal FROM banking.Loans GROUP BY CustomerID) SELECT c.CustomerID,COALESCE(a.TransactionTotal,0) AS TransactionTotal,COALESCE(l.PrincipalTotal,0) AS PrincipalTotal FROM banking.Customers c LEFT JOIN Activity a ON a.CustomerID=c.CustomerID LEFT JOIN Lending l ON l.CustomerID=c.CustomerID ORDER BY c.CustomerID;",'5 rows. Customer 1: transaction total 420, principal 15000. Principal totals sum to 58000, not multiplied by transaction count.'),
            ('Branch activity','Show all branches and their account counts, including branches without activity; count accounts rather than transactions.',"SELECT b.BranchID,b.BranchName,COUNT(a.AccountID) AS AccountCount FROM banking.Branches b LEFT JOIN banking.Accounts a ON a.BranchID=b.BranchID GROUP BY b.BranchID,b.BranchName ORDER BY b.BranchID;",'Five branches, one account each. An account with no transactions still counts.')]
    elif s=='pharma':
        reports += [
            ('Batch location trace','Show inventory ID, batch code, supplier name, product name, warehouse name and quantity on hand by joining all five tables.',"SELECT i.InventoryID,b.BatchCode,s.SupplierName,p.ProductName,w.WarehouseName,i.QuantityOnHand FROM pharma.Inventory i JOIN pharma.Batches b ON b.BatchID=i.BatchID JOIN pharma.Suppliers s ON s.SupplierID=b.SupplierID JOIN pharma.Products p ON p.ProductID=b.ProductID JOIN pharma.Warehouses w ON w.WarehouseID=i.WarehouseID ORDER BY i.InventoryID;",'6 inventory rows; quantity total=150.'),
            ('Batch stock','List every batch with supplier name, batch cost and total stock across warehouses. Include unstocked batches with zero units; do not multiply batch cost by location count.',";WITH Stock AS (SELECT BatchID,SUM(QuantityOnHand) AS Units FROM pharma.Inventory GROUP BY BatchID) SELECT b.BatchID,s.SupplierName,b.BatchCost,COALESCE(x.Units,0) AS StockUnits FROM pharma.Batches b JOIN pharma.Suppliers s ON s.SupplierID=b.SupplierID LEFT JOIN Stock x ON x.BatchID=b.BatchID ORDER BY b.BatchID;",'12 rows. Batch 1 has 50 units and cost 100 once. Batch 4 has zero stock and unknown cost.'),
            ('Empty warehouses','Return warehouses with no inventory rows; distinguish this from a warehouse holding a zero-quantity inventory row.',"SELECT w.WarehouseID,w.WarehouseName FROM pharma.Warehouses w WHERE NOT EXISTS(SELECT 1 FROM pharma.Inventory i WHERE i.WarehouseID=w.WarehouseID) ORDER BY w.WarehouseID;",'Warehouse 5 only. Warehouse 4 has an inventory row with zero quantity and is not returned.')]
    elif s=='healthcare':
        reports += [
            ('Prescription trace','Show prescription reference, patient name, doctor name, encounter ID, medication name and prescribed quantity by joining all five tables.',"SELECT r.PrescriptionReference,p.PatientName,d.DoctorName,e.EncounterID,m.MedicationName,r.Quantity FROM healthcare.Prescriptions r JOIN healthcare.Encounters e ON e.EncounterID=r.EncounterID JOIN healthcare.Patients p ON p.PatientID=e.PatientID JOIN healthcare.Doctors d ON d.DoctorID=e.DoctorID JOIN healthcare.Medications m ON m.MedicationID=r.MedicationID ORDER BY r.PrescriptionID;",'5 rows; no real clinical instructions are implied.'),
            ('Encounter billing','Return every encounter, patient name, charge and prescription count. Count prescriptions before joining, so charges appear only once per encounter.',";WITH Rx AS (SELECT EncounterID,COUNT(*) AS PrescriptionCount FROM healthcare.Prescriptions GROUP BY EncounterID) SELECT e.EncounterID,p.PatientName,e.Charge,COALESCE(r.PrescriptionCount,0) AS PrescriptionCount FROM healthcare.Encounters e JOIN healthcare.Patients p ON p.PatientID=e.PatientID LEFT JOIN Rx r ON r.EncounterID=e.EncounterID ORDER BY e.EncounterID;",'12 rows. Encounter 1 charge=100 and prescription count=2. Encounter 4 charge=NULL and count=0. Known charges total 1700.'),
            ('Unprescribed medications','Find medication IDs and names never referenced by a prescription.',"SELECT m.MedicationID,m.MedicationName FROM healthcare.Medications m WHERE NOT EXISTS(SELECT 1 FROM healthcare.Prescriptions p WHERE p.MedicationID=m.MedicationID) ORDER BY m.MedicationID;",'Medication 5 only.')]
    elif s=='oil':
        reports += [
            ('Shipment trace','Show each shipment line with site name, carrier name, product name, quantity and historical price per unit using all five tables.',"SELECT i.ShipmentItemID,s.SiteName,c.CarrierName,p.ProductName,i.Quantity,i.PricePerUnit FROM oil.ShipmentItems i JOIN oil.Shipments h ON h.ShipmentID=i.ShipmentID JOIN oil.Sites s ON s.SiteID=h.SiteID JOIN oil.Carriers c ON c.CarrierID=h.CarrierID JOIN oil.Products p ON p.ProductID=i.ProductID ORDER BY i.ShipmentItemID;",'5 line rows; each resolves to a site, carrier and product.'),
            ('Shipment reconciliation','List every shipment, site name, carrier name, recorded shipment value and total of quantity times historical price. Include missing detail as zero; return recorded value minus line total as Difference.',";WITH Lines AS (SELECT ShipmentID,SUM(Quantity*PricePerUnit) AS LineTotal FROM oil.ShipmentItems GROUP BY ShipmentID) SELECT h.ShipmentID,s.SiteName,c.CarrierName,h.ShipmentValue,COALESCE(l.LineTotal,0) AS LineTotal,h.ShipmentValue-COALESCE(l.LineTotal,0) AS Difference FROM oil.Shipments h JOIN oil.Sites s ON s.SiteID=h.SiteID JOIN oil.Carriers c ON c.CarrierID=h.CarrierID LEFT JOIN Lines l ON l.ShipmentID=h.ShipmentID ORDER BY h.ShipmentID;",'12 shipments; shipment 1 line total=100 and Difference=0. Shipment 4 Difference=NULL. All known recorded values sum to 1700.'),
            ('Unused carriers','List carriers never assigned to any shipment, including their Active flag.',"SELECT c.CarrierID,c.CarrierName,c.Active FROM oil.Carriers c WHERE NOT EXISTS(SELECT 1 FROM oil.Shipments s WHERE s.CarrierID=c.CarrierID) ORDER BY c.CarrierID;",'Carrier 5, Active=0.')]
    else:
        reports += additional_reports(m)
    return reports

def additional_reports(m):
    s=m['slug']
    if s=='retail_supply_chain':
        return [
            ('Movement provenance','Show every stock movement with warehouse, product, sourcing, originating supplier, direction, moved units and the matching current on-hand balance using five tables. Join balances on BOTH warehouse and product.',"SELECT m.MovementID,w.WarehouseName,p.ProductName,p.Sourcing,s.SupplierName,m.Direction,m.MovedUnits,b.QuantityOnHand FROM retail_supply_chain.StockMovements m JOIN retail_supply_chain.Warehouses w ON w.WarehouseID=m.WarehouseID JOIN retail_supply_chain.Products p ON p.ProductID=m.ProductID JOIN retail_supply_chain.Suppliers s ON s.SupplierID=m.SupplierID LEFT JOIN retail_supply_chain.StockBalances b ON b.WarehouseID=m.WarehouseID AND b.ProductID=m.ProductID ORDER BY m.MovementID;",'12 rows; every seed movement resolves to one warehouse/product snapshot. Movements 3, 4, 7, 8, 11 and 12 are Made products supplied by the Private Label Plant. A warehouse-only join to StockBalances would multiply rows.'),
            ('Factory to shelf','For every production order show its reference, product name, status, planned units, required material units (recipe quantity times PlannedUnits), material units used and units received into stock (IN movements that point to the order). Aggregate the recipe, the usage and the receipts separately before joining; missing values count as zero.',";WITH Recipe AS (SELECT o.ProductionOrderID,SUM(o.PlannedUnits*b.QuantityPerUnit) AS RequiredUnits FROM retail_supply_chain.ProductionOrders o JOIN retail_supply_chain.BillOfMaterials b ON b.ProductID=o.ProductID GROUP BY o.ProductionOrderID), Used AS (SELECT ProductionOrderID,SUM(QuantityUsed) AS UsedUnits FROM retail_supply_chain.MaterialUsage GROUP BY ProductionOrderID), Received AS (SELECT ProductionOrderID,SUM(MovedUnits) AS ReceivedUnits FROM retail_supply_chain.StockMovements WHERE Direction='IN' AND ProductionOrderID IS NOT NULL GROUP BY ProductionOrderID) SELECT o.ProductionReference,p.ProductName,o.ProductionStatus,o.PlannedUnits,COALESCE(r.RequiredUnits,0) AS RequiredUnits,COALESCE(u.UsedUnits,0) AS UsedUnits,COALESCE(x.ReceivedUnits,0) AS ReceivedUnits FROM retail_supply_chain.ProductionOrders o JOIN retail_supply_chain.Products p ON p.ProductID=o.ProductID LEFT JOIN Recipe r ON r.ProductionOrderID=o.ProductionOrderID LEFT JOIN Used u ON u.ProductionOrderID=o.ProductionOrderID LEFT JOIN Received x ON x.ProductionOrderID=o.ProductionOrderID ORDER BY o.ProductionOrderID;",'4 rows. PO-1: required 30, used 30.5 (0.5 over the recipe) and 3 units received so far. PO-2 is Completed but nothing is received yet. PO-3 has used 8 of 24 required units; PO-4 is Planned with no usage. Joining recipe, usage and receipts before aggregating would multiply the totals.'),
            ('Ledger reconciliation','For each warehouse/product snapshot, show opening quantity, signed net movement (IN positive, OUT negative), expected on-hand, stored on-hand and stored-minus-expected discrepancy. Include snapshots with no movements. All supplied movements are after the opening snapshot.',";WITH Net AS (SELECT WarehouseID,ProductID,SUM(CASE Direction WHEN 'IN' THEN MovedUnits ELSE -MovedUnits END) AS NetUnits FROM retail_supply_chain.StockMovements GROUP BY WarehouseID,ProductID) SELECT b.WarehouseID,b.ProductID,b.OpeningQuantity,COALESCE(n.NetUnits,0) AS NetUnits,b.OpeningQuantity+COALESCE(n.NetUnits,0) AS ExpectedOnHand,b.QuantityOnHand,b.QuantityOnHand-(b.OpeningQuantity+COALESCE(n.NetUnits,0)) AS Discrepancy FROM retail_supply_chain.StockBalances b LEFT JOIN Net n ON n.WarehouseID=b.WarehouseID AND n.ProductID=b.ProductID ORDER BY b.WarehouseID,b.ProductID;",'12 rows; all discrepancies=0. Warehouse 2/product 4: opening=10, net=8, on-hand=18. Warehouse 1/product 5 has no movements (net 0). Total opening=120 and total on-hand=130.')]
    if s=='ecommerce':
        return [
            ('Order detail','Show order ID, customer name, seller name, product name, quantity, charged unit price and line total for every order line.',"SELECT o.OrderID,c.CustomerName,s.SellerName,p.ProductName,i.Quantity,i.UnitPrice,i.Quantity*i.UnitPrice AS LineTotal FROM ecommerce.Orders o JOIN ecommerce.Customers c ON c.CustomerID=o.CustomerID JOIN ecommerce.Sellers s ON s.SellerID=o.SellerID JOIN ecommerce.OrderItems i ON i.OrderID=o.OrderID JOIN ecommerce.Products p ON p.ProductID=i.ProductID ORDER BY o.OrderID,i.OrderItemID;",'6 rows; line totals sum to 850. Orders 1 and 5 are Seller 1 (Electronics); the charged UnitPrice is used, not the catalog price.'),
            ('Settlement check','For all orders, return OrderID, OrderTotal, line total, paid total and outstanding amount. An order can be split between a gift card and a card, so aggregate lines and payments separately before joining. Preserve unknown OrderTotal; missing lines/payments count as zero.',";WITH Lines AS (SELECT OrderID,SUM(Quantity*UnitPrice) AS LineTotal FROM ecommerce.OrderItems GROUP BY OrderID), Paid AS (SELECT OrderID,SUM(PaidAmount) AS PaidTotal FROM ecommerce.Payments GROUP BY OrderID) SELECT o.OrderID,o.OrderTotal,COALESCE(l.LineTotal,0) AS LineTotal,COALESCE(p.PaidTotal,0) AS PaidTotal,o.OrderTotal-COALESCE(p.PaidTotal,0) AS Outstanding FROM ecommerce.Orders o LEFT JOIN Lines l ON l.OrderID=o.OrderID LEFT JOIN Paid p ON p.OrderID=o.OrderID ORDER BY o.OrderID;",'12 rows. Order 1 is split between a gift card (40) and a card (60): paid 100, outstanding 0. Order 3 outstanding=100, order 5 is unpaid (outstanding 50) and order 4 keeps NULL outstanding because its OrderTotal is unknown.'),
            ('Seller activity','Return every seller with its department, order count, known order revenue and distinct customers, including sellers with no orders (zero counts, zero revenue).',"SELECT s.SellerID,s.SellerName,s.Department,COUNT(o.OrderID) AS OrderCount,COALESCE(SUM(o.OrderTotal),0) AS Revenue,COUNT(DISTINCT o.CustomerID) AS DistinctCustomers FROM ecommerce.Sellers s LEFT JOIN ecommerce.Orders o ON o.SellerID=s.SellerID GROUP BY s.SellerID,s.SellerName,s.Department ORDER BY s.SellerID;",'5 rows. Seller 2 has the highest revenue (580); Seller 4 has 3 orders from 2 distinct customers; the unused seller shows zero orders and zero revenue.')]
    if s=='retail_logistics':
        return [
            ('Latest package location','Show every package, its shipment ID, customer name, carrier name, latest tracking status and scan time. Join all five tables, choosing the latest scan by ScanTime descending then TrackingEventID descending. Keep packages with no scan.',";WITH Latest AS (SELECT PackageID,EventStatus,ScanTime,ROW_NUMBER() OVER(PARTITION BY PackageID ORDER BY ScanTime DESC,TrackingEventID DESC) AS rn FROM retail_logistics.TrackingEvents) SELECT p.PackageID,h.ShipmentID,c.CustomerName,r.CarrierName,l.EventStatus,l.ScanTime FROM retail_logistics.ShipmentPackages p JOIN retail_logistics.Shipments h ON h.ShipmentID=p.ShipmentID JOIN retail_logistics.Customers c ON c.CustomerID=h.CustomerID JOIN retail_logistics.Carriers r ON r.CarrierID=h.CarrierID LEFT JOIN Latest l ON l.PackageID=p.PackageID AND l.rn=1 ORDER BY p.PackageID;",'5 rows. Package 1 is Delivered; package 2 is InTransit; package 5 has NULL status/time.'),
            ('Delivered late','Find packages whose first Delivered scan occurred on a calendar date after PromisedDate. Show package ID, promised date and first delivery time. A package without a Delivered scan must not be labeled delivered late.',";WITH Delivered AS (SELECT PackageID,MIN(ScanTime) AS DeliveredAt FROM retail_logistics.TrackingEvents WHERE EventStatus='Delivered' GROUP BY PackageID) SELECT p.PackageID,p.PromisedDate,d.DeliveredAt FROM retail_logistics.ShipmentPackages p JOIN Delivered d ON d.PackageID=p.PackageID WHERE CONVERT(date,d.DeliveredAt)>p.PromisedDate ORDER BY p.PackageID;",'Package 3 only: promised 2024-01-04, first delivered 2024-01-05. Package 1 was delivered on its promised date.'),
            ('Freight and package reconciliation','Return all shipments with recorded freight charge, declared package count and actual package count. Pre-aggregate package rows; do not join raw tracking scans into monetary totals.',";WITH Packages AS (SELECT ShipmentID,COUNT(*) AS ActualPackages FROM retail_logistics.ShipmentPackages GROUP BY ShipmentID) SELECT s.ShipmentID,s.FreightCharge,s.DeclaredPackages,COALESCE(p.ActualPackages,0) AS ActualPackages FROM retail_logistics.Shipments s LEFT JOIN Packages p ON p.ShipmentID=s.ShipmentID ORDER BY s.ShipmentID;",'12 rows; known freight charges total 1700 once each. Shipment 1 declares 1 package but has 2 recorded packages: flag the mismatch rather than changing the seed.')]
    if s=='brokerage':
        return [
            ('Client-to-execution audit','Join all five tables to show execution reference, client name, account number, security symbol, order ID, executed quantity, price and gross executed value.',"SELECT e.ExecutionReference,c.ClientName,a.AccountNumber,s.Symbol,o.OrderID,e.ExecutedQuantity,e.ExecutionPrice,e.ExecutedQuantity*e.ExecutionPrice AS GrossValue FROM brokerage.Executions e JOIN brokerage.TradeOrders o ON o.OrderID=e.OrderID JOIN brokerage.BrokerageAccounts a ON a.AccountID=o.AccountID JOIN brokerage.Clients c ON c.ClientID=a.ClientID JOIN brokerage.Securities s ON s.SecurityID=o.SecurityID ORDER BY e.ExecutionID;",'6 fills; gross executed values total 702.60. All clients and securities are fictitious.'),
            ('Fill reconciliation','For all orders, return requested, filled and remaining quantities, gross executed value and quantity-weighted average execution price. Use zero filled/gross for unfilled orders, but NULL average. Identify any overfills.',";WITH Fills AS (SELECT OrderID,SUM(ExecutedQuantity) AS FilledQuantity,SUM(ExecutedQuantity*ExecutionPrice) AS GrossValue FROM brokerage.Executions GROUP BY OrderID) SELECT o.OrderID,o.RequestedQuantity,COALESCE(f.FilledQuantity,0) AS FilledQuantity,o.RequestedQuantity-COALESCE(f.FilledQuantity,0) AS RemainingQuantity,COALESCE(f.GrossValue,0) AS GrossValue,f.GrossValue/NULLIF(f.FilledQuantity,0) AS AverageExecutionPrice FROM brokerage.TradeOrders o LEFT JOIN Fills f ON f.OrderID=o.OrderID ORDER BY o.OrderID;",'12 orders. Order 1: filled=1, remaining=0, gross=100.60, average=100.60. Order 2: filled=1.5, remaining=0.5, gross=149, average approximately 99.333333. Order 4 has NULL average. No order is overfilled.'),
            ('Client execution totals','Return all clients with gross executed value and number of fills through their accounts, including clients without executions. Avoid multiplying order estimates by fill counts.',";WITH Activity AS (SELECT a.ClientID,SUM(e.ExecutedQuantity*e.ExecutionPrice) AS GrossValue,COUNT(e.ExecutionID) AS FillCount FROM brokerage.BrokerageAccounts a JOIN brokerage.TradeOrders o ON o.AccountID=a.AccountID JOIN brokerage.Executions e ON e.OrderID=o.OrderID GROUP BY a.ClientID) SELECT c.ClientID,c.ClientName,COALESCE(a.GrossValue,0) AS GrossValue,COALESCE(a.FillCount,0) AS FillCount FROM brokerage.Clients c LEFT JOIN Activity a ON a.ClientID=c.ClientID ORDER BY c.ClientID;",'5 clients. Client 1: gross 249.60 and 4 fills; client 2: 303 and 1 fill; client 3: 150 and 1 fill; clients 4 and 5: zero. These are executed notionals, not balances or profits.')]
    raise ValueError(s)

def write_projects(records):
    report_rows=[]
    for m in MODELS:
        directory=ROOT/'domains'/m['slug'];mp=m['map'];fact,master,pname=m['base']
        lines=[f'# {m["title"]}: connected SQL Server project','',m['business'],'',
               f'**Goal:** build and explain {table_count(m)} related tables, prove that constraints protect data, safely change data and produce correct multi-table reports. There is no daily schedule. Advance after passing each checkpoint.','',
               '## 1. Understand the relationships','',
               'A primary key identifies one row. A foreign key stores the identity of a related parent row. The parent must exist before inserting a non-NULL child reference. A UNIQUE key protects another business identifier; CHECK enforces a row-level rule; NOT NULL makes a value required.','',
               '```mermaid','erDiagram']
        if m.get('source_note'):
            lines[4:4]=[m['source_note'],'']
        for t in m['tables']:
            for f in t['fks']:
                optional=next(c for c in t['columns'] if c['name']==f['column'])['rule']=='NULL'
                lines.append(f'    {f["parent"]} {"|o" if optional else "||"}--o{{ {t["name"]} : "{f["column"]}"')
        lines += ['```','',
                  'Every FK uses NO ACTION. Delete children before a referenced parent, or redesign the business workflow explicitly. Root events have a NULL parent-event ID. The self-FK verifies parent existence, while a separate CHECK rejects self-parenting; these rules do not prevent longer cycles.','',
                  f'## 2. Build the {table_count(m)} tables','',
                  'Start in a new disposable SQL Server 2017+ database. Work in this order: **'+' → '.join(t['name'] for t in m['tables'])+'**. Use the DDL Create assignments linked below. Do not run the complete setup first if you are practicing CREATE.','']
        for t in m['tables']:
            lines += [f'### {t["name"]}', '',table_brief(m,t),'']
        lines += [f'**Checkpoint:** {table_count(m)} tables exist; each has a PK; every specified FK is enabled and trusted. Explain the one-to-many relationships and the purpose of any composite UNIQUE key without reading the solution.','',
                  '## 3. Load and inspect sample data','',
                  'Use the Data Setup insert exercises in the same parent-before-child order. Alternatively, after completing all CREATE tasks, run [seed.sql](seed.sql) once. Do not both run seed.sql and repeat the inserts. The instructor-only full answer is [schema_solution.sql](schema_solution.sql).','',
                  'The main event table contains training codes A/B/C and statuses Open/Closed/Pending, not a full production workflow. Its reference strings deliberately include case and whitespace for cleaning exercises. Monetary totals are recorded event values; line details exist only for selected events to support missing-detail and reconciliation reports. NULL means unknown, not zero.','']
        for t in m['tables']:
            lines += [f'### Sample rows: {t["name"]}','','| '+' | '.join(c['name'] for c in t['columns'])+' |','|'+'|'.join('---' for _ in t['columns'])+'|']
            for row in t['rows']:
                lines.append('| '+' | '.join('NULL' if v is None else '`'+str(v)+'`' for v in row)+' |')
            lines.append('')
        lines += ['**Checkpoint:** row counts match the samples, no FK references are missing, and known event amounts total **1700**. Master ID 5 has no events. All 12 events reference real masters; there are no deliberately invalid FK values.','',
                  '## 4. Prove the rules and practice changes','',
                  'Start each exercise with the original tables and sample rows in a practice database. Ask your instructor to reset the practice tables between exercises that change them. Show the results before and after. In exercises that test a rule, an error message is expected. Keep the rules turned on. See [the beginner guide](../../BEGINNER_GUIDE.md) if these terms are new.','',
                  '## Assignment navigation','',
                  'IDs are labels, not dates. Each row below links to questions for this domain only. Open [the student question index](questions/README.md) to see all topics.','',
                  '| Topic | Subtopic | Your assignment IDs |','|---|---|---|']
        topic_order=['DDL','DATA_SETUP','CONSTRAINTS','DML','DQL','OPERATORS','JOINS','SET_OPERATIONS','STRING_FUNCTIONS','DATE_FUNCTIONS','AGGREGATES','ANALYTICAL_FUNCTIONS','CTE','DATATYPES','DATABASE_SCHEMA_USER','INTRODUCTION']
        for topic in topic_order:
            selected=[r for r in records if r['domain']==m['title'] and r['topic']==topic]
            for sub in dict.fromkeys(r['subtopic'] for r in selected):
                ids=', '.join(r['id'] for r in selected if r['subtopic']==sub)
                lines.append(f'| [{topic}](questions/{topic}.md) | {sub} | {ids} |')
        lines += ['', f'## 5. Integrate all {table_count(m)} tables','',
                  'Complete [REPORTING_ASSIGNMENTS.md](REPORTING_ASSIGNMENTS.md) after joins, aggregates and CTEs. These reports follow the domain workflow and include reconciliations that fail when joins multiply rows.','',
                  '## 6. Confidence checkpoint and capstone','',
                  'Using a fresh database and this specification, without copying the solution:',
                  '',
                  f'1. Draw and explain all {table_count(m)} tables and relationship cardinalities.',
                  '2. Re-create the schema in dependency order, including every PK, FK, UNIQUE, CHECK and default.',
                  '3. Load valid sample data; demonstrate rejection of a duplicate PK, duplicate business key, NULL required field, invalid CHECK value and nonexistent parent.',
                  '4. Demonstrate that deleting a referenced parent fails; explain a child-first deletion plan. Use a practice database with the supplied sample rows and keep the foreign keys enabled.',
                  '5. Perform a correct insert, targeted update and targeted delete, checking the number of changed rows. Ask your instructor to reset the practice tables afterwards.',
                  '6. Complete all six domain reports and reconcile their row counts and control totals.',
                  '7. Add one new valid business record with related details, rerun the reports and explain exactly which results changed. Ask your instructor to reset the practice tables afterwards.',
                  '8. Explain NULL handling, INNER versus LEFT JOIN, WHERE versus HAVING, duplicate multiplication and deterministic ranking.',
                  '',
                  '**Ready to progress:** all integrity tests pass, all six reports reconcile, and you can explain each relationship and fix a deliberately incorrect join without an answer key. If a checkpoint fails, revisit that section instead of advancing by a calendar date.','']
        (directory/'README.md').write_text(student_english('\n'.join(lines)),encoding='utf-8')
        q=[f'# {m["title"]}: reporting assignments','', 'Use the tables and sample rows you created earlier. Submit your SQL, the results it shows and a short explanation. [Domain guide](README.md). [Help with SQL terms](../../BEGINNER_GUIDE.md).','']
        a=[f'# {m["title"]}: reporting solutions','', 'The baseline in seed.sql must be intact. Compare complete output and duplicate counts, not just the number of rows.','']
        for i,(title,prompt,sql,check) in enumerate(project_reports(m),1):
            eid=f'{m["slug"].upper()}-REPORT-{i:02d}'
            prompt=student_english(prompt)
            q += [f'## {eid}: {title}','',prompt,'']
            a += [f'## {eid}: {title}','','```sql',sql,'```','',f'**Validation:** {check}','']
            report_rows.append(dict(id=eid,domain=m['title'],prompt=prompt,sql=sql,check=check))
        a+=['## Capstone validation','',
            'Use schema_solution.sql as the structural reference and seed.sql as the data reference. Inspect sys.key_constraints, sys.foreign_keys and sys.check_constraints; foreign keys/checks must be enabled and trusted. A correct PK/FK design should reject each invalid case with the expected SQL Server error (515 for NOT NULL, 2627 for PK/UNIQUE, 547 for CHECK/FK).','',
            'For the parent-deletion test, choose a master with existing events (ID 1), attempt its deletion in a transaction, catch 547 and roll back. For the new-record scenario, require valid parent IDs and unique business identifiers. Verify the expected increase in counts/totals, then roll back and rerun baseline checks.','',
            'Pass only when all structural and integrity checks pass and all six reports reconcile. Grade explanations and independent correction of a faulty many-to-many join, not memorized syntax alone.','']
        (directory/'REPORTING_ASSIGNMENTS.md').write_text('\n'.join(q),encoding='utf-8')
        (directory/'REPORTING_SOLUTIONS.md').write_text('\n'.join(a),encoding='utf-8')

        # A self-contained student folder: prompts and reference data only.
        student=directory/'questions'
        student.mkdir(exist_ok=True)
        index=[f"# {m['title']} — Student questions", '',
               'Start with DDL to create the tables, then Data Setup to add the sample rows. Continue with the topics below as they are taught.', '',
               '[Table details and sample rows](DOMAIN_GUIDE.md) · [Beginner guide](BEGINNER_GUIDE.md)', '',
               '| Topic | Questions |', '|---|---:|']
        for topic in topic_order:
            selected=[r for r in records if r['domain']==m['title'] and r['topic']==topic]
            pages=[f"# {m['title']} — {topic.replace('_', ' ')}", '',
                   '[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)', '',
                   'Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.', '']
            if topic == 'DDL':
                pages += ['After the Create exercises, use [Large practice data](PRACTICE_DATA.md) for a dataset with at least 50 rows per master and 100 per detail table.', '']
            for sub in dict.fromkeys(r['subtopic'] for r in selected):
                pages += [f'## {sub}', '']
                for row in selected:
                    if row['subtopic'] != sub: continue
                    prompt=re.sub(r'\]\(\.\./domains/[^/]+/README\.md\)', '](DOMAIN_GUIDE.md)', row['prompt'])
                    prompt=prompt.replace('](../README.md)', '](DOMAIN_GUIDE.md)').replace('](../BEGINNER_GUIDE.md)', '](BEGINNER_GUIDE.md)')
                    pages += [f"### {row['id']}", '', prompt, '']
            (student/f'{topic}.md').write_text('\n'.join(pages),encoding='utf-8')
            index.append(f'| [{topic.replace("_", " ")}]({topic}.md) | {len(selected)} |')
        index += ['| [Reporting assignments](REPORTING_ASSIGNMENTS.md) | 6 |', '',
                  '[Large practice data: row counts and loading instructions](PRACTICE_DATA.md)', '',
                  'Submit your SQL and results. Assignment IDs are reference labels.', '']
        (student/'README.md').write_text('\n'.join(index),encoding='utf-8')
        guide=student_english('\n'.join(lines))
        guide=guide.replace('questions/README.md', 'README.md').replace('questions/', '')
        guide=guide.replace('../../BEGINNER_GUIDE.md', 'BEGINNER_GUIDE.md')
        guide=guide.replace('Alternatively, after completing all CREATE tasks, run [seed.sql](seed.sql) once. Do not both run seed.sql and repeat the inserts. The instructor-only full answer is [schema_solution.sql](schema_solution.sql).', 'Use the sample rows below. Ask your instructor for help loading them if needed. Add them only once.')
        (student/'DOMAIN_GUIDE.md').write_text(guide,encoding='utf-8')
        (student/'BEGINNER_GUIDE.md').write_text((ROOT/'BEGINNER_GUIDE.md').read_text(encoding='utf-8'),encoding='utf-8')
        reports='\n'.join(q).replace('](README.md)', '](DOMAIN_GUIDE.md)').replace('../../BEGINNER_GUIDE.md', 'BEGINNER_GUIDE.md')
        (student/'REPORTING_ASSIGNMENTS.md').write_text(reports,encoding='utf-8')

    (ROOT/'domain_reports.json').write_text(json.dumps(report_rows,indent=2)+'\n',encoding='utf-8')
    from advanced_queries import generate
    generate(MODELS)
    from instructor_solutions import generate as generate_solutions
    generate_solutions(MODELS, records)
