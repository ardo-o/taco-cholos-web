#SQL statments

def getMenu():
 return "SELECT * FROM MENU"

def customerExist(first_name, last_name, phone_number, email):
    return f"SELECT CustomerID FROM Customer WHERE FirstName = '{first_name}' AND LastName = '{last_name}' AND PhoneNumber = '{phone_number}' AND EmailAddress = '{email}'"

def insertCustomer(first_name, last_name, phone_number, email):
    return f"INSERT INTO Customer (FirstName, LastName, PhoneNumber, EmailAddress) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}')"

def addOrderLine(EmployeeID, CustomerID, OrderDate, AmountPaid, PaymentMethod):
   return f"INSERT INTO Order_Line (EmployeeID, CustomerID, OrderDate, AmountPaid, PaymentMethod) VALUES ('{EmployeeID}', '{CustomerID}', '{OrderDate}', '{AmountPaid}', '{PaymentMethod}')"

def addOrderItem(OrderID, ItemID, Quantity, Subtotal):
   return f"INSERT INTO Order_Item (OrderID, ItemID, Quantity, Subtotal) VALUES ('{OrderID}', '{ItemID}', '{Quantity}', '{Subtotal}')"

def getMenuItems():
   return "SELECT ItemName, Description FROM Menu"

def getEmployee():
   return "SELECT * FROM employee"

def getCustomer():
   return "SELECT * FROM customer"

def getSupplier():
   return "SELECT * FROM supplier"

def getIngredients():
   return "SELECT * FROM Ingredients"

def JoinItemMenu():
   return """SELECT 
    oi.OrderItemID,
    oi.OrderID,
    oi.ItemID,
    m.ItemName,
    oi.Quantity,
    m.Price,
    oi.Subtotal


FROM 
    Order_Item oi
JOIN 
    Menu m ON oi.ItemID = m.ItemID;"""

def JoinOrderCustomer():
   return """SELECT
    ol.OrderID,
    ol.EmployeeID,
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    e.JobTitle AS EmployeeJobTitle,
    ol.CustomerID,
    c.FirstName AS CustomerFirstName,
    c.LastName AS CustomerLastName,
    ol.OrderDate,
    ol.AmountPaid,
    ol.PaymentMethod
FROM 
    Order_Line ol
JOIN 
    Customer c ON ol.CustomerID = c.CustomerID
JOIN 
    Employee e ON ol.EmployeeID = e.EmployeeID;"""

def metricsLine():
   return "SELECT OrderDate, SUM(AmountPaid) FROM Order_Line GROUP BY OrderDate"

def addMenu(ItemName, Description, price):
   return f"INSERT INTO Menu (ItemName, Description, price) VALUES ('{ItemName}', '{Description}', '{price}')"

def reduceInventory(updated_value):
   return f"UPDATE Ingredients SET QuantityInStock = QuantityInStock -1   WHERE IngredientID = '{updated_value}'"

def itemIngredient(item_id):
   return f"SELECT * FROM Ingredients where itemid = {item_id};"
