# Retail Supply Chain: advanced queries

Use the existing domain tables. Prerequisites: joins, grouped aggregates, CTEs and window functions. Submit SQL, results and an explanation of row counts, NULL handling and tie handling. These are read-only SQL Server 2017+ exercises. Use the small sample data first, then the large practice dataset; fixed expected results in the instructor key apply only to the small sample.

[All topics](README.md) · [Table definitions](DOMAIN_GUIDE.md)

## RETAIL_SUPPLY_CHAIN-ADV-01: Monthly activity with missing months and growth

For every `[retail_supply_chain].[Warehouses]` row, return all twelve months of 2024, including months with no `StockMovements` rows. Use `MovementDate` for month boundaries and `MovementValue` for totals. Return `WarehouseID`, `WarehouseName`, MonthStart, EventCount, KnownValueCount, TotalValue, PreviousMonthValue and GrowthPercent. A month with no rows has total zero; a month containing only unknown values has total NULL. Sum known values for mixed months. Growth is 100 * (current - previous) / previous; return NULL when either total is unknown, there is no previous month, or the previous total is zero. Partition LAG by the master key. Use a calendar CTE and order by `WarehouseID`, MonthStart.

## RETAIL_SUPPLY_CHAIN-ADV-02: Consecutive active-date streaks

Find consecutive calendar-date streaks per `WarehouseID` in `[retail_supply_chain].[StockMovements]` using `MovementDate`. Deduplicate same-day activity before using ROW_NUMBER and a gaps-and-islands grouping key. Return `WarehouseID`, `WarehouseName`, StreakStart, StreakEnd and ActiveDays for streaks of at least two days. Multiple rows on one date count as one active day. NULL monetary values still count as activity. Order by `WarehouseID`, StreakStart.

## RETAIL_SUPPLY_CHAIN-ADV-03: Top contributors with ties and category share

Aggregate known `MovementValue` by `MovementCategory` and `WarehouseID` in `[retail_supply_chain].[StockMovements]`, join `[retail_supply_chain].[Warehouses]` for `WarehouseName`, then return the top two distinct total-value ranks per category using DENSE_RANK. Include every tie. Calculate each master’s percentage of the complete category total before filtering ranks. Exclude groups with no known values; keep known zero totals. Return CategoryTotal and SharePercent alongside `MovementCategory`, `WarehouseID`, `WarehouseName`, TotalValue and ValueRank. Use NULL percentage for zero category totals. Order by `MovementCategory`, ValueRank, `WarehouseID`.

## RETAIL_SUPPLY_CHAIN-ADV-04: Trailing 30-calendar-day comparison

For every `[retail_supply_chain].[StockMovements]` row, compute the average known `MovementValue` for the same `WarehouseID` over dates from `MovementDate` minus 30 days inclusive to `MovementDate` exclusive. Exclude all same-day rows, not just the current row. Include the count of prior known values. Return only rows whose current value is strictly more than 1.5 times that average. Return `MovementID`, `WarehouseID`, `MovementDate`, `MovementValue`, PriorKnownCount and PriorAverage. Use a self join and grouped CTE; preserve decimal arithmetic. Order by `WarehouseID`, `MovementDate`, `MovementID`. Explain why ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING would answer a different question.

## RETAIL_SUPPLY_CHAIN-ADV-05: Masters covering every required category

Find `[retail_supply_chain].[Warehouses]` rows with at least one `[retail_supply_chain].[StockMovements]` row in each required `MovementCategory` value A, B and C during 2024, based on `MovementDate`. Use a required-category CTE and nested NOT EXISTS (relational division). Count activity regardless of whether `MovementValue` is NULL. Separately aggregate 2024 activity and join it to the qualifying masters. Return `WarehouseID`, `WarehouseName`, EventCount, KnownValueCount and TotalValue. Sum only known values; retain NULL if all values are unknown. Avoid multiplying rows by the required-category list. Order by `WarehouseID`.
