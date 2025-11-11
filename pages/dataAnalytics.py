import streamlit as st
from pathlib import Path


#continue break and pass


st.set_page_config(layout="wide")

st.sidebar.title("Data Analytics")

# Initialize session state to store the selected page
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Overview"

# Sidebar selectbox for page navigation with session state
option = st.sidebar.selectbox(
    "Choose a concept", 
    ["Overview","Data Manipulation"],
    key="selected_page"
)

# Refresh the page when a new option is selected
if st.session_state.selected_page != option:
    st.session_state.selected_page = option
    st.experimental_rerun()


#option = st.sidebar.selectbox("Choose a concept", ["Overview", "Variables", "Operators", "Strings", "Lists", "Tuples", "Sets"])

if option == "Overview":
    with open(Path("pages/dataAnalysis/overview.py")) as f:
        exec(f.read())


elif option == "Data Manipulation":
    with open(Path("pages/dataAnalysis/dataManipulation/dataManipulate.py")) as f:
        exec(f.read())  
    

 