import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# Set the aesthetics for the plot
sns.set_theme(style="whitegrid")  # Sets the style of the plot to include gridlines

# Decorator for caching data loading
@st.cache_data
def load_data():
    return pd.read_csv('./data/abalone.csv')

data = load_data()

# Sidebar controls for interactivity
st.sidebar.header('Histogram Settings')
column = st.sidebar.selectbox("Choose the column for histogram", data.select_dtypes(include=[np.number]).columns.tolist())
bins = st.sidebar.slider("Select number of bins", min_value=10, max_value=100, value=30)
kde = st.sidebar.checkbox("Show KDE", value=False)  # Adds an option to toggle KDE
color = st.sidebar.color_picker("Pick a color", '#0000ff')  # Allows users to pick a histogram color

# Create the histogram using seaborn for better aesthetics and functionality
st.markdown(f"""<div style='text-align: center;'>
            <strong style='font-size: 18px; color: darkblue;'>Histogram for {column} with {bins} bins</strong></div>""", 
            unsafe_allow_html=True)

fig, ax = plt.subplots()
sns.histplot(data[column].dropna(), bins=bins, kde=kde, ax=ax, color=color)  # Use chosen color and KDE toggle
ax.set_xlabel(column, fontsize=14)  # Set x-label with custom font size
ax.set_ylabel("Frequency", fontsize=14)  # Set y-label with custom font size
st.pyplot(fig)


# Utilize columns or expander for better layout management
with st.expander("See Explanation"):
    st.markdown(f"""
        This histogram represents the distribution of the column **{column}** from the Abalone dataset.
        
        Use the sidebar controls to change the parameters and customize the visualization.
    """, unsafe_allow_html=True)
