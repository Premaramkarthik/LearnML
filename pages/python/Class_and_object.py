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


st.title("Understanding Classes and Objects in Python")

# Introduction
st.header("Introduction")
st.write("""
In Python, **classes** and **objects** are fundamental concepts of Object-Oriented Programming (OOP). 
A class serves as a blueprint for creating objects, which are instances of that class. 
Classes encapsulate data for the object and define behaviors (methods) that the objects can perform.
""")

# Key Concepts
st.header("Key Concepts")
st.write("""
- **Class**: A class is a user-defined prototype for an object that defines a set of attributes and methods that characterize any object of the class.
- **Object**: An object is an instance of a class. It has the attributes defined in the class and can use the methods defined for that class.
- **Attributes**: These are variables that belong to the class and define the properties of an object.
- **Methods**: These are functions defined within a class that describe the behaviors of an object.
""")

# Creating a Class
st.header("Creating a Class")
st.write("""
To define a class in Python, use the `class` keyword followed by the class name. 
The class body contains attributes and methods that define the characteristics and behaviors of the objects.
""")

class_example = """
class Dog:
    # Constructor method to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method to display dog's information
    def bark(self):
        return f"{self.name} says Woof!"
"""

st.code(class_example, language='python')

st.write("""
In this example, we define a class named `Dog` with an `__init__` method, which is the constructor used to initialize the object's attributes (`name` and `age`). 
The `bark` method defines a behavior for the object, which, when called, returns a string indicating the dog's sound.
""")

# Creating an Object
st.header("Creating an Object")
st.write("""
Once a class is defined, you can create an object (instance) of that class by calling the class name like a function.
""")

object_example = """
# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and methods
st.write(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
st.write(my_dog.bark())  # Outputs: Buddy says Woof!
"""

st.code(object_example, language='python')

st.write("""
In this example, we create an object `my_dog` of the `Dog` class and initialize it with the name "Buddy" and age 3. 
We can access the object's attributes and methods using the dot (`.`) notation.
""")

# Class Attributes vs Instance Attributes
st.header("Class Attributes vs Instance Attributes")
st.write("""
- **Instance Attributes**: These are attributes defined within the `__init__` method and are specific to each object.
- **Class Attributes**: These are attributes that belong to the class itself and are shared among all instances of the class.
""")

class_attributes_example = """
class Cat:
    species = "Feline"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances of the Cat class
cat1 = Cat("Whiskers", 2)
cat2 = Cat("Luna", 4)

# Accessing class and instance attributes
print(cat1.name)      # Outputs: Whiskers
print(cat1.species)   # Outputs: Feline
print(cat2.name)      # Outputs: Luna
print(cat2.species)   # Outputs: Feline
"""

st.code(class_attributes_example, language='python')



st.title("Understanding Class Methods and Static Methods in Python")

# Introduction
st.header("Introduction")
st.write("""
In Python, methods can be classified into three main types:
1. Instance methods
2. Class methods
3. Static methods

This app focuses on class methods and static methods, explaining their usage and differences.
""")

# Class Method
st.header("Class Method")
st.write("""
A **class method** is a method that is bound to the class and not the instance of the class. 
It takes `cls` as the first parameter, which refers to the class itself. 
Class methods can be called on the class itself or on instances of the class.
""")

class_method_example = """
class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)  # Create a new Circle instance using the class method

    def area(self):
        return self.pi * (self.radius ** 2)

# Creating a Circle object using the class method
circle_from_diameter = Circle.from_diameter(10)
st.write(f"Radius: {circle_from_diameter.radius}, Area: {circle_from_diameter.area()}")
"""

st.code(class_method_example, language='python')

st.write("""
In this example:
- The `Circle` class has a class method `from_diameter`, which creates a new `Circle` instance from a given diameter.
- The method uses `cls` to create an instance of the class, demonstrating the utility of class methods in providing alternative constructors.
""")

# Static Method
st.header("Static Method")
st.write("""
A **static method** is a method that does not take any special first parameter (like `self` or `cls`). 
It behaves like a regular function but belongs to the class's namespace. 
Static methods cannot access or modify class or instance state. They are used to perform operations that do not depend on class or instance attributes.
""")

static_method_example = """
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Using static methods
sum_result = MathOperations.add(5, 3)
product_result = MathOperations.multiply(4, 2)

st.write(f"Sum: {sum_result}, Product: {product_result}")
"""

st.code(static_method_example, language='python')

