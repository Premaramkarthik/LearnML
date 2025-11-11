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
st.title('Introduction to Python Dictionaries')

st.markdown('''
**Dictionaries** in Python are mutable, unordered collections of key-value pairs. Each key is unique, and values can be of any data type. 
Dictionaries are useful when you need to associate a unique key with a value for fast lookups.

### Key Features:
- Keys must be **unique**.
- Keys are **immutable** data types (e.g., strings, numbers, tuples).
- Values can be **mutable** or **immutable** (e.g., strings, numbers, lists, another dictionary).
- Dictionaries are **unordered**, meaning they don't maintain the order of items added.

#### Basic Syntax:
A dictionary is created using curly braces `{}` or with the `dict()` function.
''')

# Example of dictionary creation
st.subheader('Example 1: Creating a Dictionary')
st.code('''
# Creating a dictionary
student = {
"name": "John",
"age": 20,
"major": "Computer Science"
}

print(student)
''')

# Output for the example
st.text('Output:')
st.text('{"name": "John", "age": 20, "major": "Computer Science"}')

st.markdown('''
In this example, we created a dictionary `student` with three key-value pairs: `"name"`, `"age"`, and `"major"`. Each key is associated with a specific value.

### Accessing Values:
Values in a dictionary can be accessed using their keys.
''')

# Example of accessing values
st.subheader('Example 2: Accessing Dictionary Values')
st.code('''
# Accessing values
name = student["name"]
age = student.get("age")

print(f"Name: {name}, Age: {age}")
''')

st.text('Output:')
st.text('Name: John, Age: 20')

st.markdown('''
Here, we used the key `"name"` to retrieve the value associated with it. The `get()` method can also be used to access values, providing the key as an argument.

### Adding and Updating Values:
You can add new key-value pairs or update existing ones in a dictionary.
''')

# Example of adding/updating values
st.subheader('Example 3: Adding/Updating Dictionary Values')
st.code('''
# Adding a new key-value pair
student["graduation_year"] = 2024

# Updating an existing value
student["age"] = 21

print(student)
''')

st.text('Output:')
st.text('{"name": "John", "age": 21, "major": "Computer Science", "graduation_year": 2024}')


example_code = '''
# Example Code
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
'''
st.code(example_code, language='python')

# Example output
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
st.write("Example Output:", my_dict)

st.title('Dictionary Methods')

# Dropdown for Dictionary Methods
method = st.selectbox(
    "Choose a dictionary method to learn about:",
    [
        'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 
        'update', 'values'
    ]
)

# Explaining the selected method
if method == "clear":
    st.markdown("<h3>clear()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `clear()` method removes all items from the dictionary.
    #### Syntax
    `dict.clear()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    my_dict.clear()
    print(my_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    my_dict.clear()
    st.write("Example Output:", my_dict)

elif method == "copy":
    st.markdown("<h3>copy()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `copy()` method returns a shallow copy of the dictionary.
    #### Syntax
    `dict.copy()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    new_dict = my_dict.copy()
    print(new_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    new_dict = my_dict.copy()
    st.write("Example Output:", new_dict)

elif method == "fromkeys":
    st.markdown("<h3>fromkeys()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `fromkeys()` method creates a new dictionary from the given keys, with values set to a specified value (default is None).
    #### Syntax
    `dict.fromkeys(keys, value=None)`
    ''')

    example_code = '''
    # Example Code
    keys = ('name', 'age', 'city')
    new_dict = dict.fromkeys(keys, "unknown")
    print(new_dict)
    '''
    st.code(example_code, language='python')

    keys = ('name', 'age', 'city')
    new_dict = dict.fromkeys(keys, "unknown")
    st.write("Example Output:", new_dict)

elif method == "get":
    st.markdown("<h3>get()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `get()` method returns the value for a specified key. If the key does not exist, it returns None (or a specified default value).
    #### Syntax
    `dict.get(key, default=None)`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    value = my_dict.get("name")
    print(value)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    value = my_dict.get("name")
    st.write("Example Output:", value)

elif method == "items":
    st.markdown("<h3>items()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `items()` method returns a view object that displays a list of a dictionary's key-value tuple pairs.
    #### Syntax
    `dict.items()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    items = my_dict.items()
    print(items)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    items = my_dict.items()
    st.write("Example Output:", list(items))

elif method == "keys":
    st.markdown("<h3>keys()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `keys()` method returns a view object that displays a list of all the keys in the dictionary.
    #### Syntax
    `dict.keys()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    keys = my_dict.keys()
    print(keys)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    keys = my_dict.keys()
    st.write("Example Output:", list(keys))

elif method == "pop":
    st.markdown("<h3>pop()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `pop()` method removes the specified key and returns the corresponding value. If the key does not exist, it raises a KeyError.
    #### Syntax
    `dict.pop(key, default)`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    value = my_dict.pop("age")
    print(value)
    print(my_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    value = my_dict.pop("age")
    st.write("Example Output: Value:", value, "Updated Dictionary:", my_dict)

elif method == "popitem":
    st.markdown("<h3>popitem()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `popitem()` method removes and returns the last inserted key-value pair as a tuple.
    #### Syntax
    `dict.popitem()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25}
    item = my_dict.popitem()
    print(item)
    print(my_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25}
    item = my_dict.popitem()
    st.write("Example Output: Item:", item, "Updated Dictionary:", my_dict)

elif method == "setdefault":
    st.markdown("<h3>setdefault()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `setdefault()` method returns the value of a specified key. If the key does not exist, it inserts the key with a specified value (default is None).
    #### Syntax
    `dict.setdefault(key, default=None)`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice"}
    value = my_dict.setdefault("age", 25)
    print(value)
    print(my_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice"}
    value = my_dict.setdefault("age", 25)
    st.write("Example Output: Value:", value, "Updated Dictionary:", my_dict)

elif method == "update":
    st.markdown("<h3>update()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `update()` method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
    #### Syntax
    `dict.update([other])`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice"}
    my_dict.update({"age": 25})
    print(my_dict)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice"}
    my_dict.update({"age": 25})
    st.write("Example Output:", my_dict)

elif method == "values":
    st.markdown("<h3>values()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `values()` method returns a view object that displays a list of all the values in the dictionary.
    #### Syntax
    `dict.values()`
    ''')

    example_code = '''
    # Example Code
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    values = my_dict.values()
    print(values)
    '''
    st.code(example_code, language='python')

    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    values = my_dict.values()
    st.write("Example Output:", list(values))


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



