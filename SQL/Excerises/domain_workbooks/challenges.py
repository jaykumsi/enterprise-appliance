"""Interview Challenges: 10 multi-step questions per domain, in the style of real interview problems
(DataLemur-type: repeats within a window, medians, month-to-date totals, gaps and islands, cohorts, Pareto,
fan-out traps, reconciliations, pair and combination self-joins, top-N with ties).

Each challenge is (title, question, answer_sql, hint). The hint is shown with the expected result, so a student
sees it only after trying. The answer SQL stays private (items/<domain>_challenges.json).
"""

# ---------------------------------------------------------------------------------------------------------------
# Shared patterns, written once over each domain's event table (E) and party table (P)
# ---------------------------------------------------------------------------------------------------------------
G = {
    'healthcare': dict(s='healthcare', E='Encounters', id='EncounterID', P='Patients', fk='PatientID', name='PatientName',
                       date='EncounterDate', cat='EncounterType', amt='Charge', ev='encounter', evs='encounters', pt='patient', pts='patients', amtn='charge'),
    'banking': dict(s='banking', E='Transactions', id='TransactionID', P='Accounts', fk='AccountID', name='AccountName',
                    date='TransactionDate', cat='TransactionType', amt='Amount', ev='transaction', evs='transactions', pt='account', pts='accounts', amtn='amount'),
    'brokerage': dict(s='brokerage', E='TradeOrders', id='OrderID', P='BrokerageAccounts', fk='AccountID', name='AccountName',
                      date='OrderDate', cat='RoutingCategory', amt='EstimatedValue', ev='trade order', evs='trade orders', pt='account', pts='accounts', amtn='estimated value'),
    'oil': dict(s='oil', E='Shipments', id='ShipmentID', P='Sites', fk='SiteID', name='SiteName',
                date='ShipDate', cat='ShipmentType', amt='ShipmentValue', ev='shipment', evs='shipments', pt='site', pts='sites', amtn='shipment value'),
    'pharma': dict(s='pharma', E='Batches', id='BatchID', P='Suppliers', fk='SupplierID', name='SupplierName',
                   date='ManufactureDate', cat='BatchType', amt='BatchCost', ev='batch', evs='batches', pt='supplier', pts='suppliers', amtn='batch cost'),
    'retail': dict(s='retail', E='Orders', id='OrderID', P='Customers', fk='CustomerID', name='CustomerName',
                   date='OrderDate', cat='SalesChannel', amt='OrderTotal', ev='order', evs='orders', pt='customer', pts='customers', amtn='order total', status='OrderStatus'),
    'retail_inventory': dict(s='retail_inventory', E='StockMovements', id='MovementID', P='Warehouses', fk='WarehouseID', name='WarehouseName',
                             date='MovementDate', cat='MovementCategory', amt='MovementValue', ev='stock movement', evs='stock movements', pt='warehouse', pts='warehouses', amtn='movement value'),
    'retail_logistics': dict(s='retail_logistics', E='Shipments', id='ShipmentID', P='Customers', fk='CustomerID', name='CustomerName',
                             date='ShipDate', cat='ShipmentCategory', amt='FreightCharge', ev='shipment', evs='shipments', pt='customer', pts='customers', amtn='freight charge'),
    'retail_manufacturing': dict(s='retail_manufacturing', E='ProductionOrders', id='ProductionOrderID', P='Products', fk='ProductID', name='ProductName',
                                 date='ProductionDate', cat='ProductionCategory', amt='PlannedCost', ev='production order', evs='production orders', pt='product', pts='products', amtn='planned cost'),
}
for _g in G.values():
    _g.setdefault('status', 'WorkflowStatus' if _g['s'] == 'brokerage' else 'Status')


def quick(g, days):
    return (f"Quick repeat {g['evs']}",
            f"A *quick repeat* is {'an' if g['ev'][0] in 'aeiou' else 'a'} {g['ev']} that comes {days} days or less after the same {g['pt']}'s previous {g['ev']}. "
            f"For every {g['pt']} with at least one quick repeat, show {g['fk']}, {g['name']}, QuickRepeats (how many) and "
            f"ShortestGapDays (the smallest gap in days between two of their consecutive {g['evs']}). "
            f"Sort by QuickRepeats descending, then ShortestGapDays, then {g['fk']}.",
            f"""WITH e AS (
    SELECT {g['fk']},
           DATEDIFF(day, LAG({g['date']}) OVER (PARTITION BY {g['fk']} ORDER BY {g['date']}, {g['id']}), {g['date']}) AS GapDays
    FROM {g['s']}.{g['E']}
)
SELECT p.{g['fk']}, p.{g['name']}, COUNT(*) AS QuickRepeats, MIN(e.GapDays) AS ShortestGapDays
FROM e
JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = e.{g['fk']}
WHERE e.GapDays <= {days}
GROUP BY p.{g['fk']}, p.{g['name']}
ORDER BY QuickRepeats DESC, ShortestGapDays, p.{g['fk']};""",
            f"LAG({g['date']}) OVER (PARTITION BY {g['fk']} ORDER BY {g['date']}) gives each row the previous date for the same {g['pt']}. "
            "Compute the gap in a CTE first: a window function cannot go in WHERE.")


def median(g):
    return (f"Median vs average {g['amtn']}",
            f"Averages hide outliers. For each {g['cat']}, show {g['cat']}, {g['E']} (how many {g['evs']}), AverageValue, MedianValue "
            f"and AboveMedian (AverageValue minus MedianValue), all money values rounded to 2 decimals. "
            f"Use the {g['amt']} column. Sort by {g['cat']}.",
            f"""WITH m AS (
    SELECT DISTINCT {g['cat']},
           COUNT(*) OVER (PARTITION BY {g['cat']}) AS {g['E']},
           AVG({g['amt']}) OVER (PARTITION BY {g['cat']}) AS AvgV,
           PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY {g['amt']}) OVER (PARTITION BY {g['cat']}) AS MedV
    FROM {g['s']}.{g['E']}
)
SELECT {g['cat']}, {g['E']},
       CAST(AvgV AS decimal(12,2)) AS AverageValue,
       CAST(MedV AS decimal(12,2)) AS MedianValue,
       CAST(AvgV - MedV AS decimal(12,2)) AS AboveMedian
FROM m
ORDER BY {g['cat']};""",
            "PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ...) OVER (PARTITION BY ...) returns the median on every row of the group; "
            "SELECT DISTINCT collapses it to one row per group. When the median is far below the average, a few large values pull the average up.")


def mtd(g):
    return ("Month-to-date running total",
            f"For Closed {g['evs']} only, show each {g['date']} with DayTotal (the sum of {g['amt']} that day) and MonthToDate: "
            f"the running total that starts again on the first day of each month. Sort by {g['date']}.",
            f"""WITH d AS (
    SELECT {g['date']}, SUM({g['amt']}) AS DayTotal
    FROM {g['s']}.{g['E']}
    WHERE {g['status']} = 'Closed'
    GROUP BY {g['date']}
)
SELECT {g['date']}, DayTotal,
       SUM(DayTotal) OVER (PARTITION BY YEAR({g['date']}), MONTH({g['date']})
                           ORDER BY {g['date']} ROWS UNBOUNDED PRECEDING) AS MonthToDate
FROM d
ORDER BY {g['date']};""",
            "Aggregate to one row per day first, then SUM() OVER (PARTITION BY year and month ORDER BY date). "
            "The PARTITION BY is what makes the total restart each month.")


def pareto(g):
    return (f"The {g['pts']} behind half of all value",
            f"Rank {g['pts']} by their total {g['amtn']} (all {g['evs']}). Show the smallest group of top {g['pts']} that together "
            f"make up at least 50% of the grand total: {g['fk']}, {g['name']}, Total and CumulativePct (their running share of the "
            f"grand total, 2 decimals). Break ties in Total by {g['fk']}. Sort by Total descending, then {g['fk']}.",
            f"""WITH t AS (
    SELECT {g['fk']}, SUM({g['amt']}) AS Total
    FROM {g['s']}.{g['E']}
    GROUP BY {g['fk']}
), r AS (
    SELECT {g['fk']}, Total,
           SUM(Total) OVER (ORDER BY Total DESC, {g['fk']} ROWS UNBOUNDED PRECEDING) AS Running,
           SUM(Total) OVER () AS Grand
    FROM t
)
SELECT r.{g['fk']}, p.{g['name']}, r.Total, CAST(100.0 * r.Running / r.Grand AS decimal(5,2)) AS CumulativePct
FROM r
JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = r.{g['fk']}
WHERE r.Running - r.Total < 0.5 * r.Grand
ORDER BY r.Total DESC, r.{g['fk']};""",
            "Total per group, then a running SUM() OVER (ORDER BY Total DESC). Keep a row while the running total *before* it "
            "(Running minus Total) is still under half: that includes the row that crosses the line.")


def cohort(g, days):
    return ("First-month cohort retention",
            f"Group {g['pts']} by the month of their first {g['ev']}. For each first month show FirstMonth (yyyy-MM), "
            f"New{g['P'].replace('Brokerage', '')} (how many {g['pts']} started that month), ReturnedWithin{days} "
            f"(how many had another {g['ev']} on a later date within {days} days of their first one) and RetentionPct (2 decimals). "
            "Sort by FirstMonth.",
            f"""WITH e AS (
    SELECT {g['fk']}, {g['date']}, MIN({g['date']}) OVER (PARTITION BY {g['fk']}) AS FirstDate
    FROM {g['s']}.{g['E']}
), c AS (
    SELECT {g['fk']}, FirstDate,
           MAX(CASE WHEN {g['date']} > FirstDate AND {g['date']} <= DATEADD(day, {days}, FirstDate) THEN 1 ELSE 0 END) AS Returned
    FROM e
    GROUP BY {g['fk']}, FirstDate
)
SELECT FORMAT(FirstDate, 'yyyy-MM') AS FirstMonth,
       COUNT(*) AS New{g['P'].replace('Brokerage', '')},
       SUM(Returned) AS ReturnedWithin{days},
       CAST(100.0 * SUM(Returned) / COUNT(*) AS decimal(5,2)) AS RetentionPct
FROM c
GROUP BY FORMAT(FirstDate, 'yyyy-MM')
ORDER BY FirstMonth;""",
            f"Step 1: MIN(date) OVER (PARTITION BY {g['fk']}) tags every row with that {g['pt']}'s first date. "
            f"Step 2: one row per {g['pt']} with a 1/0 flag (MAX of a CASE). Step 3: group by the first month.")


