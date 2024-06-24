import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def box_plot(data):
    # Set the aesthetics for the plot
    sns.set_theme(style="whitegrid")  # Sets the style of the plot to include gridlines

    # Sidebar controls for interactivity
    st.sidebar.header('Box Plot Settings')
    column = st.sidebar.selectbox("Choose the column for box plot", data.select_dtypes(include=[np.number]).columns.tolist())

    # Display the box plot
    st.markdown(f"""<div style='text-align: center;'>
                <strong style='font-size: 18px; color: darkblue;'>Detailed Box Plot for {column}</strong></div>""",
                unsafe_allow_html=True)

    fig, ax = plt.subplots()
    # Creating the box plot with Seaborn
    sns.boxplot(x=data[column], color="lightgray", showfliers=True, flierprops={'marker':'o', 'markerfacecolor':'red', 'markeredgecolor':'black', 'label':'Outliers'})

    # Getting the resulting whiskers from seaborn (new method using artists)
    whiskers = [artist.get_xdata() for artist in ax.lines if len(artist.get_xdata()) == 2]
    whisker_low, whisker_high = whiskers[0][1], whiskers[1][1]  # Assuming Seaborn returns them in order

    # Highlighting the median and quartiles
    median = data[column].median()
    quartile1 = data[column].quantile(0.25)
    quartile3 = data[column].quantile(0.75)

    # Adding lines for median, quartiles, and whiskers
    ax.axvline(median, color='magenta', label='Median', linestyle='--')
    ax.axvline(quartile1, color='cyan', label='1st Quartile', linestyle=':')
    ax.axvline(quartile3, color='blue', label='3rd Quartile', linestyle=':')
    ax.axvline(whisker_low, color='orange', label='Lower Whisker', linestyle='-.')
    ax.axvline(whisker_high, color='green', label='Upper Whisker', linestyle='-.')

    # Moving the legend to the right of the plot
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Labels
    ax.set_xlabel(column, fontsize=14)
    ax.set_ylabel("Value", fontsize=14)
    st.pyplot(fig)