st.write("""
In this example:
- The `MathOperations` class has two static methods, `add` and `multiply`, which perform basic arithmetic operations.
- These methods do not depend on class or instance attributes and can be called directly on the class itself.
""")

# Differences Between Class Methods and Static Methods
st.header("Differences Between Class Methods and Static Methods")
st.write("""
| Feature                     | Class Method                        | Static Method                     |
|-----------------------------|-------------------------------------|-----------------------------------|
| First parameter              | `cls` (class itself)               | None                              |
| Access to class/instance data| Can access class and instance data | Cannot access class or instance data |
| Purpose                      | To operate on the class itself     | To perform utility functions that do not need class/instance context |
| Calling method               | Can be called on class or instance | Can be called on class or instance |
""")

# Conclusion
st.header("Conclusion")
st.write("""
Class methods and static methods are essential concepts in Python that provide different ways to define methods in a class. 
- Use **class methods** when you need to operate on the class itself or need an alternative constructor.
- Use **static methods** when you want to perform operations that do not depend on the class or instance.

Understanding when to use each type can lead to cleaner and more organized code.
""")


st.title("Understanding Multiple Dispatch in Python")

# Introduction
st.header("Introduction")
st.write("""
**Multiple Dispatch** is a feature that allows a function to be called based on the runtime types of its arguments. 
Unlike traditional method overloading, which is determined at compile time, multiple dispatch resolves the function to call at runtime based on the types of the arguments provided.
This is particularly useful in object-oriented programming, where methods can have different implementations based on the types of the arguments.
""")

# Basic Example of Multiple Dispatch
st.header("Basic Example of Multiple Dispatch")
st.write("""
Python does not have built-in support for multiple dispatch, but it can be implemented using libraries like `multipledispatch`. 
This library allows functions to have different implementations based on the types of their arguments.
""")

# Example Code
multiple_dispatch_example = """
from multipledispatch import dispatch

class Shape:
    @dispatch(int, int)
    def area(self, length, breadth):
        return length * breadth

    @dispatch(int)
    def area(self, side):
        return side * side

    @dispatch(float, float)
    def area(self, radius):
        return 3.14 * (radius ** 2)

# Creating an instance of Shape
shape = Shape()

st.write(f"Area of rectangle (length=5, breadth=3): {shape.area(5, 3)}")  # Outputs: 15
st.write(f"Area of square (side=4): {shape.area(4)}")                     # Outputs: 16
st.write(f"Area of circle (radius=2.5): {shape.area(2.5)}")              # Outputs: 19.625
"""

st.code(multiple_dispatch_example, language='python')

st.write("""
In this example:
- The `Shape` class has a method `area` that is overloaded with different implementations based on the argument types.
- The `@dispatch` decorator from the `multipledispatch` library is used to define multiple versions of the `area` method.
- When the `area` method is called, Python dynamically selects the appropriate implementation based on the types of the arguments provided.
""")

# Advantages of Multiple Dispatch
st.header("Advantages of Multiple Dispatch")
st.write("""
1. **Flexibility**: Allows functions to operate on different types without the need for explicit type checking.
2. **Code Clarity**: Improves code readability by avoiding long chains of conditional statements to handle different types.
3. **Extensibility**: New types can be added easily without modifying existing code, promoting the open/closed principle in software design.
4. **Dynamic Behavior**: Functions can behave differently based on the types of their arguments, making it easier to write generic code.
""")

# Comparison with Traditional Overloading
st.header("Comparison with Traditional Overloading")
st.write("""
| Feature                    | Multiple Dispatch                 | Traditional Overloading             |
|----------------------------|-----------------------------------|-------------------------------------|
| Resolution Time            | Runtime (based on argument types) | Compile time (based on function signature) |
| Flexibility                | Highly flexible                   | Limited by the number of signatures defined |
| Type Checking              | Dynamic                           | Static                              |
| Use Case                   | Complex systems with many types   | Simpler scenarios with few types    |
""")

# Conclusion
st.header("Conclusion")
st.write("""
Multiple dispatch is a powerful programming concept that enhances the flexibility and readability of code by allowing functions to have different behaviors based on the runtime types of their arguments. 
By using libraries like `multipledispatch`, Python developers can implement this feature to create cleaner and more dynamic applications.

While Python's built-in method overloading is limited, multiple dispatch provides a more robust alternative, particularly in scenarios involving complex data types and operations.
""")




st.title("Understanding Access Modifiers in Python")

