import streamlit as st
import pandas as pd

st.set_page_config(page_title="home", layout="wide")
st.image(
    r"C:\Users\techno\Desktop\MIDTERM\air quality.jpg",
    use_container_width=True
)
html= st.markdown("""
<div style="text-align: center; color: blue;">
   Air Quality Data and Analysis project 
</div>
""", unsafe_allow_html=True)