def streak(g, months):
    return ("Longest monthly streak (gaps and islands)",
            f"For each {g['pt']}, find runs of consecutive calendar months that each have at least one {g['ev']}. "
            f"Show every run of {months} or more months: {g['fk']}, {g['name']}, StreakStart and StreakEnd (yyyy-MM) and Months. "
            f"Sort by Months descending, then StreakStart, then {g['fk']}.",
            f"""WITH m AS (
    SELECT DISTINCT {g['fk']}, DATEFROMPARTS(YEAR({g['date']}), MONTH({g['date']}), 1) AS MonthStart
    FROM {g['s']}.{g['E']}
), g AS (
    SELECT {g['fk']}, MonthStart,
           DATEADD(month, -ROW_NUMBER() OVER (PARTITION BY {g['fk']} ORDER BY MonthStart), MonthStart) AS Island
    FROM m
), r AS (
    SELECT {g['fk']}, MIN(MonthStart) AS StreakStart, MAX(MonthStart) AS StreakEnd, COUNT(*) AS Months
    FROM g
    GROUP BY {g['fk']}, Island
)
SELECT r.{g['fk']}, p.{g['name']}, FORMAT(r.StreakStart, 'yyyy-MM') AS StreakStart,
       FORMAT(r.StreakEnd, 'yyyy-MM') AS StreakEnd, r.Months
FROM r
JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = r.{g['fk']}
WHERE r.Months >= {months}
ORDER BY r.Months DESC, r.StreakStart, r.{g['fk']};""",
            "The classic gaps-and-islands trick: reduce dates to distinct months, then subtract ROW_NUMBER() months from each month. "
            "Consecutive months get the same result, so GROUP BY that value gives one row per streak.")


def transitions(g):
    return (f"What comes next? {g['cat']} transitions",
            f"Put each {g['pt']}'s {g['evs']} in date order (ties by {g['id']}). For every pair of consecutive {g['evs']}, "
            f"the first one's {g['cat']} is the From value and the next one's is the To value. Show From{g['cat']}, To{g['cat']}, "
            f"Transitions (how many times) and PctOfFrom (share of all transitions that start from that From value, 2 decimals). "
            f"Sort by From{g['cat']}, then To{g['cat']}.",
            f"""WITH e AS (
    SELECT {g['cat']} AS FromV,
           LEAD({g['cat']}) OVER (PARTITION BY {g['fk']} ORDER BY {g['date']}, {g['id']}) AS ToV
    FROM {g['s']}.{g['E']}
)
SELECT FromV AS From{g['cat']}, ToV AS To{g['cat']}, COUNT(*) AS Transitions,
       CAST(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY FromV) AS decimal(5,2)) AS PctOfFrom
FROM e
WHERE ToV IS NOT NULL
GROUP BY FromV, ToV
ORDER BY From{g['cat']}, To{g['cat']};""",
            "LEAD() looks at the next row in the same partition. The last row per partition has no next value, so filter out the NULLs. "
            "SUM(COUNT(*)) OVER (PARTITION BY ...) is a window over the grouped result: it gives the group total for the percentage.")


def longest_gap(g):
    return ("Longest quiet period per region",
            f"For each Region (from {g['P']}), find the longest stretch with no {g['evs']} at all between two consecutive "
            f"{g['ev']} dates in that region. Show Region, GapStart (the last date before the gap), GapEnd (the next date) and "
            "DaysWithout. If two gaps tie for longest in a region, show both. Sort by DaysWithout descending, then Region, then GapStart.",
            f"""WITH d AS (
    SELECT p.Region, e.{g['date']} AS GapEnd,
           LAG(e.{g['date']}) OVER (PARTITION BY p.Region ORDER BY e.{g['date']}, e.{g['id']}) AS GapStart
    FROM {g['s']}.{g['E']} AS e
    JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = e.{g['fk']}
), r AS (
    SELECT Region, GapStart, GapEnd, DATEDIFF(day, GapStart, GapEnd) AS DaysWithout,
           RANK() OVER (PARTITION BY Region ORDER BY DATEDIFF(day, GapStart, GapEnd) DESC) AS rk
    FROM d
    WHERE GapStart IS NOT NULL
)
SELECT Region, GapStart, GapEnd, DaysWithout
FROM r
WHERE rk = 1
ORDER BY DaysWithout DESC, Region, GapStart;""",
            "LAG over the region's dates gives the previous date; DATEDIFF gives the gap. RANK() (not ROW_NUMBER) keeps ties for the top spot.")


def mom(g, jump=50):
    return ("Month-over-month jumps per region",
            f"Total the {g['amt']} per Region (from {g['P']}) and calendar month. Compare each month with the region's *previous "
            f"calendar month* (if the region had nothing that month, there is nothing to compare). Show Region, Month (yyyy-MM), "
            f"MonthTotal, PrevMonthTotal and GrowthPct (2 decimals) for every jump of {jump}% or more. "
            "Sort by GrowthPct descending, then Region, then Month.",
            f"""WITH m AS (
    SELECT p.Region, DATEFROMPARTS(YEAR(e.{g['date']}), MONTH(e.{g['date']}), 1) AS MonthStart, SUM(e.{g['amt']}) AS MonthTotal
    FROM {g['s']}.{g['E']} AS e
    JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = e.{g['fk']}
    GROUP BY p.Region, DATEFROMPARTS(YEAR(e.{g['date']}), MONTH(e.{g['date']}), 1)
), l AS (
    SELECT Region, MonthStart, MonthTotal,
           LAG(MonthTotal) OVER (PARTITION BY Region ORDER BY MonthStart) AS PrevMonthTotal,
           LAG(MonthStart) OVER (PARTITION BY Region ORDER BY MonthStart) AS PrevMonth
    FROM m
)
SELECT Region, FORMAT(MonthStart, 'yyyy-MM') AS Month, MonthTotal, PrevMonthTotal,
       CAST(100.0 * (MonthTotal - PrevMonthTotal) / PrevMonthTotal AS decimal(9,2)) AS GrowthPct
FROM l
WHERE PrevMonth = DATEADD(month, -1, MonthStart)
  AND MonthTotal >= PrevMonthTotal * {1 + jump / 100}
ORDER BY GrowthPct DESC, Region, Month;""",
            "LAG() returns the previous row, which is not always the previous calendar month. Bring back the previous month's date "
            "with a second LAG and check it equals DATEADD(month, -1, this month).")


def rank_shift(g, places=10):
    return ("Climbers and fallers: H1 vs H2 rank",
            f"Rank {g['pts']} by their total {g['amt']} in the first half of 2024 (January to June) and again in the second half "
            f"(July to December), using RANK() with 1 = highest. Only include {g['pts']} with {g['evs']} in both halves. Show "
            f"{g['fk']}, {g['name']}, H1Rank, H2Rank and Moved (H1Rank minus H2Rank, so positive means it climbed) for those that "
            f"moved {places} or more places either way. Sort by Moved descending, then {g['fk']}.",
            f"""WITH h AS (
    SELECT {g['fk']},
           SUM(CASE WHEN {g['date']} < '2024-07-01' THEN {g['amt']} END) AS H1,
           SUM(CASE WHEN {g['date']} >= '2024-07-01' THEN {g['amt']} END) AS H2
    FROM {g['s']}.{g['E']}
    GROUP BY {g['fk']}
), r AS (
    SELECT {g['fk']}, RANK() OVER (ORDER BY H1 DESC) AS H1Rank, RANK() OVER (ORDER BY H2 DESC) AS H2Rank
    FROM h
    WHERE H1 IS NOT NULL AND H2 IS NOT NULL
)
SELECT r.{g['fk']}, p.{g['name']}, r.H1Rank, r.H2Rank, r.H1Rank - r.H2Rank AS Moved
FROM r
JOIN {g['s']}.{g['P']} AS p ON p.{g['fk']} = r.{g['fk']}
WHERE ABS(r.H1Rank - r.H2Rank) >= {places}
ORDER BY Moved DESC, r.{g['fk']};""",
            "Pivot the two halves into columns with SUM(CASE ...) in one pass, filter to rows that have both, and only then rank. "
            "Ranking before the filter would give different rank numbers.")


def quartiles(g):
    return ("Value tiers with NTILE",) + quartiles_body(g, g['P'].replace('Brokerage', ''))


def quartiles_body(g, col):
    return (f"Split the {g['pts']} that have {g['evs']} into 4 equal-sized tiers by total {g['amt']} with NTILE(4), tier 1 = highest "
            f"(ties broken by {g['fk']}). For each tier show Tier, {col} (how many), MinTotal, MaxTotal, TierTotal and ShareOfAllPct "
            "(the tier's share of the grand total, 2 decimals). Sort by Tier.",
            f"""WITH t AS (
    SELECT {g['fk']}, SUM({g['amt']}) AS Total
    FROM {g['s']}.{g['E']}
    GROUP BY {g['fk']}
), n AS (
    SELECT {g['fk']}, Total, NTILE(4) OVER (ORDER BY Total DESC, {g['fk']}) AS Tier
    FROM t
)
SELECT Tier, COUNT(*) AS {col}, MIN(Total) AS MinTotal, MAX(Total) AS MaxTotal, SUM(Total) AS TierTotal,
       CAST(100.0 * SUM(Total) / SUM(SUM(Total)) OVER () AS decimal(5,2)) AS ShareOfAllPct
FROM n
GROUP BY Tier
ORDER BY Tier;""",
            "NTILE(4) OVER (ORDER BY ...) deals rows into 4 buckets. After GROUP BY Tier, SUM(SUM(Total)) OVER () is the grand total "
            "across all tiers, so the share needs no second query.")

MEDS_NEVER = ("Medications nobody was prescribed",
              "List medications that appear in no prescription at all, with MedicationName, MedicationCode, UnitCost and "
              "PriceRank (the medication's rank by UnitCost among *all* medications, 1 = most expensive, ties share a rank). "
              "Sort by PriceRank, then MedicationName.",
              """WITH r AS (
    SELECT MedicationID, MedicationName, MedicationCode, UnitCost,
           RANK() OVER (ORDER BY UnitCost DESC) AS PriceRank
    FROM healthcare.Medications
)
SELECT r.MedicationName, r.MedicationCode, r.UnitCost, r.PriceRank
FROM r
WHERE NOT EXISTS (SELECT 1 FROM healthcare.Prescriptions AS rx WHERE rx.MedicationID = r.MedicationID)
ORDER BY r.PriceRank, r.MedicationName;""",
              "Rank first over all medications, then filter with NOT EXISTS. Filtering first would rank only the unused ones "
              "and give different numbers: order of operations matters.")

