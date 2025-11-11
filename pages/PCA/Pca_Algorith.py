
# Page configuration
#st.set_page_config(page_title="Principal Component Analysis (PCA)", layout="wide")

def run():
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    
    # Inject CSS for custom styling (optional for a professional look)
    st.markdown(
        """
        <style>
        .section-header { font-size: 1.4em; font-weight: bold; color: #333; }
        .subsection-header { font-size: 1.2em; font-weight: bold; margin-top: 1em; color: #444; }
        .content-box { border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        </style>
        """, unsafe_allow_html=True
    )

    # Main Title and Introduction
    st.title("Principal Component Analysis (PCA)")

    st.info(
        """
        **Principal Component Analysis (PCA)** is a widely-used dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional space.
        This process creates new features, called **principal components**, which capture the most significant variance in the data, helping to simplify complex datasets while retaining essential information.
        PCA is commonly applied in data visualization, noise reduction, and enhancing machine learning performance.
        """
    )

    # Load Dataset
    # @st.cache
    def load_data():
        iris = load_iris()
        X = iris.data
        y = iris.target
        return X, y

    X, y = load_data()

    # Key Steps in PCA
    st.subheader("Key Steps in Principal Component Analysis (PCA)")

    # Columns layout for step-by-step explanation
    col1, col2 = st.columns([1.5, 1])  

    # Step 1: Standardizing the Data
    with col1:
        # st.markdown("<div class='subsection-header'>1. Standardizing the Data</div>", unsafe_allow_html=True)
        st.write("##### 1. Standardizing the Data")
        st.write("""
        PCA begins by standardizing the dataset, which is a critical preprocessing step. 
        This involves two main actions:

        - **Centering**: The data is adjusted so that each feature has a mean of zero. This means that the average value of each feature is subtracted from the dataset, ensuring that the data is centered around the origin in the feature space.

        - **Scaling**: Each feature is scaled to have a variance of one. This ensures that features with larger ranges do not dominate the analysis. By standardizing, PCA creates a uniform scale across all features, allowing them to contribute equally to the analysis.
        """)

        st.write("")

    # Step 2: Covariance Matrix Calculation
        # st.markdown("<div class='subsection-header'>2. Covariance Matrix Calculation</div>", unsafe_allow_html=True)
        st.write("##### 2. Covariance Matrix Calculation")
        st.write("""
        Once the data is standardized, PCA computes the covariance matrix. 
        This matrix serves as a summary of how different features in the dataset relate to one another:

        - **Understanding Relationships**: The covariance matrix captures how features vary together. 
        For instance, if two features tend to increase or decrease together, their covariance will be positive; if one increases while the other decreases, their covariance will be negative.

        - **Identifying Patterns**: By analyzing this matrix, PCA can identify patterns and correlations between features, which are crucial for understanding the underlying structure of the data.
        """)

        st.write("")

    # Step 3: Eigenvalues and Eigenvectors
        #st.markdown("<div class='subsection-header'>3. Eigenvalues and Eigenvectors</div>", unsafe_allow_html=True)
        st.write("##### 3. Eigenvalues and Eigenvectors")
        st.write("""
        After constructing the covariance matrix, PCA calculates eigenvalues and eigenvectors:

        - **Eigenvalues**: These values indicate how much variance each principal component captures from the data. Higher eigenvalues correspond to components that explain more variability.

        - **Eigenvectors**: Each eigenvector represents a direction in the feature space along which the data varies most significantly. These directions become the new axes (principal components) onto which the original data will be projected.
        """)
        
        # Adding an expander with an image
        # with st.expander("See the visualization of Eigenvalues and Eigenvectors"):
        #     st.image("path_to_your_image.png", caption="Eigenvectors and Eigenvalues Visualization", use_column_width=True)


        st.write("")

        # st.markdown("<div class='subsection-header'>4. Sorting and Selecting Components</div>", unsafe_allow_html=True)
        st.write("##### 4. Sorting and Selecting Components")
        st.write("""
        The next step involves sorting these principal components based on their eigenvalues:

        - **Ranking Variance Explained**: The components are ordered from highest to lowest eigenvalue, allowing PCA to rank them according to how much variance they explain in the dataset.

        - **Prioritizing Information**: This ranking helps identify which components capture the most significant patterns in the data, making it easier to decide which components to retain for further analysis.
        """)

        st.write("")

        # st.markdown("<div class='subsection-header'>5. Projecting onto Principal Components</div>", unsafe_allow_html=True)
        st.write("##### 5. Projecting onto Principal Components")

        st.write("""
        With the selected principal components determined, PCA projects the original dataset onto this new set of axes:

        - **Dimensionality Reduction**: This projection transforms the original high-dimensional data into a lower-dimensional space while retaining as much variance as possible. The new representation emphasizes the most important features of the data.

        - **Simplifying Analysis**: By reducing dimensionality, PCA simplifies subsequent analyses and visualizations, making it easier to interpret complex datasets.
        """)

        st.write("")

        # st.markdown("<div class='subsection-header'>6. Visualizing the Transformed Data</div>", unsafe_allow_html=True)
        st.write("##### 6. Visualizing the Transformed Data")

        st.write("""
        Finally, PCA facilitates visualization of the transformed data:

        - **Identifying Patterns**: Visualizing data in terms of its principal components allows analysts to observe clustering patterns, relationships between different classes, and overall distributions within the dataset.

        - **Enhanced Interpretation**: By plotting data points in this reduced-dimensional space, it becomes easier to identify trends and anomalies that may not be apparent in higher dimensions.

        Visualizations such as scatter plots or biplots can reveal insights into how different groups are separated or how features interact with one another.
        """)



    with col2:

        import streamlit as st
        import numpy as np
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        from pandas.plotting import parallel_coordinates
        from sklearn.decomposition import PCA
        from sklearn.datasets import load_digits
        from sklearn.preprocessing import StandardScaler
        from mpl_toolkits.mplot3d import Axes3D

        # Load Iris dataset
        iris = sns.load_dataset("iris")

        # Extract features (X) and target (y)
        X = iris.drop("species", axis=1)  # Drop the species column for features
        y = iris["species"].map({"setosa": 1, "versicolor": 2, "virginica": 3})  # Map species names to numbers

        # Standardize the data
        X_std = StandardScaler().fit_transform(X)

        # Apply PCA to reduce dimensions
        n_components = st.slider("Select number of PCA components", 1, 3, 2)

        # Perform PCA on standardized data
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X_std)
        X_pca_df = pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(n_components)])

        # Display the original standardized data
        st.subheader("Original Standardized Data")
        st.write(pd.DataFrame(X) )#, columns=[f"Feature {i+1}" for i in range(X_std.shape[1])]).head())

        # Display the PCA-transformed data
        st.subheader(f"PCA-Transformed Data ({n_components} Components):")
        st.write(X_pca_df.head())

        # Visualize PCA result in 2D or 3D
        if n_components == 2:
            plt.figure(figsize=(10, 6))
            plt.scatter(X_pca_df["PC1"], X_pca_df["PC2"], c=y.values, cmap='viridis', alpha=0.6, s=20)
            plt.xlabel("PC1")
            plt.ylabel("PC2")
            plt.title("PCA 2D Visualization of Digits Dataset",fontsize = 12)
            st.pyplot(plt)

        elif n_components == 3:
            fig = plt.figure(figsize=(10, 6))
            ax = fig.add_subplot(111, projection='3d')
            scatter = ax.scatter(X_pca_df["PC1"], X_pca_df["PC2"], X_pca_df["PC3"], c=y.values, cmap='viridis', alpha=0.6, s=20)
            ax.set_xlabel("PC1")
            ax.set_ylabel("PC2")
            ax.set_zlabel("PC3")
            ax.set_title("PCA 3D Visualization of Digits Dataset",fontsize = 8)
            st.pyplot(fig)


    # Explained Variance Section
    st.header("Explained Variance")

    st.write(
        """
        Explained variance is a critical metric in PCA, quantifying the proportion of the total variance captured by each principal component.
        By analyzing the explained variance, we can determine the optimal number of components needed without significant loss of information.
        """
    )


    col1, col2 = st.columns(2)

    with col1:
        st.code(
            """
        # Example code for calculating explained variance using Scikit-Learn's PCA
        pca_sklearn = PCA(n_components=2)
        pca_sklearn.fit(X_std)
        explained_variance_ratio = pca_sklearn.explained_variance_ratio_

        # Plotting Explained Variance Ratio
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7, color='skyblue')
        ax.set_title('Explained Variance Ratio of Principal Components')
        ax.set_xlabel('Principal Components')
        ax.set_ylabel('Explained Variance Ratio')
        ax.set_xticks(range(1, len(explained_variance_ratio) + 1))
        ax.set_xticklabels([f'PC{i}' for i in range(1, len(explained_variance_ratio) + 1)])

        # Display the plot in Streamlit
        st.pyplot(fig)


            """, language="python"
        )


    with col2:
                
            # Explained Variance for Digits dataset
            explained_variance_digits = pca.explained_variance_ratio_

            # Plotting Explained Variance Ratio for Digits Dataset
            fig, ax = plt.subplots(figsize=(8, 3))  # Adjusting the plot size
            bars = ax.barh(range(1, len(explained_variance_digits) + 1), explained_variance_digits, alpha=0.7, color='skyblue')

            # Adding titles and labels with font size adjustments
            ax.set_title('Explained Variance Ratio of Principal Components', fontsize=14)
            ax.set_xlabel('Explained Variance Ratio', fontsize=12)
            ax.set_ylabel('')

            # Adjusting tick labels and their font sizes
            ax.set_yticks(range(1, len(explained_variance_digits) + 1))
            ax.set_yticklabels([f'PC{i}' for i in range(1, len(explained_variance_digits) + 1)], fontsize=10)
            ax.tick_params(axis='y', labelsize=10)  # Y-tick labels font size
            ax.tick_params(axis='x', labelsize=10)  # X-tick labels font size

            # Annotating data labels on the bars
            for bar in bars:
                width = bar.get_width()
                ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', 
                        va='center', ha='left', fontsize=10, color='black')

            plt.tight_layout()  # Adjust layout to avoid label overlap
            st.pyplot(fig)


    # # Summary Section
    # st.header("Summary")
    # st.write(
    #     """
    #     In summary, PCA helps to transform data into a reduced-dimensional space, retaining the maximum possible variance.
    #     Libraries like Scikit-Learn simplify applying PCA, making it an efficient and accessible tool for dimensionality reduction.
    #     """
    # )
