import streamlit as st


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

# Options for the string manipulation methods
options = [
    "Get Length of String",
    "Split String",
    "Reverse Split String",
    "Split Lines",
    "Count Substring",
    "Find Substring",
     "Split Lines",
    "Count Substring",
    "Find Substring",
    "Find Last Substring",
    "Index Substring",
    "Find Last Index Substring",
    "Split Lines",
    "Count Substring",
    "Find Substring",
    "Find Last Substring",
    "Index Substring",
    "Find Last Index Substring",
    "Convert to Uppercase",
    "Convert to Lowercase",
    "Swap Case",
    "Title Case",
    "Split Lines",
    "Count Substring",
    "Find Substring",
    "Find Last Substring",
    "Index Substring",
    "Find Last Index Substring",
    "Convert to Uppercase",
    "Convert to Lowercase",
    "Swap Case",
    "Title Case",
    "Capitalize",
    "Is ASCII",
    "Is Alpha",
    "Is Alphanumeric",
    "Is Lowercase",
    "Is Uppercase",
    "Check Title Case",
    "Check Digits",
    "Check Decimal",
    "Check Numeric",
    "Check Whitespace",
    "Check Starts With",
    "Check Ends With",
    "Partition String",
    "R Partition String",
    "Replace Substring",
    "Center String",
    "Left Justify String",
    "Right Justify String",
    "Case Fold String",
    "Remove Prefix",
    "Zero Fill",
    "Join Iterable",
    "Strip Characters",
    "Left Strip Characters",
    "Right Strip Characters",
    "Check Printable",
    "Check Identifier",
    "Make Translation Table",
    "Translate String",
    "Check Substring",
    "Concatenate Strings",
    "Make Translation Table",
    "Translate String",
    "Check Substring",
    "Concatenate Strings",
    "Repeat String",
    "Check Equality"
]

st.title("String Manipulation Methods")
st.write("This app provides an introduction to various string manipulation methods without using any built-in functions.")

# Create a selectbox for the user to choose a function
selection = st.selectbox('Choose a string manipulation method', options)

