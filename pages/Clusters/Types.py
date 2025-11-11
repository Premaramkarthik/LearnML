import streamlit as st

def run():
    st.header('**Types of Clusters**')
    
    st.info("""Clustering is an unsupervised learning technique used in machine learning and data analysis to group similar data points together. The aim of clustering is to find inherent structures or patterns within a dataset by organizing it into groups, where data points in the same group (or cluster) are more similar to each other than to those in other groups. There are various approaches to clustering, each suited for different kinds of data and problems. These approaches primarily differ based on how they define cluster membership and handle the assignment of data points. Broadly speaking, clustering algorithms can be classified into two main types:
    """)

    col1, spacer, col2 = st.columns([1, 0.05, 1])

    with col1:

        # Set up the main title and introductory overview
        st.title("Hard Clusters")
        st.image('pages/clusterImages/Hard Clusters.png',width=280)
        st.write(
            """
            Hard clustering is a widely used method in unsupervised machine learning that assigns each data point to a single, exclusive cluster.
            This approach is ideal for datasets with distinct, well-defined groups, making it effective for partitioning data into non-overlapping categories.
            """
        )

        # Section for Core Concepts
        with st.expander("Core Concepts of Hard Clustering"):
            
            st.subheader("Core Concepts of Hard Clustering")
            st.write("""
                Hard clustering is characterized by exclusive assignments and well-defined boundaries, simplifying the analysis. Key concepts include:
            """)

            st.write("**1. Exclusive Membership**")
            st.write("Each data point belongs to only one cluster, creating distinct, separate groupings within the dataset.")

            st.write("**2. Defined Boundaries**")
            st.write("Hard clustering is suitable when clusters have clear boundaries, simplifying interpretation and analysis.")

            st.write("**3. Distance-Based Assignments**")
            st.write("Most hard clustering algorithms use distance metrics to assign data points to the nearest cluster center, creating straightforward groupings.")

        # Section for Methods of Hard Clustering
        with st.expander("Methods of Hard Clustering"):
            st.subheader("Methods of Hard Clustering")
            st.write("""
                Hard clustering employs various methods that enforce exclusive memberships. Here are some common techniques:
            """)

            st.write("**1. K-Means**")
            st.write("""
                - Partitions the dataset into a predefined number of clusters, each represented by a center (centroid).
                - Assigns data points to the closest centroid, iteratively refining cluster centers to minimize within-cluster variance.
            """)
            st.write("")
            st.write("**2. Hierarchical Clustering**")
            st.write("""
                - Builds a hierarchy of clusters represented as a tree-like structure called a dendrogram.
                - Can be either Agglomerative (bottom-up) or Divisive (top-down), grouping points based on similarity.
            """)
            st.write("")
            st.write("**3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**")
            st.write("""
                - Groups points based on data density, effective for irregularly shaped clusters and noise handling.
                - Clusters high-density regions within a certain distance threshold, leaving low-density points as noise.
            """)

        # Section for Real-World Applications
        with st.expander("Real-World Applications of Hard Clustering"):
            st.subheader("Real-World Applications of Hard Clustering")
            st.write("""
                Hard clustering is valuable in scenarios where distinct groupings are beneficial for analysis. Here are a few applications:
            """)

            st.write("**1. Customer Segmentation**")
            st.write("Groups customers into exclusive categories based on similar behaviors or demographics, aiding in targeted marketing.")

            st.write("**2. Image Classification**")
            st.write("Separates images into non-overlapping categories based on visual features, commonly used in computer vision.")

            st.write("**3. Document Classification**")
            st.write("Groups documents into exclusive topics, useful for organizing large text datasets effectively.")

            st.write("**4. Anomaly Detection**")
            st.write("Identifies outliers or anomalies by recognizing data points that don’t fit well within any established cluster.")

        # Section for Advantages and Challenges
        with st.expander("Advantages and Challenges of Hard Clustering"):
            st.subheader("Advantages and Challenges")
            st.write("### Advantages")
            st.write("**1. Clear Group Separation**")
            st.write("Hard clustering ensures each data point is assigned to a single group, simplifying analysis and interpretation.")

            st.write("**2. Efficient and Scalable**")
            st.write("Many hard clustering algorithms are computationally efficient and suitable for large datasets.")

            st.write("### Challenges")
            st.write("**1. Rigidity**")
            st.write("Assigning points to only one cluster may be limiting when data points have overlapping characteristics.")

            st.write("**2. Sensitivity to Initial Conditions**")
            st.write("Methods like K-means may yield different results based on initial cluster centroids, affecting consistency.")

        # Section for Summary
        with st.expander("Summary"):
            st.subheader("Summary")
            st.write("""
                Hard clustering provides a structured approach to categorizing data into exclusive, well-defined groups. 
                This technique is advantageous for datasets with clear group distinctions, such as customer segmentation or anomaly detection.
                Familiarity with both hard and soft clustering techniques allows data scientists to select the best approach for analyzing complex datasets.
            """)

    with col2:
        # Set up the main title and introductory overview
        st.title("Soft Clusters")
        st.image('pages/clusterImages/Soft Clusters.png',width=280)
        st.write(
            """
            Soft clustering is an advanced approach in unsupervised machine learning that allows data points to belong to multiple clusters with different degrees of membership.
            This method is particularly useful for analyzing datasets where boundaries between clusters are unclear or overlapping.
            """
        )

        # Section for Core Concepts
        with st.expander("Core Concepts of Soft Clustering"):
            st.subheader("Core Concepts of Soft Clustering")
            st.write("""
                Soft clustering accommodates complex and overlapping data structures, adapting to the ambiguity often found in real-world datasets. Here are some key characteristics:
            """)

            st.write("**1. Multiple Memberships**")
            st.write("Each data point can partially belong to multiple clusters, described by membership coefficients. These coefficients indicate the degree of association with each cluster.")

            st.write("**2. Flexibility for Real-World Data**")
            st.write("Soft clustering captures the overlapping features present in many real-world datasets, accommodating data complexity.")

            st.write("**3. Probabilistic Assignments**")
            st.write("Many methods use probabilistic models, allowing for uncertainty in cluster assignments and adding depth to data analysis.")

        # Section for Methods of Soft Clustering
        with st.expander("Methods of Soft Clustering"):
            st.subheader("Methods of Soft Clustering")
            st.write("""
                Soft clustering employs various methods that allow data points to have partial cluster memberships. Below are some common techniques:
            """)
            st.write("")
            st.write("**1. Fuzzy C-Means (FCM)**")
            st.write("""
                - Allows partial association of data points with multiple clusters.
                - Minimizes an objective function that considers distances to each cluster center, weighted by degrees of membership.
            """)
            st.write("")
            st.write("**2. Gaussian Mixture Models (GMM)**")
            st.write("""
                - Assumes data comes from multiple Gaussian distributions, with each cluster represented by a unique Gaussian.
                - Uses the Expectation-Maximization (EM) algorithm to estimate parameters for each distribution, enabling probabilistic assignments of data points.
            """)
            st.write("")
            st.write("""**3. Weighted K-Means**""")
            st.write("""
                - An extension of traditional K-means, where data points are assigned weights, allowing them to influence multiple clusters.
                - Each point influences clustering based on its assigned weight, making the method more flexible.
            """)

        # Section for Real-World Applications
        with st.expander("Real-World Applications of Soft Clustering"):
            st.subheader("Real-World Applications of Soft Clustering")
            st.write("""
                Soft clustering techniques are useful in a variety of fields, especially when overlapping groups are naturally present. Here are a few examples:
            """)

            st.write("**1. Image Segmentation**")
            st.write("Used in image processing to identify overlapping objects or segments within images.")

            st.write("**2. Customer Segmentation**")
            st.write("In market research, it helps group customers with similar, but not identical, preferences.")

            st.write("**3. Bioinformatics**")
            st.write("Helps classify genes or proteins that may participate in multiple biological functions.")

            st.write("**4. Text Analysis**")
            st.write("Groups documents or texts with overlapping themes, beneficial for Natural Language Processing tasks.")

        # Section for Advantages and Challenges
        with st.expander("Advantages and Challenges of Soft Clustering"):
            st.subheader("Advantages and Challenges")
            st.write("### Advantages")
            st.write("**1. Accommodates Overlapping Data**")
            st.write("Well-suited for datasets where points logically belong to multiple groups.")

            st.write("**2. Enhanced Interpretability**")
            st.write("Probabilistic memberships provide richer insights into data relationships.")

            st.write("### Challenges")
            st.write("**1. Complexity**")
            st.write("These methods can be more computationally intensive compared to hard clustering.")

            st.write("**2. Parameter Sensitivity**")
            st.write("Initial parameter choices can influence outcomes, leading to different results across different runs.")

        # Section for Summary
        with st.expander("Summary"):
            st.subheader("Summary")
            st.write("""
                Soft clustering broadens the analysis of datasets with overlapping features, where traditional clustering methods may fall short.
                By leveraging partial memberships and probabilistic approaches, soft clustering provides a nuanced exploration of data relationships, proving especially valuable in fields such as image processing, market research, and bioinformatics.
                A solid understanding of both soft and hard clustering techniques equips data scientists with a full toolkit for handling diverse and complex data.
            """)
