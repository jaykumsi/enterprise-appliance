# Pharma — DQL

[All topics](README.md) · [Tables and sample rows](DOMAIN_GUIDE.md)

Write the SQL for each question. Use your practice database. For exercises that change existing tables or data, start with the original sample data; ask your instructor to reset the practice tables between exercises.

## Select

### DQL-01-03

Pharma: List BatchID values, BatchCode values and BatchCost values, ordered by BatchID. Use `[pharma].[Batches]`.

### DQL-01-08

Pharma: Return each distinct BatchType once, sorted by BatchType. Use `[pharma].[Batches]`.

### DQL-01-13

Pharma: Show BatchID and BatchCost multiplied by PackCount as ExtendedAmount; keep unknown BatchCost values. Use `[pharma].[Batches]`.

### DQL-01-18

Pharma: Show BatchID, BatchType as BusinessGroup and Status as WorkflowState. Use `[pharma].[Batches]`.

### DQL-01-23

Pharma: Return distinct combinations of `BatchType` and `Status`, ordered by `BatchType`, then `Status`. Use `[pharma].[Batches]`.

## Where

### DQL-02-03

Pharma: Find Open batches; return BatchID and Status. Use `[pharma].[Batches]`.

### DQL-02-08

Pharma: Find known BatchCost values of at least 150 in BatchType B; return BatchID and BatchCost. Use `[pharma].[Batches]`.

### DQL-02-13

Pharma: Find unknown BatchCost values; return BatchID and BatchCost. Use `[pharma].[Batches]`.

### DQL-02-18

Pharma: Find batches in January 2024 using an inclusive start and exclusive end; return BatchID values and ManufactureDate values. Use `[pharma].[Batches]`.

### DQL-02-23

Pharma: Find batches that are Open or Pending, with a positive BatchCost; return BatchID, Status and BatchCost. Use `[pharma].[Batches]`.

## Group By

### DQL-03-03

Pharma: Count batches per BatchType. Use `[pharma].[Batches]`.

### DQL-03-08

Pharma: Total known BatchCost values per Status. Use `[pharma].[Batches]`.

### DQL-03-13

Pharma: Return average known BatchCost for each BatchType/Status pair. Use `[pharma].[Batches]`.

### DQL-03-18

Pharma: Count batches by calendar year and month of `ManufactureDate`. Use `[pharma].[Batches]`.

### DQL-03-23

Pharma: Return each SupplierID (which is NOT NULL), batch count and total PackCount. Use `[pharma].[Batches]`.

## Having

### DQL-04-03

Pharma: Find BatchType values with more than three batches; show count. Use `[pharma].[Batches]`.

### DQL-04-08

Pharma: Find Status values with total known BatchCost values above 500; show total. Use `[pharma].[Batches]`.

### DQL-04-13

Pharma: Among positive BatchCost values, find BatchType values averaging at least 150; show average. Use `[pharma].[Batches]`.

### DQL-04-18

Pharma: Find SupplierID values with at least two batches; SupplierID is NOT NULL; show count. Use `[pharma].[Batches]`.

### DQL-04-23

Pharma: Find BatchType values containing an unknown BatchCost; show total and known-BatchCost counts. Use `[pharma].[Batches]`.

## Order By

### DQL-05-03

Pharma: List BatchID values and BatchCost values from lowest to highest BatchCost, NULL first, then BatchID. Use `[pharma].[Batches]`.

### DQL-05-08

Pharma: List BatchID values and BatchCost values from highest to lowest BatchCost, then BatchID ascending. Use `[pharma].[Batches]`.

### DQL-05-13

Pharma: List BatchID values, BatchType values and ManufactureDate values, grouped by BatchType then newest ManufactureDate first and BatchID ascending. Use `[pharma].[Batches]`.

### DQL-05-18

Pharma: List BatchID values and BatchCost values ascending but place unknown BatchCost values last. Use `[pharma].[Batches]`.

### DQL-05-23

