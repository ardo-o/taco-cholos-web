import streamlit as st
import pandas as pd
import os
from mySQL_Function import greet
from PIL import Image
import mysql.connector
import numpy as np


st.set_page_config(
    page_title="Cholos Tacos",
    initial_sidebar_state="collapsed",
    layout="wide"
    
)

DbPass = os.environ['DBPass']
st.title("Tacos Los Cholos")

# Connecting from the server
db = mysql.connector.connect(user='root',
                   password=DbPass,
                   host='127.0.0.1',
                   database='CholosTacos')
 
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM Menu")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df = pd.DataFrame(rows, columns=columns)

cur.execute("SELECT * FROM employee")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df2 = pd.DataFrame(rows, columns=columns)

cur.execute("SELECT * FROM customer")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df3 = pd.DataFrame(rows, columns=columns)

cur.execute("SELECT * FROM supplier")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df4 = pd.DataFrame(rows, columns=columns)

cur.execute("SELECT * FROM Ingredients")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df5 = pd.DataFrame(rows, columns=columns)

#cur.execute("SELECT * FROM Order_Item")
cur.execute(
"""SELECT 
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
    Menu m ON oi.ItemID = m.ItemID;""")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df6 = pd.DataFrame(rows, columns=columns)

#cur.execute("SELECT * FROM Order_Line")
cur.execute(
"""SELECT
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
    Employee e ON ol.EmployeeID = e.EmployeeID;""")


# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df7 = pd.DataFrame(rows, columns=columns)

cur.execute('SELECT OrderDate, SUM(AmountPaid) FROM Order_Line GROUP BY OrderDate')
rows = cur.fetchall()

# Process the data
dates = [row[0] for row in rows]
amounts_paid = [float(row[1]) for row in rows]  # Ensure 'AmountPaid' is treated as a float

# Create a DataFrame
df8 = pd.DataFrame({'Date': dates, 'AmountPaid': amounts_paid})
df8['Date'] = pd.to_datetime(df8['Date'])  # Convert 'Date' column to datetime format
df8.set_index('Date', inplace=True)





Dashboard, Edit  = st.tabs(["Dashboard","Edit"])
with Dashboard:
    c = st.container()
    col1, col2, col3 = c.columns(3)
    total_orders = df7['OrderID'].nunique()
    total_customers = df7['CustomerID'].nunique()
    total_amount_paid = round(df8['AmountPaid'].sum(),2)
    
    col1.metric(label="Total Orders", value=total_orders, delta=total_orders-100,)
    col2.metric(label="Total Customers", value=total_customers, delta=total_customers-125)
    col3.metric(label="Total Sales", value=total_amount_paid, delta=total_amount_paid -1000)

    chartcol1, chartcol2 = st.columns(2)
    chart_data = df7
    #pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

    #chartcol1.line_chart(chart_data, x=df7['OrderDate'],y="AmountPaid") 
    chartcol1.subheader("Daily Sales")
    # Time series chart
    chartcol1.line_chart(df8)

    #chart_data2 = pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

    #chartcol2.bar_chart(chart_data2)
    chartcol2.subheader("Payment Method Distribution")
    payment_method_counts = df7['PaymentMethod'].value_counts()
    chartcol2.bar_chart(payment_method_counts)

with Edit:
    st.header("Menu")
    edited_df = st.data_editor(df,column_config={
        "Item": st.column_config.Column(width=300),
        "Price":st.column_config.NumberColumn(format="$%.2f") },use_container_width=True,num_rows="dynamic",disabled=["ItemID"])

    submit_button= st.button("Submit",use_container_width=True)
    if submit_button:
        for index, row in edited_df.iterrows():
            # Extract values from the row
            price = row['Price']
            item_id = str(row['ItemID'])
            Description = row['Description']
            ItemName = row['ItemName']
            print(item_id)
            if item_id == "nan" :
            
                # Execute the SQL INSERT statement for each row
                cur.execute("INSERT INTO Menu (ItemName, Description, price) VALUES (%s, %s, %s)", (ItemName, Description, price ))

    db.commit()
    st.success("Data inserted successfully!")
    st.divider()

    st.header("Employee")
    edited_df = st.data_editor(df2,column_config={
        "EmployeeID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=["EmployeeID"])
    st.button("Save Employee",use_container_width=True)
    st.divider()

    st.header("Customer")
    edited_df = st.data_editor(df3,column_config={
        "CustomerID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=["CustomerID"])
    st.button("Save Customer",use_container_width=True)   
    st.divider()

    st.header("Supplier")
    edited_df = st.data_editor(df4,column_config={
        "SupplierID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=["SupplierID"])
    st.button("Save Supplier",use_container_width=True)       
    st.divider()

    st.header("Ingredients")
    edited_df = st.data_editor(df5,column_config={
        "IngredientID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=["IngredientID"])
    st.button("Save Ingredient",use_container_width=True)          
    st.divider()

    st.header("Order_Line")
    edited_df = st.data_editor(df7,column_config={
        "OrderID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=True)      
    st.divider()

    st.header("Order Item")
    edited_df = st.data_editor(df6,column_config={
        "OrderItemID": st.column_config.Column(width=100) },use_container_width=True,num_rows="dynamic",disabled=True)  
    st.divider()




