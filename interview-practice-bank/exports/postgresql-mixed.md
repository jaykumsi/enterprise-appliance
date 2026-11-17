# PostgreSQL mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## PG-QUERIES-05-B12 — Windows and deterministic ties

PostgreSQL / Queries / Beginner

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime. Suggested time: 15 minutes.

**Core problem**

Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / baseline**

Baseline expected: [[1,1],[2,3],[3,5]].

**Interview requirement**

Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture — instructor may preload this before the timer**

```sql
-- Fresh scratch database only. Portable relational practice fixture.
CREATE TABLE Customers(CustomerID INTEGER PRIMARY KEY, CustomerName VARCHAR(80) NOT NULL, Region VARCHAR(10) NOT NULL);
CREATE TABLE Orders(OrderID INTEGER PRIMARY KEY, CustomerID INTEGER NOT NULL REFERENCES Customers(CustomerID), AmountCents INTEGER NULL, Status VARCHAR(10) NOT NULL, CreatedAt VARCHAR(30) NOT NULL);
INSERT INTO Customers VALUES (1,'Ada','North'),(2,'Ben','South'),(3,'Cy','North'),(4,'Dee','West');
INSERT INTO Orders VALUES
(1,1,100,'Open','2024-01-01T00:00:00Z'),
(2,1,100,'Closed','2024-01-02T00:00:00Z'),
(3,2,200,'Open','2024-01-02T00:00:00Z'),
(4,2,NULL,'Pending','2024-01-03T00:00:00Z'),
(5,3,0,'Open','2024-02-01T00:00:00Z');
```


## PG-QUERIES-06-I03 — Recursive CTEs

PostgreSQL / Queries / Intermediate

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime. Suggested time: 30 minutes.

**Core problem**

Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / baseline**

Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Interview requirement**

Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## PG-QUERIES-01-A07 — Filtering and null semantics

PostgreSQL / Queries / Advanced

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime. Suggested time: 45 minutes.

**Core problem**

Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / baseline**

Baseline expected: [[3,200]].

**Interview requirement**

Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture — instructor may preload this before the timer**

```sql
-- Fresh scratch database only. Portable relational practice fixture.
CREATE TABLE Customers(CustomerID INTEGER PRIMARY KEY, CustomerName VARCHAR(80) NOT NULL, Region VARCHAR(10) NOT NULL);
CREATE TABLE Orders(OrderID INTEGER PRIMARY KEY, CustomerID INTEGER NOT NULL REFERENCES Customers(CustomerID), AmountCents INTEGER NULL, Status VARCHAR(10) NOT NULL, CreatedAt VARCHAR(30) NOT NULL);
INSERT INTO Customers VALUES (1,'Ada','North'),(2,'Ben','South'),(3,'Cy','North'),(4,'Dee','West');
INSERT INTO Orders VALUES
(1,1,100,'Open','2024-01-01T00:00:00Z'),
(2,1,100,'Closed','2024-01-02T00:00:00Z'),
(3,2,200,'Open','2024-01-02T00:00:00Z'),
(4,2,NULL,'Pending','2024-01-03T00:00:00Z'),
(5,3,0,'Open','2024-02-01T00:00:00Z');
```