Pharma: List BatchID values and Status in business priority Open, Pending, Closed, then BatchID. Use `[pharma].[Batches]`.

## Top

### DQL-06-03

Pharma: Return exactly the three highest-BatchCost batches, breaking ties by BatchID ascending. Use `[pharma].[Batches]`.

### DQL-06-08

Pharma: Return the two earliest batches, breaking ties by BatchID. Use `[pharma].[Batches]`. Use `ManufactureDate` to determine chronological order.

### DQL-06-13

Pharma: Return the top three BatchCost positions and all BatchCost ties at the cutoff. Order by BatchCost descending only. Use `[pharma].[Batches]`.

### DQL-06-18

Pharma: Return the highest-BatchCost Open batch, breaking ties by BatchID. Use `[pharma].[Batches]`.

### DQL-06-23

Pharma: Return the top 25 percent of batches by latest ManufactureDate, then BatchID ascending. Use `[pharma].[Batches]`.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview practice

Each subtopic below has15 questions per level. Each ID identifies the complete task,analysis rule or core case,and edge conditions. The earlier questions retain their original IDs as foundation practice.

### Select: progression

**Beginner:15 questions**

#### PHARMA-DQL-01-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-01-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-01-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-01-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Select:** The analysis value is `BatchCost` multiplied by `PackCount`; unknown values stay unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

### Where: progression

**Beginner:15 questions**

#### PHARMA-DQL-02-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-02-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-02-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-02-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Where:** Only Open/Pending `Status` rows in 2024 qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

### Group By: progression

**Beginner:15 questions**

#### PHARMA-DQL-03-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-03-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-03-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-03-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Group By:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

### Having: progression

**Beginner:15 questions**

#### PHARMA-DQL-04-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-04-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-04-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-04-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Having:** Combine source rows at `SupplierID`/`ManufactureDate` grain. Use the smallest contributing `BatchID` as the analysis row ID and the sum of known `BatchCost` as analysis value; an all-unknown group stays unknown. Retain groups having at least two rows or known sum at least 200. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

### Order By: progression

**Beginner:15 questions**

#### PHARMA-DQL-05-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-05-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-05-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-05-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Order By:** Within each `SupplierID`, retain the first three rows by `BatchCost` descending, then `BatchID` ascending. Unknown values do not qualify. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

### Top: progression

**Beginner:15 questions**

#### PHARMA-DQL-06-B01

**Analysis audit** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its owner,date,value and segment.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Keep null values and stored token spaces.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B02

**Known versus unknown** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return only analysis rows with a known value.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero is not unknown.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B03

**Unknown-value queue** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return the IDs and dates of rows whose analysis value is unknown.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ActivityDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An empty queue must have the requested columns.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B04

**Threshold review** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return known analysis values at least100.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The lower bound is inclusive;unknown values cannot pass.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B05

**Deterministic shortlist** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return at most five rows by descending known analysis value,then ascending source ID;unknown values are excluded.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `MetricValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MetricValue DESC,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return fewer than five if fewer qualify;ties do not expand the result.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B06

**Active-owner totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner present in the analysis population,return row count,known-value count and sum of known values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown owner has null total,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B07

**All-owner coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every master owner,including those with no eligible activity. Empty owners have count0,known count0,total0;an active all-unknown owner has null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Count real activity,not an outer-join placeholder.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B08

**Segment profile** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each analysis segment with row count,known count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Use SQL Server collation equality for segment grouping.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B09

**Owner segment coverage** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each distinct owner/segment pair exactly once.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated activity in one segment does not duplicate its owner/segment pair.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B10

**Observed-month totals** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per calendar month present in the analysis population,with event count,known count and sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not fabricate missing months in this question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B11

**Daily workload** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one row per owner/analysis date with count and known-value sum.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Different source rows on the same day remain separate contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B12

**No eligible activity** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return master owner IDs having no analysis rows.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An owner with an unknown-value row is active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B13

**Visible parent link** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return analysis row IDs whose parent is also an analysis row,and the parent ID and both values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentID`, `ChildValue`, `ParentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A parent excluded by the analysis eligibility rule is not visible here.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B14

**Bounded-value counts** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every observed segment,return total rows and count of known values in the inclusive interval[100,200].

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `EventCount`, `InRangeCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Return0 for a segment with no values in the interval.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-B15

