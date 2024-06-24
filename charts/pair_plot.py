import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def pair_plot(data):
    # Set the aesthetics for the plot
    sns.set(style="whitegrid")

    # Sidebar controls for selecting columns and hue
    st.sidebar.header('Enhanced Pair Plot Settings')
    
    # Selection of columns
    available_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    selected_columns = st.sidebar.multiselect("Select columns to include in the plot:", available_columns, default=available_columns[:min(3, len(available_columns))])

    # Selection of categories for hue
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_columns:
        hue_option = st.sidebar.selectbox("Choose the column for Hue (color)", categorical_columns)
        categories = data[hue_option].unique()
        active_categories = st.sidebar.multiselect(f"Select categories to display from selected column: {hue_option}", categories, default=categories)
    else:
        st.sidebar.error("No categorical columns available for hue!")
        return

    # Check if any columns and categories are selected to generate the plot
    if not selected_columns or not active_categories:
        st.warning("Please select at least one column and one category to display the plot.")
        return

    # Filter data based on active categories
    filtered_data = data[data[hue_option].isin(active_categories)]

    # Display the multivariate plot
    st.markdown(f"""<div style='text-align: center;'>
                <strong style='font-size: 18px; color: darkblue;'>Pair Plot with Columns: {', '.join(selected_columns)} and Categories: {', '.join(active_categories)}</strong></div>""",
                unsafe_allow_html=True)

    # Creating the pairplot
    pairplot_fig = sns.pairplot(filtered_data[selected_columns + [hue_option]], hue=hue_option, markers=["o", "s", "D"])

    # Show the plot
    st.pyplot(pairplot_fig.figure)

    # Provide code example and explanations
    st.markdown("""
        ### Python Code for Creating a Pair Plot
        ```python
        import seaborn as sns
        import pandas as pd

        data = pd.read_csv('your_data.csv')
        sns.set(style="whitegrid")
        sns.pairplot(data[['column1', 'column2', 'column3', 'Sex']], hue='Sex', palette='viridis')
        ```
        This multivariate plot (pairplot) visualizes pairwise relationships in the dataset across several dimensions (selected columns). Points are colored by the categorical column to differentiate data by categories, aiding in identifying patterns and correlations specific to each category.
        """, unsafe_allow_html=True)

    # Utilize an expander for further explanation
    with st.expander("See Explanation"):
        st.markdown("""
            ### Detailed Explanation of the Pair Plot Code

            **1. Importing Libraries:**
            - `import seaborn as sns`: Imports Seaborn, a library for making statistical graphics in Python. It builds on top of Matplotlib and integrates closely with pandas data structures.
            - `import pandas as pd`: Imports Pandas, which is crucial for data manipulation and analysis.

            **2. Loading Data:**
            - `data = pd.read_csv('your_data.csv')`: This command loads your data from a CSV file directly into a pandas DataFrame.

            **3. Setting Up the Plot:**
            - `sns.set(style="whitegrid")`: Sets the aesthetic style of the plots. Here, "whitegrid" is selected which applies a white background with grid lines which is useful for graphs that have potentially overlapping elements.
            - `sns.pairplot(data, hue='Sex', palette='viridis')`: Generates a matrix of plots showing the relationships between several pairs of variables in your DataFrame. The 'hue' parameter is used to color points by the 'Sex' column using a color palette called 'viridis'.

            **4. Plot Explanation:**
            - This type of plot is particularly useful for exploring correlations and relationships between numerical data points. By coloring data points with a categorical variable, it helps in understanding how relationships vary by group.

        """, unsafe_allow_html=True)



