import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import seaborn as sns


def run():
    # App title
    st.title("Cluster Analysis: Step-by-Step Guide")
    st.write(
        "Cluster analysis is a key unsupervised machine learning technique for grouping data points based on similarity. "
        "Let's explore the complete process of cluster analysis, from data preparation to visualization and evaluation."
    )

    # 1. Define the Problem and Objectives
    with st.expander("1. Define the Problem and Objectives", expanded=True):
        st.subheader("Define the Problem")
        st.write(
            "- **Purpose:** Are you segmenting customers, identifying patterns, or clustering items?"
            "\n- **Variables:** Select features that capture relevant patterns for your objectives."
        )
    
    # 2. Data Collection and Preprocessing
    with st.expander("2. Data Collection and Preprocessing", expanded=True):
        st.subheader("Synthetic Data Generation")

        st.write(
                "Gather data from your sources (e.g., database, CSV files)."
                "Clean the data by handling missing values, outliers, or duplicates."
                "Standardize or normalize the data if needed (e.g., scaling features to a similar range), as many clustering algorithms are sensitive to feature scaling.")

        st.write("For this Analysis, we're generating a synthetic dataset using make_blobs with predefined clusters. "
                 "This will help us illustrate the clustering process clearly and effectively.")

        # Generate data
        X, y_true = make_blobs(n_samples=300, centers=4, n_features=2, cluster_std=1.0, random_state=42)
        data = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
        st.write("Sample Data:")
        st.write(data.head())

    # 3. Determine Optimal Number of Clusters
    with st.expander("3. Determine Optimal Number of Clusters", expanded=True):

        st.subheader("Determining Optimal Number of Clusters")

        st.write("- **Elbow Method:** Plot within-cluster variance against the number of clusters to find an **elbow**, suggesting a suitable number.")
        st.write("- **Silhouette Score:** Measures how well each point fits into its cluster. A higher score suggests better-defined clusters.")
        st.write("- **Gap Statistics, AIC/BIC:** Advanced techniques that estimate the optimal number of clusters based on model complexity.")
        st.write("")
        st.write(
            "To decide on the optimal number of clusters, we use the Elbow Method, which shows how the within-cluster sum of squares(SSE) changes as we increase the number of clusters. We look for the 'elbow point,' where adding more clusters does not significantly decrease the SSE."
        )

        # Elbow Method
        sse = []
        k_range = range(1, 10)
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)
            sse.append(kmeans.inertia_)
        
        # Plot Elbow Curve
        fig, ax = plt.subplots()
        ax.plot(k_range, sse, marker="o", color="b")
        ax.set_title("Elbow Method")
        ax.set_xlabel("Number of Clusters")
        ax.set_ylabel("SSE")
        st.pyplot(fig)

    # 4. Apply Clustering Algorithm
    with st.expander("4. Apply Clustering Algorithm", expanded=True):

        st.subheader("Select the Clustering Algorithm")

        st.write(
                "Based on the nature of your data and problem, choose an appropriate clustering technique:"
                "\n- **K-Means:** Efficient for large datasets, assuming clusters are spherical and balanced."
                "\n- **Hierarchical Clustering:** Builds a hierarchy of clusters, good for smaller datasets and identifying nested clusters."
                "\n- **DBSCAN:** Suitable for data with noise and non-spherical clusters.")

        optimal_clusters = 4
        kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
        data["Cluster"] = kmeans.fit_predict(X)
        st.write("")
        st.write(
            f"We apply K-Means clustering with the optimal number of clusters set to {optimal_clusters}.")
        st.write(f"Silhouette Score: {silhouette_score(X, data['Cluster']):.2f}")

    # 5. Visualize Clusters
    with st.expander("5. Visualize Clusters", expanded=True):
        st.subheader("Cluster Visualization")
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x="Feature 1", y="Feature 2", hue="Cluster", palette="viridis", ax=ax)
        ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c="red", marker="X", label="Centroids")
        ax.set_title("Cluster Visualization")
        st.pyplot(fig)

    # 6. Cluster Analysis
    with st.expander("6. Cluster Analysis", expanded=True):
        st.subheader("Analyze Cluster Characteristics")
        # cluster_summary = data.groupby("Cluster").mean()
        # st.write("Cluster Summary:")
        # st.write(cluster_summary)
        
        st.write(
            "We now analyze each cluster by examining the mean values of each feature. "
            "This helps us understand the characteristics of each cluster and draw insights based on the features."
        )

        # Display mean values for each feature by cluster
        cluster_summary = data.groupby("Cluster").mean()
        st.write("Cluster Summary Statistics:")
        st.write(cluster_summary)

        # Distribution of points in each cluster
        cluster_counts = data["Cluster"].value_counts().sort_index()
        fig, ax = plt.subplots()
        sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette="viridis", ax=ax)
        ax.set_title("Number of Points in Each Cluster")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("Number of Points")
        st.pyplot(fig)

        st.write("Alternative Analysis Techniques:")
        st.write("- **Principal Component Analysis (PCA)**: Use PCA to reduce dimensionality before clustering for better visualization.")
        st.write("- **Feature Importance Analysis**: Identify which features contribute most to clustering decisions.")


    # 7. Silhouette Analysis
    with st.expander("7. Silhouette Analysis for Cluster Quality ", expanded=True):
        # st.subheader("Silhouette Analysis")
                # Step 6: Silhouette Analysis for Cluster Quality
        st.subheader("Silhouette Analysis")
        st.write(
            "Silhouette analysis measures how well-separated each cluster is from others. "
            "A silhouette score closer to 1 indicates that the sample is well-matched to its own cluster, "
            "while a score close to -1 indicates a possible mismatch."
        )
        silhouette_vals = silhouette_samples(X, data["Cluster"])
        data["Silhouette"] = silhouette_vals
        fig, ax = plt.subplots()
        sns.boxplot(x="Cluster", y="Silhouette", data=data, palette="viridis", ax=ax)
        ax.set_title("Silhouette Scores")
        st.pyplot(fig)


    # Conclusion
    st.header("Summary")
    st.write("In this analysis, we applied K-Means clustering to understand and segment data into distinct groups. To determine the ideal number of clusters, we used approaches such as the Elbow Method and Silhouette Scores, providing quantitative insights into the clustering structure. The resulting clusters were visualized and analyzed to highlight their unique characteristics, demonstrating how these techniques can reveal underlying patterns and structures in various datasets. This foundational approach to cluster analysis serves as a versatile tool for uncovering meaningful insights in diverse applications."
    )
# Run the Streamlit app
if __name__ == "__main__":
    run()
