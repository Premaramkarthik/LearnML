import streamlit as st
from importlib import import_module


st.set_page_config(
    page_title="Clustering Techniques in Unsupervised Learning",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for horizontal navigation
st.markdown("""
    <style>
    .stButton button {
        width: 105%;
        border-radius: 10px;
        height: 65px;
        background-color: #000000;
        border: none;
        font-weight: bold;
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
st.title("Clustering Techniques in Unsupervised Learning")
st.markdown("### Explore the Techniques of Clustering")

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
    module = import_module(f"pages.Clusters.{module_name}")
    module.run()


# Horizontal Navigation
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    intro_btn = st.button("Overview")
with col2:
    Type_btn = st.button("Types")
with col3:
    Alg_btn = st.button("Algorithms")
with col4:
    Dst_btn = st.button("Distance Metrics")
with col5:
    Img_btn = st.button("Cluster Metrics")
with col6:
    Clst_btn = st.button("Cluster Analysis")
with col7:
    Img_seg = st.button("Image Segmentation")
with col8:
    Smy_btn = st.button("Summary")



# Store current page in session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Overview"


# Update current page based on button clicks
if intro_btn:
    st.session_state.current_page = "Overview"
elif Type_btn:
    st.session_state.current_page = "Types"
elif Alg_btn:
    st.session_state.current_page = "Algorithms"
elif Dst_btn:
    st.session_state.current_page = "Distance Metrics"
elif Clst_btn:
    st.session_state.current_page = "Cluster Analysis"
elif Img_btn:
    st.session_state.current_page = "Cluster Metrics"
elif Img_seg:
    st.session_state.current_page = "Image Segmentation"
elif Smy_btn:
    st.session_state.current_page = "Summary"


# Display content based on current page
st.markdown("---")  # Separator line
if st.session_state.current_page == "Overview":
    load_module("Intro")
elif st.session_state.current_page == "Types":
    load_module("Types")
elif st.session_state.current_page == "Algorithms":
    load_module("Algorithms")
elif st.session_state.current_page == "Distance Metrics":
    load_module("Distance_Evaluation")
elif st.session_state.current_page == "Cluster Metrics":
    load_module("Cluster_Metrics")
elif st.session_state.current_page == "Cluster Analysis":
    load_module("Cluster_Analysis")
elif st.session_state.current_page == "Image Segmentation":
    load_module("Image_Segmentation")
elif st.session_state.current_page == "Summary":
    load_module("Summary")




