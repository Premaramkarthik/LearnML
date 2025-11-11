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

st.markdown("<h2>Tuples in Python</h2>", unsafe_allow_html=True)

# Explanation of tuples
st.markdown('''
A tuple is a collection that is ordered and immutable. This means that once a tuple is created, you cannot modify or change its elements. Tuples are written with round brackets `()`.\n
Tuples are similar to lists in terms of indexing, slicing, and access, but unlike lists, they cannot be modified. Here are some important characteristics of tuples:\n
i. **Immutability**: Tuples cannot be changed after creation. If you need a collection of items that should remain constant, use a tuple.\n
ii. **Accessing Elements**: Like lists, tuples can be accessed using indexing and slicing.\n
iii. **Mixed Data Types**: Tuples can contain items of different data types.\n
iv. **Efficient**: Since tuples are immutable, Python optimizes them for performance, making them faster than lists in certain cases.\n

Some commonly used tuple methods are:\n
`count()`,
 `index()` 
''')

# Select the tuple method to explain
tuple_method = st.selectbox("Choose a tuple method", 
                             ["count()", "index()"])

if st.session_state.get('last_tuple_method') != tuple_method:
    st.session_state.code = ''  # Reset code input area
    st.session_state.last_tuple_method = tuple_method  # Update last tuple method
    
# Explanation based on the selected tuple method
if tuple_method == "count()":
    st.markdown("<h3>count()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `count()` method returns the number of times a specified value appears in a tuple.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_tuple = (1, 2, 3, 2, 2, 4)
    count_of_2 = my_tuple.count(2)
    print(count_of_2)  # Output: 3
    '''
    
    st.code(example_code, language='python')
    
    my_tuple = (1, 2, 3, 2, 2, 4)
    count_of_2 = my_tuple.count(2)
    st.write(f"Example Output: {count_of_2}")

elif tuple_method == "index()":
    st.markdown("<h3>index()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `index()` method searches the tuple for a specified value and returns the index of the first match.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_tuple = (1, 2, 3, 2, 2, 4)
    index_of_2 = my_tuple.index(2)
    print(index_of_2)  # Output: 1
    '''
    
    st.code(example_code, language='python')
    
    my_tuple = (1, 2, 3, 2, 2, 4)
    index_of_2 = my_tuple.index(2)
    st.write(f"Example Output: {index_of_2}")


# General explanation about tuples in Python
st.markdown('''

Here are some more examples:
''')

example_code = '''
# Example 1: Creating a tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)

# Example 2: Accessing tuple elements
print(my_tuple[1])  # Output: 2
print(my_tuple[-1])  # Output: 4

# Example 3: Tuple with mixed data types
mixed_tuple = ("apple", 3, 4.5)
print(mixed_tuple)  # Output: ('apple', 3, 4.5)
'''

st.code(example_code, language='python')


# Allow users to try their own Python code
st.markdown('<h4>Try it yourself!</h4>', unsafe_allow_html=True)

# Code input area for users to enter their Python code
code = st.text_area("Enter your Python code here:", height=200, value=st.session_state.code, key='code_input')

# Button to run the code
if st.button("Run Code"):
    import sys
    import io
    
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    try:
        # Execute the user's code
        exec(st.session_state.code_input)
        
        # Get output
        output = new_stdout.getvalue()
        st.text_area("Output:", output, height=150)
    except Exception as e:
        # Handle any errors
        st.error(f"Error: {e}")
    
    # Reset stdout
    sys.stdout = old_stdout