PEAK_STOCK = ("Peak stock level per warehouse",
              "A warehouse's stock level starts at the sum of its OpeningQuantity in StockBalances. Apply its Closed movements in "
              "MovedAt order (IN adds MovedUnits, OUT subtracts). For each warehouse with movements, show WarehouseName, Opening, "
              "PeakLevel (highest level reached after any movement), PeakAt (MovedAt of the first time it reached that peak) and "
              "EndLevel (level after its last movement). Show the 10 warehouses with the highest PeakLevel (ties by WarehouseName). "
              "Sort by PeakLevel descending, then WarehouseName.",
              """WITH o AS (
    SELECT WarehouseID, SUM(OpeningQuantity) AS Opening
    FROM retail_inventory.StockBalances
    GROUP BY WarehouseID
), r AS (
    SELECT m.WarehouseID, m.MovedAt, m.MovementID, o.Opening,
           o.Opening + SUM(CASE WHEN m.Direction = 'IN' THEN m.MovedUnits ELSE -m.MovedUnits END)
               OVER (PARTITION BY m.WarehouseID ORDER BY m.MovedAt, m.MovementID ROWS UNBOUNDED PRECEDING) AS Level
    FROM retail_inventory.StockMovements AS m
    JOIN o ON o.WarehouseID = m.WarehouseID
    WHERE m.Status = 'Closed'
), s AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY WarehouseID ORDER BY Level DESC, MovedAt, MovementID) AS PeakN,
           ROW_NUMBER() OVER (PARTITION BY WarehouseID ORDER BY MovedAt DESC, MovementID DESC) AS LastN
    FROM r
), w AS (
    SELECT WarehouseID, MAX(Opening) AS Opening,
           MAX(CASE WHEN PeakN = 1 THEN Level END) AS PeakLevel,
           MAX(CASE WHEN PeakN = 1 THEN MovedAt END) AS PeakAt,
           MAX(CASE WHEN LastN = 1 THEN Level END) AS EndLevel
    FROM s
    GROUP BY WarehouseID
)
SELECT TOP (10) wh.WarehouseName, w.Opening, w.PeakLevel, w.PeakAt, w.EndLevel
FROM w
JOIN retail_inventory.Warehouses AS wh ON wh.WarehouseID = w.WarehouseID
ORDER BY w.PeakLevel DESC, wh.WarehouseName;""",
              "Signed running SUM() OVER (PARTITION BY warehouse ORDER BY time) plus the opening stock gives the level after every "
              "movement. Then two ROW_NUMBERs pick the peak row and the last row, and MAX(CASE ...) folds them into one row.")


# ---------------------------------------------------------------------------------------------------------------
# Domain-specific challenges
# ---------------------------------------------------------------------------------------------------------------
def retail():
    g = G['retail']
    return [
        quick(g, 14),
        median(g),
        mtd(g),
        ("Payment reconciliation",
         "Compare each order's OrderTotal with the total of its payments. List every order that is not settled exactly: "
         "OrderID, OrderTotal, Paid (0 when there is no payment), Difference (OrderTotal minus Paid) and PaymentState "
         "('Unpaid', 'Underpaid' or 'Overpaid'). Sort by PaymentState, then Difference descending, then OrderID.",
         """WITH p AS (
    SELECT OrderID, SUM(PaidAmount) AS Paid
    FROM retail.Payments
    GROUP BY OrderID
)
SELECT o.OrderID, o.OrderTotal, COALESCE(p.Paid, 0) AS Paid,
       o.OrderTotal - COALESCE(p.Paid, 0) AS Difference,
       CASE WHEN p.Paid IS NULL THEN 'Unpaid'
            WHEN p.Paid < o.OrderTotal THEN 'Underpaid'
            ELSE 'Overpaid' END AS PaymentState
FROM retail.Orders AS o
LEFT JOIN p ON p.OrderID = o.OrderID
WHERE COALESCE(p.Paid, 0) <> o.OrderTotal
ORDER BY PaymentState, Difference DESC, o.OrderID;""",
         "An order can have several payments, so total them per order in a CTE before joining. LEFT JOIN keeps orders with no payment, "
         "and COALESCE turns their NULL into 0."),
        ("Fan-out trap: one report, three totals",
         "For each customer Region show Orders, Revenue (sum of OrderTotal), ItemsSold (sum of OrderItems.Quantity) and Paid "
         "(sum of Payments.PaidAmount). Every number must be right. Sort by Revenue descending.",
         """WITH i AS (
    SELECT OrderID, SUM(Quantity) AS Qty FROM retail.OrderItems GROUP BY OrderID
), p AS (
    SELECT OrderID, SUM(PaidAmount) AS Paid FROM retail.Payments GROUP BY OrderID
)
SELECT c.Region, COUNT(*) AS Orders, SUM(o.OrderTotal) AS Revenue,
       SUM(COALESCE(i.Qty, 0)) AS ItemsSold, SUM(COALESCE(p.Paid, 0)) AS Paid
FROM retail.Orders AS o
JOIN retail.Customers AS c ON c.CustomerID = o.CustomerID
LEFT JOIN i ON i.OrderID = o.OrderID
LEFT JOIN p ON p.OrderID = o.OrderID
GROUP BY c.Region
ORDER BY Revenue DESC;""",
         "Joining Orders to OrderItems and Payments in one go repeats each order once per item *and* per payment, which inflates "
         "Revenue and Paid. Pre-aggregate each child table to one row per order, then join."),
        ("Bought together",
         "Find pairs of different products that appear in the same order in at least 2 orders. Show ProductA and ProductB "
         "(names; ProductA is the one with the smaller ProductID) and TimesTogether. Sort by TimesTogether descending, then ProductA, then ProductB.",
         """SELECT pa.ProductName AS ProductA, pb.ProductName AS ProductB, COUNT(DISTINCT a.OrderID) AS TimesTogether
FROM retail.OrderItems AS a
JOIN retail.OrderItems AS b ON b.OrderID = a.OrderID AND b.ProductID > a.ProductID
JOIN retail.Products AS pa ON pa.ProductID = a.ProductID
JOIN retail.Products AS pb ON pb.ProductID = b.ProductID
GROUP BY a.ProductID, b.ProductID, pa.ProductName, pb.ProductName
HAVING COUNT(DISTINCT a.OrderID) >= 2
ORDER BY TimesTogether DESC, ProductA, ProductB;""",
         "Self-join OrderItems on the same OrderID. The condition b.ProductID > a.ProductID removes self-pairs and keeps each pair once (A,B but not B,A)."),
        pareto(g),
        cohort(g, 90),
        streak(g, 3),
        ("Top 3 products per region, ties included",
         "For each customer Region, rank products by revenue (Quantity × UnitPrice from OrderItems). Show the top 3 ranks, "
         "keeping ties (two products with the same revenue share a rank and the next rank is not skipped): Region, RankInRegion, "
         "ProductName and Revenue. Sort by Region, RankInRegion, ProductName.",
         """WITH s AS (
    SELECT c.Region, p.ProductID, p.ProductName, SUM(i.Quantity * i.UnitPrice) AS Revenue
    FROM retail.OrderItems AS i
    JOIN retail.Orders AS o ON o.OrderID = i.OrderID
    JOIN retail.Customers AS c ON c.CustomerID = o.CustomerID
    JOIN retail.Products AS p ON p.ProductID = i.ProductID
    GROUP BY c.Region, p.ProductID, p.ProductName
), r AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY Region ORDER BY Revenue DESC) AS RankInRegion
    FROM s
)
SELECT Region, RankInRegion, ProductName, Revenue
FROM r
WHERE RankInRegion <= 3
ORDER BY Region, RankInRegion, ProductName;""",
         "Four tables lead from Region to product revenue. DENSE_RANK keeps ties without gaps; ROW_NUMBER would drop tied products "
         "and RANK would skip a rank after a tie."),
    ]


def banking():
    g = G['banking']
    return [
        quick(g, 7),
        median(g),
        mtd(g),
        pareto(g),
        transitions(g),
        ("Loans vs activity: the double-count trap",
         "For each customer who has at least one loan, show CustomerID, CustomerName, Loans (count), TotalPrincipal, "
         "Transactions (count, across all their accounts) and TotalTransacted (sum of Amount). Sort by TotalPrincipal descending, then CustomerID.",
         """WITH l AS (
    SELECT CustomerID, COUNT(*) AS Loans, SUM(Principal) AS TotalPrincipal
    FROM banking.Loans
    GROUP BY CustomerID
), t AS (
    SELECT a.CustomerID, COUNT(*) AS Transactions, SUM(x.Amount) AS TotalTransacted
    FROM banking.Transactions AS x
    JOIN banking.Accounts AS a ON a.AccountID = x.AccountID
    GROUP BY a.CustomerID
)
SELECT c.CustomerID, c.CustomerName, l.Loans, l.TotalPrincipal,
       COALESCE(t.Transactions, 0) AS Transactions, COALESCE(t.TotalTransacted, 0) AS TotalTransacted
FROM l
JOIN banking.Customers AS c ON c.CustomerID = l.CustomerID
LEFT JOIN t ON t.CustomerID = l.CustomerID
ORDER BY l.TotalPrincipal DESC, c.CustomerID;""",
         "Loans and transactions are two separate one-to-many branches under the customer. Joining both at once multiplies rows; "
         "aggregate each branch to one row per customer first."),
        ("Dormant accounts",
         "Take the latest TransactionDate in the whole table as 'today'. List accounts that had at least one transaction but none "
         "in the 90 days up to and including today. Show AccountID, AccountName, Region, LastTransaction and DaysSilent "
         "(days from LastTransaction to today). Sort by DaysSilent descending, then AccountID.",
         """WITH today AS (
    SELECT MAX(TransactionDate) AS D FROM banking.Transactions
), last AS (
    SELECT AccountID, MAX(TransactionDate) AS LastTransaction
    FROM banking.Transactions
    GROUP BY AccountID
)
SELECT a.AccountID, a.AccountName, a.Region, l.LastTransaction,
       DATEDIFF(day, l.LastTransaction, t.D) AS DaysSilent
FROM last AS l
CROSS JOIN today AS t
JOIN banking.Accounts AS a ON a.AccountID = l.AccountID
WHERE l.LastTransaction < DATEADD(day, -90, t.D)
ORDER BY DaysSilent DESC, a.AccountID;""",
         "Find 'today' from the data, not GETDATE(), so the answer never changes. One row per account with its last date, "
         "then compare with a CROSS JOIN to the single 'today' row."),
        ("Highest-rate loan in each city, ties included",
         "Loans link to an account, and the account to a branch. For each branch City, show the loan(s) with the highest AnnualRate: "
         "City, LoanReference, BranchName, AnnualRate and Principal. Keep ties. Sort by City, then LoanReference.",
         """WITH r AS (
    SELECT b.City, l.LoanReference, b.BranchName, l.AnnualRate, l.Principal,
           RANK() OVER (PARTITION BY b.City ORDER BY l.AnnualRate DESC) AS rk
    FROM banking.Loans AS l
    JOIN banking.Accounts AS a ON a.AccountID = l.AccountID
    JOIN banking.Branches AS b ON b.BranchID = a.BranchID
)
SELECT City, LoanReference, BranchName, AnnualRate, Principal
FROM r
WHERE rk = 1
ORDER BY City, LoanReference;""",
         "Top-1 per group with ties is RANK() = 1 (or DENSE_RANK). The path Loans → Accounts → Branches gets you from loan to city."),
        streak(g, 3),
        longest_gap(g),
    ]


