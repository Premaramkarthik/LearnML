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

st.title("Understanding Functions in Python")

# Introduction
st.header("Introduction")
st.write("""
A function in Python is a block of code that only runs when it is called. 
Functions help in organizing code, making it reusable, and improving readability. 
Python provides many built-in functions, and you can also create your own functions known as **user-defined functions**.
""")


st.write("""
- **def**: This keyword is used to define a function.
- **function_name**: This is the name you give to the function, following naming conventions.
- **parameters**: These are inputs passed to the function (optional).
- **docstring**: An optional string that describes what the function does.
- **return**: This is used to return a value from the function (optional).
""")


# Function Example
st.subheader("Function Example")
normal_function_example = """
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
"""
st.code(normal_function_example, language='python')

st.write("""
In this example, `greet` is a simple function that takes one argument (`name`) and prints a greeting message. When `greet("Alice")` is called, it prints `Hello, Alice!`.
""")

# Function Arguments Overview
st.header("Types of Function Arguments")
st.write("""
Python functions can accept various types of arguments:

1. **Default Arguments**: Assigns a default value to a parameter if no value is provided during the function call.
2. **Keyword (Named) Arguments**: Passes arguments using the parameter name, allowing you to skip the order of parameters.
3. **Positional Arguments**: Passes arguments in the order they are defined in the function.
4. **Arbitrary Arguments (`*args`)**: Allows a function to accept any number of positional arguments.
5. **Arbitrary Keyword Arguments (`**kwargs`)**: Allows a function to accept any number of keyword arguments.
""")

# Default Arguments
st.header("1. Default Arguments")
st.write("""
Default arguments are used to assign a default value to a function parameter. If no argument is provided for that parameter, the default value is used.
""")

# Default Arguments Example
st.subheader("Default Arguments Example")
default_arg_example = """
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # No argument passed, so the default value 'Guest' is used
greet("Alice")  # Argument 'Alice' is passed, so it overrides the default
"""
st.code(default_arg_example, language='python')

st.write("""
In this example, the `greet` function has a default argument `name="Guest"`. If no argument is passed, it uses the default value (`Guest`). If an argument is provided, it overrides the default.
""")

# Keyword Arguments
st.header("2. Keyword (Named) Arguments")
st.write("""
Keyword arguments (also called named arguments) allow you to pass arguments to a function by specifying the parameter name. This makes the function call more readable and flexible.
""")

# Keyword Arguments Example
st.subheader("Keyword Arguments Example")
keyword_arg_example = """
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Using keyword arguments
display_info(age=25, name="Alice")
"""
st.code(keyword_arg_example, language='python')

st.write("""
In this example, the order of arguments doesn't matter because the arguments are passed using the parameter names (`name="Alice"`, `age=25`).
""")

# Positional Arguments
st.header("3. Positional Arguments")
st.write("""
Positional arguments are the most common way to pass arguments to a function. They are passed in the same order as they are defined in the function. The number of arguments must match the number of parameters.
""")

# Positional Arguments Example
st.subheader("Positional Arguments Example")
positional_arg_example = """
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Using positional arguments
display_info("Alice", 25)
"""
st.code(positional_arg_example, language='python')

st.write("""
In this example, the arguments `"Alice"` and `25` are passed in the order that the parameters `name` and `age` are defined in the function.
""")

# Arbitrary Arguments
st.header("4. Arbitrary Arguments (*args)")
st.write("""
Sometimes, you may want a function to accept a variable number of positional arguments. This can be achieved using `*args`. The `*args` collects all extra positional arguments passed to the function into a tuple.
""")

# Arbitrary Arguments Example
st.subheader("Arbitrary Arguments Example")
arbitrary_args_example = """
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(f"Total: {total}")

add_numbers(1, 2, 3, 4, 5)  # You can pass as many arguments as needed
"""
st.code(arbitrary_args_example, language='python')

st.write("""
In this example, the function `add_numbers` takes any number of arguments and adds them up. The `*args` collects all positional arguments passed and stores them in a tuple.
""")

# Arbitrary Keyword Arguments
st.header("5. Arbitrary Keyword Arguments (**kwargs)")
st.write("""
Similar to `*args`, you can also pass a variable number of keyword arguments to a function using `**kwargs`. The `**kwargs` collects all extra keyword arguments and stores them in a dictionary.
""")

