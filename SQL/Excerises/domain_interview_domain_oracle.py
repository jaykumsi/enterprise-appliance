"""Small-fixture five-table reconciliation oracle,independent of reference SQL."""
from collections import defaultdict
from datetime import date,datetime
from decimal import Decimal


def number(x):return Decimal(str(x))
def total(values):return sum((number(x) for x in values if x is not None),Decimal(0))
def records(model,name):
    t=next(t for t in model['tables'] if t['name']==name)
    return [dict(zip((c['name'] for c in t['columns']),r)) for r in t['rows']]
def index(rows,key):return {r[key]:r for r in rows}
def dt(x):
    if isinstance(x,(date,datetime)):return x
    text=str(x)
    if len(text)==8 and text.isdigit():return date(int(text[:4]),int(text[4:6]),int(text[6:]))
    return datetime.fromisoformat(text.replace('Z','+00:00'))


def reconciliation(model,eligible_ids):
    s=model['slug'];mp=model['map'];fact,master,_=model['base'];fk=mp['PartyID'];pk=mp['RecordID'];amt=mp['Amount']
    facts=[r for r in records(model,fact) if r[pk] in eligible_ids]
    out=[]
    def tab(name):return records(model,name)
    for owner in tab(master):
        oid=owner[fk];fs=[r for r in facts if r[fk]==oid];ids={r[pk] for r in fs};values=[r[amt] for r in fs if r[amt] is not None]
        row={fk:oid,'EventCount':len(fs),'KnownCount':len(values),'TotalValue':total(values) if values or not fs else None}
        if s=='retail':
            lines=[r for r in tab('OrderItems') if r['OrderID'] in ids];paid=[r for r in tab('Payments') if r['OrderID'] in ids]
            row.update(LineValue=total(number(r['Quantity'])*number(r['UnitPrice']) for r in lines),PaidValue=total(r['PaidAmount'] for r in paid),DistinctProducts=len({r['ProductID'] for r in lines}))
            row['Outstanding']=None if row['TotalValue'] is None else row['TotalValue']-row['PaidValue']
        elif s=='banking':
            loans=[r for r in tab('Loans') if r['AccountID']==oid];customers=index(tab('Customers'),'CustomerID');branches=index(tab('Branches'),'BranchID')
            row.update(CustomerName=customers[owner['CustomerID']]['CustomerName'],BranchName=branches[owner['BranchID']]['BranchName'],LoanPrincipal=total(r['Principal'] for r in loans),LoanCount=len(loans),LoanOwnerMismatch=sum(r['CustomerID']!=owner['CustomerID'] for r in loans))
        elif s=='pharma':
            inv=[r for r in tab('Inventory') if r['BatchID'] in ids];batches=index(fs,'BatchID');products=index(tab('Products'),'ProductID');wh=index(tab('Warehouses'),'WarehouseID');units=defaultdict(Decimal)
            for r in inv:units[r['WarehouseID']]+=number(r['QuantityOnHand'])
            row.update(StockUnits=total(r['QuantityOnHand'] for r in inv),StandardStockValue=total(number(r['QuantityOnHand'])*number(products[batches[r['BatchID']]['ProductID']]['StandardCost']) for r in inv),WarehouseCount=len(units),OverCapacityWarehouses=sum(v>wh[k]['Capacity'] for k,v in units.items()))
        elif s=='healthcare':
            rx=[r for r in tab('Prescriptions') if r['EncounterID'] in ids];med=index(tab('Medications'),'MedicationID');docs=index(tab('Doctors'),'DoctorID');docids={r['DoctorID'] for r in fs}
            row.update(DoctorCount=len(docids),SpecialtyCount=len({docs[k]['Specialty'] for k in docids}),PrescribedUnits=total(r['Quantity'] for r in rx),DistinctMedications=len({r['MedicationID'] for r in rx}),MedicationCostProxy=total(number(r['Quantity'])*number(med[r['MedicationID']]['UnitCost']) for r in rx))
        elif s=='oil':
            lines=[r for r in tab('ShipmentItems') if r['ShipmentID'] in ids];products=index(tab('Products'),'ProductID');carriers=index(tab('Carriers'),'CarrierID')
            row.update(LineUnits=total(r['Quantity'] for r in lines),HistoricalLineValue=total(number(r['Quantity'])*number(r['PricePerUnit']) for r in lines),CarrierCount=len({r['CarrierID'] for r in fs}),InactiveCarrierShipments=sum(not carriers[r['CarrierID']]['Active'] for r in fs),CatalogPriceDifferences=sum(number(r['PricePerUnit'])!=number(products[r['ProductID']]['PricePerUnit']) for r in lines))
        elif s=='retail_manufacturing':
            pairs={};materials=index(tab('Materials'),'MaterialID')
            for f in fs:
                for b in tab('BillOfMaterials'):
                    if b['ProductID']==f['ProductID']:pairs[(f['ProductionOrderID'],b['MaterialID'])]=[number(f['PlannedUnits'])*number(b['QuantityPerUnit']),Decimal(0),False]
            for u in tab('MaterialUsage'):
                if u['ProductionOrderID'] in ids:
                    key=(u['ProductionOrderID'],u['MaterialID'])
                    if key not in pairs:pairs[key]=[Decimal(0),Decimal(0),True]
                    pairs[key][1]+=number(u['QuantityUsed'])
            row.update(RequiredUnits=total(p[0] for p in pairs.values()),ActualUnits=total(p[1] for p in pairs.values()),ActualCostProxy=total(p[1]*number(materials[k[1]]['UnitCost']) for k,p in pairs.items()),UnexpectedUnits=total(p[1] for p in pairs.values() if p[2]),ShortagePairs=sum(p[1]<p[0] for p in pairs.values()))
        elif s=='retail_logistics':
            packages=[r for r in tab('ShipmentPackages') if r['ShipmentID'] in ids];carrier=index(tab('Carriers'),'CarrierID');latest_delivered=late=unscanned=scans=0
            for p in packages:
                ts=[r for r in tab('TrackingEvents') if r['PackageID']==p['PackageID']];scans+=len(ts)
                if not ts:unscanned+=1
                else:latest_delivered+=max(ts,key=lambda r:(dt(r['ScanTime']),r['TrackingEventID']))['EventStatus']=='Delivered'
                ds=[r for r in ts if r['EventStatus']=='Delivered']
                if ds:late+=min(dt(r['ScanTime']) for r in ds).date()>dt(p['PromisedDate'])
            row.update(ServiceLevelCount=len({carrier[r['CarrierID']]['ServiceLevel'] for r in fs}),PackageCount=len(packages),PackageWeightKg=total(r['WeightKg'] for r in packages),LatestDeliveredCount=latest_delivered,LateFirstDeliveryCount=late,UnscannedCount=unscanned,TrackingScanCount=scans)
        elif s=='retail_inventory':
            net=defaultdict(Decimal)
            for r in fs:net[r['ProductID']]+=number(r['MovedUnits'])*(1 if r['Direction']=='IN' else -1)
            balances=[r for r in tab('StockBalances') if r['WarehouseID']==oid];products=index(tab('Products'),'ProductID');suppliers=index(tab('Suppliers'),'SupplierID');balance_products={r['ProductID'] for r in balances}
            row.update(OpeningUnits=total(r['OpeningQuantity'] for r in balances),StoredUnits=total(r['QuantityOnHand'] for r in balances),SelectedNetUnits=total(net[r['ProductID']] for r in balances),QuantityDifference=total(number(r['QuantityOnHand'])-number(r['OpeningQuantity'])-net[r['ProductID']] for r in balances),StandardStockValue=total(number(r['QuantityOnHand'])*number(products[r['ProductID']]['UnitCost']) for r in balances),MissingBalancePairs=len(set(net)-balance_products),MaxLeadTimeDays=max((suppliers[r['SupplierID']]['LeadTimeDays'] for r in fs),default=None))
        else:
            executions=[r for r in tab('Executions') if r['OrderID'] in ids];clients=index(tab('Clients'),'ClientID');qty=total(r['ExecutedQuantity'] for r in executions);value=total(number(r['ExecutedQuantity'])*number(r['ExecutionPrice']) for r in executions)
            row.update(ClientName=clients[owner['ClientID']]['ClientName'],RequestedQuantity=total(r['RequestedQuantity'] for r in fs),ExecutedQuantity=qty,ExecutionValue=value,WeightedExecutionPrice=value/qty if qty else None,OverfilledOrders=sum(total(x['ExecutedQuantity'] for x in executions if x['OrderID']==r['OrderID'])>r['RequestedQuantity'] for r in fs),SecurityCount=len({r['SecurityID'] for r in fs}))
        out.append(row)
    return out
