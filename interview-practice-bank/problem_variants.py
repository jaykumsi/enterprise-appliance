"""Fifteen distinct programming cores per skill, reused across difficulty tiers.

Each entry includes its own acceptance example. Equivalent language skills
share contracts, not language-specific solution text.
"""
PROBLEMS={}


def group(name,text):
    PROBLEMS[name]=[dict(core=c.strip(),example=e.strip()) for c,e in
                    (line.split('|') for line in text.strip().splitlines() if line.strip())]
    assert len(PROBLEMS[name])==15,name


group('numbers',r'''
Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.|"12.3" -> 1230; "1.234" -> INVALID.
Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.|-1 -> "-0.01"; 1200 -> "12.00".
Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.|"01.200" and "1.2" -> true; "-0" and "0" -> true.
Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.|"1.25"+"-0.30" -> "0.95".
Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.|2147483647+1 with signed32 bounds -> OVERFLOW.
Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.|(10,3) -> [4,3,3].
Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.|(101,1000) -> 10.
Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.|("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".
Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.|(-7,3) -> -3; (7,-3) -> -3.
Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.|(123,2,3) -> 1230; (123,2,1) -> INEXACT.
Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.|(1,3,2,6) -> 0.
Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.|"-000" -> "0"; "+0012" -> "12".
Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.|([2,3,-1],-4,4) -> 1.
Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.|(10,[1,1,1]) -> [4,3,3].
Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.|("-1A",16) -> -26; ("2",2) -> INVALID.
''')

group('loops',r'''
Implement shipping(grams): positive integer weights through1000 cost500 cents,each started additional1000 costs200. Invalid weight -> INVALID.|1001 -> 700; 2000 -> 700.
Implement fizz_labels(n) returning labels for1..n: multiples3 -> Fizz,5 -> Buzz,both -> FizzBuzz,otherwise decimal number. Nonnegative integer n required.|n=5 -> [1,2,Fizz,4,Buzz].
Implement digit_sum(n) for signed integers,ignoring the sign. Do not convert the entire number to floating point.|-1203 -> 6; 0 -> 0.
Implement run_lengths(values),returning [value,count] for each consecutive equal run in original order.|[a,a,b,a] -> [[a,2],[b,1],[a,1]].
Implement longest_positive_streak(values),returning the maximum consecutive count of integers>0.|[1,2,0,3,-1,4,5,6] -> 3.
Implement next_business_day(day,closed_days) using integer day numbers. closed_days is a finite set; return smallest integer>day not in the set.|day5,closed[6,7] -> 8.
Implement tier_cost(units): first100 units at2 cents each,next100 at3,remaining at5. Units is nonnegative integer; return exact total.|250 -> 750.
Implement multiplicative_steps(start,target) for positive integers: repeatedly double start until >=target. Return steps and final value.|(3,20) -> {steps:3,value:24}.
Implement balance_path(deltas) returning running integer totals from zero and the first negative index or null.|[2,-3,5] -> totals[2,-1,4],first_negative1.
Implement triangle_rows(n) returning rows [1],[1,2],...,[1..n]. Nonnegative integer n; no shared mutable row references.|3 -> [[1],[1,2],[1,2,3]].
Implement collatz_step(n) for a positive integer only: even -> n/2,odd ->3n+1. Implement trace until1 with max_steps positive; return LIMIT if not complete.|n3,max10 -> [3,10,5,16,8,4,2,1].
Implement count_between(values,low,high) with low inclusive,high exclusive. Reject low>high; return count and matching original indices.|([1,2,3,2],2,3) -> count2,indices[1,3].
Implement staircase_change(coins,target) for a supplied descending list of positive denominations; repeatedly take largest available denomination<=remaining. Return greedy counts or IMPOSSIBLE; do not claim minimum coins.|coins[4,3],target6 -> greedy IMPOSSIBLE despite possible3+3.
Implement stop_at_sentinel(values,sentinel) returning sum and count before the first sentinel. Do not include or read beyond the sentinel in an iterator.|[2,3,-1,100],sentinel-1 -> sum5,count2.
Implement decimal_digits(n),returning signed integer n as a sign flag and most-significant-first digit array using integer operations.|-105 -> {negative:true,digits:[1,0,5]}.
''')

