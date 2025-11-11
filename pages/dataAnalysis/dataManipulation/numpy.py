import streamlit as st
import numpy as np

if 'code' not in st.session_state:
    st.session_state.code = ''

st.title('Numpy')

select = ['Introduction  about Numpy','Creating Arrays in NumPy', "Understanding Broadcasting in NumPy",'Filtering in NumPy']

select_option_1 = st.selectbox("select the topic ",select)

match select_option_1:
    
    case 'Introduction  about Numpy':
        
        st.title("Introduction to NumPy")

        # Introduction about NumPy
        st.header("What is NumPy?")
        st.write("""
            NumPy (Numerical Python) is an open-source library used for numerical computing in Python.
            It provides support for large, multi-dimensional arrays and matrices, along with a collection 
            of mathematical functions to operate on these arrays. NumPy is a core library for scientific 
            computing and is widely used in fields such as data science, machine learning, and engineering 
            due to its efficiency and ease of use.
        """)

        # Key Features of NumPy
        st.header("Key Features of NumPy:")

        st.subheader("1. N-dimensional Arrays")
        st.write("""
            NumPy provides the `ndarray` object, which is a fast, flexible container for large data sets. 
            Arrays in NumPy are more efficient and allow for operations on entire datasets without the need 
            for explicit loops, leading to faster computations.
        """)

        st.subheader("2. Mathematical Operations")
        st.write("""
            NumPy supports a wide range of mathematical functions (e.g., addition, multiplication, linear 
            algebra operations) that can be performed directly on arrays. These operations are optimized for 
            performance and use underlying C and Fortran code.
        """)

        st.subheader("3. Broadcasting")
        st.write("""
            NumPy allows for operations between arrays of different shapes and sizes through broadcasting. 
            It automatically adjusts the smaller array to match the shape of the larger one, making element-wise 
            operations easier and more efficient.
        """)

        st.subheader("4. Array Slicing and Reshaping")
        st.write("""
            NumPy provides powerful tools to slice and reshape arrays, enabling flexible manipulation of data 
            without copying the data itself.
        """)

        st.subheader("5. Integration with Other Libraries")
        st.write("""
            NumPy is the foundation for many other scientific libraries in Python, such as SciPy, pandas, and 
            scikit-learn. These libraries build on NumPy to provide more specific functionality, like data 
            analysis or machine learning.
        """)

        st.header("Conclusion")
        st.write("""
            NumPy is essential for tasks that require fast numerical operations, such as working with large 
            datasets or implementing machine learning algorithms.
        """)

    case 'Creating Arrays in NumPy':

        st.title("Creating Arrays in NumPy")

        # Introduction to array creation
        st.header("Introduction to NumPy Array Creation")
        st.write("""
            In NumPy, arrays are the central data structure and are more efficient than Python lists for 
            numerical computations. Here, we will explore different ways to create NumPy arrays.
        """)

        # Creating a 1D Array using np.array()
        st.subheader("1. Creating a 1D Array")
        st.write("""
            The `np.array()` function is used to create a NumPy array. You can create arrays from lists or 
            tuples, and NumPy will automatically determine the shape and data type.
        """)

        st.code("""
            # Create a 1D array from a list
            arr_1d = np.array([1, 2, 3, 4, 5])
            st.write(f"1D Array: {arr_1d}")
        """)

        arr_1d = np.array([1, 2, 3, 4, 5])
        st.write(f"1D Array: {arr_1d}")

        # Creating a 2D Array using np.array()
        st.subheader("2. Creating a 2D Array")
        st.write("""
            You can create multi-dimensional arrays (like 2D or 3D arrays) by passing a list of lists to 
            `np.array()`. This will create an array with the specified dimensions.
        """)

        st.code("""
            # Create a 2D array from a list of lists
            arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
            st.write(f"2D Array: {arr_2d}")
        """)

        arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
        st.write(f"2D Array: {arr_2d}")

        # Creating an array with np.zeros()
        st.subheader("3. Creating an Array with Zeros")
        st.write("""
            The `np.zeros()` function creates an array of the specified shape, filled with zeros. This is 
            useful for initializing arrays before populating them with data.
        """)

        st.code("""
            # Create a 2D array with zeros
            arr_zeros = np.zeros((3, 4))  # 3 rows, 4 columns
            st.write(f"Array of Zeros: {arr_zeros}")
        """)

        arr_zeros = np.zeros((3, 4))
        st.write(f"Array of Zeros: {arr_zeros}")

        # Creating an array with np.ones()
        st.subheader("4. Creating an Array with Ones")
        st.write("""
            Similarly, `np.ones()` creates an array of the specified shape, filled with ones.
        """)

        st.code("""
            # Create a 2D array with ones
            arr_ones = np.ones((2, 3))  # 2 rows, 3 columns
            st.write(f"Array of Ones: {arr_ones}")
        """)

        arr_ones = np.ones((2, 3))
        st.write(f"Array of Ones: {arr_ones}")

        # Creating an array with np.arange()
        st.subheader("5. Creating an Array with np.arange()")
        st.write("""
            The `np.arange()` function is used to create arrays with evenly spaced values over a specified 
            range. It is similar to Python's `range()` function, but returns a NumPy array.
        """)

        st.code("""
            # Create an array with values from 0 to 9
            arr_arange = np.arange(10)
            st.write(f"Array with np.arange(): {arr_arange}")
        """)

        arr_arange = np.arange(10)
        st.write(f"Array with np.arange(): {arr_arange}")

        # Creating an array with np.linspace()
        st.subheader("6. Creating an Array with np.linspace()")
        st.write("""
            The `np.linspace()` function creates an array of evenly spaced values over a specified range, 
            with a specified number of points.
        """)

        st.code("""
            # Create an array of 5 equally spaced values between 0 and 1
            arr_linspace = np.linspace(0, 1, 5)
            st.write(f"Array with np.linspace(): {arr_linspace}")
        """)

        arr_linspace = np.linspace(0, 1, 5)
        st.write(f"Array with np.linspace(): {arr_linspace}")

        # Creating a random array with np.random.rand()
        st.subheader("7. Creating a Random Array")
        st.write("""
            The `np.random.rand()` function generates an array of random values from a uniform distribution 
            between 0 and 1.
        """)

        st.code("""
            # Create a 2D array of random values between 0 and 1
            arr_random = np.random.rand(3, 2)  # 3 rows, 2 columns
            st.write(f"Random Array: {arr_random}")
        """)

        arr_random = np.random.rand(3, 2)
        st.write(f"Random Array: {arr_random}")

    case "Understanding Broadcasting in NumPy":
        
        st.title("Understanding Broadcasting in NumPy")

        # Introduction to Broadcasting
        st.header("What is Broadcasting?")
        st.write("""
            Broadcasting in NumPy refers to the ability to perform arithmetic operations on arrays 
            of different shapes. When performing operations on arrays of different shapes, NumPy 
            automatically expands the smaller array to match the shape of the larger array in a 
            way that allows the operation to be performed element-wise. Broadcasting is a powerful 
            feature that avoids the need for explicit loops, making operations on large datasets faster.
        """)

        st.subheader("How Broadcasting Works")
        st.write("""
            Broadcasting works by comparing the shapes of the arrays involved in the operation.
            Two arrays are compatible for broadcasting if:
            
            - Starting from the rightmost dimension, the size of each dimension is either 
            the same or one of them is 1.
            - NumPy will "stretch" the smaller array to match the dimensions of the larger array.

            Here's an example that demonstrates broadcasting.
        """)

        # Example of Broadcasting
        st.subheader("Example 1: Adding a 1D Array to a 2D Array")
        st.write("""
            In this example, we will add a 1D array to a 2D array. The 1D array will be broadcast 
            over the rows of the 2D array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

            # Create a 1D array to be broadcast
            arr_1d = np.array([10, 20, 30])

            # Broadcasting arr_1d over arr_2d
            result = arr_2d + arr_1d
            st.write(f"Result of Broadcasting: {result}")
        """)

        # Broadcasting example 1
        arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
        arr_1d = np.array([10, 20, 30])
        result = arr_2d + arr_1d
        st.write(f"Result of Broadcasting: {result}")

        st.write("""
            The 1D array `[10, 20, 30]` is broadcast over each row of the 2D array. 
            The result is:
            ```
            [[11, 22, 33],
            [14, 25, 36]]
            ```

            Notice how the 1D array was added to each row of the 2D array.
        """)

        # Example of Broadcasting with Different Shapes
        st.subheader("Example 2: Broadcasting with Different Shapes")
        st.write("""
            Let's see another example where the dimensions of the two arrays are not the same, 
            but they are still compatible for broadcasting.
        """)

        st.code("""
            # Create a 2D array (3x3)
            arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

            # Create a 1D array (3,)
            arr_1d = np.array([1, 0, -1])

            # Broadcasting arr_1d over arr_2d
            result = arr_2d + arr_1d
            st.write(f"Result of Broadcasting: {result}")
        """)

        # Broadcasting example 2
        arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        arr_1d = np.array([1, 0, -1])
        result = arr_2d + arr_1d
        st.write(f"Result of Broadcasting: {result}")

        st.write("""
            The 1D array `[1, 0, -1]` is broadcast across the rows of the 2D array.
            The result is:
            ```
            [[ 2  2  2]
            [ 5  5  5]
            [ 8  8  8]]
            ```

            The 1D array was added to each row of the 2D array, with the values in the 1D array 
            being added element-wise to each row.
        """)

        # Example of Broadcasting with a Scalar
        st.subheader("Example 3: Broadcasting with a Scalar")
        st.write("""
            You can also perform broadcasting with a scalar. The scalar is automatically 
            broadcast across all elements of the array.
        """)

        st.code("""
            # Create a 2D array (3x3)
            arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

            # Add a scalar to the array
            result = arr_2d + 10
            st.write(f"Result of Broadcasting with Scalar: {result}")
        """)

        # Broadcasting example with scalar
        arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = arr_2d + 10
        st.write(f"Result of Broadcasting with Scalar: {result}")

        st.write("""
            Adding the scalar `10` to the 2D array results in:
            ```
            [[11 12 13]
            [14 15 16]
            [17 18 19]]
            ```

            The scalar was broadcasted across each element of the array.
        """)

    case 'Filtering in NumPy':

        st.title("Filtering in NumPy")

        # Introduction to Filtering
        st.header("What is Filtering in NumPy?")
        st.write("""
            Filtering in NumPy allows you to select elements from an array based on certain conditions.
            Instead of looping through the array manually, NumPy allows for efficient filtering using 
            Boolean indexing. With Boolean indexing, we create a Boolean array where each element corresponds
            to a condition applied to the original array, and then use that array to extract the elements that meet
            the condition.
        """)

        st.subheader("Why Use Filtering?")
        st.write("""
            Filtering allows for fast and efficient data extraction from large arrays. It is commonly used in 
            data analysis, machine learning, and scientific computing tasks to isolate specific values, 
            such as values above a certain threshold, values within a range, or values satisfying a certain condition.
        """)

        # Example of Filtering with a Condition
        st.subheader("Example 1: Filtering Elements Greater Than a Threshold")
        st.write("""
            In this example, we'll filter elements of an array that are greater than a specified threshold.
        """)

        st.code("""
            # Create a NumPy array
            arr = np.array([1, 3, 5, 7, 9, 11, 13, 15])

            # Define the threshold
            threshold = 7

            # Filter the elements greater than the threshold
            result = arr[arr > threshold]
            st.write(f"Filtered Result: {result}")
        """)

        # Filtering example 1
        arr = np.array([1, 3, 5, 7, 9, 11, 13, 15])
        threshold = 7
        result = arr[arr > threshold]
        st.write(f"Filtered Result: {result}")

        st.write("""
            The condition `arr > 7` creates a Boolean array `[False, False, False, False, True, True, True, True]`,
            which is then used to filter out the elements greater than 7. The result is:
            ```
            [ 9 11 13 15]
            ```

            This demonstrates how NumPy's filtering can efficiently extract elements based on conditions.
        """)

        # Example of Filtering with Multiple Conditions
        st.subheader("Example 2: Filtering with Multiple Conditions")
        st.write("""
            You can also combine multiple conditions using logical operators (AND, OR, NOT).
            Here, we'll filter elements that are greater than 5 and less than 13.
        """)

        st.code("""
            # Create a NumPy array
            arr = np.array([1, 3, 5, 7, 9, 11, 13, 15])

            # Define the conditions: elements greater than 5 and less than 13
            condition = (arr > 5) & (arr < 13)

            # Apply the condition
            result = arr[condition]
            st.write(f"Filtered Result with Multiple Conditions: {result}")
        """)

        # Filtering example 2
        condition = (arr > 5) & (arr < 13)
        result = arr[condition]
        st.write(f"Filtered Result with Multiple Conditions: {result}")

        st.write("""
            In this case, we used the condition `(arr > 5) & (arr < 13)`, which is equivalent to:
            ```
            [False False False  True  True  True False False]
            ```

            The result is:
            ```
            [ 7  9 11]
            ```

            You can also use other logical operators like `|` for OR and `~` for NOT to create complex conditions.
        """)

        # Example of Filtering with a 2D Array
        st.subheader("Example 3: Filtering in a 2D Array")
        st.write("""
            You can filter elements in multi-dimensional arrays, like 2D arrays, based on conditions.
            Let's say we want to filter values greater than 5 in a 2D array.
        """)

        st.code("""
            # Create a 2D NumPy array
            arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

            # Define the condition: elements greater than 5
            condition = arr_2d > 5

            # Apply the condition
            result = arr_2d[condition]
            st.write(f"Filtered Result from 2D Array: {result}")
        """)

        # Filtering example 3
        arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        condition = arr_2d > 5
        result = arr_2d[condition]
        st.write(f"Filtered Result from 2D Array: {result}")

        st.write("""
            The condition `arr_2d > 5` creates a Boolean array:
            ```
            [[False False False]
            [False False  True]
            [ True  True  True]]
            ```

            The result is:
            ```
            [6 7 8 9]
            ```

            This demonstrates how to filter elements in multi-dimensional arrays using NumPy.
        """)

        # Example of Filtering with String Arrays
        st.subheader("Example 4: Filtering String Arrays")
        st.write("""
            You can also filter string arrays based on conditions, like selecting strings that contain a specific substring.
        """)

        st.code("""
            # Create a string NumPy array
            arr_str = np.array(["apple", "banana", "cherry", "date", "elderberry"])

            # Define the condition: strings that contain 'e'
            condition = np.char.find(arr_str, 'e') != -1

            # Apply the condition
            result = arr_str[condition]
            st.write(f"Filtered Strings Containing 'e': {result}")
        """)

        # Filtering example with string arrays
        arr_str = np.array(["apple", "banana", "cherry", "date", "elderberry"])
        condition = np.char.find(arr_str, 'e') != -1
        result = arr_str[condition]
        st.write(f"Filtered Strings Containing 'e': {result}")

        st.write("""
            The condition `np.char.find(arr_str, 'e') != -1` creates a Boolean array:
            ```
            [ True False  True False  True]
            ```

            The result is:
            ```
            ['apple' 'cherry' 'elderberry']
            ```

            This example shows how you can filter string arrays using NumPy's string operations.
        """)


