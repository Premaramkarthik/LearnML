import streamlit as st
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

# Create tabs for each section
tabs = st.tabs([
    "Home", 
    "Vectors", 
    "Scalars", 
    "Matrices", 
    "Matrix Operations", 
    "Eigenvalues & Eigenvectors", 
    "Next Steps"
])


# Content for the "Home" tab
with tabs[0]:  # Home tab
    st.subheader("Foundation of Linear Algebra")
    st.write("""
    To effectively grasp the role of linear algebra in machine learning, it’s essential to understand several foundational 
    terms. Here, we’ll explore each of these terms, providing definitions, examples, and visual illustrations.
    """)

    
    st.write("""


        In this module, we cover the following key topics:
        - **Vectors**: The building blocks of data representation and manipulation.
        - **Scalars**: Understanding single-value quantities and their role in linear algebra.
        - **Matrices**: Essential tools for representing and transforming data.
        - **Matrix Operations**: Operations like addition, multiplication, and inversion.
        - **Eigenvalues and Eigenvectors**: Core concepts for dimensionality reduction and data analysis.

        We encourage you to explore each of the tabs to gain a deep understanding of these topics and how they are applied in real-world machine learning problems. 

        The **Next Steps** tab will guide you through practical applications and more advanced topics after you have a solid grasp of the basics.
    """)




# Load and display each section based on the tab selected
with tabs[1]:  # Vectors tab
    with open(Path("pages/linear_algebra/vectors.py")) as f:
        exec(f.read())

with tabs[2]:  # Scalars tab
    with open(Path("pages/linear_algebra/scalars.py")) as f:
        exec(f.read())

with tabs[3]:  # Matrices tab
    with open(Path("pages/linear_algebra/matrices.py")) as f:
        exec(f.read())

with tabs[4]:  # Matrix Operations tab
    with open(Path("pages/linear_algebra/matrix_operations.py")) as f:
        exec(f.read())

with tabs[5]:  # Eigenvalues & Eigenvectors tab
    with open(Path("pages/linear_algebra/eigenvalues_eigenvectors.py")) as f:
        exec(f.read())

with tabs[6]:  # Next Steps tab
    with open(Path("pages/linear_algebra/next_steps.py")) as f:
        exec(f.read())
