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

st.title("Understanding Concepts of Object-Oriented Programming (OOP) in Python")

# Introduction
st.header("Introduction to OOP")
st.write("""
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software programs. 
OOP is designed to facilitate code reusability, scalability, and maintainability. 
The main concepts of OOP include:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
""")

operator_type = st.selectbox("Choose the option",["1. Encapsulation","2. Inheritance", "3. Polymorphism", "4. Abstraction"])


if st.session_state.get('last_operator_type') != operator_type:
    st.session_state.code = ''  # Reset code input area
    st.session_state.last_operator_type = operator_type
    
# Encapsulation
if operator_type == "1. Encapsulation":
    st.title("Understanding Encapsulation in Python")

    # Introduction
    st.header("Introduction")
    st.write("""
    **Encapsulation** is one of the fundamental concepts of object-oriented programming (OOP). 
    It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit or class. 
    Encapsulation restricts direct access to some of the object's components, which can prevent the accidental modification of data. 
    This is often achieved through the use of access modifiers, which define the visibility of class attributes and methods.
    """)

    # Benefits of Encapsulation
    st.header("Benefits of Encapsulation")
    st.write("""
    1. **Data Hiding**: Encapsulation helps to hide the internal state of an object from the outside world, exposing only what is necessary.
    2. **Control**: It provides control over the data by restricting access to the attributes and methods of the object.
    3. **Improved Maintenance**: Since the internal representation of an object can be changed without affecting external code, maintenance becomes easier.
    4. **Increased Security**: Sensitive data can be kept safe from unauthorized access or modification.
    """)

    # Access Modifiers in Python
    st.header("Access Modifiers in Python")
    st.write("""
    Python uses the following access modifiers to control access to class attributes and methods:
    - **Public**: Attributes and methods that can be accessed from outside the class.
    - **Protected**: Attributes and methods that can be accessed within the class and by subclasses (indicated by a single underscore `_`).
    - **Private**: Attributes and methods that cannot be accessed from outside the class (indicated by a double underscore `__`).
    """)

    # Example of Encapsulation
    st.header("Example of Encapsulation")
    st.write("""
    Below is an example demonstrating encapsulation using a `BankAccount` class, which encapsulates account details and provides methods to access and modify these details safely.
    """)

    encapsulation_example = """
    class BankAccount:
        def __init__(self, account_number, balance):
            self.__account_number = account_number  # Private attribute
            self.__balance = balance  # Private attribute

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                return f"Deposited {amount}. New balance: {self.__balance}"
            else:
                return "Deposit amount must be positive!"

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew {amount}. New balance: {self.__balance}"
            else:
                return "Insufficient balance or invalid withdrawal amount!"

        def get_balance(self):
            return f"Current balance: {self.__balance}"

    # Creating an instance of BankAccount
    account = BankAccount("123456789", 1000)

    # Accessing methods
    st.write(account.deposit(500))  # Outputs: Deposited 500. New balance: 1500
    st.write(account.withdraw(200))  # Outputs: Withdrew 200. New balance: 1300
    st.write(account.get_balance())   # Outputs: Current balance: 1300
    """

    st.code(encapsulation_example, language='python')

    st.write("""
    In this example:
    - The `BankAccount` class has private attributes `__account_number` and `__balance`, which cannot be accessed directly from outside the class.
    - The class provides public methods like `deposit`, `withdraw`, and `get_balance` to interact with these private attributes, ensuring controlled access to the account details.
    - This prevents unauthorized access and modification of the account's balance.

    ### Attempting to Access Private Attributes
    You can see that if we try to access private attributes directly, we will receive an error:
    """)

    private_access_example = """
    # Attempting to access private attributes
    # st.write(account.__balance)  # This will raise an AttributeError
    # st.write(account.__account_number)  # This will raise an AttributeError
    """

    st.code(private_access_example, language='python')

    st.write("""
    If you uncomment the lines above, you'll see that trying to access private attributes directly raises an `AttributeError`.
    This illustrates how encapsulation protects the internal state of an object from unauthorized access.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Encapsulation is a key concept in object-oriented programming that promotes data hiding and control over data access. 
    By encapsulating data and methods within classes, Python allows for improved code maintenance, increased security, and better organization of code. 
    Encapsulation ensures that the internal state of an object is protected from unauthorized access, promoting the integrity of the object's data.
    """)

