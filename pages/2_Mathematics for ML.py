import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import importlib
from pathlib import Path



# Injecting custom CSS into Streamlit for all headers
st.markdown("""
    <style>
        /* General header styling */
        .main-heading {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        .highlight {
            color: #64FFDA;
        }

        /* Applying the same style to all headings (h1, h2, etc.) */
        h1, h2, h3, h4, h5, h6 {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        /* Highlighted part for emphasis */
        h1 span, h2 span, h3 span, h4 span, h5 span, h6 span {
            color: #64FFDA;
        }
        
        /* Custom Primary Color for Streamlit Components */
        .css-1e5b38f {  /* Streamlit button color class */
            background-color: #64FFDA !important;  /* Your custom primary color */
            color: white !important;
        }

        .css-1e5b38f:hover {
            background-color: #64FFDA !important; /* Keep hover effect */
        }

        /* Change link color */
        a {
            color: #64FFDA !important;
        }

        /* Customizing Streamlit sidebar color */
        .css-1l4p5n1 {
            background-color: #64FFDA !important;
        }

        /* Customize selected items and borders */
        .streamlit-expanderHeader {
            color: #64FFDA !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #112240; /* slate teal */
    }
    /* Main page background color */
    .stApp {
        background-color: #0A192F; /* Ivory */
    
    </style>
    """, unsafe_allow_html=True)



def lengthy_introduction():
    # Custom header using HTML (this is where the style is applied)
    st.markdown("<div class='main-heading'>Linear Algebra: The Foundation of <span class='highlight'>Machine Learning</span></div>", unsafe_allow_html=True)

    # First Column Layout for Text and Image
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("""
        Linear algebra forms the backbone of machine learning and data science, offering the tools necessary to 
        understand and implement algorithms at a mathematical level. It's a language for representing and manipulating data, 
        allowing us to model relationships, optimize functions, and project high-dimensional data into interpretable forms. 
        Whether we are working with simple regression models or complex neural networks, understanding linear algebra 
        empowers us to not only execute but also innovate with algorithms.

        This introduction will explore the importance of linear algebra concepts in data-driven fields. We'll also 
        highlight how linear algebra underpins methods used for data transformation, dimensionality reduction, and even 
        model optimization.
        """)
    with col2:
        st.image("images/img_intro.jpg", caption="Visualization of high-dimensional data.", width=250)

    # Section: Importance of Linear Algebra in ML
    st.write("<h2>Why Linear Algebra is Important in <span class='highlight'>Machine Learning</span></h2>", unsafe_allow_html=True)
    
    # Second Column Layout for Detailed Points and Another Image
    col3, col4 = st.columns([3, 2])
    with col3:
        st.write("""
        Linear algebra enables us to represent data points and features as vectors and matrices, 
        providing a structured way to work with high-dimensional data. When dealing with models, understanding matrices 
        and vectors allows us to perform operations that lead to efficient computation. For instance:
        
        - **Representing Data**: High-dimensional data in ML often comes as matrices, where each row is a data instance 
          and each column represents a feature.
        - **Model Computation**: Calculations, such as those in neural networks, rely heavily on matrix multiplications 
          for processing and propagating information across layers.
        - **Data Transformation**: Techniques like Principal Component Analysis (PCA) utilize matrix decomposition to 
          reduce data dimensions, preserving important information while minimizing noise.
        """)
    with col4:
        st.image("images/img_2.png", caption="Matrix operations in machine learning.", width=250)

    # Concluding Section
    st.write("""
    Throughout this guide, we’ll introduce and explain these terms in detail, with real-world applications and visualizations to solidify each concept.

    As you proceed, remember that linear algebra is more than an abstract subject; it's the bridge between data and 
    meaningful models. The terms, visualizations, and examples provided here will establish a strong foundation for 
    practical applications in machine learning.
    """)