group('functions',r'''
Implement apply_discount(prices,pct): integer cents>=0,pct0..100. Return new prices floor(price*(100-pct)/100),without input mutation.|[101,200],10 -> [90,180].
Implement compose(functions) producing a function that applies supplied pure unary functions left to right. Empty list means identity.|[x+1,x*2] applied3 -> 8.
Implement partition(values,predicate) returning accepted and rejected lists in original order. Call predicate exactly once per value.|[1,2,3],even -> accepted[2],rejected[1,3].
Implement fold_until(values,initial,step,stop). Apply step to each item and stop before the next item once stop(accumulator) is true. Return accumulator and consumed count.|[2,3,9],initial0,sum,stop>=5 -> value5,consumed2.
Implement map_with_index(values,fn),calling fn(value,index) once per value and returning new results. Indices start0.|[a,b],concatenate value/index -> [a0,b1].
Implement make_counter(initial) with independent add(delta),value() closures. State changes only within that instance.|Counters0 and10; first.add2 -> first2,second10.
Implement apply_if(value,predicate,transform): call transform only when predicate is true; otherwise return original. Return a trace of which callbacks ran.|-1,is_positive,double -> -1,trace[predicate].
Implement curry3(fn) accepting arguments across three one-argument calls. Each partially applied instance retains only its own arguments.|add3(1)(2)(3) -> 6; separate partials remain independent.
Implement safe_call(fn,arg),returning {ok:value} or {error:type,message}; catch only declared application exceptions,not cancellation/termination signals.|fn raises ValidationError -> structured error,not false success.
Implement memoized_last(fn) caching only the most recent immutable argument/result. Exceptions never populate cache; expose invocation count.|Calls a,a,b,a -> underlying3 calls.
Implement route(value,rules,default) using the first predicate that matches and only its transform. Evaluate predicates in order; no later predicates after a match.|Rules negative->N,even->E; value-2 -> N.
Implement zip_apply(functions,values),requiring equal lengths,calling each function on corresponding value. Reject mismatched lengths before any callback.|[double,negate],[3,4] -> [6,-4].
Implement repeat_until(value,transform,predicate,limit),checking predicate before each transform. Return value,steps and satisfied; stop after at most limit transforms.|start1,double,predicate>=5,limit3 -> value8,steps3,true.
Implement validate_then(value,validators,action). Run validators in order,collect all returned field errors,and invoke action once only when no errors.|Two validation errors -> both reported,action calls0.
Implement pipeline(stages,input),where each stage returns {ok:value} or {error:code}. Stop at first error and report its stage index; later stages never run.|success+error+success -> error at1,third calls0.
''')

group('lists',r'''
Implement merge_intervals for half-open integer intervals. Ignore empty intervals,merge overlap/touch,reject start>end,sort ascending.|[[5,8],[1,3],[3,6]] -> [[1,8]].
Implement rotate_right(values,k) for nonnegative integer k,without mutating input. Empty list remains empty.|[1,2,3],4 -> [3,1,2].
Implement stable_partition(values,pivot): values<pivot first,then equal,then greater,each group retaining input order.|[3,1,2,1],2 -> [1,1,2,3].
Implement move_zeros(values),moving numeric zeros to the end and retaining other element order. Return a new integer list.|[0,2,0,1] -> [2,1,0,0].
Implement intersect_multiset(a,b),retaining each integer min(count_a,count_b) times,output ascending.|[2,1,2],[2,2,3] -> [2,2].
Implement merge_sorted(a,b),retaining all duplicates and ascending order without sorting the concatenation.|[1,3],[1,2] -> [1,1,2,3].
Implement missing_ranges(sorted_distinct,low,high) returning inclusive missing intervals within inclusive bounds.|[1,3,7],1,8 -> [[2,2],[4,6],[8,8]].
Implement transpose(matrix). Require rectangular rows; [] -> []; ragged input -> INVALID. Output rows must not alias input rows.|[[1,2],[3,4]] -> [[1,3],[2,4]].
Implement flatten_one(values) where each element is either integer or list of integers; flatten exactly one level and reject deeper nesting.|[1,[2,3],[]] -> [1,2,3].
Implement maximum_subarray(values) returning sum,start,end for nonempty integer input. End exclusive; ties prefer smallest start then smallest end.|[-2,3,-1,3] -> {sum:5,start:1,end:4}.
Implement product_except_self(values) for integers,using no division. Return products of all other positions; empty -> []; one item -> [1].|[1,2,3] -> [6,3,2]; [0,2,0] -> [0,0,0].
Implement deduplicate_sorted(values) returning unique ascending integers plus original multiplicities,without mutating input.|[1,1,2,2,2] -> values[1,2],counts[2,3].
Implement pair_indices(values,target) returning lexicographically smallest [i,j],i<j,whose integer values sum to target,or null.|[3,2,4,3],6 -> [0,3].
Implement k_way_merge(sorted_lists),retaining all integer duplicates,ascending,without flatten-and-sort.|[[1,4],[],[1,3]] -> [1,1,3,4].
Implement circular_next_greater(values),returning next strictly greater value to the right wrapping once,or null per position.|[1,2,1] -> [2,null,2].
''')

