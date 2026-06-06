CREATE TABLE IF NOT EXISTS Salesman(
Salesman_id TEXT PRIMARY KEY,
name TEXT,
City TEXT,
Commision REAL 
);
INSERT INTO SALESMAN(Salesman_id,name,City,Commision)VALUES
('2214','Kushaan','Chennai',0.15),
('2215','Pranave','Kerala',0.13),
('2216','Yashwath','Ooty',1.35),
('2217','Manesh','Singapur',2.1),
('2218','Yash','Chennai',0.15),
('2219','Parush','Kerala',0.13);
SELECT * FROM Salesman ;

CREATE TABLE IF NOT EXISTS Customer(
customer_id TEXT PRIMARY KEY,
cust_name TEXT,
city TEXT,
grade INTEGER,
Salesman_id TEXT,
FOREIGN KEY (Salesman_id) REFERENCES Salesman (Salesman_id)
);
INSERT INTO Customer(customer_id,cust_name,city,grade,Salesman_id)VALUES
('2220','Chandresh','Chennai',0.15,'2214'),
('2221','Magesh','Kerala',0.13,'2215'),
('2222','Yash','Ooty',1.35,'2216'),
('2223','Raj','Singapur',2.1,'2217'),
('2224','Yashwath','Chennai',0.15,'2218'),
('2225','Pracash','Kerala',0.13,'2219');
SELECT * FROM Customer ;

CREATE TABLE IF NOT EXISTS Orders(
ord_no TEXT PRIMARY KEY,
purch_amd REAL,
Ord_text TEXT,
customer_id TEXT,
Salesman_id TEXT,
FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
FOREIGN KEY(Salesman_id) REFERENCES Salesman(Salesman_id)
);
INSERT INTO Orders(ord_no,purch_amd,Ord_text,customer_id,Salesman_id)VALUES
('70001', 150.5, '2012-10-05', '2220','2214'),
('70009',270.65, '2012-09-10', '2221', '2215'),
('70002', 65.26, '2012-10-05', '2222', '2216'),
('70004', 110.5, '2012-08-17', '2223', '2217'),
( '70007', 948.5, '2012-09-10', '2224', '2218'),
('70005', 2400.6, '2012-07-27', '2225', '2219');
SELECT *
FROM Customer
JOIN Orders ON Customer.customer_id=Orders.customer_id
WHERE Orders.ord_text='2012-10-05';
SELECT Customer.cust_name,Salesman.name
from Customer
JOIN Salesman ON Customer.Salesman_id=Salesman.Salesman_id;
