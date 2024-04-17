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

CREATE TABLE Menu(
    ItemID INT AUTO_INCREMENT PRIMARY KEY,
    ItemName VARCHAR(100) NOT NULL,
    Description VARCHAR(400),
    Price DECIMAL(10,2) NOT NULL
);

CREATE TABLE Employee(
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(25) NOT NULL,
    JobTitle VARCHAR(50) NOT NULL,
    EmployeeStatus CHAR(1) NOT NULL
);

CREATE TABLE Customer(
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(25) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL
);

CREATE TABLE Order_Line(
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT NOT NULL,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    AmountPaid DECIMAL(10,2) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
-- Create the CholosTacos table as shown in Replit.
CREATE TABLE Order_Item (
    OrderItemID INT AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ItemID INT NOT NULL,
    Quantity INT NOT NULL,
    Subtotal DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderItemID, OrderID), -- Combined primary key
    FOREIGN KEY (OrderID) REFERENCES Order_Line(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Menu(ItemID)
);

CREATE TABLE Supplier(
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    ContactPerson VARCHAR(100),
    PhoneNumber VARCHAR(25) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL
);

CREATE TABLE Ingredients(
    IngredientID INT,
    ItemID INT NOT NULL,
    SupplierID INT NOT NULL,
    IngredientName VARCHAR(100) NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    QuantityInStock INT NOT NULL,
	PRIMARY KEY (IngredientID, ItemID),
    FOREIGN KEY (ItemID) REFERENCES Menu(ItemID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

-- Dislpay all the tables in the current database.
show tables;

-- Inserting records into the Employee table
INSERT INTO Employee (EmployeeID, FirstName, LastName, EmailAddress, PhoneNumber, JobTitle, EmployeeStatus) VALUES
(1, 'James', 'Rodriguez', 'jrod@gmail.com', '(123)-456-7891', 'Cashier', 'A'),
(2, 'Diego', 'Gonzalez', 'Diegogonz@outlook.com', '(245)-367-9845', 'Cook', 'A'),
(3, 'Juan', 'Rivera', 'jriver22@hotmail.com', '(567)-242-7845', 'Server', 'A'),
(4, 'Maria', 'Lopez', 'marialopez@gmail.com', '(789)-123-4567', 'Manager', 'A'),
(5, 'Carlos', 'Sanchez', 'csanchez@yahoo.com', '(321)-654-9876', 'Server', 'A'),
(6, 'Ana', 'Martinez', 'anamartinez@gmail.com', '(987)-654-3210', 'Cook', 'A'),
(7, 'Pedro', 'Garcia', 'pgarcia@gmail.com', '(555)-555-5555', 'Server', 'A');

-- Inserting records into the Customer table
INSERT INTO Customer(CustomerID, FirstName, LastName, PhoneNumber, EmailAddress) VALUES
(1, 'Karla', 'Gomez', '(944)-276-0978', 'kgomez12@gmail.com'),
(2, 'DJ', 'White', '(343)-245-0974', 'djwhite1999@gmail.com'),
(3, 'Emeily', 'Jackson', '(566)-242-0771', 'emja2001@hotmail.com'),
(4, 'Michael', 'Johnson', '(123)-456-7890', 'michael.johnson@example.com'),
(5, 'Jennifer', 'Brown', '(234)-567-8901', 'jennifer.brown@example.com'),
(6, 'David', 'Davis', '(345)-678-9012', 'david.davis@example.com'),
(7, 'Sarah', 'Taylor', '(456)-789-0123', 'sarah.taylor@example.com');

INSERT INTO Menu (ItemID, ItemName, Description, Price)
VALUES
    (1, 'Tacos', 'Authentic Mexican tacos served with carna asada, topped with fresh cilantro, and onion, wrapped in soft tortillas.', 5.99),
    (2, 'Burritos', 'Classic burritos filled with seasoned carne asada, rice, beans, and cheese, wrapped in a warm flour tortilla.', 9.99),
	(3, 'Quesadillas', 'Grilled flour tortillas filled with melted cheese and steak, served with onion, and cilantro.', 7.99),
    (4, 'Soda', 'Refreshing coke to wash down the delicious food.',4.25),
    (5, 'Michelada', 'Traditional Mexican beer cocktail made with beer, lime juice, assorted sauces, spices, and peppers, served in a chilled, salt-rimmed glass.', 6.50),
    (6, 'Churro', 'Deep-fried dough pastry dusted with cinnamon and sugar, served hot and crispy.', 3.75),
	(7, 'Flan', 'Classic Mexican dessert made with creamy caramel custard, topped with a rich caramel sauce.', 4.99);
    
-- Inserting records into the Supplier table
INSERT INTO Supplier(SupplierID, SupplierName, ContactPerson, PhoneNumber, EmailAddress) VALUES
(123, 'West Coast Prime Meats', 'Carl Sujo', '(323)-876-0934', 'info@westcoastprimemeats.com'),
(124, 'Natures Produce', 'Brooke Swanek', '(213)-482-9274' ,'info@naturesproduce.com'),
(125, 'El Metate', 'Antonio Mejilla', '(714)-0034-9820' , 'info@elmetate.com'),
(126, 'La Tiendita Mexicana', 'Maria Sanchez', '(555)-666-7777', 'maria@latienditamexicana.com'),
(127, 'Los Amigos Tortilleria', 'Juan Hernandez', '(777)-888-9999', 'juan@losamigostortilleria.com'),
(128, 'Salsa y Más', 'Elena Garcia', '(888)-999-0000', 'elena@salsaymas.com'),
(129, 'La Cocina de Abuela', 'Pedro Martinez', '(111)-222-3333', 'pedro@lacocinadeabuela.com');    

-- Inserting records into the Order_Line table
INSERT INTO Order_Line(OrderID, EmployeeID, CustomerID, OrderDate, AmountPaid, PaymentMethod) VALUES
(256 , 3, 01, '2024-03-18', 27.96, 'Debit'),
(257 , 5, 02, '2024-03-19', 7.99, 'Credit'),
(258 , 5, 03, '2024-03-20', 28.22, 'Credit'),
(259 , 7, 04, '2024-03-21', 15.75, 'Cash'),
(260 , 3, 05, '2024-03-22', 42.50, 'Credit'),
(261 , 5, 06, '2024-03-23', 19.99, 'Debit'),
(262 , 7, 07, '2024-03-24', 33.75, 'Cash');

INSERT INTO Order_Item (OrderItemID, OrderID, ItemID, Quantity,Subtotal) VALUES
(1, 256, 1,3,17.97),
(2, 256, 2,1,9.99),
(3, 257, 3,1,7.99),
(4, 258, 1,1,5.99),
(5, 258, 2,1,9.99),
(6, 258, 3,1,7.99),
(7, 258, 4, 1, 4.25);

INSERT INTO Ingredients (IngredientID, ItemID, SupplierID, IngredientName, UnitPrice, QuantityInStock)
VALUES
    (1, 1, 127, 'Tortillas', 0.50, 100),
    (2, 1, 123, 'Asada', 2.75, 50),
    (3, 1, 124, 'Cilantro', 0.25, 30),
    (4, 1, 128, 'Onion', 0.25, 40),
    (1, 2, 127, 'Tortillas', 1.00, 100),
    (6, 2, 124, 'Rice', 1.00, 30),
    (7, 2, 124, 'Beans', 1.00, 40),
    (2, 2, 123, 'Asada', 3.25, 50),
    (5, 2, 124, 'Cheese', 0.50, 60),
	(3, 2, 124, 'Cilantro', 0.25, 30),
    (4, 2, 128, 'Onion', 0.25, 40),
	(5, 3, 124, 'Cheese', 0.50, 60),
    (1, 3, 127, 'Tortillas', 1.00, 100),
	(2, 3, 123, 'Asada', 3.50, 50),
    (3, 3, 124, 'Cilantro', 0.25, 30),
    (4, 3, 128, 'Onion', 0.25, 40),
    (8, 4, 124, 'Soda', 1.50, 40),
    (9, 5, 125, 'Michelada', 4.50, 40),
    (10, 6, 126, 'Churro', 1.50, 40),
    (11, 7, 129, 'Flan', 2.50, 40);

-- Display all data from CholosTacos.

SELECT * FROM menu ;