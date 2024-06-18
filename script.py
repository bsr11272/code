import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Set the aesthetics for the plot
sns.set_theme(style="whitegrid")  # Sets the style of the plot to include gridlines


# Set the page config and theme at the very start of your script
st.set_page_config(
    page_title="Histogram Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
    theme={"base": "light"}  # Setting the theme to light
)

# Decorator for caching data loading
@st.cache_data
def load_data():
    return pd.read_csv('./data/abalone.csv')

data = load_data()

# Sidebar controls for interactivity
st.sidebar.header('Histogram Settings')
column = st.sidebar.selectbox("Choose the column for histogram", data.select_dtypes(include=[np.number]).columns.tolist())
bins = st.sidebar.slider("Select number of bins", min_value=10, max_value=1000, value=30)
kde = st.sidebar.checkbox("Show KDE", value=False)  # Adds an option to toggle KDE
color = st.sidebar.color_picker("Pick a color", '#0000ff')  # Allows users to pick a histogram color

# Display the histogram
st.markdown(f"""<div style='text-align: center;'>
            <strong style='font-size: 18px; color: darkblue;'>Histogram for {column} with {bins} bins</strong></div>""", 
            unsafe_allow_html=True)

fig, ax = plt.subplots()
sns.histplot(data[column].dropna(), bins=bins, kde=kde, ax=ax, color=color)  # Use chosen color and KDE toggle
ax.set_xlabel(column, fontsize=14)  # Set x-label with custom font size
ax.set_ylabel("Frequency", fontsize=14)  # Set y-label with custom font size
st.pyplot(fig)

# Provide code example
st.markdown("""
    ### Python Code for Creating a Histogram
    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # Load your data
    data = pd.read_csv('your_data.csv')

    # Create the histogram
    sns.set(style="whitegrid")
    fig, ax = plt.subplots()
    sns.histplot(data['your_column'], bins=30, kde=False, ax=ax, color='blue')
    ax.set_xlabel('Your Column')
    ax.set_ylabel('Frequency')
    plt.show()
    ```
    """, unsafe_allow_html=True)

# Utilize an expander for further explanation
with st.expander("See Explanation"):
    st.markdown("""
        ### Detailed Explanation of the Histogram Code

        **1. Importing Libraries:**
        - `import seaborn as sns`: Imports Seaborn, a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
        - `import matplotlib.pyplot as plt`: Imports Matplotlib's pyplot, a collection of functions that make Matplotlib work like MATLAB, which is used here primarily for creating figures and axes.
        - `import pandas as pd`: Imports Pandas, which is used for data manipulation and analysis. Here, it's primarily used to load and handle the dataset.

        **2. Loading Data:**
        - `data = pd.read_csv('your_data.csv')`: Loads data from a CSV file into a Pandas DataFrame. This line assumes that your data is in the same directory as your script or specifies the path to where your data resides.

        **3. Creating the Histogram:**
        - `sns.set(style="whitegrid")`: Sets the aesthetic style of the plots. In this case, we're using "whitegrid" which is suitable for plots with heavy data elements.
        - `fig, ax = plt.subplots()`: Creates a figure and a set of subplots. This is where our plot will actually be drawn.
        - `sns.histplot(data['your_column'], bins=30, kde=False, ax=ax, color='blue')`: Creates a histogram for 'your_column' from the dataset. The number of bins is set to 30, KDE (Kernel Density Estimation) is turned off, and the plot color is set to blue.
        - `ax.set_xlabel('Your Column')`: Sets the label for the x-axis.
        - `ax.set_ylabel('Frequency')`: Sets the label for the y-axis.
        - `plt.show()`: Displays the plot.

        This code snippet shows how to generate a basic histogram, which is useful for understanding the distribution of data points across a single variable.
    """, unsafe_allow_html=True)

