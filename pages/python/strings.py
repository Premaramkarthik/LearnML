
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

# Introduction to Strings
st.markdown("<h2>Strings in Python</h2>", unsafe_allow_html=True)
st.markdown('''
**Strings** in Python are sequences of characters enclosed within single or double quotes. They are immutable, meaning that once created, they cannot be changed.
You can create strings, assign them to variables, and use them in various operations. Below is an example of how to create and print strings:
''')

example_code = '''
# Example Code
a = "Hello, World!"
b = "Python is fun."
c = 'She said "Hello"'
print(a)
print(b)
print(c)
'''
st.code(example_code, language='python')

# Example output
a = "Hello, World!"
b = "Python is fun."
c = 'She said "Hello"'

st.write("Example Output:", a, b, c)

# Dropdown for String Methods
method = st.selectbox(
    "Choose a string method to learn about:",
    [
        'upper', 'lower', 'capitalize', 'swapcase', 'casefold',  'title', 'center', 'count', 'replace',
        'index', 'rindex',  'join', 'encode', 'startswith', 'endswith', 'expandtabs', 'find',  'rfind', 
        'split', 'rsplit',  'splitlines', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
        'isidentifier', 'islower', 'isnumeric', 'isprintable','isspace', 'istitle', 'isupper', 'partition',
        'rpartition', 'ljust', 'rjust', 'strip', 'lstrip', 'rstrip' , 'removeprefix', 'removesuffix',     
        'format', 'format_map', 'translate', 'maketrans', 'zfill'
    ]
)

# Explaining the selected method
if method == "capitalize":
    st.markdown("<h3>capitalize()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `capitalize()` method returns a copy of the string with its first character capitalized and the rest lowercased.
    #### Syntax
    `string.capitalize()`
    ''')

    example_code = '''
    # Example Code
    txt = "hello, world!"
    x = txt.capitalize()
    print(x)
    '''
    st.code(example_code, language='python')

    txt = "hello, world!"
    x = txt.capitalize()
    st.write("Example Output:", x)

elif method == "casefold":
    st.markdown("<h3>casefold()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `casefold()` method is similar to `lower()`, but it removes all case distinctions and is stronger.
    #### Syntax
    `string.casefold()`
    ''')

    example_code = '''
    # Example Code
    txt = "HELLO, WORLD!"
    x = txt.casefold()
    print(x)
    '''
    st.code(example_code, language='python')

    txt = "HELLO, WORLD!"
    x = txt.casefold()
    st.write("Example Output:", x)

elif method == "center":
    st.markdown("<h3>center()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `center()` method returns a centered string of a specified width, padding with specified characters (default is space).
    #### Syntax
    `string.center(width, fillchar)`
    ''')

    example_code = '''
    # Example Code
    txt = "Python"
    x = txt.center(20, "*")
    print(x)
    '''
    st.code(example_code, language='python')

    txt = "Python"
    x = txt.center(20, "*")
    st.write("Example Output:", x)

elif method == "count":
    st.markdown("<h3>count()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The `count()` method returns the number of occurrences of a substring in the string.
    #### Syntax
    `string.count(substring, start, end)`
    ''')

    example_code = '''
    # Example Code
    txt = "I love Python. Python is fun."
    x = txt.count("Python")
    print(x)
    '''
    st.code(example_code, language='python')

    txt = "I love Python. Python is fun."
    x = txt.count("Python")
    st.write("Example Output:", x)