# Match the selected option
match selection:
    case "Get Length of String":
        st.code("""
def length(s):
    '''Get the length of a String.
        Parameters:
          string - The string to find length
        Returns:
          int: The length of the value in the String.

        Example:
         s='Hello'
         length(s)
         output - 5
    '''
    l = 0
    for i in s:
        l += 1
    return l
        """)

    case "Split String":
        st.code("""
def split_(s, delimiter=' ', max_split=-1):
    '''Split a string into a list of substrings based on a specified separator.
    Parameters:
    - string - The string to be split.
    - delimiter(str, Optional) - Specifies the delimiter character or substring.
      If not provided or set to None, the default is to split at whitespace characters.
    - maxsplit (int, optional): Specifies the maximum number of splits to perform.
      If provided, the string is split at most maxsplit times, and the remaining part of the string
      is returned as the last element of the resulting list. Default is -1, indicating no limit.

    Returns:
      list of str: A list of substrings obtained by splitting the original string based on the specified separator.
    Example:
      s="a,b,c,d,e"
      s.split_(',',2)
      Output - ['a','b','c,d,e']
    '''
    split_list = []
    n = length(delimiter)  # Assume length is defined elsewhere
    w = ''
    j, k = -1, -1
    for i in range(length(s)):
        if s[i:i+n] == delimiter and max_split != 0:
            split_list.append(w)
            w = ''
            max_split -= 1
            j, k = i, i + n
        if i in range(j, k):
            continue
        else:
            w += s[i]
    split_list.append(w)
    return split_list
        """)

    case "Reverse Split String":
        st.code("""
def r_split(s, sep=" ", max_split=-1):
    '''Split a string into a list of substrings starting from the right based on a specified separator.
    Parameters:
      - input_string (str): The string to be split.
      - separator (str, optional): Specifies the delimiter character or substring.
        If not provided or set to None, the default is to split at whitespace characters.
      - maxsplit (int, optional): Specifies the maximum number of splits to perform.
        If provided, the string is split at most maxsplit times, and the remaining part of the string
        is returned as the first element of the resulting list. Default is -1, indicating no limit.
    Returns:
      list of strings: A list of substrings obtained by splitting the original string based on the specified separator.
    Example:
      s="a,b,c,d,e"
      s.r_split(',',2)
      Output - ['a,b,c','d','e']
    '''
    split_list = []
    n = length(sep)  # Assume length is defined elsewhere
    w = ''
    j = k = -1
    for i in range(length(s) - 1, -1, -1):
        if s[i-n+1:i+1] == sep and max_split != 0:
            split_list.insert(0, w)
            w = ''
            max_split -= 1
            j, k = i, i - n
        if i in range(k + 1, j + 1):
            continue
        else:
            w = s[i] + w
    split_list.insert(0, w)
    return split_list
        """)

    case "Split Lines":
        st.code("""
def split_lines(s, keepends=False):
    '''
    Return a list of lines from the input string, breaking at line boundaries.
    Parameters:
    - input_string (str): The string to be split into lines.
    - keepends (bool, optional): If True, line breaks are included in the resulting lines.
      If False (default), line breaks are stripped from the lines.
    Returns:
      list of str: A list of lines obtained by splitting the original string at line boundaries.
    Example:
    - s = "First line\\n Second line\\n Third line"
      split_lines(s)
      Output - ['First line', 'Second line', 'Third line']
    - split_lines(s, keepends=True)
      Output - ['First line\\n', 'Second line\\n', 'Third line\\n']
    '''
    lines_list = []
    sentence = ''
    for i in range(len(s)):
        if s[i:i + 2] == '\\n' or s[i] == '\\n':
            if keepends:
                sentence += '\\n'
            lines_list.append(sentence)
            sentence = ''
        else:
            sentence += s[i]
    lines_list.append(sentence)
    return lines_list
        """)

    case "Count Substring":
        st.code("""
def count_(s, sub, start=0, end=-1):
    '''
    Count the occurrences of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for occurrences of the substring.
    - sub (str): The substring to count within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is -1, meaning the search continues to the end of the string.
    Returns:
    - int: The number of occurrences of the substring in the specified range.
    Example:
     s = 'hello all'
     count_(s, 'l')
     Output - 4
     count_(s, 'l', 3, 5)
     Output - 1
    '''
    n = len(sub)
    if end == -1: end = len(s)
    count = 0
    for i in range(start, end):
        if sub == s[i:i + n]:
            count += 1
    return count
        """)

    case "Find Substring":
        st.code("""
def find_(s, sub, start=0, end=-1):
    '''
    Find the index of the first occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the first occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is -1, meaning the search continues to the end of the string.
    Returns:
      int: The index of the first occurrence of the substring, or -1 if not found.
    Example:
    s = 'Hello World'
    find_(s, 'll')
    Output - 2
    find_(s, 'z')
    Output - -1
    '''
    n = len(sub)
    if end == -1: end = len(s)
    for i in range(start, end):
        if sub == s[i:i + n]:
            return i
    return -1
        """)
    
    case "Split Lines":
        st.code("""
def split_lines(s, keepends=False):
    # (Function code here)
        """)

    case "Count Substring":
        st.code("""
def count_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Substring":
        st.code("""
def find_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Last Substring":
        st.code("""
def rfind_(s, sub, start=0, end=-1):
    '''
    Find the index of the last occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the last occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is -1,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the last occurrence of the substring, or -1 if not found.
    Example:
      s = 'Hello World'
      rfind_(s, 'l')
      Output - 9
      rfind_(s, 'z')
      Output - -1
    '''
    n = len(sub)
    if end == -1: end = len(s)
    for i in range(end - 1, start - 1, -1):
        if sub == s[i:i + n]:
            return i
    return -1
        """)

    case "Index Substring":
        st.code("""
def index_(s, sub, start=0, end=-1):
    '''
    Find the index of the first occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the first occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is -1,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the first occurrence of the substring.
    Raises:
      ValueError: If the substring is not found in the specified range.
    Example:
      s = 'Hello World'
      index_(s, 'e')
      Output - 1
      index_(s, 'z')
      Output - "ValueError: substring not found"
    '''
    n = len(sub)
    if end == -1: end = len(s)
    indx = -1
    for i in range(start, end):
        if sub == s[i:i + n]:
            indx = i
            break
    assert indx != -1, 'ValueError: substring not found'
    return indx
        """)

    case "Find Last Index Substring":
        st.code("""
def rindex_(s, sub, start=0, end=-1):
    '''
    Find the index of the last occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the last occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is -1,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the last occurrence of the substring.
    Raises:
      ValueError: If the substring is not found in the specified range.
    Example:
      s = 'Hello World'
      rindex_(s, 'o')
      Output - 7
      rindex_(s, 'z')
      Output - "ValueError: substring not found"
    '''
    n = len(sub)
    if end == -1: end = len(s)
    indx = -1
    for i in range(end - 1, start - 1, -1):
        if sub == s[i:i + n]:
            indx = i
            break
    assert indx != -1, 'ValueError: substring not found'
    return indx
        """)
    
    case "Split Lines":
        st.code("""
def split_lines(s, keepends=False):
    # (Function code here)
        """)

    case "Count Substring":
        st.code("""
def count_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Substring":
        st.code("""
def find_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Last Substring":
        st.code("""
def rfind_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Index Substring":
        st.code("""
def index_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Last Index Substring":
        st.code("""
def rindex_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Convert to Uppercase":
        st.code("""
def upper_(s):
    '''
    Convert all lowercase characters in the given string to uppercase.
    Parameters:
    - input_string (str): The string to convert to uppercase.
    Returns:
      str: A new string with all lowercase characters converted to uppercase.
    Example:
      s='Hello World @123'
      upper_(s)
      Output - HELLO WORLD @123
    '''
    s_upper = ''
    for i in s:
        if ord(i) in range(97, 123):
            s_upper += chr(ord(i) - 32)
        else:
            s_upper += i
    return s_upper
        """)

    case "Convert to Lowercase":
        st.code("""
def lower_(s):
    '''
    Convert all uppercase characters in the given string to lowercase.
    Parameters:
    - input_string (str): The string to convert to lowercase.
    Returns:
      str: A new string with all uppercase characters converted to lowercase.
    Example:
      s='Hello World @123'
      lower_(s)
      Output - hello world @123
    '''
    s_lower = ''
    for i in s:
        if ord(i) in range(65, 91):
            s_lower += chr(ord(i) + 32)
        else:
            s_lower += i
    return s_lower
        """)

    case "Swap Case":
        st.code("""
def swap_case(s):
    '''
    Swap the case of each character in the given string.
    Parameters:
    - input_string (str): The string to swap the case.
    Returns:
      str: A new string with uppercase characters converted to lowercase
         and lowercase characters converted to uppercase.
    Example:
      s='HeLLo WorLd @123'
      swap_case(s)
      Output - hEllO wORlD @123
    '''
    s_swap = ''
    for i in s:
        if ord(i) in range(97, 123):
            s_swap += chr(ord(i) - 32)
        elif ord(i) in range(65, 91):
            s_swap += chr(ord(i) + 32)
        else:
            s_swap += i
    return s_swap
        """)

    case "Title Case":
        st.code("""
def title_(s):
    '''
    Return a titlecased version of the given string.
    The titlecased version of a string is where the first character of each word is
    capitalized and the rest of the characters are lowercase.

    Parameters:
    - input_string (str): The string to be titlecased.
    Returns:
      str: A new string with the first character of each word capitalized.
    Example:
      s='hello @123welcome'
      title_(s)
      Output - Hello @123Welcome
    '''
    s = []
    str_list = s.split()  # Assuming you have a split method or use str.split()
    for word in str_list:
        w = ''
        c = 0
        for i in word:
            if ord(i) in range(97, 123) and c == 0:
                w += chr(ord(i) - 32)
                c += 1
            elif (ord(i) in range(65, 91)) and c == 0:
                w += i
                c += 1
            elif ord(i) in range(65, 91):
                w += chr(ord(i) + 32)
            else:
                w += i
        s.append(w)
    z = ' '.join(s)
    return z
        """)
    
    case "Split Lines":
        st.code("""
def split_lines(s, keepends=False):
    # (Function code here)
        """)

    case "Count Substring":
        st.code("""
def count_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Substring":
        st.code("""
def find_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Last Substring":
        st.code("""
def rfind_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Index Substring":
        st.code("""
def index_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Find Last Index Substring":
        st.code("""
def rindex_(s, sub, start=0, end=-1):
    # (Function code here)
        """)

    case "Convert to Uppercase":
        st.code("""
def upper_(s):
    # (Function code here)
        """)

    case "Convert to Lowercase":
        st.code("""
def lower_(s):
    # (Function code here)
        """)

    case "Swap Case":
        st.code("""
def swap_case(s):
    # (Function code here)
        """)

    case "Title Case":
        st.code("""
def title_(s):
    # (Function code here)
        """)

    case "Capitalize":
        st.code("""
def capitalize_(s):
    '''
    Return a copy of the given string with its first character capitalized and the rest lowercase.
    Parameters:
    - input_string (str): The string to be capitalized.
    Returns:
      str: A new string with the first character capitalized and the rest in lowercase.
    Example:
      s= 'HELLO WorLd'
      capitalize_(s)
      output- Hello world
    '''
    s_capital = ''
    c = 0
    for i in s:
        if ord(i) in range(97, 123) and c == 0:
            s_capital += chr(ord(i) - 32)
            c += 1
        elif (ord(i) in range(65, 91) and c == 0) or (ord(i) in range(48, 58)):
            s_capital += i
            c += 1
        elif ord(i) in range(65, 91):
            s_capital += chr(ord(i) + 32)
        else:
            s_capital += i
    return s_capital
        """)

    case "Is ASCII":
        st.code("""
def is_ascii(s):
    """
    """
    Check if all characters in the given string are ASCII characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are ASCII, False otherwise.
    Example:
      s = 'hello'
      is_ascii(s)
      Output - True"""
    """
    for i in s:
        if ord(i) not in range(0, 128):
            return False
    return True
        """)

    case "Is Alpha":
        st.code("""
def is_alpha(s):"""

    """Check if all characters in the given string are alphabetic (letters).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are alphabetic, False otherwise.
    Example:
      s = 'hello'
      is_alpha(s)
      Output - True
      s = 'Hello World'
      is_alpha(s)
      Output - False"""
  """
    for i in s:
        if ord(i) not in range(65, 91) and ord(i) not in range(97, 123):
            return False
    return True
        """)

    case "Is Alphanumeric":
        st.code("""
def is_alnum(s):
    '''
    Check if all characters in the given string are alphanumeric (letters or digits).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are alphanumeric, False otherwise.
    Example:
      s = 'Hello123'
      is_alnum(s)
      Output - True
      s = 'Hello 123'
      is_alnum(s)
      Output - False
    '''
    for i in s:
        if ord(i) not in range(65, 91) and ord(i) not in range(97, 123) and ord(i) not in range(48, 58):
            return False
    return True
        """)

    case "Is Lowercase":
        st.code("""
def is_lower(s):
    '''
    Check if all characters in the given string are lowercase.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are lowercase, False otherwise.
    Example:
      s = 'hello all'
      is_lower(s)
      Output - True
      s = 'Hello all'
      is_lower(s)
      Output - False
    '''
    for i in s:
        if ord(i) in range(65, 91):
            return False
    return True
        """)

    case "Is Uppercase":
        st.code("""
def is_upper(s):
    '''
    Check if all characters in the given string are uppercase.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are uppercase, False otherwise.
    Example:
      s = 'HELLO ALL'
      is_upper(s)
      Output - True
      s = 'HELLO All'
      is_upper(s)
      Output - False
    '''
    for i in s:
        if ord(i) in range(97, 123):
            return False
    return True
        """)
        
    case "Check Title Case":
        st.code("""
def is_title(s):
    '''
    Check if the given string is titlecased.
    A string is considered titlecased if it consists of words separated by spaces,
    and each word starts with an uppercase character, followed by lowercase characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if the string is titlecased, False otherwise.
    Example:
      s='Hello All'
      is_title(s)
      Output - True
      s='Hello ALL'
      is_title(s)
      Output - False
    '''
    words = s.split()  # Assuming you have a split method or use str.split()
    for word in words:
        if not word:
            return False
        if not (word[0].isupper() and word[1:].islower()):
            return False
    return True
        """)

    case "Check Digits":
        st.code("""
def is_digit(s):
    '''
    Check if all characters in the given string are digits.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are digits, False otherwise.
    Example:
      s='1234567'
      is_digit(s)
      Output - True
      s='123 456'
      is_digit(s)
      Output - False
    '''
    return all(c.isdigit() for c in s)
        """)

    case "Check Decimal":
        st.code("""
def is_decimal(s):
    '''
    Check if all characters in the given string are decimal characters.
    Decimal characters are those that can be used to represent numbers in base 10.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are decimal, False otherwise.
    Example:
      s='123'
      is_decimal(s)
      Output - True
      s='12.56'
      is_decimal(s)
      Output - False
    '''
    return all(c.isdigit() for c in s)
        """)

    case "Check Numeric":
        st.code("""
def is_numeric(s):
    '''
    Check if all characters in the given string are numeric characters.
    Numeric characters include digits, numeric characters from other scripts,
    and characters that represent numeric values (like fractions).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are numeric, False otherwise.
    Example:
      s='2345'
      is_numeric(s)
      Output - True
      s='12abc'
      is_numeric(s)
      Output - False
    '''
    return all(c.isdigit() for c in s)
        """)
        
    case "Check Whitespace":
        st.code("""
def is_space(s):
    '''
    Check if all characters in the given string are whitespace characters.
    Whitespace characters include spaces, tabs, and newline characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are whitespace, False otherwise.
    Example:
      s='   '
      is_space(s)
      Output - True
      s=' \\n '
      is_space(s)
      Output - True
    '''
    return all(c in [' ', '\\n', '\\t', '\\r', '\\f'] for c in s)
        """)

    case "Check Starts With":
        st.code("""
def starts_with(s, prefix, start=0, end=None):
    '''
    Check if the given string starts with a specified prefix.
    Parameters:
    - input_string (str): The string to check.
    - prefix (str): The prefix to check for at the beginning of the string.
    - start (int, optional): The starting index for the check. Default is 0.
    - end (int, optional): The ending index for the check. Default is None,
      meaning the check continues to the end of the string.
    Returns:
      bool: True if the string starts with the specified prefix, False otherwise.
    Example:
      s='Hello World'
      starts_with(s, 'Hello')
      Output - True
    '''
    if end is None:
        end = len(s)
    return s[start:end].startswith(prefix)
        """)

    case "Check Ends With":
        st.code("""
def ends_with(s, suffix, start=0, end=None):
    '''
    Check if the given string ends with a specified suffix.
    Parameters:
    - input_string (str): The string to check.
    - suffix (str): The suffix to check for at the end of the string.
    - start (int, optional): The starting index for the check. Default is 0.
    - end (int, optional): The ending index for the check. Default is None,
      meaning the check continues to the end of the string.
    Returns:
      bool: True if the string ends with the specified suffix, False otherwise.
    Example:
      s="Hello World"
      ends_with(s, 'd')
      Output - True
    '''
    if end is None:
        end = len(s)
    return s[start:end].endswith(suffix)
        """)

    case "Partition String":
        st.code("""
def partition_(s, sep):
    '''
    Partition the given string into three parts based on the first occurrence of a separator.
    Parameters:
    - input_string (str): The string to be partitioned.
    - separator (str): The separator used to split the string.
    Returns:
      tuple: A tuple containing three parts of the string: the text before the separator,
           the separator itself, and the text after the separator.
    Example:
      s='Hello World'
      partition_(s, 'l')
      Output - ('Hel', 'l', 'o World')
    '''
    parts = s.split(sep, 1)  # Split on the first occurrence of the separator
    if len(parts) == 1:
        return (parts[0], '', '')  # No separator found
    return (parts[0], sep, parts[1])
        """)

    case "R Partition String":
        st.code("""
def r_partition(s, sep):
    '''
    Partition the given string into three parts based on the last occurrence of a separator.
    Parameters:
    - input_string (str): The string to be partitioned.
    - separator (str): The separator used to split the string.
    Returns:
      tuple: A tuple containing three parts of the string: the text before the last separator,
           the last separator itself, and the text after the last separator.
    Example:
      s='abcdedcba'
      r_partition(s, 'c')
      Output - ('abcded','c','ba')
    '''
    parts = s.rsplit(sep, 1)  # Split on the last occurrence of the separator
    if len(parts) == 1:
        return (parts[0], '', '')  
    return (parts[0], sep, parts[1])
        """)

    case "Replace Substring":
        st.code("""
def replace_(s, old, new, count=-1):
    '''
    Replace occurrences of a specified substring with another substring in the given string.
    Parameters:
    - input_string (str): The string in which replacements will be performed.
    - old_str (str): The substring to be replaced.
    - new_str (str): The substring to replace occurrences of `old_str`.
    - count (int, optional): Maximum number of occurrences to replace. Default is -1,
      meaning all occurrences will be replaced.
    Returns:
      str: A new string with replacements.
    Example:
      s='Python Programming Language'
      replace(s, 'ng', 'z')
      Output - 'Python Programmiz Lazuage'
    '''
    return s.replace(old, new, count)  # Using Python's built-in replace for simplicity
        """)

    case "Center String":
        st.code("""
def center_(s, width, fillchar=' '):
    '''
    Return a centered string within a specified width.
    Parameters:
    - input_string (str): The string to be centered.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces around the string.
      Default is a space (' ').
    Returns:
      str: A new string centered within the specified width.
    Example:
      s='Hello'
      center(s, 10, '*')
      Output - '**Hello***'
    '''
    str_len = len(s)
    n = width - str_len
    return fillchar * (n // 2) + s + fillchar * (n - n // 2)
        """)

    case "Left Justify String":
        st.code("""
def l_just(s, width, fillchar=' '):
    '''
    Return a left-justified string within a specified width.
    Parameters:
    - input_string (str): The string to be left-justified.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces to the right of the string.
      Default is a space (' ').
    Returns:
      str: A new string left-justified within the specified width.
    Example:
      s='Hello'
      l_just(s, 10, '*')
      Output - 'Hello*****'
    '''
    str_len = len(s)
    n = width - str_len
    return s + fillchar * n
        """)

    case "Right Justify String":
        st.code("""
def r_just(s, width, fillchar=' '):
    '''
    Return a right-justified string within a specified width.
    Parameters:
    - input_string (str): The string to be right-justified.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces to the left of the string.
      Default is a space (' ').
    Returns:
      str: A new string right-justified within the specified width.
    Example:
      s='Hello'
      r_just(s, 10, '*')
      Output - '*****Hello'
    '''
    str_len = len(s)
    n = width - str_len
    return fillchar * n + s
        """)

    case "Case Fold String":
        st.code("""
def case_fold(s):
    '''
    Return a casefolded version of the given string.
    Casefolding is similar to lowercase conversion but more aggressive, removing
    all case distinctions from the string. It is suitable for case-insensitive comparisons.
    Parameters:
    - input_string (str): The string to be casefolded.
    Returns:
      str: A new string with all case distinctions removed.
    Example:
      s= 'HELLO World'
      case_fold(s)
      Output - 'hello world'
    '''
    return s.lower()  # Using Python's built-in lower for simplicity
        """)

    case "Remove Prefix":
        st.code("""
def remove_prefix(s, prefix):
    '''
    Remove a specified prefix from the given string.
    Parameters:
    - input_string (str): The string from which the prefix will be removed.
    - prefix (str): The prefix to be removed.
    Returns:
      str: A new string with the specified prefix removed.
    Example:
      s='@@@@Hello'
      remove_prefix(s, '@@@@')
      Output - 'Hello'
    '''
    length = len(prefix)
    if s.startswith(prefix):
        return s[length:]
    return s
        """)    
      
    case "Zero Fill":
        st.code("""
def z_fill(s, width):
    '''
    Pad the given string with zeros on the left to achieve a specified width.
    Parameters:
    - input_string (str): The string to be padded.
    - width (int): The minimum width of the resulting string.
    Returns:
      str: A new string padded with zeros on the left.
    Example:
      s='234'
      z_fill(s, 6)
      Output - '00234'
    '''
    str_len = len(s)
    n = width - str_len
    return '0' * n + s
        """)

    case "Join Iterable":
        st.code("""
def join_(iterable, sep=''):
    '''
    Concatenate the elements of an iterable with a specified separator.
    Parameters:
    - iterable (iterable): An iterable containing elements to be joined.
    - separator (str): The string used to join the elements.
    Returns:
      str: A new string created by concatenating the elements with the specified separator.
    Example:
      join(['1', '2', '3', '4', '5'], '-') 
      Output - '1-2-3-4-5'
    '''
    return sep.join(map(str, iterable))  # Using Python's built-in join for simplicity
        """)

    case "Strip Characters":
        st.code("""
def strip_(s, char=' '):
    '''
    Return a copy of the given string with leading and trailing characters removed.
    Parameters:
    - input_string (str): The string to be stripped.
    - chars (str, optional): A string specifying the set of characters to be removed.
      If not provided, whitespaces are removed.
    Returns:
      str: A new string with leading and trailing characters removed.
    Example:
      s='    hello    '
      strip_(s)
      Output - 'hello'
    '''
    return s.strip(char)  # Using Python's built-in strip for simplicity
        """)  
    
    case "Left Strip Characters":
        st.code("""
def l_strip(s, char=' '):
    new_str = ''
    start = -1
    end = len(s)
    for i in range(len(s)):
        if s[i] in char:
            start = i
            continue
        else:
            break
    new_str = s[start+1:end]
    return new_str
        """)

    case "Right Strip Characters":
        st.code("""
def r_strip(s, char=' '):
    new_str = ''
    start = -1
    end = len(s)
    for i in range(len(s)-1, -1, -1):
        if s[i] in char:
            end = i
            continue
        else:
            break
    new_str = s[start+1:end]
    return new_str
        """)

    case "Check Printable":
        st.code("""
def is_printable(s):
    pList = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''
    for i in s:
        if i not in pList:
            return False
    return True
        """)

    case "Check Identifier":
        st.code("""
def is_identifier(s):
    id_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    if ord(s[0]) in range(48, 58):
        return False
    for i in s:
        if i not in id_list:
            return False
    return True
        """)
    
    case "Make Translation Table":
        st.code("""
def make_trans(from_chars, to_chars, delete_chars=''):
    assert len(from_chars) == len(to_chars), "'ValueError': the first two maketrans arguments must have equal length"
    dic = {}
    for i in range(len(from_chars)):
        dic[ord(from_chars[i])] = ord(to_chars[i])
    for i in delete_chars:
        dic[ord(i)] = None
    return dic
        """)

    case "Translate String":
        st.code("""
def translate_(s, dic):
    str_trans = ''
    for i in s:
        if ord(i) in dic:
            if dic[ord(i)] is None:
                continue
            str_trans += chr(dic[ord(i)])
        else:
            str_trans += i
    return str_trans
        """)

    case "Check Substring":
        st.code("""
def __contains__(s, value):
    return value in s
        """)

    case "Concatenate Strings":
        st.code("""
def __add__(s, other):
    if isinstance(other, str):
        return s + other
    else:
        return "Error"
        """)

    case "Repeat String":
        st.code("""
def __mul__(s, n):
    if isinstance(n, int):
        return s * n
    else:
        return 'Error'
        """)

    case "Check Equality":
        st.code("""
def __eq__(s, other):
    if len(s) != len(other):
        return False
    for i, j in zip(s, other):
        if i != j:
            return False
    return True
        """)
