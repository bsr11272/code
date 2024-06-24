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
                <strong style='font-size: 18px; color: darkblue;'>Box Plot for column: {column}</strong></div>""",
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
    st.pyplot(fig)
    
    # Provide code example
    st.markdown("""
        ### Python Code for Creating a Box Plot
        ```python
        import seaborn as sns
        import matplotlib.pyplot as plt
        import pandas as pd

        # Load your data
        data = pd.read_csv('your_data.csv')

        # Create the box plot
        sns.set(style="whitegrid")
        fig, ax = plt.subplots()
        sns.boxplot(x=data['your_column'])
        ax.set_xlabel('Your Column')
        ax.set_ylabel('Value')
        plt.show()
        ```
        """, unsafe_allow_html=True)

    # Utilize an expander for further explanation
    with st.expander("See Explanation"):
        st.markdown("""
            ### Detailed Explanation of the Box Plot Code

            **1. Importing Libraries:**
            - `import seaborn as sns`: Imports Seaborn, a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
            - `import matplotlib.pyplot as plt`: Imports Matplotlib's pyplot, a module that provides a MATLAB-like interface. It is used here for creating figures and axes.
            - `import pandas as pd`: Imports Pandas, which is used for data manipulation and analysis, and here it is primarily used to load and handle the dataset.

            **2. Loading Data:**
            - `data = pd.read_csv('your_data.csv')`: Loads data from a CSV file into a Pandas DataFrame. This line assumes that your data is in the same directory as your script or specifies the path to where your data resides.

            **3. Creating the Box Plot:**
            - `sns.set(style="whitegrid")`: Sets the aesthetic style of the plots. This style is suitable for plots with heavy data elements and to highlight outliers.
            - `fig, ax = plt.subplots()`: Creates a figure and a set of subplots. This is where our plot will actually be drawn.
            - `sns.boxplot(x=data['your_column'])`: Creates a box plot for 'your_column' from the dataset.
            - `ax.set_xlabel('Your Column')`: Sets the label for the x-axis.
            - `ax.set_ylabel('Value')`: Sets the label for the y-axis.
            - `plt.show()`: Displays the plot.

            Box plots are very useful for showing the distribution of data through their quartiles and for spotting outliers.
        """, unsafe_allow_html=True)