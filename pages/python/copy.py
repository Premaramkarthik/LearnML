import streamlit as st
import copy


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

import streamlit as st
import copy

st.title("Shallow Copy vs Deep Copy in Python")

# Introduction
st.header("Introduction")
st.write("""
In Python, when you assign or copy one object to another, the copying process is either 'shallow' or 'deep'. 
Both these methods copy objects but handle nested objects (objects containing other objects like lists within lists) differently.
""")

# Shallow Copy
st.header("Shallow Copy")
st.write("""
A shallow copy means constructing a new collection object and populating it with references to the child objects found in the original. 
In other words, the 'outer' object is copied, but the 'inner' objects are still referenced.
""")

# Shallow Copy Example
st.subheader("Shallow Copy Example")
shallow_example = """
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

# Modify one of the inner lists
shallow_copied_list[0][0] = 'Modified'

print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)
"""
st.code(shallow_example, language='python')

st.write("""
In this example, both the `original_list` and `shallow_copied_list` reference the same inner lists. 
So, modifying an element in the `shallow_copied_list` affects the `original_list` as well.
""")

# Deep Copy
st.header("Deep Copy")
st.write("""
A deep copy creates a new object and recursively copies all objects found within the original, 
meaning that it duplicates the 'inner' objects as well. The original and the copied object become fully independent of each other.
""")

# Deep Copy Example
st.subheader("Deep Copy Example")
deep_example = """
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

# Modify one of the inner lists
deep_copied_list[0][0] = 'Modified'

print("Original list:", original_list)
print("Deep copied list:", deep_copied_list)
"""
st.code(deep_example, language='python')

st.write("""
In this example, the `deep_copied_list` and the `original_list` are completely independent. 
Modifying an element in the `deep_copied_list` does not affect the `original_list`.
""")

# Key Differences
st.header("Key Differences")
st.write("""
1. **Shallow Copy**:
   - Only copies the outer object, not the nested ones.
   - If the nested objects (e.g., lists within lists) are modified, both the original and the copied object will reflect the change.
   
2. **Deep Copy**:
   - Recursively copies the entire structure, including all nested objects.
   - Modifying the copied object does not affect the original object, and vice versa.
""")

# Demonstrating the difference interactively
st.subheader("Interactive Example")

option = st.selectbox(
    'Select Copy Type',
    ('Shallow Copy', 'Deep Copy'))

if option == 'Shallow Copy':
    original_list = [[1, 2, 3], [4, 5, 6]]
    shallow_copied_list = copy.copy(original_list)
    shallow_copied_list[0][0] = 'Modified'
    st.write("Original list:", original_list)
    st.write("Shallow copied list:", shallow_copied_list)
else:
    original_list = [[1, 2, 3], [4, 5, 6]]
    deep_copied_list = copy.deepcopy(original_list)
    deep_copied_list[0][0] = 'Modified'
    st.write("Original list:", original_list)
    st.write("Deep copied list:", deep_copied_list)

st.write("""
You can observe that in a shallow copy, changes made to the nested object in the copied list 
are reflected in the original list, whereas in a deep copy, the original list remains unchanged.
""")


# Code input area for users to enter their Python code

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



