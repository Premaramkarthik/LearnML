import streamlit as st
from sklearn.datasets import make_classification, load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates
from PIL import Image
from sklearn.datasets import make_blobs  # Add this import

#st.set_page_config(layout="wide")

def run():
    
    # Title of the Streamlit app
    st.title("Understanding the Curse of Dimensionality")

    # Introduction section
    st.info("""
    In machine learning, we often work with data that has many features, or dimensions. As the number of features increases, we encounter a set of challenges known as the **Curse of Dimensionality**. This concept describes the difficulties that arise when analyzing high-dimensional data and highlights why it can be tough to build effective machine learning models.
    """)

    col1, col2 = st.columns(2)

    with col1:
            
        # Importance section
        st.subheader("Why It Matters")
        st.write("""
        Understanding the Curse of Dimensionality is crucial for anyone involved in machine learning and data science. It impacts various stages of the modeling process, from data collection and preprocessing to model training and evaluation. Recognizing these challenges allows practitioners to make informed decisions about how to handle high-dimensional data effectively.""")

        # Challenges section
        st.subheader("Challenges of High-Dimensional Data")
        challenges = {
            "1. Data Sparsity": "In high-dimensional spaces, data points become increasingly sparse. This means that as more dimensions are added, the volume of the space increases exponentially, leading to fewer data points being available in any given region. For example, if you consider a one-dimensional line, it’s easy to find points close together. However, as you move to two dimensions (a square) or three dimensions (a cube), the points need to be more widely distributed to fill the space adequately. In higher dimensions, this sparsity makes it challenging to identify patterns or relationships among data points, as nearby points become rare.",
            "2. Increased Computational Complexity": "The computational resources required to process high-dimensional data grow significantly with the addition of each dimension. This is because more dimensions mean more calculations are needed for tasks such as distance measurement and model training. Consequently, training machine learning models becomes more time-consuming and resource-intensive. The amount of data required to make statistically sound predictions also increases exponentially with dimensionality.",
            "3. Model Overfitting": "With an increasing number of features, models can become overly complex and start to 'memorize' noise in the training data instead of identifying generalizable patterns. This phenomenon, known as overfitting, results in poor performance on new, unseen data. Essentially, while a model may perform exceptionally well on its training dataset, it fails to generalize effectively when applied to real-world scenarios.",
            "4. Distance Measurement Challenges": "Many machine learning algorithms rely on distance metrics (like Euclidean distance) to classify or cluster data points. However, in high-dimensional spaces, distances between points tend to become less meaningful as most points are equidistant from each other. This diminishes the effectiveness of algorithms that depend on these distance calculations."
        }

        for challenge, description in challenges.items():
            with st.expander(challenge):
                st.write(description)


        # Conclusion section
        st.subheader("Summary")
        st.write("""
        By exploring these issues, we can better understand the impact of high-dimensional data in machine learning and discover ways to tackle these challenges effectively. Let’s dive into this topic and learn how to navigate the complexities of working with many dimensions!
        """)


    with col2:
        # Function to generate high-dimensional clumpy data
        def generate_data():
            np.random.seed(42)
            X, y = make_blobs(n_samples=100, n_features=25, centers=3, cluster_std=1.5, random_state=42)
            df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(25)])
            df['Cluster'] = y
            return df

        # Generate the high-dimensional clumpy data
        df = generate_data()

        # Create and display the parallel coordinates plot
        fig, ax = plt.subplots(figsize=(12, 7))
        parallel_coordinates(df, class_column='Cluster', color=plt.cm.viridis(np.linspace(0, 1, 3)), alpha=0.7, ax=ax)

        # Rotate x-ticks to 90 degrees for better readability
        plt.xticks(rotation=90)
        plt.title('Parallel Coordinates Plot for High-Dimensional Clumpy Data (25 Features)')
        plt.xlabel('')
        plt.ylabel('')
        plt.grid(True)
        st.pyplot(fig)