group('maps',r'''
Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.|[b,a,b,c] -> a.
Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.|[b,a,b] -> [{value:a,count:1},{value:b,count:2}].
Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.|[b,a,b] -> {a:[1],b:[0,2]}.
Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.|{a:x,b:x} -> duplicates[x].
Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.|left[a,b],right[b:2] -> [a:null,b:2].
Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.|[a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].
Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.|a:v1/x,a:v2/y -> a:v2/y.
Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.|[eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].
Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.|[a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.
Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.|{1:2,5:3},{1:4,2:7} -> 8.
Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.|a:+5,a:-5,b:+3 -> a:0,b:3.
Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.|[1,1,2,2],3 -> 4.
Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].|[a,b,a,c],3 -> [2,3].
Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.|{a:1,b:2},a->b,b->a -> {a:2,b:1}.
Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.|[e:x,e:x,f:y] -> [e:x,f:y].
''')

group('strings',r'''
Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.|" ab-012 " -> "AB-012".
Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.|"abba" -> 2; "" -> 0.
Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.|" a  b " -> "b a".
Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.|"A man, a plan, a canal: Panama" -> true.
Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.|[flower,flow,flight] -> fl.
Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.|"aaabb" -> [{character:a,count:3},{character:b,count:2}].
Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.|"([)]" -> invalid index2; "([])" -> valid.
Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.|"a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].
Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.|[{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.
Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.|"swiss" -> 1.
Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.|"ADOBECODEBANC","ABC" -> "BANC".
Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.|"1.02.0","1.2" -> 0.
Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.|"babad" -> "bab".
Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.|"3,1-3,5" -> [1,2,3,5].
Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.|"waterbottle","erbottlewat" -> true.
''')

group('patterns',r'''
Extract distinct standalone codes matching two uppercase ASCII letters,hyphen,three digits. Adjacent ASCII letter/digit invalidates a boundary. Preserve first occurrence.|"AB-123 xAB-124 AB-125!" -> [AB-123,AB-125].
Validate usernames: lowercase ASCII letter then2..19 lowercase letters/digits. Return VALID or INVALID with no partial match.|abc -> VALID; 1abc -> INVALID.
Parse YYYY-MM-DD text and validate actual Gregorian calendar dates,not only the regex shape. Return canonical date or INVALID.|2024-02-29 valid; 2023-02-29 invalid.
Parse signed decimal text with optional minus and at most2 fractional digits,requiring digits before decimal. Return integer cents; no exponent/whitespace.|-1.2 -> -120; .5 -> INVALID.
Extract key=value tokens with ASCII identifier keys and double-quoted values supporting escaped quote/backslash. Reject malformed nonspace text and duplicate keys.|a="x y" b="z" -> {a:"x y",b:"z"}.
Validate IPv4 dotted decimal: exactly4 components0..255,no leading zeros except0. Return four integers or INVALID.|192.168.0.1 valid; 01.2.3.4 invalid.
Parse a log line LEVEL timestamp message,LEVEL in INFO,WARN,ERROR and timestamp integer>=0. Preserve the entire message after the second separator.|"INFO 10 hello world" -> {level:INFO,time:10,message:"hello world"}.
Replace standalone ASCII secret assignments token=VALUE with token=[REDACTED],where VALUE is nonempty nonwhitespace text. Do not redact mytoken= text.|"token=abc mytoken=def" -> "token=[REDACTED] mytoken=def".
Extract @mentions from text with name[A-Za-z][A-Za-z0-9_]{0,19}; mention must not be preceded by an ASCII word character. Return occurrences with code-point offsets.|"Hi @Ada and x@Bob" -> Ada only,offset3.
Validate order references ORD-YYYY-NNNN with year2000..2099 and exactly4 digits suffix. Return parsed year/sequence or INVALID.|ORD-2024-0007 -> {year:2024,sequence:7}.
Parse ISO-like durations PT followed by optional hours then minutes then seconds,integer quantities,at least one field. Return total seconds; reject repeated/out-of-order fields.|PT1H2M3S -> 3723; PT1M1H -> INVALID.
Extract decimal integer tokens bounded by non-word characters,allowing a leading minus. Return exact integers and original positions; do not capture digits embedded in IDs.|"x12 -3 +4" -> -3 and4,not12.
Validate semantic versions major.minor.patch with nonnegative integer components,no leading zeros,optional hyphen prerelease[A-Za-z0-9.-]+. Return components and prerelease or INVALID.|1.2.3-beta -> parsed; 01.2.3 -> INVALID.
Implement wildcard_match(text,pattern) where ? matches one code point and * any sequence; backslash has no special meaning. Match the entire string without translating untrusted text into executable code.|abc,a*c -> true; abc,a? -> false.
Validate a password policy without logging the value: length12..64 code points,at least one ASCII uppercase,lowercase,digit,and one of!@#$; no whitespace. Return missing requirement names sorted.|"Abcdefghij1!" -> no failures.
''')

