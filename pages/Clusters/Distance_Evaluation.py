def run():
    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.neighbors import NearestNeighbors
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.datasets import make_blobs

    # Helper function to generate random data
    def generate_data(n_samples=300, centers=4, cluster_std=0.60):
        X, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=42)
        return X

    st.title("Distance Metrics Visualization")

    st.info("Distance metrics are essential in many machine learning algorithms to quantify the similarity or dissimilarity between data points. These metrics are used in clustering, classification, and other tasks to determine how close or far apart points are in a feature space.")

    # Generate synthetic data
    X = generate_data(n_samples=100)

    # Create tabs and unpack them into variables
    tab_euclidean, tab_manhattan, tab_minkowski, tab_cosine = st.tabs(["Euclidean", "Manhattan", "Minkowski", "Cosine"])

    # Euclidean Tab
    with tab_euclidean:
        col1, spacer, col2 = st.columns([1, 0.06, 1])

        with col2:
            st.image('pages/clusterImages/Euclidean.png',width=600)

        with col1:
            st.write("### Understanding Euclidean Distance")
            st.write("""
            *Euclidean Distance* is the straight-line distance between two points in Euclidean space.
            """)
            st.write("### Understanding Euclidean Distance")

            st.write("""
            Euclidean Distance is a fundamental metric in mathematics that measures the straight-line distance between two points in Euclidean space. 
            It is commonly used in various fields such as geometry, physics, and machine learning, representing the shortest path connecting two points.

            **Mathematical Definition**  
            The Euclidean distance between two points \( A \) and \( B \) in a two-dimensional space is defined as follows:
            """)

            # Using st.latex to render the formula for 2D
            st.latex(r'd(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')

            st.write("""
            Where:
            - \( A = (x_1, y_1) \) and \( B = (x_2, y_2) \) are the coordinates of the two points.
            
            In an n-dimensional space, the formula generalizes to:
            """)

            # Using st.latex to render the formula for n-dimensional space
            st.latex(r'd(X, Y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}')

            st.write("""
            Where:
            - \( X = (x_1, x_2, \ldots, x_n) \) and \( Y = (y_1, y_2, \ldots, y_n) \).

            **Key Characteristics**  
            - **Non-Negativity**: The distance is always zero or positive; thus, \( d(A, B) \geq 0 \).
            - **Identity**: The distance between identical points is zero; hence, \( d(A, A) = 0 \).
            - **Symmetry**: The distance from point \( A \) to point \( B \) equals the distance from point \( B \) to point \( A\); that is, \( d(A, B) = d(B, A) \).
            - **Triangle Inequality**: For any three points \( A, B, C \), the relationship holds that \( d(A, C) \leq d(A, B) + d(B, C).

            **Advantages of Euclidean Distance**  
            - **Simplicity**: It is easy to compute and understand intuitively.
            - **Geometric Interpretation**: It aligns well with our natural understanding of space and distances.
            - **Widely Used**: It serves as a fundamental building block for many algorithms in clustering (like K-Means), classification (like K-Nearest Neighbors), and regression.

            **Limitations to Consider**  
            - **Sensitivity to Scale**: Euclidean distance is sensitive to the scale of the data. Features with larger ranges can disproportionately influence the distance calculation. Normalization or standardization may be required.
            - **High-Dimensionality Challenges**: In high-dimensional spaces (often referred to as the "curse of dimensionality"), all points tend to become equidistant from each other, making Euclidean distance less effective.
            - **Outliers**: The metric can be heavily influenced by outliers since it squares the differences; thus, large deviations can significantly affect the overall distance.

            **Practical Applications**  
            - **Clustering Algorithms**: Used extensively in clustering methods like K-Means where centroid calculations rely on Euclidean distances.
            - **Image Processing**: In image recognition tasks where pixel intensity values are compared.
            - **Machine Learning Models**: Often used in algorithms like K-Nearest Neighbors (KNN) for classification tasks.
            - **Geospatial Analysis**: Measuring distances between geographical locations on a map.

            In summary, Euclidean Distance is a foundational metric that plays a crucial role in data analysis and machine learning due to its intuitive nature and effectiveness across various applications.
            """)

    # Manhattan Tab
    with tab_manhattan:
        col1, spacer, col2 = st.columns([1, 0.06, 1])

        with col2:
            st.image('pages/clusterImages/Manhattan.png',width=600)

        with col1:
            st.write("### Understanding Manhattan Distance")
            st.write("""
            *Manhattan Distance* measures distance as the sum of absolute differences across dimensions.
            """)
            st.write("### Understanding Manhattan Distance")
        
            st.write("""
            **What is Manhattan Distance?**  
            Manhattan Distance, also known as Taxicab Distance or City Block Distance, measures the distance between two points in a grid-like layout. 
            This metric is particularly useful in scenarios where movement is restricted to horizontal and vertical paths, resembling how a taxi would navigate through city streets.

            **Mathematical Definition**  
            The Manhattan distance between two points \( A \) and \( B \) in a two-dimensional space is defined as follows:
            """)

            # Using st.latex to render the formula for 2D
            st.latex(r'd(A, B) = |x_2 - x_1| + |y_2 - y_1|')

            st.write("""
            Where:
            - \( A = (x_1, y_1) \) and \( B = (x_2, y_2) \) are the coordinates of the two points.
            
            In an n-dimensional space, the formula generalizes to:
            """)

            # Using st.latex to render the formula for n-dimensional space
            st.latex(r'd(X, Y) = \sum_{i=1}^{n} |x_i - y_i|')

            st.write("""
            Where:
            - \( X = (x_1, x_2, \ldots, x_n) \) and \( Y = (y_1, y_2, \ldots, y_n) \).

            **Key Characteristics**  
            - **Non-Negativity**: The distance is always zero or positive; thus, \( d(A, B) \geq 0 \).
            - **Identity**: The distance between identical points is zero; hence, \( d(A, A) = 0 \).
            - **Symmetry**: The distance from point \( A \) to point \( B \) equals the distance from point \( B \) to point \( A\); that is, \( d(A, B) = d(B, A) \).
            - **Triangle Inequality**: For any three points \( A, B, C \), the relationship holds that \( d(A, C) \leq d(A, B) + d(B, C).

            **Advantages of Manhattan Distance**  
            - **Simplicity**: Easy to compute and understand intuitively.
            - **Robustness in High Dimensions**: Unlike Euclidean distance, it does not amplify differences between features due to squaring values. This makes it particularly effective in high-dimensional datasets.
            - **Less Sensitive to Outliers**: Since it sums absolute differences rather than squaring them, it is less affected by outliers compared to Euclidean distance.

            **Limitations to Consider**  
            - **Grid-Like Assumption**: It assumes movement along grid lines; thus, it may not be suitable for all types of data distributions.
            - **Dimensionality Issues**: While it performs well in high dimensions, the curse of dimensionality can still impact its effectiveness in distinguishing between close and distant points.

            **Practical Applications**  
            - **Machine Learning Algorithms**: Frequently used in classification algorithms like K-Nearest Neighbors (KNN), where distances are calculated to classify test data based on training data.
            - **Urban Navigation Systems**: Employed in routing algorithms for delivery services that operate within grid-like city layouts (e.g., optimizing delivery routes).
            - **Data Analysis**: Useful in various statistical analyses where absolute differences are more meaningful than squared differences.

            In summary, Manhattan Distance is a versatile metric that plays a crucial role in various applications across machine learning and data analysis. Its intuitive nature and robustness make it a preferred choice when dealing with high-dimensional data or grid-like structures.
            """)


    # Minkowski Tab
    with tab_minkowski:
        col1, spacer, col2 = st.columns([1, 0.06, 1])

        with col2:
            st.image('pages/clusterImages/Minkowski.png',width=600)

        with col1:
            st.write("### Understanding Minkowski Distance")
            st.write("""
            *Minkowski Distance* is a generalized metric that encompasses both Euclidean and Manhattan distances.
            """)
            st.write("### Understanding Minkowski Distance")

            st.write("""
            Minkowski Distance is a versatile metric used to measure the distance between two points in a normed vector space. 
            It generalizes both Euclidean and Manhattan distances, making it adaptable for various applications depending on the parameter \( p \). 
            Named after the mathematician Hermann Minkowski, this distance metric is particularly useful in machine learning and data analysis.

            **Mathematical Definition**  
            The Minkowski distance between two points \( X \) and \( Y \) in an n-dimensional space is defined as follows:
            """)

            # Using st.latex to render the formula
            st.latex(r'D(X, Y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{\frac{1}{p}}')

            st.write("""
            Where:
            - \( X = (x_1, x_2, \ldots, x_n) \) and \( Y = (y_1, y_2, \ldots, y_n) \) are two points in n-dimensional space.
            - \( p \) is a parameter that determines the type of distance being calculated.

            **Key Characteristics**  
            - **Non-Negativity**: The distance is always zero or positive; thus, \( D(X, Y) \geq 0 \).
            - **Identity**: The distance between identical points is zero; hence, \( D(X, X) = 0 \).
            - **Symmetry**: The distance from point \( X \) to point \( Y \) equals the distance from point \( Y \) to point \( X\); that is, \( D(X, Y) = D(Y, X) \).
            - **Triangle Inequality**: For any three points \( X, Y, Z \), the relationship holds that \( D(X, Z) \leq D(X, Y) + D(Y, Z) \).
                        
                     
            **Parameter Variations**  
            - When \( p = 1\), the Minkowski distance becomes the **Manhattan Distance**, which measures the sum of absolute differences.
            - When \( p = 2\), it corresponds to the **Euclidean Distance**, which measures the straight-line distance.
            - As \( p \) approaches infinity, it converges to the **Chebyshev Distance**, which measures the maximum absolute difference across dimensions.

                     
            **Advantages of Minkowski Distance**  
            - **Flexibility**: The ability to adjust the parameter \( p \) allows for tailored distance calculations based on specific data characteristics and requirements.
            - **Generalization**: It encompasses both Manhattan and Euclidean distances as special cases, making it versatile for various applications.
            - **Applicability in High Dimensions**: It can be effectively used in high-dimensional spaces where other metrics might struggle.

            **Limitations to Consider**  
            - **Sensitivity to Outliers**: Depending on the value of \( p\), large differences can disproportionately influence the distance calculation.
            - **Choice of Parameter**: Selecting an appropriate value for \( p\) can significantly impact results; incorrect choices may lead to misleading interpretations.

            **Practical Applications**  
            - **Machine Learning Algorithms**: Commonly used in clustering and classification algorithms like K-Nearest Neighbors (KNN), where different values of \( p\) can yield different clustering behaviors.
            - **Data Analysis**: Useful for measuring similarity between data points in numerical datasets where various metrics might be applicable based on context.
            - **Pattern Recognition**: Employed in image processing and computer vision tasks to compare feature vectors effectively.

            In summary, Minkowski Distance is a powerful and adaptable metric that plays a crucial role in data analysis and machine learning. 
            Its ability to generalize other distance metrics makes it a valuable tool for understanding relationships between data points across diverse applications.                     
                     
                     """)

    # Cosine Tab
    with tab_cosine:
        col1, spacer, col2 = st.columns([1, 0.06, 1])

        with col2:
            st.image('pages/clusterImages/Cosine.png',width=600)

        with col1:
            st.write("### Understanding Cosine Similarity")

            st.write("""
            **What is Cosine Similarity?**  
            Cosine Similarity is a measure of similarity between two non-zero vectors that calculates the cosine of the angle between them. It is commonly used in text analysis, recommendation systems, and clustering tasks where the orientation (or direction) of vectors is more significant than their magnitude.

            **Mathematical Definition**  
            The cosine similarity between two vectors \( A \) and \( B \) is defined as follows:
            """)

            # Using st.latex to render the formula
            st.latex(r'\text{cosine}(A, B) = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \cdot \sqrt{\sum_{i=1}^{n} B_i^2}}')

            st.write("""
            Where:
            - \( A \) and \( B \) are vectors in n-dimensional space.
            - Cosine similarity values range between -1 and 1, where 1 means identical orientation, -1 means opposite, and 0 means orthogonality (no similarity).

            **Key Characteristics**  
            - **Orientation-Focused**: It measures the angle, not the distance, making it ideal for high-dimensional data like text.
            - **Range**: The similarity score is bounded between -1 and 1.
            
            **Advantages of Cosine Similarity**  
            - **Magnitude Independence**: Focuses on direction, ignoring vector magnitude, which is useful in text and document similarity tasks.
            - **Effective in High Dimensions**: Works well with high-dimensional data and sparse matrices.
            
            **Limitations to Consider**  
            - **Not a True Distance Metric**: Cosine similarity does not satisfy the properties of a distance metric, such as the triangle inequality.
            - **Zero Vectors**: Not applicable if either vector has zero magnitude.

            **Practical Applications**  
            - **Text Mining**: Used in text similarity for document and sentence comparisons.
            - **Recommendation Systems**: Frequently used in collaborative filtering techniques for recommendations.
            - **Image Analysis**: Useful in cases where vector orientation is more meaningful than distance.

            In summary, Cosine Similarity is essential in scenarios where orientation matters more than distance, particularly in text and high-dimensional vector spaces.
            """)
