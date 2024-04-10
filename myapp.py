import streamlit as st
import pandas as pd
import os
from Query import *
from PIL import Image
import mysql.connector
import re
from decimal import Decimal
from datetime import date

st.set_page_config(

    page_title="Cholos Tacos new",

    initial_sidebar_state="collapsed",
    layout="wide"
    
)
st.sidebar.markdown("Select page view.")

DbPass = os.environ['DBPass']

# Connecting from the server
db = mysql.connector.connect(user='root',
                   password=DbPass,
                   host='127.0.0.1',
                   database='CholosTacos')
 

cur = db.cursor()

cur.execute(getMenu())
# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df = pd.DataFrame(rows, columns=columns)
df['Quantity'] = 0



def validate_phone_number(phone_number):
    # Regular expression to match a valid phone number format
    pattern = r'^[0-9]{10}$'  # Matches a 10-digit number
    if not re.match(pattern, str(phone_number)):
        return False
    return True

st.title("Tacos Los Cholos")

HomeTab, OrderTab, MenuTab,   = st.tabs(["Home","Order","Menu"])
with HomeTab:
    col1, col2, col3 = st.columns(3)
    col1.image("https://i.ibb.co/FXSBgTx/pizza.png")
    col2.image("https://i.ibb.co/QJCQWXc/food3.png")
    col3.image("https://i.ibb.co/rG6WYRY/food4.png")


with OrderTab:
    OTcol1, OTcol2 = st.columns(2)

    first_name = OTcol1.text_input("First Name", key="first_name")
    last_name = OTcol2.text_input("Last Name", key="last_name")
    email = OTcol1.text_input("Email Address", key="email")
    phone_number = OTcol2.number_input("Phone Number", step=1, format="%i", key="phone_number")
    c = st.container()

    edited_df = c.data_editor(df,column_config={
        "ItemName": st.column_config.Column(width=300),
        "Price":st.column_config.NumberColumn(format="$%.2f") },use_container_width=True,hide_index=True,disabled=["ItemName","ItemID","Description","Price"])
    
        
    
    edited_df['Price'] = edited_df['Price'].apply(Decimal)
    edited_df['Quantity'] = edited_df['Quantity'].apply(Decimal)
    columnsum = (edited_df['Price'] * edited_df['Quantity']).sum()
    tax_rate = Decimal('0.075')
    tax = columnsum * tax_rate
    tax = round(tax, 2)
    c.markdown(f"<div style='text-align: right;'>Sub Total: $<b>{columnsum}</b></div>", unsafe_allow_html=True)
    c.markdown(f"<div style='text-align: right;'>Tax: $<b>{tax}</b></div>", unsafe_allow_html=True)
    c.markdown(f"<div style='text-align: right;'>Total: $<b>{columnsum+tax}</b></div>", unsafe_allow_html=True)

    submit_button= c.button("Submit",use_container_width=True)

    if submit_button:
        # Data validation
        if not first_name:
            st.warning("Please enter a valid First Name.")
        elif not last_name:
            st.warning("Please enter a valid Last Name.")
        elif not email:
            st.warning("Please enter a valid Email Address.")
        elif not validate_phone_number(phone_number):
            st.warning("Please enter a valid 10-digit Phone Number.")
        elif columnsum ==0:
            st.warning("Please enter a QTY.")
        else:
            # Define values to insert or check
            values = (first_name, last_name, str(phone_number), email)

            # Execute a SELECT query to check if the record exists
            cur.execute(customerExist(first_name, last_name, str(phone_number), email))

            # Fetch the first row (if any)
            rowd = cur.fetchone()

            if rowd:
                # If the record exists, retrieve the primary key
                customer_id = rowd[0]
                
            else:
                # If the record does not exist, insert a new record
                cur.execute(insertCustomer(first_name, last_name, str(phone_number), email))
                
                # Retrieve the primary key of the newly inserted record
                customer_id = cur.lastrowid

            while cur.nextset():
                pass

            today_date = date.today().isoformat()
            cur.execute(addOrderLine(1, customer_id, today_date, columnsum+tax,"Debit"))
            orderID = cur.lastrowid

            for index, row in edited_df.iterrows():
                # Extract values from the row
                Price = row['Price']
                item_id = row['ItemID']
                quantity = row['Quantity']
                subtot = Price*quantity

                if quantity > 0:
                
                    cur.execute( addOrderItem(orderID, item_id, quantity,subtot ))

            db.commit()
            st.success("Data inserted successfully!")
        

with MenuTab:
    cur.execute(getMenuItems())
    # Fetch all the rows from the SQL result
    rows = cur.fetchall()

    # Get column names
    columns = [desc[0] for desc in cur.description]

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Initialize an empty string to store the HTML code
    html_code = ''

    # Iterate through each row of the DataFrame
    for index, row in df.iterrows():
        # Extract values from the current row
        item_name = row['ItemName']
        description = row['Description']
        
        # Construct HTML code for the current row
        row_html = f'<h2>{item_name}</h2>\n<p>{description}</p>\n'
        
        # Append the HTML code for the current row to the overall HTML code
        html_code += row_html

        # Display the HTML content using Streamlit
    st.markdown(html_code, unsafe_allow_html=True)

st.divider()


st.markdown("""
<div style='display: flex; justify-content: center;'>
    <img src="https://img.icons8.com/fluency/48/instagram-new.png" width="25" style='margin-right: 10px;'/>
    <img src="https://img.icons8.com/fluency/48/facebook-new.png" width="25" style='margin-right: 10px;'/>
    <img src="https://img.icons8.com/nolan/64/tiktok.png" width="25" style='margin-right: 10px;'/>
</div>
""", unsafe_allow_html=True)


st.markdown("<small style='display: block; text-align: center; color: grey;'>©2023 Tacos Los Cholos. All rights reserved.</small>", unsafe_allow_html=True)

db.close()

