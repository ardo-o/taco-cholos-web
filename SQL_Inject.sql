-- Show all the available database.
SHOW DATABASES;

-- To reset and have a clean start, let's drop the CholosTacos database if it exists.
DROP database IF EXISTS CholosTacos;

-- create the database, CholosTacos;
create database CholosTacos;

-- Show all the available database (again).
SHOW DATABASES;

-- Activate the CholosTacos database to make it a default.
use CholosTacos;

-- Dislpay all the tables in the current database (CholosTacos).
SHOW TABLES;

-- To reset and have a clean start, let's drop the CholosTacos table if it exists.
DROP TABLE IF EXISTS Order_Item;

DROP TABLE IF EXISTS Employee;

DROP TABLE IF EXISTS Customer;

DROP TABLE IF EXISTS Supplier;

DROP TABLE IF EXISTS Order_Line;

DROP TABLE IF EXISTS Menu;

DROP TABLE IF EXISTS Ingredient;

-- Create the CholosTacos table as shown in Replit.
CREATE TABLE Order_Item (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    ItemID INT,
    Quantity INT,
    Subtotal DECIMAL(10, 2)
);

CREATE TABLE Employee(
	EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(100),
    EmailAddress VARCHAR(100),
    PhoneNumber VARCHAR(25),
    JobTitle VARCHAR(50),
    EmployeeStatus VARCHAR(1)
);

CREATE TABLE Customer(
	CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(100),
    PhoneNumber Varchar(25),
    EmailAddress VARCHAR(100)
);

CREATE TABLE Supplier(
	SupplierID INT,
    SupplierName VARCHAR(100),
    ContactPerson VARCHAR(100),
    PhoneNumber VARCHAR(25),
    EmailAddress VARCHAR(100)
);

CREATE TABLE Menu(
    ItemID INT,
    ItemName VARCHAR(100),
    Description VARCHAR(400),
    Price DECIMAL(10,2)
);

CREATE TABLE Ingredients(
	IngredientID INT,
    ItemID INT,
    SupplierID INT,
    IngredientName  VARCHAR(100),
    UnitPrice DECIMAL(10,2),
    QuanitityInStock Int
);

CREATE TABLE Order_Line(
OrderID INT,
EmployeeID INT,
CustomerID INT(10),
OrderDate DATE,
AmountPaid DECIMAL(10,2),
PaymentMethod VARCHAR(50)
);


-- Dislpay all the tables in the current database.
show tables;

INSERT INTO Order_Item (OrderItemID, OrderID, ItemID, Quantity,Subtotal) VALUES
(1, 256, 1,3,17.97),
(2, 256, 2,1,9.99),
(3, 257, 3,1,7.99),
(4, 258, 1,1,5.99),
(5, 258, 2,1,9.99),
(6, 258, 3,1,7.99),
(7, 258, 4, 1, 4.25);

INSERT INTO Employee (EmployeeID, FirstName, LastName, EmailAddress, PhoneNumber, JobTitle, EmployeeStatus) VALUES
(1, 'James', 'Rodriguez', 'jrod@gmail.com', '(123)-456-7891', 'Cashier', 'A'),
(2, 'Diego', 'Gonzalez', 'Diegogonz@outlook.com', '(245)-367-9845', 'Cook', 'A'),
(3, 'Juan', 'Rivera', 'jriver22@hotmail.com', '(567)-242-7845', 'Server', 'A');

INSERT INTO Customer(CustomerID, FirstName, LastName, PhoneNumber, EmailAddress) VALUES
(01, 'Karla', 'Gomez', '(944)-276-0978', 'kgomez12@gmail.com'),
(02, 'DJ', 'White', '(343)-245-0974', 'djwhite1999@gmail.com'),
(03, 'Emeily', 'Jackson', '(566)-242-0771', 'emja2001@hotmail.com');

INSERT INTO Supplier(SupplierID, SupplierName, ContactPerson, PhoneNumber, EmailAddress) VALUES
(123, 'West Coast Prime Meats', 'Carl Sujo', '(323)-876-0934)', 'info@westcoastprimemeats.com'),
(124, 'Natures Produce', 'Brooke Swanek', '(213)-482-9274' ,'info@naturesproduce.com'),
(125, 'El Metate', 'Antonio Mejilla', '(714)-0034-9820' , 'info@elmetate.com');

INSERT INTO Order_Line(OrderID, EmployeeID, CustomerID, OrderDate, AmountPaid, PaymentMethod) VALUES
(256 , 1, 02, '2024-03-18', 27.96, 'Debit'),
(257 , 2, 01, '2024-03-19', 7.99, 'Credit'),
(258 , 3, 03, '2024-03-20', 28.22, 'Credit');

INSERT INTO Menu (ItemID, ItemName, Description, Price)
VALUES
    (1, 'Tacos', 'Authentic Mexican tacos served with carna asada, topped with fresh cilantro, and onion, wrapped in soft tortillas.', 5.99),
    (2, 'Burritos', 'Classic burritos filled with seasoned carne asada, rice, beans, and cheese, wrapped in a warm flour tortilla.', 9.99),
	(3, 'Quesadillas', 'Grilled flour tortillas filled with melted cheese and steak, served with onion, and cilantro.', 7.99),
    (4, 'Soda', 'Refreshing coke to wash down the delicious food.',4.25);

INSERT INTO Ingredients (IngredientID, ItemID, SupplierID, IngredientName, UnitPrice, QuanitityInStock)
VALUES
    (1, 1, 125, 'Tortillas', 0.50, 100),
    (2, 1, 123, 'Asada', 2.75, 50),
    (3, 1, 124, 'Cilantro', 0.25, 30),
    (4, 1, 124, 'Onion', 0.25, 40),
    (5, 2, 124, 'Cheese', 0.50, 60),
    (6, 2, 125, 'Tortillas', 1.00, 100),
    (7, 2, 124, 'Rice', 1.00, 30),
    (8, 2, 124, 'Beans', 1.00, 40),
    (9, 2, 123, 'Asada', 3.25, 50),
    (10, 2, 124, 'Cheese', 0.50, 60),
	(11, 2, 124, 'Cilantro', 0.25, 30),
    (12, 2, 124, 'Onion', 0.25, 40),
	(13, 3, 124, 'Cheese', 0.50, 60),
    (14, 3, 125, 'Tortillas', 1.00, 100),
	(15, 3, 123, 'Asada', 3.50, 50),
    (16, 3, 124, 'Cilantro', 0.25, 30),
    (17, 3, 124, 'Onion', 0.25, 40),
    (18, 4, 124, 'Soda', 1.50, 40);


-- Display all data from CholosTacos.