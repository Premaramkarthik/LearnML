# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs

def run():

    # Page title
    st.title("Unsupervised Learning")


    # Introduction section
    st.info("""
    Imagine you're observing a crowd of people in a public place. You start noticing groups forming based on common traits, like families with kids or friends in similar attire, without anyone explicitly telling you who belongs together.
    Similarly, in unsupervised learning, a model analyzes data to discover hidden patterns or groups without labeled outcomes.
    """)


    # Explanation of Unsupervised Learning
    st.subheader("What is Unsupervised Learning?")
    st.write("""
    Unsupervised learning is a machine learning approach where models work with unlabeled data. The main objective is to identify patterns, structures, or relationships within data without predefined categories or outputs.
    """)


    # Types of Unsupervised Learning Problems
    st.subheader("Types of Unsupervised Learning Problems")
    st.write("The two primary types of unsupervised learning tasks are clustering and dimensionality reduction.")


    # Define a table to differentiate clustering and dimensionality reduction
    types_data = {
        'Type': ['Clustering', 'Dimensionality Reduction'],
        'Goal': [
            'Group similar data points together (e.g., customer segmentation)',
            'Reduce the number of features in data while retaining structure (e.g., data compression)'
        ],
        'Example': [
            'Market segmentation, social network analysis',
            'Principal Component Analysis (PCA), t-SNE for visualization'
        ]
    }
    types_df = pd.DataFrame(types_data)
    st.table(types_df)


    # Clustering Example
    st.subheader("Clustering Example: Customer Segmentation")
    st.write("""
    Consider a retail store with customer data. Using clustering, we can group customers based on similar buying patterns, which helps in creating targeted marketing strategies.
    """)


    # Create a synthetic dataset for clustering visualization
    X, y = make_blobs(n_samples=100, centers=3, random_state=42)
    fig, ax = plt.subplots()
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette="viridis", ax=ax)
    ax.set_title("Clustering: Grouping Data Points")
    st.pyplot(fig)


    # Dimensionality Reduction Example
    st.subheader("Dimensionality Reduction Example: Visualizing High-Dimensional Data")
    st.write("""
    Imagine a dataset with numerous features. Dimensionality reduction can project high-dimensional data onto a 2D or 3D space for easier visualization, revealing patterns that may not be apparent in the original dimensions.
    """)


    # Display a real-world table illustrating unsupervised learning in customer segmentation
    customer_data = {
        'Customer ID': [1, 2, 3, 4, 5],
        'Annual Income ($)': [40000, 60000, 80000, 120000, 200000],
        'Spending Score': [30, 60, 80, 95, 40],
        'Cluster': ['Low Spend', 'Medium Spend', 'High Spend', 'Premium', 'Low Spend']
    }
    customer_df = pd.DataFrame(customer_data)
    st.table(customer_df)


    # Advantages and Disadvantages of Unsupervised Learning
    st.subheader("Advantages of Unsupervised Learning")
    st.markdown("""
    - Allows for pattern discovery in unlabeled data
    - Useful for data compression and feature reduction
    - Can reveal hidden insights, aiding data exploration
    """)


    st.subheader("Disadvantages of Unsupervised Learning")
    st.markdown("""
    - Harder to evaluate due to lack of labeled data
    - May produce arbitrary groupings without clear interpretation
    - Can be computationally intensive, especially for high-dimensional data
    """)


    # Summary
    st.subheader("Summary")
    st.write("""
    Unsupervised learning enables models to find patterns and structures in unlabeled data, primarily used for clustering and dimensionality reduction. It is widely applicable for customer segmentation, anomaly detection, and visualization of complex datasets.
    However, its effectiveness heavily depends on the quality of the data and the chosen algorithms.
    """)


