import streamlit as st

# Add custom CSS to set text color


# Title and Overview
st.markdown("<h1>Leetcode Questions</h1>", unsafe_allow_html=True)

# Introduction to Leetcode Questions
st.markdown('''### Welcome to the Leetcode Questions Hub
This section provides a collection of coding challenges from Leetcode designed to improve your programming skills. Each problem offers an opportunity to practice and enhance your coding abilities in a structured format.
''')

# What You Can Do
st.subheader("What You Can Do:")
st.markdown("""
- **Explore a Variety of Problems**: Choose from a diverse set of coding challenges that cover various algorithms and data structures.
- **Real-Time Coding Environment**: Use the embedded code editor to write your solution directly in this app.
- **Instant Feedback**: Run your code against test cases and receive immediate feedback.
- **Example Cases**: Each problem includes detailed examples and constraints to help you understand the requirements better.
- **Track Your Progress**: Monitor the challenges you've completed and see your growth as a programmer.
""")

# Getting Started
st.subheader("Getting Started:")
st.markdown("""
Follow these steps to effectively use this hub:
1. **Select a Problem**: Browse through the list of Leetcode questions available.
2. **Read the Problem Statement**: Understand the requirements and constraints before coding.
3. **Write Your Code**: Implement your solution in the provided editor.
4. **Run Your Solution**: Click the 'Run' button to test your implementation.
5. **Revise Your Code**: Use the feedback to refine your solution and retest.
6. **Keep Practicing**: Try different problems to continuously improve your skills.
""")

# Conclusion
st.markdown('''### Summary
This Leetcode Questions Hub is designed to help you practice and master your programming skills. Embrace the challenges and enjoy the journey toward becoming a proficient coder!
''')