elif operator_type == "2. Inheritance":
    # Inheritance
    st.header("Inheritance")
    st.write("""
    Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). 
    It promotes code reusability and can help create a hierarchical classification.
    """)

    inheritance_example = """
    class Animal:
        def speak(self):
            return "Animal makes a sound."

    class Dog(Animal):  # Dog inherits from Animal
        def speak(self):
            return "Dog barks."

    class Cat(Animal):  # Cat inherits from Animal
        def speak(self):
            return "Cat meows."

    # Creating objects
    dog = Dog()
    cat = Cat()

    st.write(dog.speak())  # Outputs: Dog barks.
    st.write(cat.speak())   # Outputs: Cat meows.
    """

    st.code(inheritance_example, language='python')

    st.write("""
    In this example, both `Dog` and `Cat` classes inherit from the `Animal` class. 
    They can override the `speak` method to provide their specific implementation while still maintaining a relationship with the `Animal` class.
    """)

    st.title("Types of Inheritance in Python")

    # Introduction
    st.header("Introduction")
    st.write("""
    **Inheritance** is a fundamental concept in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class). 
    This promotes code reuse and establishes a hierarchical relationship between classes. 
    Python supports several types of inheritance, which are:
    - Single Inheritance
    - Multiple Inheritance
    - Multilevel Inheritance
    - Hierarchical Inheritance
    - Hybrid Inheritance
    """)

    # Single Inheritance
    st.header("Single Inheritance")
    st.write("""
    **Single Inheritance** is when a child class inherits from a single parent class. This is the simplest form of inheritance.
    """)

    single_inheritance_example = """
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):  # Dog inherits from Animal
        def bark(self):
            return "Dog barks"

    # Creating an instance of Dog
    dog = Dog()
    st.write(dog.speak())  # Outputs: Animal speaks
    st.write(dog.bark())   # Outputs: Dog barks
    """

    st.code(single_inheritance_example, language='python')

    # Multiple Inheritance
    st.header("Multiple Inheritance")
    st.write("""
    **Multiple Inheritance** occurs when a child class inherits from more than one parent class. 
    This allows the child class to combine the functionality of multiple parent classes.
    """)

    multiple_inheritance_example = """
    class Flyable:
        def fly(self):
            return "Can fly"

    class Swimmable:
        def swim(self):
            return "Can swim"

    class Duck(Flyable, Swimmable):  # Duck inherits from Flyable and Swimmable
        def quack(self):
            return "Duck quacks"

    # Creating an instance of Duck
    duck = Duck()
    st.write(duck.fly())    # Outputs: Can fly
    st.write(duck.swim())   # Outputs: Can swim
    st.write(duck.quack())  # Outputs: Duck quacks
    """

    st.code(multiple_inheritance_example, language='python')

    # Multilevel Inheritance
    st.header("Multilevel Inheritance")
    st.write("""
    **Multilevel Inheritance** occurs when a class is derived from another derived class, forming a multi-level hierarchy.
    """)

    multilevel_inheritance_example = """
    class Grandparent:
        def greet(self):
            return "Hello from Grandparent"

    class Parent(Grandparent):  # Parent inherits from Grandparent
        def welcome(self):
            return "Welcome from Parent"

    class Child(Parent):  # Child inherits from Parent
        def say_goodbye(self):
            return "Goodbye from Child"

    # Creating an instance of Child
    child = Child()
    st.write(child.greet())      # Outputs: Hello from Grandparent
    st.write(child.welcome())     # Outputs: Welcome from Parent
    st.write(child.say_goodbye()) # Outputs: Goodbye from Child
    """

    st.code(multilevel_inheritance_example, language='python')

    # Hierarchical Inheritance
    st.header("Hierarchical Inheritance")
    st.write("""
    **Hierarchical Inheritance** occurs when multiple child classes inherit from a single parent class.
    """)

    hierarchical_inheritance_example = """
    class Vehicle:
        def start(self):
            return "Vehicle started"

    class Car(Vehicle):  # Car inherits from Vehicle
        def drive(self):
            return "Car is driving"

    class Bike(Vehicle):  # Bike inherits from Vehicle
        def ride(self):
            return "Bike is riding"

    # Creating instances
    car = Car()
    bike = Bike()

    st.write(car.start())  # Outputs: Vehicle started
    st.write(car.drive())  # Outputs: Car is driving
    st.write(bike.start()) # Outputs: Vehicle started
    st.write(bike.ride())  # Outputs: Bike is riding
    """

    st.code(hierarchical_inheritance_example, language='python')

    # Hybrid Inheritance
    st.header("Hybrid Inheritance")
    st.write("""
    **Hybrid Inheritance** is a combination of two or more types of inheritance. 
    It can include multiple and hierarchical inheritance in a single program.
    """)

    hybrid_inheritance_example = """
    class Person:
        def info(self):
            return "Person information"

    class Employee(Person):  # Employee inherits from Person
        def work(self):
            return "Employee works"

    class Manager(Employee):  # Manager inherits from Employee
        def manage(self):
            return "Manager manages"

    class Intern(Person):  # Intern inherits from Person
        def learn(self):
            return "Intern learns"

    # Creating instances
    manager = Manager()
    intern = Intern()

    st.write(manager.info())   # Outputs: Person information
    st.write(manager.work())    # Outputs: Employee works
    st.write(manager.manage())   # Outputs: Manager manages
    st.write(intern.info())     # Outputs: Person information
    st.write(intern.learn())     # Outputs: Intern learns
    """

    st.code(hybrid_inheritance_example, language='python')

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Inheritance is a powerful feature in Python that allows for code reuse and the creation of complex class hierarchies. 
    Understanding the different types of inheritance helps in designing better software systems. 
    - **Single Inheritance**: One parent, one child.
    - **Multiple Inheritance**: One child, multiple parents.
    - **Multilevel Inheritance**: Class derived from another derived class.
    - **Hierarchical Inheritance**: Multiple children from one parent.
    - **Hybrid Inheritance**: Combination of two or more inheritance types.

    Choosing the right type of inheritance is crucial for maintaining code clarity and structure.
    """)

elif operator_type == "3. Polymorphism": 

    st.title("Understanding Polymorphism in Python")

    # Introduction
    st.header("Introduction")
    st.write("""
    **Polymorphism** is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. 
    The term means "many forms," which indicates that a single function or method can work in different ways depending on the object it is acting upon. 
    Polymorphism enables flexibility and the ability to use the same interface for different underlying forms (data types).
    """)

    # Types of Polymorphism
    st.header("Types of Polymorphism")
    st.write("""
    Polymorphism can be classified into two main types:
    1. **Compile-time Polymorphism** (Static Polymorphism): Achieved through method overloading or operator overloading.
    2. **Run-time Polymorphism** (Dynamic Polymorphism): Achieved through method overriding in inheritance.
    """)

    # Compile-time Polymorphism
    st.header("Compile-time Polymorphism")
    st.write("""
    **Compile-time Polymorphism** is achieved by method overloading. In Python, we don't have traditional method overloading like in other languages, 
    but we can achieve similar behavior using default arguments or variable-length arguments.
    """)

    # Example of Method Overloading
    st.subheader("Example of Method Overloading")
    method_overloading_example = """
    class MathOperations:
        def add(self, a, b, c=0):  # Default argument for third parameter
            return a + b + c

    math_op = MathOperations()
    st.write(math_op.add(2, 3))         # Outputs: 5
    st.write(math_op.add(2, 3, 4))      # Outputs: 9
    """

    st.code(method_overloading_example, language='python')

    # Run-time Polymorphism
    st.header("Run-time Polymorphism")
    st.write("""
    **Run-time Polymorphism** is achieved through method overriding. It occurs when a subclass provides a specific implementation of a method 
    that is already defined in its superclass.
    """)

    # Example of Method Overriding
    st.subheader("Example of Method Overriding")
    method_overriding_example = """
    class Animal:
        def sound(self):
            return "Animal sound"

    class Dog(Animal):
        def sound(self):  # Overriding the sound method
            return "Bark"

    class Cat(Animal):
        def sound(self):  # Overriding the sound method
            return "Meow"

    def make_sound(animal):
        return animal.sound()

    # Creating instances
    dog = Dog()
    cat = Cat()

    st.write(make_sound(dog))  # Outputs: Bark
    st.write(make_sound(cat))   # Outputs: Meow
    """

    st.code(method_overriding_example, language='python')

    st.write("""
    In this example:
    - The `Animal` class has a method `sound()`, which is overridden in the `Dog` and `Cat` subclasses.
    - The `make_sound` function takes an `Animal` object as an argument and calls its `sound()` method.
    - This demonstrates how different subclasses can have different behaviors (methods) while sharing the same interface.
    """)

    # Importance of Polymorphism
    st.header("Importance of Polymorphism")
    st.write("""
    1. **Code Reusability**: Polymorphism allows for writing more generic and reusable code. 
    For example, a function can accept objects of different classes, making it easier to extend functionality.
    
    2. **Flexibility**: It allows the use of a unified interface for different types, enabling easier modifications and extensions.
    
    3. **Simplified Code**: Polymorphism can help reduce code complexity by enabling a single interface for multiple implementations.
    
    4. **Enhanced Maintainability**: Code is easier to maintain because changes to implementations do not affect the code that uses the polymorphic interface.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Polymorphism is a powerful feature in object-oriented programming that enhances flexibility, reusability, and maintainability of code. 
    By allowing methods to do different things based on the object it is acting upon, polymorphism enables cleaner and more efficient designs in software development. 
    Understanding and utilizing polymorphism effectively can lead to more robust and scalable code.
    """)

elif operator_type == "4. Abstraction":

    st.title("Understanding Abstraction in Python")

    # Introduction
    st.header("Introduction")
    st.write("""
    **Abstraction** is a fundamental concept in object-oriented programming (OOP) that involves hiding the complex implementation details of a system 
    while exposing only the necessary features to the user. The main goal of abstraction is to reduce complexity and increase efficiency 
    by allowing the programmer to focus on interacting with high-level interfaces rather than low-level details.
    """)

    # Importance of Abstraction
    st.header("Importance of Abstraction")
    st.write("""
    1. **Simplification**: By hiding unnecessary details, abstraction simplifies code and makes it easier to manage and understand.
    
    2. **Code Reusability**: Abstract classes and interfaces promote code reuse by allowing different implementations to be substituted 
    without changing the code that uses them.
    
    3. **Encapsulation of Complexity**: It helps to encapsulate complex systems, making it easier to work with and maintain code.
    
    4. **Improved Focus**: Programmers can focus on the higher-level functionalities without worrying about the intricate details.
    """)

    # Abstract Classes and Methods
    st.header("Abstract Classes and Methods")
    st.write("""
    In Python, abstraction is achieved using **abstract classes** and **abstract methods**. An abstract class is a class that cannot be instantiated 
    and is typically used as a base class. It can contain abstract methods that are declared but contain no implementation. 
    Subclasses that derive from the abstract class must provide implementations for the abstract methods.
    """)

    # Example of Abstraction
    st.subheader("Example of Abstraction")
    abstraction_example = """
    from abc import ABC, abstractmethod

    class Animal(ABC):  # Abstract class
        @abstractmethod
        def sound(self):  # Abstract method
            pass

    class Dog(Animal):
        def sound(self):  # Implementation of the abstract method
            return "Bark"

    class Cat(Animal):
        def sound(self):  # Implementation of the abstract method
            return "Meow"

    def animal_sound(animal):
        return animal.sound()

    # Creating instances
    dog = Dog()
    cat = Cat()

    st.write(animal_sound(dog))  # Outputs: Bark
    st.write(animal_sound(cat))   # Outputs: Meow
    """

    st.code(abstraction_example, language='python')

    st.write("""
    In this example:
    - The `Animal` class is an abstract class that defines an abstract method `sound()`.
    - The subclasses `Dog` and `Cat` provide concrete implementations of the `sound()` method.
    - The function `animal_sound` takes an `Animal` object and calls its `sound()` method, demonstrating polymorphism and abstraction together.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Abstraction is a key principle in object-oriented programming that allows for simplification and encapsulation of complex systems. 
    By using abstract classes and methods, developers can create cleaner and more manageable code, promoting better design and easier maintenance. 
    Understanding and effectively utilizing abstraction can lead to more efficient and scalable applications.
    """)

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

