import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

def parallel_coordinates_plot(data):
    st.sidebar.header('Parallel Coordinates Plot Settings')
    
    # Selecting numerical columns to include in the plot
    numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    selected_columns = st.sidebar.multiselect("Select numerical columns to include in the plot:", 
                                              numerical_columns, 
                                              default=numerical_columns[:min(4, len(numerical_columns))])

    # Selecting a categorical column for coloring (hue)
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    hue_option = st.sidebar.selectbox("Choose the column for Hue (color)", categorical_columns if categorical_columns else ['None'])

    if not selected_columns or hue_option == 'None':
        st.warning("Please select at least one numerical column and one hue option to display the plot.")
        return
    
    # Creating a color mapping for the categorical hue
    unique_categories = data[hue_option].unique()
    color_map = {cat: i for i, cat in enumerate(unique_categories)}
    data['color_mapped'] = data[hue_option].map(color_map)

    # Creating the parallel coordinates plot using Plotly Express
    fig = px.parallel_coordinates(data, 
                                  dimensions=selected_columns, 
                                  color='color_mapped',
                                  labels={col: col.replace('_', ' ').title() for col in selected_columns},
                                  color_continuous_scale=px.colors.diverging.Tealrose)

    # Adding a custom legend manually since Plotly doesn't support legends for parallel coordinates directly
    for cat in unique_categories:
        fig.add_trace(go.Scatter(
            x=[None], y=[None], mode='markers',
            marker=dict(size=10, color=px.colors.qualitative.Plotly[color_map[cat] % len(px.colors.qualitative.Plotly)]),
            legendgroup=cat,
            showlegend=True,
            name=cat
        ))

    # Display the plot
    st.plotly_chart(fig, use_container_width= True)

    # Providing the Python code for user reference
    st.markdown("""
        ### Python Code for Creating a Parallel Coordinates Plot
        ```python
        import pandas as pd
        import plotly.express as px

        # Load data
        data = pd.read_csv('your_data.csv')
        # Assume 'Sex' is the categorical column used for hue
        data['Sex_mapped'] = data['Sex'].astype('category').cat.codes

        fig = px.parallel_coordinates(data, dimensions=['Length', 'Diameter', 'Height', 'Whole weight'],
                                      color='Sex_mapped', color_continuous_scale=px.colors.diverging.Tealrose)
        fig.show()
        ```
        Detailed explanation: This plot visualizes relationships across selected numerical metrics colored by a categorical variable, which helps in understanding patterns across categories.
        """, unsafe_allow_html=True)

