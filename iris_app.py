import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris(as_frame=True)
df = iris['frame']
df['species'] = df['target'].replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # Map target values to species names

# Streamlit App Interface
st.set_page_config(page_title="Iris Dataset Explorer", layout="wide")

# Header and Introduction
st.title('🌸 Iris Dataset Explorer')
st.markdown(
    """
    This app allows you to explore the famous **Iris dataset**. 
    Use the sidebar to filter and visualize different features of the dataset.
    """
)

# Sidebar: Inputs for filtering and controlling the data
st.sidebar.header('🔎 Filter Parameters')

# Select species with a default value for all species
selected_species = st.sidebar.multiselect(
    'Select Species',
    df['species'].unique(),
    default=df['species'].unique(),
    help="Filter data by Iris species."
)

# Slider for Sepal Length Range
sepal_length_range = st.sidebar.slider(
    'Sepal Length Range (cm)',
    min_value=float(df['sepal length (cm)'].min()), 
    max_value=float(df['sepal length (cm)'].max()), 
    value=(df['sepal length (cm)'].min(), df['sepal length (cm)'].max()),
    step=0.1,
    help="Select a range of Sepal Length."
)

# Slider for Petal Length Range
petal_length_range = st.sidebar.slider(
    'Petal Length Range (cm)',
    min_value=float(df['petal length (cm)'].min()), 
    max_value=float(df['petal length (cm)'].max()), 
    value=(df['petal length (cm)'].min(), df['petal length (cm)'].max()),
    step=0.1,
    help="Select a range of Petal Length."
)

# Filter the DataFrame based on user inputs
filtered_df = df[
    (df['species'].isin(selected_species)) &
    (df['sepal length (cm)'] >= sepal_length_range[0]) &
    (df['sepal length (cm)'] <= sepal_length_range[1]) &
    (df['petal length (cm)'] >= petal_length_range[0]) &
    (df['petal length (cm)'] <= petal_length_range[1])
]

# Layout: Define two columns for better presentation of graphs
col1, col2 = st.columns(2)

# Column 1: Scatter plot of Sepal Length vs Petal Length
with col1:
    st.subheader('🔷 Sepal Length vs Petal Length')
    fig, ax = plt.subplots()
    for species in selected_species:
        species_data = filtered_df[filtered_df['species'] == species]
        ax.scatter(
            species_data['sepal length (cm)'], 
            species_data['petal length (cm)'], 
            label=species, alpha=0.8, s=80
        )
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Petal Length (cm)')
    ax.set_title('Scatter Plot of Sepal vs Petal Length')
    ax.legend(title="Species")
    st.pyplot(fig)

# Column 2: Plotly histogram for Sepal Width Distribution
with col2:
    st.subheader('📊 Sepal Width Distribution')
    fig_hist_sepal = px.histogram(
        filtered_df, x='sepal width (cm)', 
        color='species', 
        title='Distribution of Sepal Width by Species',
        nbins=20,
        template='plotly_white',
        marginal="box"  # Show marginal box plot to the side
    )
    st.plotly_chart(fig_hist_sepal)

# Full-width plot: Plotly histogram for Petal Width Distribution
st.subheader('📊 Petal Width Distribution')
fig_hist_petal = px.histogram(
    filtered_df, x='petal width (cm)', 
    color='species', 
    title='Distribution of Petal Width by Species',
    nbins=20,
    template='plotly_white',
    marginal="box"
)
st.plotly_chart(fig_hist_petal, use_container_width=True)

# Display filtered data in an expandable section
with st.expander("🔍 View Filtered Data"):
    st.write(filtered_df)

# Footer with a brief description
st.markdown(
    """
    **About this dataset**: The Iris dataset is a classic dataset used in data science and machine learning, 
    containing 150 samples of three species of Iris flowers (setosa, versicolor, and virginica).
    """
)
