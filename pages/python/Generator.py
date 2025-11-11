import streamlit as st


if 'code' not in st.session_state:
    st.session_state.code = ''

# Injecting custom CSS into Streamlit for all headers
st.markdown("""
    <style>
        /* General header styling */
        .main-heading {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        .highlight {
            color: #64FFDA;
        }

        /* Applying the same style to all headings (h1, h2, etc.) */
        h1, h2, h3, h4, h5, h6 {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        /* Highlighted part for emphasis */
        h1 span, h2 span, h3 span, h4 span, h5 span, h6 span {
            color: #64FFDA;
        }
        
        /* Custom Primary Color for Streamlit Components */
        .css-1e5b38f {  /* Streamlit button color class */
            background-color: #64FFDA !important;  /* Your custom primary color */
            color: white !important;
        }

        .css-1e5b38f:hover {
            background-color: #64FFDA !important; /* Keep hover effect */
        }

        /* Change link color */
        a {
            color: #64FFDA !important;
        }

        /* Customizing Streamlit sidebar color */
        .css-1l4p5n1 {
            background-color: #64FFDA !important;
        }

        /* Customize selected items and borders */
        .streamlit-expanderHeader {
            color: #64FFDA !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #112240; /* slate teal */
    }
    /* Main page background color */
    .stApp {
        background-color: #0A192F; /* Ivory */
    
    </style>
    """, unsafe_allow_html=True)


st.title("Understanding Generators in Python")

# Introduction
st.header("Introduction")
st.write("""
A **generator** in Python is a special type of iterator that allows you to iterate through a sequence of values. 
Unlike a regular function that returns a single value, a generator can yield multiple values, one at a time, and maintains its state between each yield. 
This makes generators particularly useful for handling large datasets or streams of data without consuming much memory.
""")

# How Generators Work
st.header("How Generators Work")
st.write("""
Generators use the `yield` statement to produce a series of values. When a generator function is called, it returns a generator object, 
but the function body does not execute immediately. Instead, the code runs each time the generator's `__next__()` method is called, 
which is done implicitly in a loop or explicitly with the `next()` function.
""")

# Example of a Generator Function
st.subheader("Example of a Generator Function")
generator_example = """
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Creating a generator object
counter = count_up_to(5)

# Using next() to retrieve values
print(next(counter))  # Outputs 1
print(next(counter))  # Outputs 2
"""
st.code(generator_example, language='python')

st.write("""
In this example, the `count_up_to` function generates numbers from 1 to `n`. 
When called, it returns a generator object that can be iterated over. 
The `yield` statement allows the function to produce a value and pause its execution, maintaining its state until the next value is requested.
You can explicitly retrieve the next value using the `next()` function, which moves the generator to the next yield statement.
""")

# Using next() with Generators
st.header("Using next() with Generators")
st.write("""
The `next()` function retrieves the next value from a generator. 
If the generator is exhausted (meaning there are no more values to yield), calling `next()` will raise a `StopIteration` exception.
""")

next_example = """
# Creating a generator object
counter = count_up_to(3)

# Using next() in a loop
try:
    while True:
        print(next(counter))
except StopIteration:
    print("Generator is exhausted.")
"""
st.code(next_example, language='python')

st.write("""
In this example, the `while True` loop continues to call `next(counter)` until the generator is exhausted, 
at which point the `StopIteration` exception is caught, and a message is printed. 
This demonstrates how you can control the flow of a generator using `next()`.
""")

# Benefits of Generators
st.header("Benefits of Generators")
st.write("""
1. **Memory Efficiency**: Generators produce items one at a time and only when required, which can save memory compared to returning a list of all items at once.
2. **Infinite Sequences**: Generators can represent infinite sequences, such as data streams, without consuming memory for all possible values.
3. **Better Performance**: They can improve performance when processing large data sets since values are generated on-the-fly.
""")

# Example of a Generator Expression
st.subheader("Example of a Generator Expression")
generator_expression_example = """
# Creating a generator expression
squares = (x * x for x in range(10))

# Iterating through the generator expression
for square in squares:
    print(square)
"""
st.code(generator_expression_example, language='python')

st.write("""
Generator expressions are similar to list comprehensions but use parentheses instead of square brackets. 
They provide a concise way to create generators without defining a function.
""")

# Use Case: Reading Large Files
st.header("Use Case: Reading Large Files")
st.write("""
Generators are especially useful for reading large files line by line without loading the entire file into memory at once. 
Here's an example of how to use a generator to read a file:
""")

file_reading_example = """
def read_large_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()

# Usage
for line in read_large_file('large_file.txt'):
    print(line)
"""
st.code(file_reading_example, language='python')

st.write("""
In this example, the `read_large_file` generator reads a file line by line. 
When you iterate over the generator, each line is read and yielded one at a time, making it memory efficient for large files.
""")

# Conclusion
st.header("Conclusion")
st.write("""
Generators are a powerful feature in Python that allow for memory-efficient iteration over sequences of values. 
They are particularly useful for processing large datasets and can greatly simplify the code required for complex iteration logic. 
Understanding how to create and use generators, as well as the role of the `next()` function, can lead to more efficient and Pythonic code.
""")



#
import io
import contextlib
            
st.title('Python Code Executor')
st.write("You can write and execute any Python code in the text area below.")

# Add a text area for the user to input Python code
code_input = st.text_area("Enter your Python code here:")

# Button to execute the code
if st.button("Run Code"):
    # Create a StringIO buffer to capture the output
    buffer = io.StringIO()

    # Try-except block to handle any exceptions during code execution
    try:
        # Redirect stdout to the buffer
        with contextlib.redirect_stdout(buffer):
            exec_globals = {}
            exec(code_input, exec_globals)  # Execute the code entered by the user
    except Exception as e:
        st.error(f"Error: {e}")

    # Display the captured output
    output = buffer.getvalue()
    if output:
        st.subheader("Output:")
        st.text(output)
    else:
        st.write("No output to display.")



