import streamlit as st
import pandas as pd


def run():
    st.header('Summary and Key Takeaways')

    # Define the comparison table data
    data = {
        "Clustering Algorithm": [
            "K-Means", "K-Means++", "Agglomerative (Hierarchical)", 
            "Divisive (Hierarchical)", "DBSCAN", "Fuzzy C-Means", 
            "Gaussian Mixture Model (GMM)", "Weighted K-Means"
        ],
        "Type": [
            "Hard", "Hard", "Hard", "Hard", "Density-Based", "Soft", "Soft", "Hard"
        ],
        "Cluster Shape": [
            "Spherical", "Spherical", "Arbitrary", "Arbitrary", 
            "Arbitrary", "Arbitrary", "Elliptical", "Spherical"
        ],
        "Scalability": [
            "Fast (O(n))", "Fast (O(n))", "Moderate (O(n²))", 
            "Slow (O(n³))", "Moderate (O(n log n))", 
            "Moderate (O(n²))", "Moderate (O(n³))", "Fast (O(n))"
        ],
        "Distance Metric": [
            "Euclidean", "Euclidean", "Euclidean or others", 
            "Euclidean or others", "Euclidean", "Euclidean", 
            "Gaussian distribution", "Euclidean"
        ],
        "Parameter Sensitivity": [
            "Sensitive to K value", "Sensitive to K value", 
            "None (Automatic clustering)", "None (Automatic clustering)", 
            "Sensitive to eps and minPts", "Sensitive to fuzziness parameter", 
            "Sensitive to K and covariance structure", "Sensitive to K value"
        ],
        "Handling Noise": [
            "Poor", "Poor", "Good", "Good", "Good", 
            "Good", "Poor", "Poor"
        ],
        "Example Use Cases": [
            "Image Compression, Market Segmentation", 
            "Similar to K-Means but with better initialization", 
            "Gene Expression, Document Clustering", 
            "Text clustering, customer segmentation", 
            "Anomaly Detection, Spatial Data Analysis", 
            "Image Segmentation, Medical Imaging", 
            "Speech Recognition, Anomaly Detection", 
            "Weighted clustering in financial applications"
        ],
        "Advantages": [
            "Simple, Fast, Easy to understand", 
            "Improved initialization, better results", 
            "Produces a dendrogram, no need to predefine K", 
            "Detailed hierarchical structure, no need to predefine K", 
            "Identifies noise, no need to predefine K", 
            "Handles soft boundaries, flexible", 
            "Probabilistic assignment, handles overlapping clusters", 
            "Accounts for sample importance in clustering"
        ],
        "Disadvantages": [
            "Sensitive to initial centroids, outliers", 
            "Still sensitive to K value, not good with outliers", 
            "Computationally expensive for large data", 
            "Computationally expensive, slow", 
            "Struggles with varying densities, needs parameter tuning", 
            "Computationally expensive, sensitive to initialization", 
            "Requires assumptions on distribution, computationally expensive", 
            "Sensitive to K value, not robust to outliers"
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Streamlit app
    st.write(
        """
        Below is a detailed comparison of popular clustering algorithms. 
        You can scroll horizontally to view all columns.
        """
    )
    st.dataframe(df)

    st.write("""
        Clustering is essential for understanding data patterns and discovering structures. It’s widely used in applications 
        like customer segmentation, anomaly detection, and more. Choosing the right algorithm depends on the nature of the 
        data and the problem at hand.
    """)