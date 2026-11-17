"""Per-domain configuration for the AmeriMed-style SQL workbooks.

Roles follow the healthcare workbook, which is the source the other domains are translated from:
  E = event table (Encounters)     P = party table (Patients)
  D = person/dimension on E (Doctors)   M = catalog with a price (Medications)   L = line table under E (Prescriptions)
A role is None when the domain has no equivalent; questions that need it are rewritten by hand in wb_overrides.
"""

HC = {
    'E': {'Encounters': None, 'EncounterID': 'RecordID', 'PatientID': 'PartyID', 'EncounterReference': 'Label',
          'EncounterType': 'Category', 'Status': 'Status', 'Charge': 'Amount', 'ServiceUnits': 'Quantity',
          'EncounterDate': 'EventDate', 'StartedAt': 'EventTime', 'ParentEncounterID': 'ParentID'},
    'P': ['Patients', 'PatientID', 'PatientName', 'PatientNumber', 'Region'],
    'D': ['Doctors', 'DoctorID', 'DoctorName', 'LicenseNumber', 'Specialty'],
    'M': ['Medications', 'MedicationID', 'MedicationName', 'MedicationCode', 'UnitCost'],
    'L': ['Prescriptions', 'PrescriptionID', 'PrescriptionReference', 'Quantity'],
}