# Wide Variety of Applications
def wide_variety_of_applications(): 
    # st.subheader("Wide Variety of Applications of Linear Algebra in Machine Learning")
    st.write("<h2>Wide Variety of Applications of Linear Algebra in <span class='highlight'>Machine Learning</span></h2>", unsafe_allow_html=True)
    st.image("images/img_3.png", caption="image", use_column_width=True)
    st.write("""
    Linear algebra powers numerous applications in machine learning, from data processing to model building. 
    Below are some key applications, each with an example to illustrate its real-world impact.
    """)

    st.write("### 1. Dimensionality Reduction")
    # st.write("<h2>1. Dimensionality <span class='highlight'>Reduction</span></h2>", unsafe_allow_html=True)

    st.write("""
    **Application**: Dimensionality reduction techniques, such as Principal Component Analysis (PCA), use linear 
    algebra to reduce the number of features in a dataset while preserving essential information.
    
    **Example**: In image processing, PCA helps reduce the dimensionality of pixel data, making it faster and more 
    efficient to train models.
    
    *(Don’t worry if terms like eigenvalues or matrix decompositions seem unfamiliar – we’ll cover these topics in further sessions.)*
    """)

    st.write("### 2. Natural Language Processing (NLP)")
    # st.write("<h2>2. Natural Language Processing <span class='highlight'>(NLP)</span></h2>", unsafe_allow_html=True)

    st.write("""
    **Application**: Linear algebra is used to represent text data as vectors in high-dimensional space, 
    enabling machine learning models to analyze relationships between words, sentences, and documents.
    
    **Example**: Word embeddings like Word2Vec and GloVe use matrix factorization techniques to represent words in 
    a way that similar words are closer in vector space.
    """)

    st.write("### 3. Neural Networks")
    # st.write("<h2>3. Neural <span class='highlight'>Networks</span></h2>", unsafe_allow_html=True)

    st.write("""
    **Application**: Matrix operations are the foundation of neural networks, where weight matrices and activations 
    are multiplied to propagate data through layers.
    
    **Example**: In a neural network’s forward pass, linear transformations are applied to input data, and these 
    transformations are optimized during backpropagation.
    """)

    st.write("### 4. Computer Vision")
    st.write("""
    **Application**: Linear algebra is used in image transformations, such as scaling, rotation, and translation, 
    making it possible to modify images in specific ways for data augmentation.
    
    **Example**: Convolutional neural networks (CNNs) rely on matrix operations to extract features from image data, 
    which are then used to classify or recognize objects.
    """)

    st.write("### 5. Recommendation Systems")
    st.write("""
    **Application**: Matrix factorization, a linear algebra technique, is essential in building recommendation systems, 
    such as those used by Netflix and Amazon.
    
    **Example**: Collaborative filtering uses matrix factorization to predict user preferences based on similar 
    users' past interactions.
    """)
    
    st.write("### 6. Clustering and Classification")
    st.write("""
    **Application**: Linear algebra enables methods like k-means clustering and support vector machines (SVM) to 
    separate and group data points in feature space.
    
    **Example**: In SVM, hyperplanes are defined in vector space to maximize the margin between classes, separating 
    data points for classification.
    """)

    st.write("""
    Each of these applications demonstrates how linear algebra concepts are applied in machine learning, shaping 
    the capabilities of various algorithms. In the upcoming sections, we’ll build on these foundational ideas.
    """)





# Function for Page Title and Introduction
def introduction():
    # st.title("Linear Algebra: The Foundation of Machine Learning")
    st.markdown("<div class='main-heading'>Linear Algebra: The Foundation of <span class='highlight'>Machine Learning</span></div>", unsafe_allow_html=True)

    st.write("""
    Linear algebra is fundamental to understanding and implementing machine learning algorithms. This guide lays out 
    key concepts that form the foundation of linear algebra in the context of ML. Each term is introduced with definitions, 
    examples, and visual aids to solidify your understanding before moving on to applications in machine learning.
    """)

introduction()  





lengthy_introduction()  # Adds the lengthy introduction at the start

wide_variety_of_applications()



# Displays the main introduction
# terms = st.tabs(["Vectors", "Scalars", "Matrices", "Matrix Operations", "Eigenvalues & Eigenvectors"])

# with terms[0]:
#     vectors_section()
# with terms[1]:
#     scalars_section()
# with terms[2]:
#     matrices_section()
# with terms[3]:
#     matrix_operations_section()
# with terms[4]:
#     eigenvalues_eigenvectors_section()
#   # Adds the applications section after foundational terms
# next_steps_section()  # Adds the next steps at the end


# # Create tabs for each section
# tabs = st.tabs([
#     "Home", 
#     "Vectors", 
#     "Scalars", 
#     "Matrices", 
#     "Matrix Operations", 
#     "Eigenvalues & Eigenvectors", 
#     "Next Steps"
# ])


# # Content for the "Home" tab
# with tabs[0]:  # Home tab
#     st.subheader("Foundation of Linear Algebra")
#     st.write("""
#     To effectively grasp the role of linear algebra in machine learning, it’s essential to understand several foundational 
#     terms. Here, we’ll explore each of these terms, providing definitions, examples, and visual illustrations.
#     """)

    
#     st.write("""


#         In this module, we cover the following key topics:
#         - **Vectors**: The building blocks of data representation and manipulation.
#         - **Scalars**: Understanding single-value quantities and their role in linear algebra.
#         - **Matrices**: Essential tools for representing and transforming data.
#         - **Matrix Operations**: Operations like addition, multiplication, and inversion.
#         - **Eigenvalues and Eigenvectors**: Core concepts for dimensionality reduction and data analysis.

#         We encourage you to explore each of the tabs to gain a deep understanding of these topics and how they are applied in real-world machine learning problems. 

#         The **Next Steps** tab will guide you through practical applications and more advanced topics after you have a solid grasp of the basics.
#     """)




# # Load and display each section based on the tab selected
# with tabs[1]:  # Vectors tab
#     with open(Path("pages/linear_algebra/vectors.py")) as f:
#         exec(f.read())

# with tabs[2]:  # Scalars tab
#     with open(Path("pages/linear_algebra/scalars.py")) as f:
#         exec(f.read())

# with tabs[3]:  # Matrices tab
#     with open(Path("pages/linear_algebra/matrices.py")) as f:
#         exec(f.read())

# with tabs[4]:  # Matrix Operations tab
#     with open(Path("pages/linear_algebra/matrix_operations.py")) as f:
#         exec(f.read())

# with tabs[5]:  # Eigenvalues & Eigenvectors tab
#     with open(Path("pages/linear_algebra/eigenvalues_eigenvectors.py")) as f:
#         exec(f.read())

# with tabs[6]:  # Next Steps tab
#     with open(Path("pages/linear_algebra/next_steps.py")) as f:
#         exec(f.read())