import streamlit as st
import pandas as pd

from charts.Histogram_plot import histogram
from charts.Box_plot import box_plot

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('./data/abalone.csv')

data = load_data()

# Access the current query parameters
params = st.query_params  # No parentheses needed, accessed as a property
chart_type = params.get('chart', 'Histogram')  # Get the 'chart' parameter, default to 'Histogram'

# Define functions for each chart type
def show_histogram():
    histogram(data)

def show_box_plot():
    box_plot(data)
# Map chart types to functions
chart_functions = {
    'Histogram': show_histogram,
    'Box_Plot': show_box_plot,
}

# Display the appropriate chart based on URL parameter
if chart_type in chart_functions:
    chart_functions[chart_type]()
else:
    st.error("Chart type not supported! Please check the URL parameters.")

