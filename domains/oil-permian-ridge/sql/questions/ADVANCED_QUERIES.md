# Oil: advanced queries

Use the existing domain tables. Prerequisites: joins, grouped aggregates, CTEs and window functions. Submit SQL, results and an explanation of row counts, NULL handling and tie handling. These are read-only SQL Server 2017+ exercises. Use the small sample data first, then the large practice dataset; fixed expected results in the instructor key apply only to the small sample.

[All topics](README.md) · [Table definitions](DOMAIN_GUIDE.md)

## OIL-ADV-01: Monthly activity with missing months and growth

For every `[oil].[Sites]` row, return all twelve months of 2024, including months with no `Shipments` rows. Use `ShipDate` for month boundaries and `ShipmentValue` for totals. Return `SiteID`, `SiteName`, MonthStart, EventCount, KnownValueCount, TotalValue, PreviousMonthValue and GrowthPercent. A month with no rows has total zero; a month containing only unknown values has total NULL. Sum known values for mixed months. Growth is 100 * (current - previous) / previous; return NULL when either total is unknown, there is no previous month, or the previous total is zero. Partition LAG by the master key. Use a calendar CTE and order by `SiteID`, MonthStart.

## OIL-ADV-02: Consecutive active-date streaks

Find consecutive calendar-date streaks per `SiteID` in `[oil].[Shipments]` using `ShipDate`. Deduplicate same-day activity before using ROW_NUMBER and a gaps-and-islands grouping key. Return `SiteID`, `SiteName`, StreakStart, StreakEnd and ActiveDays for streaks of at least two days. Multiple rows on one date count as one active day. NULL monetary values still count as activity. Order by `SiteID`, StreakStart.

## OIL-ADV-03: Top contributors with ties and category share

Aggregate known `ShipmentValue` by `ShipmentType` and `SiteID` in `[oil].[Shipments]`, join `[oil].[Sites]` for `SiteName`, then return the top two distinct total-value ranks per category using DENSE_RANK. Include every tie. Calculate each master’s percentage of the complete category total before filtering ranks. Exclude groups with no known values; keep known zero totals. Return CategoryTotal and SharePercent alongside `ShipmentType`, `SiteID`, `SiteName`, TotalValue and ValueRank. Use NULL percentage for zero category totals. Order by `ShipmentType`, ValueRank, `SiteID`.

## OIL-ADV-04: Trailing 30-calendar-day comparison

For every `[oil].[Shipments]` row, compute the average known `ShipmentValue` for the same `SiteID` over dates from `ShipDate` minus 30 days inclusive to `ShipDate` exclusive. Exclude all same-day rows, not just the current row. Include the count of prior known values. Return only rows whose current value is strictly more than 1.5 times that average. Return `ShipmentID`, `SiteID`, `ShipDate`, `ShipmentValue`, PriorKnownCount and PriorAverage. Use a self join and grouped CTE; preserve decimal arithmetic. Order by `SiteID`, `ShipDate`, `ShipmentID`. Explain why ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING would answer a different question.

## OIL-ADV-05: Masters covering every required category

Find `[oil].[Sites]` rows with at least one `[oil].[Shipments]` row in each required `ShipmentType` value A, B and C during 2024, based on `ShipDate`. Use a required-category CTE and nested NOT EXISTS (relational division). Count activity regardless of whether `ShipmentValue` is NULL. Separately aggregate 2024 activity and join it to the qualifying masters. Return `SiteID`, `SiteName`, EventCount, KnownValueCount and TotalValue. Sum only known values; retain NULL if all values are unknown. Avoid multiplying rows by the required-category list. Order by `SiteID`.
