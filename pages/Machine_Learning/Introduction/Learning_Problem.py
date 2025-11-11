# Import necessary libraries
import streamlit as st
from graphviz import Digraph

def run():
    
    # Set page to wide layout
    # st.set_page_config(layout="wide")


    # Add custom CSS to remove padding and make it full-width
    st.markdown("""
        <style>
            .css-18e3th9 { padding-top: 1rem; padding-bottom: 1rem; }
            .css-1d391kg, .css-1e5imcs { padding: 0; }
        </style>
        """, unsafe_allow_html=True)


    # # Page title
    # st.title("Machine Learning Problem Workflow")


    # # Introduction section
    # st.write("""
    # In machine learning, the goal is to approximate an unknown function using a learning process. We use sample data to train a model, allowing the algorithm to make accurate predictions or classify unseen data.
    # This workflow can be broken down into a sequence of elements, which are as follows:
    # """)


    # Layout for two columns: Explanations and Diagram
    col1, col2 = st.columns([2, 1])  # Adjust the ratios as necessary


    # # Column 1: Explanations
    # with col1:




    #     # Unknown Function explanation
    #     st.subheader("**1. Unknown Function**")
    #     st.write("""
    #     The unknown function represents the real-world relationship we aim to model. For instance, in a weather prediction model, the unknown function maps historical weather data to future predictions.
    #     Since we don’t know this function, we need data to approximate it.
    #     """)


    #     # Training Data explanation
    #     st.subheader("**2. Training Data (Sample Data)**")
    #     st.write("""
    #     The training data consists of sample observations that represent the unknown function. It typically includes labeled data (features and labels) used to teach the algorithm about the patterns within the data.
    #     """)


    #     # Hypothesis Set explanation
    #     st.subheader("**3. Hypothesis Set (Set of Models)**")
    #     st.write("""
    #     The hypothesis set includes all potential models that the learning algorithm can choose from. These models range from simple linear models to complex neural networks, depending on the complexity of the problem.
    #     """)


    #     # Learning Algorithm explanation
    #     st.subheader("**4. Learning Algorithm**")
    #     st.write("""
    #     The learning algorithm is the process used to select the best model from the hypothesis set. It analyzes the training data and iteratively refines the model parameters to minimize errors, helping to approximate the unknown function.
    #     """)


    #     # Final Hypothesis explanation
    #     st.subheader("**5. Final Hypothesis**")
    #     st.write("""
    #     The final hypothesis is the resulting model selected by the learning algorithm. It represents the best approximation of the unknown function based on the training data and hypothesis set.
    #     """)


    # # Column 2: Graphviz Flowchart
    # with col2:
    #     # Subheader for the flowchart
    #     st.subheader("ML Workflow Diagram")


    #     # Create a flowchart using Graphviz
    #     flowchart = Digraph()


    #     # Define flowchart nodes
    #     flowchart.node('A', 'Unknown Function')
    #     flowchart.node('B', 'Training Data\n(Sample Data)')
    #     flowchart.node('C', 'Learning Algorithm')
    #     flowchart.node('D', 'Hypothesis Set\n(Set of Models)')
    #     flowchart.node('E', 'Final Hypothesis')


    #     # Define flowchart connections
    #     flowchart.edge('A', 'B')
    #     flowchart.edge('B', 'C')
    #     flowchart.edge('D', 'C')
    #     flowchart.edge('C', 'E')


    #     # Render flowchart in Streamlit
    #     st.graphviz_chart(flowchart)


    #     # Explanation of the process (optional if space allows)
    #     st.write("""
    #     This flowchart visually represents a typical machine learning workflow, emphasizing the key stages and inputs involved in approximating an unknown function.
    #     """)


    # # Set page to wide layout
    # #st.set_page_config(layout="wide")


    st.title("Machine Learning Problem Workflow with Error Evaluation")
    st.write("""
    This Machine Learning workflow describes the process of building and evaluating a model by analyzing both in-sample (Error In) and out-of-sample (Error Out) errors. Each element below contributes to the model’s ability to generalize well to unseen data.
    """)


    # Layout for two columns: Explanations and Diagram
    col1, col2 = st.columns([2, 1])  # Adjust the ratios as necessary


    # Column 1: Explanations
    with col1:


        # Explanations for each step with Error In and Error Out context
        st.subheader("**1. Unknown Function**")
        st.write("""
        The unknown function represents the real-world relationship we aim to model. Since we cannot access this function directly, we approximate it using data and models.
        """)


        st.subheader("**2. Training Data (Sample Data)**")
        st.write("""
        Training data is used to fit the model, minimizing **Error In** to ensure accurate predictions on this data. Low **Error In** alone, however, doesn’t guarantee the model will generalize to unseen data.
        """)


        st.subheader("**3. Hypothesis Set (Set of Models)**")
        st.write("""
        The hypothesis set is a collection of possible models. The learning algorithm evaluates each model’s **Error In** and **Error Out** to select one that balances both, ensuring it’s neither underfit nor overfit.
        """)


        st.subheader("**4. Learning Algorithm**")
        st.write("""
        The learning algorithm optimizes the model by reducing **Error In** and uses validation techniques to estimate **Error Out**. This helps select a model that generalizes well.
        """)


        st.subheader("**5. Final Hypothesis**")
        st.write("""
        The final hypothesis is the chosen model with an acceptable balance of **Error In** and **Error Out**. A well-chosen model minimizes both errors, ensuring good performance on both training and unseen data.
        """)


    # Column 2: Graphviz Flowchart with Error In and Error Out labels
    with col2:
        st.subheader("ML Workflow with Error Evaluation")


        # Create a flowchart using Graphviz
        flowchart = Digraph()


        # Define flowchart nodes
        flowchart.node('A', 'Unknown Function')
        flowchart.node('B', 'Training Data\n(Sample Data)')
        flowchart.node('C', 'Learning Algorithm\n(Error In Minimization)')
        flowchart.node('D', 'Hypothesis Set\n(Set of Models)')
        flowchart.node('E', 'Final Hypothesis\n(Balance Error In & Error Out)')
        flowchart.node('F', 'Estimated Error Out\n(on Unseen Data)')


        # Define flowchart connections
        flowchart.edge('A', 'B')
        flowchart.edge('B', 'C')
        flowchart.edge('D', 'C', label='Input')
        flowchart.edge('C', 'E')
        flowchart.edge('E', 'F')


        # Render flowchart in Streamlit
        st.graphviz_chart(flowchart)


        # Explanation of the process (optional if space allows)
        st.write("""
        This flowchart visually represents an ML workflow with an emphasis on minimizing **Error In** during training and estimating **Error Out** to ensure the model generalizes effectively.
        """)


