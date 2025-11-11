import streamlit as st
import sys
import io



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


st.markdown("### Variables", unsafe_allow_html=True)

st.markdown('''
In Python, variables are containers for storing data values. Unlike other programming languages, Python has no command for declaring a variable.
''')

# Initialize session state for method and code
if 'method' not in st.session_state:
    st.session_state.method = ''
if 'code' not in st.session_state:
    st.session_state.code = ''
if 'output' not in st.session_state:
    st.session_state.output = ''

# Function to reset code and output when the method changes
def reset_code():
    st.session_state.code = ''
    st.session_state.output = ''

# Choose a topic
method = st.selectbox("Choose a topic", ["Assigning Values", "Multiple Assignments", "Global and Local Variables", "Type Casting", "Variable Names"])

# Check if the method has changed and reset the code input area
if st.session_state.method != method:
    reset_code()
    st.session_state.method = method

# Logic for displaying different topics
if method == "Assigning Values":
    st.markdown("<h2>Assigning Values</h2>", unsafe_allow_html=True)
    st.markdown('''
    In Python, assigning values to a variable is simple. You just use the equal sign (`=`).
    #### Syntax:
    ```
    variable_name = value
    ```
    #### Example:
    ''')
    example_code = '''
# Example Code
x = 5
y = "Hello"
print(x)
print(y)
    '''
    st.code(example_code, language='python')

    x = 5
    y = "Hello"
    st.write("Example Output:", x, y)

elif method == "Multiple Assignments":
    st.markdown("<h2 style='color:#064747;'>Multiple Assignments</h2>", unsafe_allow_html=True)
    st.markdown('''
    Python allows you to assign values to multiple variables in one line.
    #### Syntax:
    ```
    var1, var2, var3 = value1, value2, value3
    ```
    #### Example:
    ''')
    example_code = '''
# Example Code
a, b, c = 1, "apple", 3.14
print(a)
print(b)
print(c)
    '''
    st.code(example_code, language='python')

    a, b, c = 1, "apple", 3.14
    st.write("Example Output:", a, b, c)

elif method == "Global and Local Variables":
    st.markdown("<h2 style='color:#064747;'>Global and Local Variables</h2>", unsafe_allow_html=True)
    st.markdown('''
    Variables created inside a function are local, while variables created outside a function are global.
    You can use the `global` keyword to modify a global variable inside a function.
    
    #### Example:
    ''')
    example_code = '''
# Example Code
x = "global variable"
def my_func():
    global x
    x = "changed inside function"
    print(x)
my_func()
print(x)
    '''
    st.code(example_code, language='python')

    x = "global variable"

    def my_func():
        global x
        x = "changed inside function"

    my_func()
    st.write("Example Output:", x)

elif method == "Type Casting":
    st.markdown("<h2 style='color:#064747;'>Type Casting</h2>", unsafe_allow_html=True)
    st.markdown('''
    You can specify the type of a variable using casting, which is done using constructor functions such as `int()`, `str()`, and `float()`.
    
    #### Example:
    ''')
    example_code = '''
# Example Code
x = str(3)    # '3'
y = int(3.8)  # 3
z = float(5)  # 5.0
print(x)
print(y)
print(z)
    '''
    st.code(example_code, language='python')

    x = str(3)
    y = int(3.8)
    z = float(5)
    st.write("Example Output:", x, y, z)

elif method == "Variable Names":
    st.markdown("<h2 style='color:#064747;'>Variable Names</h2>", unsafe_allow_html=True)
    st.markdown('''
    Python has some rules for variable names:\n
    (i) A variable name must start with a letter or the underscore character.\n
    (ii) A variable name cannot start with a number.\n
    (iii) A variable name can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_`).\n
    (iv) Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables).\n
    #### Example:
    ''')
    example_code = '''
# Example Code
myVar = 5
_my_var = "Hello"
MyVar = 3.14
print(myVar)
print(_my_var)
print(MyVar)
    '''
    st.code(example_code, language='python')

    myVar = 5
    _my_var = "Hello"
    MyVar = 3.14
    st.write("Example Output:", myVar, _my_var, MyVar)

# Code input area for users to enter their Python code
st.markdown('<h4>Try it yourself!</h4>', unsafe_allow_html=True)
code = st.text_area("Enter your Python code here:", height=200, value=st.session_state.code)

# Button to run the code
if st.button("Run Code"):
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        # Execute the user's code
        exec(code)

        # Get output
        st.session_state.output = new_stdout.getvalue()
        st.text_area("Output:", st.session_state.output, height=150)
    except Exception as e:
        # Handle any errors
        st.session_state.output = f"Error: {e}"
        st.error(st.session_state.output)

    # Reset stdout
    sys.stdout = old_stdout

def reset_code_output():
    st.session_state.code = ''
    st.session_state.output = ''

# Call the reset function based on method change or page change
reset_code_output()