**Value sign reconciliation** · Beginner · Suggested coding time:15 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return one summary row splitting all analysis rows into unknown,negative,zero and positive counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `EventCount`, `UnknownCount`, `NegativeCount`, `ZeroCount`, `PositiveCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** EventCount.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** All four classes must sum to EventCount;empty input returns five zero counts.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Intermediate:15 questions**

#### PHARMA-DQL-06-I01

**Exactly two per owner** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return up to two known-value rows per owner ordered by value descending then source ID ascending. Keep the position1 or2.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `Position`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Position.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Ties cannot expand a two-row limit.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I02

**Two value positions with ties** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all rows in each owner's two highest distinct known analysis values. Return ValueRank.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `MetricValue`, `ValueRank`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ValueRank,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Several rows may share rank2;all must remain.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I03

**Running value and knowledge** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each row,return the running known-value sum and known count through that row within its owner,ordered by date then source ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `ActivityDate`, `MetricValue`, `RunningValue`, `RunningKnownCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An all-unknown prefix has null RunningValue.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I04

**Previous row delta** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return each row's immediately preceding analysis value within its owner,date/source-ID order,and current-minus-previous.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PreviousValue`, `Delta`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not skip an unknown predecessor.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I05

**Share before filtering** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Sum only positive analysis values per segment/owner. Return the top two distinct owner totals per segment,including all ties,and each owner's percentage of the complete segment total before filtering.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `SegmentTotal`, `SharePercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Filtered-out owners must still contribute to the denominator.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I06

**Every required segment** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owners having at least one analysis row in each exact stored category role A,B,C,and their activity count and known total across all stored category roles.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value activity still proves coverage;an owner with no activity cannot cover a nonempty requirement list.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I07

**Prior calendar window** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every row,return count and average of known values for the same owner on dates from current date minus30 inclusive to current date exclusive.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `PriorKnownCount`, `PriorAverage`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude every same-day row,not just the current source ID;no known history gives count0 and null average.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I08

**First and last known rows** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each master owner,return first and last known-value source IDs by analysis date then source ID. Owners without known values have null IDs.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `LastEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Known zero participates;do not independently take the minimum value instead of the first row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I09

**Complete 2024 calendar** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return all12 calendar months of2024 for every master owner,with event/known counts and total. No activity means total0;an active all-unknown month means null.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `MonthStart`, `EventCount`, `KnownCount`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,MonthStart.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Each owner has exactly12 rows;2025 activity cannot enter2024.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I10

**Dominant segments** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every tied highest-known-total segment per owner. Exclude all-unknown segment groups;keep known zero or negative totals.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `Segment`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,Segment.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The best of several negative totals is the least negative,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I11

**Same-day repeated values** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return owner/date/value groups occurring at least twice,including a repeated unknown value as one group. Return Multiplicity.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `ActivityDate`, `MetricValue`, `Multiplicity`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,ActivityDate,MetricValue.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Unknown-value groups are compared using grouping semantics rather than equality-to-null predicates.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I12

**First threshold crossing** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,consider positive values ordered by date/source ID. Return the first row where cumulative value reaches at least80 percent of that owner's complete positive total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `BatchID`, `RunningValue`, `TotalValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Owners with no positive values produce no threshold crossing.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I13

**Owner median** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return the median known analysis value and KnownCount. Use the average of the two central values for an even count.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `KnownCount`, `MedianValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** No known values gives count0 and null median,not zero.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I14

**Two-generation comparison** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Return every analysis row with its visible parent and visible grandparent IDs and values;retain rows missing either ancestor.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `ParentEventID`, `GrandparentEventID`, `MetricValue`, `ParentValue`, `GrandparentValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two joins cannot follow an excluded parent through to its grandparent.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-I15

