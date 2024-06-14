import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
st.cache_data   # This decorator helps cache the data loading for speed and efficiency
def load_data():
    data = pd.read_csv('./data/abalone.csv')
    return data

data = load_data()

# Sidebar controls for interactivity
column = st.sidebar.selectbox("Choose the column for histogram", data.select_dtypes(include=[np.number]).columns.tolist())
bins = st.sidebar.slider("Select number of bins", min_value=10, max_value=100, value=30)

# Create the histogram using seaborn for better aesthetics and functionality
st.write(f"Histogram for {column}")
fig, ax = plt.subplots()
sns.histplot(data[column].dropna(), bins=bins, kde=False, ax=ax, color='blue')  # Use seaborn's histplot
st.pyplot(fig)
