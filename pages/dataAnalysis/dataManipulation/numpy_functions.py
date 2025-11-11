
import streamlit as st
import numpy as np
import time

if 'code' not in st.session_state:
    st.session_state.code = ''

st.title('Numpy Functions')

select = ["where() Function","repeat() Function","mean() Function","sum() Function","subtract() Function","multiply() Function",
          "divide() Function","floor_divide() Function","argmin() Function","Sorting Rows and Columns in NumPy","Lexicographical Sorting",
          "Vectorization in NumPy","apply_along_axis() Function","numpy.apply_over_axes() Function","unique() Function","dot() Function",
          "digitize() Function","clip() Function","bincount() Function","flatten() Function"]

select_option = st.selectbox("select the topic ",select)

match select_option:

    case "where() Function":

        st.title("NumPy `where()` Function")

        # Introduction to `where()` function
        st.header("What is the `where()` Function?")
        st.write("""
            The `where()` function in NumPy is used to select elements from an array based on a condition. 
            It can also be used to get the indices of elements that satisfy a given condition. 
            The syntax is as follows:
            
            ```
            np.where(condition, [x, y])
            ```
            - **condition**: A Boolean array or condition based on which elements are selected.
            - **x**: Value to return when the condition is `True`.
            - **y**: Value to return when the condition is `False`.
            
            The function returns an array with elements selected based on the condition.
        """)

        # Example 1: Using `where()` for Conditional Replacement
        st.subheader("Example 1: Conditional Replacement")
        st.write("""
            In this example, we use the `where()` function to replace values in an array based on a condition. 
            If the condition is `True`, the elements will be replaced with a specific value; otherwise, 
            they will be replaced with another value.
        """)

        st.code("""
            # Create a NumPy array
            arr = np.array([10, 20, 30, 40, 50])

            # Define the condition: elements greater than 30
            result = np.where(arr > 30, 'Greater', 'Smaller or Equal')
            st.write(f"Result after replacement: {result}")
        """)

        # Conditional replacement example 1
        arr = np.array([10, 20, 30, 40, 50])
        result = np.where(arr > 30, 'Greater', 'Smaller or Equal')
        st.write(f"Result after replacement: {result}")

        st.write("""
            In this case, the condition `arr > 30` checks for values greater than 30. 
            If the condition is `True`, the element is replaced by 'Greater', 
            and if `False`, it is replaced by 'Smaller or Equal'. 
            The result is:
            ```
            ['Smaller or Equal' 'Smaller or Equal' 'Smaller or Equal' 'Greater' 'Greater']
            ```
        """)

        # Example 2: Using `where()` to Get Indices of Elements Satisfying a Condition
        st.subheader("Example 2: Finding Indices of Elements Satisfying a Condition")
        st.write("""
            The `where()` function can also return the indices of elements that satisfy a specific condition. 
            In this example, we will find the indices of elements that are greater than 30.
        """)

        st.code("""
            # Find indices of elements greater than 30
            indices = np.where(arr > 30)
            st.write(f"Indices of elements greater than 30: {indices}")
        """)

        # Finding indices example 2
        indices = np.where(arr > 30)
        st.write(f"Indices of elements greater than 30: {indices}")

        st.write("""
            In this case, the condition `arr > 30` returns the indices where the condition is `True`. 
            The result is:
            ```
            (array([3, 4]),)
            ```
            This means that elements at indices 3 and 4 are greater than 30.
        """)

        # Example 3: Using `where()` to Replace with Different Values
        st.subheader("Example 3: Replacing with Different Values")
        st.write("""
            You can use `where()` to replace values with different outputs for the `True` and `False` conditions.
            For example, we can replace values above 30 with 100 and others with 0.
        """)

        st.code("""
            # Replace values greater than 30 with 100, else replace with 0
            result = np.where(arr > 30, 100, 0)
            st.write(f"Result with replaced values: {result}")
        """)

        # Replacing values example 3
        result = np.where(arr > 30, 100, 0)
        st.write(f"Result with replaced values: {result}")

        st.write("""
            In this case, if an element is greater than 30, it is replaced with 100; otherwise, 
            it is replaced with 0. The result is:
            ```
            [  0   0   0 100 100]
            ```
        """)

        # Example 4: Using `where()` with a 2D Array
        st.subheader("Example 4: Using `where()` with a 2D Array")
        st.write("""
            You can also use `where()` with multi-dimensional arrays. In this example, 
            we will replace elements in a 2D array that are greater than 5 with 10, 
            and the others with 0.
        """)

        st.code("""
            # Create a 2D NumPy array
            arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

            # Replace values greater than 5 with 10, others with 0
            result = np.where(arr_2d > 5, 10, 0)
            st.write(f"Result with replaced values in 2D array: {result}")
        """)

        # Replacing values in 2D array example 4
        arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = np.where(arr_2d > 5, 10, 0)
        st.write(f"Result with replaced values in 2D array: {result}")

        st.write("""
            In this case, elements greater than 5 are replaced with 10, and all others are replaced with 0.
            The result is:
            ```
            [[ 0  0  0]
            [ 0  0 10]
            [10 10 10]]
            ```
        """)

    case "repeat() Function":

        st.title("NumPy `repeat()` Function and Axis")

        # Introduction to `repeat()` and axis
        st.header("What is the `repeat()` Function?")
        st.write("""
            The `repeat()` function in NumPy repeats elements of an array along the specified axis.
            You can specify how many times each element should be repeated, and optionally, along which axis to repeat.
            
            Syntax:
            ```
            np.repeat(arr, repeats, axis=None)
            ```
            - **arr**: The input array.
            - **repeats**: The number of repetitions for each element. This can be a scalar or an array of the same shape as the input array.
            - **axis**: Axis along which to repeat. If `None` (default), the input array is flattened before repeating. For multi-dimensional arrays, setting the axis allows you to repeat along specific axes.
            
            The `axis` parameter is essential when dealing with multi-dimensional arrays to control how the data is replicated.
        """)

        # Example 1: Repeating elements in a 1D array
        st.subheader("Example 1: Repeating elements in a 1D array")
        st.write("""
            In this example, we'll repeat the elements of a 1D array. 
            We'll repeat each element a specified number of times.
        """)

        st.code("""
            # Create a 1D array
            arr = np.array([1, 2, 3])

            # Repeat each element 3 times
            result = np.repeat(arr, 3)
            st.write(f"Result after repeating: {result}")
        """)

        # Repeating elements in 1D example 1
        arr = np.array([1, 2, 3])
        result = np.repeat(arr, 3)
        st.write(f"Result after repeating: {result}")

        st.write("""
            In this case, the elements `[1, 2, 3]` are repeated 3 times each, producing the result:
            ```
            [1 1 1 2 2 2 3 3 3]
            ```
        """)

        # Example 2: Repeating elements in a 2D array along axis 0
        st.subheader("Example 2: Repeating elements along axis 0 (row-wise)")
        st.write("""
            In this example, we will repeat the rows of a 2D array along axis 0 (vertically).
            This will duplicate the rows in the array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4]])

            # Repeat rows 2 times along axis 0
            result = np.repeat(arr_2d, 2, axis=0)
            st.write(f"Result after repeating rows: {result}")
        """)

        # Repeating along axis 0 example 2
        arr_2d = np.array([[1, 2], [3, 4]])
        result = np.repeat(arr_2d, 2, axis=0)
        st.write(f"Result after repeating rows: {result}")

        st.write("""
            In this case, the rows `[[1, 2], [3, 4]]` are repeated 2 times along axis 0, producing the result:
            ```
            [[1 2]
            [1 2]
            [3 4]
            [3 4]]
            ```
        """)

        # Example 3: Repeating elements in a 2D array along axis 1
        st.subheader("Example 3: Repeating elements along axis 1 (column-wise)")
        st.write("""
            In this example, we will repeat the elements along axis 1 (horizontally).
            This means the columns will be duplicated.
        """)

        st.code("""
            # Repeat columns 2 times along axis 1
            result = np.repeat(arr_2d, 2, axis=1)
            st.write(f"Result after repeating columns: {result}")
        """)

        # Repeating along axis 1 example 3
        result = np.repeat(arr_2d, 2, axis=1)
        st.write(f"Result after repeating columns: {result}")

        st.write("""
            In this case, the elements `[[1, 2], [3, 4]]` are repeated 2 times along axis 1, producing the result:
            ```
            [[1 1 2 2]
            [3 3 4 4]]
            ```
        """)

        # Example 4: Repeating each element a different number of times
        st.subheader("Example 4: Repeating elements with varying counts")
        st.write("""
            You can also specify a different number of repetitions for each element. 
            In this case, we'll repeat elements of the array `arr_2d` by different amounts for each element.
        """)

        st.code("""
            # Define a repetition pattern
            repeats = [2, 3]

            # Repeat the elements of the 2D array with different counts
            result = np.repeat(arr_2d, repeats, axis=0)
            st.write(f"Result after varying repetitions: {result}")
        """)

        # Repeating elements with varying counts example 4
        repeats = [2, 3]
        result = np.repeat(arr_2d, repeats, axis=0)
        st.write(f"Result after varying repetitions: {result}")

        st.write("""
            In this case, the first row is repeated 2 times, and the second row is repeated 3 times, resulting in:
            ```
            [[1 2]
            [1 2]
            [3 4]
            [3 4]
            [3 4]]
            ```
        """)

        # Example 5: Flattening and repeating a 2D array
        st.subheader("Example 5: Flattening the array and repeating")
        st.write("""
            By default, if you don't specify an axis, `repeat()` will flatten the array before repeating.
            In this example, we'll flatten a 2D array and repeat the entire array.
        """)

        st.code("""
            # Flatten and repeat the array
            result = np.repeat(arr_2d, 2)
            st.write(f"Result after flattening and repeating: {result}")
        """)

        # Flattening and repeating example 5
        result = np.repeat(arr_2d, 2)
        st.write(f"Result after flattening and repeating: {result}")

        st.write("""
            In this case, the entire array is flattened into a 1D array, and then each element is repeated 2 times:
            ```
            [1 1 2 2 3 3 4 4]
            ```
        """)
    case "mean() Function":

        st.title("NumPy `mean()` Function and Axis")

        # Introduction to `mean()` and axis
        st.header("What is the `mean()` Function?")
        st.write("""
            The `mean()` function in NumPy calculates the average of the elements in an array.
            It is a key statistical function used in data analysis, machine learning, and deep learning.

            Syntax:
            ```
            np.mean(arr, axis=None, dtype=None, out=None, keepdims=False)
            ```
            - **arr**: The input array or object that can be converted to an array.
            - **axis**: The axis or axes along which the means are computed. If `None` (default), the mean of all the elements is computed.
            - **dtype**: The data type used to calculate the mean.
            - **keepdims**: If True, the reduced dimensions will be kept in the result as dimensions with size one.

            The **`axis`** parameter determines whether the mean is calculated row-wise, column-wise, or over specific dimensions in multi-dimensional arrays.
        """)

        # Example 1: Mean of a 1D array
        st.subheader("Example 1: Mean of a 1D array")
        st.write("""
            In this example, we'll calculate the mean of a simple 1D array.
        """)

        st.code("""
            # Create a 1D array
            arr = np.array([1, 2, 3, 4, 5])

            # Calculate the mean
            result = np.mean(arr)
            st.write(f"Mean of the array: {result}")
        """)

        # Mean of a 1D array example 1
        arr = np.array([1, 2, 3, 4, 5])
        result = np.mean(arr)
        st.write(f"Mean of the array: {result}")

        st.write("""
            The mean of the array `[1, 2, 3, 4, 5]` is:
            ```
            3.0
            ```
        """)

        # Example 2: Mean along axis 0 (Row-wise in a 2D array)
        st.subheader("Example 2: Mean along axis 0 (Row-wise in a 2D array)")
        st.write("""
            In this example, we will calculate the mean of each column (along axis 0) in a 2D array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

            # Calculate the mean along axis 0 (columns)
            result = np.mean(arr_2d, axis=0)
            st.write(f"Mean along axis 0 (columns): {result}")
        """)

        # Mean along axis 0 example 2
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        result = np.mean(arr_2d, axis=0)
        st.write(f"Mean along axis 0 (columns): {result}")

        st.write("""
            The mean along axis 0 (columns) of the 2D array is:
            ```
            [3. 4.]
            ```
            This is the average of each column.
        """)

        # Example 3: Mean along axis 1 (Column-wise in a 2D array)
        st.subheader("Example 3: Mean along axis 1 (Column-wise in a 2D array)")
        st.write("""
            In this example, we will calculate the mean of each row (along axis 1) in a 2D array.
        """)

        st.code("""
            # Calculate the mean along axis 1 (rows)
            result = np.mean(arr_2d, axis=1)
            st.write(f"Mean along axis 1 (rows): {result}")
        """)

        # Mean along axis 1 example 3
        result = np.mean(arr_2d, axis=1)
        st.write(f"Mean along axis 1 (rows): {result}")

        st.write("""
            The mean along axis 1 (rows) of the 2D array is:
            ```
            [1.5 3.5 5.5]
            ```
            This is the average of each row.
        """)

        # Example 4: Mean in multi-dimensional arrays
        st.subheader("Example 4: Mean in a 3D array")
        st.write("""
            In this example, we calculate the mean in a 3D array along different axes.
        """)

        st.code("""
            # Create a 3D array
            arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

            # Calculate the mean along axis 0
            result_0 = np.mean(arr_3d, axis=0)

            # Calculate the mean along axis 1
            result_1 = np.mean(arr_3d, axis=1)

            st.write(f"Mean along axis 0: {result_0}")
            st.write(f"Mean along axis 1: {result_1}")
        """)

        # Mean in a 3D array example 4
        arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result_0 = np.mean(arr_3d, axis=0)
        result_1 = np.mean(arr_3d, axis=1)
        st.write(f"Mean along axis 0: {result_0}")
        st.write(f"Mean along axis 1: {result_1}")

        st.write("""
            In the case of a 3D array:
            - The mean along axis 0 gives the average across the depth of the array.
            - The mean along axis 1 gives the average across the rows in each matrix.
        """)

        # Use of Mean in ML and DL
        st.header("How the `mean()` Function Helps in ML, DL, and Data Analysis")
        st.write("""
            - **Data Normalization and Feature Scaling**: In machine learning, the `mean()` function is often used to calculate the mean of features in the dataset. This is important for data normalization, where features are scaled to have a mean of 0 and a standard deviation of 1 (Z-score normalization). This helps ML models converge faster and perform better.

            - **Loss Function Calculation**: In deep learning, the mean is frequently used to calculate the average of the loss function during training. For example, in Mean Squared Error (MSE), the mean of the squared differences between predicted and actual values is computed to optimize the model.

            - **Data Analysis**: In data analysis, the mean is used as a simple statistical measure of central tendency. It helps summarize datasets, identify trends, and detect anomalies. It is commonly used to summarize data before performing more advanced analysis or visualization.

            For example:
            - In **image processing** (DL), we often calculate the mean pixel value of an image to normalize it before feeding it into a neural network.
            - In **recommendation systems** (ML), the mean rating for a product or service can be used to compare different items.
        """)

        # Example of Normalizing Data (Z-score normalization)
        st.subheader("Example: Z-score Normalization Using Mean")
        st.write("""
            Z-score normalization is a common technique in machine learning to scale features. It is performed by subtracting the mean and dividing by the standard deviation.
        """)

        st.code("""
            # Z-score normalization
            arr_data = np.array([1, 2, 3, 4, 5])

            # Calculate the mean and standard deviation
            mean_data = np.mean(arr_data)
            std_data = np.std(arr_data)

            # Normalize
            normalized_data = (arr_data - mean_data) / std_data
            st.write(f"Z-score normalized data: {normalized_data}")
        """)

        # Z-score normalization example
        arr_data = np.array([1, 2, 3, 4, 5])
        mean_data = np.mean(arr_data)
        std_data = np.std(arr_data)
        normalized_data = (arr_data - mean_data) / std_data
        st.write(f"Z-score normalized data: {normalized_data}")

    case "sum() Function":

        st.title("NumPy `sum()` Function and Axis")

        # Introduction to `sum()` function
        st.header("What is the `sum()` Function?")
        st.write("""
            The `sum()` function in NumPy is used to calculate the sum of elements in an array.
            It is a simple yet powerful tool for performing aggregations and statistical operations.
            
            Syntax:
            ```python
            np.sum(arr, axis=None, dtype=None, out=None, keepdims=False)
            ```
            - **arr**: The input array.
            - **axis**: The axis or axes along which the sum is computed. If `None` (default), the sum of all elements is computed.
            - **dtype**: The data type for the sum.
            - **out**: The location to store the result.
            - **keepdims**: If `True`, the reduced dimensions are kept in the result as dimensions with size one.

            This function is commonly used in data analysis, machine learning, and deep learning for tasks such as aggregation and loss function computation.
        """)

        # Example 1: Sum of all elements in a 1D array
        st.subheader("Example 1: Sum of all elements in a 1D array")
        st.write("""
            In this example, we'll calculate the sum of a simple 1D array.
        """)

        st.code("""
            # Create a 1D array
            arr = np.array([1, 2, 3, 4, 5])

            # Calculate the sum
            result = np.sum(arr)
            st.write(f"Sum of the array: {result}")
        """)

        # Sum of a 1D array example 1
        arr = np.array([1, 2, 3, 4, 5])
        result = np.sum(arr)
        st.write(f"Sum of the array: {result}")

        st.write("""
            The sum of the array `[1, 2, 3, 4, 5]` is:
            ```
            15
            ```
        """)

        # Example 2: Sum along axis 0 (Row-wise in a 2D array)
        st.subheader("Example 2: Sum along axis 0 (Row-wise in a 2D array)")
        st.write("""
            In this example, we will calculate the sum of each column (along axis 0) in a 2D array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

            # Calculate the sum along axis 0 (columns)
            result = np.sum(arr_2d, axis=0)
            st.write(f"Sum along axis 0 (columns): {result}")
        """)

        # Sum along axis 0 example 2
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        result = np.sum(arr_2d, axis=0)
        st.write(f"Sum along axis 0 (columns): {result}")

        st.write("""
            The sum along axis 0 (columns) of the 2D array is:
            ```
            [9 12]
            ```
            This is the sum of each column.
        """)

        # Example 3: Sum along axis 1 (Column-wise in a 2D array)
        st.subheader("Example 3: Sum along axis 1 (Column-wise in a 2D array)")
        st.write("""
            In this example, we will calculate the sum of each row (along axis 1) in a 2D array.
        """)

        st.code("""
            # Calculate the sum along axis 1 (rows)
            result = np.sum(arr_2d, axis=1)
            st.write(f"Sum along axis 1 (rows): {result}")
        """)

        # Sum along axis 1 example 3
        result = np.sum(arr_2d, axis=1)
        st.write(f"Sum along axis 1 (rows): {result}")

        st.write("""
            The sum along axis 1 (rows) of the 2D array is:
            ```
            [3 7 11]
            ```
            This is the sum of each row.
        """)

        # Example 4: Sum in multi-dimensional arrays (3D array)
        st.subheader("Example 4: Sum in a 3D array")
        st.write("""
            In this example, we calculate the sum in a 3D array along different axes.
        """)

        st.code("""
            # Create a 3D array
            arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

            # Calculate the sum along axis 0
            result_0 = np.sum(arr_3d, axis=0)

            # Calculate the sum along axis 1
            result_1 = np.sum(arr_3d, axis=1)

            st.write(f"Sum along axis 0: {result_0}")
            st.write(f"Sum along axis 1: {result_1}")
        """)

        # Sum in a 3D array example 4
        arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result_0 = np.sum(arr_3d, axis=0)
        result_1 = np.sum(arr_3d, axis=1)
        st.write(f"Sum along axis 0: {result_0}")
        st.write(f"Sum along axis 1: {result_1}")

        st.write("""
            In the case of a 3D array:
            - The sum along axis 0 gives the sum across the depth of the array.
            - The sum along axis 1 gives the sum across the rows in each matrix.
        """)

        # Use of Sum in ML and DL
        st.header("How the `sum()` Function Helps in ML, DL, and Data Analysis")
        st.write("""
            - **Loss Function Calculation**: In deep learning, the `sum()` function is used in the calculation of the loss function. For example, in the Mean Squared Error (MSE) loss function, the sum of squared errors is computed before averaging over all samples.
            
            - **Aggregation**: In machine learning, the `sum()` function is often used to compute aggregate metrics, such as the total number of correct predictions, sum of residuals, or total error in a model.
            
            - **Feature Engineering**: When working with datasets, the `sum()` function can be used to compute the sum of features, which may be useful for feature engineering, such as creating new features that capture the total sum of certain attributes.

            - **Data Analysis**: In data analysis, the `sum()` function is used to compute totals, such as the total sales in a dataset or the total count of events in a time period.
        """)

        # Example of calculating total loss (Sum of errors)
        st.subheader("Example: Calculating Total Loss Using `sum()` Function")
        st.write("""
            In machine learning, we may calculate the sum of the errors to get an idea of how well the model is performing.
        """)

        st.code("""
            # Example of calculating loss (difference between predicted and actual)
            predicted = np.array([3, 4, 5])
            actual = np.array([2, 4, 6])

            # Calculate the sum of squared errors
            squared_errors = (predicted - actual) ** 2
            total_loss = np.sum(squared_errors)
            st.write(f"Total loss (sum of squared errors): {total_loss}")
        """)

        # Total loss example
        predicted = np.array([3, 4, 5])
        actual = np.array([2, 4, 6])
        squared_errors = (predicted - actual) ** 2
        total_loss = np.sum(squared_errors)
        st.write(f"Total loss (sum of squared errors): {total_loss}")

    case "subtract() Function":
        

        st.title("NumPy `subtract()` Function")

        # Introduction to np.subtract()
        st.header("What is the `subtract()` Function?")
        st.write("""
            The `subtract()` function in NumPy is used to subtract the elements of one array from another. It performs element-wise subtraction.
            This function is commonly used in data analysis, machine learning, and deep learning to calculate differences, residuals, or errors.
            
            Syntax:
            ```python
            np.subtract(x1, x2, out=None, where=True)
            ```
            - **x1**: The first input array.
            - **x2**: The second input array.
            - **out**: An optional output array to store the result.
            - **where**: A condition for where to apply the operation.
        """)

        # Example 1: Subtraction of two 1D arrays
        st.subheader("Example 1: Subtracting two 1D arrays")
        st.write("""
            Let's subtract two 1D arrays element-wise.
        """)

        st.code("""
            # Create two 1D arrays
            arr1 = np.array([5, 10, 15])
            arr2 = np.array([1, 2, 3])

            # Perform subtraction
            result = np.subtract(arr1, arr2)
            st.write(f"Result of subtraction: {result}")
        """)

        # Subtract two 1D arrays
        arr1 = np.array([5, 10, 15])
        arr2 = np.array([1, 2, 3])
        result = np.subtract(arr1, arr2)
        st.write(f"Result of subtraction: {result}")
        st.write("""
            The result of subtracting `[1, 2, 3]` from `[5, 10, 15]` is:
            ```
            [4, 8, 12]
            ```
        """)

        # Example 2: Subtraction along axis in a 2D array (row-wise and column-wise)
        st.subheader("Example 2: Subtracting along an axis in a 2D array")
        st.write("""
            In this example, we subtract each row or each column from a specific value.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[5, 10], [15, 20], [25, 30]])

            # Subtract a scalar value (e.g., 5) from each element
            result_scalar = np.subtract(arr_2d, 5)

            # Subtract another 2D array element-wise
            arr2_2d = np.array([[1, 2], [3, 4], [5, 6]])
            result_elementwise = np.subtract(arr_2d, arr2_2d)

            st.write(f"Result of subtracting scalar 5: {result_scalar}")
            st.write(f"Result of subtracting element-wise: {result_elementwise}")
        """)

        # Subtract scalar and element-wise 2D arrays
        arr_2d = np.array([[5, 10], [15, 20], [25, 30]])
        result_scalar = np.subtract(arr_2d, 5)
        arr2_2d = np.array([[1, 2], [3, 4], [5, 6]])
        result_elementwise = np.subtract(arr_2d, arr2_2d)

        st.write(f"Result of subtracting scalar 5: {result_scalar}")
        st.write(f"Result of subtracting element-wise: {result_elementwise}")

        st.write("""
            - Subtracting scalar 5 from each element gives:
            ```
            [[ 0  5]
            [10 15]
            [20 25]]
            ```

            - Subtracting the 2D array `[[1, 2], [3, 4], [5, 6]]` from the original array gives:
            ```
            [[ 4  8]
            [12 16]
            [20 24]]
            ```
        """)

        # Example 3: Subtracting across different dimensions
        st.subheader("Example 3: Subtracting arrays with different shapes (broadcasting)")
        st.write("""
            Broadcasting allows us to subtract arrays of different shapes, as long as they are compatible.
        """)

        st.code("""
            # Create a 2D array and a 1D array
            arr_2d = np.array([[5, 10], [15, 20], [25, 30]])
            arr_1d = np.array([1, 2])

            # Perform broadcasting subtraction
            result_broadcasting = np.subtract(arr_2d, arr_1d)

            st.write(f"Result with broadcasting: {result_broadcasting}")
        """)

        # Subtract with broadcasting
        arr_2d = np.array([[5, 10], [15, 20], [25, 30]])
        arr_1d = np.array([1, 2])
        result_broadcasting = np.subtract(arr_2d, arr_1d)

        st.write(f"Result with broadcasting: {result_broadcasting}")

        st.write("""
            The result of subtracting the 1D array `[1, 2]` from each row of the 2D array is:
            ```
            [[ 4  8]
            [14 18]
            [24 28]]
            ```
            Here, the 1D array is broadcast across the rows of the 2D array, subtracting element-wise.
        """)

        # Use of `subtract()` in ML and DL
        st.header("How the `subtract()` Function Helps in ML, DL, and Data Analysis")
        st.write("""
            - **Error Calculation**: In machine learning and deep learning, the `subtract()` function is frequently used to calculate residuals or errors. For instance, subtracting predicted values from actual values in regression tasks, or computing the error terms in optimization.
            
            - **Loss Function**: In neural networks, subtraction is a key component in computing loss functions like Mean Squared Error (MSE), where the difference between predicted and actual values is squared and summed.
            
            - **Feature Engineering**: The `subtract()` function can also be used to create new features, such as calculating the difference between two variables over time or between different samples.

            - **Data Transformation**: In data preprocessing, subtraction helps in scaling and normalization tasks, such as centering the data by subtracting the mean from each feature.
        """)

        # Example of calculating error (in regression)
        st.subheader("Example: Calculating Errors in Regression")
        st.write("""
            In regression, we subtract the predicted values from the actual values to calculate the error.
        """)

        st.code("""
            # Predicted and actual values
            predicted = np.array([2.5, 0.5, 2.1, 7.8])
            actual = np.array([3.0, 0.0, 2.0, 8.0])

            # Subtract predicted from actual to get the error
            error = np.subtract(predicted, actual)
            st.write(f"Errors: {error}")
        """)

        # Error calculation example
        predicted = np.array([2.5, 0.5, 2.1, 7.8])
        actual = np.array([3.0, 0.0, 2.0, 8.0])
        error = np.subtract(predicted, actual)
        st.write(f"Errors: {error}")

    case "multiply() Function":

        st.title("NumPy `multiply()` Function")

        # Introduction to np.multiply()
        st.header("What is the `multiply()` Function?")
        st.write("""
            The `multiply()` function in NumPy is used to perform element-wise multiplication of two arrays. 
            This operation is highly efficient and supports broadcasting, allowing arrays of different shapes to be multiplied, 
            as long as they follow the broadcasting rules.
            
            Syntax:
            ```python
            np.multiply(x1, x2, out=None, where=True)
            ```
            - **x1**: The first input array.
            - **x2**: The second input array.
            - **out**: An optional output array to store the result.
            - **where**: An optional condition for where to apply the operation.
        """)

        # Example 1: Element-wise multiplication of two 1D arrays
        st.subheader("Example 1: Element-wise multiplication of two 1D arrays")
        st.write("""
            Let's multiply two 1D arrays element-wise.
        """)

        st.code("""
            # Create two 1D arrays
            arr1 = np.array([2, 4, 6])
            arr2 = np.array([1, 2, 3])

            # Perform multiplication
            result = np.multiply(arr1, arr2)
            st.write(f"Result of multiplication: {result}")
        """)

        # Multiplying two 1D arrays
        arr1 = np.array([2, 4, 6])
        arr2 = np.array([1, 2, 3])
        result = np.multiply(arr1, arr2)
        st.write(f"Result of multiplication: {result}")
        st.write("""
            The result of multiplying `[2, 4, 6]` and `[1, 2, 3]` element-wise is:
            ```
            [2, 8, 18]
            ```
        """)

        # Example 2: Element-wise multiplication of 2D arrays
        st.subheader("Example 2: Element-wise multiplication of two 2D arrays")
        st.write("""
            In this example, we'll multiply two 2D arrays element-wise.
        """)

        st.code("""
            # Create two 2D arrays
            arr1_2d = np.array([[2, 4], [6, 8]])
            arr2_2d = np.array([[1, 2], [3, 4]])

            # Perform element-wise multiplication
            result_2d = np.multiply(arr1_2d, arr2_2d)
            st.write(f"Result of 2D multiplication: {result_2d}")
        """)

        # Multiplying two 2D arrays
        arr1_2d = np.array([[2, 4], [6, 8]])
        arr2_2d = np.array([[1, 2], [3, 4]])
        result_2d = np.multiply(arr1_2d, arr2_2d)
        st.write(f"Result of 2D multiplication: {result_2d}")
        st.write("""
            The result of multiplying the 2D arrays element-wise is:
            ```
            [[ 2  8]
            [18 32]]
            ```
        """)

        # Example 3: Multiplication with broadcasting
        st.subheader("Example 3: Multiplying with broadcasting")
        st.write("""
            Broadcasting allows us to multiply arrays of different shapes.
            Let's multiply a 2D array with a 1D array using broadcasting.
        """)

        st.code("""
            # Create a 2D array and a 1D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
            arr_1d = np.array([2, 3])

            # Perform multiplication with broadcasting
            result_broadcasting = np.multiply(arr_2d, arr_1d)
            st.write(f"Result with broadcasting: {result_broadcasting}")
        """)

        # Multiplying with broadcasting
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        arr_1d = np.array([2, 3])
        result_broadcasting = np.multiply(arr_2d, arr_1d)

        st.write(f"Result with broadcasting: {result_broadcasting}")
        st.write("""
            The result of multiplying the 2D array by the 1D array is:
            ```
            [[ 2  6]
            [ 6 12]
            [10 18]]
            ```
            Here, the 1D array `[2, 3]` is broadcast across each row of the 2D array.
        """)

        # Example 4: Scalar multiplication
        st.subheader("Example 4: Scalar multiplication")
        st.write("""
            You can also multiply a scalar with an array. This is called scalar multiplication.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

            # Multiply by a scalar value
            scalar_result = np.multiply(arr_2d, 3)
            st.write(f"Result of scalar multiplication: {scalar_result}")
        """)

        # Scalar multiplication
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        scalar_result = np.multiply(arr_2d, 3)
        st.write(f"Result of scalar multiplication: {scalar_result}")
        st.write("""
            The result of multiplying the array by the scalar value `3` is:
            ```
            [[ 3  6]
            [ 9 12]
            [15 18]]
            ```
        """)

        # Example 5: Multiplying arrays with different dimensions (broadcasting)
        st.subheader("Example 5: Multiplying arrays with different dimensions")
        st.write("""
            Broadcasting also allows multiplication between arrays of different dimensions.
        """)

        st.code("""
            # Create a 1D array and a 2D array
            arr_1d = np.array([1, 2])
            arr_2d = np.array([[1, 2], [3, 4]])

            # Perform multiplication with broadcasting
            result_diff_dims = np.multiply(arr_1d, arr_2d)
            st.write(f"Result of multiplication with different dimensions: {result_diff_dims}")
        """)

        # Multiplying arrays with different dimensions
        arr_1d = np.array([1, 2])
        arr_2d = np.array([[1, 2], [3, 4]])
        result_diff_dims = np.multiply(arr_1d, arr_2d)

        st.write(f"Result of multiplication with different dimensions: {result_diff_dims}")
        st.write("""
            The result of multiplying the 1D array `[1, 2]` with the 2D array `[[1, 2], [3, 4]]` using broadcasting is:
            ```
            [[1 2]
            [3 8]]
            ```
        """)

    case "divide() Function":

        st.title("NumPy `divide()` Function")

        # Introduction to np.divide()
        st.header("What is the `divide()` Function?")
        st.write("""
            The `divide()` function in NumPy is used to perform element-wise division between two arrays. 
            This operation supports broadcasting, which allows arrays of different shapes to be divided, 
            as long as they follow broadcasting rules.
            
            Syntax:
            ```python
            np.divide(x1, x2, out=None, where=True)
            ```
            - **x1**: The first input array.
            - **x2**: The second input array.
            - **out**: An optional output array to store the result.
            - **where**: An optional condition to specify where to apply the operation.
        """)

        # Example 1: Element-wise division of two 1D arrays
        st.subheader("Example 1: Element-wise division of two 1D arrays")
        st.write("""
            Let's divide two 1D arrays element-wise.
        """)

        st.code("""
            # Create two 1D arrays
            arr1 = np.array([6, 12, 18])
            arr2 = np.array([2, 4, 6])

            # Perform division
            result = np.divide(arr1, arr2)
            st.write(f"Result of division: {result}")
        """)

        # Performing division
        arr1 = np.array([6, 12, 18])
        arr2 = np.array([2, 4, 6])
        result = np.divide(arr1, arr2)
        st.write(f"Result of division: {result}")
        st.write("""
            The result of dividing `[6, 12, 18]` by `[2, 4, 6]` element-wise is:
            ```
            [3. 3. 3.]
            ```
        """)

        # Example 2: Element-wise division of 2D arrays
        st.subheader("Example 2: Element-wise division of two 2D arrays")
        st.write("""
            In this example, we'll divide two 2D arrays element-wise.
        """)

        st.code("""
            # Create two 2D arrays
            arr1_2d = np.array([[6, 12], [18, 24]])
            arr2_2d = np.array([[2, 4], [6, 8]])

            # Perform element-wise division
            result_2d = np.divide(arr1_2d, arr2_2d)
            st.write(f"Result of 2D division: {result_2d}")
        """)

        # Performing division on 2D arrays
        arr1_2d = np.array([[6, 12], [18, 24]])
        arr2_2d = np.array([[2, 4], [6, 8]])
        result_2d = np.divide(arr1_2d, arr2_2d)
        st.write(f"Result of 2D division: {result_2d}")
        st.write("""
            The result of dividing the 2D arrays element-wise is:
            ```
            [[3. 3.]
            [3. 3.]]
            ```
        """)

        # Example 3: Division with broadcasting
        st.subheader("Example 3: Division with broadcasting")
        st.write("""
            Broadcasting allows us to divide arrays of different shapes.
            Let's divide a 2D array by a 1D array using broadcasting.
        """)

        st.code("""
            # Create a 2D array and a 1D array
            arr_2d = np.array([[2, 4], [6, 8], [10, 12]])
            arr_1d = np.array([2, 4])

            # Perform division with broadcasting
            result_broadcasting = np.divide(arr_2d, arr_1d)
            st.write(f"Result with broadcasting: {result_broadcasting}")
        """)

        # Performing division with broadcasting
        arr_2d = np.array([[2, 4], [6, 8], [10, 12]])
        arr_1d = np.array([2, 4])
        result_broadcasting = np.divide(arr_2d, arr_1d)

        st.write(f"Result with broadcasting: {result_broadcasting}")
        st.write("""
            The result of dividing the 2D array by the 1D array using broadcasting is:
            ```
            [[1. 1.]
            [3. 2.]
            [5. 3.]]
            ```
            Here, the 1D array `[2, 4]` is broadcast across each row of the 2D array.
        """)

        # Example 4: Scalar division
        st.subheader("Example 4: Scalar division")
        st.write("""
            You can also divide an array by a scalar. This is called scalar division.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

            # Divide by a scalar value
            scalar_result = np.divide(arr_2d, 2)
            st.write(f"Result of scalar division: {scalar_result}")
        """)

        # Scalar division
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        scalar_result = np.divide(arr_2d, 2)
        st.write(f"Result of scalar division: {scalar_result}")
        st.write("""
            The result of dividing the array by the scalar value `2` is:
            ```
            [[0.5 1. ]
            [1.5 2. ]
            [2.5 3. ]]
            ```
        """)

        # Example 5: Handling division by zero
        st.subheader("Example 5: Handling division by zero")
        st.write("""
            NumPy handles division by zero gracefully, either by returning `inf` or `nan`.
        """)

        st.code("""
            # Create an array with a zero
            arr_1 = np.array([6, 0, 18])
            arr_2 = np.array([2, 0, 6])

            # Perform division
            result_zero = np.divide(arr_1, arr_2)
            st.write(f"Result with division by zero: {result_zero}")
        """)

        # Division with zero
        arr_1 = np.array([6, 0, 18])
        arr_2 = np.array([2, 0, 6])
        result_zero = np.divide(arr_1, arr_2)

        st.write(f"Result with division by zero: {result_zero}")
        st.write("""
            The result of dividing the arrays with a zero in the second array is:
            ```
            [ 3.  inf  3.]
            ```
            Division by zero results in `inf` for the second element.
        """)

    case "floor_divide() Function":

        st.title("NumPy `floor_divide()` Function")

        # Introduction to np.floor_divide()
        st.header("What is the `floor_divide()` Function?")
        st.write("""
            The `floor_divide()` function in NumPy is used to perform element-wise division between two arrays, 
            followed by applying the floor operation to the result. This means that the result is rounded down to 
            the nearest integer.
            
            Syntax:
            ```python
            np.floor_divide(x1, x2, out=None, where=True)
            ```
            - **x1**: The first input array.
            - **x2**: The second input array.
            - **out**: Optional output array to store the result.
            - **where**: Optional condition to specify where to apply the operation.
        """)

        # Example 1: Element-wise floor division of two 1D arrays
        st.subheader("Example 1: Element-wise floor division of two 1D arrays")
        st.write("""
            Let's perform floor division on two 1D arrays.
        """)

        st.code("""
            # Create two 1D arrays
            arr1 = np.array([9, 18, 27])
            arr2 = np.array([4, 7, 5])

            # Perform floor division
            result = np.floor_divide(arr1, arr2)
            st.write(f"Result of floor division: {result}")
        """)

        # Performing floor division
        arr1 = np.array([9, 18, 27])
        arr2 = np.array([4, 7, 5])
        result = np.floor_divide(arr1, arr2)
        st.write(f"Result of floor division: {result}")
        st.write("""
            The result of performing floor division on `[9, 18, 27]` and `[4, 7, 5]` is:
            ```
            [2 2 5]
            ```
            The division results are rounded down to the nearest integer.
        """)

        # Example 2: Element-wise floor division of 2D arrays
        st.subheader("Example 2: Element-wise floor division of two 2D arrays")
        st.write("""
            In this example, we'll floor divide two 2D arrays element-wise.
        """)

        st.code("""
            # Create two 2D arrays
            arr1_2d = np.array([[10, 20], [30, 40]])
            arr2_2d = np.array([[3, 5], [7, 9]])

            # Perform floor division
            result_2d = np.floor_divide(arr1_2d, arr2_2d)
            st.write(f"Result of 2D floor division: {result_2d}")
        """)

        # Performing floor division on 2D arrays
        arr1_2d = np.array([[10, 20], [30, 40]])
        arr2_2d = np.array([[3, 5], [7, 9]])
        result_2d = np.floor_divide(arr1_2d, arr2_2d)
        st.write(f"Result of 2D floor division: {result_2d}")
        st.write("""
            The result of performing floor division on the 2D arrays is:
            ```
            [[3 4]
            [4 4]]
            ```
            The division results are rounded down to the nearest integer.
        """)

        # Example 3: Division with broadcasting
        st.subheader("Example 3: Floor division with broadcasting")
        st.write("""
            Broadcasting allows us to divide arrays of different shapes. 
            Let's perform floor division with broadcasting.
        """)

        st.code("""
            # Create a 2D array and a 1D array
            arr_2d = np.array([[10, 20], [30, 40], [50, 60]])
            arr_1d = np.array([3, 6])

            # Perform floor division with broadcasting
            result_broadcasting = np.floor_divide(arr_2d, arr_1d)
            st.write(f"Result with broadcasting: {result_broadcasting}")
        """)

        # Performing floor division with broadcasting
        arr_2d = np.array([[10, 20], [30, 40], [50, 60]])
        arr_1d = np.array([3, 6])
        result_broadcasting = np.floor_divide(arr_2d, arr_1d)

        st.write(f"Result with broadcasting: {result_broadcasting}")
        st.write("""
            The result of floor division with broadcasting is:
            ```
            [[3 3]
            [10 6]
            [16 10]]
            ```
            The 1D array `[3, 6]` is broadcast across each row of the 2D array.
        """)

        # Example 4: Scalar floor division
        st.subheader("Example 4: Scalar floor division")
        st.write("""
            You can also floor divide an array by a scalar. This is called scalar floor division.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

            # Floor divide by a scalar value
            scalar_result = np.floor_divide(arr_2d, 2)
            st.write(f"Result of scalar floor division: {scalar_result}")
        """)

        # Scalar floor division
        arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
        scalar_result = np.floor_divide(arr_2d, 2)
        st.write(f"Result of scalar floor division: {scalar_result}")
        st.write("""
            The result of floor dividing the array by the scalar value `2` is:
            ```
            [[0 1]
            [1 2]
            [2 3]]
            ```
        """)

    case "argmin() Function":

        st.title("argmin() Function")

        # Introduction to np.argmin()
        st.header("What is the `argmin()` Function?")
        st.write("""
            The `argmin()` function in NumPy is used to return the index of the minimum value along a specified axis.
            - **axis=None**: The function will return the index of the minimum value in the flattened array.
            - **axis=0**: Find the minimum value along columns (vertical axis).
            - **axis=1**: Find the minimum value along rows (horizontal axis).
        """)

        # Example 1: argmin on 1D array
        st.subheader("Example 1: argmin on a 1D array")
        st.write("""
            Let's find the index of the minimum value in a 1D array.
        """)

        st.code("""
            # Create a 1D array
            arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

            # Find the index of the minimum value
            result = np.argmin(arr)
            st.write(f"Index of the minimum value: {result}")
        """)

        # Perform argmin on 1D array
        arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
        result = np.argmin(arr)
        st.write(f"Index of the minimum value: {result}")
        st.write("""
            The minimum value in the array is `1`, and its index is `1`.
        """)

        # Example 2: argmin on 2D array along axis 0 (columns)
        st.subheader("Example 2: argmin on 2D array along axis 0 (columns)")
        st.write("""
            Now, let's find the index of the minimum value in each column of a 2D array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

            # Find the index of the minimum value along each column (axis=0)
            result_axis0 = np.argmin(arr_2d, axis=0)
            st.write(f"Index of the minimum value along each column: {result_axis0}")
        """)

        # Perform argmin on 2D array along axis 0 (columns)
        arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
        result_axis0 = np.argmin(arr_2d, axis=0)
        st.write(f"Index of the minimum value along each column: {result_axis0}")
        st.write("""
            The minimum values along each column are at indices `[1, 0, 0]` respectively.
        """)

        # Example 3: argmin on 2D array along axis 1 (rows)
        st.subheader("Example 3: argmin on 2D array along axis 1 (rows)")
        st.write("""
            In this example, let's find the index of the minimum value in each row of a 2D array.
        """)

        st.code("""
            # Find the index of the minimum value along each row (axis=1)
            result_axis1 = np.argmin(arr_2d, axis=1)
            st.write(f"Index of the minimum value along each row: {result_axis1}")
        """)

        # Perform argmin on 2D array along axis 1 (rows)
        result_axis1 = np.argmin(arr_2d, axis=1)
        st.write(f"Index of the minimum value along each row: {result_axis1}")
        st.write("""
            The minimum values along each row are at indices `[1, 0, 0]` respectively.
        """)

        # Example 4: argmin on a flattened 2D array
        st.subheader("Example 4: argmin on a flattened 2D array")
        st.write("""
            If no axis is specified, the function returns the index of the minimum value in the flattened array.
        """)

        st.code("""
            # Flatten the 2D array and find the index of the minimum value
            flattened_result = np.argmin(arr_2d)
            st.write(f"Index of the minimum value in the flattened array: {flattened_result}")
        """)

        # Perform argmin on a flattened 2D array
        flattened_result = np.argmin(arr_2d)
        st.write(f"Index of the minimum value in the flattened array: {flattened_result}")
        st.write("""
            The flattened array is `[3, 1, 4, 1, 5, 9, 2, 6, 5]`. The index of the minimum value `1` is `1`.
        """)

    case "Sorting Rows and Columns in NumPy":

        st.title("Sorting Rows and Columns in NumPy")

        # Introduction to sorting in NumPy
        st.header("Sorting Rows and Columns in NumPy")
        st.write("""
            The `np.sort()` function can be used to sort arrays row-wise and column-wise:
            - **axis=0**: Sorts each column (vertical sort).
            - **axis=1**: Sorts each row (horizontal sort).
        """)

        # Example 1: Row-wise sorting
        st.subheader("Example 1: Row-wise Sorting")
        st.write("""
            Let's sort the rows of a 2D array.
        """)

        st.code("""
            # Create a 2D array
            arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

            # Sort rows (axis=1)
            row_sorted = np.sort(arr_2d, axis=1)
            st.write(f"Row-wise sorted array:\\n{row_sorted}")
        """)

        # Perform row-wise sorting
        arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
        row_sorted = np.sort(arr_2d, axis=1)
        st.write(f"Row-wise sorted array:\n{row_sorted}")
        st.write("""
            The array after sorting each row is:
            ```
            [[1 3 4]
            [1 5 9]
            [2 5 6]]
            ```
        """)

        # Example 2: Column-wise sorting
        st.subheader("Example 2: Column-wise Sorting")
        st.write("""
            Now, let's sort the columns of the 2D array.
        """)

        st.code("""
            # Sort columns (axis=0)
            col_sorted = np.sort(arr_2d, axis=0)
            st.write(f"Column-wise sorted array:\\n{col_sorted}")
        """)

        # Perform column-wise sorting
        col_sorted = np.sort(arr_2d, axis=0)
        st.write(f"Column-wise sorted array:\n{col_sorted}")
        st.write("""
            The array after sorting each column is:
            ```
            [[1 1 4]
            [2 5 5]
            [3 6 9]]
            ```
        """)

        
    case "Lexicographical Sorting":

        st.title("Lexicographical Sorting with `np.lexsort()`")

        # Introduction to np.lexsort()
        st.header("What is Lexicographical Sorting?")
        st.write("""
            Lexicographical sorting is a method for sorting data based on multiple keys. In `np.lexsort()`, 
            the last key in the list is the primary key for sorting, and the first key is the least significant key.
        """)

        # Explanation of the function
        st.write("""
            **Syntax**:
            ```python
            np.lexsort(keys, axis=-1)
            ```
            - **keys**: A tuple or list of arrays representing the sorting keys.
            - **axis**: The axis along which to sort (default is `-1`).
        """)

        # Example 1: Lexicographical sorting with simple data
        st.subheader("Example 1: Lexicographical Sorting with Simple Data")
        st.write("""
            Consider an array representing people's ages and their scores. We want to sort primarily by age and, 
            in cases of ties, by scores.
        """)

        st.code("""
            # Define two key arrays
            ages = np.array([25, 30, 22, 25, 28])
            scores = np.array([85, 95, 80, 90, 88])

            # Perform lexicographical sorting
            indices = np.lexsort((scores, ages))
            
            # Display sorted results
            sorted_ages = ages[indices]
            sorted_scores = scores[indices]

            st.write(f"Indices of sorted data: {indices}")
            st.write(f"Sorted ages: {sorted_ages}")
            st.write(f"Sorted scores: {sorted_scores}")
        """)

        # Perform lexicographical sorting
        ages = np.array([25, 30, 22, 25, 28])
        scores = np.array([85, 95, 80, 90, 88])
        indices = np.lexsort((scores, ages))
        
        # Display results
        st.write("Original data:")
        st.write(f"Ages: {ages}")
        st.write(f"Scores: {scores}")
        st.write("Sorted indices from `np.lexsort()`: ", indices)

        sorted_ages = ages[indices]
        sorted_scores = scores[indices]

        st.write("Sorted data:")
        st.write(f"Sorted Ages: {sorted_ages}")
        st.write(f"Sorted Scores: {sorted_scores}")

        # Explanation of sorting order
        st.write("""
            In this example, the `ages` array is the primary key and the `scores` array is the secondary key.
            The data is sorted primarily by age and, for rows with the same age, by score.
        """)

        
    case "Vectorization in NumPy":

        st.title("Understanding Vectorization in NumPy")

        # Introduction to Vectorization
        st.header("What is Vectorization?")
        st.write("""
            Vectorization is the process of performing operations on entire arrays without the need for explicit Python loops.
            This results in highly efficient code due to the use of optimized C and Fortran libraries underneath.
            
            **Benefits of Vectorization:**
            - **Speed**: Operations are much faster compared to traditional Python loops.
            - **Simplicity**: Code is cleaner and more readable.
            - **Memory Efficiency**: Operations are performed in-place where possible, reducing overhead.
        """)

        # Basic Example of Vectorization
        st.subheader("Basic Example of Vectorization")
        st.write("""
            Let's compare a loop-based approach with a vectorized approach for adding two arrays.
        """)

        # Code snippet for loop-based approach
        st.code("""
        # Loop-based approach
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([10, 20, 30, 40, 50])
        result = []
        for i in range(len(a)):
            result.append(a[i] + b[i])
        result = np.array(result)
        st.write(f"Loop-based result: {result}")
        """, language="python")

        # Code snippet for vectorized approach
        st.code("""
        # Vectorized approach
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([10, 20, 30, 40, 50])
        result_vectorized = a + b
        st.write(f"Vectorized result: {result_vectorized}")
        """, language="python")


        st.write("""
            As we can see, the result from the loop-based and vectorized approaches is the same, 
            but the vectorized code is more concise and runs faster.
        """)

        # Example 2: Vectorized Mathematical Operations
        st.subheader("Example 2: Vectorized Mathematical Operations")
        st.write("""
            NumPy allows for vectorized operations such as addition, subtraction, multiplication, and division. 
            This can be extremely useful in data science and machine learning when performing operations on large datasets.
        """)

        # Demonstrating vectorized operations
        st.code("""
        array1 = np.array([2, 4, 6, 8])
        array2 = np.array([1, 2, 3, 4])

        st.write("Given arrays:")
        st.write("Array 1:", array1)
        st.write("Array 2:", array2)

        st.write("Addition:", array1 + array2)
        st.write("Subtraction:", array1 - array2)
        st.write("Multiplication:", array1 * array2)
        st.write("Division:", array1 / array2)""")


        # Example 3: Vectorized Functions using NumPy's Universal Functions (ufuncs)
        st.subheader("Example 3: Vectorized Functions with Universal Functions (ufuncs)")
        st.write("""
            NumPy provides built-in universal functions (ufuncs) that operate element-wise on arrays and are vectorized.
            Common ufuncs include `np.sin()`, `np.exp()`, `np.sqrt()`, and more.
        """)

        st.code("""# Demonstrating vectorized ufuncs
        x = np.linspace(0, 2 * np.pi, 5)
        st.write("Array for demonstration (x):", x)

        st.write("Sine of x:", np.sin(x))
        st.write("Exponential of x:", np.exp(x))
        st.write("Square root of x:", np.sqrt(x))""")

        # Conclusion
        st.write("""
            **Conclusion**:
            Vectorization in NumPy simplifies code and improves performance, making it essential for efficient data manipulation 
            and numerical computing in data science, machine learning, and other fields.
        """)

    case "apply_along_axis() Function":

        st.title("Understanding `numpy.apply_along_axis()`")

        # Explanation of `apply_along_axis`
        st.header("What is `numpy.apply_along_axis()`?")
        st.write("""
            `numpy.apply_along_axis()` is a powerful function that applies a given function to 1-D slices along the specified axis of an array.
            
            **Syntax**:
            ```python
            np.apply_along_axis(func1d, axis, arr, *args, **kwargs)
            ```
            
            - **`func1d`**: The function to apply to 1-D slices of the array.
            - **`axis`**: The axis along which the function is applied.
            - **`arr`**: The input array.
            - **`*args`**: Additional arguments passed to `func1d`.
            - **`**kwargs`**: Additional keyword arguments passed to `func1d`.
            
            This function is useful when you want to apply a custom operation on each row or column of an array.
        """)

        # Example array
        array = np.array([[1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]])
        
        st.write("Example 2D Array:")
        st.write(array)

        # Define a custom function to apply
        def custom_sum(x):
            return np.sum(x)

        st.subheader("Example: Applying a Custom Sum Function")
        st.write("""
            Let's apply a custom sum function to each row and column of the array using `apply_along_axis()`.
        """)

        # Applying the custom function along axis 1 (row-wise)
        sum_along_rows = np.apply_along_axis(custom_sum, axis=1, arr=array)
        st.write("Sum along rows (axis=1):", sum_along_rows)

        # Applying the custom function along axis 0 (column-wise)
        sum_along_columns = np.apply_along_axis(custom_sum, axis=0, arr=array)
        st.write("Sum along columns (axis=0):", sum_along_columns)

        st.write("""
            **Explanation**:
            - When `axis=1`, the function is applied to each row individually.
            - When `axis=0`, the function is applied to each column individually.
            
            In this example, we used `np.sum()` as the function, but you can replace it with any custom 1-D function.
        """)

    case "numpy.apply_over_axes() Function":

        st.title("Understanding `numpy.apply_over_axes()`")

        # Explanation of `apply_over_axes`
        st.header("What is `numpy.apply_over_axes()`?")
        st.write("""
            `numpy.apply_over_axes()` allows you to apply a function over multiple axes of an array at once.
            
            **Syntax**:
            ```python
            np.apply_over_axes(func, a, axes)
            ```
            
            - **`func`**: The function to apply to the input array `a`.
            - **`a`**: The input array.
            - **`axes`**: The axes over which the function should be applied.
            
            This function is especially useful when you need to apply an operation across multiple dimensions (e.g., both rows and columns) of an array.
        """)

        # Example array
        array = np.array([[1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]])
        
        st.write("Example 2D Array:")
        st.write(array)

        # Define a custom function to apply
        def custom_func(x):
            return np.sum(x)  # Sum the values over the axes

        st.subheader("Example: Applying `custom_func` Over Multiple Axes")
        st.write("""
            Let's apply a custom function that sums the values of an array over both `axis=0` (columns) and `axis=1` (rows).
        """)

        # Applying the custom function over axes (0 and 1)
        result = np.apply_over_axes(custom_func, array, axes=(0, 1))
        st.write("Result of applying custom function over both axes:", result)

        st.write("""
            **Explanation**:
            - The function `np.sum(x)` is applied over both the rows (axis=1) and columns (axis=0).
            - The result is a scalar value that sums all elements in the array.
        """)

    case "unique() Function":

        st.markdown("""
                    
            The `unique` function in NumPy is a versatile tool that lets you find and manage unique values in an array. This function is especially useful when dealing with datasets where you need to eliminate duplicates, count occurrences, or perform other operations on unique values. Here’s a comprehensive breakdown of how `np.unique` works and the options available for different use cases.

### Overview of `numpy.unique`

The `unique` function in NumPy provides several ways to interact with the unique values in an array, including finding unique elements, retrieving their indices, reconstructing the original array from the unique elements, and counting occurrences.

### Basic Syntax

```python
numpy.unique(array, return_index=False, return_inverse=False, return_counts=False)
```

- **array**: This is the main input array from which you want to find unique elements.
- **return_index**: When set to `True`, returns the indices of the first occurrences of the unique elements in the original array.
- **return_inverse**: When set to `True`, returns an array that can be used to reconstruct the original array from the unique array.
- **return_counts**: When set to `True`, returns the count of each unique element.

By default, `numpy.unique` only returns the unique elements in sorted order.

### Example 1: Basic Usage

In its simplest form, `np.unique` returns an array with unique values only:

```python
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_values = np.unique(arr)
print("Unique values:", unique_values)
```

**Output:**

```
Unique values: [1 2 3 4 5]
```

### Example 2: Using `return_index`

To get the indices of the first occurrence of each unique value in the original array, set `return_index=True`. This is helpful when you need to track where each unique element first appears.

```python
unique_values, indices = np.unique(arr, return_index=True)
print("Unique values:", unique_values)
print("Indices of unique values:", indices)
```

**Output:**

```
Unique values: [1 2 3 4 5]
Indices of unique values: [0 1 3 4 6]
```

In this example, the index array `[0, 1, 3, 4, 6]` indicates the positions of `1`, `2`, `3`, `4`, and `5` in the original array.

### Example 3: Using `return_inverse`

Setting `return_inverse=True` returns an array that shows how to reconstruct the original array from the unique values. This is useful if you need to map each original element back to its position in the unique array.

```python
unique_values, inverse = np.unique(arr, return_inverse=True)
print("Unique values:", unique_values)
print("Inverse indices:", inverse)
```

**Output:**

```
Unique values: [1 2 3 4 5]
Inverse indices: [0 1 1 2 3 3 4]
```

Here, the inverse indices array `[0, 1, 1, 2, 3, 3, 4]` indicates how to reconstruct the original array: `unique_values[inverse]` would produce `[1, 2, 2, 3, 4, 4, 5]`.

### Example 4: Using `return_counts`

When `return_counts=True`, `np.unique` returns an array indicating the count of each unique element. This is useful for finding the frequency of each element.

```python
unique_values, counts = np.unique(arr, return_counts=True)
print("Unique values:", unique_values)
print("Counts of unique values:", counts)
```

**Output:**

```
Unique values: [1 2 3 4 5]
Counts of unique values: [1 2 1 2 1]
```

In this case, the count array `[1, 2, 1, 2, 1]` tells us that:
- `1` appears once,
- `2` appears twice,
- `3` appears once,
- `4` appears twice, and
- `5` appears once.

### Combining Parameters

You can use any combination of `return_index`, `return_inverse`, and `return_counts` to get multiple outputs at once. For example:

```python
unique_values, indices, inverse, counts = np.unique(arr, return_index=True, return_inverse=True, return_counts=True)
print("Unique values:", unique_values)
print("Indices:", indices)
print("Inverse:", inverse)
print("Counts:", counts)
```

This will output all unique values, their indices, inverse indices, and counts simultaneously.

### Practical Applications of `numpy.unique`

1. **Removing Duplicates**: Use `np.unique` to easily remove duplicates from data, which can be useful in data cleaning.
   
2. **Counting Frequency**: By using `return_counts=True`, you can quickly summarize the frequency of each unique element, which is often helpful in data analysis.

3. **Data Reconstruction**: With `return_inverse=True`, you can reconstruct an array based on unique elements, which is beneficial in machine learning tasks where you want to map categories back to a smaller set of unique values.

### Summary

The `numpy.unique` function is a versatile tool that helps with duplicate removal, counting frequencies, and reconstructing original arrays. Understanding how to use its parameters efficiently can save you a lot of time, especially when working with large datasets.        
            
                    """)
    case "dot() Function":
        st.markdown("""
                    
            The dot product is a fundamental operation in linear algebra, widely used in fields like physics, computer science, and machine learning. In NumPy, the `dot` function allows you to compute the dot product of two arrays efficiently, whether they are vectors or matrices.

### Understanding the Dot Product

1. **Dot Product of Vectors**: For two vectors \( A \) and \( B \), the dot product is calculated as:
   \[
   A \cdot B = a_1 \times b_1 + a_2 \times b_2 + \dots + a_n \times b_n
   \]
   where \( a_i \) and \( b_i \) are the elements of \( A \) and \( B \), respectively.

2. **Matrix Multiplication**: For two matrices \( A \) and \( B \), the dot product is the matrix multiplication of \( A \) and \( B \). Each element in the resulting matrix is the dot product of a row in \( A \) with a column in \( B \).

### Basic Syntax of `numpy.dot`

In NumPy, the syntax for the dot product is straightforward:

```python
numpy.dot(a, b, out=None)
```

- **a**: First array (vector or matrix).
- **b**: Second array (vector or matrix).
- **out**: Optional. If provided, it stores the result in this array.

### Examples of Using `numpy.dot`

#### 1. Dot Product of Two Vectors

```python
import numpy as np

# Define two vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Compute the dot product
dot_product = np.dot(A, B)
print("Dot product of A and B:", dot_product)
```

**Output:**

```
Dot product of A and B: 32
```

This result is calculated as:
\[
1 \times 4 + 2 \times 5 + 3 \times 6 = 4 + 10 + 18 = 32
\]

#### 2. Matrix Multiplication Using `numpy.dot`

When `a` and `b` are 2D arrays (matrices), `numpy.dot` performs matrix multiplication.

```python
# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Compute the dot product (matrix multiplication)
result = np.dot(A, B)
print("Matrix product of A and B:\n", result)
```

**Output:**

```
Matrix product of A and B:
 [[19 22]
  [43 50]]
```

The calculation for each element in the resulting matrix is as follows:
- First row, first column: \(1 \times 5 + 2 \times 7 = 19\)
- First row, second column: \(1 \times 6 + 2 \times 8 = 22\)
- Second row, first column: \(3 \times 5 + 4 \times 7 = 43\)
- Second row, second column: \(3 \times 6 + 4 \times 8 = 50\)

#### 3. Dot Product with Higher-Dimensional Arrays

For arrays with more than two dimensions, `numpy.dot` behaves differently depending on the input shapes. Generally:
- If one or both arrays are 1D, `numpy.dot` treats them as vectors.
- For 2D arrays, `numpy.dot` performs matrix multiplication.
- For arrays with more than two dimensions, `numpy.dot` performs a sum-product over the last axis of `a` and the second-to-last axis of `b`.

### Practical Uses of Dot Product

1. **Cosine Similarity**: The dot product can be used to measure similarity between two vectors by calculating the cosine of the angle between them.

2. **Projection**: Dot products help project one vector onto another, which is essential in computer graphics and physics.

3. **Neural Networks**: In machine learning, dot products are used to compute the weighted sum of inputs and weights in neural networks.

4. **Solving Linear Systems**: Matrix multiplication (a form of dot product) is often used in solving linear systems in scientific computations.

### Summary

The `numpy.dot` function is a powerful and flexible tool in linear algebra. It can handle vector dot products, matrix multiplication, and even more complex operations on higher-dimensional arrays. This versatility makes it crucial for applications in data science, machine learning, and scientific computing.
                    """)
        
    case 'digitize() Function':
        st.markdown("""
                    
                    In NumPy, the `digitize` function is used to categorize or "bin" continuous data into discrete intervals. This is particularly useful in data analysis, where you may want to group data points into different ranges or categories. By using `numpy.digitize`, you can quickly assign data values to specified bins, which makes it easier to analyze patterns, summarize distributions, or visualize data in intervals.

### Syntax and Parameters

```python
numpy.digitize(x, bins, right=False)
```

- **x**: The input array of values you want to categorize or bin. This can be a one-dimensional array of numeric values.
- **bins**: A one-dimensional array defining the bin edges. This array should be sorted in ascending order.
- **right**: A boolean value (`False` by default). If `right=False`, the bins include the left edge and exclude the right edge (left-closed intervals). If `right=True`, the bins include the right edge and exclude the left edge (right-closed intervals).

### How `digitize` Works

The function checks each element in `x` to determine which bin it falls into, based on the bin edges in `bins`. It returns an array of the same shape as `x`, where each element is replaced by the bin index (1-based index) it belongs to. 

### Examples of Using `numpy.digitize`

#### 1. Basic Usage with Left-Closed Bins (`right=False`)

In this example, `right=False` means each bin includes its left edge but excludes the right edge.

```python
import numpy as np

# Data to categorize
x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])

# Define bins (left-closed intervals)
bins = np.array([1, 2, 3, 4])

# Categorize values into bins
indices = np.digitize(x, bins)
print("Binned indices:", indices)
```

**Output:**

```
Binned indices: [0 1 2 3 4]
```

Explanation:
- Values less than `1` are placed in bin `0`.
- The interval `[1, 2)` corresponds to bin `1`, so `1.5` falls in bin `1`.
- `2.5` is in the interval `[2, 3)`, corresponding to bin `2`.
- `3.5` is in the interval `[3, 4)`, corresponding to bin `3`.
- `4.5` falls outside all bins, so it's placed in the next bin index `4`.

#### 2. Using Right-Closed Bins (`right=True`)

With `right=True`, each bin includes its right edge and excludes the left edge, which can be useful when you want the bins to capture values up to and including their upper bound.

```python
indices = np.digitize(x, bins, right=True)
print("Binned indices with right-closed intervals:", indices)
```

**Output:**

```
Binned indices with right-closed intervals: [1 2 3 4 4]
```

Explanation:
- The interval `(0, 1]` corresponds to bin `1`, so `0.5` falls in bin `1`.
- The interval `(1, 2]` corresponds to bin `2`, so `1.5` falls in bin `2`.
- The interval `(2, 3]` corresponds to bin `3`, so `2.5` falls in bin `3`.
- `3.5` falls in bin `4`, in the interval `(3, 4]`.
- `4.5` also falls in bin `4`, as it meets the upper bound of `4`.

#### 3. Handling Values Outside of Bin Range

Values in `x` that fall below the lowest bin or above the highest bin are assigned indices outside the range of bins. For example, if a value in `x` is less than the smallest bin edge, it gets an index of `0`. If it’s greater than the highest bin edge, it’s assigned to the next bin index after the last bin.

```python
# Input data with values outside bin range
x = np.array([-1.0, 0.5, 1.5, 3.5, 5.0])

# Bins with left-closed intervals
indices = np.digitize(x, bins)
print("Binned indices with values outside bin range:", indices)
```

**Output:**

```
Binned indices with values outside bin range: [0 0 1 3 4]
```

Explanation:
- `-1.0` and `0.5` are both below the first bin (`1`), so they are assigned to index `0`.
- `5.0` is above the last bin (`4`), so it’s assigned to index `4`, the bin after the last defined interval.

#### 4. Using `digitize` for Data Grouping and Analysis

`digitize` is commonly used for grouping data. For example, suppose you have an array representing scores, and you want to categorize them into "grades" based on score ranges.

```python
scores = np.array([55, 70, 82, 90, 95])
grade_bins = np.array([60, 70, 80, 90])  # Define bins for grading

# Bin the scores
grade_indices = np.digitize(scores, grade_bins)
print("Grade indices:", grade_indices)

# Label each bin as a grade
grades = np.array(["F", "D", "C", "B", "A"])
assigned_grades = grades[grade_indices]
print("Assigned grades:", assigned_grades)
```

**Output:**

```
Grade indices: [0 1 2 3 4]
Assigned grades: ['F' 'D' 'C' 'B' 'A']
```

Explanation:
- The `grade_indices` array indicates the bin index for each score, and by using this array, the score is mapped to its corresponding grade.

### Practical Applications of `numpy.digitize`

1. **Data Grouping**: Often used in data analysis for grouping continuous data (e.g., temperatures, incomes) into intervals or categories.
2. **Histogram Binning**: Useful for preparing data for histogram visualizations or other interval-based summaries.
3. **Discretization for Machine Learning**: Often, continuous features need to be binned or categorized before training certain machine learning models.

### Summary

The `numpy.digitize` function is a powerful utility for organizing continuous data into discrete intervals. Its flexibility with bin types and interval configurations makes it a valuable tool in data preprocessing, analysis, and visualization. Understanding how to use `right` and how to handle values outside bin ranges can help in effective data grouping and categorization.
                    `""")
    
    case "clip() Function":
        st.markdown("""
                    
            The `clip` function in NumPy is used to limit or "clip" the values in an array within a specified range. Any values that are lower than a specified minimum are set to the minimum, and any values that are higher than a specified maximum are set to the maximum. This is useful when you want to limit the values of an array to a certain range, which is common in tasks like image processing, normalization, and data cleaning.

### Syntax of `numpy.clip`

```python
numpy.clip(a, a_min, a_max, out=None)
```

- **a**: The input array that you want to clip.
- **a_min**: The minimum value. Elements less than this will be set to `a_min`.
- **a_max**: The maximum value. Elements greater than this will be set to `a_max`.
- **out**: Optional. If provided, the result will be placed in this array. It should have the same shape as the input array.

### How `clip` Works

- For each element in the array:
  - If the element is less than `a_min`, it is replaced by `a_min`.
  - If the element is greater than `a_max`, it is replaced by `a_max`.
  - If the element falls within the range `[a_min, a_max]`, it remains unchanged.

The resulting array will contain values only within the specified range.

### Examples of Using `numpy.clip`

#### 1. Basic Clipping

Let's say you have an array of values, and you want to ensure that all values stay within a range of 0 to 10:

```python
import numpy as np

# Define an array
arr = np.array([5, -3, 12, 7, 0, 9, 15])

# Clip values to be within 0 and 10
clipped_arr = np.clip(arr, 0, 10)
print("Original array:", arr)
print("Clipped array:", clipped_arr)
```

**Output:**

```
Original array: [ 5 -3 12  7  0  9 15]
Clipped array: [ 5  0 10  7  0  9 10]
```

Explanation:
- Values less than 0 are set to 0 (e.g., -3 becomes 0).
- Values greater than 10 are set to 10 (e.g., 12 and 15 become 10).
- Values within the range 0 to 10 remain unchanged.

#### 2. Clipping with Only a Maximum or Only a Minimum

You can also clip only the minimum or only the maximum by setting `a_min` or `a_max` to `None`.

```python
# Define an array
arr = np.array([5, -3, 12, 7, 0, 9, 15])

# Clip only the maximum to 10
clipped_max = np.clip(arr, None, 10)
print("Clipped with max 10 only:", clipped_max)

# Clip only the minimum to 0
clipped_min = np.clip(arr, 0, None)
print("Clipped with min 0 only:", clipped_min)
```

**Output:**

```
Clipped with max 10 only: [ 5 -3 10  7  0  9 10]
Clipped with min 0 only: [ 5  0 12  7  0  9 15]
```

Explanation:
- **Clipping maximum only**: Values greater than 10 are set to 10; values less than 10 remain unchanged.
- **Clipping minimum only**: Values less than 0 are set to 0; values greater than 0 remain unchanged.

#### 3. Clipping on Multi-dimensional Arrays

`numpy.clip` can also work with multi-dimensional arrays. The clipping operation is applied element-wise.

```python
# Define a 2D array
arr_2d = np.array([[5, -3, 12], [7, 0, 9]])

# Clip values to be within 0 and 10
clipped_2d = np.clip(arr_2d, 0, 10)
print("Original 2D array:\n", arr_2d)
print("Clipped 2D array:\n", clipped_2d)
```

**Output:**

```
Original 2D array:
 [[ 5 -3 12]
  [ 7  0  9]]
Clipped 2D array:
 [[ 5  0 10]
  [ 7  0  9]]
```

Explanation:
Each element in the 2D array is clipped independently to fit within the range 0 to 10.

#### 4. Using `out` Parameter for In-Place Clipping

If you want to save memory or apply the clipping directly to an existing array, you can use the `out` parameter.

```python
# Define an array
arr = np.array([5, -3, 12, 7, 0, 9, 15])

# Clip values and store the result in the same array
np.clip(arr, 0, 10, out=arr)
print("In-place clipped array:", arr)
```

**Output:**

```
In-place clipped array: [ 5  0 10  7  0  9 10]
```

Explanation:
By using `out=arr`, the result is stored in `arr` itself, modifying the original array in-place.

### Practical Applications of `numpy.clip`

1. **Data Normalization**: Limiting data within a specific range is common in image processing, where pixel values may need to stay within `[0, 255]`.
   
2. **Removing Outliers**: Clipping can be used to set outliers to a maximum threshold, which can be useful for smoothing noisy data in machine learning.

3. **Bounding Calculated Values**: When calculating values that should stay within a range (e.g., probabilities between 0 and 1), `clip` ensures that calculations don’t exceed defined bounds.

### Summary

The `numpy.clip` function is a convenient tool for setting limits on array values. It’s useful for data cleaning, bounding values in calculations, and data normalization tasks. By understanding its behavior and the use of the `out` parameter, you can use `clip` efficiently in a variety of data preprocessing and manipulation tasks.
                    """)
    
    case "bincount() Function":
        st.markdown("""
                    
                    The `bincount` function in NumPy counts the occurrences of each value in an array of non-negative integers. This can be particularly useful for tasks such as counting frequencies, histogram generation, and data analysis where you need to know the count of each integer in a dataset.

### Syntax of `numpy.bincount`

```python
numpy.bincount(x, weights=None, minlength=0)
```

- **x**: The input array of non-negative integers.
- **weights**: Optional. If provided, this should be an array of the same length as `x` containing weights for each element in `x`. The resulting bins will contain the sum of weights rather than counts.
- **minlength**: Optional. Specifies the minimum length of the output array. If `minlength` is greater than the largest value in `x`, additional bins will be added at the end with a count of zero.

### How `bincount` Works

The function generates a 1D array where the value at each index represents the count of occurrences of that index in `x`. For example, if you have `x = [1, 2, 2, 3]`, then `np.bincount(x)` will return `[0, 1, 2, 1]`, indicating:
- 0 occurs 0 times.
- 1 occurs 1 time.
- 2 occurs 2 times.
- 3 occurs 1 time.

### Examples of Using `numpy.bincount`

#### 1. Basic Usage

```python
import numpy as np

# Define an array of integers
x = np.array([1, 2, 2, 3, 3, 3, 4])

# Count occurrences of each integer
counts = np.bincount(x)
print("Bin counts:", counts)
```

**Output:**

```
Bin counts: [0 1 2 3 1]
```

Explanation:
- `0` appears `0` times.
- `1` appears `1` time.
- `2` appears `2` times.
- `3` appears `3` times.
- `4` appears `1` time.

#### 2. Using `minlength` to Extend the Output Array

If you want the output to have a certain minimum length, you can use `minlength`. This is useful if you want a fixed-length array regardless of the values in `x`.

```python
# Set minlength to extend the output array
counts = np.bincount(x, minlength=6)
print("Bin counts with minlength=6:", counts)
```

**Output:**

```
Bin counts with minlength=6: [0 1 2 3 1 0]
```

Explanation:
The output array now has six elements. Any missing bins, like `5` in this example, have a count of `0`.

#### 3. Using Weights

If you want to calculate weighted counts, you can pass an array of weights to `weights`. In this case, each element in `x` is counted with its corresponding weight.

```python
# Define weights for each element in x
weights = np.array([0.5, 1.0, 1.5, 2.0, 0.5, 1.0, 1.5])

# Calculate weighted counts
weighted_counts = np.bincount(x, weights=weights)
print("Weighted bin counts:", weighted_counts)
```

**Output:**

```
Weighted bin counts: [0.  0.5 2.5 3.5 1.5]
```

Explanation:
- The value `1` has a weight of `0.5`.
- The value `2` appears twice with weights `1.0` and `1.5`, resulting in a total weight of `2.5`.
- The value `3` appears three times with weights `2.0`, `0.5`, and `1.0`, resulting in a total weight of `3.5`.
- The value `4` has a weight of `1.5`.

#### 4. Counting Frequencies of Large Arrays

`numpy.bincount` is highly optimized and can efficiently count occurrences in large arrays. This can be particularly useful in data analysis for counting discrete values.

```python
# Generate a large array of random integers between 0 and 5
large_array = np.random.randint(0, 6, size=1000)

# Count occurrences
large_counts = np.bincount(large_array)
print("Bin counts in large array:", large_counts)
```

This will give you a count of each integer from `0` to `5` in `large_array`.

### Practical Applications of `numpy.bincount`

1. **Counting and Frequencies**: Quickly get the frequency of each unique value in a dataset, such as counting occurrences in survey responses or other categorical data.

2. **Histograms for Non-negative Integers**: `bincount` can be used as an alternative to a histogram function for integer data, which is often more efficient than `numpy.histogram` for discrete values.

3. **Weighted Averages and Sums**: With the `weights` parameter, `bincount` can be used to calculate the weighted sum of occurrences, which can be useful in fields like finance or data analysis where different items carry different importance.

### Summary

The `numpy.bincount` function is a powerful tool for efficiently counting the occurrences of values in arrays of non-negative integers. With its support for weighted counts and minimum length, it can handle a variety of counting and summarization tasks in data analysis and statistics. Understanding how to leverage its features makes it a valuable function for data preprocessing and summarization.
                    """)
    
    case "flatten() Function":
        st.markdown("""
            
            The `flatten` function in NumPy is used to return a 1D array containing all the elements of a multi-dimensional array. It does so by converting the array into a single, contiguous 1D array, preserving the data order (row-wise in C-order by default).

### Syntax of `numpy.flatten`

```python
numpy.ndarray.flatten(order='C')
```

- **order**: Optional. It determines the order in which the array elements are read and flattened:
  - `'C'`: C-style row-major (default). This means elements are read row by row, i.e., flattening is done along the rows first, then columns.
  - `'F'`: Fortran-style column-major. This means elements are read column by column, i.e., flattening is done along the columns first, then rows.

### How `flatten` Works

- The `flatten` method returns a new 1D array that contains all the elements from the original multi-dimensional array, in the same order as they appear in memory (according to the specified order).
- It does **not** modify the original array; instead, it creates and returns a new array.

### Example 1: Basic Flattening

```python
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the 2D array to a 1D array
flattened_arr = arr.flatten()

print("Original Array:\n", arr)
print("Flattened Array:", flattened_arr)
```

**Output:**

```
Original Array:
 [[1 2 3]
  [4 5 6]]
Flattened Array: [1 2 3 4 5 6]
```

Explanation:
- The 2D array is converted to a 1D array by flattening all elements row by row (the default C-order).

### Example 2: Flattening with Fortran Order

```python
# Flatten the array with Fortran-style (column-major) order
flattened_arr_f = arr.flatten(order='F')

print("Flattened Array with Fortran order:", flattened_arr_f)
```

**Output:**

```
Flattened Array with Fortran order: [1 4 2 5 3 6]
```

Explanation:
- Here, the array is flattened column by column, rather than row by row.

### Example 3: Flattening a Higher Dimensional Array

```python
# Create a 3D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Flatten the 3D array
flattened_arr_3d = arr_3d.flatten()

print("Original 3D Array:\n", arr_3d)
print("Flattened 3D Array:", flattened_arr_3d)
```

**Output:**

```
Original 3D Array:
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
Flattened 3D Array: [1 2 3 4 5 6 7 8]
```

Explanation:
- The 3D array is flattened into a 1D array with all elements placed in row-major order by default.

### Example 4: Using `flatten` with Large Arrays

Flattening can be especially useful when you want to convert a large multi-dimensional array into a 1D array for easier processing, such as when working with machine learning datasets.

```python
# Create a 2D array of random integers
arr_large = np.random.randint(0, 10, size=(3, 4, 2))

# Flatten the 3D array
flattened_large_arr = arr_large.flatten()

print("Flattened Large Array:", flattened_large_arr)
```

### Example 5: In-Place Modification with `reshape`

Note that `flatten` does not modify the original array, but if you want to reshape the array in-place, you can use `reshape`.

```python
# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape the array to 1D (in-place modification)
arr_reshaped = arr.reshape(-1)

print("Reshaped Array:", arr_reshaped)
```

### Difference between `flatten` and `ravel`

- **`flatten`** returns a new 1D array and does not affect the original array.
- **`ravel`** also returns a 1D array, but if possible, it returns a view of the original array (not a copy), so changes to the result may affect the original array.

In general, use `flatten` when you need a guaranteed copy of the array, and use `ravel` when you want to avoid unnecessary memory usage and are fine with a view.

### Summary

- `flatten` is used to convert any multi-dimensional array into a 1D array.
- The default is row-major (`'C'`), but you can use column-major (`'F'`) for different memory orders.
- It is a very useful method when you need a single, contiguous 1D array from higher-dimensional data.     
                    
                    """)
    
    case "ravel() Function":
        st.markdown("""
            The `ravel` function in NumPy is similar to `flatten` but with a key difference: it returns a **view** of the original array whenever possible, rather than a new copy. This can save memory when working with large arrays. If the array cannot be viewed as a contiguous 1D array, `ravel` will return a flattened copy.

### Syntax of `numpy.ravel`

```python
numpy.ndarray.ravel(order='C')
```

- **order**: Optional. This specifies the order in which the array is read. It works the same way as in `flatten`:
  - `'C'`: C-style row-major order (default), meaning elements are read row by row.
  - `'F'`: Fortran-style column-major order, meaning elements are read column by column.

### How `ravel` Works

- `ravel` returns a 1D array that contains all the elements of the original multi-dimensional array.
- **Key difference from `flatten`**: `ravel` returns a **view** of the original array if possible. This means that modifying the result of `ravel` may also modify the original array.
- If a view is not possible (e.g., the original array is not contiguous in memory), `ravel` will return a new flattened copy of the array, just like `flatten`.

### Example 1: Basic Usage of `ravel`

```python
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array using ravel
raveled_arr = arr.ravel()

print("Original Array:\n", arr)
print("Raveled Array:", raveled_arr)
```

**Output:**

```
Original Array:
 [[1 2 3]
  [4 5 6]]
Raveled Array: [1 2 3 4 5 6]
```

Explanation:
- The 2D array `arr` is converted to a 1D array by `ravel`.

### Example 2: Ravel with Fortran Order

```python
# Flatten the array using Fortran-style order
raveled_arr_f = arr.ravel(order='F')

print("Raveled Array with Fortran order:", raveled_arr_f)
```

**Output:**

```
Raveled Array with Fortran order: [1 4 2 5 3 6]
```

Explanation:
- The array is flattened column by column, rather than row by row, as specified by the `'F'` order.

### Example 3: Modifying the Original Array through the View

If `ravel` returns a view of the original array, modifying the raveled array will also modify the original array.

```python
# Modify the raveled array
raveled_arr[0] = 99

print("Modified Raveled Array:", raveled_arr)
print("Original Array after modification:\n", arr)
```

**Output:**

```
Modified Raveled Array: [99  2  3  4  5  6]
Original Array after modification:
 [[99  2  3]
  [ 4  5  6]]
```

Explanation:
- The raveled array is a view of the original array, so modifying the raveled array also modifies the original array.

### Example 4: Using `ravel` with Non-contiguous Arrays

Sometimes, when working with advanced indexing or reshaping operations, the array may not be contiguous in memory. In such cases, `ravel` will return a copy of the array, ensuring that the result is contiguous.

```python
# Create a non-contiguous array using slicing
arr_non_contig = arr[:, ::2]

# Flatten using ravel
raveled_non_contig = arr_non_contig.ravel()

print("Non-contiguous array:", arr_non_contig)
print("Raveled (copy) of non-contiguous array:", raveled_non_contig)
```

**Output:**

```
Non-contiguous array: [[1 3]
 [4 6]]
Raveled (copy) of non-contiguous array: [1 3 4 6]
```

Explanation:
- The sliced array `arr[:, ::2]` is non-contiguous, so `ravel` returns a flattened copy.

### Key Differences between `ravel` and `flatten`

- **Return Type**:
  - `ravel`: Returns a **view** of the original array when possible, meaning modifications to the raveled array may affect the original array.
  - `flatten`: Always returns a new **copy** of the array, meaning the original array is not affected by modifications to the flattened array.

- **Memory Efficiency**:
  - `ravel` is more memory-efficient, as it attempts to return a view instead of a copy when possible.
  - `flatten` always creates a new array, which uses more memory.

- **In-Place Modifications**:
  - Since `ravel` may return a view, it can allow in-place modifications of the original array.
  - `flatten` creates a copy, so the original array remains unchanged.

### Summary

- `numpy.ravel` is used to convert a multi-dimensional array into a 1D array, and it returns a view of the original array if possible.
- It is memory-efficient since it avoids creating a copy of the data when it can return a view.
- Use `ravel` when you want to flatten an array without creating a new array if you don't need a separate copy.
- `flatten`, on the other hand, always returns a copy, making it safer if you need to preserve the original array's state.        
            
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