**Largest inactive gap** · Intermediate · Suggested coding time:30 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates per owner. Return its largest consecutive-active-date gap in calendar days,with start/end dates;ties choose earlier start. Include all owners with null gap if fewer than two active dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `GapDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Multiple source rows on one day do not create a zero-day consecutive-date gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. Use the small baseline first;the same contract must work on the large practice data.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

**Advanced:15 questions**

#### PHARMA-DQL-06-A01

**Session boundaries and comparable recovery** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each owner,date/source-ID order,new activity starts a new session only when its calendar-date gap from the immediately preceding row exceeds30 days. Return each session's start/end,count,known count,total,previous-session total and percentage change. Include an inactive owner with SessionNo0,null dates,zero counts/total and null comparison.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SessionNo`, `StartDate`, `EndDate`, `EventCount`, `KnownCount`, `TotalValue`, `PreviousValue`, `GrowthPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SessionNo.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A gap exactly30 remains in the session. Null or zero previous total gives null growth. Unknown rows still keep a session active.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A02

**Prior-window median anomaly** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every analysis row,find known values for the same owner over[current date-30,current date),calculate their exact median and count,and flag current value strictly greater than twice that median. Return every current row,not only anomalies.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `SupplierID`, `MetricValue`, `PriorKnownCount`, `PriorMedian`, `IsAnomaly`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Exclude all same-day peers. An even history needs both central values. No known history or unknown current value means IsAnomaly0.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A03

**Smallest complete tie groups reaching80 percent** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,total positive analysis values per owner. Select the smallest descending sequence of complete tied-total groups reaching at least80 percent of that segment's positive total. Never split a tie. Return selected owners,total,distinct-value rank,whole-peer-group cumulative total and complete segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `ValueRank`, `CumulativeValue`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,ValueRank,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** When a peer group crosses80 percent,include the whole group. Known zero/negative/unknown values do not contribute to this positive-share report.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A04

**Six-month cohort retention** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** An owner's acquisition month is the first month in its complete eligible activity history. For acquisition cohorts starting in2024,return offsets0..5 with cohort size,distinct active owners in the offset month and retention percentage. Include zero-activity offset months,including2025 where applicable.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `CohortMonth`, `MonthOffset`, `ActivityMonth`, `CohortSize`, `ActiveOwners`, `RetentionPercent`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** CohortMonth,MonthOffset.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Repeated rows or repeated dates cannot multiply an owner. Do not define acquisition from the2024 slice if earlier history exists.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A05

**Longest activity run with one missing day** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Deduplicate active dates. For each owner,choose an inclusive start/end interval whose endpoints are active and which contains at most one inactive calendar day in total. Maximize number of active dates;ties choose earliest start then earliest end. Include inactive owners with null dates and zero counts.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `ActiveDays`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Two separate one-day holes violate the budget. Multiple source rows on one day count once.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A06

**Cycle-safe parent resolution** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each analysis row,follow visible parent IDs until a root,a missing/excluded parent,or a repeated ID. Return starting ID,terminal visited ID,root ID only if an actual null-parent root is reached,traversed-edge count,cycle flag,boundary flag and slash-delimited visited path. Do not append the repeated cycle ID.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `TerminalEventID`, `RootEventID`, `Depth`, `CycleFlag`, `BoundaryFlag`, `VisitPath`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The supported chain has at most100 edges. A recursion-limit error is not acceptable cycle detection;IDs1 and11 must not be confused by substring matching.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A07

**As-of correction-chain survivors** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each visible null-parent root,consider all visible descendants including the root. At cutoff2024-12-31,choose the latest candidate date not after cutoff,ties greatest source ID. Return root ID,selected ID,date,value and descendant depth;keep a root with no as-of candidate as null selection. Candidates may branch;one branch must not hide another.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `RootEventID`, `SelectedEventID`, `ActivityDate`, `MetricValue`, `Depth`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** RootEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A newer unknown value remains unknown;do not fall back to an older known value. Rootless cycles are excluded and must be diagnosed by the parent-resolution question.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A08

**FIFO interval allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Per owner,treat positive stored category role-A values as supply and positive stored category role-B values as demand. Order each stream by date/source ID and allocate FIFO value without requiring supply date<=demand date. Return every positive supply/demand overlap with allocated value,and a row with the other ID null for each unallocated supply or unfilled demand remainder. Ignore all other stored category roles and nonpositive/unknown values.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `SupplyEventID`, `DemandEventID`, `AllocatedValue`, `UnmatchedValue`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,SupplyEventID,DemandEventID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A supply may feed several demands and vice versa. Allocation plus unmatched supply/demand must independently conserve both sides. Boundary-touching intervals allocate zero and must not appear.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A09

**Conserved largest-remainder allocation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Within each segment,sum positive values per owner and allocate exactly10000 integer basis points proportionally to owner totals. Floor each ideal share,then give leftover points by greatest fractional remainder,ties owner ID ascending. Return totals,allocated basis points and segment total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `Segment`, `SupplierID`, `TotalValue`, `BasisPoints`, `SegmentTotal`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** Segment,SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Independent rounded percentages need not sum to10000. Compare exact remainders,not ratios rounded before flooring. Input positive totals in one segment are bounded by10^18 and analysis values have at most four fractional digits. Exclude segments with no positive contributions.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A10

**Complete inactivity intervals** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every master owner,return maximal inclusive date intervals without eligible activity inside2024. No daily expansion is allowed in the submitted query. Include Jan1/Dec31 boundaries and the leap day correctly.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartDate`, `EndDate`, `MissingDays`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID,StartDate.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** An inactive owner has one366-day interval. Repeated active dates cannot split a gap.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A11

