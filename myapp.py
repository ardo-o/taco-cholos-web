import streamlit as st
import os
from mySQL_Function import greet

# Call the function
result = greet("ff")
print(result)

user = os.environ['USERNAME']

st.write(""" hi""")