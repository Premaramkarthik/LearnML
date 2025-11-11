import streamlit as st

def run():

    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    # Sample data for clustering
    X, y = make_blobs(n_samples=500, centers=5, random_state=42)

    # Title for the page
    st.title("Clustering Evaluation Metrics")

    # Introduction Section
    st.info("Introduction to Clustering Evaluation")
    st.write("""
    Clustering is a powerful technique in unsupervised learning, yet determining the effectiveness of a clustering model can be challenging.
    Unlike supervised models, clustering lacks true labels, which means we can't directly measure accuracy. 
    Instead, we rely on specific evaluation metrics to assess the quality of the clustering by analyzing aspects like **cohesion** 
    (how closely related the data points within a cluster are) and **separation** (how distinct each cluster is from others).
    """)

    # Cohesion and Separation Section
    # st.subheader("Cohesion and Separation")
    col1, spacer, col2 = st.columns([1,0.1,1])
    with col1:
        st.write("""### Cohesion
                 \n Measures the closeness of data points within a cluster. High cohesion means that points within the same cluster are similar to each other, which is desirable.""")
        st.image('pages/clusterImages/Cohesion.png',width=300)
    
    with col2:
        st.write("""
        ### Separation
         \nMeasures how far clusters are from each other. High separation indicates distinct boundaries between clusters, which ideally makes clusters easier to interpret and use for downstream tasks.""")
        st.image('pages/clusterImages/Separation.png',width=300)


    # Effective clustering achieves a good balance of high cohesion and high separation, which the following metrics aim to evaluate.
    # """)

    # Evaluation Metrics Section
    st.subheader("Evaluation Metrics for Clustering")
        # Silhouette Score
    with st.expander("Silhouette Score"):
        col1, spacer, col2 = st.columns([1,0.04,1])

        with col1:

            # Set the title of the app
            st.title("Understanding Silhouette Score")

            st.info(
                "The Silhouette Score is a valuable metric used to evaluate the quality of clustering algorithms. "
                "It measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). "
                "The score ranges from -1 to +1, providing insights into the effectiveness of the clustering."
            )

            # Score Interpretation Section
            st.subheader("Score Interpretation")
            st.write(
                "- **+1**: Indicates that the point is well matched to its own cluster and poorly matched to neighboring clusters.\n"
                "- **0**: Suggests that the point lies on or very close to the boundary between two clusters.\n"
                "- **-1**: Implies that the point may have been assigned to the wrong cluster."
            )

            # Calculation of Silhouette Score Section
            st.subheader("Calculation of Silhouette Score")
            st.write(
                "The Silhouette Score for a single data point \( i \) can be calculated using the following formula:\n\n"
                "$$ s(i) = \\frac{b(i) - a(i)}{\\max(a(i), b(i))} $$\n\n"
                "Where:\n"
            )
            st.write(
                "- **a(i)**: Average distance from point \( i \) to all other points in the same cluster (cohesion).\n"
                "- **b(i)**: Average distance from point \( i \) to all points in the nearest neighboring cluster (separation).\n\n"
                "This calculation provides a measure of how well-separated and cohesive the clusters are."
            )

            # Steps for Calculation Section
            st.subheader("Steps for Calculation")
            st.write("##### 1. Cohesion Calculation:")
            st.write("For each point \( i \) in a cluster, calculate the average distance to all other points in the same cluster.")

            st.write("##### 2. Separation Calculation:")
            st.write("For each point \( i \), calculate the average distance to all points in each neighboring cluster and take the minimum of these distances.")

            st.write("##### 3. Silhouette Value:")
            st.write("Use the formula above to compute the silhouette score for each point.")

            # Usage of Silhouette Score Section
            st.subheader("Usage of Silhouette Score")
            st.write(
                "The Silhouette Score is particularly useful for:\n"
            )
            st.write(
                "- **Evaluating Clustering Quality**: A higher average silhouette score indicates better-defined clusters.\n"
                "- **Determining Optimal Number of Clusters**: By comparing silhouette scores across different numbers of clusters, one can identify which configuration yields the best separation and cohesion."
            )

        # Conclusion Section
        st.subheader("Conclusion")
        st.write(
            "The Silhouette Score is an essential tool for assessing clustering techniques. By measuring both cohesion and separation, "
            "it provides a comprehensive view of clustering quality. Understanding how to calculate and interpret this score, along with its graphical representations, "
            "is crucial for effectively evaluating clustering outcomes in data analysis tasks."
        )

        with col2:

            k_values = range(2, 10)
            silhouette_scores = []
            
            # Calculate Silhouette Scores for different numbers of clusters
            for k in k_values:
                kmeans = KMeans(n_clusters=k, random_state=42)
                clusters = kmeans.fit_predict(X)
                score = silhouette_score(X, clusters)
                silhouette_scores.append(score)
            
            # Create a plot for Silhouette Scores
            fig, ax = plt.subplots()
            ax.plot(k_values, silhouette_scores, marker='o', color='b')
            ax.set_title("Silhouette Score vs Number of Clusters (k)")
            ax.set_xlabel("Number of Clusters (k)")
            ax.set_ylabel("Silhouette Score")
            st.pyplot(fig)

            # Section on Interpreting Silhouette Score Graphs
            st.subheader("Interpreting the Silhouette Score Graph")
            st.write(
                "The plot visualizes how the Silhouette Score varies with different numbers of clusters. Here are some key points to consider:"
            )

            st.write("##### Understanding the Plot:")
            st.write(
                "This graph illustrates the relationship between the number of clusters (k) and their corresponding Silhouette Scores. "
                "It helps identify how well-defined the clusters are as you vary k."
            )

            st.write("##### Key Observations:")
            st.write(
                "- A higher Silhouette Score indicates better-defined clusters. Look for peaks in the graph to determine optimal clustering.\n"
                "- If the score increases with more clusters, it suggests improved separation and cohesion.\n"
                "- Conversely, if you notice a decline after a certain number of clusters, it may indicate overfitting or that too many clusters have been chosen."
            )

            st.write("##### Cluster Separation Insights:")
            st.write(
                "In an ideal scenario, most points should have high positive Silhouette Scores, reflecting good separation between clusters. "
                "If many points have low or negative scores, it indicates potential issues with cluster selection."
            )

    
    with st.expander("Elbow Method"):
        import matplotlib.pyplot as plt
        from sklearn.cluster import KMeans
        from sklearn.datasets import make_blobs
        from sklearn.metrics import silhouette_score

        # Generate example data
        X, _ = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)

        col1, spacer, col2 = st.columns([1.2, 0.04, 1])

        with col1:
            # Set the title of the app
            st.title("Understanding the Elbow Method")

            st.info(
                "The Elbow Method is a technique used to determine the optimal number of clusters "
                "by observing the change in variance (sum of squared distances) as the number of clusters increases. "
                "The goal is to find the 'elbow' point where additional clusters bring diminishing returns in reducing variance."
            )

            # Concept of the Elbow Method Section
            st.subheader("Concept of the Elbow Method")
            st.write(
                "The Elbow Method analyzes the trade-off between the number of clusters (k) and the total variance "
                "(sum of squared distances from points to their cluster centroids) to select the ideal number of clusters."
            )
            st.write(
                "As k increases, the within-cluster variance decreases because each cluster becomes more compact. "
                "However, at a certain point (the 'elbow'), the decrease slows significantly, suggesting the optimal number of clusters."
            )

            # How the Elbow Method is Used Section
            st.subheader("How the Elbow Method is Used")
            st.write(
                "1. Calculate the **sum of squared errors (SSE)** for different values of k.\n"
                "2. Plot the SSE values against k.\n"
                "3. Identify the 'elbow' in the plot — the point where the rate of decrease sharply slows.\n\n"
                "This point typically represents the optimal number of clusters as it balances cluster compactness and minimal within-cluster variance."
            )

            # Steps for Implementing the Elbow Method
            st.subheader("Steps for Implementing the Elbow Method")
            st.write(
                "1. Run KMeans with different values of k (e.g., from 1 to 10).\n"
                "2. For each k, calculate the sum of squared distances (SSE) from each point to its assigned centroid.\n"
                "3. Plot k against SSE to observe the 'elbow' point, where further increases in k yield diminishing reductions in SSE."
            )

            # Usage of the Elbow Method Section
            st.subheader("Usage of the Elbow Method")
            st.write(
                "The Elbow Method is especially helpful for:\n"
                "- **Selecting Optimal Clusters**: Provides a visual tool to decide on the best number of clusters by minimizing within-cluster variance.\n"
                "- **Understanding Cluster Compactness**: Helps identify when adding more clusters ceases to significantly improve compactness, balancing efficiency and performance."
            )

            # Conclusion Section
            st.subheader("Conclusion")
            st.write(
                "The Elbow Method offers a straightforward approach to identifying the optimal number of clusters. "
                "Understanding and interpreting the 'elbow' in the plot helps balance cluster count and within-cluster cohesion effectively in clustering analysis."
            )

        with col2:
            # Calculate Sum of Squared Errors (SSE) for different k values
            k_values = range(1, 11)
            sse = []

            for k in k_values:
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(X)
                sse.append(kmeans.inertia_)

            # Create the Elbow Method plot
            fig, ax = plt.subplots()
            ax.plot(k_values, sse, marker='o', color='b')
            ax.set_title("Elbow Method: SSE vs Number of Clusters (k)")
            ax.set_xlabel("Number of Clusters (k)")
            ax.set_ylabel("Sum of Squared Errors (SSE)")
            st.pyplot(fig)

            # Interpreting the Elbow Method Graph
            # st.subheader("Interpreting the Elbow Method Graph")
            st.write(
                "The plot displays how the Sum of Squared Errors (SSE) changes as the number of clusters increases. "
                "Here’s how to interpret the plot:"
            )

            st.write("##### Understanding the Plot:")
            st.write(
                "As the number of clusters (k) increases, the SSE decreases. However, after a certain k (the 'elbow'), "
                "the rate of SSE reduction slows, indicating that additional clusters offer diminishing returns in reducing variance."
            )

            st.write("##### Key Observations:")
            st.write(
                "- The 'elbow' point is the suggested optimal number of clusters, where the SSE starts to decrease at a slower rate.\n"
                "- If no clear elbow is present, the data may not have well-defined clusters, or another clustering metric might be more suitable.\n"
                "- The chosen k should balance cluster compactness with computational efficiency."
            )

            st.write("##### Cluster Compactness Insights:")
            st.write(
                "At the 'elbow' point, clusters are generally well-defined and compact, with minimal within-cluster variance. "
                "Adding more clusters after this point usually indicates over-clustering without significant benefit to compactness."
            )

    with st.expander("Akaike Information Criterion (AIC)"):

        import matplotlib.pyplot as plt
        from sklearn.mixture import GaussianMixture
        from sklearn.datasets import make_blobs

        # Generate example data
        X, _ = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)

        col1, spacer, col2 = st.columns([1.2, 0.04, 1])

        with col1:
            # Set the title of the app
            st.title("Understanding Akaike Information Criterion (AIC)")

            st.info(
                "The Akaike Information Criterion (AIC) is a metric used to evaluate the quality of statistical models, "
                "specifically focusing on the trade-off between the goodness of fit and model complexity. "
                "Lower AIC values indicate a model with better explanatory power and minimal complexity."
            )

            # Concept of AIC Section
            st.subheader("Concept of AIC")
            st.write(
                "AIC evaluates how well a model fits the data while penalizing models with more parameters. "
                "This helps in selecting models that generalize better without being overly complex."
            )
            st.write(
                "Mathematically, AIC is calculated as:\n\n"
                "$$ \\text{AIC} = 2k - 2 \\ln(L) $$\n\n"
                "Where:\n"
            )
            st.write(
                "- **k**: Number of parameters in the model.\n"
                "- **L**: Maximum likelihood of the model, indicating how likely the model is given the data.\n"
                "This formula balances model complexity and goodness of fit, encouraging simpler models with high explanatory power."
            )

            # How AIC is Used Section
            st.subheader("How AIC is Used")
            st.write(
                "1. Fit the model to the data and calculate the maximum likelihood.\n"
                "2. Use the AIC formula to calculate the AIC score for different models.\n"
                "3. Choose the model with the lowest AIC score as it best balances fit and simplicity.\n\n"
                "By comparing AIC scores across multiple models, the model with the smallest AIC is preferred."
            )

            # Steps for Implementing AIC
            st.subheader("Steps for Implementing AIC")
            st.write(
                "1. Apply Gaussian Mixture Modeling (or other probabilistic models) to fit the data.\n"
                "2. Calculate AIC for each model with a different number of components (e.g., clusters).\n"
                "3. Select the model with the lowest AIC score to identify the optimal number of clusters."
            )

            # Usage of AIC Section
            st.subheader("Usage of AIC")
            st.write(
                "AIC is useful for:\n"
                "- **Model Selection**: Helps determine the number of components that best fits the data while avoiding overfitting.\n"
                "- **Balancing Fit and Complexity**: Discourages models with too many parameters unless they significantly improve fit."
            )

        # Conclusion Section
        st.subheader("Conclusion")
        st.write(
            "The Akaike Information Criterion is a valuable tool in model selection. "
            "It provides a balanced approach to choosing models that fit the data well without being overly complex. "
            "By understanding and applying AIC, you can make informed decisions in clustering and statistical modeling tasks."
        )

        with col2:
            # Calculate AIC for different number of components in Gaussian Mixture Model
            component_values = range(1, 11)
            aic_scores = []

            for n_components in component_values:
                gmm = GaussianMixture(n_components=n_components, random_state=42)
                gmm.fit(X)
                aic_scores.append(gmm.aic(X))

            # Create the AIC plot
            fig, ax = plt.subplots()
            ax.plot(component_values, aic_scores, marker='o', color='b')
            ax.set_title("Akaike Information Criterion (AIC) vs Number of Components")
            ax.set_xlabel("Number of Components")
            ax.set_ylabel("AIC Score")
            st.pyplot(fig)

            # Interpreting the AIC Graph
            st.write(
                "The plot displays how the AIC score changes as the number of components in the model increases. "
                "Here’s how to interpret the plot:"
            )

            st.write("##### Understanding the Plot:")
            st.write(
                "As the number of components increases, the AIC score initially decreases due to better fit. "
                "However, beyond a certain point, additional components lead to minimal improvements in fit, indicating overfitting."
            )

            st.write("##### Key Observations:")
            st.write(
                "- A lower AIC score suggests a better model in terms of fit and simplicity.\n"
                "- Look for the point where the AIC score reaches a minimum before it begins to increase again, indicating the optimal number of components.\n"
                "- Avoid models with unnecessarily low AIC scores that may result from excessive complexity."
            )

            st.write("##### Model Simplicity Insights:")
            st.write(
                "Choosing the model with the minimum AIC score helps balance fit and complexity, leading to a more generalizable model. "
                "Adding components beyond this point typically results in overfitting without substantial improvement in explanatory power."
            )

    with st.expander("Bayesian Information Criterion (BIC)"):
        
        col1, spacer, col2 = st.columns([1.2, 0.04, 1])

        with col1:
            # Set the title of the app
            st.title("Understanding Bayesian Information Criterion (BIC)")

            st.info(
                "The Bayesian Information Criterion (BIC) is a metric used for model selection, balancing model fit with complexity. "
                "BIC penalizes complex models to discourage overfitting, preferring models that explain the data well with fewer parameters. "
                "Lower BIC values suggest a model with a good balance of fit and simplicity."
            )

            # Concept of BIC Section
            st.subheader("Concept of BIC")
            st.write(
                "BIC measures model quality based on the likelihood of the model and the number of parameters used, aiming to find a model "
                "that explains the data well without unnecessary complexity."
            )
            st.write(
                "Mathematically, BIC is calculated as:\n\n"
                "$$ \\text{BIC} = k \\ln(n) - 2 \\ln(L) $$\n\n"
                "Where:\n"
            )
            st.write(
                "- **k**: Number of parameters in the model.\n"
                "- **n**: Number of data points.\n"
                "- **L**: Maximum likelihood of the model, indicating the probability of the observed data given the model.\n\n"
                "This formula favors models with high likelihood while penalizing models with more parameters to avoid overfitting."
            )

            # How BIC is Used Section
            st.subheader("How BIC is Used")
            st.write(
                "1. Fit the model to the data to calculate the maximum likelihood.\n"
                "2. Use the BIC formula to calculate the BIC score for models with different complexities (e.g., different numbers of clusters).\n"
                "3. Choose the model with the lowest BIC score for an optimal balance of fit and simplicity.\n\n"
                "Comparing BIC scores across models helps in selecting a model with the minimum necessary complexity."
            )

            # Steps for Implementing BIC
            st.subheader("Steps for Implementing BIC")
            st.write(
                "1. Apply a probabilistic model, such as Gaussian Mixture Modeling, to fit the data.\n"
                "2. Calculate BIC for each model with a different number of components (e.g., clusters).\n"
                "3. Select the model with the lowest BIC score to determine the optimal number of components."
            )

            # Usage of BIC Section
            st.subheader("Usage of BIC")
            st.write(
                "BIC is useful for:\n"
                "- **Model Selection**: Helps identify the best-fit model without overfitting.\n"
                "- **Comparing Models of Different Complexities**: Penalizes overly complex models unless they significantly improve the likelihood."
            )

        # Conclusion Section
        st.subheader("Conclusion")
        st.write(
            "The Bayesian Information Criterion is a powerful tool for model selection, offering a balance between fit and simplicity. "
            "Understanding and applying BIC helps in selecting models that generalize well by penalizing unnecessary complexity, making it "
            "useful for clustering, statistical modeling, and more."
        )

        with col2:
            # Calculate BIC for different number of components in Gaussian Mixture Model
            component_values = range(1, 11)
            bic_scores = []

            for n_components in component_values:
                gmm = GaussianMixture(n_components=n_components, random_state=42)
                gmm.fit(X)
                bic_scores.append(gmm.bic(X))

            # Create the BIC plot
            fig, ax = plt.subplots()
            ax.plot(component_values, bic_scores, marker='o', color='b')
            ax.set_title("Bayesian Information Criterion (BIC) vs Number of Components")
            ax.set_xlabel("Number of Components")
            ax.set_ylabel("BIC Score")
            st.pyplot(fig)

            # Interpreting the BIC Graph
            st.subheader("Interpreting the BIC Graph")
            st.write(
                "The plot displays how the BIC score changes with an increasing number of components in the model. "
                "Here’s how to interpret the plot:"
            )

            st.write("##### Understanding the Plot:")
            st.write(
                "As the number of components increases, the BIC score may initially decrease due to better fit. "
                "However, beyond a certain point, additional components lead to a penalty for complexity, resulting in an increase in the BIC score."
            )

            st.write("##### Key Observations:")
            st.write(
                "- A lower BIC score suggests a better model in terms of fit and simplicity.\n"
                "- Look for the point where the BIC score reaches a minimum, indicating the optimal number of components.\n"
                "- Avoid models with unnecessarily low BIC scores resulting from too many parameters, as they may lead to overfitting."
            )

            st.write("##### Optimal Model Insights:")
            st.write(
                "Selecting the model with the minimum BIC score achieves a balance between fit and complexity, "
                "leading to a model that is more likely to generalize well. Adding components beyond this point typically increases complexity without significant benefits in fit."
            )


    with st.expander("Gap Statistic"):

        import matplotlib.pyplot as plt
        import numpy as np
        from sklearn.cluster import KMeans
        from sklearn.datasets import make_blobs
        from sklearn.metrics import pairwise_distances
        from sklearn.preprocessing import MinMaxScaler

        # Generate example data
        X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
        X = MinMaxScaler().fit_transform(X)  # Scale data for better reference gap calculation

        col1, spacer, col2 = st.columns([1.3, 0.04, 1])

        with col1:
            # Set the title of the app
            st.title("Understanding Gap Statistic")

            st.info(
                "The Gap Statistic is a metric for estimating the optimal number of clusters in a dataset. "
                "It compares the within-cluster dispersion of the dataset to that of a uniformly random reference dataset. "
                "A higher gap indicates that the clusters are well-separated, guiding the choice of cluster count."
            )

            # Concept of Gap Statistic Section
            st.subheader("Concept of Gap Statistic")
            st.write(
                "The Gap Statistic assesses the clustering structure by comparing the within-cluster sum of squares (WSS) to that of random "
                "data uniformly distributed over the same range. The optimal number of clusters is the one with the maximum gap value, "
                "where the WSS in the dataset is farthest from random clustering."
            )
            st.write(
                "The Gap Statistic formula is:\n\n"
                "$$ \\text{Gap}(k) = \\mathbb{E}_{\\text{ref}}[\\log(W_k)] - \\log(W_k) $$\n\n"
                "Where:\n"
            )
            st.write(
                "- **W_k**: Within-cluster dispersion for the dataset with \( k \) clusters.\n"
                "- **\\( \\mathbb{E}_{\\text{ref}}[\\log(W_k)] \\)**: Expected WSS for a random reference dataset with \( k \) clusters.\n\n"
                "This comparison provides insight into how well-separated the actual clusters are compared to random data."
            )

            # Steps for Implementing Gap Statistic
            st.subheader("Steps for Implementing Gap Statistic")
            st.write(
                "1. For each cluster count \( k \), compute the within-cluster sum of squares (WSS) for both the dataset and a uniformly random reference dataset.\n"
                "2. Calculate the log of WSS for each \( k \), and take the difference between the actual data and reference data.\n"
                "3. Plot the Gap statistic for each \( k \) and look for the maximum gap."
            )

            # Usage of Gap Statistic Section
            st.subheader("Usage of Gap Statistic")
            st.write(
                "The Gap Statistic helps to:\n"
                "- **Estimate Optimal Clusters**: Identify the ideal number of clusters by comparing data clustering to random clustering.\n"
                "- **Avoid Overfitting**: Helps avoid selecting too many clusters by finding the point where additional clusters no longer provide separation benefits."
            )

        # Conclusion Section
        st.subheader("Conclusion")
        st.write(
            "The Gap Statistic is a robust technique for cluster selection. It provides an objective way to estimate the number of clusters "
            "by comparing the actual clustering structure to random clustering. The maximum gap value indicates an optimal clustering structure."
        )

        with col2:
            # Calculate Gap Statistic for different numbers of clusters
            def compute_gap_statistic(X, k_values, n_references=5):
                gap_values = []
                for k in k_values:
                    # Fit KMeans to the original data and calculate WSS
                    kmeans = KMeans(n_clusters=k, random_state=42)
                    clusters = kmeans.fit_predict(X)
                    wss = np.log(np.sum(np.min(pairwise_distances(X, kmeans.cluster_centers_, metric='euclidean')**2, axis=1)))
                    
                    # Generate random reference datasets and compute WSS for each
                    reference_wss = []
                    for _ in range(n_references):
                        random_data = np.random.uniform(0, 1, X.shape)
                        kmeans_ref = KMeans(n_clusters=k, random_state=42)
                        clusters_ref = kmeans_ref.fit_predict(random_data)
                        ref_wss = np.log(np.sum(np.min(pairwise_distances(random_data, kmeans_ref.cluster_centers_, metric='euclidean')**2, axis=1)))
                        reference_wss.append(ref_wss)
                    
                    # Calculate the Gap statistic
                    gap = np.mean(reference_wss) - wss
                    gap_values.append(gap)
                return gap_values

            # Define range of clusters and compute gap statistic
            k_values = range(1, 11)
            gap_values = compute_gap_statistic(X, k_values)

            # Plot Gap Statistic
            fig, ax = plt.subplots()
            ax.plot(k_values, gap_values, marker='o', color='b')
            ax.set_title("Gap Statistic vs Number of Clusters (k)")
            ax.set_xlabel("Number of Clusters (k)")
            ax.set_ylabel("Gap Statistic")
            st.pyplot(fig)

            # Interpreting the Gap Statistic Graph
            st.write(
                "The graph shows the Gap Statistic as a function of the number of clusters. The optimal number of clusters is typically where "
                "the gap is at its highest value, suggesting the greatest deviation from random clustering."
            )

            st.write("##### Understanding the Plot:")
            st.write(
                "The Gap Statistic plot indicates how the clustering structure diverges from a random reference structure. "
                "A higher gap value at a specific \( k \) value suggests that this is an ideal number of clusters."
            )

            st.write("##### Key Observations:")
            st.write(
                "- Look for the highest peak in the Gap Statistic plot; this indicates the most distinct clustering structure.\n"
                "- The peak suggests the optimal number of clusters, balancing separation and simplicity.\n"
                "- If the gap does not significantly increase with more clusters, it may indicate that additional clusters provide minimal benefit."
            )

            st.write("##### Optimal Cluster Insights:")
            st.write(
                "The ideal number of clusters is found at the point with the highest gap value. This suggests that the dataset has a well-defined clustering structure "
                "relative to a random distribution, and adding more clusters beyond this point would likely lead to overfitting."
            )






    # col1, spacer, col2 = st.columns([1.2,0.01,1])



    # with col1:

        # # Silhouette Score
        # with st.expander("Silhouette Score"):
        #     st.write("""
        #     - **Purpose**: Measures how similar a point is to its own cluster (cohesion) compared to other clusters (separation).
        #     - **Range**: The score ranges from -1 to +1, where:
        #         - A score close to +1 indicates that the point is well-matched to its cluster and poorly matched to neighboring clusters.
        #         - A score of 0 indicates that the point is on or very close to the boundary between two clusters.
        #         - A score of -1 indicates that the point might have been assigned to the wrong cluster.
        #     - **How It’s Calculated**:
        #         - For each point, calculate the average distance to all other points in the same cluster (cohesion) and to all points in the nearest cluster (separation).
        #         - The silhouette score combines these two distances to gauge overall clustering quality.
        #     - **Usage**: Silhouette Score is ideal for analyzing both cohesion and separation and is especially useful for selecting the optimal number of clusters.
        #     """)

        # # Elbow Method
        # with st.expander("Elbow Method"):
        #     st.write("""
        #     - **Purpose**: Helps determine the optimal number of clusters by analyzing the variance within each cluster.
        #     - **Concept**:
        #         - Plot the sum of squared distances (SSE) between points and their assigned cluster centroids for various values of \( k \) (number of clusters).
        #         - The "elbow" point, where the rate of decrease sharply slows, often indicates the best number of clusters, balancing cohesion with efficiency.
        #     - **Usage**: The Elbow Method is often used as an initial approach to select \( k \) by visualizing the diminishing returns in cluster cohesion as \( k \) increases.
        #     """)

        # Akaike Information Criterion (AIC)
        # with st.expander("Akaike Information Criterion (AIC)"):
        #     st.write("""
        #     - **Purpose**: AIC is a statistical metric used to evaluate model quality while penalizing complexity, helping to avoid overfitting.
        #     - **How It’s Calculated**:
        #         - Based on the log-likelihood of the clustering model, AIC incorporates a penalty proportional to the number of parameters.
        #         - Lower AIC values suggest a better balance of model fit and simplicity.
        #     - **Usage**: AIC is useful for models like Gaussian Mixture Models where likelihoods are computed. It is especially helpful in comparing models of different complexities.
        #     """)

        # # Bayesian Information Criterion (BIC)
        # with st.expander("Bayesian Information Criterion (BIC)"):
        #     st.write("""
        #     - **Purpose**: Similar to AIC, BIC assesses model fit while introducing a stronger penalty for complexity, making it stricter in avoiding overfitting.
        #     - **How It’s Calculated**:
        #         - Like AIC, BIC uses the log-likelihood but includes a larger penalty factor based on data points and the model’s parameters.
        #     - **Usage**: BIC is often preferred over AIC when working with larger datasets, as it typically favors simpler models. It is also suitable for models like Gaussian Mixture Models and aids in selecting the optimal number of clusters.
        #     """)

        # # Gap Statistic
        # with st.expander("Gap Statistic"):
        #     st.write("""
        #     - **Purpose**: Provides an alternative approach to determining the optimal number of clusters by comparing observed cluster dispersion with that of a random distribution.
        #     - **Concept**:
        #         - The gap statistic calculates the difference between the within-cluster dispersion for the observed data and that of random uniformly distributed data.
        #         - A larger gap value indicates that the data is well-clustered at the chosen \( k \), suggesting an optimal cluster count.
        #     - **Usage**: The Gap Statistic is valuable in identifying the best number of clusters, especially in datasets with irregular shapes or varied densities.
        #     """)

        # Summary Section
    st.subheader("Summary of Clustering Evaluation Metrics")
    st.write("""
    Each of these metrics offers unique insights into clustering quality:
    - **Silhouette Score** provides a direct measure of cohesion and separation.
    - **Elbow Method** helps to identify optimal cluster numbers by examining the trade-off between cohesion and the number of clusters.
    - **AIC and BIC** penalize complexity to prevent overfitting, favoring simpler clustering models.
    - **Gap Statistic** compares the observed clustering structure to random structures, identifying significant cluster groupings.

    Using these metrics together allows for a comprehensive evaluation of clustering results, balancing different aspects of clustering quality for a robust analysis.
    """)

    # with col2:



    #     # # Silhouette Score Visualization
    #     # with st.expander("Silhouette Score Visualization"):
    #     #     k_values = range(2, 10)
    #     #     silhouette_scores = []
            
    #     #     for k in k_values:
    #     #         kmeans = KMeans(n_clusters=k, random_state=42)
    #     #         clusters = kmeans.fit_predict(X)
    #     #         score = silhouette_score(X, clusters)
    #     #         silhouette_scores.append(score)
            
    #     #     fig, ax = plt.subplots()
    #     #     ax.plot(k_values, silhouette_scores, marker='o', color='b')
    #     #     ax.set_title("Silhouette Score vs Number of Clusters (k)")
    #     #     ax.set_xlabel("Number of Clusters (k)")
    #     #     ax.set_ylabel("Silhouette Score")
    #     #     st.pyplot(fig)

    #     # Elbow Method Visualization
    #     with st.expander("Elbow Method Visualization"):
    #         sse = []
            
    #         for k in k_values:
    #             kmeans = KMeans(n_clusters=k, random_state=42)
    #             kmeans.fit(X)
    #             sse.append(kmeans.inertia_)
            
    #         fig, ax = plt.subplots()
    #         ax.plot(k_values, sse, marker='o', color='g')
    #         ax.set_title("Elbow Method: SSE vs Number of Clusters (k)")
    #         ax.set_xlabel("Number of Clusters (k)")
    #         ax.set_ylabel("Sum of Squared Errors (SSE)")
    #         st.pyplot(fig)

    #     # AIC and BIC Visualization (Example with Gaussian Mixture)
    #     with st.expander("AIC/BIC Visualization"):
    #         from sklearn.mixture import GaussianMixture
            
    #         aic_scores = []
    #         bic_scores = []
            
    #         for k in k_values:
    #             gmm = GaussianMixture(n_components=k, random_state=42)
    #             gmm.fit(X)
    #             aic_scores.append(gmm.aic(X))
    #             bic_scores.append(gmm.bic(X))
            
    #         fig, ax = plt.subplots(figsize = (5,5))
    #         ax.plot(k_values, aic_scores, marker='o', color='purple', label="AIC")
    #         ax.plot(k_values, bic_scores, marker='x', color='red', label="BIC")
    #         ax.set_title("AIC and BIC vs Number of Clusters (k)")
    #         ax.set_xlabel("Number of Clusters (k)")
    #         ax.set_ylabel("Score")
    #         ax.legend()
    #         st.pyplot(fig)

    #     # Gap Statistic Visualization (Mock Example)
    #     with st.expander("Gap Statistic Visualization"):
    #         # Generate a mock plot for Gap Statistic as an example
    #         # Note: Calculating the real gap statistic can be complex without external libraries
    #         gap_values = np.log(np.array(sse)) - np.random.uniform(0, 0.5, size=len(sse))  # Mock gap values for visualization
            
    #         fig, ax = plt.subplots()
    #         ax.plot(k_values, gap_values, marker='o', color='orange')
    #         ax.set_title("Gap Statistic vs Number of Clusters (k)")
    #         ax.set_xlabel("Number of Clusters (k)")
    #         ax.set_ylabel("Gap Value")
    #         st.pyplot(fig)


    # Run the app with `streamlit run <filename>.py`
