
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import IncrementalPCA

#st.set_page_config(layout="wide")

def run():

    st.title("Introduction to PCA for Color Image Compression")
    st.info("""
        **Principal Component Analysis (PCA)** is a dimensionality reduction technique that identifies the most important features within data by projecting it onto a lower-dimensional space. 
        For color images, each pixel in an image corresponds to a 3-dimensional RGB space, and we apply PCA on each color channel (Red, Green, and Blue) separately. 
        This approach allows us to reduce data volume significantly, making it useful for image compression where we aim to reduce file size while retaining essential image features.
    """)


    col1, spacer ,col2 = st.columns([1,0.015,1])

    with col2:
            
        # Section: PCA for Image Data
        st.subheader("Apply PCA on Image")
        st.write("""
            **Principal Component Analysis (PCA)** can be applied to color images by separately compressing the Red, Green, and Blue channels.
            This approach allows us to retain the color details while reducing the image's dimensionality for compression.
            Use the slider below to adjust the number of PCA components and observe how it affects the reconstructed color image.
        """)

        # Step 1: Upload Image
        uploaded_file = st.file_uploader("Choose an image file (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            # Load and display the original color image
            img = Image.open(uploaded_file)
            img = img.resize((250, 250), Image.LANCZOS)  # Resize for faster processing

            # Convert the image to numpy array
            img_np = np.array(img)
            st.subheader("Original Image")
            st.image(img, caption="Original Color Image", use_column_width=False, width=250)


            # Step 2: Select Number of PCA Components
            n_components = st.slider("Select number of PCA components", min_value=1, max_value=200, value=50)
            st.write(f"Selected PCA components: **{n_components}**")

            # Step 3: Apply Incremental PCA to each color channel and calculate variance
            channels_reconstructed = []
            cumulative_variances = []
            explained_variances_all = []

            for i in range(3):  # Loop over R, G, B channels
                channel = img_np[:, :, i].astype('float') / 255.0

                icpca = IncrementalPCA(n_components=n_components)
                transformed = icpca.fit_transform(channel)
                channel_reconstructed = icpca.inverse_transform(transformed)
                channels_reconstructed.append(channel_reconstructed)

                # Calculate cumulative variance for each channel
                pca_full = IncrementalPCA(n_components=100)
                pca_full.fit(channel)
                explained_variance = pca_full.explained_variance_ratio_ * 100
                cumulative_variance = np.cumsum(explained_variance)
                cumulative_variances.append(cumulative_variance)  # Append as array
                explained_variances_all.append(cumulative_variance)

            # Ensure cumulative_variances has arrays for each channel
            avg_variance = np.mean([cum_var[min(n_components - 1, len(cum_var) - 1)] for cum_var in cumulative_variances])
            st.write(f"**Average Variance captured by {n_components} components across RGB channels:** {avg_variance:.2f}%")

            # Step 4: Display Original vs Reconstructed Image
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            ax[0].imshow(img_np)
            ax[0].set_title("Original Image")

            reconstructed_img = np.stack(channels_reconstructed, axis=2)
            reconstructed_img = (reconstructed_img * 255).astype(np.uint8)
            ax[1].imshow(reconstructed_img)
            ax[1].set_title(f"Reconstructed Image ({n_components} Components)")

            st.pyplot(fig)
            
        else:
            st.info("Please upload an image to proceed with PCA.")


    with col1:

        with st.expander("Understanding Channel-Specific PCA for Images",expanded=True):
            st.subheader("Understanding Channel-Specific PCA for Images")
            st.write("""
            When applying PCA to color images, each color channel (Red, Green, and Blue) is treated as a separate 2D array. 
            PCA is then applied to each channel independently, reducing the dimensionality of each channel individually. 
            By preserving the most significant principal components in each channel, we retain the most crucial color and intensity information in the image.

            This method ensures that color balance is preserved while achieving compression. For instance, even with fewer components, the compressed image closely resembles the original.""")

        with st.expander("The Effect of PCA Component Selection on Image Quality",expanded=True):

            st.subheader("The Effect of PCA Component Selection on Image Quality")
            st.write("""
            The number of PCA components selected determines the amount of detail retained in the compressed image. 
            Each additional component adds more information about the image structure and color variance.

            - **Higher Components**: Retaining a high number of components (close to the original dimensions) keeps more of the fine details and color nuances, leading to a high-quality, accurate reconstruction of the original image.
            - **Lower Components**: Using fewer components retains only the most essential features and structures in the image, resulting in a lower-quality but highly compressed version. This may introduce blurring or loss of fine details but significantly reduces data size.""")

        with st.expander("Benefits and Trade-offs of Using PCA for Image Compression",expanded=True):

            st.subheader("Benefits and Trade-offs of Using PCA for Image Compression")
            st.write("""
            - **Efficient Data Reduction**: PCA reduces the amount of information required to represent an image, leading to smaller file sizes and faster processing times.
            - **Feature Extraction**: For applications in computer vision and machine learning, PCA helps in extracting the essential features from images, making it easier to analyze patterns and structures.
            
            **Trade-offs**:
            - **Loss of Fine Details**: Reducing the number of components results in some loss of image details, as only the main structures are retained.
            - **Computation for Large Images**: While PCA is efficient, processing large images with many components may still require significant computation.

            Overall, PCA-based compression is a powerful tool when we want a balance between storage efficiency and quality, making it ideal for preliminary analysis and fast processing.""")


        with st.expander("Final Thoughts",expanded=True):

            st.subheader("Final Thoughts")
            st.write("""
                Principal Component Analysis (PCA) offers a powerful approach to reducing image data while retaining essential details. By applying PCA to each color channel independently, we can significantly compress image data and achieve a balance between quality and storage efficiency.
                
                While PCA does introduce some loss of detail when reducing components, it remains an effective technique for applications that prioritize data reduction and feature extraction, such as in preliminary data analysis, machine learning, and low-storage environments.
                
                - **Versatility**: PCA can be applied beyond traditional data, extending to images and other high-dimensional data.
                - **Quality-Controlled Compression**: With a careful selection of components, PCA allows for customizable compression levels.
                - **Balance of Efficiency and Detail**: PCA is particularly useful for retaining key features without requiring large data storage, making it ideal for scenarios where efficiency is crucial.
                
                We hope this exploration has provided insight into how PCA functions for image compression and its broader applications in data science. Feel free to experiment with the number of components to see firsthand how this trade-off between quality and compression works!
            """)
