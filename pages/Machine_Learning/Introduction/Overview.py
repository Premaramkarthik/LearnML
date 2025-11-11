import streamlit as st

def run():
    # Set the page configuration
    # st.set_page_config(page_title="Understanding Machine Learning", page_icon="🚀", layout="wide")

    # Title
    st.title("Understanding Machine Learning")

    # Introduction to Machine Learning Section
    with st.expander("Intro to Machine Learning", expanded=True):
        st.subheader("What is Machine Learning?")
        st.write("""
        Machine Learning (ML) is a crucial subset of Artificial Intelligence (AI) that empowers systems to learn from data and improve their performance autonomously, without requiring explicit programming.
        
        As a distinct branch of AI, ML focuses on data-driven learning, enabling applications to adapt and evolve based on the information they process.
        
        ML encompasses various techniques and algorithms that allow computers to identify patterns, make predictions, and take actions based on data.
        
        By leveraging historical data, ML models can uncover hidden insights and trends that might be missed through traditional programming approaches.
        """)

    # Key Aspects of Machine Learning
    with st.expander("Key Aspects of Machine Learning"):
        st.write("""
        - **Data-Driven Insights**: ML relies on vast amounts of data to discover patterns and generate predictions.
        - **Adaptive Learning**: Models continuously refine their performance as they encounter new data.
        - **Automated Decision-Making**: ML algorithms facilitate decisions with minimal human intervention.
        """)

    # Real-World Applications Section
    with st.expander("Real-World Applications of Machine Learning"):
        st.subheader("Real-World Applications of Machine Learning")
        st.write("Here are some impactful uses of Machine Learning across various sectors:")
        st.write("""
        - **Recommendation Systems**: Platforms like Netflix and Amazon leverage ML to provide tailored content suggestions.
        - **Autonomous Vehicles**: Self-driving cars utilize ML algorithms to make real-time driving decisions.
        - **Healthcare**: Machine Learning aids in disease detection by analyzing complex medical data.
        """)

if __name__ == "__main__":
    run()