def brokerage():
    g = G['brokerage']
    return [
        quick(g, 7),
        median(g),
        mtd(g),
        pareto(g),
        transitions(g),
        ("Fill status of every order",
         "Compare each trade order's RequestedQuantity with the total ExecutedQuantity of its executions. Classify orders as "
         "'Unfilled' (no executions), 'Partial' (less than requested), 'Filled' (exactly requested) or 'Overfilled'. "
         "Show FillStatus, Orders and AvgFillPct (average of executed ÷ requested × 100 per order, 2 decimals). Sort by FillStatus.",
         """WITH x AS (
    SELECT OrderID, SUM(ExecutedQuantity) AS Done
    FROM brokerage.Executions
    GROUP BY OrderID
), f AS (
    SELECT o.OrderID, o.RequestedQuantity, COALESCE(x.Done, 0) AS Done,
           CASE WHEN x.Done IS NULL THEN 'Unfilled'
                WHEN x.Done < o.RequestedQuantity THEN 'Partial'
                WHEN x.Done = o.RequestedQuantity THEN 'Filled'
                ELSE 'Overfilled' END AS FillStatus
    FROM brokerage.TradeOrders AS o
    LEFT JOIN x ON x.OrderID = o.OrderID
)
SELECT FillStatus, COUNT(*) AS Orders,
       CAST(AVG(100.0 * Done / RequestedQuantity) AS decimal(7,2)) AS AvgFillPct
FROM f
GROUP BY FillStatus
ORDER BY FillStatus;""",
         "Sum executions per order first, LEFT JOIN so orders with no execution stay, then a CASE builds the label you group by."),
        ("VWAP vs simple average price",
         "For each security with executions, show Symbol, Executions, SimpleAvgPrice (plain average of ExecutionPrice), "
         "VWAP (volume-weighted average price: sum of quantity × price ÷ sum of quantity) and DiffPct ((VWAP − SimpleAvgPrice) ÷ "
         "SimpleAvgPrice × 100). Round prices to 4 decimals and DiffPct to 2. Show only securities where the absolute DiffPct is at "
         "least 1. Sort by absolute DiffPct descending, then Symbol.",
         """WITH v AS (
    SELECT s.Symbol, COUNT(*) AS Executions,
           AVG(e.ExecutionPrice) AS AvgP,
           SUM(e.ExecutedQuantity * e.ExecutionPrice) / SUM(e.ExecutedQuantity) AS Vwap
    FROM brokerage.Executions AS e
    JOIN brokerage.TradeOrders AS o ON o.OrderID = e.OrderID
    JOIN brokerage.Securities AS s ON s.SecurityID = o.SecurityID
    GROUP BY s.Symbol
)
SELECT Symbol, Executions,
       CAST(AvgP AS decimal(12,4)) AS SimpleAvgPrice,
       CAST(Vwap AS decimal(12,4)) AS VWAP,
       CAST(100.0 * (Vwap - AvgP) / AvgP AS decimal(7,2)) AS DiffPct
FROM v
WHERE ABS(100.0 * (Vwap - AvgP) / AvgP) >= 1
ORDER BY ABS(100.0 * (Vwap - AvgP) / AvgP) DESC, Symbol;""",
         "VWAP is a ratio of two sums, not an average of ratios. Executions reach a security only through TradeOrders."),
        quartiles(g),
        ("Clients who hold both stocks and ETFs",
         "List clients who have traded at least one 'Stock' and at least one 'ETF' (any account of theirs). Show ClientID, ClientName, "
         "Stocks and ETFs (how many different securities of each class) and TotalOrders. Sort by TotalOrders descending, then ClientID.",
         """SELECT c.ClientID, c.ClientName,
       COUNT(DISTINCT CASE WHEN s.AssetClass = 'Stock' THEN s.SecurityID END) AS Stocks,
       COUNT(DISTINCT CASE WHEN s.AssetClass = 'ETF' THEN s.SecurityID END) AS ETFs,
       COUNT(*) AS TotalOrders
FROM brokerage.TradeOrders AS o
JOIN brokerage.BrokerageAccounts AS a ON a.AccountID = o.AccountID
JOIN brokerage.Clients AS c ON c.ClientID = a.ClientID
JOIN brokerage.Securities AS s ON s.SecurityID = o.SecurityID
GROUP BY c.ClientID, c.ClientName
HAVING COUNT(DISTINCT CASE WHEN s.AssetClass = 'Stock' THEN s.SecurityID END) > 0
   AND COUNT(DISTINCT CASE WHEN s.AssetClass = 'ETF' THEN s.SecurityID END) > 0
ORDER BY TotalOrders DESC, c.ClientID;""",
         "Conditional aggregation: COUNT(DISTINCT CASE WHEN ... THEN id END) counts one class at a time. "
         "Put the 'both' test in HAVING, after grouping."),
        longest_gap(g),
    ]


def oil():
    g = G['oil']
    return [
        quick(g, 7),
        median(g),
        mtd(g),
        pareto(g),
        streak(g, 3),
        transitions(g),
        mom(g),
        rank_shift(g),
        ("Three-product bundles",
         "Take the 6 products with the most units shipped (ties broken by ProductID). List every bundle of 3 different products from "
         "those 6 with the bundle's catalog price (sum of the three PricePerUnit values). Show Product1, Product2, Product3 (in "
         "ProductID order within the bundle) and BundlePrice. Sort by BundlePrice descending, then Product1, Product2, Product3.",
         """WITH top6 AS (
    SELECT TOP (6) p.ProductID, p.ProductName, p.PricePerUnit
    FROM oil.ShipmentItems AS i
    JOIN oil.Products AS p ON p.ProductID = i.ProductID
    GROUP BY p.ProductID, p.ProductName, p.PricePerUnit
    ORDER BY SUM(i.Quantity) DESC, p.ProductID
)
SELECT a.ProductName AS Product1, b.ProductName AS Product2, c.ProductName AS Product3,
       a.PricePerUnit + b.PricePerUnit + c.PricePerUnit AS BundlePrice
FROM top6 AS a
JOIN top6 AS b ON b.ProductID > a.ProductID
JOIN top6 AS c ON c.ProductID > b.ProductID
ORDER BY BundlePrice DESC, Product1, Product2, Product3;""",
         "Combinations come from a triple self-join with a < b < c on the ID: that lists each set of three exactly once (6 choose 3 = 20 rows)."),
        ("Each region's busiest carrier, ties included",
         "For each site Region, find the carrier(s) that handled the most shipments there. Show Region, CarrierName, Shipments and "
         "ShareOfRegionPct (that carrier's shipments ÷ all shipments in the region × 100, 2 decimals). Keep ties. Sort by Region, then CarrierName.",
         """WITH c AS (
    SELECT st.Region, ca.CarrierName, COUNT(*) AS Shipments,
           SUM(COUNT(*)) OVER (PARTITION BY st.Region) AS RegionTotal,
           RANK() OVER (PARTITION BY st.Region ORDER BY COUNT(*) DESC) AS rk
    FROM oil.Shipments AS s
    JOIN oil.Sites AS st ON st.SiteID = s.SiteID
    JOIN oil.Carriers AS ca ON ca.CarrierID = s.CarrierID
    GROUP BY st.Region, ca.CarrierID, ca.CarrierName
)
SELECT Region, CarrierName, Shipments, CAST(100.0 * Shipments / RegionTotal AS decimal(5,2)) AS ShareOfRegionPct
FROM c
WHERE rk = 1
ORDER BY Region, CarrierName;""",
         "Window functions run after GROUP BY, so RANK() OVER (... ORDER BY COUNT(*)) and SUM(COUNT(*)) OVER (...) work in the same SELECT."),
    ]


def pharma():
    g = G['pharma']
    return [
        median(g),
        mtd(g),
        pareto(g),
        transitions(g),
        longest_gap(g),
        ("Warehouse utilisation",
         "Each warehouse has a Capacity. Using Inventory.QuantityOnHand, show WarehouseName, Capacity, OnHand, UtilisationPct "
         "(OnHand ÷ Capacity × 100, 2 decimals) and Band: 'Over capacity' (above 100%), 'Tight' (80–100%) or 'OK'. Include warehouses "
         "with no inventory (OnHand 0). Sort by UtilisationPct descending, then WarehouseName.",
         """WITH i AS (
    SELECT WarehouseID, SUM(QuantityOnHand) AS OnHand
    FROM pharma.Inventory
    GROUP BY WarehouseID
)
SELECT w.WarehouseName, w.Capacity, COALESCE(i.OnHand, 0) AS OnHand,
       CAST(100.0 * COALESCE(i.OnHand, 0) / w.Capacity AS decimal(7,2)) AS UtilisationPct,
       CASE WHEN 100.0 * COALESCE(i.OnHand, 0) / w.Capacity > 100 THEN 'Over capacity'
            WHEN 100.0 * COALESCE(i.OnHand, 0) / w.Capacity >= 80 THEN 'Tight'
            ELSE 'OK' END AS Band
FROM pharma.Warehouses AS w
LEFT JOIN i ON i.WarehouseID = w.WarehouseID
ORDER BY UtilisationPct DESC, w.WarehouseName;""",
         "Multiply by 100.0, not 100: integer ÷ integer in SQL Server drops the decimals. LEFT JOIN keeps empty warehouses."),
        mom(g),
        rank_shift(g),
        quartiles(g),
        ("Batches with no stock anywhere",
         "Per batch Status, show Batches, NotStocked (batches with no Inventory row at all), NotStockedPct (2 decimals) and "
         "NotStockedCost (sum of BatchCost of those batches). Sort by Status.",
         """WITH i AS (
    SELECT DISTINCT BatchID FROM pharma.Inventory
), f AS (
    SELECT b.Status, b.BatchCost, CASE WHEN i.BatchID IS NULL THEN 1 ELSE 0 END AS NotStocked
    FROM pharma.Batches AS b
    LEFT JOIN i ON i.BatchID = b.BatchID
)
SELECT Status, COUNT(*) AS Batches, SUM(NotStocked) AS NotStocked,
       CAST(100.0 * SUM(NotStocked) / COUNT(*) AS decimal(5,2)) AS NotStockedPct,
       SUM(CASE WHEN NotStocked = 1 THEN BatchCost ELSE 0 END) AS NotStockedCost
FROM f
GROUP BY Status
ORDER BY Status;""",
         "Reduce Inventory to one row per batch (DISTINCT), LEFT JOIN it and flag the NULLs. Joining raw Inventory rows would "
         "count stocked batches once per warehouse. SQL Server does not allow EXISTS inside SUM(), so build the flag first."),
    ]


