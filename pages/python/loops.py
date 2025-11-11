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

# Title and Introduction
st.title('Understanding Loops in Python')

st.markdown('''
**Loops** are a fundamental concept in programming that allow you to execute a block of code multiple times. They are particularly useful for repetitive tasks where the number of iterations is either known beforehand or can change based on certain conditions.

### Why Use Loops?
1. **Efficiency**: Instead of writing the same code multiple times, you can use a loop to run the code as many times as needed. This reduces redundancy and saves time.

2. **Automation**: Loops automate repetitive tasks, making your code cleaner and easier to maintain. You can process large datasets, perform calculations, or generate reports without manually writing each step.

3. **Dynamic Iteration**: Loops can adapt to different situations. For example, you can loop through elements in a list or until a condition is met, making your code flexible and robust.
''')




st.title('Types of loops')
select = ['for loop', 'while loop', ]

select_option = st.selectbox("select",select)

match select_option:
    
    case 'for loop':

        # Title and Introduction
        st.title('For Loops in Python')

        st.markdown('''
        A **for loop** in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or to execute a block of code a specific number of times. It allows you to easily access each element in the sequence and perform operations on it.

        ### The range() Function
        The `range()` function is often used with `for` loops to generate a sequence of numbers. It returns a sequence of numbers starting from the specified number (default is 0) to the specified number (exclusive). You can also specify a step to determine the increment between each number in the sequence.

        ### Syntax of range()
        ```python
        range(start, stop, step)
        ```

        - **start**: The starting value of the sequence (inclusive).
        - **stop**: The ending value of the sequence (exclusive).
        - **step**: The amount by which to increment (default is 1).

        ### Example of Using a For Loop with range()
        Here’s a simple example that uses a `for` loop to print numbers from 0 to 4:
        ''')

        st.code('''
    # Example of for loop using range
    for i in range(5):
        print(i)
        ''')

        st.markdown('''
        **Output:**
        ```
        0
        1
        2
        3
        4
        ```

        ### Example with Custom Start and Step
        You can also customize the start and step values. For example, to print even numbers from 0 to 10:
        ''')

        st.code('''
    # Example of for loop with custom start and step
    for i in range(0, 11, 2):
        print(i)
        ''')

        st.markdown('''
        **Output:**
        ```
        0
        2
        4
        6
        8
        10
        ```

        ### Conclusion
        The `for` loop is a powerful tool in Python that allows you to iterate over sequences easily. The `range()` function is commonly used to specify the number of iterations, making it versatile for various programming tasks.
        ''')

    case 'while loop':
        
        # Title and Introduction
        st.title('While Loops in Python')

        st.markdown('''
        A **while loop** in Python repeatedly executes a block of code as long as a specified condition is `True`. It's useful when you want to repeat an action until a certain condition changes.

        ### Syntax of While Loop
        ```python
        while condition:
            # code to execute
        ```

        - **condition**: A boolean expression that is checked before each iteration. If it evaluates to `True`, the code inside the loop will execute. If it evaluates to `False`, the loop will terminate.

        ### Example of a Basic While Loop
        Here’s a simple example that uses a `while` loop to print numbers from 0 to 4:
        ''')

        st.code('''
    # Example of a basic while loop
    count = 0
    while count < 5:
        print(count)
        count += 1  # Increment count to avoid an infinite loop
        ''')

        st.markdown('''
        **Output:**
        ```
        0
        1
        2
        3
        4
        ```

        ### Infinite Loops
        Be cautious with `while` loops, as it's easy to create an infinite loop if the condition never becomes `False`. For example:
        ''')

        st.code('''
    # Example of an infinite while loop (commented out to prevent execution)
    # count = 0
    # while count < 5:
    #     print(count)  # This will keep printing 0 indefinitely
        ''')

        st.markdown('''
        This loop would continue indefinitely because the value of `count` never changes, making the condition `True` forever. Always ensure to modify the condition within the loop to avoid infinite loops.

        ### Example with User Input
        You can also use `while` loops with user input. Here’s an example where the loop continues until the user enters 'exit':
        ''')

        st.code('''
    # Example of while loop with user input
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("Type 'exit' to stop the loop: ")
        print(f"You typed: {user_input}")
        ''')

        st.markdown('''
        **Conclusion**
        While loops are powerful for situations where the number of iterations is not predetermined. However, always ensure the loop condition will eventually become `False` to avoid infinite loops.
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