group('search',r'''
Implement lower_bound(sorted,target): first index value>=target,or length. Integers ascending; logarithmic comparisons.|[1,2,2,5],2 -> 1.
Implement upper_bound(sorted,target): first index value>target,or length. Integers ascending; logarithmic comparisons.|[1,2,2,5],2 -> 3.
Return first/last target positions in an ascending integer list,or null if absent,using logarithmic search.|[1,2,2,5],2 -> [1,2].
Implement insertion_index for descending integers: first index value<=target. Preserve earlier strictly larger values.|[9,7,7,2],7 -> 1.
Search a rotated ascending distinct integer list,return original index or null. Do not reconstruct/sort the list.|[4,5,1,2,3],2 -> 3.
Find the minimum in a nonempty rotated ascending distinct integer list using logarithmic comparisons.|[4,5,1,2,3] -> 1.
Find kth smallest integer in two ascending lists,one-based k,without sorting the combined lists. Invalid k -> INVALID.|[1,3],[2,4],3 -> 3.
Implement stable order sort: amount descending,null last,id ascending; IDs unique. Do not mutate input.|b:200,a:200,c:null -> [a,b,c].
Return the three smallest distinct values with their full multiplicities from unsorted integers; fewer than3 distinct means all distinct.|[5,1,2,1,4] -> [(1,2),(2,1),(4,1)].
Implement integer_sqrt(n) for nonnegative integers: largest x with x*x<=n. Use no floating sqrt and reject negative input.|15 -> 3; 16 -> 4.
Given sorted nonoverlapping inclusive intervals,find the interval containing point or null using logarithmic search.|[[1,3],[5,8]],5 -> [5,8].
Given monotone predicate false then true over indices0..n-1,find first true or null with bounded predicate calls. Do not call outside range.|[false,false,true,true] -> 2.
Find the smallest positive capacity allowing ordered positive jobs to be split into at most d contiguous groups,each sum<=capacity.|jobs[3,2,2],d2 -> 4.
Return count of sorted integers in half-open [low,high) using two bounds; low>high -> INVALID.|[1,2,2,3],2,3 -> 2.
Merge k ascending streams using a heap,retaining duplicates and returning ascending output. Never materialize all streams before the first output.|[1,4],[1,3],[] -> [1,1,3,4].
''')

group('graphs',r'''
Return lexicographically smallest topological order of nodes with edges prerequisite->dependent. Missing references -> INVALID; cycle -> CYCLE.|a->c,b->c -> [a,b,c].
Return all reachable nodes from start in a directed graph,excluding start unless reached again through a cycle. Output IDs sorted.|a->b,b->c -> froma [b,c].
Return shortest unweighted directed path from start to goal,ties choose lexicographically smallest node sequence. No path -> null.|a->b,a->c,b->d,c->d -> [a,b,d].
Detect a directed cycle and return a concrete closed path witness,or null. Visit starting nodes/neighbors in lexicographic order for deterministic output.|a->b,b->a -> [a,b,a].
Return connected components of an undirected graph; nodes inside each component sorted,components ordered by smallest node. Keep isolated nodes.|nodes[a,b,c],edgea-b -> [[a,b],[c]].
Return tree depths from root for parent-pointer records; reject missing parent and cycles. Root depth0; disconnected roots remain separate.|a:null,b:a,c:b -> depths0,1,2.
Return longest prerequisite-chain length in a DAG,measured in edges. Cycle -> CYCLE; empty graph ->0.|a->b,b->c,a->c -> 2.
Return all ancestor sources of a target: upstream nodes with indegree0. Detect cycles in the target's upstream subgraph.|a->b,b->c,d->c -> sources[a,d].
Clone a directed graph preserving node IDs,edges and cycles but no shared mutable node/adjacency objects with the input.|a->b,b->a -> independent equal structure.
Given task durations and a DAG,compute earliest finish times with unlimited parallel workers. Each task starts after all predecessors finish.|a:2,b:3 both ->c:1 => c finish4.
Determine whether an undirected graph is bipartite. Return two sorted color groups or a concrete odd-cycle witness.|trianglea-b-c-a -> not bipartite.
Return a node's nearest common ancestor in a single-root parent tree for two nodes. Reject absent nodes/cycles.|a root,b:a,c:a,d:b; d,c -> a.
Count distinct directed paths from source to target in a DAG using exact integers; cycle -> CYCLE. Empty path source=target counts1.|a->b,a->c,b->d,c->d ->2.
Remove one specified edge from a graph copy and return which previously reachable nodes from source become unreachable. Do not mutate input.|a->b,b->c; removea->b -> [b,c].
Return strongly connected components of a directed graph,sorting nodes and components deterministically. Preserve isolated nodes.|a<->b,b->c -> [[a,b],[c]].
''')

