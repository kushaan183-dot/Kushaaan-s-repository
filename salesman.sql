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

CREATE TABLE IF NOT EXISTS Customer (
customer_id TEXT PRIMARY KEY,
cust_name TEXT,
city TEXT,
grade INTEGER,
Salesman_id TEXT,
FOREIGN KEY (Salesman_id) REFERENCES Salesman (Salesman_id)
);
INSERT INTO Customer(customer_id,cust_name,city,grade,Salesman_id)VALUES
('2214','Chandresh','Chennai',0.15,'Kushaan'),
('2215','Magesh','Kerala',0.13,'Pranave'),
('2216','Yash','Ooty',1.35,'Yashwath'),
('2217','Raj','Singapur',2.1,'Manesh'),
('2218','Yashwath','Chennai',0.15,'Yash'),
('2219','Pracash','Kerala',0.13,'Parush');
SELECT * FROM Customer ;