# Nouns: (singular, plural). Roles that do not exist are None.
DOMAINS = {
    'banking': dict(
        company='Harborstone Bank', short='Harborstone', industry='Banking', db='HarborstonePractice',
        tagline='Retail bank with branches, customers, accounts, transactions and loans',
        P=['Accounts', 'AccountID', 'AccountName', 'AccountNumber', 'Region'], D=None, M=None, L=None,
        n=dict(ev=('transaction', 'transactions'), pt=('account', 'accounts'), amt=('amount', 'amounts')),
        color='#3b82f6', light='#1d4ed8', icon='bank'),
    'brokerage': dict(
        company='Ridgeline Securities', short='Ridgeline', industry='Brokerage', db='RidgelinePractice',
        tagline='Broker-dealer with clients, accounts, securities, trade orders and executions',
        P=['BrokerageAccounts', 'AccountID', 'AccountName', 'AccountNumber', 'Region'],
        D=['Securities', 'SecurityID', 'SecurityName', 'Symbol', 'AssetClass'], M=None,
        L=['Executions', 'ExecutionID', 'ExecutionReference', 'ExecutedQuantity'],
        lverb='executed', n=dict(ev=('trade order', 'trade orders'), pt=('account', 'accounts'), amt=('estimated value', 'estimated values'),
               d=('security', 'securities'), l=('execution', 'executions')),
        color='#8b5cf6', light='#6d28d9', icon='chart'),
    'oil': dict(
        company='Permian Ridge Energy', short='Permian Ridge', industry='Oil & Gas', db='PermianRidgePractice',
        tagline='Energy shipper with sites, carriers, products, shipments and shipment items',
        P=['Sites', 'SiteID', 'SiteName', 'SiteCode', 'Region'],
        D=['Carriers', 'CarrierID', 'CarrierName', 'CarrierCode', None],
        M=['Products', 'ProductID', 'ProductName', 'ProductCode', 'PricePerUnit'],
        L=['ShipmentItems', 'ShipmentItemID', None, 'Quantity'],
        lverb='shipped', n=dict(ev=('shipment', 'shipments'), pt=('site', 'sites'), amt=('shipment value', 'shipment values'),
               d=('carrier', 'carriers'), m=('product', 'products'), l=('shipment item', 'shipment items')),
        color='#f59e0b', light='#b45309', icon='fuel'),
    'pharma': dict(
        company='Novacrest Pharmaceuticals', short='Novacrest', industry='Pharma', db='NovacrestPractice',
        tagline='Drug maker with suppliers, products, warehouses, batches and inventory',
        P=['Suppliers', 'SupplierID', 'SupplierName', 'SupplierCode', 'Region'],
        D=['Products', 'ProductID', 'ProductName', 'ProductCode', None],
        M=['Warehouses', 'WarehouseID', 'WarehouseName', 'WarehouseCode', None],
        L=['Inventory', 'InventoryID', None, 'QuantityOnHand'],
        lverb='stocked', n=dict(ev=('batch', 'batches'), pt=('supplier', 'suppliers'), amt=('batch cost', 'batch costs'),
               d=('product', 'products'), m=('warehouse', 'warehouses'), l=('inventory record', 'inventory records')),
        color='#ec4899', light='#be185d', icon='flask'),
    'retail': dict(
        company='Maple & Main Stores', short='Maple & Main', industry='Retail', db='MapleMainStoresPractice',
        tagline='Store division: customers, products, orders, order items and payments',
        P=['Customers', 'CustomerID', 'CustomerName', 'CustomerCode', 'Region'], D=None,
        M=['Products', 'ProductID', 'ProductName', 'SKU', 'UnitPrice'],
        L=['OrderItems', 'OrderItemID', None, 'Quantity'],
        lverb='ordered', n=dict(ev=('order', 'orders'), pt=('customer', 'customers'), amt=('order total', 'order totals'),
               m=('product', 'products'), l=('order item', 'order items')),
        color='#ef4444', light='#b91c1c', icon='cart'),
    'retail_inventory': dict(
        company='Maple & Main Merchandising', short='Maple & Main Merchandising', industry='Retail Inventory',
        db='MapleMainMerchPractice',
        tagline='Stock division: warehouses, products, suppliers, stock movements and balances',
        P=['Warehouses', 'WarehouseID', 'WarehouseName', 'WarehouseCode', 'Region'],
        D=['Suppliers', 'SupplierID', 'SupplierName', 'SupplierCode', None],
        M=['Products', 'ProductID', 'ProductName', 'SKU', 'UnitCost'], L=None,
        n=dict(ev=('stock movement', 'stock movements'), pt=('warehouse', 'warehouses'), amt=('movement value', 'movement values'),
               d=('supplier', 'suppliers'), m=('product', 'products')),
        color='#10b981', light='#047857', icon='box'),
    'retail_logistics': dict(
        company='Maple & Main Distribution', short='Maple & Main Distribution', industry='Retail Logistics',
        db='MapleMainDistPractice',
        tagline='Distribution division: customers, carriers, shipments, packages and tracking scans',
        P=['Customers', 'CustomerID', 'CustomerName', 'CustomerCode', 'Region'],
        D=['Carriers', 'CarrierID', 'CarrierName', 'CarrierCode', 'ServiceLevel'], M=None,
        L=['ShipmentPackages', 'PackageID', 'TrackingNumber', 'WeightKg'],
        lverb='packed', n=dict(ev=('shipment', 'shipments'), pt=('customer', 'customers'), amt=('freight charge', 'freight charges'),
               d=('carrier', 'carriers'), l=('package', 'packages')),
        color='#06b6d4', light='#0e7490', icon='truck'),
    'retail_manufacturing': dict(
        company='Maple & Main Private Label', short='Maple & Main Private Label', industry='Retail Manufacturing',
        db='MapleMainMfgPractice',
        tagline='Own-brand factory: products, materials, production orders, recipes and material usage',
        P=['Products', 'ProductID', 'ProductName', 'ProductCode', 'Region'], D=None,
        M=['Materials', 'MaterialID', 'MaterialName', 'MaterialCode', 'UnitCost'],
        L=['MaterialUsage', 'UsageID', None, 'QuantityUsed'],
        lverb='used', n=dict(ev=('production order', 'production orders'), pt=('product', 'products'), amt=('planned cost', 'planned costs'),
               m=('material', 'materials'), l=('material usage record', 'material usage records')),
        color='#f97316', light='#c2410c', icon='factory'),
}
