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

st.markdown("<h2>Sets in Python</h2>", unsafe_allow_html=True)

# Explanation of sets
st.markdown('''
A set is a collection that is unordered, unindexed, and does not allow duplicate elements. Sets are written with curly brackets `{}`.\n
Sets are used to store multiple items in a single variable. They are commonly used when you need to perform mathematical set operations like union, intersection, and difference.\n
Some important characteristics of sets:\n
i. **Unordered**: The items in a set have no defined order.\n
ii. **Unchangeable** (but you can add or remove items).\n
iii. **No duplicates**: Sets do not allow duplicate values.\n

Here are some of the commonly used set methods in Python:\n
 `add()`,
 `clear()`,
 `copy()`,
 `difference()`,
 `difference_update()`,
 `discard()`,
 `intersection()`,
 `intersection_update()`,
 `isdisjoint()`,
 `issubset()`,
 `issuperset()`,
 `pop()`,
 `remove()`,
 `symmetric_difference()`,
 `symmetric_difference_update()`,
 `union()`,
 `update()`
''')

# Select the set method to explain
set_method = st.selectbox("Choose a set method", 
                             ["add()", "clear()", "copy()", "difference()", 
                              "difference_update()", "discard()", "intersection()",
                              "intersection_update()", "isdisjoint()", "issubset()",
                              "issuperset()", "pop()", "remove()", "symmetric_difference()", 
                              "symmetric_difference_update()", "union()", "update()"])

if st.session_state.get('last_set_method') != set_method:
    st.session_state.code = ''  # Reset code input area
    st.session_state.last_set_method = set_method  # Update last set method
    
# Explanation based on the selected set method
if set_method == "add()":
    st.markdown("<h3>add()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `add()` method adds an element to the set.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)  # Output: {1, 2, 3, 4}
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3}
    my_set.add(4)
    st.write(f"Example Output: {my_set}")

elif set_method == "clear()":
    st.markdown("<h3>clear()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `clear()` method removes all elements from the set.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)  # Output: set()
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3}
    my_set.clear()
    st.write(f"Example Output: {my_set}")

elif set_method == "copy()":
    st.markdown("<h3>copy()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `copy()` method returns a shallow copy of the set.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3}
    new_set = my_set.copy()
    print(new_set)  # Output: {1, 2, 3}
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3}
    new_set = my_set.copy()
    st.write(f"Example Output: {new_set}")

elif set_method == "difference()":
    st.markdown("<h3>difference()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `difference()` method returns a set containing the difference between two or more sets.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    diff = set1.difference(set2)
    print(diff)  # Output: {1, 2}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    diff = set1.difference(set2)
    st.write(f"Example Output: {diff}")

elif set_method == "difference_update()":
    st.markdown("<h3>difference_update()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `difference_update()` method removes the items in this set that are also included in another set.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.difference_update(set2)
    print(set1)  # Output: {1, 2}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.difference_update(set2)
    st.write(f"Example Output: {set1}")

elif set_method == "discard()":
    st.markdown("<h3>discard()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `discard()` method removes the specified element from the set, if it is present.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3, 4}
    my_set.discard(3)
    print(my_set)  # Output: {1, 2, 4}
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3, 4}
    my_set.discard(3)
    st.write(f"Example Output: {my_set}")

elif set_method == "intersection()":
    st.markdown("<h3>intersection()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `intersection()` method returns a set that is the intersection of two or more sets.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    intersec = set1.intersection(set2)
    print(intersec)  # Output: {3, 4}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    intersec = set1.intersection(set2)
   
elif set_method == "intersection_update()":
    st.markdown("<h3>intersection_update()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `intersection_update()` method removes the items in this set that are not present in other sets. 
    It modifies the original set to keep only the elements found in all sets.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.intersection_update(set2)
    print(set1)  # Output: {3, 4}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.intersection_update(set2)
    st.write(f"Example Output: {set1}")

elif set_method == "isdisjoint()":
    st.markdown("<h3>isdisjoint()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `isdisjoint()` method returns `True` if two sets have no elements in common, otherwise it returns `False`.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    print(set1.isdisjoint(set2))  # Output: True
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    is_disjoint = set1.isdisjoint(set2)
    st.write(f"Example Output: {is_disjoint}")

elif set_method == "issubset()":
    st.markdown("<h3>issubset()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `issubset()` method returns `True` if all elements of this set are present in another set, otherwise it returns `False`.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    print(set1.issubset(set2))  # Output: True
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    is_subset = set1.issubset(set2)
    st.write(f"Example Output: {is_subset}")

elif set_method == "issuperset()":
    st.markdown("<h3>issuperset()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `issuperset()` method returns `True` if this set contains all elements of another set, otherwise it returns `False`.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    print(set1.issuperset(set2))  # Output: True
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    is_superset = set1.issuperset(set2)
    st.write(f"Example Output: {is_superset}")

elif set_method == "pop()":
    st.markdown("<h3>pop()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `pop()` method removes and returns an arbitrary element from the set. 
    Since sets are unordered, the removed element is not guaranteed to be the first or last item.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3, 4}
    popped_item = my_set.pop()
    print(popped_item)  # Output: (an arbitrary element, e.g., 1)
    print(my_set)       # Output: {2, 3, 4}
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3, 4}
    popped_item = my_set.pop()
    st.write(f"Example Output: Popped item: {popped_item}, Set after pop: {my_set}")

elif set_method == "remove()":
    st.markdown("<h3>remove()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `remove()` method removes the specified element from the set. 
    If the element is not found, it raises a `KeyError`.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    my_set = {1, 2, 3, 4}
    my_set.remove(3)
    print(my_set)  # Output: {1, 2, 4}
    '''
    
    st.code(example_code, language='python')
    
    my_set = {1, 2, 3, 4}
    my_set.remove(3)
    st.write(f"Example Output: {my_set}")

elif set_method == "symmetric_difference()":
    st.markdown("<h3>symmetric_difference()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `symmetric_difference()` method returns a set that contains elements that are in either of the sets, but not in both.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    sym_diff = set1.symmetric_difference(set2)
    print(sym_diff)  # Output: {1, 2, 5, 6}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    sym_diff = set1.symmetric_difference(set2)
    st.write(f"Example Output: {sym_diff}")

elif set_method == "symmetric_difference_update()":
    st.markdown("<h3>symmetric_difference_update()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `symmetric_difference_update()` method updates the original set, keeping only the elements that are not common with the other set.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.symmetric_difference_update(set2)
    print(set1)  # Output: {1, 2, 5, 6}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set1.symmetric_difference_update(set2)
    st.write(f"Example Output: {set1}")

elif set_method == "union()":
    st.markdown("<h3>union()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `union()` method returns a set that contains all elements from both sets, without duplicates.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1.union(set2)
    print(union_set)  # Output: {1, 2, 3, 4, 5}
    '''
    
    st.code(example_code, language='python')
    
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1.union(set2)
    st.write(f"Example Output: {union_set}")

elif set_method == "update()":
    st.markdown("<h3>update()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `update()` method updates the set with the union of this set and others. 
    It adds all the elements from another set to the original set, automatically removing any duplicates.
    
    Example:
    ''')
    example_code = '''
    # Example Code
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1.update(set2)
    print(set1)  # Output: {1, 2, 3, 4, 5}
    '''
    
    st.code(example_code, language='python')
    
    # Example in Streamlit
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set1.update(set2)
    st.write(f"Example Output: {set1}")

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
