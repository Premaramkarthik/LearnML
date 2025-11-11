import streamlit as st


# Title and Overview
st.markdown("<h1>Introduction to Data Analysis</h1>", unsafe_allow_html=True)

# What is Data Analysis?
st.markdown('''### What is Data Analysis?
Data Analysis is the process of inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, drawing conclusions, and supporting decision-making. It is widely used in various industries such as finance, marketing, healthcare, and more.

### Why Learn Data Analysis?
- **Informed Decision-Making**: Enables organizations to make data-driven decisions.
- **Improves Efficiency**: Helps identify process improvements and reduce waste.
- **Predictive Insights**: Allows businesses to anticipate future trends.
- **Competitive Advantage**: Provides a competitive edge by leveraging data insights.
''')

# Key Steps in Data Analysis
st.markdown("<h2>Key Steps in Data Analysis</h2>", unsafe_allow_html=True)

st.markdown('''
The data analysis process typically includes the following steps:

1. **Data Collection**: Gathering relevant data from various sources.
2. **Data Cleaning**: Removing inconsistencies and preparing data for analysis.
3. **Data Exploration**: Exploring data to understand patterns and relationships.
4. **Data Modeling**: Applying statistical methods and machine learning models to draw insights.
5. **Data Interpretation**: Interpreting results and making conclusions.

Each step is essential for producing reliable and actionable insights from the data.
''')

# Data Analysis Tools and Libraries
st.markdown("<h2>Popular Data Analysis Tools and Libraries</h2>", unsafe_allow_html=True)

st.markdown('''### Python Libraries for Data Analysis:
Python offers a variety of libraries that are widely used for data analysis:

- **Pandas**: Ideal for data manipulation and analysis.
- **NumPy**: Provides support for large, multi-dimensional arrays and matrices.
- **Matplotlib & Seaborn**: Libraries for data visualization.
- **SciPy**: Useful for scientific and technical computing.
- **Scikit-Learn**: A popular machine learning library.

### Example Code with Pandas:
Let's load a sample dataset and perform a basic analysis.
''')

# Example Code
example_code = '''
import pandas as pd

# Load a sample dataset
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [88, 92, 85, 91]
})

# Calculate the average score
average_score = data['Score'].mean()
print("Average Score:", average_score)
'''

st.code(example_code, language='python')

# Example Output
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [88, 92, 85, 91]
})

average_score = data['Score'].mean()
st.write("Example Output:")
st.write("Average Score:", average_score)

# Data Visualization Section
st.markdown("<h2>Data Visualization</h2>", unsafe_allow_html=True)

st.markdown('''### Importance of Data Visualization:
Data visualization is a key part of data analysis as it allows us to see trends, patterns, and insights that might not be apparent in raw data.

### Example Visualization:
Using libraries like Matplotlib or Seaborn, we can create visual representations of our data to gain further insights.
''')

# Example Visualization Code
visualization_code = '''
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [88, 92, 85, 91]
})

# Plot a bar chart
plt.figure(figsize=(8, 4))
sns.barplot(x='Name', y='Score', data=data)
plt.title("Scores by Name")
plt.show()
'''

st.code(visualization_code, language='python')

# Summary
st.markdown('''### Summary
Data Analysis is a powerful tool that enables businesses and researchers to gain insights from data, make informed decisions, and drive growth. By following a structured approach to data analysis, using the right tools, and applying visualization techniques, we can uncover valuable information from datasets.

In the following sections, we'll explore advanced topics like machine learning, statistical analysis, and real-world case studies.
''')