**Ordered three-stage funnel** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Find each owner's earliest completion of stored category role A then B then C in strictly increasing(date,source ID) order. Among chains ending at that earliest C,choose latest B,then latest A before that B. Return the three IDs and start/completion dates.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `FirstEventID`, `SecondEventID`, `ThirdEventID`, `StartDate`, `EndDate`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** A,B,C on the same date can qualify only in increasing source-ID order. Do not independently pick each segment's earliest row.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A12

**Earliest rolling coverage with witnesses** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,find the earliest eligible activity date on which stored category roles A,B,C all occur in the inclusive30-calendar-day window ending that day. Return that trigger date and the latest(date,source ID) witness for each required stored category role within that window.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `TriggerDate`, `AEventID`, `BEventID`, `CEventID`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** The window starts trigger date minus29,not minus30. Unknown-value activity counts;witnesses must come from the same qualifying window.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A13

**Distinct descendant exposure with cycles** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For every eligible row,return count and known-value sum of its distinct proper descendants reachable through visible parent links,and whether any reachable path closes a cycle. Exclude the start row itself even when a cycle returns to it. No descendants means count0,total0;descendants all unknown means null total.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `BatchID`, `DescendantCount`, `KnownCount`, `TotalValue`, `CycleFlag`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** BatchID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Do not add the same descendant twice or hide a rootless cycle. Supported paths have at most100 edges.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A14

**Best mean-centered contiguous block** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** For each owner,let N be its known-value count and T its complete known-value total. Give each known row exact signed score N*analysis value-T;this is a scaled mean-centered score,not a monetary amount. In date/source-ID order,unknown values break the sequence into separate blocks. Select the nonempty contiguous known-row subarray with greatest total score. Ties choose earliest start position then earliest end position. Include owners without known values as null IDs/score and count0.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `StartEventID`, `EndEventID`, `BlockScore`, `EventCount`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Compute N/T over the complete owner,not separately per known block. Even nonnegative stored values can have negative scores. Never choose an empty zero block. Reference cardinality<=1000 rows per owner;explain a scalable prefix-based alternative for larger inputs.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ParentBatchID]; [pharma].[Suppliers].[SupplierID].

#### PHARMA-DQL-06-A15

