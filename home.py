import streamlit as st
from image import get_image
import os

API_KEY = os.environ.get("API_KEY")
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

image = get_image(URL)

st.set_page_config(layout='wide')
col1, col2, col3 = st.columns([0.5, 1.5, 0.5])

with col2:
    st.header("Galaxy Picture of the Day")
    st.subheader(image["Title"])
    st.image('image.jpg')
    st.write(image["Description"])
