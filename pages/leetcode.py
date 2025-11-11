import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

st.sidebar.title("LeetCode Questions")


# Initialize session state to store the selected page
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# Sidebar selectbox for page navigation with session state
option = st.sidebar.selectbox(
    "Choose a concept", 
    ["Home", "Easy Problems", "Intermediate Problems"],
    key="selected_page"
)

# Refresh the page when a new option is selected
if st.session_state.selected_page != option:
    st.session_state.selected_page = option
    st.experimental_rerun()




if option == "Home":
    with open(Path("pages/Leetcode/home.py")) as f:
        exec(f.read())
elif option == "Easy Problems":
    with open(Path("pages/Leetcode/easy.py")) as f:
        exec(f.read())
elif option == "Intermediate Problems":
    with open(Path("pages/Leetcode/Intermediate.py")) as f:
        exec(f.read())
