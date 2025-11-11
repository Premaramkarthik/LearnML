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


st.title("Control Flow Statements: continue, break, and pass in Python")

# Introduction
st.header("Introduction")
st.write("""
In Python, the `continue`, `break`, and `pass` statements are control flow tools that help you manage loops and conditionals more effectively. 
Each has a specific purpose in controlling the flow of loops.
""")

# Break
st.header("break Statement")
st.write("""
The `break` statement is used to exit a loop prematurely, regardless of the loop's condition. 
Once `break` is encountered, the loop terminates, and the control moves to the next statement outside the loop.
""")

# Break Example
st.subheader("break Example")
break_example = """
for i in range(1, 10):
    if i == 5:
        break
    print(i)
"""
st.code(break_example, language='python')

st.write("""
In this example, the loop prints numbers from 1 to 4. When `i == 5`, the `break` statement is executed, and the loop terminates.
""")

# Continue
st.header("continue Statement")
st.write("""
The `continue` statement is used to skip the rest of the code inside the current loop iteration and move to the next iteration. 
The loop doesn’t terminate; it just skips the remaining code for the current iteration.
""")

# Continue Example
st.subheader("continue Example")
continue_example = """
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
"""
st.code(continue_example, language='python')

st.write("""
In this example, when `i == 5`, the `continue` statement skips the print statement for that iteration, 
so the number 5 is not printed, but the loop continues to print the other numbers.
""")

# Pass
st.header("pass Statement")
st.write("""
The `pass` statement is a placeholder in Python that does nothing when executed. It is useful in situations where 
a statement is syntactically required but you don’t want to execute any code. 
Commonly used when you’re planning to add code in the future or want to avoid errors in incomplete code blocks.
""")

# Pass Example
st.subheader("pass Example")
pass_example = """
for i in range(1, 10):
    if i == 5:
        pass  # Placeholder for future code
    print(i)
"""
st.code(pass_example, language='python')

st.write("""
In this example, the `pass` statement does nothing when `i == 5`, so the loop continues as normal, printing all numbers from 1 to 9.
""")

# Key Differences
st.header("Key Differences")
st.write("""
1. **break**:
   - Exits the loop entirely, regardless of the iteration.
   
2. **continue**:
   - Skips the current iteration and moves on to the next one.

3. **pass**:
   - Does nothing, acts as a placeholder when you need to insert code in the future or handle a condition temporarily.
""")

# Interactive Example
st.subheader("Interactive Example")

option = st.selectbox(
    'Select Control Flow Statement',
    ('break', 'continue', 'pass'))

if option == 'break':
    st.write("Using break:")
    for i in range(1, 10):
        if i == 5:
            break
        st.write(i)
elif option == 'continue':
    st.write("Using continue:")
    for i in range(1, 10):
        if i == 5:
            continue
        st.write(i)
else:
    st.write("Using pass:")
    for i in range(1, 10):
        if i == 5:
            pass
        st.write(i)

st.write("""
In the interactive example, you can choose between `break`, `continue`, or `pass` to see how the loop behaves with each control flow statement.
""")


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



