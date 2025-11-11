import streamlit as st


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

# Title and Overview
st.markdown("<div class='main-heading'>Introduction to<span class='highlight'> Python Programming</span></div>", unsafe_allow_html=True)

# Introduction to Python
st.markdown('''### What is Python?
Python is a high-level, interpreted programming language with dynamic semantics. It is widely used for:\n
Web development (server-side), Software development, Mathematics, and System scripting.

### Why Learn Python?
**Easy to Read, Learn, and Write**: Python has a simple syntax similar to English, making it easier to learn.\n
**Free and Open-Source**: Python is free to use and distribute, even for commercial use.\n
**High-Level Language**: You do not need to manage memory manually.\n
**Extensive Libraries**: Python has a large number of libraries and frameworks that support various areas of development.\n

### Python's Syntax
Python syntax is simple and easy to follow compared to other programming languages. It emphasizes readability, allowing developers to write less code to achieve the same result.
''')

# Python Example Code
st.markdown('Let’s take a look at a basic Python program:')

example_code = '''
# Example Code
# This is a simple Python program to print "Hello, World!"

print("Hello, World!")
'''

st.code(example_code, language='python')

st.write("Example Output: ")
st.write("Hello, World!")

# Python Variables Section
st.markdown("<div class='main-heading'>Variables in <span class='highlight'>Python</span></div>", unsafe_allow_html=True)

st.markdown('''### What are Variables?
Variables are containers for storing data values in a program. In Python, you do not need to declare the type of the variable, Python automatically knows whether you’re working with a string, an integer, or something else.

### Example of Variables:
Let's assign some values to variables and print them:
''')

variable_code = '''
# Example Code
# Assigning values to variables
name = "John"
age = 25
height = 5.9

# Display the values
print("Name:", name)
print("Age:", age)
print("Height:", height)
'''

st.code(variable_code, language='python')

# Showing output for variable example
name = "John"
age = 25
height = 5.9
st.write("Example Output:")
st.write(f"Name: {name}")
st.write(f"Age: {age}")
st.write(f"Height: {height}")

# Python Data Types
st.markdown("<h2 style='color:#064747;'>Data Types in Python</h2>", unsafe_allow_html=True)

st.markdown('''Python supports various data types such as:
**String**: Text data (`"Hello"`)\n
**Integer**: Whole numbers (`25`)\n
**Float**: Decimal numbers (`5.9`)\n
**Boolean**: True or False values\n

### Example:
Let’s see an example where we assign different data types to variables:
''')

data_types_code = '''
# Example Code
name = "Alice"  # String
age = 30        # Integer
weight = 68.5   # Float
is_student = False  # Boolean

print("Name:", name)
print("Age:", age)
print("Weight:", weight)
print("Is Student:", is_student)
'''

st.code(data_types_code, language='python')

# Showing output for data types example
name = "Alice"
age = 30
weight = 68.5
is_student = False
st.write("Example Output:")
st.write(f"Name: {name}")
st.write(f"Age: {age}")
st.write(f"Weight: {weight}")
st.write(f"Is Student: {is_student}")

# Conclusion
st.markdown('''### Summary
Python is an easy-to-learn, versatile programming language that is widely used for many types of development. Its syntax is clean and readable, making it a great choice for both beginners and experienced developers.

In the next sections, we'll dive deeper into the core concepts of Python, such as loops, functions, and data structures.
''')