# Introduction
st.header("Introduction")
st.write("""
Access modifiers in Python are used to define the scope and visibility of class attributes and methods. 
They help in encapsulating data and controlling how the attributes and methods can be accessed from outside the class. 
Python primarily uses naming conventions to indicate the intended accessibility of attributes and methods.
""")

# Types of Access Modifiers
st.header("Types of Access Modifiers")
st.write("""
Python has three main types of access modifiers:
1. **Public**: Attributes and methods that can be accessed from anywhere.
2. **Protected**: Attributes and methods that are intended to be accessed only within the class and its subclasses.
3. **Private**: Attributes and methods that are intended to be accessible only within the class itself.
""")

# Public Access Modifier
st.header("Public Access Modifier")
st.write("""
Public attributes and methods can be accessed from any part of the program. 
By default, all attributes and methods in a class are public unless specified otherwise.
""")

public_example = """
class Dog:
    def __init__(self, name):
        self.name = name  # Public attribute

    def bark(self):  # Public method
        return f"{self.name} says Woof!"

# Creating an object of the Dog class
dog = Dog("Buddy")
st.write(dog.bark())  # Outputs: Buddy says Woof!
"""

st.code(public_example, language='python')

st.write("""
In this example, the `name` attribute and the `bark` method are public, allowing access from outside the class.
""")

# Protected Access Modifier
st.header("Protected Access Modifier")
st.write("""
Protected attributes and methods are intended to be accessible only within the class and its subclasses. 
In Python, protected members are indicated by a single underscore (`_`) before the attribute or method name.
""")

protected_example = """
class Animal:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _speak(self):  # Protected method
        return f"{self._name} makes a noise."

class Dog(Animal):
    def speak(self):
        return f"{self._name} barks."

# Creating an object of the Dog class
dog = Dog("Max")
st.write(dog.speak())  # Outputs: Max barks.
"""

st.code(protected_example, language='python')

st.write("""
In this example, `_name` and `_speak` are protected members. 
While they can be accessed within the `Dog` subclass, they are intended to be used internally and should be treated as non-public.
""")

# Private Access Modifier
st.header("Private Access Modifier")
st.write("""
Private attributes and methods are intended to be accessible only within the class itself. 
In Python, private members are indicated by a double underscore (`__`) before the attribute or method name. 
This name mangling ensures that they cannot be accessed directly from outside the class.
""")

private_example = """
class Cat:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __speak(self):  # Private method
        return f"{self.__name} says Meow!"

    def get_name(self):  # Public method to access the private attribute
        return self.__name

# Creating an object of the Cat class
cat = Cat("Luna")
st.write(cat.get_name())  # Outputs: Luna
# st.write(cat.__speak())  # This will raise an AttributeError
"""

st.code(private_example, language='python')

st.write("""
In this example, `__name` and `__speak` are private members of the `Cat` class. 
They can be accessed only through public methods like `get_name()`. 
Trying to access them directly from outside the class would raise an `AttributeError`.
""")

# Summary of Access Modifiers
st.header("Summary of Access Modifiers")
st.write("""
- **Public**: Accessible from anywhere; no special syntax required.
- **Protected**: Intended for internal use; indicated by a single underscore `_`.
- **Private**: Accessible only within the class; indicated by a double underscore `__`.

While Python does not enforce strict access controls like some other languages (e.g., Java, C++), following these conventions helps in maintaining cleaner and more understandable code.
""")

# Conclusion
st.header("Conclusion")
st.write("""
Access modifiers are essential for encapsulation in Object-Oriented Programming. 
By understanding and using public, protected, and private access modifiers appropriately, you can control access to your class's attributes and methods, leading to better-organized code and enhanced data integrity.
""")


st.title("Understanding Name Mangling in Python")

# Introduction
st.header("Introduction")
st.write("""
Name mangling is a technique used in Python to modify the names of private attributes and methods to prevent name conflicts in subclasses. 
When an attribute or method name starts with a double underscore (`__`), Python alters its name to include the class name, which helps avoid accidental access from outside the class.
""")

# Example of Name Mangling
st.header("Example of Name Mangling")
st.write("""
Consider the following example, where we define a class with a private attribute and method.
""")

name_mangling_example = """
class MyClass:
    def __init__(self):
        self.__private_attribute = "This is a private attribute"  # Private attribute

    def __private_method(self):  # Private method
        return "This is a private method"

    def access_private(self):
        return self.__private_method()  # Accessing private method within the class

# Creating an instance of MyClass
obj = MyClass()

# Accessing the private attribute (will raise an AttributeError)
# print(obj.__private_attribute)

# Accessing the private method (will raise an AttributeError)
# print(obj.__private_method())

# Correctly accessing the private attribute using name mangling
st.write(obj._MyClass__private_attribute)  # Outputs: This is a private attribute

# Correctly accessing the private method using name mangling
st.write(obj._MyClass__private_method())  # Outputs: This is a private method
"""

