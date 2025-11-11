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

import copy


# Title and Introduction
st.title('Conditional Statements in Python')

st.markdown('''
Conditional statements in Python allow you to execute certain pieces of code based on specific conditions. The primary conditional statements are **if**, **elif**, and **else**. They help in decision-making in your code.

## 1. If Statement
The `if` statement evaluates a condition and executes a block of code if the condition is `True`.

### Syntax:
```python
if condition:
    # block of code
```

### Example:
''')

st.code('''
# Example of if statement
age = 20
if age >= 18:
print("You are eligible to vote.")
''')

st.markdown('''
**Output:**
```
You are eligible to vote.
```

## 2. Elif Statement
The `elif` (short for "else if") statement allows you to check multiple expressions for `True` and execute a block of code as soon as one of the conditions is `True`.

### Syntax:
```python
if condition1:
    # block of code
elif condition2:
    # block of code
```

### Example:
''')

st.code('''
# Example of elif statement
score = 85
if score >= 90:
print("Grade: A")
elif score >= 80:
print("Grade: B")
elif score >= 70:
print("Grade: C")
else:
print("Grade: D")
''')

st.markdown('''
**Output:**
```
Grade: B
```

## 3. Else Statement
The `else` statement executes a block of code when the condition(s) in the `if` and `elif` statements are `False`.

### Syntax:
```python
if condition:
    # block of code
else:
    # block of code
```

### Example:
''')

st.code('''
# Example of else statement
temperature = 30
if temperature > 35:
print("It's a hot day.")
else:
print("It's not a hot day.")
''')

st.markdown('''
**Output:**
```
It's not a hot day.
```

## 4. Nested Conditional Statements
You can also nest conditional statements to check multiple conditions.

### Example:
''')

st.code('''
# Example of nested conditional statements
num = 10
if num >= 0:
if num == 0:
    print("The number is zero.")
else:
    print("The number is positive.")
else:
print("The number is negative.")
''')

st.markdown('''
**Output:**
```
The number is positive.
```

## 5. Ternary Operator
Python also has a shorthand way to write conditional statements called the **ternary operator**.

### Syntax:
```python
value_if_true if condition else value_if_false
```

### Example:
''')

st.code('''
# Example of ternary operator
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)
''')

st.markdown('''
**Output:**
```
Odd
```

## Conclusion
Conditional statements are fundamental in programming. They allow you to control the flow of your program based on conditions and user inputs. Mastering these statements is essential for developing complex logic in your applications.
''')


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