group('validation',r'''
Validate rows with nonempty string id and positive integer qty. Booleans are not integers. Return accepted rows and rejected index/reasons sorted by field.|[{id:a,qty:0}] -> rejected index0,reason qty.
Validate a date-range request requiring valid Gregorian start/end and start<=end. Return all field errors; reversed valid dates -> RANGE.|2024-02-30..2024-03-01 -> start error.
Validate port text as canonical decimal integer1..65535,no sign/whitespace/leading zeros. Return integer or field error.|"080" -> error; "80" ->80.
Validate a batch of unique IDs. Reject all positions whose ID is repeated rather than choosing an arbitrary survivor; return rejected positions ascending.|[a,b,a] -> rejected[0,2],accepted[b].
Validate nested order items: id nonempty,items array,each sku nonempty and qty positive integer. Return JSON-pointer-style paths for all errors sorted.|{id:a,items:[{sku:"",qty:0}]} -> /items/0/qty,/items/0/sku.
Validate an enum transition Open->Paid->Shipped or Open->Cancelled. Illegal event returns INVALID_TRANSITION without changing original state.|Paid->Cancelled -> rejected,still Paid.
Validate CSV-like integer fields without coercing empty/null/boolean to0. Return typed integer or TYPE,FORMAT,RANGE for supplied bounds.|text"0",bounds0..2 ->0; empty -> FORMAT.
Validate percentages as integer0..100 and amounts as nonnegative integer cents; collect independent field errors before calculation.|pct101,amount-1 -> errors amount,pct.
Validate object keys against required[id,qty] and optional[note]. Return missing and unknown keys separately,sorted.|{id:a,quantity:1} -> missing qty,unknown quantity.
Validate a finite dependency graph's referenced nodes before cycle checking. Report all missing references first,otherwise return a cycle witness if present.|nodes[a],edgea->b -> missing[b].
Validate Unicode display names: after trimming ASCII outer spaces,require1..40 code points and no control characters U+0000..001F. Return normalized name or errors.|" Ada " -> Ada; newline inside -> control error.
Validate checksums as exactly64 lowercase hexadecimal characters; distinguish missing,wrong type and invalid format.|64 a characters -> valid; uppercase A -> FORMAT.
Validate schema compatibility old/new field type/required maps: optional additions allowed,removal/type change/optional->required rejected.|Add optional note -> compatible; cents type changed -> incompatible.
Implement validate_then_commit(batch,validator,store). Validate every item first; any error means zero store calls. Return all item errors.|One invalid of3 -> no writes.
Implement safe_error(exception) mapping known validation/conflict/not-found types to safe codes; unknown error -> INTERNAL and sanitized message,never stack/secret text.|Unknown exception containing synthetic password -> INTERNAL with no password.
''')

group('reconcile',r'''
Reconcile unique-id integer balances,returning missing,extra and changed entries sorted by id. Duplicate IDs -> INVALID.|expected a:0,b:2;actual b:3 -> missinga,changedb.
Compare multisets of complete rows,including nulls; return each distinct row's expected/actual multiplicity when unequal.|expected[a,a],actual[a] -> a counts2,1.
Compare two ordered sequences and return first differing zero-based index or null; a missing trailing element differs from null value.|[a,null],[a] -> index1.
Reconcile versions per id: missing,extra,stale,newer and same-version-conflicting payloads. Exact match produces no finding.|a:v2/x vs a:v1/x -> stalea.
Verify a total by independently summing signed ledger entries; return computed,claimed and delta. Use exact integers.|entries[5,-2],claimed4 -> computed3,delta-1.
Check a partition's accepted/rejected lineage covers each input position exactly once. Return missing,double-covered and unknown positions.|input0..2,accepted[0,1],rejected[1] -> missing2,double1.
Reconcile a left join's source IDs: each source must appear once,including unmatched rows. Return multiplied and missing source IDs.|source[a,b],output[a,a] -> multiplieda,missingb.
Compare schemas by name,type,nullability and column order; return structural changes separately from reorders.|[id:int,note:text] vs reversed -> reorder only.
Validate a transition trace against allowed edges and increasing sequence numbers. Return first impossible transition or numbering gap.|Open->Paid->Open -> invalid second transition.
Check sorted output with explicit nulls-last,amount-descending,id-ascending rules. Return first adjacent violating pair.|a:100,b:200 -> violation0,1.
Reconcile parent/child references,returning orphan child IDs and unused parent IDs separately,sorted.|parents[a,b],children[x->a,y->c] -> orphan[y],unused[b].
Compare a cached response to authoritative revision. Return FRESH only if key,tenant and revision all match; else named mismatches.|same key and revision,wrong tenant -> tenant mismatch.
Verify allocation conservation: shares must be integers>=0,sum equal total,and optional weights list length match. Return all invariant failures.|total10,shares[4,3,2] -> sum failure.
Compare source/sink manifests by path and checksum; distinguish missing,extra and changed content despite matching file counts.|source a/x,b/y;sink a/x,c/y -> missingb,extrac.
Implement a test-case reducer for a supplied deterministic predicate fails(list). Repeatedly remove one item left-to-right if failure remains until no single removal works; return locally minimal list.|Failure when both a,b present;[x,a,y,b] -> [a,b].
''')