st.code(name_mangling_example, language='python')

st.write("""
In this example:
- The attribute `__private_attribute` and the method `__private_method` are private members of `MyClass`.
- They cannot be accessed directly from outside the class, which would raise an `AttributeError`.
- However, you can access them using their mangled names: `_MyClass__private_attribute` and `_MyClass__private_method()`.
""")

# Summary of Name Mangling
st.header("Summary of Name Mangling")
st.write("""
- Name mangling helps to prevent name conflicts in subclasses.
- By prefixing an attribute or method with a double underscore (`__`), Python changes its name to `_ClassName__attributeName`.
- While this doesn't make the attribute or method truly private, it discourages direct access from outside the class.
""")

# Conclusion
st.header("Conclusion")
st.write("""
Name mangling is an essential aspect of Python's access control mechanisms. 
By understanding how name mangling works, you can better design your classes and avoid potential naming conflicts when subclassing.
""")

import streamlit as st

st.title("Understanding Method Overloading and Method Overriding in Python")

# Introduction
st.header("Introduction")
st.write("""
In Python, methods can be defined in a way that allows for flexibility in how they are called and executed. 
Two important concepts in this context are **method overloading** and **method overriding**.
- **Method Overloading**: Defining multiple methods with the same name but different parameters.
- **Method Overriding**: Redefining a method in a child class that already exists in the parent class.
""")

# Method Overloading
st.header("Method Overloading")
st.write("""
**Method Overloading** allows a class to have more than one method with the same name, but with different parameters. 
While Python does not support method overloading in the traditional sense (as seen in languages like Java), it can be implemented using default arguments or variable-length arguments.
""")

method_overloading_example = """
class MathOperations:
    def add(self, a, b, c=0):  # Method with default argument
        return a + b + c

# Creating an instance of MathOperations
math_ops = MathOperations()

st.write(f"Sum of 2 numbers (5, 3): {math_ops.add(5, 3)}")      # Outputs: 8
st.write(f"Sum of 3 numbers (5, 3, 2): {math_ops.add(5, 3, 2)}")  # Outputs: 10
"""

st.code(method_overloading_example, language='python')

st.write("""
In this example:
- The `add` method can accept two or three arguments.
- When called with two arguments, it defaults the third to zero.
- This demonstrates a form of method overloading by using default parameters to provide flexibility in method calls.
""")

# Method Overriding
st.header("Method Overriding")
st.write("""
**Method Overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
This allows a subclass to modify the behavior of the method for its own needs while retaining the same method name.
""")

method_overriding_example = """
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Dog barks"

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Cat meows"

# Creating instances
dog = Dog()
cat = Cat()

st.write(dog.speak())  # Outputs: Dog barks
st.write(cat.speak())   # Outputs: Cat meows
"""

st.code(method_overriding_example, language='python')

st.write("""
In this example:
- The `Animal` class has a method `speak`, which is overridden in the `Dog` and `Cat` subclasses.
- Each subclass provides its own specific implementation of the `speak` method, demonstrating method overriding.
""")

# Differences Between Method Overloading and Method Overriding
st.header("Differences Between Method Overloading and Method Overriding")
st.write("""
| Feature                     | Method Overloading                  | Method Overriding                    |
|-----------------------------|-------------------------------------|--------------------------------------|
| Definition                  | Multiple methods with the same name but different parameters | Redefining a method in a subclass that exists in the superclass |
| Implementation               | Achieved using default/variable-length arguments | Achieved by redefining the method in the subclass |
| Purpose                     | Provides flexibility in method calls | Allows subclasses to provide specific implementations |
| Relation                    | No relation between overloaded methods | Involves a relationship between parent and child classes |
""")

# Conclusion
st.header("Conclusion")
st.write("""
Understanding method overloading and method overriding is essential for effective object-oriented programming in Python. 
- **Method Overloading** provides a way to define methods that can handle different types or numbers of arguments, enhancing flexibility.
- **Method Overriding** allows subclasses to customize or extend the behavior of inherited methods, promoting code reuse and maintainability.

Using these concepts effectively can lead to cleaner, more intuitive, and more efficient code.
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



