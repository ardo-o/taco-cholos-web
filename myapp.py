import streamlit as st
import pandas as pd
import os
from mySQL_Function import greet
from PIL import Image
import mysql.connector

st.set_page_config(
    page_title="Cholos Tacos",
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
 
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM orders")

# Fetch all the rows from the SQL result
rows = cur.fetchall()

# Get column names
columns = [desc[0] for desc in cur.description]

# Create a DataFrame
df = pd.DataFrame(rows, columns=columns)





# Call the function
result = greet("ff")
print(result)


image1 = Image.open('Photos/pizza.png')
image2 = Image.open('Photos/food3.png')
image3 = Image.open('Photos/food4.png')


st.title("Tacos Los Cholos")

HomeTab, OrderTab, MenuTab, CateringTab,  = st.tabs(["Home","Order","Menu","Catering",])
with HomeTab:
    col1, col2, col3 = st.columns(3)
    col1.image(image1)
    col2.image(image2)
    col3.image(image3)

with OrderTab:
    OTcol1, OTcol2 = st.columns(2)

    OTcol1.text_input("First Name")
    OTcol2.text_input("Last Name")
    OTcol1.text_input("Email Address")
    OTcol2.number_input("Phone Number",step=1,format="%i")
    #%d %e %f %g %i %u
    c = st.container()

 #   df = pd.DataFrame(
 #   [
 #      {"Item": "Food 1","Price":10, "Quantity": 0 },
 #      {"Item": "Food 2", "Price":10,"Quantity": 0 },
 #      {"Item": "Food 3","Price":10, "Quantity": 0},
 #  ]
 #   )

    edited_df = c.data_editor(df,column_config={
        "Item": st.column_config.Column(width=300),
        "Price":st.column_config.NumberColumn(format="$%d") },use_container_width=True,hide_index=True)
    
        # Sum column 'A' where column 'B' is True
    columnsum = (edited_df['Price'] * edited_df['Quantity']).sum()
    c.markdown(f"<div style='text-align: right;'>Total: $<b>{columnsum}</b></div>", unsafe_allow_html=True)


    c.button("Submit",use_container_width=True)

with CateringTab:
    st.text_input("Label 2")

with MenuTab:
    cur.execute("SELECT ItemName, Description FROM Menu")

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

