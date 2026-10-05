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
df = pd.read_parquet("Air_Quality_Cleaned.parquet")
st.subheader("Data Overview")
st.dataframe(df.head(10))
#sata description
st.subheader("Data Description")

description_df = pd.DataFrame({
    "Column Name": [
        "Unique ID",
        "Indicator ID",
        "Name",
        "Measure",
        "Measure Info",
        "Geo Type Name",
        "Geo Join ID",
        "Geo Place Name",
        "Time Period",
        "Start_Date",
        "Data Value",
        "Message"
    ],

    "Description": [
        "A unique identifier for each record.",
        "An identifier for the air quality indicator.",
        "The name of the air quality indicator, such as PM2.5, NO2, or Ozone.",
        "The type of measurement used for the indicator.",
        "The unit or measurement information associated with the value.",
        "The geographic level of the measurement, such as Borough, Citywide, CD, UHF34, or UHF42.",
        "An identifier for the geographic area.",
        "The name of the geographic area where the measurement was recorded.",
        "The time period covered by the measurement.",
        "The starting date of the measurement period.",
        "The recorded value of the air quality indicator.",
        "Additional message or information associated with the record."
    ]
})

st.dataframe(
    description_df,
    use_container_width=True,
    height=400
)