import streamlit as st
from importlib import import_module

# Page configuration
#st.set_page_config(page_title="Understanding Machine Learning", page_icon="🚀", layout="wide")

st.title("Introduction to Machine Learning")



# Custom navigation selection as boxes
main_selection = st.selectbox(
    "",
    ["Overview", "Explicit & Implicit", "Types of ML", "Learning Problem", "Occams Razor"]
)

# Function to load a selected module
def load_module(module_name):
    module = import_module(f"pages.Machine_Learning.Introduction.{module_name}")
    module.run()

# Load the main selection topics or subtopics
if main_selection == "Overview":
    load_module("Overview")

elif main_selection == "Explicit & Implicit":
    load_module("Explicit_Implicit")

elif main_selection == "Types of ML":
    st.write("Machine learning is a powerful technology that enables systems to learn from data, improve their performance over time, and make predictions or decisions without being explicitly programmed.")
    st.write("To effectively harness its potential, machine learning is categorized into several distinct types based on the nature of the data and the objectives of the learning process.")
    st.write("The primary types of machine learning are supervised learning, unsupervised learning, semi-supervised learning, and reinforcement learning. Each type addresses different challenges and is suited to specific kinds of problems, providing a framework for choosing the appropriate approach for various applications.")

    # Subtopic navigation for "Types of ML"
    st.subheader("Select Type of ML")
    ml_type_selection = st.selectbox(
        "",
        ["Supervised", "Unsupervised", "Semi-Supervised", "Reinforcement"])
    
    # Dictionary to map selection to module name
    ml_type_map = {
        "Supervised": "Types.Supervised",
        "Unsupervised": "Types.Unsupervised",
        "Semi-Supervised": "Types.Semi-Supervised",
        "Reinforcement": "Types.Reinforcement"
    }
    
    # Load the selected ML type module
    selected_module = ml_type_map.get(ml_type_selection)
    load_module(selected_module)

elif main_selection == "Learning Problem":
    load_module("Learning_Problem")

elif main_selection == "Occams Razor":
    load_module("Occams Razzor")







###############################
