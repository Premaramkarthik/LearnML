def run():
    # st.header('Clustering Algorithms and Techniques')
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import make_blobs
    from scipy.spatial.distance import cdist
    import seaborn as sns
    import plotly.express as px
    from sklearn.datasets import make_blobs
    from scipy.cluster.hierarchy import dendrogram, linkage
    import seaborn as sns

        
    # Helper function to generate random data
    def generate_data(n_samples=300, centers=4, cluster_std=0.60):
        X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=42)
        return X

    # Helper function to generate overlapping (soft) clusters
    def generate_soft_cluster_data(n_samples=300, centers=4, cluster_std=1.5):
        X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=42)
        return X

    # Function for KMeans Clustering
    def kmeans_clustering(X, n_clusters=3):
        kmeans = KMeans(n_clusters=n_clusters)
        y_kmeans = kmeans.fit_predict(X)
        return kmeans, y_kmeans

    # Function for DBSCAN Clustering
    def dbscan_clustering(X, eps=0.5, min_samples=5):
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        y_dbscan = dbscan.fit_predict(X)
        return dbscan, y_dbscan

    # Function for KMeans++ Clustering
    def kmeans_plus_plus(X, n_clusters=3):
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10)
        y_kmeans = kmeans.fit_predict(X)
        return kmeans, y_kmeans

    # Function for Agglomerative Clustering
    def agglomerative_clustering(X, n_clusters=3):
        agg_clust = AgglomerativeClustering(n_clusters=n_clusters)
        y_agg = agg_clust.fit_predict(X)
        return agg_clust, y_agg


    
    cluster = st.selectbox( "Choose type Clustering Algorithms",["Hard Clusters", "Soft Cluster"])

    if cluster == "Hard Clusters":

        # Generate some sample data
        X = generate_data()
        # Dropdown for selecting clustering algorithm
        algorithm = st.selectbox(
            "Choose a clustering algorithm",
            ["K-Means", "K-Means++", "Hirearchial", "DBSCAN"]
        )
        if algorithm == "K-Means":
                st.subheader("K-Means Clustering")
                        
                st.info("K-Means is a popular unsupervised machine learning algorithm that partitions data into \( K \) distinct clusters, each represented by its centroid (the mean of points in the cluster). The goal is to minimize variance within clusters while maximizing variance between them.")
                
                col1, spacer, col2= st.columns([1, 0.06, 1])

                with col1:

                    st.write("""
                    #### Algorithm Workflow 

                    1. **Initialization**:
                    - **Choosing \( K \)**: The process starts by selecting the number of clusters, \( K \), which represents the distinct groups the data will be partitioned into. This is often determined using the Elbow Method, which plots the sum of squared distances between points and their assigned centroids for various \( K \) values, helping identify the point where adding more clusters yields little improvement in reducing variance. 
                    - **Centroid Initialization**: Initial centroids, which represent the centers of each cluster, are then selected. This can be done randomly, which convergence by spreading the initial centroids farther apart, reducing the chances of poor clustering results.

                    2. **Point Assignment**:
                    - In this step, each data point is assigned to the nearest centroid based on a chosen distance metric (typically Euclidean distance), which calculates the straight-line distance between points. The goal is to group each point with the centroid that it is closest to, thereby forming clusters of points that share spatial proximity.

                    3. **Centroid Update**:
                    - Once points are assigned to clusters, new centroids are recalculated for each cluster. The centroid of a cluster is the mean position of all the points in that cluster, so the algorithm calculates the average position (or "center of mass") of the points in each cluster. This process helps reposition each centroid to better represent the data points assigned to it.

                    4. **Convergence Check**:
                    - The algorithm then re-evaluates point assignments and centroid locations, continuing to iterate between these steps until the centroids and point assignments no longer change significantly. This indicates that clusters have stabilized, meaning the centroids are now in optimal positions, and no further adjustments are needed.

                    5. **Final Cluster Output**:
                    - Once convergence is achieved, the algorithm finalizes the output by providing the final positions of centroids and the cluster assignments for each data point. This final result offers a clear and stable partitioning of the data into distinct clusters, with each data point grouped according to proximity, revealing underlying patterns or structures within the data.
                    """)

                with col2:
                
                    st.write("")    

                    n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)

                    X = generate_data()

                    kmeans, y_kmeans = kmeans_clustering(X, n_clusters=n_clusters)

                    fig, ax = plt.subplots()
                    ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
                    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)
                    ax.set_title(f"K-Means Clustering with {n_clusters} clusters")
                    st.pyplot(fig)


                    st.write("")

                    

                    st.write("")

                col1, spacer, col2= st.columns([1, 0.06, 1])

                with col1:
                    st.write("""####  Key Benefits""")
                            
                    st.write("""
                    - **Simplicity**: Easy to implement and understand.
                    - **Efficiency**: Generally faster for large datasets.
                    - **Scalability**: Can handle large datasets effectively.
                    - **Convergence**: Quickly converges to a solution, ensuring faster execution in many clustering tasks.""")

                with col2:

                    st.write("""
                    #### Limitations

                    - **Choosing \( K \)**: Requires prior knowledge of the number of clusters.
                    - **Sensitivity to Initialization**: Poor initialization can lead to suboptimal results.
                    - **Assumption of Spherical Clusters**: Assumes clusters are spherical and equally sized.
                    - **Outlier Sensitivity**: Outliers can skew centroid positions.""")
                
                st.write("""
                        #### Real-World Use Cases

                        K-Means clustering has a wide range of applications across various domains, including:

                        - **Market Segmentation**: Identifying distinct customer segments based on purchasing behavior or demographic information.
                        - **Image Compression**: Reducing the number of colors in an image by clustering pixel colors and replacing them with their respective centroid colors.
                        - **Pattern Recognition**: Classifying patterns in datasets, such as handwriting recognition or facial recognition.
                        - **Anomaly Detection**: Identifying outliers in data by observing which points do not fit well into any cluster.""")
                
                st.write("""
                        ### Summary
                        
                        K-Means is a powerful and widely used clustering technique that provides valuable insights into data structures through its ability to partition datasets into meaningful groups. Understanding its mechanics and applications can help practitioners effectively utilize this algorithm for various data analysis tasks.                """)



        elif algorithm == "K-Means++":

                st.subheader("K-Means++ Clustering")
                                
                st.info("K-Means++ is an enhanced version of the standard K-Means algorithm designed to improve the initialization of cluster centers. By selecting initial centroids more strategically, K-Means++ aims to achieve better clustering results and faster convergence.")

                col1, spacer, col2 = st.columns([1, 0.06, 1])

                with col1:
                    st.write("""
                    #### Algorithm Steps 

                    1. **Initialization**:
                    - **Choosing \( K \)**: The process begins by deciding on the number of clusters, \( K \), using methods like the Elbow Method or the Silhouette Score to help find an optimal number, balancing clustering quality and complexity.
                    - **First Centroid Selection**: The algorithm selects the first centroid randomly from the data points, setting the foundation for spread-out centroids.

                    2. **Subsequent Centroid Selection**:
                    - For each remaining data point, the distance to the nearest already chosen centroid is calculated. This step ensures that new centroids are selected from areas that are distant from existing centroids, aiming to prevent tightly grouped initial centroids and promoting better spread.

                    3. **Probability-Based Selection**:
                    - The next centroid is selected from the remaining data points based on a probability proportional to the square of the distance from the nearest existing centroid. Points farther from existing centroids have a higher chance of being selected, which helps maintain diverse initial centroid placement and supports effective clustering.

                    4. **Repeat Process**:
                    - This probability-based selection continues until all \( K \) centroids have been initialized, ensuring each centroid is placed in a unique, well-spread region within the data space.

                    5. **Standard K-Means Execution**:
                    - Once initialization is complete, the standard K-Means steps follow: data points are assigned to the nearest centroid, centroids are updated based on the mean of assigned points, and the process iterates. This continues until assignments stabilize, achieving convergence, with well-distributed final clusters.
                    """)



                with col2:
                
                    st.write("")
                    
                    # n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)
                    # Reuse the K-Means function with K-Means++ initialization
                    n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)
                    kmeans, y_kmeans = kmeans_clustering(X, n_clusters=n_clusters)
                    
                    # Plot K-Means++ clustering results
                    fig, ax = plt.subplots()
                    ax.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
                    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)
                    ax.set_title(f"K-Means++ Clustering with {n_clusters} Clusters")
                    st.pyplot(fig)

                    # st.write("")

                    # st.write("")

                col1, spacer, col2 = st.columns([1, 0.06, 1])

                with col1:

                    st.write("""#### Key Advantages""")
                                    
                    st.write("""
                    - **Improved Initialization**: Reduces the likelihood of poor clustering results due to random initialization.
                    - **Faster Convergence**: By starting with better initial centroids, K-Means++ often converges more quickly than standard K-Means.
                    - **Better Final Clustering**: Generally yields lower clustering error compared to traditional K-Means due to more effective centroid placement.
                    """)

                with col2:

                    st.write("""
                    #### Limitations

                    - **Choosing \( K \)**: Requires prior knowledge of the number of clusters.
                    - **Sensitivity to Initialization**: While improved, it can still be sensitive to initial seeds.
                    - **Local Optima**: Like standard K-Means, it can get stuck in local optima; running multiple times can help mitigate this.
                    """)

                

                st.write("""
                        #### Real-World Applications

                        K-Means++ has a wide range of applications across various domains, including:

                        - **Market Segmentation**: Identifying distinct customer segments based on purchasing behavior or demographic information.
                        - **Image Compression**: Reducing the number of colors in an image by clustering pixel colors and replacing them with their respective centroid colors.
                        - **Pattern Recognition**: Classifying patterns in datasets, such as handwriting recognition or facial recognition.
                        - **Anomaly Detection**: Identifying outliers in data by observing which points do not fit well into any cluster.
                """)

                st.write("""
                        ### Conclusion
                        
                        K-Means++ is a powerful enhancement over traditional K-Means that provides better initialization for cluster centers. Understanding its mechanics and applications can help practitioners effectively utilize this algorithm for various data analysis tasks.
                """)


        elif algorithm == "Hirearchial":

            # col1, spacer ,col2 = st.columns([1,0.7,1])

            hire = st.radio("Select type of Hirearchial Clustering Technique", ["Agglomerative Clustering","Divisive Clustering"])
            
            if hire == "Agglomerative Clustering":
                # st.write("""
                #     **Agglomerative Clustering** is a hierarchical clustering method that starts with each data point as its own cluster. 
                #     In each step, the algorithm merges the closest clusters based on a chosen linkage criterion (e.g., single, complete, or average linkage) 
                #     until only the desired number of clusters remains.
                # """)
                
                # # Parameters for Agglomerative Clustering
                # n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)
                # agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
                # y_agglo = agglomerative.fit_predict(X)
                
                # # Plot Agglomerative Clustering results
                # fig, ax = plt.subplots(figsize=(2, 2))
                # ax.scatter(X[:, 0], X[:, 1], c=y_agglo, s=50, cmap='viridis')
                # ax.set_title(f"Agglomerative Clustering with {n_clusters} Clusters")
                # st.pyplot(fig)

                # if algorithm == "Agglomerative Clustering":
                    st.subheader("Agglomerative Clustering")
                                    
                    st.info("Agglomerative Clustering is a hierarchical clustering method that builds a hierarchy of clusters by iteratively merging the closest pairs of clusters. It is particularly effective for identifying clusters of various shapes.")

                    col1, spacer, col2 = st.columns([1, 0.06, 1])

                    with col1:
                        st.write("""
                        #### Algorithm Steps 

                        1. **Initialization**:
                        - **Start with Individual Clusters**: Begin by treating each data point as its own cluster, resulting in a large number of small clusters equal to the number of data points.
                        - **Distance Calculation**: Calculate the distances between each pair of clusters according to a chosen linkage criterion, such as single-linkage (minimum distance), complete-linkage (maximum distance), or average-linkage (average distance). This criterion determines how clusters are defined and influences the shape of the final clusters.

                        2. **Merging Clusters**:
                        - Identify the two clusters that are closest based on the chosen distance metric, then merge them into a single cluster. This step reduces the number of clusters by one and progressively builds larger clusters by combining the most similar ones.

                        3. **Repeat**:
                        - Continue calculating distances and merging the closest clusters in each iteration until either all points are merged into a single cluster or a specified number of clusters is achieved. This process builds a hierarchy of clusters, moving from many individual points to fewer, larger clusters.

                        4. **Dendrogram Representation**:
                        - The hierarchical clustering results can be visualized as a dendrogram, which is a tree-like diagram that shows the order of merges and the relative distance at which clusters were joined. The dendrogram provides a clear view of the cluster hierarchy and can help identify an optimal number of clusters by examining where larger gaps appear between clusters.

                        5. **Final Cluster Output**:
                        - After the merging process is complete, the algorithm outputs the final cluster assignments for each data point and a dendrogram that represents the clustering process. This final output enables a clear understanding of the data’s hierarchical structure and cluster relationships.
                        """)


                    with col2:
                
                        st.write("")
                        import streamlit as st
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from scipy.cluster.hierarchy import dendrogram, linkage
                        from sklearn.datasets import make_blobs

                        # Helper function to generate random data
                        def generate_data(n_samples=10, centers=3, cluster_std=0.60):
                            X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=42)
                            return X

                        st.info("The dendrogram visualizes this process from bottom to top.")

                        # Generate synthetic data with fewer samples for clarity in visualization
                        X = generate_data(n_samples=10)  # Reduced number of samples for clearer dendrogram

                        # Compute the linkage matrix
                        Z = linkage(X, method='ward')

                        # Create a figure for the dendrogram
                        fig, ax = plt.subplots(figsize=(10, 6))

                        # Plot the dendrogram
                        dendrogram(Z, ax=ax)  # Show full dendrogram for clarity

                        # Draw a horizontal line to indicate where clusters are formed (Agglomerative)
                        n_clusters = st.slider('Select Number of Clusters', min_value=2, max_value=5, value=3)
                        threshold = Z[-(n_clusters-1), 2]  # Get the distance at which to cut for n_clusters
                        ax.axhline(y=threshold, color='r', linestyle='--')

                        # Set titles and labels
                        ax.set_title("Dendrogram for Agglomerative Clustering")
                        ax.set_xlabel("Sample Index")
                        ax.set_ylabel("Distance")

                        # Rotate x-ticks for better visibility if needed (optional)
                        plt.xticks(rotation=45)

                        # Show plot in Streamlit
                        st.pyplot(fig)

                        st.write("The red dashed line indicates the threshold for merging clusters based on your selection.")

                        st.write("")

                        st.write("")

                    col1, spacer, col2 = st.columns([1, 0.06, 1])

                    with col1:
                        st.write("""#### Key Advantages""")
                                        
                        st.write("""
                        - **No Need to Specify Number of Clusters**: Unlike K-Means, there is no requirement to predetermine the number of clusters.
                        - **Flexible Cluster Shapes**: Capable of identifying clusters of various shapes and sizes due to its hierarchical nature.
                        - **Dendrogram Visualization**: Provides a clear visual representation of the clustering process and relationships between clusters.
                        """)


                    with col2:

                        st.write("""
                        #### Limitations

                        - **Computationally Intensive**: The algorithm can be slow for large datasets due to distance calculations between all pairs of clusters.
                        - **Sensitive to Noise and Outliers**: Outliers can significantly affect clustering results and lead to suboptimal cluster formations.
                        - **Requires Distance Metric**: The choice of distance metric can impact clustering results and may require careful consideration.
                        """)
                    

                    st.write("""
                            #### Real-World Applications

                            Agglomerative Clustering has a wide range of applications across various domains, including:

                            - **Customer Segmentation**: Identifying distinct groups of customers based on purchasing behavior or preferences.
                            - **Gene Expression Analysis**: Grouping genes with similar expression patterns in bioinformatics.
                            - **Image Segmentation**: Dividing images into segments based on pixel similarity for image processing tasks.
                            - **Social Network Analysis**: Identifying communities within social networks based on user interactions.
                    """)

                    st.write("""
                            ### Conclusion
                            
                            Agglomerative Clustering is a powerful hierarchical clustering technique that provides valuable insights into data structures through its ability to build a hierarchy of clusters. Understanding its mechanics and applications can help practitioners effectively utilize this algorithm for various data analysis tasks.
                    """)


            elif hire == "Divisive Clustering":
                # st.subheader("Divisive Clustering")

                # st.write("""
                #     **Divisive Clustering**, also known as DIANA (Divisive Analysis), is a hierarchical clustering approach that begins with all data points in a single cluster.
                #     It then splits clusters iteratively, focusing on separating data based on dissimilarities. This top-down approach is particularly useful for datasets where broad groupings can be progressively refined.
                # """)
                
                # # Perform divisive clustering and visualize with a dendrogram
                # st.write("Divisive clustering uses a dendrogram to show splits within clusters.")
                # Z = linkage(X, 'ward')  # Using Ward's method to illustrate the divisive structure
                
                # fig, ax = plt.subplots(figsize=(2, 2))
                # dendrogram(Z, truncate_mode='level', p=4)
                # ax.set_title("Dendrogram for Divisive Clustering")
                # st.pyplot(fig)

                # if algorithm == "Divisive Clustering":
                st.subheader("Divisive Clustering")
                                
                st.info("Divisive Clustering is a hierarchical clustering method that starts with all data points in a single cluster and recursively splits the most heterogeneous clusters until each data point is in its own cluster or a specified number of clusters is reached.")

                col1, spacer, col2 = st.columns([1, 0.06, 1])

                with col1:
                    st.write("""
                    #### Algorithm Steps 

                    1. **Initialization**:
                    - **Start with One Cluster**: The algorithm begins by treating all data points as a single cluster, representing the entire dataset as one unified group. This contrasts with agglomerative clustering, which starts with each point as its own cluster.

                    2. **Cluster Splitting**:
                    - **Use a Flat Clustering Method**: To split the current cluster, a flat clustering algorithm, such as K-Means, is applied. This divides the current cluster into two or more sub-clusters by grouping points based on similarity, thus creating an initial separation within the data.

                    3. **Select Cluster to Split**:
                    - **Choose the Most Heterogeneous Cluster**: After splitting, the algorithm identifies the cluster with the greatest internal dissimilarity, typically measured by variance or Sum of Squared Error (SSE). The cluster with the highest SSE is considered the most heterogeneous and is selected for further splitting, ensuring that divisions occur where clusters are less cohesive.

                    4. **Repeat**:
                    - **Iterative Splitting Process**: This process of identifying and splitting the most heterogeneous cluster is repeated. The algorithm continues splitting clusters iteratively until each data point forms its own cluster or until a specified number of clusters is reached, refining the separation of data points step by step.

                    5. **Final Cluster Output**:
                    - **Output the Clusters Formed**: The algorithm concludes by providing the final clusters, representing a hierarchical division of the data. These clusters can be used for further analysis or visualization, offering insights into the dataset's inherent structure and patterns.
                    """)

                    
                    # st.write("")

                    # st.write("")

                with col2:
                
                    st.write("")

                    # Note: Divisive clustering does not have a direct implementation in popular libraries like scikit-learn,
                    # so we will not include code for visualization here.
                    # Assuming X is already defined as your data
                    # Streamlit application for Divisive Clustering
                    import streamlit as st
                    import numpy as np
                    import matplotlib.pyplot as plt
                    from scipy.cluster.hierarchy import dendrogram, linkage
                    from sklearn.datasets import make_blobs

                    # Helper function to generate random data
                    def generate_data(n_samples=30, centers=3, cluster_std=0.60):
                        X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=42)
                        return X
                    # Generate synthetic data with sufficient samples for clarity in visualization
                    X = generate_data(n_samples=30)  # Increased number of samples for clarity

                    # Compute the linkage matrix using Ward's method (used for visualization purposes)
                    Z = linkage(X, method='ward')

                    # Create a figure for the dendrogram
                    fig, ax = plt.subplots(figsize=(10, 6))

                    # Plot the dendrogram
                    dendrogram(Z, ax=ax)  # Do not reverse order; show natural structure

                    # Slider for user input on number of clusters
                    n_clusters = st.slider('Select Number of Clusters', min_value=2, max_value=5, value=3)

                    # Draw a horizontal line to indicate where clusters are formed (Divisive)
                    threshold = Z[-(n_clusters-1), 2]  # Get the distance at which to cut for n_clusters
                    ax.axhline(y=threshold, color='g', linestyle='--')  # Use green color for clarity

                    # Set titles and labels
                    ax.set_title("Dendrogram for Divisive Clustering")
                    ax.set_xlabel("Sample Index")
                    ax.set_ylabel("Distance")

                    # Rotate x-ticks for better visibility if needed (optional)
                    plt.xticks(rotation=45)

                    # Show plot in Streamlit
                    st.pyplot(fig)

                    st.write("The green dashed line indicates the threshold for splitting clusters based on your selection.")

                col1, spacer, col2 = st.columns([1, 0.06, 1])

                with col1:

                    st.write("""#### Key Advantages""")
                                    
                    st.write("""
                    - **No Need to Specify Number of Clusters Initially**: Similar to agglomerative clustering, it does not require prior knowledge of the number of clusters.
                    - **Effective for Large Clusters**: Can efficiently identify larger clusters within the dataset.
                    - **Hierarchical Structure**: Provides a clear hierarchical representation of how clusters are formed.
                    """)
                    

                with col2:

                    st.write("""
                    #### Limitations

                    - **Computational Complexity**: The algorithm can be computationally intensive due to repeated splitting operations.
                    - **Requires Distance Metric**: The choice of distance metric can significantly affect clustering results and may require careful consideration.
                    - **Less Commonly Used**: Compared to agglomerative clustering, divisive clustering is less frequently applied in practice and may lack robust implementations.
                    """)

                st.write("""
                        #### Real-World Applications

                        Divisive Clustering can be applied in various domains, including:

                        - **Market Research**: Identifying distinct groups within large datasets by starting with broad categories and refining them into specific segments.
                        - **Gene Expression Analysis**: Grouping genes based on expression levels by initially considering all genes as one group and splitting them into more specific categories.
                        - **Document Clustering**: Organizing documents into hierarchical categories based on content similarity by starting with all documents in one cluster.
                        - **Social Network Analysis**: Analyzing community structures by treating entire networks as single entities and progressively identifying sub-communities.
                """)

                st.write("""
                        ### Conclusion
                        
                        Divisive Clustering is a powerful hierarchical clustering technique that provides insights into data structures by starting from a single cluster and recursively splitting it. Understanding its mechanics and applications can help practitioners effectively utilize this algorithm for various data analysis tasks.
                """)


        elif algorithm == "DBSCAN":
            


            # if algorithm == "DBSCAN":
            st.subheader("DBSCAN Clustering")
                            
            st.info("DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised clustering algorithm that groups together points that are closely packed, marking points in low-density regions as outliers. It is particularly effective for identifying clusters of arbitrary shape and handling noise.")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:
                st.write("""
                #### Algorithm Steps 

                1. **Parameter Selection**:
                - **Epsilon (ε)**: Set the radius of the neighborhood around each point, determining the maximum distance for points to be considered neighbors. A suitable ε value defines the local neighborhood for density calculations and impacts the size and shape of clusters.
                - **MinPts**: Specify the minimum number of points required within the ε-neighborhood to consider a region dense enough to form a cluster. MinPts helps distinguish between dense regions (clusters) and sparse regions (noise).

                2. **Core Point Identification**:
                - A point is classified as a **core point** if it has at least MinPts points within its ε-neighborhood. Core points serve as the foundation of clusters, as they signify dense areas in the dataset where clusters can grow.

                3. **Cluster Expansion**:
                - Starting from any unvisited core point, the algorithm adds all reachable points within its ε-neighborhood to the cluster. For each new core point added, this expansion process continues recursively, growing the cluster by including all neighboring points until no more points satisfy the criteria for inclusion.

                4. **Border and Noise Points**:
                - Points that are reachable from core points but do not meet the MinPts criterion within their own ε-neighborhood are designated as **border points**. These points lie on the edges of clusters, linking dense regions to less dense areas. Points that are neither core nor border points are classified as **noise** or **outliers**, as they do not belong to any dense region.

                5. **Final Cluster Output**:
                - Upon completion, the algorithm outputs the clusters formed along with any identified noise points. The result clearly shows dense regions as distinct clusters, while noise points are marked separately, providing a robust clustering solution for data with varying densities and noise.
                """)

                
                # st.write("")

                # st.write("")



            with col2:
                
                st.write("")

                X = generate_data()

                eps = st.slider('Select epsilon (distance threshold)', min_value=0.1, max_value=1.0, value=0.3)
                min_samples = st.slider('Select minimum samples', min_value=1, max_value=10, value=5)

                dbscan = DBSCAN(eps=eps, min_samples=min_samples)
                y_dbscan = dbscan.fit_predict(X)

                fig_dbscan, ax_dbscan = plt.subplots()
                ax_dbscan.scatter(X[:, 0], X[:, 1], c=y_dbscan, s=50, cmap='viridis')
                ax_dbscan.set_title("DBSCAN Clustering")
            
                st.pyplot(fig_dbscan)

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:
                st.write("""#### Key Advantages""")
                                
                st.write("""
                - **No Predefined Number of Clusters**: Unlike K-Means, DBSCAN does not require specifying the number of clusters in advance.
                - **Arbitrary Shape Clusters**: Can find clusters of various shapes and sizes, making it versatile for different datasets.
                - **Robust to Outliers**: Effectively identifies noise and outliers without affecting clustering results.
                - **Density-Based Approach**: Focuses on the density of data points, allowing it to discover clusters that are not connected.
                """)


            with col2:

                st.write("""
                #### Limitations

                - **Parameter Sensitivity**: The results can be sensitive to the choice of ε and MinPts; improper settings can lead to poor clustering.
                - **Varied Density Issues**: Struggles with datasets containing clusters of varying densities.
                - **High Dimensionality Challenges**: Performance may degrade in high-dimensional spaces due to the curse of dimensionality.
                """)

            st.write("""
                    #### Real-World Applications

                    DBSCAN has a wide range of applications across various domains, including:

                    - **Geospatial Analysis**: Identifying clusters in geographical data such as locations of events or incidents.
                    - **Image Processing**: Segmenting images by grouping similar pixel values while ignoring noise.
                    - **Anomaly Detection**: Detecting outliers in datasets by identifying points that do not belong to any cluster.
                    - **Biological Data Analysis**: Grouping genes or proteins based on expression levels or other biological features.
            """)

            st.write("""
                    ### Conclusion
                    
                    DBSCAN is a powerful density-based clustering technique that excels at identifying clusters in noisy datasets without requiring prior knowledge of the number of clusters. Its ability to discover arbitrarily shaped clusters makes it a valuable tool for various data analysis tasks.
            """)

    elif cluster == "Soft Cluster":
        
        algorith = st.selectbox(
            "Choose a clustering algorithm",
            ["Fuzzy C-Means", "Gaussian Mixture Models", "Weighted K-Means"])
        
        # Generate some sample data
        X = generate_data()
        # Dropdown for selecting clustering algorithm
        

        if algorith == "Fuzzy C-Means":
            st.subheader("Fuzzy C-Means Clustering")
            
            st.info("Fuzzy C-Means (FCM) is an unsupervised clustering algorithm that allows each data point to belong to multiple clusters with varying degrees of membership. Unlike K-Means, which assigns each point to a single cluster, FCM provides a more flexible approach by using fuzzy logic.")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:
                st.write("""
                #### Algorithm Workflow 

                1. **Initialization**:
                - **Choosing \( C \)**: The number of clusters, \( C \), is selected, often through methods like the Elbow Method or Silhouette Analysis. These methods help determine the optimal number of clusters that best partition the data based on how compact and separated the clusters are.
                - **Membership Initialization**: The membership matrix, which represents the degree of membership of each data point to each cluster, is initialized randomly or uniformly. This matrix evolves as the algorithm progresses, allowing data points to have partial membership across multiple clusters.

                2. **Centroid Update**:
                - The centroids of each cluster are recalculated by taking the weighted average of all data points, where the weights are determined by the membership values. Points with higher membership values in a cluster will have a greater influence on the new centroid's position, ensuring the centroid is more closely aligned with the dense areas of the data.

                3. **Membership Update**:
                - After centroids are updated, the membership values are recalculated for each data point based on its distance to the centroids. A point’s membership value for a cluster increases as it gets closer to the cluster's centroid, reflecting the fuzzy nature of this clustering method, where data points can belong to multiple clusters with varying degrees.

                4. **Convergence Check**:
                - The algorithm iterates between updating centroids and membership values. Convergence is checked when changes in the membership values fall below a predefined threshold, indicating that further iterations will result in minimal changes and the clusters have stabilized.

                5. **Final Cluster Output**:
                - Once the algorithm has converged, it outputs the final cluster centroids and the membership values for each data point. This provides a clear representation of how the data points are distributed across clusters, allowing for further analysis or visualization to gain insights into the fuzzy partitioning of the dataset.
                """)



            with col2:

                st.write("")
                                
                                # Parameters
                n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=10, value=3)
                # m = 2  # Fuzziness parameter
                m = st.slider('Fuzziness parameter', min_value=1.1, max_value=5.0, value=2.0, step=0.1)
                max_iter = 100
                error = 0.005

                from skfuzzy.cluster import cmeans

                # Generate synthetic data (you need to define `generate_soft_cluster_data` separately)
                X = generate_soft_cluster_data(n_samples=100)

                # Perform Fuzzy C-Means clustering
                result = cmeans(X.T, n_clusters, m=m, error=error, maxiter=max_iter)

                # Assuming `result` is the tuple containing the values
                cntr, u, obj_fcn, n_iter, fpc, *extra_values = result


                # for i, arr in enumerate(result):
                #     if hasattr(arr, 'shape'):  # Check if `arr` has the `shape` attribute
                #         st.write(f"Array {i} - Shape: {arr.shape}")
                #         st.write(f"Array {i} (first few elements): {arr[:5]}")  # Show first 5 elements
                #     else:
                #         st.write(f"Array {i} (scalar or non-indexable): {arr}")  # Print scalar or other non-indexable value

                # st.write(f"Result length: {len(result)}")
                # st.write(f"Result contents: {result}")
                # # Display each result in the Fuzzy C-Means output with type checking
                # for i, arr in enumerate([cntr, u, obj_fcn, n_iter, fpc]):
                #     if isinstance(arr, np.ndarray):  # Check if `arr` is an array
                #         st.write(f"Array {i} (first few elements): {arr[:5]}")  # Show first 5 elements if array
                #     else:
                #         st.write(f"Array {i} (scalar value): {arr}")  # Just display the scalar value if not an array
                 
                
                 
                # # Assign clusters based on maximum membership
                y_fcm = np.argmax(u, axis=0)

                # Plot the clusters and centroids
                fig, ax = plt.subplots()
                scatter = ax.scatter(X[:, 0], X[:, 1], c=y_fcm, s=50, cmap='viridis')
                ax.scatter(cntr[:, 0], cntr[:, 1], c='red', s=200, alpha=0.5)  # Centroids

                # Add labels for clarity
                for i, center in enumerate(cntr):
                    ax.text(center[0] + 0.5, center[1] + 0.1, f'{i+1}', color='red', fontsize=12, ha='left')

                # Set plot title and axis labels
                ax.set_title(f"Fuzzy C-Means Clustering with {n_clusters} clusters")

                # Show colorbar for cluster assignment
                fig.colorbar(scatter)

                # Display the plot in Streamlit
                st.pyplot(fig)

                # st.write("")

                st.write("")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:
                st.write("""#### Key Benefits""")
                
                st.write("""
                - **Soft Clustering**: Allows data points to belong to multiple clusters with varying degrees of membership.
                - **Flexibility**: More adaptable to real-world data where boundaries between clusters are not always clear.
                - **Improved Performance**: Can provide better results than hard clustering methods in datasets with overlapping clusters.
                - **Robustness to Noise**: Better handles noise and outliers by distributing their influence across multiple clusters.
                """)


            with col2:

                st.write("""
                #### Limitations

                - **Choosing \( C \)**: Requires prior knowledge of the number of clusters.
                - **Sensitivity to Initialization**: Poor initialization can lead to suboptimal results.
                - **Computational Complexity**: More computationally intensive than K-Means due to iterative updates of memberships.
                - **Parameter Sensitivity**: The choice of fuzziness parameter \( m \) can significantly affect results.
                """)

            st.write("""
                    #### Real-World Use Cases

                    Fuzzy C-Means clustering has various applications across different fields:

                    - **Image Segmentation**: Identifying regions in images where boundaries are not well defined.
                    - **Medical Diagnosis**: Classifying patient data where symptoms may overlap between conditions.
                    - **Market Research**: Understanding customer segments that may belong to multiple categories based on behavior.
                    - **Pattern Recognition**: Recognizing patterns in datasets where classes overlap significantly.
            """)

            st.write("""
                    ### Summary
                    
                    Fuzzy C-Means is a powerful clustering technique that provides flexibility in assigning data points to multiple clusters. Its ability to handle uncertainty and overlapping data makes it suitable for various applications in real-world scenarios. Understanding its mechanics and applications can help practitioners utilize this algorithm effectively for complex data analysis tasks.
            """)


        elif algorith == "Gaussian Mixture Models":
            st.subheader("Gaussian Mixture Models Clustering")

            st.info("Gaussian Mixture Models (GMMs) are a probabilistic model that assumes all data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters. GMMs can perform soft clustering, assigning probabilities to each data point for belonging to each cluster.")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:
                st.write("""
                #### Algorithm Workflow 

                1. **Initialization**:
                - **Choosing \( K \)**: The number of Gaussian components, \( K \), is chosen, often determined using methods like the Elbow Method or Bayesian Information Criterion (BIC), which help identify the optimal number of clusters by balancing fit and model complexity.
                - **Parameter Initialization**: The parameters of the Gaussian components, including the means, covariances, and mixing coefficients, are initialized. These parameters define the characteristics of the Gaussian distributions and are iteratively refined during the algorithm’s execution.

                2. **Expectation Step (E-Step)**:
                - In this step, the algorithm calculates the probability (or responsibility) that each data point belongs to each Gaussian component, based on the current estimates of the means, covariances, and mixing coefficients. This step assigns a "soft" membership to each data point, meaning a point can belong to multiple clusters with varying probabilities.

                3. **Maximization Step (M-Step)**:
                - Based on the probabilities computed in the E-step, the algorithm updates the parameters of the Gaussian components. The means, covariances, and mixing coefficients are adjusted to better fit the data, reflecting the updated distribution of points across the clusters.

                4. **Convergence Check**:
                - The E-step and M-step are repeated iteratively until the algorithm converges. Convergence is typically reached when changes in the parameters of the Gaussian components are smaller than a predefined threshold, indicating that further updates will result in minimal adjustments.

                5. **Final Cluster Output**:
                - Once the algorithm has converged, it outputs the final cluster assignments and the parameters of the Gaussian distributions. This provides a probabilistic representation of the data, where each point has a soft assignment to one or more clusters, and the cluster boundaries are modeled as Gaussian distributions.
                """)



            with col2:
                
                st.write("")
                
                n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)

                X = generate_soft_cluster_data(n_samples=100)  # Generate synthetic data

                # Perform Gaussian Mixture Model clustering
                from sklearn.mixture import GaussianMixture

                gmm = GaussianMixture(n_components=n_clusters)
                gmm.fit(X)
                
                # Predict cluster labels
                y_gmm = gmm.predict(X)

                fig, ax = plt.subplots()
                ax.scatter(X[:, 0], X[:, 1], c=y_gmm, s=50, cmap='viridis')
                
                # Plotting the ellipses representing Gaussian components
                for mean, covar in zip(gmm.means_, gmm.covariances_):
                    v, w = np.linalg.eigh(covar)
                    u = w[0] / np.linalg.norm(w[0])
                    angle = np.arctan(u[1] / u[0])
                    angle = np.degrees(angle)
                    ell = plt.matplotlib.patches.Ellipse(mean, v[0] * 2, v[1] * 2,
                                                        angle=angle,
                                                        color='red', alpha=0.5)
                    ax.add_patch(ell)

                ax.set_title(f"Gaussian Mixture Models Clustering with {n_clusters} clusters")
                
                st.pyplot(fig)

                # st.write("")

                # st.write("")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:

                st.write("""#### Key Benefits""")
                
                st.write("""
                - **Soft Clustering**: Allows data points to belong to multiple clusters with varying degrees of membership.
                - **Flexibility**: Can model clusters with different shapes and sizes due to its use of Gaussian distributions.
                - **Probabilistic Interpretation**: Provides probabilities for cluster membership, allowing for uncertainty in assignments.
                - **Robustness**: Better handles overlapping clusters compared to hard clustering methods like K-Means.
                """)


            with col2:

                st.write("""
                #### Limitations

                - **Choosing \( K \)**: Requires prior knowledge of the number of clusters.
                - **Sensitivity to Initialization**: Poor initialization can lead to suboptimal results; using multiple initializations can help mitigate this.
                - **Computational Complexity**: More computationally intensive than K-Means due to iterative updates and calculations.
                - **Assumption of Gaussian Distribution**: Assumes that clusters follow a Gaussian distribution; may not perform well if this assumption is violated.
                """)

            st.write("""
                    #### Real-World Use Cases

                    GMM clustering has various applications across different fields:

                    - **Image Segmentation**: Identifying regions in images where pixel values are similar.
                    - **Speech Recognition**: Modeling different phonemes as mixtures of Gaussians for improved classification accuracy.
                    - **Anomaly Detection**: Identifying outliers by modeling normal behavior as a mixture of Gaussians.
                    - **Financial Modeling**: Analyzing market behaviors where returns may follow a mixture of distributions.
            """)

            st.write("""
                    ### Summary
                    
                    Gaussian Mixture Models provide a powerful framework for clustering that accommodates overlapping clusters and offers probabilistic interpretations. Understanding its mechanics and applications can help practitioners effectively utilize this algorithm for various data analysis tasks.
            """)



        elif algorith == "Weighted K-Means":
            st.subheader("Weighted K-Means Clustering")

            st.info("Weighted K-Means is an extension of the standard K-Means algorithm that incorporates weights for each data point during the clustering process. This allows for different levels of importance for data points, enabling more nuanced clustering results.")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:

                st.write("""
                #### Algorithm Workflow 

                1. **Initialization**:
                - **Choosing \( K \)**: The number of clusters, \( K \), is selected, typically using methods like the Elbow Method, which helps visualize the trade-off between the number of clusters and the explained variance, helping to determine the optimal \( K \).
                - **Weight Initialization**: Weights are assigned to each data point based on their importance or relevance to the clustering task. This could depend on factors such as feature significance or prior knowledge about the data.

                2. **Point Assignment**:
                - Each data point is assigned to the nearest centroid based on a weighted distance metric. This metric considers both the Euclidean distance to the centroids and the assigned weights, ensuring that points with higher weights have a stronger influence on the clustering process.

                3. **Centroid Update**:
                - New centroids are calculated as the weighted mean of all points in each cluster. The weighting of points ensures that centroids are repositioned to better represent the current cluster members, with more influence given to points with higher weights.

                4. **Convergence Check**:
                - The algorithm iterates between the assignment and update steps. It continues until the cluster assignments no longer change significantly, indicating that the clusters have stabilized, or until a predefined maximum number of iterations is reached.

                5. **Final Cluster Output**:
                - After convergence, the algorithm outputs the final cluster assignments and the positions of the centroids. This provides a clear partitioning of the data into distinct clusters, where the influence of individual points is determined by their assigned weights.
                """)

            with col2:
                
                st.write("")
                
                n_clusters = st.slider('Select the number of clusters', min_value=2, max_value=6, value=3)

                # Generate synthetic data
                X = generate_soft_cluster_data(n_samples=100)  # Assuming you have a function to generate synthetic data

                # Assign random weights to each point
                weights = np.random.rand(X.shape[0])  # Random weights between 0 and 1

                # Perform Weighted K-Means clustering
                from sklearn.cluster import KMeans

                kmeans = KMeans(n_clusters=n_clusters)
                
                # Fit model using sample_weight parameter
                kmeans.fit(X, sample_weight=weights)

                # Predict cluster labels
                y_wkmeans = kmeans.predict(X)

                fig, ax = plt.subplots()
                ax.scatter(X[:, 0], X[:, 1], c=y_wkmeans, s=50, cmap='viridis')
                
                # Plot centroids
                ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)
                
                ax.set_title(f"Weighted K-Means Clustering with {n_clusters} clusters")
                
                st.pyplot(fig)

                st.write("")

                st.write("")

            col1, spacer, col2 = st.columns([1, 0.06, 1])

            with col1:

                st.write("""#### Key Benefits""")
                
                st.write("""
                - **Flexibility**: Allows different weights for data points, enabling more nuanced clustering results.
                - **Improved Performance**: Can enhance clustering quality by emphasizing more important data points.
                - **Robustness**: Better handles datasets with varying importance among observations.
                - **Applicability**: Suitable for scenarios where certain data points should have more influence on cluster formation than others.
                """)

            with col2:

                st.write("""
                #### Limitations

                - **Choosing \( K \)**: Requires prior knowledge of the number of clusters.
                - **Sensitivity to Initialization**: Poor initialization can lead to suboptimal results; using multiple initializations can help mitigate this.
                - **Complexity in Weight Assignment**: Determining appropriate weights for each data point can be challenging and may require domain knowledge.
                - **Computational Overhead**: More computationally intensive than standard K-Means due to weight handling.
                """)

            st.write("""
                    #### Real-World Use Cases

                    Weighted K-Means clustering has various applications across different fields:

                    - **Market Segmentation**: Identifying customer segments where certain customers are more influential based on their purchasing power.
                    - **Anomaly Detection**: Focusing on important features or points that should influence clustering decisions more heavily.
                    - **Resource Allocation**: Allocating resources in scenarios where certain tasks or projects have different levels of priority or importance.
                    - **Environmental Studies**: Clustering geographical data where some locations are more significant due to ecological importance or population density.
            """)

            st.write("""
                    ### Summary
                    
                    Weighted K-Means is a powerful extension of the standard K-Means technique that allows for varying levels of influence among data points in clustering. Understanding its mechanics and applications can help practitioners utilize this algorithm effectively for complex data analysis tasks.
            """)
