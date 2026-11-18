# Connected project data dictionary

Each domain has five physical tables (E-commerce has six and Retail Supply Chain has nine), each with a primary key. Foreign keys are enforced: there are no deliberately orphaned event records. Full column definitions, business rules, relationships and exact seed rows are in the domain briefs.

| Domain | Schema brief and seed values |
|---|---|
| Retail | [Customers, Products, Orders, OrderItems, Payments](domains/retail/README.md) |
| Banking | [Branches, Customers, Accounts, Transactions, Loans](domains/banking/README.md) |
| Pharma | [Suppliers, Products, Warehouses, Batches, Inventory](domains/pharma/README.md) |
| Healthcare | [Patients, Doctors, Medications, Encounters, Prescriptions](domains/healthcare/README.md) |
| Oil | [Sites, Carriers, Products, Shipments, ShipmentItems](domains/oil/README.md) |
| Retail Supply Chain | [Warehouses, Suppliers, Products, Materials, BillOfMaterials, ProductionOrders, MaterialUsage, StockMovements, StockBalances](domains/retail_supply_chain/README.md) |
| Retail Logistics | [Customers, Carriers, Shipments, ShipmentPackages, TrackingEvents](domains/retail_logistics/README.md) |
| E-commerce | [Customers, Sellers, Products, Orders, OrderItems, Payments](domains/ecommerce/README.md) |
| Brokerage | [Clients, Securities, BrokerageAccounts, TradeOrders, Executions](domains/brokerage/README.md) |

## Main event tables

| Domain | Event | Parent/master relationship | Known amount | Date | Quantity measure |
|---|---|---|---|---|---|
| Retail | Orders | CustomerID → Customers | OrderTotal | OrderDate | PackageCount |
| Banking | Transactions | AccountID → Accounts | Amount | TransactionDate | UnitCount (processing units) |
| Pharma | Batches | SupplierID → Suppliers; ProductID → Products | BatchCost | ManufactureDate | PackCount |
| Healthcare | Encounters | PatientID → Patients; DoctorID → Doctors | Charge | EncounterDate | ServiceUnits |
| Oil | Shipments | SiteID → Sites; CarrierID → Carriers | ShipmentValue | ShipDate | UnitCount (shipping units) |
| Retail Supply Chain | StockMovements | WarehouseID → Warehouses; ProductID → Products; SupplierID → Suppliers; ProductionOrderID → ProductionOrders (optional) | MovementValue | MovementDate | MovedUnits |
| Retail Logistics | Shipments | CustomerID → Customers; CarrierID → Carriers | FreightCharge | ShipDate | DeclaredPackages |
| E-commerce | Orders | CustomerID → Customers; SellerID → Sellers | OrderTotal | OrderDate | ItemCount |
| Brokerage | TradeOrders | AccountID → BrokerageAccounts; SecurityID → Securities | EstimatedValue | OrderDate | RequestedQuantity |

Event IDs run from 1 through 12. They reference existing master IDs 1–4; master 5 has no related events. Each event table also has a nullable parent-event FK, with event 1 as the root of an acyclic teaching hierarchy. The self-FK and self-parent CHECK do not independently prevent longer cycles; the seed data is deliberately acyclic.

Event references/codes are unique but include whitespace and mixed case for string-function practice. Codes A/B/C group events; statuses Open/Closed/Pending describe a simplified workflow. Status defaults to Open when omitted. All event timestamps have time 12:30:45.123 on the business date. Interpret the timestamp as UTC unless an assignment explicitly reinterprets it; RecordedAt stores the same instant with +00:00.

Note is NULL on events 1,4,7,10 and confirmed otherwise. BackupNote is backup on odd event IDs and NULL on even IDs. Event 4's monetary value is unknown (NULL). Zero and NULL have different meanings.

## Control totals

For each event table: 12 rows, 11 known monetary values, known total 1700, minimum 0, maximum 300. The quantity measure totals 30. Each category/status contains four events; A totals 180, B totals 520, C totals 1000. Master IDs and event IDs: 1 → 1,2,11; 2 → 3,4,12; 3 → 5,6; 4 → 7,8,9,10; 5 → none.

Joining the main event table to its master gives 12 INNER JOIN rows. Preserving all masters gives 13 LEFT JOIN rows (or reversed RIGHT JOIN). FULL JOIN also gives 13: its one unmatched row is master 5, not an invalid foreign key. CROSS JOIN gives 60 pairs. A required FK's IS NULL query correctly returns no rows; use nullable amounts/notes/parent-event IDs to practice missing data.

Products, payments, loans, stock and prescriptions have their own counts and values shown in the briefs. Details exist only for selected events so reports can detect missing detail. Historical line prices are separate from current catalog prices. Header monetary values are already event totals: do not multiply them by package/service counts to calculate revenue. Any single-table amount-times-quantity exercise is arithmetic practice only; use the project reporting tasks for business reconciliation.

All data is synthetic. These simplified models teach relational SQL, not production banking, clinical, pharmaceutical or oil-industry rules. In the banking model, a loan borrower and servicing-account owner may differ; there is no composite FK asserting they must be identical.

## New-domain business rules

- **Manufacturing:** recipe QuantityPerUnit times PlannedUnits gives required material quantity. Actual usage may differ; a missing usage row means no consumption was recorded, not proof that production was completed efficiently.
- **Logistics:** a shipment has packages and each package has many scans. Package 5 intentionally has no scans. Shipment 1 has a declared/actual package mismatch for reconciliation practice. Use the first Delivered scan for delivery lateness and the latest scan for current tracking status.
- **Inventory:** Direction determines the sign of positive MovedUnits. All supplied movements occur after the OpeningQuantity snapshot. Current on-hand totals 120 = opening 110 + net receipts/issues 10. A warehouse/product balance is unique; no trigger automatically maintains it when movements are changed.

- **Brokerage:** synthetic buy orders support fractional partial executions. EstimatedValue is not executed notional or cash balance. Derive fill status from quantities, not the administrative WorkflowStatus. The seed has 702.60 gross executed value and no overfills. Compute weighted execution prices and keep unfilled average prices NULL.
