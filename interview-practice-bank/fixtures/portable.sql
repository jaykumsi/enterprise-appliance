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
