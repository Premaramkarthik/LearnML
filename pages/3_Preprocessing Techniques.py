import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from importlib import import_module

def load_module(module_name):
    module = import_module(f"pages.{module_name}")
    module.run()

def main():
    # Page config
    st.set_page_config(
        page_title="Preprocessing Techniques",
        page_icon="🛠️",
        layout="wide"
    )
    
    # Custom CSS for horizontal navigation
    st.markdown("""
        <style>
        .stButton button {
            width: 100%;
            border-radius: 10px;
            height: 55px;
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
    st.title("Preprocessing Techniques")
    st.markdown("### Preprocess your data")
    
    # Horizontal Navigation
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        intro_btn = st.button("Introduction")
    with col2:
        Scale_btn = st.button("Scaling & Transformations")
    with col3:
        Encoders_btn = st.button("Categorical Encoders")
    with col4:
        Text_btn = st.button("Text Preprocessing")
    with col5:
        Vecs_btn = st.button("Vectorization & Embeddings")
    with col6:
        Img_bttn = st.button("Image Preprocessing")

    # Store current page in session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Introduction"
    
    # Update current page based on button clicks
    if intro_btn:
        st.session_state.current_page = "Introduction"
    elif Scale_btn:
        st.session_state.current_page = "Scaling & Transformations"
    elif Encoders_btn:
        st.session_state.current_page = "Categorical Encoders"
    elif Text_btn:
        st.session_state.current_page = "Text Preprocessing"
    elif Vecs_btn:
        st.session_state.current_page = "Vectorization & Embeddings"
    elif Img_bttn:
        st.session_state.current_page = "Image Preprocessing"
    
    # Display content based on current page
    st.markdown("---")  # Separator line
    if st.session_state.current_page == "Introduction":
        show_introduction()
    elif st.session_state.current_page == "Scaling & Transformations":
        load_module("proprocessing.Scaling")
    elif st.session_state.current_page == "Categorical Encoders":
        load_module("proprocessing.Encoders")
    elif st.session_state.current_page == "Text Preprocessing":
        load_module("proprocessing.Text")
    elif st.session_state.current_page == "Vectorization & Embeddings":
        load_module("proprocessing.Vectorization")
    elif st.session_state.current_page == "Image Preprocessing":
        load_module("proprocessing.Image")

def show_introduction():
    st.header("What are Preprocessing Techniques?")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        Preprocessing techniques are essential steps in the machine learning workflow, used to prepare data for model training. 
        Raw data often comes with imperfections—like missing values, inconsistent formats, or irrelevant information—that can 
        hinder a model's accuracy and performance. Preprocessing aims to clean, transform, and organize this data into a 
        format suitable for analysis and modeling, ensuring the model can learn effectively.
        
        There are various types of preprocessing methods, including:
        - Data cleaning, which handles missing and inconsistent values
        - Feature scaling, which standardizes or normalizes data to aid model performance
        - Encoding, which transforms categorical data into numerical form
        - Data augmentation, which generates variations to improve model robustness
        """)
    with col2:
        st.success("""
        Why preprocessing is important:
        - Ensures data quality for accurate model training
        - Reduces bias introduced by inconsistent data
        - Helps models generalize better to new data
        """)

    # # with col2:
    # from graphviz import Digraph

    # # Create a flowchart using Graphviz
    # flowchart = Digraph()

    # # Define main node
    # flowchart.node('A', 'Preprocessing Techniques')

    # # Define child nodes for Tabular Data, Text Data, Image Data
    # flowchart.node('B', 'Tabular Data')
    # flowchart.node('C', 'Text Data')
    # flowchart.node('D', 'Image Data')

    # # Define further child nodes for each category
    # flowchart.node('E', 'Scaling')
    # flowchart.node('F', 'Transformations')
    # flowchart.node('G', 'Encodings')

    # flowchart.node('H', 'Tokenization')
    # flowchart.node('I', 'Lowercasing')
    # flowchart.node('J', 'Removing Stopwords')
    # flowchart.node('K', 'Stemming')
    # flowchart.node('L', 'Lemmatization')

    # flowchart.node('M', 'Vectorization Techniques')
    # flowchart.node('N', 'Bag of Words (BoW)')
    # flowchart.node('O', 'Tfidf')
    # flowchart.node('P', 'Word2Vec')
    # flowchart.node('Q', 'GloVe')
    # flowchart.node('R', 'Fast Text')

    # flowchart.node('S', 'Resizing')
    # flowchart.node('T', 'Enhancer')
    # flowchart.node('U', 'Brightness')
    # flowchart.node('V', 'Edge Detection')
    # flowchart.node('W', 'Flip')
    # flowchart.node('X', 'Rotate')
    # flowchart.node('Y', 'Sharpness')

    # # Define flowchart connections
    # flowchart.edge('A', 'B')
    # flowchart.edge('A', 'C')
    # flowchart.edge('A', 'D')

    # flowchart.edge('B', 'E')
    # flowchart.edge('B', 'F')
    # flowchart.edge('B', 'G')

    # flowchart.edge('C', 'H')
    # flowchart.edge('C', 'I')
    # flowchart.edge('C', 'J')
    # flowchart.edge('C', 'K')
    # flowchart.edge('C', 'L')

    # flowchart.edge('C', 'M')
    # flowchart.edge('M', 'N')
    # flowchart.edge('M', 'O')
    # flowchart.edge('M', 'P')
    # flowchart.edge('M', 'Q')
    # flowchart.edge('M', 'R')

    # flowchart.edge('D', 'S')
    # flowchart.edge('D', 'T')
    # flowchart.edge('D', 'U')
    # flowchart.edge('D', 'V')
    # flowchart.edge('D', 'W')
    # flowchart.edge('D', 'X')
    # flowchart.edge('D', 'Y')

    #     # Render flowchart in Streamlit
    # st.graphviz_chart(flowchart)


    from graphviz import Digraph

    # Create a flowchart using Graphviz
    flowchart = Digraph(format='png', engine='dot')

    # Set global graph attributes to improve appearance
    flowchart.attr(dpi='70', size='60,60', ratio='auto', fontname='Helvetica')

    # Define main node with styling
    flowchart.node('A', 'Preprocessing Techniques', shape='ellipse', style='filled', fillcolor='#c6e2ff', fontsize='20', fontweight='bold')

    # Define child nodes for Tabular Data, Text Data, Image Data with styling
    flowchart.node('B', 'Tabular Data', shape='box', style='filled', fillcolor='#ffebcc', fontsize='16', fontweight='bold')
    flowchart.node('C', 'Text Data', shape='box', style='filled', fillcolor='#ffebcc', fontsize='16', fontweight='bold')
    flowchart.node('D', 'Image Data', shape='box', style='filled', fillcolor='#ffebcc', fontsize='16', fontweight='bold')

    # Define further child nodes for each category
    flowchart.node('E', 'Scaling', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('F', 'Transformations', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('G', 'Encodings', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')

    flowchart.node('H', 'Tokenization', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('I', 'Lowercasing', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('J', 'Removing Stopwords', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('K', 'Stemming', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('L', 'Lemmatization', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')

    flowchart.node('M', 'Vectorization Techniques', shape='box', style='filled', fillcolor='#ffe4b5', fontsize='16', fontweight='bold')
    flowchart.node('N', 'Bag of Words (BoW)', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('O', 'Tfidf', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('P', 'Word2Vec', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('Q', 'GloVe', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('R', 'Fast Text', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')

    flowchart.node('S', 'Resizing', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('T', 'Enhancer', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('U', 'Brightness', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('V', 'Edge Detection', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('W', 'Flip', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('X', 'Rotate', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')
    flowchart.node('Y', 'Sharpness', shape='box', style='filled', fillcolor='#f0f8ff', fontsize='14', fontweight='normal')

    # Define flowchart connections
    flowchart.edge('A', 'B', fontsize='14')
    flowchart.edge('A', 'C', fontsize='14')
    flowchart.edge('A', 'D', fontsize='14')

    flowchart.edge('B', 'E', fontsize='14')
    flowchart.edge('B', 'F', fontsize='14')
    flowchart.edge('B', 'G', fontsize='14')

    flowchart.edge('C', 'H', fontsize='14')
    flowchart.edge('C', 'I', fontsize='14')
    flowchart.edge('C', 'J', fontsize='14')
    flowchart.edge('C', 'K', fontsize='14')
    flowchart.edge('C', 'L', fontsize='14')

    flowchart.edge('C', 'M', fontsize='14')
    flowchart.edge('M', 'N', fontsize='14')
    flowchart.edge('M', 'O', fontsize='14')
    flowchart.edge('M', 'P', fontsize='14')
    flowchart.edge('M', 'Q', fontsize='14')
    flowchart.edge('M', 'R', fontsize='14')

    flowchart.edge('D', 'S', fontsize='14')
    flowchart.edge('D', 'T', fontsize='14')
    flowchart.edge('D', 'U', fontsize='14')
    flowchart.edge('D', 'V', fontsize='14')
    flowchart.edge('D', 'W', fontsize='14')
    flowchart.edge('D', 'X', fontsize='14')
    flowchart.edge('D', 'Y', fontsize='14')

    # Render flowchart in Streamlit
    st.graphviz_chart(flowchart)



if __name__ == "__main__":
    main()