def healthcare():
    g = G['healthcare']
    return [
        median(g),
        mtd(g),
        pareto(g),
        quartiles(g),
        longest_gap(g),
        ("Encounter charge vs medication cost",
         "For each encounter, the medication cost is the sum of Prescriptions.Quantity × Medications.UnitCost. Per EncounterType, show "
         "Encounters, WithPrescriptions (encounters that have at least one prescription), TotalCharge, MedicationCost and MedCostPct "
         "(MedicationCost ÷ TotalCharge × 100, 2 decimals). TotalCharge must count every encounter once. Sort by EncounterType.",
         """WITH m AS (
    SELECT rx.EncounterID, SUM(rx.Quantity * md.UnitCost) AS MedCost
    FROM healthcare.Prescriptions AS rx
    JOIN healthcare.Medications AS md ON md.MedicationID = rx.MedicationID
    GROUP BY rx.EncounterID
)
SELECT e.EncounterType, COUNT(*) AS Encounters, COUNT(m.EncounterID) AS WithPrescriptions,
       SUM(e.Charge) AS TotalCharge, COALESCE(SUM(m.MedCost), 0) AS MedicationCost,
       CAST(100.0 * COALESCE(SUM(m.MedCost), 0) / SUM(e.Charge) AS decimal(5,2)) AS MedCostPct
FROM healthcare.Encounters AS e
LEFT JOIN m ON m.EncounterID = e.EncounterID
GROUP BY e.EncounterType
ORDER BY e.EncounterType;""",
         "Joining Encounters straight to Prescriptions repeats the Charge once per prescription. Total the prescriptions per encounter "
         "first. COUNT(m.EncounterID) counts only matched rows."),
        mom(g),
        ("First vs latest charge per patient",
         "For each patient with 2 or more encounters, compare the charge of their first encounter with the charge of their latest one "
         "(by EncounterDate, ties by EncounterID). Show PatientID, PatientName, FirstCharge, LatestCharge and Change (latest minus first). "
         "Show only patients whose charge went up. Sort by Change descending, then PatientID.",
         """WITH e AS (
    SELECT PatientID, Charge,
           ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate, EncounterID) AS FirstN,
           ROW_NUMBER() OVER (PARTITION BY PatientID ORDER BY EncounterDate DESC, EncounterID DESC) AS LastN,
           COUNT(*) OVER (PARTITION BY PatientID) AS Visits
    FROM healthcare.Encounters
), f AS (
    SELECT PatientID,
           MAX(CASE WHEN FirstN = 1 THEN Charge END) AS FirstCharge,
           MAX(CASE WHEN LastN = 1 THEN Charge END) AS LatestCharge
    FROM e
    WHERE Visits >= 2
    GROUP BY PatientID
)
SELECT f.PatientID, p.PatientName, f.FirstCharge, f.LatestCharge, f.LatestCharge - f.FirstCharge AS Change
FROM f
JOIN healthcare.Patients AS p ON p.PatientID = f.PatientID
WHERE f.LatestCharge > f.FirstCharge
ORDER BY Change DESC, f.PatientID;""",
         "Number the rows both ways (oldest first and newest first), then pick row 1 of each with MAX(CASE ...). "
         "FIRST_VALUE / LAST_VALUE work too, but LAST_VALUE needs a full window frame."),
        ("Three-medication combinations",
         "Take the 6 medications prescribed in the most encounters (ties by MedicationID). List every combination of 3 of them with "
         "CombinationCost (sum of the three UnitCost values). Show Medication1, Medication2, Medication3 (in MedicationID order) and "
         "CombinationCost. Sort by CombinationCost descending, then Medication1, Medication2, Medication3.",
         """WITH top6 AS (
    SELECT TOP (6) m.MedicationID, m.MedicationName, m.UnitCost
    FROM healthcare.Prescriptions AS rx
    JOIN healthcare.Medications AS m ON m.MedicationID = rx.MedicationID
    GROUP BY m.MedicationID, m.MedicationName, m.UnitCost
    ORDER BY COUNT(DISTINCT rx.EncounterID) DESC, m.MedicationID
)
SELECT a.MedicationName AS Medication1, b.MedicationName AS Medication2, c.MedicationName AS Medication3,
       a.UnitCost + b.UnitCost + c.UnitCost AS CombinationCost
FROM top6 AS a
JOIN top6 AS b ON b.MedicationID > a.MedicationID
JOIN top6 AS c ON c.MedicationID > b.MedicationID
ORDER BY CombinationCost DESC, Medication1, Medication2, Medication3;""",
         "A triple self-join with a < b < c on the ID gives each set of three once: 6 choose 3 = 20 rows."),
        MEDS_NEVER,
    ]


def retail_logistics():
    g = G['retail_logistics']
    return [
        quick(g, 7),
        median(g),
        mtd(g),
        pareto(g),
        ("On-time delivery rate per carrier",
         "A package is on time when its Delivered scan happens on or before its PromisedDate. For each carrier show CarrierName, "
         "ServiceLevel, Delivered (packages with a Delivered scan), OnTime and OnTimePct (2 decimals). Only carriers with at least "
         "5 delivered packages. Sort by OnTimePct, then CarrierName.",
         """WITH d AS (
    SELECT PackageID, MIN(ScanTime) AS DeliveredAt
    FROM retail_logistics.TrackingEvents
    WHERE EventStatus = 'Delivered'
    GROUP BY PackageID
)
SELECT c.CarrierName, c.ServiceLevel, COUNT(*) AS Delivered,
       SUM(CASE WHEN CAST(d.DeliveredAt AS date) <= pk.PromisedDate THEN 1 ELSE 0 END) AS OnTime,
       CAST(100.0 * SUM(CASE WHEN CAST(d.DeliveredAt AS date) <= pk.PromisedDate THEN 1 ELSE 0 END) / COUNT(*) AS decimal(5,2)) AS OnTimePct
FROM d
JOIN retail_logistics.ShipmentPackages AS pk ON pk.PackageID = d.PackageID
JOIN retail_logistics.Shipments AS s ON s.ShipmentID = pk.ShipmentID
JOIN retail_logistics.Carriers AS c ON c.CarrierID = s.CarrierID
GROUP BY c.CarrierID, c.CarrierName, c.ServiceLevel
HAVING COUNT(*) >= 5
ORDER BY OnTimePct, c.CarrierName;""",
         "Get one delivered time per package first. ScanTime has a time part and PromisedDate does not: compare dates (CAST AS date), "
         "or a delivery at 10:00 on the promised day looks late."),
        ("Packages that never arrived",
         "List packages that have a PickedUp scan but no Delivered scan. Show TrackingNumber, CustomerName, PromisedDate, LastStatus "
         "(EventStatus of the latest scan), LastScan (its ScanTime) and LastLocation. Sort by PromisedDate, then TrackingNumber.",
         """WITH last AS (
    SELECT PackageID, EventStatus, ScanTime, LocationName,
           ROW_NUMBER() OVER (PARTITION BY PackageID ORDER BY ScanTime DESC, TrackingEventID DESC) AS rn
    FROM retail_logistics.TrackingEvents
)
SELECT pk.TrackingNumber, cu.CustomerName, pk.PromisedDate,
       l.EventStatus AS LastStatus, l.ScanTime AS LastScan, l.LocationName AS LastLocation
FROM retail_logistics.ShipmentPackages AS pk
JOIN retail_logistics.Shipments AS s ON s.ShipmentID = pk.ShipmentID
JOIN retail_logistics.Customers AS cu ON cu.CustomerID = s.CustomerID
JOIN last AS l ON l.PackageID = pk.PackageID AND l.rn = 1
WHERE EXISTS (SELECT 1 FROM retail_logistics.TrackingEvents AS t WHERE t.PackageID = pk.PackageID AND t.EventStatus = 'PickedUp')
  AND NOT EXISTS (SELECT 1 FROM retail_logistics.TrackingEvents AS t WHERE t.PackageID = pk.PackageID AND t.EventStatus = 'Delivered')
ORDER BY pk.PromisedDate, pk.TrackingNumber;""",
         "EXISTS for 'has this scan', NOT EXISTS for 'has no such scan'. The latest scan per package is ROW_NUMBER() ... ORDER BY ScanTime DESC = 1."),
        quartiles(g),
        ("Pickup-to-delivery hours by service level",
         "For each delivered package, measure hours from its first PickedUp scan to its first Delivered scan. Per carrier ServiceLevel "
         "show Packages, AvgHours, MedianHours and MaxHours (all to 1 decimal). Sort by AvgHours.",
         """WITH p AS (
    SELECT t.PackageID,
           MIN(CASE WHEN t.EventStatus = 'PickedUp' THEN t.ScanTime END) AS PickedUp,
           MIN(CASE WHEN t.EventStatus = 'Delivered' THEN t.ScanTime END) AS Delivered
    FROM retail_logistics.TrackingEvents AS t
    GROUP BY t.PackageID
), h AS (
    SELECT c.ServiceLevel, DATEDIFF(minute, p.PickedUp, p.Delivered) / 60.0 AS Hours
    FROM p
    JOIN retail_logistics.ShipmentPackages AS pk ON pk.PackageID = p.PackageID
    JOIN retail_logistics.Shipments AS s ON s.ShipmentID = pk.ShipmentID
    JOIN retail_logistics.Carriers AS c ON c.CarrierID = s.CarrierID
    WHERE p.PickedUp IS NOT NULL AND p.Delivered IS NOT NULL
), m AS (
    SELECT DISTINCT ServiceLevel,
           COUNT(*) OVER (PARTITION BY ServiceLevel) AS Packages,
           AVG(Hours) OVER (PARTITION BY ServiceLevel) AS AvgH,
           PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Hours) OVER (PARTITION BY ServiceLevel) AS MedH,
           MAX(Hours) OVER (PARTITION BY ServiceLevel) AS MaxH
    FROM h
)
SELECT ServiceLevel, Packages, CAST(AvgH AS decimal(8,1)) AS AvgHours,
       CAST(MedH AS decimal(8,1)) AS MedianHours, CAST(MaxH AS decimal(8,1)) AS MaxHours
FROM m
ORDER BY AvgHours;""",
         "Pivot the scans onto one row per package with MIN(CASE WHEN status = ... THEN ScanTime END), then measure, then summarise."),
        ("Late deliveries in a customer's first 60 days",
         "For customers whose first shipment was in the first half of 2024 (January to June), look only at packages on their shipments "
         "dispatched within 60 days of that first shipment. Show CustomerID, CustomerName, Packages, Late (Delivered scan after "
         "PromisedDate, or no Delivered scan at all) and LatePct (2 decimals), for customers with at least one late package. "
         "Sort by LatePct descending, then CustomerID.",
         """WITH f AS (
    SELECT CustomerID, MIN(ShipDate) AS FirstShip
    FROM retail_logistics.Shipments
    GROUP BY CustomerID
    HAVING MIN(ShipDate) >= '2024-01-01' AND MIN(ShipDate) < '2024-07-01'
), d AS (
    SELECT PackageID, MIN(ScanTime) AS DeliveredAt
    FROM retail_logistics.TrackingEvents
    WHERE EventStatus = 'Delivered'
    GROUP BY PackageID
), p AS (
    SELECT s.CustomerID,
           CASE WHEN d.DeliveredAt IS NULL OR CAST(d.DeliveredAt AS date) > pk.PromisedDate THEN 1 ELSE 0 END AS IsLate
    FROM f
    JOIN retail_logistics.Shipments AS s ON s.CustomerID = f.CustomerID
         AND s.ShipDate <= DATEADD(day, 60, f.FirstShip)
    JOIN retail_logistics.ShipmentPackages AS pk ON pk.ShipmentID = s.ShipmentID
    LEFT JOIN d ON d.PackageID = pk.PackageID
)
SELECT p.CustomerID, c.CustomerName, COUNT(*) AS Packages, SUM(p.IsLate) AS Late,
       CAST(100.0 * SUM(p.IsLate) / COUNT(*) AS decimal(5,2)) AS LatePct
FROM p
JOIN retail_logistics.Customers AS c ON c.CustomerID = p.CustomerID
GROUP BY p.CustomerID, c.CustomerName
HAVING SUM(p.IsLate) > 0
ORDER BY LatePct DESC, p.CustomerID;""",
         "Three steps: each customer's first date (filtered in HAVING), the shipments inside their 60-day window (a join condition "
         "relative to that date), then a late flag per package. Missing delivery counts as late, so LEFT JOIN the delivery scans."),
        longest_gap(g),
    ]


