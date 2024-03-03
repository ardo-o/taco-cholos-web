import streamlit as st
import os
from mySQL_Function import greet
from PIL import Image

st.set_page_config(
    page_title="Cholos Tacos"
    
)

# Call the function
result = greet("ff")
print(result)


image1 = Image.open('Photos/pizza.png')
image2 = Image.open('Photos/food3.png')
image3 = Image.open('Photos/food4.png')


user = os.environ['USERNAME']

st.title("Tacos Los Cholos")

HomeTab, OrderTab, CateringTab, MenuTab = st.tabs(["Home","Order","Menu","Catering",])
with HomeTab:
    col1, col2, col3 = st.columns(3)
    col1.image(image1)
    col2.image(image2)
    col3.image(image3)

with OrderTab:
    st.text_input("Label 1")

with CateringTab:
    st.text_input("Label 2")

with MenuTab:
    st.text_input("Label 3")

st.divider()


st.markdown("""
<div style='display: flex; justify-content: center;'>
    <img src="https://img.icons8.com/fluency/48/instagram-new.png" width="25" style='margin-right: 10px;'/>
    <img src="https://img.icons8.com/fluency/48/facebook-new.png" width="25" style='margin-right: 10px;'/>
    <img src="https://img.icons8.com/nolan/64/tiktok.png" width="25" style='margin-right: 10px;'/>
</div>
""", unsafe_allow_html=True)


st.markdown("<small style='display: block; text-align: center; color: grey;'>©2023 Tacos Los Cholos. All rights reserved.</small>", unsafe_allow_html=True)
