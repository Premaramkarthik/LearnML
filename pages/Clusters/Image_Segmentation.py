import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def run():
    # Function for K-Means clustering
    def kmeans_segmentation(image, n_clusters):
        image_array = np.array(image)
        pixels = image_array.reshape(-1, 3)  # Reshape to 2D array
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(pixels)
        segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]
        segmented_image = segmented_pixels.reshape(image_array.shape).astype(np.uint8)
        return segmented_image

    # Streamlit App
    st.title("Image Segmentation Using Clustering")

    st.write("    Image segmentation involves partitioning an image into meaningful regions or segments to simplify its representation and make it more analyzable. Clustering, an unsupervised machine learning technique, is widely used for this purpose because it groups pixels with similar characteristics (like color, intensity, or texture) into segments.")

    # Columns for explanation and interactive segmentation
    col1, col2 = st.columns(2)

    # Column 1: Explanation
    with col1:
        # st.header("Image Segmentation: Explanation")
        st.write("""

        ### Why Use Clustering for Image Segmentation?
        - **Unsupervised Nature**: Clustering does not require labeled data, making it suitable for image segmentation tasks where annotated datasets might not be available.
        - **Similarity Grouping**: It groups pixels based on features like color, intensity, or spatial proximity.
        - **Versatility**: Clustering can be applied to grayscale and colored images, as well as multimodal images (e.g., medical scans).""")

        st.write("""### Key Clustering Techniques for Image Segmentation""")

        # Create tabs
        tabs = st.tabs(["K-Means Clustering", "Hierarchical Clustering", "DBSCAN", "Gaussian Mixture Models (GMM)"])

        # K-Means Clustering Tab
        with tabs[0]:
            st.subheader("K-Means Clustering")
            
            st.markdown("""
            **Steps**:
            - **Feature Extraction**: Represent each pixel as a feature vector. Commonly used features are:
                - RGB values for color images.
                - Intensity values for grayscale images.
                - Additional features like spatial coordinates or texture.
            - **Initialization**: Select K cluster centers randomly.
            - **Assignment**: Assign each pixel to the nearest cluster based on a distance metric (e.g., Euclidean distance).
            - **Update**: Recalculate cluster centroids as the mean of pixels assigned to each cluster.
            - **Convergence**: Repeat the assignment and update steps until the centroids stabilize.
            - **Output**: Pixels in the same cluster are assigned the same label or color, creating distinct regions in the image.

            **Advantages**:
            - Simple and fast.
            - Effective for segmenting images with distinct color or intensity regions.

            **Disadvantages**:
            - Sensitive to the choice of K.
            - May not handle complex images with overlapping color distributions well.
            """)

        # Hierarchical Clustering Tab
        with tabs[1]:
            st.subheader("Hierarchical Clustering")
            
            st.markdown("""
            **Steps**:
            - **Feature Representation**: Represent each pixel as a feature vector.
            - **Linkage**: Calculate the distance between clusters using methods like single linkage, complete linkage, or average linkage.
            - **Merge**: Iteratively merge clusters based on the distance metric until all pixels belong to one cluster.
            - **Output**: Cut the dendrogram at a certain height to obtain the desired number of clusters.

            **Advantages**:
            - Does not require pre-specifying the number of clusters (K).
            - Provides a hierarchy of segmentations.

            **Disadvantages**:
            - Computationally expensive for large images.
            - Sensitive to noise and outliers.
            """)

        # DBSCAN Tab
        with tabs[2]:
            st.subheader("DBSCAN (Density-Based Spatial Clustering of Applications with Noise)")
            
            st.markdown("""
            **Steps**:
            - **Feature Representation**: Represent pixels as feature vectors.
            - **Density Estimation**: Identify core points with a minimum number of neighbors within a specified radius.
            - **Cluster Formation**: Group all points that are density-connected to core points into clusters.
            - **Noise Detection**: Label points that do not belong to any cluster as noise.

            **Advantages**:
            - Detects clusters of arbitrary shape.
            - Handles noise effectively.

            **Disadvantages**:
            - Requires tuning of parameters like the neighborhood radius (eps) and minimum points (minPts).
            - Can be computationally intensive for large images.
            """)

        # Gaussian Mixture Models (GMM) Tab
        with tabs[3]:
            st.subheader("Gaussian Mixture Models (GMM)")
            
            st.markdown("""
            **Steps**:
            - **Feature Representation**: Represent each pixel as a feature vector.
            - **Model Initialization**: Initialize parameters for K Gaussian distributions (means, covariances, and weights).
            - **Expectation-Maximization (EM)**: Iteratively estimate the likelihood of each pixel belonging to a Gaussian and update the parameters.
            - **Segmentation**: Assign pixels to the Gaussian distribution with the highest probability.

            **Advantages**:
            - Models overlapping clusters well.
            - Provides soft assignments, allowing a pixel to partially belong to multiple clusters.

            **Disadvantages**:
            - Requires the number of clusters (K).
            - Computationally intensive.
            """)


        st.write("""
        ### Applications of Image Segmentation Using Clustering
        - **Medical Imaging**: Segmenting tumors or organs in MRI or CT scans.
        - **Remote Sensing**: Identifying land cover types like forests, water bodies, and urban areas in satellite imagery.
        - **Object Detection**: Separating objects from backgrounds in scenes for further processing.
        - **Content-Based Image Retrieval**: Segmenting images into regions for efficient searching and indexing.""")


        st.write("""
        ### Practical Considerations
        - **Feature Selection**: Carefully choose features (color, intensity, texture, spatial coordinates) for better segmentation.
        - **Preprocessing**: Normalize or standardize features to ensure fair clustering.
        - **Postprocessing**: Smoothen segments using morphological operations to reduce noise and refine boundaries.
        - **Cluster Validation**: Evaluate the quality of segmentation using metrics like Dice coefficient, Intersection over Union (IoU), or visual inspection.
        """)

    # Column 2: K-Means Clustering Interactive Demo
    with col2:
        st.header("Interactive K-Means Segmentation")
        uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

        if uploaded_image:
            # Load the image
            image = Image.open(uploaded_image).convert("RGB")
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Slider to select the number of clusters
            n_clusters = st.slider("Select Number of Clusters", min_value=2, max_value=10, value=4)

            # Perform K-Means segmentation
            segmented_image = kmeans_segmentation(image, n_clusters)

            # Display segmented image
            st.image(segmented_image, caption=f"Segmented Image with {n_clusters} Clusters", use_column_width=True)
