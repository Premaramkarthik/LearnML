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


st.markdown("<h2>Lists in Python </h2>", unsafe_allow_html=True)

# Explanation of lists
st.markdown('''
A **list** is a collection in Python that is ordered, changeable, and allows duplicate values. Lists are one of Python's most versatile and powerful tools for storing a collection of items, which can be of mixed data types (e.g., integers, strings, or even other lists). Lists are defined by enclosing items in square brackets `[]`.

 ##### Characteristics of Lists:\n
 i. **Ordered**: The items in a list have a defined order, and that order will not change unless you explicitly do so.\n
 ii. **Changeable**: You can modify a list after it is created, meaning you can add, remove, or change items.\n
 iii. **Allow Duplicates**: Lists can contain multiple occurrences of the same item.\n

##### Basic Syntax:
```python
my_list = [1, 2, 3, "hello", 3.14]
```
\n
Here are some important list methods and what they do:\n
 `append()`, 
 `clear()`, 
 `copy()` ,
 `count()` ,
 `extend()`,
 `index()` ,
`insert()`,
 `pop()` ,
 `remove()` ,
 `reverse()`, 
 `sort()` 
''')

# Select the list method to explain
list_method = st.selectbox("Choose a list method", 
                             ["append()", "clear()", "copy()", "count()", 
                              "extend()", "index()", "insert()", "pop()", 
                              "remove()", "reverse()", "sort()"])

if st.session_state.get('last_list_method') != list_method:
    st.session_state.code = ''  # Reset code input area
    st.session_state.last_list_method = list_method  # Update last list method

# Explanation based on the selected list method
if list_method == "append()":
    st.markdown("<h3>append()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `append()` method adds an element to the end of the list. The length of the list increases by one.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    my_list.append(4)
    st.write(f"Example Output: {my_list}")

elif list_method == "clear()":
    st.markdown("<h3>clear()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `clear()` method removes all elements from the list, leaving it empty.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list)  # Output will be an empty list
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    my_list.clear()
    st.write(f"Example Output: {my_list}")

elif list_method == "copy()":
    st.markdown("<h3>copy()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `copy()` method returns a shallow copy of the list, meaning it creates a new list with the same elements.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    new_list = my_list.copy()
    print(new_list)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    new_list = my_list.copy()
    st.write(f"Example Output: {new_list}")

elif list_method == "count()":
    st.markdown("<h3>count()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `count()` method returns the number of times the specified element appears in the list.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 2, 3]
    count_of_twos = my_list.count(2)
    print(count_of_twos)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 2, 3]
    count_of_twos = my_list.count(2)
    st.write(f"Example Output: {count_of_twos}")

elif list_method == "extend()":
    st.markdown("<h3>extend()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `extend()` method adds all elements of an iterable (like another list) to the end of the current list.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    st.write(f"Example Output: {my_list}")

elif list_method == "index()":
    st.markdown("<h3>index()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `index()` method returns the index of the first occurrence of the specified element.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    index_of_two = my_list.index(2)
    print(index_of_two)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    index_of_two = my_list.index(2)
    st.write(f"Example Output: {index_of_two}")

elif list_method == "insert()":
    st.markdown("<h3>insert()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `insert()` method inserts an element at the specified position.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    my_list.insert(1, 4)  # Inserts 4 at index 1
    print(my_list)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    st.write(f"Example Output: {my_list}")

elif list_method == "pop()":
    st.markdown("<h3>pop()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `pop()` method removes the element at the specified position (or the last element if no index is specified).
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3]
    my_list.pop(1)  # Removes the element at index 1
    print(my_list)
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3]
    my_list.pop(1)
    st.write(f"Example Output: {my_list}")

elif list_method == "remove()":
    st.markdown("<h3>remove()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `remove()` method removes the first occurrence of the specified value.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3, 2]
    my_list.remove(2)  # Removes the first occurrence of 2
    print(my_list)
    '''
    
elif list_method == "reverse()":
    st.markdown("<h3>reverse()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `reverse()` method reverses the elements of the list in place. It changes the order of the list to the reverse of what it was previously.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [1, 2, 3, 4]
    my_list.reverse()  # Reverses the list
    print(my_list)  # Output: [4, 3, 2, 1]
    '''
    
    st.code(example_code, language='python')
    
    my_list = [1, 2, 3, 4]
    my_list.reverse()
    st.write(f"Example Output: {my_list}")

elif list_method == "sort()":
    st.markdown("<h3>sort()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `sort()` method sorts the list in ascending order by default. You can sort it in descending order by setting the `reverse` parameter to `True`.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_list = [3, 1, 4, 2]
    my_list.sort()  # Sorts the list in ascending order
    print(my_list)  # Output: [1, 2, 3, 4]
    
    # Sorting in descending order
    my_list.sort(reverse=True)
    print(my_list)  # Output: [4, 3, 2, 1]
    '''
    
    st.code(example_code, language='python')
    
    my_list = [3, 1, 4, 2]
    my_list.sort()
    st.write(f"Example Output (ascending): {my_list}")
    
    my_list.sort(reverse=True)
    st.write(f"Example Output (descending): {my_list}")

 
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
