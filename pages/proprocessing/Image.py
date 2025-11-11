import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def run():
    # Initialize session state if not already set
    if "str_input" not in st.session_state:
        st.session_state.str_input = None
    if "str_output" not in st.session_state:
        st.session_state.str_output = None
    
    st.title("Image Preprocessing Techniques")
    st.write("""
    ### Introduction
    This section explores various image preprocessing techniques used in Machine Learning and Computer Vision.
    Each preprocessing step transforms raw image data into a format that models can better understand.
    Select each tab to see how it works on your uploaded image!
    """)

    col1, col2 = st.columns(2)

    # Upload image
    with col2:
        st.write("**Image before preprocessing**: ")
        uploaded_image = st.file_uploader("Upload an image to preprocess", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            # Display original image
            original_image = Image.open(uploaded_image)
            st.image(original_image, caption="Original Image", use_column_width=True)
            image = np.array(original_image)

    # Image Preprocessing functions
    def display_image_processing(image, step, processed_image):
        st.subheader(step)
        st.session_state.str_input = st.image(processed_image, caption=step, use_column_width=True)
    with col1:
        # Tabs for each preprocessing technique
        tabs = st.tabs(["Resizing", "Enhancer", "Brightness Adjustment", "Edge Detection", "Flip Image", "Rotate Image", "Sharpness Adjustment"])

        with tabs[0]:
            st.subheader("Resizing")
            st.write("""
            Resizing changes the dimensions of an image, which can help standardize input sizes for a model.
            """)
            
            # Set new dimensions
            width = st.slider("Width", 50, 500, 200)
            height = st.slider("Height", 50, 500, 200)
            
            if st.checkbox("Apply Resizing") and uploaded_image is not None:
                resized_image = original_image.resize((width, height))
                st.session_state.str_output = display_image_processing(image, "Resized Image", resized_image)

        with tabs[1]:
            st.subheader("Enhance Image")
            st.write("""
            Enhancing an image can adjust its quality by modifying various attributes like contrast, brightness, and sharpness.
            """)
            
            enhancer = st.slider("Enhancement factor", 1.0, 2.0, 1.5)
            if st.checkbox("Enhance Image") and uploaded_image is not None:
                enhancer_image = ImageEnhance.Contrast(original_image).enhance(enhancer)
                st.session_state.str_output = display_image_processing(image, "Enhanced Image", enhancer_image)

        with tabs[2]:
            st.subheader("Adjust Brightness")
            st.write("""
            Brightness adjustment alters the lightness of an image.
            """)
            
            brightness_factor = st.slider("Brightness factor", 0.5, 2.0, 1.0)
            if st.checkbox("Adjust Brightness") and uploaded_image is not None:
                brightness_image = ImageEnhance.Brightness(original_image).enhance(brightness_factor)
                st.session_state.str_output = display_image_processing(image, "Brightness Adjusted", brightness_image)

        with tabs[3]:
            st.subheader("Edge Detection")
            st.write("""
            Edge detection identifies the boundaries within images, useful for identifying structures and contours.
            """)
            
            if st.checkbox("Apply Edge Detection") and uploaded_image is not None:
                # Convert to grayscale for edge detection
                grayscale_image = original_image.convert("L")
                edges = np.array(grayscale_image.filter(ImageFilter.FIND_EDGES))
                st.session_state.str_output = display_image_processing(image, "Edge Detection", edges)

        with tabs[4]:
            st.subheader("Flip Image")
            st.write("""
            Flipping the image horizontally or vertically to augment the dataset.
            """)
            
            flip_choice = st.selectbox("Select Flip Direction", ["Horizontal", "Vertical"])
            if st.checkbox("Flip Image") and uploaded_image is not None:
                if flip_choice == "Horizontal":
                    flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
                else:
                    flipped_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
                st.session_state.str_output = display_image_processing(image, "Flipped Image", flipped_image)

        with tabs[5]:
            st.subheader("Rotate Image")
            st.write("""
            Rotating the image to change the orientation of the object.
            """)
            
            angle = st.slider("Rotation Angle", -180, 180, 0)
            if st.checkbox("Rotate Image") and uploaded_image is not None:
                rotated_image = original_image.rotate(angle)
                st.session_state.str_output = display_image_processing(image, "Rotated Image", rotated_image)

        with tabs[6]:
            st.subheader("Adjust Sharpness")
            st.write("""
            Adjusting the sharpness enhances the details and edges in the image.
            """)
            
            sharpness_factor = st.slider("Sharpness factor", 1.0, 2.0, 1.5)
            if st.checkbox("Adjust Sharpness") and uploaded_image is not None:
                sharpness = ImageEnhance.Sharpness(original_image)
                sharp_image = sharpness.enhance(sharpness_factor)
                st.session_state.str_output = display_image_processing(image, "Sharpness Adjusted", sharp_image)

if __name__ == "__main__":
    run()
