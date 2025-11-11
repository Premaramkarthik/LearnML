import streamlit as st

if 'code' not in st.session_state:
    st.session_state.code = ''
# Define the custom style for the page

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

st.markdown("<h2>Operators in Python</h2>", unsafe_allow_html=True)

# Explanation of operators
st.markdown('''
### Python Operators
Operators are used to perform operations on variables and values. In Python, we have the following types of operators:\n
1.Arithmetic operators\n
2.Comparison operators\n
3.Assignment operators\n
4.Logical operators\n
5.Identity operators\n
6.Membership operators\n
7.Bitwise operators\n
''')

# Select the type of operator to explain
operator_type = st.selectbox("Choose an operator type", 
                             ["Arithmetic Operators", "Comparison Operators", "Assignment Operators", 
                              "Logical Operators", "Identity Operators", "Membership Operators", "Bitwise Operators"])

if st.session_state.get('last_operator_type') != operator_type:
    st.session_state.code = ''  # Reset code input area
    st.session_state.last_operator_type = operator_type  # Update last operator type
    
# Explanation based on the selected operator type
if operator_type == "Arithmetic Operators":
    st.markdown("<h3>Arithmetic Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Arithmetic operators are used to perform common mathematical operations.
    
    | Operator | Description           | Example           |
    |----------|-----------------------|-------------------|
    | +        | Addition               | x + y             |
    | -        | Subtraction            | x - y             |
    | *        | Multiplication         | x * y             |
    | /        | Division               | x / y             |
    | %        | Modulus                | x % y             |
    | **       | Exponentiation         | x ** y            |
    | //       | Floor division         | x // y            |
    ''')
    
    example_code = '''
    # Example Code
    x = 10
    y = 3
    print(f"Addition: {x + y}")
    print(f"Subtraction: {x - y}")
    print(f"Multiplication: {x * y}")
    print(f"Division: {x / y}")
    print(f"Modulus: {x % y}")
    print(f"Exponentiation: {x ** y}")
    print(f"Floor Division: {x // y}")
    '''
    
    st.code(example_code, language='python')
    
    # Output example
    x = 10
    y = 3
    st.write(f"Example Output:\nAddition: {x + y}, Subtraction: {x - y}, Multiplication: {x * y}, Division: {x / y}")
    st.write(f"Modulus: {x % y}, Exponentiation: {x ** y}, Floor Division: {x // y}")

elif operator_type == "Comparison Operators":
    st.markdown("<h3>Comparison Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Comparison operators are used to compare two values.
    
    | Operator | Description           | Example           |
    |----------|-----------------------|-------------------|
    | ==       | Equal                 | x == y            |
    | !=       | Not equal             | x != y            |
    | >        | Greater than          | x > y             |
    | <        | Less than             | x < y             |
    | >=       | Greater than or equal | x >= y            |
    | <=       | Less than or equal    | x <= y            |
    ''')

    example_code = '''
    # Example Code
    x = 5
    y = 10
    print(x == y)   # False
    print(x != y)   # True
    print(x > y)    # False
    print(x < y)    # True
    print(x >= y)   # False
    print(x <= y)   # True
    '''
    
    st.code(example_code, language='python')
    
    # Output example
    x = 5
    y = 10
    st.write(f"Example Output:\nEqual: {x == y}, Not equal: {x != y}, Greater than: {x > y}, Less than: {x < y}")
    st.write(f"Greater than or equal: {x >= y}, Less than or equal: {x <= y}")