**Five-table reconciliation** · Advanced · Suggested coding time:60 minutes

**Analysis population — Top:** Within each `SupplierID`, retain all rows in its top two distinct known `BatchCost` value positions; include all ties and exclude unknown values. For fixed A/B/C sequence,coverage and supply/demand roles,use the original `BatchType` of the analysis row's representative source ID,not a transformed text token.

**Task:** Use only original fact records whose primary keys appear in the analysis population. For aggregated analysis rows,this means their representative minimum source ID,not all contributors. Use original stored header values for this reconciliation,not the derived analysis value. For every Suppliers row,return eligible Batches count/known count/sum BatchCost once per batch,inventory units,current product StandardCost*inventory units as a clearly labelled standard-value proxy,distinct stocked warehouses,and count of warehouses where that supplier's eligible inventory units alone exceed Capacity. Missing inventory means zero,not an absent supplier.

**Required results:** Return two result sets. First,an analysis audit with `BatchID`,`SupplierID`,`AnalysisDate`,`AnalysisValue`,`AnalysisSegment`,`AnalysisParentID`,`AnalysisKind`,ordered by `BatchID`. The date,value and segment come from the analysis rule above;parent ID remains the original parent link. `AnalysisKind` is original `BatchType` for the representative source ID. Second,return the business report with these exact columns: `SupplierID`, `EventCount`, `KnownCount`, `TotalValue`, `StockUnits`, `StandardStockValue`, `WarehouseCount`, `OverCapacityWarehouses`. `MetricValue`,`ActivityDate` and `Segment`,where present in the report,are the derived analysis value,date and segment,not new stored columns.

**Final report order:** SupplierID.

**Numeric contract:** Represent analysis values as decimal(28,4). Counts,IDs and exact totals must match. For computed means,medians,percentages and weighted prices,allow absolute difference at most0.000003 from the mathematical result;use decimal arithmetic. The full expected artifact retains mathematical decimal values,which may show more than six fractional digits.

**Rules that will be tested:** Preserve every master owner. Header values are counted once despite multiple children;zero activity gives total0,active all-unknown headers give null. Use historical child prices where stated,not current catalog prices.

**Constraints:** Read-only SQL Server2017+. One statement per result set. No hard-coded fixture answers. Reference-sized inputs have at most1000 analysis rows per owner and absolute analysis values at most10^15;respect any stricter bound in the task. For advanced practice,begin with the small fixture,then use the large data and defend the report grain,correctness and scaling. A solution that passes only the sample is incomplete.

Source columns: [pharma].[Suppliers].[SupplierID]; [pharma].[Suppliers].[SupplierName]; [pharma].[Suppliers].[SupplierCode]; [pharma].[Suppliers].[Region]; [pharma].[Products].[ProductID]; [pharma].[Products].[ProductName]; [pharma].[Products].[ProductCode]; [pharma].[Products].[StandardCost]; [pharma].[Warehouses].[WarehouseID]; [pharma].[Warehouses].[WarehouseName]; [pharma].[Warehouses].[WarehouseCode]; [pharma].[Warehouses].[Capacity]; [pharma].[Batches].[BatchID]; [pharma].[Batches].[SupplierID]; [pharma].[Batches].[BatchCode]; [pharma].[Batches].[BatchType]; [pharma].[Batches].[Status]; [pharma].[Batches].[BatchCost]; [pharma].[Batches].[PackCount]; [pharma].[Batches].[ManufactureDate]; [pharma].[Batches].[ProducedAt]; [pharma].[Batches].[RecordedAt]; [pharma].[Batches].[Note]; [pharma].[Batches].[BackupNote]; [pharma].[Batches].[ParentBatchID]; [pharma].[Batches].[ProductID]; [pharma].[Inventory].[InventoryID]; [pharma].[Inventory].[BatchID]; [pharma].[Inventory].[WarehouseID]; [pharma].[Inventory].[QuantityOnHand]; [pharma].[Inventory].[LastCountDate].