group('generators',r'''
Implement lazy batches(iterator,size),yielding at most size items; size positive. Emit no empty final batch and do not preconsume the next batch.|[1,2,3],2 -> [1,2],[3].
Implement lazy take(iterator,n),consuming at most n items,n>=0. n0 must not request even one source item.|source1,2,3;n2 ->1,2.
Implement lazy drop_while(iterator,predicate). Stop invoking predicate after first false and yield that item plus all remaining.|[1,2,0,3],positive ->0,3.
Implement lazy pairwise(iterator),yielding consecutive overlapping pairs with constant retained state.|[1,2,3] ->(1,2),(2,3).
Implement lazy running_sum(iterator) for signed integers,emitting each prefix sum.|[2,-1,4] ->2,1,5.
Implement lazy unique_first(iterator) retaining seen immutable keys and yielding first occurrence in input order.|a,b,a,c ->a,b,c.
Implement lazy merge_sorted(a,b),retaining duplicates and at most one lookahead per input.|[1,3],[1,2] ->1,1,2,3.
Implement lazy interleave(iterators) round-robin,skipping exhausted sources,without buffering full sources.|[1,2],[a],[x,y] ->1,a,x,2,y.
Implement lazy flatten(iterables),exhausting one child at a time and closing an opened child on cancellation where its interface supports close.|[[],[1,2],[3]] ->1,2,3.
Implement lazy sliding_windows(iterator,k),yielding independent lists of exactly k items; k positive.|[1,2,3,4],3 ->[1,2,3],[2,3,4].
Implement lazy enumerate_from(iterator,start),yielding exact integer index/item pairs without reading ahead.|[a,b],start5 ->(5,a),(6,b).
Implement lazy chunks_by_key(iterator,key_fn) for adjacent equal keys. One lookahead allowed; return key/group pairs preserving order.|a1,a2,b1,a3 keyed firstletter ->a:[a1,a2],b:[b1],a:[a3].
Implement lazy limit_until(iterator,predicate),yielding items strictly before first matching sentinel and consuming that sentinel only once.|[1,2,0,9],iszero ->1,2;9 remains unread.
Implement two-consumer tee with an explicit max_lag bound. If one advances too far,return LAG_LIMIT rather than buffering unbounded input.|maxlag1;consumerA reads2 items beforeB -> second read LAG_LIMIT.
Implement lazy map_errors(iterator,fn),yielding per-item ok/error and continuing after declared application errors. Cancellation must propagate.|[1,0,2],integer reciprocal validation ->ok,error,ok.
''')

group('classes',r'''
Implement Inventory reserve/release on initial A5. Invalid qty/unknown SKU returns false; release cannot exceed reservations. Preserve available+reserved.|reserveA3 true,releaseA4 false -> available2,reserved3.
Implement BankAccount deposit/withdraw in integer cents. Positive amounts only; no overdraft; failed withdrawal leaves balance unchanged.|initial10,withdraw11 ->false,balance10.
Implement immutable Money(currency,cents),three uppercase currency letters; add only identical currency,with explicit overflow policy.|USD100+USD-20 ->USD80; USD+EUR ->INVALID.
Implement bounded FIFO Queue(capacity) with put/get,return FULL/EMPTY without mutation on rejection. Capacity positive.|cap2,put a,b,c ->thirdFULL;get ->a.
Implement Stack with push,pop,peek and snapshot independent of future mutation. Empty pop/peek ->EMPTY.|push a,b;pop ->b;snapshot[a].
Implement Reservation state Open->Confirmed->Completed or Open->Cancelled. Rejected transitions preserve state and version.|Confirmed->Cancelled ->INVALID,stillConfirmed.
Implement immutable DateRange(start,end) using integer half-open bounds,start<=end. intersect returns overlap or an empty range at max(start).|[1,5) intersect[3,7) ->[3,5).
Implement ShoppingCart keyed SKU with positive integer quantities and exact cents. Set quantity0 removes; invalid update changes nothing.|Aprice2,qty3 ->total6;setA0 ->empty.
Implement Counter instances with atomic-by-contract add and snapshot but no shared state between instances. Detect declared integer overflow.|instances1,1;first.add2 ->3,second1.
Implement Task with pending,running,succeeded,failed. Only pending->running and running->terminal allowed; result only for succeeded,error only for failed.|pending->succeeded ->INVALID.
Implement RateLimiter capacity2,refill1 per integer second using injected monotonic clock. Accepted acquire consumes1; invalid backward clock ->INVALID.|t0 two accepted,thirdrejected;t1 one accepted.
Implement versioned Document.update(expected_version,text). Initial version1; success increments; stale expected rejects without changing text.|update1,x ->v2;update1,y ->CONFLICT.
Implement SeatMap reserve(seat,owner),release(seat,owner). Only owner may release; reserving same seat/owner again is idempotent; other owner conflicts.|A byu thenA byv ->CONFLICT;releaseA byv denied.
Implement a dependency-injected Checkout using SKU price lookup and payment gateway. Validate every quantity/SKU before charging exactly once.|A200,qty2 ->charge400;unknownSKU ->zerocharges.
Implement ExpiringValue with injected clock,put(value,ttl),get(). ttl positive; value expires when now>=inserted+ttl. Do not reset expiry on read.|putx at0,ttl5;get4 ->x;get5 ->NOT_FOUND.
''')

