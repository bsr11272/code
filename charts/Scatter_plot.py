import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def scatter_plot(data):
    # Set the aesthetics for the plot
    sns.set_theme(style="whitegrid")  # Sets the style of the plot to include gridlines

    # Sidebar controls for interactivity
    st.sidebar.header('Scatter Plot Settings')
    x_column = st.sidebar.selectbox("Choose the X-axis column", data.select_dtypes(include=[np.number]).columns.tolist())
    y_column = st.sidebar.selectbox("Choose the Y-axis column", data.select_dtypes(include=[np.number]).columns.tolist(), index=1 if len(data.select_dtypes(include=[np.number]).columns) > 1 else 0)
    
    # Display the scatter plot
    st.markdown(f"""<div style='text-align: center;'>
                <strong style='font-size: 18px; color: darkblue;'>Scatter Plot for {x_column} vs {y_column}</strong></div>""",
                unsafe_allow_html=True)

    fig, ax = plt.subplots()
    sns.scatterplot(x=data[x_column], y=data[y_column], hue=data['Sex'], ax=ax)

    # Labels and legend
    ax.set_xlabel(x_column, fontsize=14)
    ax.set_ylabel(y_column, fontsize=14)
    ax.legend(title='Sex')
    st.pyplot(fig)

    # Provide code example and explanations
    st.markdown("""
        ### Python Code for Creating a Scatter Plot with Gender Hue
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd

        data = pd.read_csv('your_data.csv')
        sns.set(style="whitegrid")
        fig, ax = plt.subplots()
        sns.scatterplot(x=data['x_column'], y=data['y_column'], hue=data['Gender'], palette='viridis', ax=ax)
        plt.show()
        ```
        """, unsafe_allow_html=True)

    # Utilize an expander for further explanation
    with st.expander("See Explanation"):
        st.markdown("""
            ### Detailed Explanation of the Scatter Plot Code

            **1. Importing Libraries:**
            - `import seaborn as sns`: Imports Seaborn, a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
            - `import matplotlib.pyplot as plt`: Imports Matplotlib's pyplot, a collection of functions that make Matplotlib work like MATLAB, which is used here primarily for creating figures and axes.
            - `import pandas as pd`: Imports Pandas, which is used for data manipulation and analysis. Here, it's primarily used to load and handle the dataset.

            **2. Setting Plot Aesthetics:**
            - `sns.set(style="whitegrid")`: Sets the aesthetic style of the plots. This style is suitable for plots that need to highlight data clarity and precision.

            **3. Creating the Scatter Plot:**
            - `fig, ax = plt.subplots()`: Creates a figure and a set of subplots.
            - `sns.scatterplot(...)`: Creates a scatter plot for the specified 'x_column' and 'y_column'. The 'hue' parameter allows for color coding based on the 'Sex' category, enhancing the visual distinction between different groups.
            - `plt.show()`: Displays the plot.

            This scatter plot helps to visualize the relationship between two variables while categorizing data points based on gender, facilitating an easy comparison across different genders.
        """, unsafe_allow_html=True)