# Arbitrary Keyword Arguments Example
st.subheader("Arbitrary Keyword Arguments Example")
arbitrary_kwargs_example = """
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, location="New York")
"""
st.code(arbitrary_kwargs_example, language='python')

st.write("""
In this example, the function `display_info` takes any number of keyword arguments. The `**kwargs` collects them into a dictionary, and the function prints each key-value pair.
""")

# Key Differences
st.header("Summary of Argument Types")
st.write("""
1. **Default Arguments**: Provide default values for parameters.
2. **Keyword (Named) Arguments**: Pass arguments by specifying parameter names.
3. **Positional Arguments**: Pass arguments in the order they are defined in the function.
4. **Arbitrary Positional Arguments (`*args`)**: Accept any number of positional arguments.
5. **Arbitrary Keyword Arguments (`**kwargs`)**: Accept any number of keyword arguments.
""")


# Types of Functions
st.header("Types of Functions")

# Select box for function types
function_type = st.selectbox(
    "Select the type of function to learn more about:",
    ("Built-in Functions", "Lambda Functions", "Recursive Functions","Decorators")
)

# Built-in Functions
if function_type == "Built-in Functions":
    st.subheader("Built-in Functions")
    st.write("""
    Python provides many built-in functions that you can use without defining them. 
    Some common built-in functions include `len()`, `max()`, `sum()`, `min()`, and `sorted()`.
    """)
    
    built_in_example = """
    numbers = [1, 2, 3, 4, 5]
    print(len(numbers))  # Returns the length of the list
    print(max(numbers))  # Returns the maximum element in the list
    """
    st.code(built_in_example, language='python')

    st.write("""
    In this example, `len(numbers)` returns the number of elements in the list, 
    and `max(numbers)` returns the largest number in the list.
    """)

# Lambda Functions
elif function_type == "Lambda Functions":
    st.subheader("Lambda Functions")
    st.write("""
    A **lambda function** is a small anonymous function. 
    A lambda function can have any number of arguments, but only one expression. 
    The expression is evaluated and returned. Lambda functions are often used for short-term operations.
    """)
    
    lambda_example = """
    # Syntax of lambda function
    lambda arguments: expression

    # Example
    square = lambda x: x * x
    print(square(5))  # Outputs 25
    """
    st.code(lambda_example, language='python')

    st.write("""
    Lambda functions are often used with functions like `map()`, `filter()`, and `reduce()`. 
    For example, `map()` can apply a lambda function to all elements of an iterable.
    """)

# Recursive Functions
elif function_type == "Recursive Functions":
    st.subheader("Recursive Functions")
    st.write("""
    A **recursive function** is a function that calls itself. 
    Recursion can solve problems that can be broken down into smaller, similar sub-problems.
    """)
    
    recursive_example = """
    # Example of a recursive function to calculate factorial

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    # Calling the recursive function
    print(factorial(5))  # Outputs 120
    """
    st.code(recursive_example, language='python')

    st.write("""
    In this example, the `factorial()` function calls itself to compute the factorial of a number. 
    Recursion is a powerful tool, but it should be used carefully to avoid infinite loops or excessive memory usage.
    """)


# Decorators
elif function_type == "Decorators":
    st.subheader("Decorators")
    st.write("""
    A **decorator** is a special type of function that modifies the behavior of another function. 
    Decorators allow you to wrap another function and extend its behavior without permanently modifying it.
    """)
    
    decorator_example = """
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    # Calling the decorated function
    say_hello()
    """
    st.code(decorator_example, language='python')

    st.write("""
    In this example, `my_decorator` is a decorator that wraps the `say_hello` function. 
    When `say_hello` is called, it first executes the code in the `wrapper` function before and after calling the original `say_hello`.
    This allows for additional functionality to be added easily.
    """)

# Conclusion
st.header("Conclusion")
st.write("""
Functions are an essential part of Python programming. They allow for code reusability, organization, and modularity. 
By understanding how to define, call, and pass parameters to functions, you can write cleaner and more efficient code.
Decorators further enhance the power of functions, allowing you to modify their behavior flexibly and elegantly.
""")

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