def retail_inventory():
    g = G['retail_inventory']
    return [
        median(g),
        mtd(g),
        pareto(g),
        transitions(g),
        mom(g),
        PEAK_STOCK,
        ("Below reorder level, with the supplier to call",
         "List stock balances where QuantityOnHand is below ReorderLevel. For each, show WarehouseName, ProductName, QuantityOnHand, "
         "ReorderLevel, Shortfall (ReorderLevel minus QuantityOnHand) and the supplier who delivered that product most often into "
         "any warehouse (IN movements; ties go to the shorter LeadTimeDays, then the alphabetically first name) as Supplier and "
         "LeadTimeDays. Use NULL when the product has never been delivered. Sort by Shortfall descending, then WarehouseName, ProductName.",
         """WITH s AS (
    SELECT m.ProductID, su.SupplierName, su.LeadTimeDays,
           ROW_NUMBER() OVER (PARTITION BY m.ProductID ORDER BY COUNT(*) DESC, su.LeadTimeDays, su.SupplierName) AS rn
    FROM retail_inventory.StockMovements AS m
    JOIN retail_inventory.Suppliers AS su ON su.SupplierID = m.SupplierID
    WHERE m.Direction = 'IN'
    GROUP BY m.ProductID, su.SupplierID, su.SupplierName, su.LeadTimeDays
)
SELECT w.WarehouseName, p.ProductName, b.QuantityOnHand, b.ReorderLevel,
       b.ReorderLevel - b.QuantityOnHand AS Shortfall, s.SupplierName AS Supplier, s.LeadTimeDays
FROM retail_inventory.StockBalances AS b
JOIN retail_inventory.Warehouses AS w ON w.WarehouseID = b.WarehouseID
JOIN retail_inventory.Products AS p ON p.ProductID = b.ProductID
LEFT JOIN s ON s.ProductID = b.ProductID AND s.rn = 1
WHERE b.QuantityOnHand < b.ReorderLevel
ORDER BY Shortfall DESC, w.WarehouseName, p.ProductName;""",
         "Rank suppliers per product with ROW_NUMBER() OVER (... ORDER BY COUNT(*) DESC, tie-breakers) right after GROUP BY. "
         "Put rn = 1 in the LEFT JOIN condition (not WHERE) so products with no supplier stay."),
        ("Monthly IN vs OUT, side by side",
         "For Closed movements, show one row per month: Month (yyyy-MM), UnitsIn, UnitsOut, NetUnits (in minus out) and "
         "CumulativeNet (running NetUnits from the first month). Sort by Month.",
         """WITH m AS (
    SELECT FORMAT(MovementDate, 'yyyy-MM') AS Month,
           SUM(CASE WHEN Direction = 'IN' THEN MovedUnits ELSE 0 END) AS UnitsIn,
           SUM(CASE WHEN Direction = 'OUT' THEN MovedUnits ELSE 0 END) AS UnitsOut
    FROM retail_inventory.StockMovements
    WHERE Status = 'Closed'
    GROUP BY FORMAT(MovementDate, 'yyyy-MM')
)
SELECT Month, UnitsIn, UnitsOut, UnitsIn - UnitsOut AS NetUnits,
       SUM(UnitsIn - UnitsOut) OVER (ORDER BY Month ROWS UNBOUNDED PRECEDING) AS CumulativeNet
FROM m
ORDER BY Month;""",
         "Conditional aggregation (SUM(CASE ...)) pivots IN and OUT into columns; a running SUM() OVER (ORDER BY Month) adds the cumulative column."),
        ("Suppliers tied to a single warehouse",
         "Find suppliers with at least 2 IN movements who delivered to only one warehouse. Show SupplierName, LeadTimeDays, "
         "WarehouseName, Deliveries and UnitsDelivered. Sort by Deliveries descending, then SupplierName.",
         """SELECT su.SupplierName, su.LeadTimeDays, MIN(w.WarehouseName) AS WarehouseName,
       COUNT(*) AS Deliveries, SUM(m.MovedUnits) AS UnitsDelivered
FROM retail_inventory.StockMovements AS m
JOIN retail_inventory.Suppliers AS su ON su.SupplierID = m.SupplierID
JOIN retail_inventory.Warehouses AS w ON w.WarehouseID = m.WarehouseID
WHERE m.Direction = 'IN'
GROUP BY su.SupplierID, su.SupplierName, su.LeadTimeDays
HAVING COUNT(*) >= 2 AND COUNT(DISTINCT m.WarehouseID) = 1
ORDER BY Deliveries DESC, su.SupplierName;""",
         "'Only one X' is HAVING COUNT(DISTINCT X) = 1. With a single warehouse per group, MIN(WarehouseName) returns its name."),
        longest_gap(g),
    ]


def retail_manufacturing():
    g = G['retail_manufacturing']
    return [
        median(g),
        mtd(g),
        pareto(g),
        transitions(g),
        ("Material usage vs the recipe",
         "The recipe (BillOfMaterials) says how much of each material one unit of a product needs. For Closed production orders, "
         "compare actual MaterialUsage with PlannedUnits × QuantityPerUnit for each material in the recipe. List order-material pairs "
         "that used more than 3% over plan: ProductionReference, ProductName, MaterialName, Planned, Used and OverPct (2 decimals). "
         "Sort by OverPct descending, then ProductionReference, MaterialName.",
         """WITH u AS (
    SELECT ProductionOrderID, MaterialID, SUM(QuantityUsed) AS Used
    FROM retail_manufacturing.MaterialUsage
    GROUP BY ProductionOrderID, MaterialID
), x AS (
    SELECT po.ProductionReference, p.ProductName, m.MaterialName,
           po.PlannedUnits * b.QuantityPerUnit AS Planned, COALESCE(u.Used, 0) AS Used
    FROM retail_manufacturing.ProductionOrders AS po
    JOIN retail_manufacturing.Products AS p ON p.ProductID = po.ProductID
    JOIN retail_manufacturing.BillOfMaterials AS b ON b.ProductID = po.ProductID
    JOIN retail_manufacturing.Materials AS m ON m.MaterialID = b.MaterialID
    LEFT JOIN u ON u.ProductionOrderID = po.ProductionOrderID AND u.MaterialID = b.MaterialID
    WHERE po.Status = 'Closed'
)
SELECT ProductionReference, ProductName, MaterialName, Planned, Used,
       CAST(100.0 * (Used - Planned) / Planned AS decimal(7,2)) AS OverPct
FROM x
WHERE Used > Planned * 1.03
ORDER BY OverPct DESC, ProductionReference, MaterialName;""",
         "The plan comes from joining each order to its product's recipe; the actuals are summed per order and material, then LEFT JOINed on both keys."),
        mom(g),
        ("Actual material cost vs planned cost",
         "Actual cost of a production order is the sum of QuantityUsed × Materials.UnitCost. For Closed orders, show per ProductionCategory: "
         "Orders, PlannedCost (sum), ActualCost (sum) and OverrunPct ((Actual − Planned) ÷ Planned × 100, 2 decimals). PlannedCost must "
         "count each order once. Sort by ProductionCategory.",
         """WITH a AS (
    SELECT mu.ProductionOrderID, SUM(mu.QuantityUsed * m.UnitCost) AS ActualCost
    FROM retail_manufacturing.MaterialUsage AS mu
    JOIN retail_manufacturing.Materials AS m ON m.MaterialID = mu.MaterialID
    GROUP BY mu.ProductionOrderID
)
SELECT po.ProductionCategory, COUNT(*) AS Orders, SUM(po.PlannedCost) AS PlannedCost,
       CAST(SUM(COALESCE(a.ActualCost, 0)) AS decimal(14,2)) AS ActualCost,
       CAST(100.0 * (SUM(COALESCE(a.ActualCost, 0)) - SUM(po.PlannedCost)) / SUM(po.PlannedCost) AS decimal(7,2)) AS OverrunPct
FROM retail_manufacturing.ProductionOrders AS po
LEFT JOIN a ON a.ProductionOrderID = po.ProductionOrderID
WHERE po.Status = 'Closed'
GROUP BY po.ProductionCategory
ORDER BY po.ProductionCategory;""",
         "Cost the usage per order first; joining orders straight to usage rows would add PlannedCost once per usage row."),
        rank_shift(g),
        ("Costliest recipes per region",
         "A product's recipe cost per unit is the sum of QuantityPerUnit × Materials.UnitCost over its BillOfMaterials. For each product "
         "Region, show the top 3 ranks by recipe cost, keeping ties without skipping ranks: Region, CostRank, ProductName, Materials "
         "(how many materials in the recipe) and UnitRecipeCost (2 decimals). Sort by Region, CostRank, ProductName.",
         """WITH c AS (
    SELECT p.Region, p.ProductName, COUNT(*) AS Materials, SUM(b.QuantityPerUnit * m.UnitCost) AS Cost
    FROM retail_manufacturing.BillOfMaterials AS b
    JOIN retail_manufacturing.Products AS p ON p.ProductID = b.ProductID
    JOIN retail_manufacturing.Materials AS m ON m.MaterialID = b.MaterialID
    GROUP BY p.Region, p.ProductID, p.ProductName
), r AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY Region ORDER BY Cost DESC) AS CostRank
    FROM c
)
SELECT Region, CostRank, ProductName, Materials, CAST(Cost AS decimal(12,2)) AS UnitRecipeCost
FROM r
WHERE CostRank <= 3
ORDER BY Region, CostRank, ProductName;""",
         "Aggregate the recipe per product, then DENSE_RANK() within each region. Filter on the rank in an outer query."),
        longest_gap(g),
    ]


# ---------------------------------------------------------------------------------------------------------------
# Workbook-only domains (extra_domains.py)
# ---------------------------------------------------------------------------------------------------------------
G['retail_supply_chain'] = dict(G['retail_inventory'], s='retail_supply_chain')
G['ecommerce'] = dict(G['retail'], s='ecommerce')


def _sc(t):
    return tuple(x.replace('retail_inventory.', 'retail_supply_chain.') for x in t)


