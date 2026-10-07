import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analysis", layout="wide")
st.image(
    r"C:\Users\techno\Desktop\MIDTERM\air quality.jpg",
    use_container_width=True
)

html= st.markdown("""
<div style="text-align: center; color: blue;">
   Air Quality Data and Analysis project 
</div>
""", unsafe_allow_html=True)
st.markdown("**Prepared by: Farid Ahmed Ebrahim**")

#load the data

df = pd.read_parquet("Air_Quality_Cleaned.parquet")

df["Start_Date"] = pd.to_datetime(df["Start_Date"])

df["Start Year"] = df["Start_Date"].dt.year

df["Period Type"] = df["Time Period"].apply(
    lambda x:
        "Summer" if x.startswith("Summer")
        else "Winter" if x.startswith("Winter")
        else "Annual" if x.startswith("Annual")
        else "Year/Range"
)

st.subheader("Data Analysis")
# Data Analysis Questions

# Question 1
# --------------------------------------------------

st.header("Question 1: How do PM2.5 values vary across different geographic types?")

pm25 = df[df["Name"] == "Fine particles (PM 2.5)"]

q1 = pm25.groupby("Geo Type Name")["Data Value"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

st.dataframe(q1, use_container_width="stretch")

fig1 = px.box(
    pm25,
    x="Geo Type Name",
    y="Data Value",
    title="PM2.5 Values by Geographic Type"
)

st.plotly_chart(fig1, use_container_width=True)


# Question 2
# --------------------------------------------------

st.header("Question 2: How do PM2.5 values change over time?")

q2 = pm25.groupby("Start Year")["Data Value"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

st.dataframe(q2, use_container_width=True)

year_avg = pm25.groupby(
    "Start Year",
    as_index=False
)["Data Value"].mean()

fig2 = px.line(
    year_avg,
    x="Start Year",
    y="Data Value",
    markers=True,
    title="Average PM2.5 Values Over Time"
)

fig2.update_layout(
    xaxis_title="Start Year",
    yaxis_title="Average PM2.5"
)

st.plotly_chart(fig2, use_container_width=True)


# Question 3
# --------------------------------------------------

st.header("Question 3: How do PM2.5 values vary by period type?")

q3 = pm25.groupby("Period Type")["Data Value"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

st.dataframe(q3, use_container_width=True)

fig3 = px.box(
    pm25,
    x="Period Type",
    y="Data Value",
    title="PM2.5 Values by Period Type"
)

st.plotly_chart(fig3, use_container_width=True)


# 
# Question 4
# --------------------------------------------------

st.header("Question 4: Which geographic type shows the highest variability in PM2.5?")

q4 = pm25.groupby("Geo Type Name")["Data Value"].agg(
    ["count", "mean", "std", "min", "max"]
).round(2)

st.dataframe(q4, use_container_width=True)

fig4 = px.bar(
    q4.reset_index(),
    x="Geo Type Name",
    y="std",
    title="PM2.5 Variability by Geographic Type",
    labels={"std": "Standard Deviation"}
)

st.plotly_chart(fig4, use_container_width=True)


# 
# Question 5
# --------------------------------------------------

st.header(
    "Question 5: How does PM2.5 vary across geographic types and period types?"
)

q5 = pm25.groupby(
    ["Geo Type Name", "Period Type"]
)["Data Value"].mean().round(2).unstack()

st.dataframe(q5, use_container_width=True)

summary = pm25.groupby(
    ["Geo Type Name", "Period Type"],
    as_index=False
)["Data Value"].mean()

fig5 = px.bar(
    summary,
    x="Geo Type Name",
    y="Data Value",
    color="Period Type",
    barmode="group",
    title="Average PM2.5 by Geographic and Period Type"
)

st.plotly_chart(fig5, use_container_width=True)


# 
# Question 6
# --------------------------------------------------

st.header(
    "Question 6: How does the average PM2.5 level vary across geographic types over time?"
)

pm25_year_geo = pm25.groupby(
    ["Start Year", "Geo Type Name"],
    as_index=False
)["Data Value"].mean()

fig6 = px.line(
    pm25_year_geo,
    x="Start Year",
    y="Data Value",
    color="Geo Type Name",
    markers=True,
    title="Average PM2.5 by Geographic Type Over Time"
)

fig6.update_layout(
    xaxis_title="Start Year",
    yaxis_title="Average PM2.5"
)

st.plotly_chart(fig6, use_container_width=True)