# Air Quality Data and Analysis

## Project Overview

This project focuses on exploring, cleaning, analyzing, and visualizing a real-world air quality dataset.

The project follows a data science workflow that includes:

* Data Understanding
* Data Exploration
* Data Cleaning
* Feature Engineering
* Data Analysis
* Deployment using Streamlit

## Dataset

The dataset contains air quality measurements across different geographic areas and time periods.

The main variables include:

* Air quality indicator
* Measurement type
* Measurement unit
* Geographic type
* Geographic area
* Time period
* Start date
* Data value

## Data Cleaning

The dataset was examined for:

* Missing values
* Duplicate records
* Duplicate IDs
* Data types
* Inconsistent measurement units
* Unnecessary columns

The cleaned dataset was saved as:

`Air_Quality_Cleaned.parquet`

## Data Analysis

The analysis investigates questions related to:

* PM2.5 values across different geographic types
* Changes in PM2.5 over time
* Differences between Summer, Winter, and Annual periods
* Variability of PM2.5 across geographic types
* The relationship between geographic type and period type
* PM2.5 trends across geographic types over time

## Technologies Used

* Python 3.12.13
* Pandas
* NumPy
* Plotly
* PyArrow
* Streamlit
* Jupyter Notebook

## Streamlit Application

The project includes an interactive Streamlit application with three pages:

1. **Home**
2. **Data Explorer**
3. **Analysis**

### Home

Provides an overview of the project and dataset.

### Data Explorer

Allows users to explore numerical and categorical variables through statistical summaries and interactive visualizations.

### Analysis

Presents the main analytical questions, results, and visualizations developed during the project.

## How to Run the Application

Install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the Streamlit application:

```bash
streamlit run home.py
```

## Project Structure

```text
PROJECT
│
├── Air_Quality.csv
├── Air_Quality_Cleaned.parquet
├── Air_Quality.ipynb
├── home.py
├── requirements.txt
├── README.md
│
└── pages
    ├── Analysis.py
    └── Data Explorer.py
```

## Author

Prepared by: Farid Ahmed Ebrahim