group('cache',r'''
Implement bounded LRU memoizer for pure string-key function. Hits update recency; exceptions not cached; expose hit/miss counts.|cap2,calls a,b,a,c,b ->hits1,misses4.
Implement FIFO cache where hits do not affect eviction order. Return evicted key on insertion past capacity.|cap2,put a,b,geta,putc ->evicta.
Implement TTL cache using injected clock; expire exactly at now>=created+ttl,reads do not renew expiry.|putaat0,ttl5;get5 ->MISS.
Implement single-last-result memoizer. Only immediately repeated equal immutable argument is a hit; exceptions never cached.|a,a,b,a ->onehit.
Implement per-tenant cache keys so identical resource IDs in different tenants remain independent.|t1/a:x,t2/a:y ->two distinct values.
Implement version-aware cache lookup requiring exact resource and requested revision; stale entry must be a miss.|stored a:v2;requesta:v3 ->MISS.
Implement cache-aside lookup with injected repository; cache only nonnull successes. Failure and not-found are not cached.|missing key requested twice ->two repo calls.
Implement explicit negative caching with distinct NOT_FOUND marker and shorter ttl2 versus positive ttl10. Never confuse null payload with absence.|notfoundat0 read1 ->negativehit,read2 ->miss.
Implement batch cache lookup preserving input order/repeats and fetching each unique missing key once.|keys[a,b,a],cacheb ->fetchaonce,threeoutputs.
Implement invalidate_prefix over exact case-sensitive key strings with no path normalization. Return removed keys sorted.|raw/a,raw2/a;prefixraw/ ->remove raw/a only.
Implement write-through cache: persist before updating cache; repository failure leaves prior cache value/revision intact.|cachedx,persisty fails ->stillx.
Implement cached pure result cloning so a caller cannot mutate a cached collection through a returned reference.|get list,append ->laterget unaffected.
Implement capacity-by-weight LRU with positive integer entry weights. Oversized entry rejected before evicting any valid entry.|budget3,existinga weight2,newb weight4 ->reject,keepa.
Implement a cache statistics snapshot with hits,misses,evictions,expired removals. Snapshot must not reset counters or expose mutable internals.|onehit,twomisses ->exact counters preserved after read.
Implement canonical typed keys distinguishing integer1,string"1",booleantrue and null. Structured input objects ignore field order but retain array order.|{a:1,b:2} equals reordered object key;[1,2] differs[2,1].
''')

group('windows',r'''
Return length of longest substring with no repeated Unicode code point; empty text ->0.|abba ->2.
Return largest sum of any exactly k consecutive integers,k positive and<=length. Ties return earliest start with sum.|[1,4,-1,3],k2 ->sum5,start0.
For positive integers and positive target,return shortest contiguous length with sum>=target or0 if absent.|[2,3,1,2,4,3],7 ->2.
Return number of distinct values in every contiguous window of positive length k;k>length ->[].|[a,b,a,c],3 ->[2,3].
Return longest substring length with at most k distinct Unicode code points,k>=0.|eceba,k2 ->3.
Return longest contiguous integer-array length containing at most k zeros; every value must be0 or1.|[1,0,1,0,1],k1 ->3.
Return whether sorted integer input contains a distinct-index pair summing to target using two pointers.|[1,2,4,5],6 ->true.
Remove duplicates from a sorted integer array into a new array,allowing each value at most2 times. Preserve order.|[1,1,1,2,2,3] ->[1,1,2,2,3].
Return all unique value triplets summing to0,each triplet ascending,triplets lexicographically sorted. Use distinct original positions.|[-1,0,1,2,-1,-4] ->[[-1,-1,2],[-1,0,1]].
Return maximum water area for nonnegative integer heights: area=(j-i)*min(height_i,height_j);<2 bars ->0.|[1,8,6,2,5,4,8,3,7] ->49.
Return sorted squares from an ascending signed-integer array without sorting all output afterward.|[-4,-1,0,3] ->[0,1,9,16].
Return shortest substring covering all required code-point multiplicities,ties earliest;no match ->null,empty required ->empty.|ADOBECODEBANC,ABC ->BANC.
Return all zero-based start indices where an anagram of a nonempty pattern occurs in lowercase ASCII text.|cbaebabacd,abc ->[0,6].
Return length of longest substring that can become one repeated uppercase ASCII letter by replacing at most k characters.|AABABBA,k1 ->4.
Return count of contiguous subarrays of positive integers with product<positive target. Target<=1 yields0; use exact arithmetic.|[10,5,2,6],100 ->8.
''')

