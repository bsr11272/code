import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def box_plot(data):
    
    # Set the aesthetics for the plot
    sns.set_theme(style="whitegrid")  # Sets the style of the plot to include gridlines

    
    column = st.selectbox("Choose the column for box plot", data.select_dtypes(include=[np.number]).columns.tolist())
    
    fig, ax = plt.subplots()
    sns.boxplot(x=data[column])
    ax.set_xlabel(column)
    ax.set_ylabel("Value")
    st.pyplot(fig)
