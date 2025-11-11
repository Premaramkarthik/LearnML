# Import necessary libraries
import streamlit as st
from graphviz import Digraph

def run():
    
    # Set page to wide layout
    # st.set_page_config(layout="wide")


    # Add custom CSS to remove padding
    st.markdown("""
        <style>
            .css-18e3th9 {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
            .css-1d391kg, .css-1e5imcs {
                padding: 0;
            }
        </style>
        """, unsafe_allow_html=True)


    # Page title
    st.title("Reinforcement Learning")
    # Introduction section
    st.info("""
    Imagine teaching a dog new tricks. You reward it with treats for performing the trick correctly and ignore it when it fails. Over time, the dog learns to associate the correct actions with rewards, improving its behavior.
    This is akin to Reinforcement Learning, where an agent learns to make decisions by receiving feedback from its actions in the form of rewards or penalties.
    """)


    # Set up layout for two columns
    col1, col2 = st.columns([2, 1])  # Adjust column width ratios as needed


    # Column 1: Explanations
    with col1:


        # Reinforcement Learning Overview
        st.subheader("**What is Reinforcement Learning?**")
        with st.expander("Reinforcement Learning", expanded=True):
            st.write("""
            Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties based on its actions, guiding its learning process to maximize cumulative rewards over time.
            """)


        # How Reinforcement Learning Works
        st.subheader("**How Reinforcement Learning Works**")
        with st.expander("Working of Reinforcement Learning", expanded=True):
            st.markdown("""
            1. **Agent and Environment**: The agent interacts with the environment, taking actions that affect the state of the environment.
            2. **State Representation**: The environment is described by its current state, which the agent can observe.
            3. **Action Selection**: The agent chooses an action based on its policy, which may be random or learned.
            4. **Feedback**: After the action is taken, the environment provides feedback in the form of a reward and the new state.
            5. **Learning**: The agent updates its policy to maximize future rewards based on the feedback received.
            """)


        # Advantages of Reinforcement Learning
        st.subheader("**Advantages of Reinforcement Learning**")
        with st.expander("Advantages", expanded=True):
            st.markdown("""
            - Enables learning optimal actions based on trial and error.
            - Suitable for environments where the optimal solution is not known a priori.
            - Can adapt to changing environments dynamically.
            """)


        # Disadvantages of Reinforcement Learning
        st.subheader("**Disadvantages of Reinforcement Learning**")
        with st.expander("Disadvantages", expanded=True):
            st.markdown("""
            - Requires a large number of interactions to learn effectively.
            - May explore suboptimal actions before finding the best one.
            - Can be computationally intensive and require careful tuning of parameters.
            """)


        # Summary
        st.subheader("**Summary**")
        with st.expander("", expanded=True):
            st.write("""
                     Reinforcement Learning focuses on how agents can learn to navigate complex environments and make decisions based on experience. By balancing exploration of new actions with exploitation of known rewards, agents develop strategies that improve their performance over time. This learning paradigm has applications in various fields, including robotics, gaming, and autonomous systems.            """)


    # Column 2: Flowchart
    with col2:
        # Reinforcement Learning: Dog Fetching Example flowchart
        st.subheader("Flowchart: Dog Fetching Example")
    
        # Create a flowchart using Graphviz
        flowchart = Digraph()


        # Define flowchart nodes
        flowchart.node('A', 'Start Playing Fetch')
        flowchart.node('B', 'Dog Sees the Ball')
        flowchart.node('C', 'Dog Chooses Action\n(Run to Ball / Ignore)')
        flowchart.node('D', 'Dog Runs to Ball')
        flowchart.node('E', 'Dog Ignores Ball')
        flowchart.node('F', 'Dog Brings Ball Back\n+ Receives Treat')
        flowchart.node('G', 'No Reward Given')
        flowchart.node('H', 'Dog Learns Fetching\nis Rewarding Behavior')
        flowchart.node('I', 'Repeat the Process')


        # Define flowchart connections
        flowchart.edges(['AB', 'BC'])
        flowchart.edge('C', 'D', label='Run to Ball')
        flowchart.edge('C', 'E', label='Ignore')
        flowchart.edge('D', 'F')
        flowchart.edge('E', 'G')
        flowchart.edge('F', 'H')
        flowchart.edge('H', 'I')
        flowchart.edge('I', 'B')


        # Render flowchart in Streamlit
        st.graphviz_chart(flowchart)


        # Explanation of the process (optional if space allows)
        st.write("""
        This flowchart visually summarizes how reinforcement learning works in the context of teaching a dog to fetch, emphasizing the key elements of action, reward, and learning.
        """)


