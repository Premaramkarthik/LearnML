from pathlib import Path
import streamlit as st


# Title and Introduction
st.markdown("<h1>Data Manipulation Overview</h1>", unsafe_allow_html=True)

# What is Data Manipulation?
st.markdown('''### What is Data Manipulation?
Data Manipulation involves transforming raw data into a format that is easier to analyze. It includes various operations like cleaning, organizing, and adjusting data to prepare it for analysis.

Effective data manipulation helps:
1. Identify Patterns: Discover trends and insights from data.
2. Clean and Structure: Ensure data quality for accurate analysis.
3. Optimize Data Use: Prepare data for advanced analytics and machine learning.
''')

# Common Data Manipulation Tools
st.markdown("<h2>Popular Data Manipulation Tools</h2>", unsafe_allow_html=True)

st.markdown('''
Some popular Python libraries for data manipulation include:

1. NumPy: Provides support for arrays, matrices, and mathematical functions.
2. Pandas: Used for data manipulation and analysis.
''')

# Navigation to Learn About Tools
st.markdown("### Choose a Tool to Learn More:")

tool_choice = st.selectbox(
    "Select a Data Manipulation Tool",
    ("select", "NumPy", "NumPy Functions",'Pandas', 'Pandas Functions')
)

# Redirect based on selection
if tool_choice == "NumPy":
    with open(Path("pages/dataAnalysis/dataManipulation/numpy.py")) as f:
        exec(f.read())

elif tool_choice == "NumPy Functions":
    with open(Path("pages/dataAnalysis/dataManipulation/numpy_functions.py")) as f:
        exec(f.read())

elif tool_choice == "Pandas":
    with open(Path("pages/dataAnalysis/dataManipulation/pandas.py")) as f:
        exec(f.read())

elif tool_choice == "Pandas Functions":
    with open(Path("pages/dataAnalysis/dataManipulation/pandas_Functions.py")) as f:
        exec(f.read())