def retail_supply_chain():
    g = G['retail_supply_chain']
    inv = {c[0]: c for c in retail_inventory()}
    return [
        median(g),
        mtd(g),
        _sc(PEAK_STOCK),
        ("Below reorder level, with the source to call",
         "List stock balances where QuantityOnHand is below ReorderLevel. For each, show WarehouseName, ProductName, Sourcing, "
         "QuantityOnHand, ReorderLevel, Shortfall (ReorderLevel minus QuantityOnHand) and the supplier who delivered that product most "
         "often into any warehouse (IN movements; ties go to the shorter LeadTimeDays, then the alphabetically first name) as Supplier "
         "and LeadTimeDays. Use NULL when the product has never been delivered. Sort by Shortfall descending, then WarehouseName, ProductName.",
         """WITH s AS (
    SELECT m.ProductID, su.SupplierName, su.LeadTimeDays,
           ROW_NUMBER() OVER (PARTITION BY m.ProductID ORDER BY COUNT(*) DESC, su.LeadTimeDays, su.SupplierName) AS rn
    FROM retail_supply_chain.StockMovements AS m
    JOIN retail_supply_chain.Suppliers AS su ON su.SupplierID = m.SupplierID
    WHERE m.Direction = 'IN'
    GROUP BY m.ProductID, su.SupplierID, su.SupplierName, su.LeadTimeDays
)
SELECT w.WarehouseName, p.ProductName, p.Sourcing, b.QuantityOnHand, b.ReorderLevel,
       b.ReorderLevel - b.QuantityOnHand AS Shortfall, s.SupplierName AS Supplier, s.LeadTimeDays
FROM retail_supply_chain.StockBalances AS b
JOIN retail_supply_chain.Warehouses AS w ON w.WarehouseID = b.WarehouseID
JOIN retail_supply_chain.Products AS p ON p.ProductID = b.ProductID
LEFT JOIN s ON s.ProductID = b.ProductID AND s.rn = 1
WHERE b.QuantityOnHand < b.ReorderLevel
ORDER BY Shortfall DESC, w.WarehouseName, p.ProductName;""",
         "Rank suppliers per product with ROW_NUMBER() OVER (... ORDER BY COUNT(*) DESC, tie-breakers) right after GROUP BY. "
         "Put rn = 1 in the LEFT JOIN condition (not WHERE) so products with no supplier stay."),
        _sc(inv['Monthly IN vs OUT, side by side']),
        ("Material usage vs the recipe",
         "The recipe (BillOfMaterials) says how much of each material one unit of a Made product needs. For Completed production "
         "orders, compare actual MaterialUsage with PlannedUnits × QuantityPerUnit for each material in the recipe. List order-material "
         "pairs that used more than 3% over plan: ProductionReference, ProductName, MaterialName, Planned, Used and OverPct (2 decimals). "
         "Sort by OverPct descending, then ProductionReference, MaterialName.",
         """WITH u AS (
    SELECT ProductionOrderID, MaterialID, SUM(QuantityUsed) AS Used
    FROM retail_supply_chain.MaterialUsage
    GROUP BY ProductionOrderID, MaterialID
), x AS (
    SELECT po.ProductionReference, p.ProductName, m.MaterialName,
           po.PlannedUnits * b.QuantityPerUnit AS Planned, COALESCE(u.Used, 0) AS Used
    FROM retail_supply_chain.ProductionOrders AS po
    JOIN retail_supply_chain.Products AS p ON p.ProductID = po.ProductID
    JOIN retail_supply_chain.BillOfMaterials AS b ON b.ProductID = po.ProductID
    JOIN retail_supply_chain.Materials AS m ON m.MaterialID = b.MaterialID
    LEFT JOIN u ON u.ProductionOrderID = po.ProductionOrderID AND u.MaterialID = b.MaterialID
    WHERE po.ProductionStatus = 'Completed'
)
SELECT ProductionReference, ProductName, MaterialName, Planned, Used,
       CAST(100.0 * (Used - Planned) / Planned AS decimal(7,2)) AS OverPct
FROM x
WHERE Used > Planned * 1.03
ORDER BY OverPct DESC, ProductionReference, MaterialName;""",
         "The plan comes from joining each order to its product's recipe; the actuals are summed per order and material, then LEFT JOINed on both keys."),
        ("Actual material cost vs planned cost, by region",
         "Actual cost of a production order is the sum of QuantityUsed × Materials.UnitCost. For Completed orders, show per Region of "
         "the receiving warehouse: Orders, PlannedCost (sum), ActualCost (sum, 2 decimals) and OverrunPct ((Actual − Planned) ÷ Planned "
         "× 100, 2 decimals). PlannedCost must count each order once. Sort by OverrunPct descending, then Region.",
         """WITH a AS (
    SELECT mu.ProductionOrderID, SUM(mu.QuantityUsed * m.UnitCost) AS ActualCost
    FROM retail_supply_chain.MaterialUsage AS mu
    JOIN retail_supply_chain.Materials AS m ON m.MaterialID = mu.MaterialID
    GROUP BY mu.ProductionOrderID
)
SELECT w.Region, COUNT(*) AS Orders, SUM(po.PlannedCost) AS PlannedCost,
       CAST(SUM(COALESCE(a.ActualCost, 0)) AS decimal(14,2)) AS ActualCost,
       CAST(100.0 * (SUM(COALESCE(a.ActualCost, 0)) - SUM(po.PlannedCost)) / SUM(po.PlannedCost) AS decimal(7,2)) AS OverrunPct
FROM retail_supply_chain.ProductionOrders AS po
JOIN retail_supply_chain.Warehouses AS w ON w.WarehouseID = po.WarehouseID
LEFT JOIN a ON a.ProductionOrderID = po.ProductionOrderID
WHERE po.ProductionStatus = 'Completed'
GROUP BY w.Region
ORDER BY OverrunPct DESC, w.Region;""",
         "Cost the usage per order first; joining orders straight to usage rows would add PlannedCost once per usage row."),
        ("Factory to shelf: completed but not yet received",
         "A Completed production order is *received* when an IN stock movement points to it (StockMovements.ProductionOrderID). "
         "For each Region of the receiving warehouse show CompletedOrders, Received, NotReceived, UnitsWaiting (PlannedUnits of the "
         "orders not received) and AvgDaysToShelf (average days from CompletedDate to the first receipt's MovementDate, 1 decimal, "
         "received orders only). Sort by UnitsWaiting descending, then Region.",
         """WITH r AS (
    SELECT ProductionOrderID, MIN(MovementDate) AS ReceivedDate
    FROM retail_supply_chain.StockMovements
    WHERE ProductionOrderID IS NOT NULL AND Direction = 'IN'
    GROUP BY ProductionOrderID
)
SELECT w.Region,
       COUNT(*) AS CompletedOrders,
       COUNT(r.ProductionOrderID) AS Received,
       COUNT(*) - COUNT(r.ProductionOrderID) AS NotReceived,
       SUM(CASE WHEN r.ProductionOrderID IS NULL THEN po.PlannedUnits ELSE 0 END) AS UnitsWaiting,
       CAST(AVG(CAST(DATEDIFF(day, po.CompletedDate, r.ReceivedDate) AS decimal(9,2))) AS decimal(9,1)) AS AvgDaysToShelf
FROM retail_supply_chain.ProductionOrders AS po
JOIN retail_supply_chain.Warehouses AS w ON w.WarehouseID = po.WarehouseID
LEFT JOIN r ON r.ProductionOrderID = po.ProductionOrderID
WHERE po.ProductionStatus = 'Completed'
GROUP BY w.Region
ORDER BY UnitsWaiting DESC, w.Region;""",
         "Reduce receipts to one row per production order first, then LEFT JOIN so unreceived orders stay. COUNT(column) skips NULLs, "
         "so COUNT(*) minus COUNT(r.ProductionOrderID) is the number not received; AVG also ignores the NULL day counts."),
        ("Stock value: bought vs made",
         "Value on-hand stock as QuantityOnHand × Products.UnitCost. For each warehouse Region show BoughtValue, MadeValue, TotalValue "
         "and MadeSharePct (MadeValue as a percentage of TotalValue, 2 decimals), plus a final row with Region = 'All regions'. "
         "Sort the regions by TotalValue descending with the total row last.",
         """WITH v AS (
    SELECT w.Region,
           SUM(CASE WHEN p.Sourcing = 'Bought' THEN b.QuantityOnHand * p.UnitCost ELSE 0 END) AS BoughtValue,
           SUM(CASE WHEN p.Sourcing = 'Made' THEN b.QuantityOnHand * p.UnitCost ELSE 0 END) AS MadeValue
    FROM retail_supply_chain.StockBalances AS b
    JOIN retail_supply_chain.Warehouses AS w ON w.WarehouseID = b.WarehouseID
    JOIN retail_supply_chain.Products AS p ON p.ProductID = b.ProductID
    GROUP BY ROLLUP (w.Region)
)
SELECT COALESCE(Region, 'All regions') AS Region, BoughtValue, MadeValue, BoughtValue + MadeValue AS TotalValue,
       CAST(100.0 * MadeValue / NULLIF(BoughtValue + MadeValue, 0) AS decimal(5,2)) AS MadeSharePct
FROM v
ORDER BY CASE WHEN Region IS NULL THEN 1 ELSE 0 END, TotalValue DESC;""",
         "Conditional aggregation splits Bought and Made into columns. GROUP BY ROLLUP adds the grand-total row (Region is NULL there), "
         "and a CASE in ORDER BY pushes that row to the bottom."),
        longest_gap(g),
    ]


