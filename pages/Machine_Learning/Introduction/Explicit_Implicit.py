import streamlit as st

def run():

    # Set the page configuration
    # st.set_page_config(page_title="Explicit Learning vs. Implicit Learning", page_icon="📚", layout="wide")


    # Title
    st.title("Explicit Learning vs. Implicit Learning")


    # Overview section
    st.header("Overview")
    st.write("""
    **Explicit learning** involves the application of predefined rules or heuristics to solve problems, while **implicit learning** allows systems to learn from data without explicit programming. Traditional systems, such as rule-based expert systems, rely on human-crafted logic, which can limit their adaptability.
    """)


    # Intent section
    st.header("Purpose of Understanding These Concepts")
    st.write("""
    Understanding explicit and implicit learning is crucial for:
    - **Developing Adaptive Systems**: Knowing how to implement each approach helps in creating systems that can adapt to changing conditions.
    - **Enhancing User Experience**: Different learning methods can significantly affect user interactions with technology.
    - **Informed Decision Making**: Choosing the right learning model can improve operational efficiency and user satisfaction.
    """)


    # Comparison of Explicit and Implicit Learning
    st.header("Comparison of Explicit and Implicit Learning")
    st.write("""
    | Aspect                   | Explicit Learning                                          | Implicit Learning                                     |
    |--------------------------|----------------------------------------------------------|------------------------------------------------------|
    | **Definition**           | Involves predefined rules and heuristics                 | Learns from data without explicit programming         |
    | **Adaptability**         | Limited, relies on human-crafted logic                    | High, learns from past interactions                   |
    | **Examples**             | Rule-based expert systems, scripted responses             | Machine learning algorithms, adaptive chatbots        |
    | **Pros**                 | Easy to implement and understand                          | Flexible and powerful, handles large datasets         |
    | **Cons**                 | Inflexible, struggles with novel situations               | Requires significant data, can be complex to implement |
    """)


    # Real-World Context
    st.header("Real-World Context")
    st.write("""
    Consider **customer service chatbots**:
    - An **explicit learning** approach would involve scripting specific responses to anticipated questions, ensuring consistency but limiting the chatbot's ability to handle unexpected queries.
    - An **implicit learning** system utilizes past interactions to improve its responses over time, allowing it to adapt to new queries and enhance customer satisfaction and operational efficiency.
    """)


    # Applications of Explicit Learning
    st.header("Applications of Explicit Learning")
    st.write("""
    - **Rule-Based Expert Systems**: Utilized in fields such as healthcare for diagnosis and treatment recommendations.
    - **Static Knowledge Bases**: Effective in environments with little change but can become outdated quickly.
    - **Scripting for FAQs**: Common in customer service, providing standard responses to frequently asked questions.
    """)


    # Applications of Implicit Learning
    st.header("Applications of Implicit Learning")
    st.write("""
    - **Machine Learning Models**: Used in various sectors for predictions and recommendations.
    - **Dynamic Chatbots**: Adapt their responses based on user interactions, improving over time.
    - **Personalized Marketing**: Algorithms learn user preferences to deliver tailored advertisements.
    """)


    # Challenges in Implementing Each Approach
    st.header("Challenges in Implementation")
    st.write("""
    - **Explicit Learning**:
    - Rigidness: Difficult to modify rules once established.
    - Human Error: Dependence on human-crafted rules may introduce biases.


    - **Implicit Learning**:
    - Data Dependency: Requires large datasets for effective learning.
    - Complexity: Can necessitate advanced understanding and technical expertise for implementation.
    """)


    # Conclusion
    st.header("Conclusion")
    st.write("""
    Understanding the distinctions between explicit and implicit learning is vital for developing adaptive systems. While explicit learning provides a structured approach, implicit learning offers flexibility and growth potential, enabling systems to evolve based on real-world data.
    """)


    # Interactive feedback checkbox
    if st.checkbox("Did you find this overview helpful?"):
        st.write("🎉 Thank you for your feedback!")