if method == 'encode':
    st.markdown("<h3>Encode()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The encode() method encodes the string using the specified encoding. Default is 'utf-8'.
    #### Syntax
    'string.encode(encoding="utf-8", errors="strict")'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, World!"
    x = txt.encode()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, World!"
    x = txt.encode()
    st.write("Example Output:", x)

elif method == 'endswith':
    st.markdown("<h3>Endswith()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The endswith() method returns True if the string ends with the specified suffix, otherwise False.
    #### Syntax
    'string.endswith(value, start, end)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, World!"
    x = txt.endswith("World!")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, World!"
    x = txt.endswith("World!")
    st.write("Example Output:", x)

elif method == 'expandtabs':
    st.markdown("<h3>Expandtabs()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The expandtabs() method sets the tab size to the specified number of whitespaces.
    #### Syntax
    'string.expandtabs(tabsize)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "H\te\tl\tl\to"
    x = txt.expandtabs(2)
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "H\te\tl\tl\to"
    x = txt.expandtabs(2)
    st.write("Example Output:", x)

elif method == 'find':
    st.markdown("<h3>Find()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The find() method finds the first occurrence of the specified value and returns the index. Returns -1 if not found.
    #### Syntax
    'string.find(value, start, end)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, welcome to the world!"
    x = txt.find("welcome")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, welcome to the world!"
    x = txt.find("welcome")
    st.write("Example Output:", x)

elif method == 'lower':
    st.markdown("<h3>Lower()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The lower() method converts all characters in a string to lowercase.
    #### Syntax
    'string.lower()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "HELLO WORLD"
    x = txt.lower()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "HELLO WORLD"
    x = txt.lower()
    st.write("Example Output:", x)

elif method == 'upper':
    st.markdown("<h3>Upper()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The upper() method converts all characters in a string to uppercase.
    #### Syntax
    'string.upper()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "hello world"
    x = txt.upper()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "hello world"
    x = txt.upper()
    st.write("Example Output:", x)

elif method == 'swapcase':
    st.markdown("<h3>Swapcase()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The swapcase() method swaps cases, converting uppercase letters to lowercase and vice versa.
    #### Syntax
    'string.swapcase()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, World!"
    x = txt.swapcase()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, World!"
    x = txt.swapcase()
    st.write("Example Output:", x)

elif method == 'format':
    st.markdown("<h3>Format()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The format() method formats the specified value(s) and inserts them inside the string's placeholder(s).
    #### Syntax
    'string.format(value1, value2, ...)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, {}!"
    x = txt.format("Akshaya")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, {}!"
    x = txt.format("Akshaya")
    st.write("Example Output:", x)

elif method == 'format_map':
    st.markdown("<h3>Format Map()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The format_map() method is similar to the format() method, but it uses a dictionary.
    #### Syntax
    'string.format_map(dictionary)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, {name}!"
    dictionary = {"name": "Akshaya"}
    x = txt.format_map(dictionary)
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, {name}!"
    dictionary = {"name": "Akshaya"}
    x = txt.format_map(dictionary)
    st.write("Example Output:", x)

elif method == 'index':
    st.markdown("<h3>Index()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The index() method finds the first occurrence of the specified value. Raises an error if the value is not found.
    #### Syntax
    'string.index(value, start, end)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, welcome to my world."
    x = txt.index("welcome")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, welcome to my world."
    x = txt.index("welcome")
    st.write("Example Output:", x)

elif method == 'isalnum':
    st.markdown("<h3>Isalnum()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isalnum() method returns True if all characters in the string are alphanumeric (letters and numbers), otherwise False.
    #### Syntax
    'string.isalnum()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello123"
    x = txt.isalnum()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello123"
    x = txt.isalnum()
    st.write("Example Output:", x)

elif method == 'isalpha':
    st.markdown("<h3>Isalpha()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isalpha() method returns True if all characters in the string are alphabets (a-z, A-Z), otherwise False.
    #### Syntax
    'string.isalpha()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello"
    x = txt.isalpha()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello"
    x = txt.isalpha()
    st.write("Example Output:", x)
    
elif method == 'isascii':
    st.markdown("<h3>Isascii()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isascii() method returns True if all characters in the string are ASCII (0-127), otherwise False.
    #### Syntax
    'string.isascii()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello!"
    x = txt.isascii()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello!"
    x = txt.isascii()
    st.write("Example Output:", x)

elif method == 'isdecimal':
    st.markdown("<h3>Isdecimal()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isdecimal() method returns True if all characters in the string are decimals, otherwise False.
    #### Syntax
    'string.isdecimal()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "123"
    x = txt.isdecimal()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "123"
    x = txt.isdecimal()
    st.write("Example Output:", x)

elif method == 'isdigit':
    st.markdown("<h3>Isdigit()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isdigit() method returns True if all characters in the string are digits, otherwise False.
    #### Syntax
    'string.isdigit()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "12345"
    x = txt.isdigit()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "12345"
    x = txt.isdigit()
    st.write("Example Output:", x)

elif method == 'isidentifier':
    st.markdown("<h3>Isidentifier()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isidentifier() method returns True if the string is a valid identifier, otherwise False.
    #### Syntax
    'string.isidentifier()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Variable1"
    x = txt.isidentifier()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Variable1"
    x = txt.isidentifier()
    st.write("Example Output:", x)

elif method == 'islower':
    st.markdown("<h3>Islower()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The islower() method returns True if all characters in the string are lowercase, otherwise False.
    #### Syntax
    'string.islower()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "hello world"
    x = txt.islower()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "hello world"
    x = txt.islower()
    st.write("Example Output:", x)

elif method == 'isnumeric':
    st.markdown("<h3>Isnumeric()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isnumeric() method returns True if all characters in the string are numeric, otherwise False.
    #### Syntax
    'string.isnumeric()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "123456"
    x = txt.isnumeric()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "123456"
    x = txt.isnumeric()
    st.write("Example Output:", x)

elif method == 'isprintable':
    st.markdown("<h3>Isprintable()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isprintable() method returns True if all characters in the string are printable, otherwise False.
    #### Syntax
    'string.isprintable()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello!"
    x = txt.isprintable()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello!"
    x = txt.isprintable()
    st.write("Example Output:", x)

elif method == 'isspace':
    st.markdown("<h3>Isspace()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isspace() method returns True if all characters in the string are whitespaces, otherwise False.
    #### Syntax
    'string.isspace()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "   "
    x = txt.isspace()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "   "
    x = txt.isspace()
    st.write("Example Output:", x)

elif method == 'istitle':
    st.markdown("<h3>Istitle()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The istitle() method returns True if the string follows title case (each word starts with an uppercase letter), otherwise False.
    #### Syntax
    'string.istitle()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello World"
    x = txt.istitle()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello World"
    x = txt.istitle()
    st.write("Example Output:", x)

elif method == 'isupper':
    st.markdown("<h3>Isupper()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The isupper() method returns True if all characters in the string are uppercase, otherwise False.
    #### Syntax
    'string.isupper()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "HELLO"
    x = txt.isupper()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "HELLO"
    x = txt.isupper()
    st.write("Example Output:", x)

elif method == 'join':
    st.markdown("<h3>Join()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The join() method takes all items in an iterable and joins them into one string.
    #### Syntax
    'string.join(iterable)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    my_list = ['apple', 'banana', 'cherry']
    x = ", ".join(my_list)
    print(x)
    '''
    st.code(example_code, language='python')
    my_list = ['apple', 'banana', 'cherry']
    x = ", ".join(my_list)
    st.write("Example Output:", x)

elif method == 'ljust':
    st.markdown("<h3>Ljust()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The ljust() method returns a left-justified string with a specified width.
    #### Syntax
    'string.ljust(width, fillchar)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "banana"
    x = txt.ljust(10, '-')
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "banana"
    x = txt.ljust(10, '-')
    st.write("Example Output:", x)



elif method == 'lstrip':
    st.markdown("<h3>Lstrip()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The lstrip() method removes leading characters (spaces by default) from a string.
    #### Syntax
    'string.lstrip([chars])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "   hello"
    x = txt.lstrip()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "   hello"
    x = txt.lstrip()
    st.write("Example Output:", x)

elif method == 'maketrans':
    st.markdown("<h3>Maketrans()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The maketrans() method returns a translation table used for the translate() method.
    #### Syntax
    'string.maketrans(x, y, z)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "hello world"
    x = txt.maketrans("hlo", "HLO")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "hello world"
    trans_table = txt.maketrans("hlo", "HLO")
    st.write("Example Output:", trans_table)

elif method == 'partition':
    st.markdown("<h3>Partition()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The partition() method splits a string into three parts, the separator, and the parts before and after it.
    #### Syntax
    'string.partition(separator)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "I love apples"
    x = txt.partition("love")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "I love apples"
    x = txt.partition("love")
    st.write("Example Output:", x)

elif method == 'removeprefix':
    st.markdown("<h3>Removeprefix()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The removeprefix() method removes a specified prefix from the beginning of the string.
    #### Syntax
    'string.removeprefix(prefix)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "HelloWorld"
    x = txt.removeprefix("Hello")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "HelloWorld"
    x = txt.removeprefix("Hello")
    st.write("Example Output:", x)

elif method == 'removesuffix':
    st.markdown("<h3>Removesuffix()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The removesuffix() method removes a specified suffix from the end of the string.
    #### Syntax
    'string.removesuffix(suffix)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "HelloWorld"
    x = txt.removesuffix("World")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "HelloWorld"
    x = txt.removesuffix("World")
    st.write("Example Output:", x)

elif method == 'replace':
    st.markdown("<h3>Replace()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The replace() method replaces occurrences of a substring with another substring.
    #### Syntax
    'string.replace(old, new[, count])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "I like bananas"
    x = txt.replace("bananas", "apples")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "I like bananas"
    x = txt.replace("bananas", "apples")
    st.write("Example Output:", x)

elif method == 'rfind':
    st.markdown("<h3>rfind()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rfind() method finds the last occurrence of a substring in a string and returns its index.
    #### Syntax
    'string.rfind(sub[, start[, end]])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, welcome to the world of programming."
    x = txt.rfind("welcome")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, welcome to the world of programming."
    x = txt.rfind("welcome")
    st.write("Example Output:", x)

elif method == 'rindex':
    st.markdown("<h3>rindex()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rindex() method finds the last occurrence of a substring and returns its index.
    #### Syntax
    'string.rindex(sub[, start[, end]])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, welcome to the world of programming."
    x = txt.rindex("welcome")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, welcome to the world of programming."
    x = txt.rindex("welcome")
    st.write("Example Output:", x)

elif method == 'rjust':
    st.markdown("<h3>Rjust()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rjust() method returns a right-justified string with a specified width.
    #### Syntax
    'string.rjust(width, fillchar)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "banana"
    x = txt.rjust(10, '-')
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "banana"
    x = txt.rjust(10, '-')
    st.write("Example Output:", x)

elif method == 'rpartition':
    st.markdown("<h3>Rpartition()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rpartition() method splits the string into three parts based on the last occurrence of a separator.
    #### Syntax
    'string.rpartition(separator)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "I love apples"
    x = txt.rpartition("love")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "I love apples"
    x = txt.rpartition("love")
    st.write("Example Output:", x)

elif method == 'rsplit':
    st.markdown("<h3>Rsplit()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rsplit() method splits a string into a list, starting from the right.
    #### Syntax
    'string.rsplit([separator[, maxsplit]])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "apple, banana, cherry"
    x = txt.rsplit(", ")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "apple, banana, cherry"
    x = txt.rsplit(", ")
    st.write("Example Output:", x)

elif method == 'rstrip':
    st.markdown("<h3>Rstrip()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The rstrip() method removes any trailing characters (spaces by default) at the end of a string.
    #### Syntax
    'string.rstrip([chars])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "   banana   "
    x = txt.rstrip()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "   banana   "
    x = txt.rstrip()
    st.write("Example Output:", x)

elif method == 'split':
    st.markdown("<h3>Split()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The split() method splits a string into a list where each word is a list item.
    #### Syntax
    'string.split(separator, maxsplit)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "apple, banana, cherry"
    x = txt.split(", ")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "apple, banana, cherry"
    x = txt.split(", ")
    st.write("Example Output:", x)

elif method == 'splitlines':
    st.markdown("<h3>Splitlines()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The splitlines() method splits a string into a list, splitting by line breaks.
    #### Syntax
    'string.splitlines([keepends])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "hello\\nworld"
    x = txt.splitlines()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "hello\nworld"
    x = txt.splitlines()
    st.write("Example Output:", x)

elif method == 'startswith':
    st.markdown("<h3>Startswith()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The startswith() method returns True if a string starts with the specified prefix, otherwise False.
    #### Syntax
    'string.startswith(value, start, end)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "Hello, welcome to my world."
    x = txt.startswith("Hello")
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "Hello, welcome to my world."
    x = txt.startswith("Hello")
    st.write("Example Output:", x)

elif method == 'strip':
    st.markdown("<h2>Strip()</h2>", unsafe_allow_html=True)
    st.markdown('''
    The strip() method removes leading and trailing characters (spaces by default) from a string.
    #### Syntax
    'string.strip([chars])'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "   hello   "
    x = txt.strip()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "   hello   "
    x = txt.strip()
    st.write("Example Output:", x)



elif method == 'title':
    st.markdown("<h3>Title()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The title() method converts the first character of each word to uppercase.
    #### Syntax
    'string.title()'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "welcome to the jungle"
    x = txt.title()
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "welcome to the jungle"
    x = txt.title()
    st.write("Example Output:", x)

elif method == 'translate':
    st.markdown("<h3>Translate()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The translate() method returns a string where some specified characters are replaced, using a translation table.
    #### Syntax
    'string.translate(table)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "hello world"
    trans_table = str.maketrans("hlo", "HLO")
    x = txt.translate(trans_table)
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "hello world"
    trans_table = str.maketrans("hlo", "HLO")
    x = txt.translate(trans_table)
    st.write("Example Output:", x)



elif method == 'zfill':
    st.markdown("<h3>Zfill()</h3>", unsafe_allow_html=True)
    st.markdown('''
    The zfill() method pads a string with zeros (0) on the left, to fill the specified width.
    #### Syntax
    'string.zfill(width)'
    ''')
    #### **Example Code**
    example_code = '''
    ##### Example Code
    txt = "42"
    x = txt.zfill(5)
    print(x)
    '''
    st.code(example_code, language='python')
    txt = "42"
    x = txt.zfill(5)
    st.write("Example Output:", x)


# Try it yourself! 
st.markdown('<h4>Try it yourself!</h4>', unsafe_allow_html=True)

# Code input area for users to enter their Python code
code = st.text_area("Enter your Python code here:", height=200, value='')

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
        output = new_stdout.getvalue()
        st.text_area("Output:", output, height=150)
    except Exception as e:
        # Handle any errors
        st.error(f"Error: {e}")
    
    # Reset stdout
    sys.stdout = old_stdout
