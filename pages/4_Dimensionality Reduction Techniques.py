import streamlit as st
from importlib import import_module


st.set_page_config(
    page_title="Dimensionality Reduction Technique Algorithms in Unsupervised Learning",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 55px;
        background-color: #000000;
        border: none;
        font-weight: bold
        font-size: 1.5em;
    }
    .stButton button:hover {
        background-color: #000000;
        color: #4BFFD6;
    }
    .stButton button:focus {
        background-color: #000000;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Dimensionality Reduction Techniques in Unsupervised Learning 🔍")
st.markdown("### Explore the World of PCA")

# # Custom navigation selection as boxes
# main_selection = st.selectbox(
#     "",
#     ["Overview", "Why DRT?", "PCA", "PCA on Image"]
# )

# # Function to load a selected module
# def load_module(module_name):
#     module = import_module(f"PCA.{module_name}")
#     module.run()

# # Display content based on current page
# st.markdown("---")  # Separator line
# if main_selection == "Overview":
#     load_module("Intro")
# elif main_selection == "Why DRT?":
#     load_module("Why DRT?")
# elif main_selection == "PCA":
#     load_module("Pca_Algorith")
# elif main_selection == "PCA on Image":
#     load_module("PCA_Image")

# Function to load a selected module
def load_module(module_name):
    module = import_module(f"pages.PCA.{module_name}")
    module.run()


# Horizontal Navigation
col1, col2, col3, col4 = st.columns(4)
with col1:
    intro_btn = st.button("Overview")
with col2:
    why_btn = st.button("Why DRT?")
with col3:
    PCA_btn = st.button("PCA")
with col4:
    Img_btn = st.button("PCA on Image")

# Store current page in session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Overview"

# Update current page based on button clicks
if intro_btn:
    st.session_state.current_page = "Overview"
elif why_btn:
    st.session_state.current_page = "Why DRT?"
elif PCA_btn:
    st.session_state.current_page = "PCA"
elif Img_btn:
    st.session_state.current_page = "PCA on Image"


# Display content based on current page
st.markdown("---")  # Separator line
if st.session_state.current_page == "Overview":
    load_module("Intro")
elif st.session_state.current_page == "Why DRT?":
    load_module("Why_DRT")
elif st.session_state.current_page == "PCA":
    load_module("Pca_Algorith")
elif st.session_state.current_page == "PCA on Image":
    load_module("PCA_Image")