group('files',r'''
Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.|a,2 followed by a,-1 ->a:1.
Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.|lines a,empty,space,b ->total4,blank2,nonblank2.
Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.|bytes010203,chunk2 ->copied3,samebytes.
Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.|a\nb\nc\n,n2 ->a\n,b\n.
Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.|a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.
Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.|Existingold,newwritefails ->destinationold.
Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.|bytes61FF ->offset1.
Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.|a,b,c,n2 ->b,c.
Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.|fn failsline2 ->line1written,line2error.
Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.|data/a.csv valid;../secret invalid.
Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.|0102 vs0103 ->offset1.
Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.|valid,bad,valid ->ok,errorline2,ok.
Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.|Permissionfailure ->UNKNOWN rather thanempty.
Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.|Bodythrows ->release1,originalerrorpropagates.
Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.|Failurebeforecommit ->lastoffsetunchanged.
''')

group('formats',r'''
Parse CSV header id,amount with quoted commas/escaped quotes. Require nonempty id and signed integer amount;return records or logical record errors.|"a,b",12 ->id a,b,amount12.
Flatten JSON orders with items arrays into order_id,sku,qty rows preserving item order. Missing/null items ->empty;nonarray ->rejected.|o1 itemsA2,B1 ->2rows.
Write CSV for records containing comma,quote,newline values using a standards-aware writer,then parse back and prove exact round trip.|id a,b remains onefield.
Compare two JSON objects structurally,ignoring object-field order but retaining array order and distinguishing number,string,boolean,null.|{a:1,b:2} equals reorderedobject;[1,2] differs[2,1].
Validate NDJSON one document per nonblank line with nonempty id,integer cents;return accepted rows plus line/error paths.|line2 missingid ->rejectline2 only.
Normalize a JSON record schema requiring id:string and qty:positive integer. Extra keys retained in a separate metadata object,not silently assigned to protected fields.|{id:a,qty:2,admin:true} ->metadata admin,notauthority.
Convert a CSV row with named optional columns to JSON,null only for an explicitly supplied NULL marker;empty string stays empty.|noteempty ->"";noteNULL ->null.
Parse a JSON array of versioned records and select highest version per id;equal version/different payload ->CONFLICT.|a:v1/x,a:v2/y ->a:v2/y.
Validate nested JSON depth<=supplied positive limit and total scalar count<=budget before transformation. Return precise limit error.|depth3,limit2 ->DEPTH_LIMIT.
Flatten nested JSON objects into escaped JSON-pointer paths;arrays retain numeric indices,null remains a leaf. Root scalar path is empty.|{a:[1,null]} ->/a/0:1,/a/1:null.
Reconstruct JSON from nonconflicting pointer/leaf pairs. Reject a path that is both a scalar and an ancestor.|/a:1 and/a/b:2 ->CONFLICT.
Parse CSV with required unique headers;return duplicate/missing/unknown header findings before reading data. Required[id,cents],optional[note].|id,id ->duplicateid,missingcents.
Convert exact decimal JSON string fields into integer cents using optional minus/digits/atmost2 fractiondigits. Reject numeric floating inputs instead of guessing original precision.|"1.25" ->125;numeric1.25 ->TYPE.
Implement streaming JSON-array output for an iterator of JSON-compatible records. Correctly place commas/brackets for empty/single/multiple input;never materialize all records.|[]iterator ->"[]".
Reconcile CSV and JSON representations of the same unique-ID ledger,comparing exact cents and text values after explicit parsing rules.|CSVa,2 andJSONa cents3 ->changeda.
''')

# Rows without an authored alternate set retain their service/framework-specific
# core. Do not apply a vaguely related algorithm set just to inflate diversity.
ALIASES={
    'Numeric types and conversion':'numbers','Primitives and exact arithmetic':'numbers','Types and exact numeric boundaries':'numbers',
    'Conditions and loops':'loops','Control flow and methods':'loops',
    'Functions and scope':'functions','Closures and scope':'functions',
    'Lists and tuples':'lists','Lists and comparators':'lists',
    'Dictionaries and sets':'maps','Comprehensions and grouping':'maps','Maps sets and equality':'maps','Arrays maps and sets':'maps','Streams and collectors':'maps',
    'Parsing and normalization':'strings','Strings and Unicode':'strings',
    'Regular expressions':'patterns','Sorting and binary search':'search','Recursion and graphs':'graphs',
    'Exceptions and validation':'validation','Classes and invariants':'classes','OOP and invariants':'classes',
    'Iterators and generators':'generators','Decorators and caching':'cache',
    'Unit tests and debugging':'reconcile','Unit and integration testing':'reconcile','Tests fakes and deterministic time':'reconcile',
    'Two pointers and sliding windows':'windows','Files and context managers':'files','Exceptions and resource handling':'files','CSV and JSON':'formats',
}
