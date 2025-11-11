import streamlit as st

#st.set_page_config(layout="wide")

def run():

    # Header for the section
    st.header("Why Dimensionality Reduction?")
    st.info("""
    Dimensionality reduction is a crucial step in the machine learning process. 
    It involves reducing the number of features (or dimensions) in a dataset while preserving its essential information. 
    Here are some key reasons why dimensionality reduction is important:
    """)

    # Create two columns for layout
    col1, col2 = st.columns(2)

    with col1:
        # Simplify Data
        with st.expander("1. Simplify Data", expanded=True):
            st.subheader("Simplify Data")
            st.write("""
            High-dimensional datasets often contain many features, some of which may be irrelevant or redundant. 
            By reducing dimensions, we can eliminate these unnecessary features, which helps to:
            - **Reduce Noise**: Fewer features mean less noise, allowing the model to focus on the core patterns in the data.
            - **Improve Interpretability**: A simpler dataset is easier to understand and analyze, making it more accessible to stakeholders.
            - **Enhance Model Performance**: Simplifying data can lead to better model performance by reducing overfitting.
            """)

        # Improve Efficiency
        with st.expander("2. Improve Efficiency", expanded=True):
            st.subheader("Improve Efficiency")
            st.write("""
            Working with fewer dimensions can significantly enhance computational efficiency. This leads to:
            - **Faster Training Times**: With fewer features, machine learning algorithms can train more quickly, allowing for rapid experimentation.
            - **Lower Resource Requirements**: Reducing dimensions minimizes the amount of memory and processing power needed, making it easier to work with large datasets.
            - **Scalability**: Efficient models can be scaled more easily to larger datasets or real-time applications.
            """)

        # Enhance Visualization
        with st.expander("3. Enhance Visualization", expanded=True):
            st.subheader("Enhance Visualization")
            st.write("""
            Visualizing high-dimensional data can be challenging. Dimensionality reduction allows us to:
            - **Create 2D or 3D Visualizations**: By reducing data to two or three dimensions, we can create plots that make it easier to see patterns and relationships.
            - **Facilitate Exploratory Data Analysis**: Visual tools help us better understand the data, identify trends, and spot anomalies.
            - **Communicate Insights**: Clear visualizations make it easier to communicate findings to non-technical stakeholders.
            """)

        # Closing statement
        st.write("""
        In summary, dimensionality reduction is a vital tool in data analysis and machine learning. By simplifying, 
        optimizing, and visualizing our data more effectively, we can build more efficient and interpretable models.
        """)

    # # Suggested content for col2 (images and visualizations)
    # with col2:
    #     st.image(r"C:\Users\shiva\OneDrive\Desktop\Daily Tasks\Streamlit\DRT before after.png", caption="Example of Dimensionality Reduction Process")

    #     st.write("""
    #     This image shows a hypothetical example of dimensionality reduction. 
    #     - On the left: The high-dimensional dataset with multiple features.
    #     - On the right: The reduced-dimensional dataset visualized in two dimensions, highlighting core patterns.
        
    #     By reducing the dataset dimensions, patterns become easier to detect and analyze, illustrating the power of dimensionality reduction.
    #     """)