def ecommerce():
    g = G['ecommerce']
    return [
        ("Daily orders with a 7-day moving average",
         "For December 2024, show every OrderDate with Orders, Revenue (sum of OrderTotal), Avg7Day (average daily orders over that "
         "day and the 6 days before it, 1 decimal) and VsAvgPct (Orders compared with Avg7Day, as a percentage above or below, "
         "1 decimal). The first days of December must still average over late-November days. Sort by OrderDate.",
         """WITH d AS (
    SELECT OrderDate, COUNT(*) AS Orders, SUM(OrderTotal) AS Revenue
    FROM ecommerce.Orders
    GROUP BY OrderDate
), w AS (
    SELECT OrderDate, Orders, Revenue,
           AVG(CAST(Orders AS decimal(9,2))) OVER (ORDER BY OrderDate ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS A7
    FROM d
)
SELECT OrderDate, Orders, Revenue, CAST(A7 AS decimal(9,1)) AS Avg7Day,
       CAST(100.0 * (Orders - A7) / A7 AS decimal(9,1)) AS VsAvgPct
FROM w
WHERE OrderDate >= '2024-12-01' AND OrderDate < '2025-01-01'
ORDER BY OrderDate;""",
         "Aggregate to one row per day, compute the moving average with ROWS BETWEEN 6 PRECEDING AND CURRENT ROW over *all* days, "
         "and filter to December only in the outer query. Filtering first would cut the November days out of the window."),
        ("Busiest hour of each weekday",
         "Using PlacedAt, count orders per weekday and hour of the day (0-23). For each weekday show the busiest hour: Weekday "
         "(Monday, Tuesday, ...), HourOfDay, Orders and ShareOfDayPct (that hour's share of the weekday's orders, 2 decimals). Keep ties. "
         "Sort Monday to Sunday, then HourOfDay.",
         """WITH h AS (
    SELECT DATEDIFF(day, '19000101', PlacedAt) % 7 AS DayNo,
           DATENAME(weekday, PlacedAt) AS Weekday,
           DATEPART(hour, PlacedAt) AS HourOfDay,
           COUNT(*) AS Orders
    FROM ecommerce.Orders
    GROUP BY DATEDIFF(day, '19000101', PlacedAt) % 7, DATENAME(weekday, PlacedAt), DATEPART(hour, PlacedAt)
), r AS (
    SELECT *, RANK() OVER (PARTITION BY DayNo ORDER BY Orders DESC) AS rk,
           SUM(Orders) OVER (PARTITION BY DayNo) AS DayOrders
    FROM h
)
SELECT Weekday, HourOfDay, Orders, CAST(100.0 * Orders / DayOrders AS decimal(5,2)) AS ShareOfDayPct
FROM r
WHERE rk = 1
ORDER BY DayNo, HourOfDay;""",
         "1900-01-01 was a Monday, so DATEDIFF(day, '19000101', d) % 7 numbers Monday as 0 whatever the server's DATEFIRST setting. "
         "RANK() per weekday keeps tied hours; a window SUM over the same partition gives the day total for the share."),
        ("Same-day power buyers",
         "Find customers who placed 3 or more orders on the same day. Show CustomerID, CustomerName, OrderDate, OrdersThatDay, "
         "DaySpend (sum of OrderTotal that day), FirstAt and LastAt (time of their first and last order that day) and MinutesBetween "
         "(from first to last). Sort by OrdersThatDay descending, then DaySpend descending, then CustomerID, OrderDate.",
         """SELECT o.CustomerID, c.CustomerName, o.OrderDate, COUNT(*) AS OrdersThatDay, SUM(o.OrderTotal) AS DaySpend,
       MIN(o.PlacedAt) AS FirstAt, MAX(o.PlacedAt) AS LastAt,
       DATEDIFF(minute, MIN(o.PlacedAt), MAX(o.PlacedAt)) AS MinutesBetween
FROM ecommerce.Orders AS o
JOIN ecommerce.Customers AS c ON c.CustomerID = o.CustomerID
GROUP BY o.CustomerID, c.CustomerName, o.OrderDate
HAVING COUNT(*) >= 3
ORDER BY OrdersThatDay DESC, DaySpend DESC, o.CustomerID, o.OrderDate;""",
         "Group by customer *and* day, then HAVING COUNT(*) >= 3. MIN and MAX of the timestamp in the same group give the first and last order."),
        ("Bazaar Days lift",
         "Everyday Bazaar ran its Bazaar Days sale on 16 and 17 July 2024. For each sale day show SaleDay, Orders, BaselineOrders "
         "(average orders on the same weekday in the 4 weeks before), OrderLiftPct, Revenue, BaselineRevenue and RevenueLiftPct "
         "(lift = (sale − baseline) ÷ baseline × 100). Round baselines and percentages to 1 decimal. Sort by SaleDay.",
         """WITH d AS (
    SELECT OrderDate, COUNT(*) AS Orders, SUM(OrderTotal) AS Revenue
    FROM ecommerce.Orders
    GROUP BY OrderDate
), b AS (
    SELECT s.OrderDate AS SaleDay, s.Orders, s.Revenue,
           AVG(CAST(p.Orders AS decimal(12,2))) AS BaseOrders, AVG(p.Revenue) AS BaseRevenue
    FROM d AS s
    JOIN d AS p ON p.OrderDate IN (DATEADD(day, -7, s.OrderDate), DATEADD(day, -14, s.OrderDate),
                                   DATEADD(day, -21, s.OrderDate), DATEADD(day, -28, s.OrderDate))
    WHERE s.OrderDate IN ('2024-07-16', '2024-07-17')
    GROUP BY s.OrderDate, s.Orders, s.Revenue
)
SELECT SaleDay, Orders, CAST(BaseOrders AS decimal(9,1)) AS BaselineOrders,
       CAST(100.0 * (Orders - BaseOrders) / BaseOrders AS decimal(9,1)) AS OrderLiftPct,
       Revenue, CAST(BaseRevenue AS decimal(12,1)) AS BaselineRevenue,
       CAST(100.0 * (Revenue - BaseRevenue) / BaseRevenue AS decimal(9,1)) AS RevenueLiftPct
FROM b
ORDER BY SaleDay;""",
         "Build a daily table once, then self-join it: each sale day joins to the four days exactly 7, 14, 21 and 28 days earlier "
         "(same weekday). Comparing with the same weekday matters because weekends are busier."),
        ("Settlement check by order status",
         "Total each order's payments (an order can have a gift card plus a card). For each OrderStatus show Orders, FullyPaid "
         "(payments equal OrderTotal), Unpaid (no payment), PartPaid (some, but less), Overpaid, and OutstandingAmount (OrderTotal minus "
         "payments, over all orders of that status). Sort by OrderStatus.",
         """WITH p AS (
    SELECT OrderID, SUM(PaidAmount) AS Paid
    FROM ecommerce.Payments
    GROUP BY OrderID
)
SELECT o.OrderStatus, COUNT(*) AS Orders,
       SUM(CASE WHEN p.Paid = o.OrderTotal THEN 1 ELSE 0 END) AS FullyPaid,
       SUM(CASE WHEN p.Paid IS NULL THEN 1 ELSE 0 END) AS Unpaid,
       SUM(CASE WHEN p.Paid < o.OrderTotal THEN 1 ELSE 0 END) AS PartPaid,
       SUM(CASE WHEN p.Paid > o.OrderTotal THEN 1 ELSE 0 END) AS Overpaid,
       SUM(o.OrderTotal - COALESCE(p.Paid, 0)) AS OutstandingAmount
FROM ecommerce.Orders AS o
LEFT JOIN p ON p.OrderID = o.OrderID
GROUP BY o.OrderStatus
ORDER BY o.OrderStatus;""",
         "Sum payments per order in a CTE *before* joining, or a split payment would count the order twice. LEFT JOIN keeps unpaid "
         "orders; their Paid is NULL, which matches none of the comparisons and needs its own IS NULL test."),
        ("Fan-out trap: one report, three totals",
         "For each SalesChannel show Orders, Revenue (sum of OrderTotal), ItemsSold (sum of OrderItems.Quantity) and Paid (sum of "
         "Payments.PaidAmount). Every number must be right. Sort by Revenue descending.",
         """WITH i AS (
    SELECT OrderID, SUM(Quantity) AS Qty FROM ecommerce.OrderItems GROUP BY OrderID
), p AS (
    SELECT OrderID, SUM(PaidAmount) AS Paid FROM ecommerce.Payments GROUP BY OrderID
)
SELECT o.SalesChannel, COUNT(*) AS Orders, SUM(o.OrderTotal) AS Revenue,
       SUM(COALESCE(i.Qty, 0)) AS ItemsSold, SUM(COALESCE(p.Paid, 0)) AS Paid
FROM ecommerce.Orders AS o
LEFT JOIN i ON i.OrderID = o.OrderID
LEFT JOIN p ON p.OrderID = o.OrderID
GROUP BY o.SalesChannel
ORDER BY Revenue DESC;""",
         "Joining Orders to OrderItems and Payments in one go repeats each order once per item *and* per payment, which inflates "
         "Revenue and Paid. Pre-aggregate each child table to one row per order, then join."),
        cohort(g, 30),
        ("Top 3 sellers per department and their share",
         "Rank sellers inside their Department by revenue (sum of OrderTotal on their orders). For the top 3 in each department show "
         "Department, SellerRank, SellerName, Orders, Revenue and DeptSharePct (the seller's share of the whole department's revenue, "
         "2 decimals). Ties share a rank without skipping. Sort by Department, SellerRank, SellerName.",
         """WITH s AS (
    SELECT se.Department, se.SellerID, se.SellerName, COUNT(*) AS Orders, SUM(o.OrderTotal) AS Revenue
    FROM ecommerce.Orders AS o
    JOIN ecommerce.Sellers AS se ON se.SellerID = o.SellerID
    GROUP BY se.Department, se.SellerID, se.SellerName
), r AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY Department ORDER BY Revenue DESC) AS SellerRank,
           SUM(Revenue) OVER (PARTITION BY Department) AS DeptRevenue
    FROM s
)
SELECT Department, SellerRank, SellerName, Orders, Revenue,
       CAST(100.0 * Revenue / DeptRevenue AS decimal(5,2)) AS DeptSharePct
FROM r
WHERE SellerRank <= 3
ORDER BY Department, SellerRank, SellerName;""",
         "Aggregate per seller, then two window functions over the same department partition: DENSE_RANK for the position and SUM "
         "for the department total. The share must use the total of *all* sellers, so compute it before filtering to the top 3."),
        ("Bought together most often",
         "Find pairs of different products that appear in the same order. Show the 10 pairs bought together most often (keep ties at "
         "10th place): ProductA and ProductB (names; ProductA has the smaller ProductID) and TimesTogether. Sort by TimesTogether "
         "descending, then ProductA, then ProductB.",
         """SELECT TOP (10) WITH TIES pa.ProductName AS ProductA, pb.ProductName AS ProductB, COUNT(*) AS TimesTogether
FROM ecommerce.OrderItems AS a
JOIN ecommerce.OrderItems AS b ON b.OrderID = a.OrderID AND b.ProductID > a.ProductID
JOIN ecommerce.Products AS pa ON pa.ProductID = a.ProductID
JOIN ecommerce.Products AS pb ON pb.ProductID = b.ProductID
GROUP BY a.ProductID, b.ProductID, pa.ProductName, pb.ProductName
ORDER BY TimesTogether DESC, ProductA, ProductB;""",
         "Self-join OrderItems on the same OrderID; b.ProductID > a.ProductID removes self-pairs and keeps each pair once. "
         "TOP (10) WITH TIES needs an ORDER BY and keeps every row tied with the 10th; the extra name columns only break display order."),
        ("How often do regulars come back?",
         "For customers with at least 25 orders, measure the days between each order and their previous one. Per customer Region "
         "show Regulars (how many such customers), Gaps (how many gaps measured), AvgGapDays and MedianGapDays (1 decimal). "
         "Sort by MedianGapDays, then Region.",
         """WITH r AS (
    SELECT CustomerID
    FROM ecommerce.Orders
    GROUP BY CustomerID
    HAVING COUNT(*) >= 25
), gaps AS (
    SELECT c.Region, o.CustomerID,
           DATEDIFF(day, LAG(o.OrderDate) OVER (PARTITION BY o.CustomerID ORDER BY o.PlacedAt, o.OrderID), o.OrderDate) AS GapDays
    FROM ecommerce.Orders AS o
    JOIN r ON r.CustomerID = o.CustomerID
    JOIN ecommerce.Customers AS c ON c.CustomerID = o.CustomerID
), m AS (
    SELECT Region, CustomerID, GapDays,
           PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY GapDays) OVER (PARTITION BY Region) AS MedG
    FROM gaps
)
SELECT Region, COUNT(DISTINCT CustomerID) AS Regulars, COUNT(GapDays) AS Gaps,
       CAST(AVG(CAST(GapDays AS decimal(9,2))) AS decimal(9,1)) AS AvgGapDays,
       CAST(MAX(MedG) AS decimal(9,1)) AS MedianGapDays
FROM m
GROUP BY Region
ORDER BY MedianGapDays, Region;""",
         "Three steps: pick the regulars with HAVING, measure gaps with LAG per customer (the first order has no gap, so LAG returns "
         "NULL), then summarise per region. PERCENTILE_CONT exists only as a window function, so tag each row with its region's "
         "median, then GROUP BY (COUNT(DISTINCT ...) is not allowed with OVER). PERCENTILE_CONT, COUNT(column) and AVG all skip NULL gaps."),
    ]


BUILDERS = {'healthcare': healthcare, 'banking': banking, 'brokerage': brokerage, 'oil': oil, 'pharma': pharma,
            'retail': retail, 'retail_inventory': retail_inventory, 'retail_logistics': retail_logistics,
            'retail_manufacturing': retail_manufacturing, 'retail_supply_chain': retail_supply_chain, 'ecommerce': ecommerce}


def challenges(domain):
    items = BUILDERS[domain]()
    assert len(items) == 10, (domain, len(items))
    return items
