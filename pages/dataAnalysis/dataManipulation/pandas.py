import streamlit as st
import numpy as np

if 'code' not in st.session_state:
    st.session_state.code = ''


st.title("Comprehensive Guide to Pandas")

# Introduction
st.header("Introduction")
st.write("""
**Pandas** is a versatile and widely-used library in Python for data manipulation and analysis. 
It provides efficient and easy-to-use data structures for working with structured data.

The core data structures in Pandas are:
- **Series**: A one-dimensional labeled array, ideal for handling single columns of data.
- **DataFrame**: A two-dimensional labeled data structure, perfect for tabular data like spreadsheets or databases.
""")

# Key Features
st.header("Key Features of Pandas")
st.write("""
Pandas offers a wide range of features that make it an indispensable tool for data analysis:
- **Data Manipulation**: Effortlessly handle missing data, filter rows/columns, and transform datasets.
- **Data Aggregation**: Perform operations like grouping and summarizing data.
- **Data Cleaning**: Detect and correct errors, and handle inconsistencies in data.
- **File Handling**: Read from and write to multiple formats, including CSV, Excel, SQL, and JSON.
- **Integration**: Works seamlessly with other libraries like NumPy, Matplotlib, and Scikit-learn.
""")

# Why Use Pandas?
st.header("Why Use Pandas?")
st.write("""
Pandas simplifies the process of working with structured data, enabling you to focus on insights rather than implementation details. 
Here’s why it stands out:
- **Efficiency**: Optimized for performance with built-in methods for fast computations.
- **Flexibility**: Works well for small datasets and large datasets alike.
- **Accessibility**: Offers user-friendly methods to handle complex data manipulations.
""")

# Use Cases
st.header("Use Cases of Pandas")
st.write("""
Pandas is commonly used in various fields and industries, including:
- **Data Analysis**: Explore and analyze data patterns, trends, and outliers.
- **Data Engineering**: Prepare datasets for machine learning models by cleaning and transforming data.
- **Business Intelligence**: Generate insights from business data for decision-making.
- **Scientific Research**: Analyze experimental data and statistical computations.
""")

# Components of Pandas
st.header("Core Components of Pandas")
st.write("""
Pandas relies on two main data structures to handle and manipulate data effectively:
- **Series**: One-dimensional labeled array.
- **DataFrame**: Two-dimensional labeled data structure with rows and columns.

These structures are designed to handle diverse data types and can be easily integrated into other workflows.
""")

# Benefits of Using Pandas
st.header("Benefits of Using Pandas")
st.write("""
- **Ease of Use**: High-level functions abstract away the complexity of handling structured data.
- **Rich Ecosystem**: Extensive support for other Python libraries and frameworks.
- **Robustness**: Handles missing data gracefully and supports various indexing options.
""")

# Conclusion
st.header("Conclusion")
st.write("""
Pandas is an essential tool for anyone working with data in Python. Its comprehensive features, user-friendly syntax, 
and seamless integration with the Python ecosystem make it ideal for tasks ranging from simple data exploration 
to advanced data analysis workflows.

Whether you are a beginner or an experienced data professional, mastering Pandas will significantly enhance your ability 
to work with and understand data.
""")

st.title('About Series and DataFrame')

with st.expander('Series and DataFrame', expanded= False):
    import streamlit as st
    import pandas as pd

    # App Title
    st.title("Understanding Pandas: Series and DataFrame")
    
    # Introduction Section
    st.header("Introduction to Pandas")
    st.write("""
    **Pandas** is a Python library designed for data manipulation and analysis. 
    At its core are two key data structures:
    - **Series**: A one-dimensional labeled array, similar to a list or column in a spreadsheet.
    - **DataFrame**: A two-dimensional labeled data structure, like a table or spreadsheet.
    
    Let's dive into these structures to understand how they work and why they are so powerful.
    """)

    # Series Section
    st.header("Pandas Series")
    st.write("""
    A **Series** is essentially a one-dimensional array with labels (called index). 
    Each element in the Series is associated with an index, allowing for easy access and manipulation.
    """)

    # Series Syntax
    st.subheader("Syntax for Creating a Series")
    st.code("""
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40]
series = pd.Series(data)
""", language="python")

    # Series Example
    st.subheader("Example: Creating a Series")
    st.write("Here’s an example of how a Series looks:")
    data = [10, 20, 30, 40]
    series = pd.Series(data)
    st.write(series)

    st.write("""
    Notice that each value in the Series is associated with an index. By default, the index starts from 0.
    """)

    # DataFrame Section
    st.header("Pandas DataFrame")
    st.write("""
    A **DataFrame** is a two-dimensional labeled data structure with rows and columns. 
    Think of it as a table where:
    - Rows have unique labels (index).
    - Columns can have unique names.
    DataFrames are incredibly flexible and are the most widely used data structure in Pandas.
    """)

    # DataFrame Syntax
    st.subheader("Syntax for Creating a DataFrame")
    st.code("""
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)
""", language="python")

    # DataFrame Example
    st.subheader("Example: Creating a DataFrame")
    st.write("Here’s an example DataFrame:")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 95]
    }
    df = pd.DataFrame(data)
    st.write(df)

    st.write("""
    Notice that each column has a name, and each row has an index. This structure makes it easy to manipulate 
    and analyze data.
    """)

    # Key Operations Section
    st.header("Key Operations on Series and DataFrame")
    st.subheader("Accessing Data in a Series")
    st.write("You can access elements of a Series using their index:")
    st.code("""
# Accessing elements in a Series
print(series[0])  # Output: 10
print(series[1])  # Output: 20
""", language="python")

    st.subheader("Accessing Data in a DataFrame")
    st.write("You can access columns or rows in a DataFrame:")
    st.code("""
# Accessing a column
print(df['Name'])  # Output: ['Alice', 'Bob', 'Charlie']

# Accessing a row by index
print(df.loc[0])   # Output: Name: Alice, Age: 25, Score: 85
""", language="python")

    # Conclusion Section
    st.header("Conclusion")
    st.write("""
    - **Series**: Great for handling one-dimensional data with labels.
    - **DataFrame**: Ideal for two-dimensional, tabular data.
    
    These structures are the foundation of Pandas and provide the flexibility to manipulate and analyze data efficiently. 
    Start experimenting with them to unlock the power of Pandas!
    """)