elif operator_type == "Assignment Operators":
    st.markdown("<h3>Assignment Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Assignment operators are used to assign values to variables.
    
    | Operator | Example        | Equivalent      |
    |----------|----------------|-----------------|
    | =        | x = 5          | x = 5           |
    | +=       | x += 3         | x = x + 3       |
    | -=       | x -= 3         | x = x - 3       |
    | *=       | x *= 3         | x = x * 3       |
    | /=       | x /= 3         | x = x / 3       |
    | %=       | x %= 3         | x = x % 3       |
    | //=      | x //= 3        | x = x // 3      |
    | **=      | x **= 3        | x = x ** 3      |
    | &=       | x &= 3         | x = x & 3       |
    | \|=      | x \|= 3        | x = x \| 3      |
    ''')

    example_code = '''
    # Example Code
    x = 5
    x += 3
    print(x)  # 8
    x *= 2
    print(x)  # 16
    '''
    
    st.code(example_code, language='python')
    
    x = 5
    x += 3
    x *= 2
    st.write("Example Output:", x)

# More elif blocks can be added for other operator types (Logical, Identity, Membership, Bitwise)
elif operator_type == "Logical Operators":
    st.markdown("<h3>Logical Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Logical operators are used to combine conditional statements.
    
    | Operator | Description           | Example                |
    |----------|-----------------------|------------------------|
    | and      | Returns True if both statements are true | x < 5 and x < 10 |
    | or       | Returns True if one of the statements is true | x < 5 or x < 4 |
    | not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |
    ''')

    example_code = '''
    # Example Code
    x = 5
    print(x < 10 and x > 2)  # True
    print(x < 3 or x > 4)    # True
    print(not(x < 10 and x > 2))  # False
    '''
    
    st.code(example_code, language='python')
    
    # Output example
    x = 5
    st.write(f"Example Output:\nand: {x < 10 and x > 2}, or: {x < 3 or x > 4}, not: {not(x < 10 and x > 2)}")


elif operator_type == "Identity Operators":
    st.markdown("<h3>Identity Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Identity operators are used to compare the memory locations of two objects.
    
    | Operator | Description           | Example           |
    |----------|-----------------------|-------------------|
    | is       | Returns True if both variables are the same object | x is y |
    | is not   | Returns True if both variables are not the same object | x is not y |
    ''')

    example_code = '''
    # Example Code
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x

    print(x is z)  # True, because z is the same object as x
    print(x is y)  # False, because x is not the same object as y, even if they have the same content
    print(x == y)  # True, because x and y have the same content
    '''
    
    st.code(example_code, language='python')
    
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    st.write(f"Example Output:\nis: {x is z}, is not: {x is not y}, == : {x == y}")


elif operator_type == "Membership Operators":
    st.markdown("<h3>Membership Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Membership operators are used to test if a sequence is presented in an object.
    
    | Operator | Description           | Example           |
    |----------|-----------------------|-------------------|
    | in       | Returns True if a sequence with the specified value is present in the object | x in y |
    | not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |
    ''')

    example_code = '''
    # Example Code
    x = ["apple", "banana"]
    print("banana" in x)  # True
    print("pineapple" not in x)  # True
    '''
    
    st.code(example_code, language='python')
    
    x = ["apple", "banana"]
    st.write(f"Example Output:\nin: {'banana' in x}, not in: {'pineapple' not in x}")


elif operator_type == "Bitwise Operators":
    st.markdown("<h3>Bitwise Operators</h3>", unsafe_allow_html=True)
    st.markdown('''
    Bitwise operators are used to compare (binary) numbers.
    
    | Operator | Description           | Example           |
    |----------|-----------------------|-------------------|
    | &        | AND                   | x & y             |
    | |        | OR                    | x | y             |
    | ^        | XOR                   | x ^ y             |
    | ~        | NOT                   | ~x                |
    | <<       | Zero fill left shift  | x << 2            |
    | >>       | Signed right shift    | x >> 2            |
    ''')

    example_code = '''
    # Example Code
    x = 10  # 1010 in binary
    y = 4   # 0100 in binary

    print(x & y)   # 0
    print(x | y)   # 14
    print(x ^ y)   # 14
    print(~x)      # -11
    print(x << 2)  # 40
    print(x >> 2)  # 2
    '''
    
    st.code(example_code, language='python')
    
    x = 10
    y = 4
    st.write(f"Example Output:\nAND: {x & y}, OR: {x | y}, XOR: {x ^ y}, NOT: {~x}, Left Shift: {x << 2}, Right Shift: {x >> 2}")






# Allow users to try their own Python code
st.markdown('<h4>Try it yourself!</h4>', unsafe_allow_html=True)

# Code input area for users to enter their Python code
code = st.text_area("Enter your Python code here:", height=200, value=st.session_state.code, key='code_input')

# Button to run the code
if st.button("Run Code"):
    import sys
    import io
    
     #Redirect stdout to capture print statements
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
         #Handle any errors
        st.error(f"Error: {e}")
    
    # Reset stdout
    sys.stdout = old_stdout
