# E-commerce: advanced queries

Use the existing domain tables. Prerequisites: joins, grouped aggregates, CTEs and window functions. Submit SQL, results and an explanation of row counts, NULL handling and tie handling. These are read-only SQL Server 2017+ exercises. Use the small sample data first, then the large practice dataset; fixed expected results in the instructor key apply only to the small sample.

[All topics](README.md) · [Table definitions](DOMAIN_GUIDE.md)

## ECOMMERCE-ADV-01: Monthly activity with missing months and growth

For every `[ecommerce].[Customers]` row, return all twelve months of 2024, including months with no `Orders` rows. Use `OrderDate` for month boundaries and `OrderTotal` for totals. Return `CustomerID`, `CustomerName`, MonthStart, EventCount, KnownValueCount, TotalValue, PreviousMonthValue and GrowthPercent. A month with no rows has total zero; a month containing only unknown values has total NULL. Sum known values for mixed months. Growth is 100 * (current - previous) / previous; return NULL when either total is unknown, there is no previous month, or the previous total is zero. Partition LAG by the master key. Use a calendar CTE and order by `CustomerID`, MonthStart.

## ECOMMERCE-ADV-02: Consecutive active-date streaks

Find consecutive calendar-date streaks per `CustomerID` in `[ecommerce].[Orders]` using `OrderDate`. Deduplicate same-day activity before using ROW_NUMBER and a gaps-and-islands grouping key. Return `CustomerID`, `CustomerName`, StreakStart, StreakEnd and ActiveDays for streaks of at least two days. Multiple rows on one date count as one active day. NULL monetary values still count as activity. Order by `CustomerID`, StreakStart.

## ECOMMERCE-ADV-03: Top contributors with ties and category share

Aggregate known `OrderTotal` by `SalesChannel` and `CustomerID` in `[ecommerce].[Orders]`, join `[ecommerce].[Customers]` for `CustomerName`, then return the top two distinct total-value ranks per category using DENSE_RANK. Include every tie. Calculate each master’s percentage of the complete category total before filtering ranks. Exclude groups with no known values; keep known zero totals. Return CategoryTotal and SharePercent alongside `SalesChannel`, `CustomerID`, `CustomerName`, TotalValue and ValueRank. Use NULL percentage for zero category totals. Order by `SalesChannel`, ValueRank, `CustomerID`.

## ECOMMERCE-ADV-04: Trailing 30-calendar-day comparison

For every `[ecommerce].[Orders]` row, compute the average known `OrderTotal` for the same `CustomerID` over dates from `OrderDate` minus 30 days inclusive to `OrderDate` exclusive. Exclude all same-day rows, not just the current row. Include the count of prior known values. Return only rows whose current value is strictly more than 1.5 times that average. Return `OrderID`, `CustomerID`, `OrderDate`, `OrderTotal`, PriorKnownCount and PriorAverage. Use a self join and grouped CTE; preserve decimal arithmetic. Order by `CustomerID`, `OrderDate`, `OrderID`. Explain why ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING would answer a different question.

## ECOMMERCE-ADV-05: Masters covering every required category

Find `[ecommerce].[Customers]` rows with at least one `[ecommerce].[Orders]` row in each required `SalesChannel` value A, B and C during 2024, based on `OrderDate`. Use a required-category CTE and nested NOT EXISTS (relational division). Count activity regardless of whether `OrderTotal` is NULL. Separately aggregate 2024 activity and join it to the qualifying masters. Return `CustomerID`, `CustomerName`, EventCount, KnownValueCount and TotalValue. Sum only known values; retain NULL if all values are unknown. Avoid multiplying rows by the required-category list. Order by `CustomerID`.
