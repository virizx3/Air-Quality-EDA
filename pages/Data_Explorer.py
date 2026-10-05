import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Explorer", layout="wide")
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

st.subheader("Data Explorer")


# Numerical Columns
numerical_columns = df.select_dtypes(
    include="number"
).columns.tolist()

# Remove ID columns from numerical selection
numerical_columns = [
    col for col in numerical_columns
    if col not in ["Unique ID", "Indicator ID", "Geo Join ID"]
]


# Categorical Columns
categorical_columns = df.select_dtypes(
    include=["object", "string", "category"]
).columns.tolist()

# Remove non-analytical columns
categorical_columns = [
    col for col in categorical_columns
    if col not in ["Unique ID", "Indicator ID", "Geo Join ID"]
]


# Selection Boxes
col1, col2 = st.columns(2)

with col1:
    selected_numerical = st.selectbox(
        "Select Numerical Column",
        numerical_columns
    )

with col2:
    selected_categorical = st.selectbox(
        "Select Categorical Column",
        categorical_columns
    )


# --------------------------------------------------
# Numerical Analysis
# --------------------------------------------------

st.subheader("Numerical Analysis")

col1, col2 = st.columns(2)

with col1:

    st.write("Statistical Summary")

    st.dataframe(
        df[selected_numerical].describe().to_frame(),
        use_container_width=True
    )

with col2:

    fig_num = px.histogram(
        df,
        x=selected_numerical,
        title=f"Distribution of {selected_numerical}",
        nbins=30
    )

    st.plotly_chart(
        fig_num,
        use_container_width=True
    )


# --------------------------------------------------
# Categorical Analysis
# --------------------------------------------------

st.subheader("Categorical Analysis")

categorical_summary = (
    df[selected_categorical]
    .value_counts()
    .reset_index()
)

categorical_summary.columns = [
    selected_categorical,
    "Count"
]

col1, col2 = st.columns(2)

with col1:

    st.dataframe(
        categorical_summary,
        use_container_width=True
    )

with col2:

    fig_cat = px.bar(
        categorical_summary,
        x=selected_categorical,
        y="Count",
        title=f"Distribution of {selected_categorical}"
    )

    st.plotly_chart(
        fig_cat,
        use_container_width=True
    )