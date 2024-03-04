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

Dashboard, Edit  = st.tabs(["Dashboard","Edit"])
with Dashboard:
    c = st.container()
    col1, col2, col3 = c.columns(3)

    
    col1.metric(label="Gain", value=5000, delta=1000,)
    col2.metric(label="Loss", value=5000, delta=-1000)
    col3.metric(label="Loss", value=5000, delta=-1000)

    chartcol1, chartcol2 = st.columns(2)
    chart_data = pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

    chartcol1.line_chart(chart_data)

    chart_data2 = pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

    chartcol2.bar_chart(chart_data2)


with Edit:
    st.header("Menu")
    edited_df = st.data_editor(df,column_config={
        "Item": st.column_config.Column(width=300),
        "Price":st.column_config.NumberColumn(format="$%d") },use_container_width=True,num_rows="dynamic",disabled=["ItemID"])
    st.button("Save",use_container_width=True)
    st.divider()

    st.header("Employee")
    st.divider()

    st.header("Customer")
    st.divider()

    st.header("Supplier")
    st.divider()

    st.header("Ingredients")
    st.divider()

    st.header("Menu")
    st.divider()

    st.header("Order Item")
    st.divider()

    st.header("Order")
    st.divider()


