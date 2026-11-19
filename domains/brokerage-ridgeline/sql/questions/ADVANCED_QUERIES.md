# Brokerage: advanced queries

Use the existing domain tables. Prerequisites: joins, grouped aggregates, CTEs and window functions. Submit SQL, results and an explanation of row counts, NULL handling and tie handling. These are read-only SQL Server 2017+ exercises. Use the small sample data first, then the large practice dataset; fixed expected results in the instructor key apply only to the small sample.

[All topics](README.md) · [Table definitions](DOMAIN_GUIDE.md)

## BROKERAGE-ADV-01: Monthly activity with missing months and growth

For every `[brokerage].[BrokerageAccounts]` row, return all twelve months of 2024, including months with no `TradeOrders` rows. Use `OrderDate` for month boundaries and `EstimatedValue` for totals. Return `AccountID`, `AccountName`, MonthStart, EventCount, KnownValueCount, TotalValue, PreviousMonthValue and GrowthPercent. A month with no rows has total zero; a month containing only unknown values has total NULL. Sum known values for mixed months. Growth is 100 * (current - previous) / previous; return NULL when either total is unknown, there is no previous month, or the previous total is zero. Partition LAG by the master key. Use a calendar CTE and order by `AccountID`, MonthStart.

## BROKERAGE-ADV-02: Consecutive active-date streaks

Find consecutive calendar-date streaks per `AccountID` in `[brokerage].[TradeOrders]` using `OrderDate`. Deduplicate same-day activity before using ROW_NUMBER and a gaps-and-islands grouping key. Return `AccountID`, `AccountName`, StreakStart, StreakEnd and ActiveDays for streaks of at least two days. Multiple rows on one date count as one active day. NULL monetary values still count as activity. Order by `AccountID`, StreakStart.

## BROKERAGE-ADV-03: Top contributors with ties and category share

Aggregate known `EstimatedValue` by `RoutingCategory` and `AccountID` in `[brokerage].[TradeOrders]`, join `[brokerage].[BrokerageAccounts]` for `AccountName`, then return the top two distinct total-value ranks per category using DENSE_RANK. Include every tie. Calculate each master’s percentage of the complete category total before filtering ranks. Exclude groups with no known values; keep known zero totals. Return CategoryTotal and SharePercent alongside `RoutingCategory`, `AccountID`, `AccountName`, TotalValue and ValueRank. Use NULL percentage for zero category totals. Order by `RoutingCategory`, ValueRank, `AccountID`.

## BROKERAGE-ADV-04: Trailing 30-calendar-day comparison

For every `[brokerage].[TradeOrders]` row, compute the average known `EstimatedValue` for the same `AccountID` over dates from `OrderDate` minus 30 days inclusive to `OrderDate` exclusive. Exclude all same-day rows, not just the current row. Include the count of prior known values. Return only rows whose current value is strictly more than 1.5 times that average. Return `OrderID`, `AccountID`, `OrderDate`, `EstimatedValue`, PriorKnownCount and PriorAverage. Use a self join and grouped CTE; preserve decimal arithmetic. Order by `AccountID`, `OrderDate`, `OrderID`. Explain why ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING would answer a different question.

## BROKERAGE-ADV-05: Masters covering every required category

Find `[brokerage].[BrokerageAccounts]` rows with at least one `[brokerage].[TradeOrders]` row in each required `RoutingCategory` value A, B and C during 2024, based on `OrderDate`. Use a required-category CTE and nested NOT EXISTS (relational division). Count activity regardless of whether `EstimatedValue` is NULL. Separately aggregate 2024 activity and join it to the qualifying masters. Return `AccountID`, `AccountName`, EventCount, KnownValueCount and TotalValue. Sum only known values; retain NULL if all values are unknown. Avoid multiplying rows by the required-category list. Order by `AccountID`.
