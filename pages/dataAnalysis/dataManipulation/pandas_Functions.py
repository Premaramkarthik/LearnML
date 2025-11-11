import streamlit as st
import numpy as np
import pandas as pd 

if 'code' not in st.session_state:
    st.session_state.code = ''

st.title('Pandas Functions')
options = ['read_csv','loc and iloc','date_range','shape','describe', 'info','value_counts','unique and nunique','head and tail','set_index',
           'groupby','Grouper','Joins','reset_index','isnull','pivot','pivot table','drop','dropna','fillna','ffill and bfill','interpolate','plot']
select_option = st.selectbox('select the option', options)

match select_option:
    case 'read_csv':

        # Title
        st.title("Understanding `read_csv()` in Pandas")

        # Introduction
        st.header("What is `read_csv()`?")
        st.write("""
        The `read_csv()` function in Pandas is used to read CSV (Comma Separated Values) files and convert them into a DataFrame.
        It offers many parameters to handle different CSV formats and customize the way data is read from the file.
        """)

        # Syntax Section
        st.header("Syntax of `read_csv()`")
        st.write("""
        ```python
        pd.read_csv(filepath_or_buffer, sep=',', header='infer', index_col=None, dtype=None, encoding='utf-8', ...)
        ```

        **Key Parameters**:
        - `filepath_or_buffer`: Path to the CSV file or a URL.
        - `sep`: Delimiter that separates the values (default is a comma).
        - `header`: Row to use as the column names (default is the first row).
        - `index_col`: Column(s) to set as the index.
        - `usecols`: Specify which columns to read.
        - `dtype`: Type for each column.
        - `encoding`: Character encoding for the CSV file.
        """)

        # File Upload for User
        st.subheader("Upload Your CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            # Reading the CSV file into a DataFrame
            st.subheader("Preview of the CSV Data")
            df = pd.read_csv(uploaded_file)
            st.write(df)

            # Displaying Additional Details about the DataFrame
            st.subheader("Basic Information About the DataFrame")
            st.write("Shape of the DataFrame:", df.shape)
            st.write("Column Names:", df.columns)
            st.write("Data Types of Columns:", df.dtypes)

        # Example CSV Data
        st.subheader("Example CSV Data")
        example_data = """
        Name,Age,City
        Alice,25,New York
        Bob,30,Los Angeles
        Charlie,35,Chicago
        David,40,Miami
        """
        st.write("Here is a sample CSV data:")
        st.code(example_data, language="csv")

        # Parameters Section
        st.header("Understanding Key Parameters of `read_csv()`")
        st.write("""
        - **`sep`**: Defines the delimiter. For example, `sep='\t'` can be used for tab-separated values (TSV).
        - **`header`**: If the file does not have a header row, you can set `header=None` and manually define column names.
        - **`index_col`**: You can specify which column(s) should be used as the DataFrame index.
        - **`usecols`**: If you want to read only specific columns from a large file, pass a list of column names to `usecols`.
        - **`dtype`**: If you want to convert a column to a specific data type, you can use the `dtype` parameter.
        """)

        # Conclusion
        st.header("Key Points to Remember")
        st.write("""
        - `read_csv()` is essential for reading CSV files into a Pandas DataFrame.
        - Use `header` to control which row contains column names.
        - Use `index_col` to set a specific column as the index.
        - You can specify column types using `dtype` to optimize memory usage.
        - Explore the `usecols` and `skiprows` parameters to load specific parts of large files efficiently.
        """)

    case 'loc and iloc':
        
        # App Title
        st.title("Understanding Pandas: `loc` vs `iloc`")
        
        # Introduction Section
        st.header("Introduction to `loc` and `iloc`")
        st.write("""
        In Pandas, **`loc`** and **`iloc`** are used to access specific rows and columns in a DataFrame. 
        They are incredibly powerful tools for slicing and selecting data, but they have different use cases:
        - **`loc`**: Accesses data using **labels** (row or column names).
        - **`iloc`**: Accesses data using **integer positions** (row or column indices).

        Understanding their differences is crucial for working efficiently with Pandas.
        """)

        # `loc` Section
        st.header("What is `loc`?")
        st.write("""
        **`loc`** is label-based, meaning you use row and column **labels** to access data.
        - You can specify labels for rows, columns, or both.
        - It's inclusive, meaning it includes the endpoints of the specified range.
        """)

        # `loc` Syntax
        st.subheader("Syntax for `loc`")
        st.code("""
    # Accessing data using loc
    df.loc[row_label, column_label]
    """, language="python")

        # `loc` Example
        st.subheader("Example: Using `loc`")
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'Score': [85, 90, 95]
        }
        df = pd.DataFrame(data)
        st.write("Example DataFrame:")
        st.write(df)

        st.write("""
        To access the row where the Name is 'Bob' and the column 'Score' using `loc`:
        """)
        st.code("df.loc[1, 'Score']", language="python")
        st.write("Output:")
        st.write(df.loc[1, 'Score'])

        # `iloc` Section
        st.header("What is `iloc`?")
        st.write("""
        **`iloc`** is integer-location-based, meaning you use row and column **indices** to access data.
        - You can specify integer positions for rows, columns, or both.
        - It's zero-based indexing (the first row/column starts at index 0).
        """)

        # `iloc` Syntax
        st.subheader("Syntax for `iloc`")
        st.code("""
    # Accessing data using iloc
    df.iloc[row_index, column_index]
    """, language="python")

        # `iloc` Example
        st.subheader("Example: Using `iloc`")
        st.write("""
        To access the second row and the third column using `iloc`:
        """)
        st.code("df.iloc[1, 2]", language="python")
        st.write("Output:")
        st.write(df.iloc[1, 2])

        # Key Differences
        st.header("Key Differences Between `loc` and `iloc`")
        st.write("""
        Here’s a comparison to help you understand the differences:

        | Feature            | `loc`                           | `iloc`                     |
        |--------------------|----------------------------------|----------------------------|
        | **Type of Access** | Label-based (row/column names)  | Integer-based (indices)    |
        | **Indexing**       | Inclusive of end range          | Exclusive of end range     |
        | **Usage**          | More readable and user-friendly | Good for programmatic access |
        """)

        # Combined Example
        st.subheader("Combined Example: `loc` vs `iloc`")
        st.write("Using the same DataFrame as above, let's see the differences:")
        st.code("""
    # Using loc to access the 'Score' of 'Bob'
    df.loc[1, 'Score']

    # Using iloc to access the second row and third column
    df.iloc[1, 2]
    """, language="python")

        st.write("""
        - `loc[1, 'Score']` accesses the value using row and column **labels**.
        - `iloc[1, 2]` accesses the same value using row and column **positions**.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `loc` and `iloc`")
        st.write("""
        - Use **`loc`** when you know the **labels** of the rows or columns.
        - Use **`iloc`** when you're working with **positions** or indices.
        - Combine `loc` and `iloc` for complex operations in larger datasets.
        """)

        # Conclusion Section
        st.header("Conclusion")
        st.write("""
        - **`loc`** is intuitive and label-based, great for selecting rows or columns by name.
        - **`iloc`** is flexible and index-based, ideal for numerical indexing.
        Understanding and using both methods effectively will enhance your ability to work with data in Pandas.
        """)
    case 'date_range':
        import streamlit as st

        # App Title
        st.title("Understanding Pandas `date_range` Function")
        
        # Introduction Section
        st.header("Introduction to `date_range`")
        st.write("""
        The **`date_range`** function in Pandas is used to generate a sequence of dates or timestamps. 
        This is particularly useful for creating time series data or performing operations that involve dates.

        **Key Features**:
        - Flexible date generation with customizable frequency.
        - Ability to specify start, end, and periods.
        - Supports a wide range of frequencies such as daily, hourly, or even minute-level intervals.
        """)

        # Syntax Section
        st.header("Syntax of `date_range`")
        st.code("""
    pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None)
    """, language="python")

        st.write("""
        **Key Parameters**:
        - `start`: The starting date of the range.
        - `end`: The ending date of the range.
        - `periods`: Number of time periods to generate.
        - `freq`: Frequency string (e.g., 'D' for days, 'H' for hours).
        - `tz`: Time zone for the generated dates.
        - `normalize`: Normalize start and end dates to midnight.
        - `closed`: Specifies if the interval is closed on 'left', 'right', or both sides.
        """)

        # Example 1
        st.header("Example 1: Generating a Daily Date Range")
        st.write("Generate a range of dates from January 1, 2024, to January 7, 2024:")
        st.code("""
    pd.date_range(start='2024-01-01', end='2024-01-07')
    """, language="python")

        example_1 = pd.date_range(start='2024-01-01', end='2024-01-07')
        st.write("Output:")
        st.write(example_1)

        # Example 2
        st.header("Example 2: Generating a Custom Frequency Date Range")
        st.write("Generate a range of dates with an hourly frequency:")
        st.code("""
    pd.date_range(start='2024-01-01 00:00', end='2024-01-01 23:00', freq='H')
    """, language="python")

        example_2 = pd.date_range(start='2024-01-01 00:00', end='2024-01-01 23:00', freq='H')
        st.write("Output:")
        st.write(example_2)

        # Example 3
        st.header("Example 3: Specifying Number of Periods")
        st.write("Generate 5 dates starting from January 1, 2024, with a weekly frequency:")
        st.code("""
    pd.date_range(start='2024-01-01', periods=5, freq='W')
    """, language="python")

        example_3 = pd.date_range(start='2024-01-01', periods=5, freq='W')
        st.write("Output:")
        st.write(example_3)

        # Frequencies Section
        st.header("Common Frequencies in `date_range`")
        st.write("""
        Pandas `date_range` supports various frequencies for generating date ranges:
        - **'D'**: Daily (default).
        - **'H'**: Hourly.
        - **'T' or 'min'**: Minute.
        - **'S'**: Second.
        - **'W'**: Weekly.
        - **'M'**: Month-end.
        - **'Q'**: Quarter-end.
        - **'A'**: Year-end.
        """)

        # Practical Tips Section
        st.header("Practical Tips for Using `date_range`")
        st.write("""
        - Use **`start`** and **`end`** to define a fixed range.
        - Use **`periods`** to generate a specific number of timestamps.
        - Combine **`freq`** with offsets for custom intervals (e.g., '2D' for every 2 days).
        - Use **`tz`** to handle time zones effectively.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        The `date_range` function is a versatile tool for generating sequences of dates or timestamps. 
        It is especially useful in time series analysis and date-related operations. Experiment with different 
        parameters and frequencies to create the ranges that suit your needs!
        """)

    case 'shape':
        # App Title
        st.title("Understanding Pandas `shape` Attribute")

        # Introduction
        st.header("What is the `shape` Attribute?")
        st.write("""
        The **`shape`** attribute in Pandas is used to determine the dimensions of a DataFrame or Series. 
        It returns a tuple representing:
        - The **number of rows**.
        - The **number of columns** (for DataFrames).

        This is an essential tool for quickly understanding the structure of your dataset and is frequently used in data analysis workflows.
        """)

        # Syntax Section
        st.header("Syntax of `shape`")
        st.code("""
    # Syntax
    df.shape
    """, language="python")

        st.write("""
        The `shape` attribute is straightforward:
        - It does **not require parentheses** (unlike a function).
        - It returns a tuple `(rows, columns)`.
        """)

        # Example 1: Basic Example
        st.header("Example 1: Using `shape` with a DataFrame")
        st.write("Consider the following DataFrame:")

        # Sample DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        df = pd.DataFrame(data)
        st.write(df)

        st.write("To find the shape of the DataFrame:")
        st.code("df.shape", language="python")
        st.write("Output:")
        st.write(df.shape)  # Display shape as (4, 3)

        st.write("""
        - **4**: Number of rows.
        - **3**: Number of columns.
        """)

        # Example 2: Using `shape` with a Series
        st.header("Example 2: Using `shape` with a Series")
        st.write("Consider the following Series (a single column of data):")

        # Sample Series
        series = pd.Series([1, 2, 3, 4, 5], name="Numbers")
        st.write(series)

        st.write("To find the shape of the Series:")
        st.code("series.shape", language="python")
        st.write("Output:")
        st.write(series.shape)  # Display shape as (5,)

        st.write("""
        - **5**: The number of rows in the Series.
        - A Series has no columns, so it only returns the number of rows.
        """)

        # Use Cases
        st.header("Use Cases of `shape`")
        st.write("""
        The `shape` attribute is widely used in:
        - **Data Exploration**: Quickly checking the size of your dataset.
        - **Data Validation**: Ensuring your data has the expected dimensions.
        - **Debugging**: Identifying if operations (like filtering) have altered the dataset's size.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `shape`")
        st.write("""
        - Always check the shape of your dataset after loading it to ensure data was loaded correctly.
        - Combine `shape` with filtering or transformations to monitor changes in rows and columns.
        - Remember that `shape` works with both DataFrames and Series, but for Series, only the row count is returned.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        The `shape` attribute is a simple yet powerful tool in Pandas for understanding the structure of your data.
        It helps you quickly assess the size of your dataset and verify transformations or operations during analysis.
        """)

    case 'describe' :
    
        # App Title
        st.title("Understanding the `describe()` Function in Pandas")

        # Introduction
        st.header("What is the `describe()` Function?")
        st.write("""
        The **`describe()`** function in Pandas provides a summary of statistics for numerical or categorical data in a DataFrame or Series.
        It's a powerful tool for exploratory data analysis (EDA), giving a quick overview of the dataset.
        """)

        # Syntax Section
        st.header("Syntax of `describe()`")
        st.code("""
    df.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
    """, language="python")

        st.write("""
        **Parameters**:
        - `percentiles`: List of percentiles to include in the output (default: `[0.25, 0.5, 0.75]`).
        - `include`: Data types to include in the summary (e.g., `'all'`, `[np.number]`, `[np.object]`).
        - `exclude`: Data types to exclude from the summary.
        - `datetime_is_numeric`: Treat datetime values as numeric (default: `False`).
        """)

        # Basic Example
        st.header("Basic Example of `describe()`")
        st.write("Consider the following DataFrame:")

        # Sample DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'Score': [85.5, 90.0, 95.0, 88.0],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        df = pd.DataFrame(data)
        st.write(df)

        st.write("Using `df.describe()` on the numerical columns:")
        st.code("df.describe()", language="python")
        st.write(df.describe())

        st.write("""
        **Output Explanation**:
        - `count`: Number of non-missing values.
        - `mean`: Arithmetic mean of the values.
        - `std`: Standard deviation, a measure of variability.
        - `min`: Minimum value.
        - `25%`: 25th percentile (lower quartile).
        - `50%`: 50th percentile (median).
        - `75%`: 75th percentile (upper quartile).
        - `max`: Maximum value.
        """)

        # Describe for Categorical Data
        st.header("Using `describe()` for Categorical Data")
        st.write("Using `describe(include=['object'])` on categorical columns:")
        st.code("df.describe(include=['object'])", language="python")
        st.write(df.describe(include=['object']))

        st.write("""
        **Output Explanation**:
        - `count`: Number of non-missing values.
        - `unique`: Number of unique values.
        - `top`: Most frequent value.
        - `freq`: Frequency of the most frequent value.
        """)

        # Custom Percentiles
        st.header("Customizing Percentiles")
        st.write("You can specify custom percentiles using the `percentiles` parameter:")
        st.code("df.describe(percentiles=[0.1, 0.9])", language="python")
        st.write(df.describe(percentiles=[0.1, 0.9]))

        # Including All Columns
        st.header("Including All Columns in the Summary")
        st.write("Use `include='all'` to include all columns (numerical, categorical, etc.) in the summary:")
        st.code("df.describe(include='all')", language="python")
        st.write(df.describe(include='all'))

        # Excluding Specific Data Types
        st.header("Excluding Specific Data Types")
        st.write("Use `exclude` to exclude specific data types. For example, to exclude numerical data:")
        st.code("df.describe(exclude=[int, float])", language="python")
        st.write(df.describe(exclude=[int, float]))

        # Practical Tips
        st.header("Practical Tips for Using `describe()`")
        st.write("""
        - Use `describe()` as an initial step in EDA to get an overview of the data distribution.
        - Customize percentiles to gain more insight into data spread (e.g., deciles).
        - Include or exclude specific data types to focus on relevant columns.
        - For time-based data, use `datetime_is_numeric=True` to get meaningful statistics.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        The `describe()` function is a versatile and powerful tool for summarizing data in Pandas. 
        By customizing its parameters, you can derive meaningful insights quickly and efficiently during your analysis.
        """)
        
    case 'info':

        # App Title
        st.title("Understanding the `info()` Function in Pandas")

        # Introduction
        st.header("What is the `info()` Function?")
        st.write("""
        The **`info()`** function in Pandas provides a concise summary of a DataFrame, including:
        - The number of non-null values in each column.
        - The data type of each column.
        - Memory usage of the DataFrame.
        
        It's a crucial function for understanding the structure of your dataset during the initial stages of analysis.
        """)

        # Syntax Section
        st.header("Syntax of `info()`")
        st.code("""
    df.info(verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)
    """, language="python")

        st.write("""
        **Parameters**:
        - `verbose`: Whether to print the full summary (`True`) or just the column count (`False`).
        - `buf`: A writable buffer to send the output (e.g., a file).
        - `max_cols`: Maximum number of columns to show in the summary (default is `20`).
        - `memory_usage`: Controls memory usage display. Can be `True`, `False`, or `'deep'` for detailed memory usage.
        - `null_counts`: Whether to display non-null counts (default is `True`).

        **Note**: Some parameters are deprecated in recent versions of Pandas. Always check the documentation for your version.
        """)

        # Basic Example
        st.header("Basic Example of `info()`")
        st.write("Consider the following DataFrame:")

        # Sample DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
            'Age': [25, 30, 35, 40, 45],
            'Score': [85.5, 90.0, None, 88.0, 92.0],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Austin']
        }
        df = pd.DataFrame(data)
        st.write(df)

        st.write("Using `df.info()` provides the following summary:")
        st.code("df.info()", language="python")
        # Capture the output of info() as a string
        import io
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_output = buffer.getvalue()
        st.text(info_output)

        st.write("""
        **Output Explanation**:
        - `#`: Index number of the column.
        - `Column`: Name of the column.
        - `Non-Null Count`: Number of non-missing values in the column.
        - `Dtype`: Data type of the column (e.g., `int64`, `float64`, `object`).
        - `memory usage`: Approximate memory usage of the DataFrame.
        """)

        # Use Cases
        st.header("Use Cases of `info()`")
        st.write("""
        - Quickly identify columns with missing values.
        - Check the data types of columns to ensure correctness.
        - Estimate the memory usage of a DataFrame, especially for large datasets.
        """)

        # Parameters in Action
        st.header("Customizing `info()`")
        st.write("### Controlling Verbosity:")
        st.write("Set `verbose=False` to limit the output to just the column count:")
        st.code("df.info(verbose=False)", language="python")

        st.write("### Controlling Memory Usage:")
        st.write("Set `memory_usage='deep'` to display detailed memory usage:")
        st.code("df.info(memory_usage='deep')", language="python")

        st.write("""
        **Example**:
        """)
        buffer = io.StringIO()
        df.info(buf=buffer, memory_usage='deep')
        st.text(buffer.getvalue())

        # Practical Tips
        st.header("Practical Tips for Using `info()`")
        st.write("""
        - Use `info()` immediately after loading your dataset to understand its structure.
        - Combine `info()` with `.isnull()` to explore missing values in detail.
        - For large datasets, control verbosity and memory usage to avoid overwhelming output.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        The `info()` function is an essential tool in Pandas for gaining a quick overview of your DataFrame's structure and memory usage.
        It's a vital step in understanding your data and preparing it for further analysis.
        """)

    case 'value_counts':

        # Title
        st.title("Understanding `value_counts()` in Pandas")

        # Introduction
        st.header("What is `value_counts()`?")
        st.write("""
        The `value_counts()` function in Pandas is a powerful tool used to count the occurrences of unique values in a Series or a specific column of a DataFrame. 
        It helps you understand the frequency distribution of your data.
        
        **Key Features**:
        - Counts the occurrences of each unique value.
        - Returns the result in descending order by default.
        - Useful for analyzing categorical data or identifying value distribution.
        """)

        # Syntax Explanation
        st.subheader("Syntax")
        st.code("""
    Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
    """, language="python")

        st.write("""
        **Parameters**:
        - `normalize`: If `True`, the output will be the relative frequency instead of absolute counts.
        - `sort`: If `True` (default), sorts the results in descending order.
        - `ascending`: If `True`, sorts the results in ascending order.
        - `bins`: Groups numerical data into equal-sized bins.
        - `dropna`: If `True`, excludes `NaN` values from the result.

        **Returns**: A Series containing counts of unique values as values and the unique values as the index.
        """)

        # Example Data
        st.header("Examples of `value_counts()`")
        st.write("Let's see `value_counts()` in action with the following example:")

        # Sample Data
        data = ['Apple', 'Banana', 'Apple', 'Orange', 'Banana', 'Banana', 'Apple', 'Orange', 'Apple', 'Apple']
        series = pd.Series(data)
        st.write("Series:")
        st.write(series)

        # Applying value_counts()
        st.subheader("Example 1: Basic Usage")
        st.write("Using `value_counts()` to count the occurrences of unique values:")
        st.code("series.value_counts()", language="python")
        st.write(series.value_counts())

        st.write("""
        **Explanation**:
        - `Apple`: Appears 5 times.
        - `Banana`: Appears 3 times.
        - `Orange`: Appears 2 times.
        """)

        # Normalized value counts
        st.subheader("Example 2: Normalized Values")
        st.write("You can use the `normalize=True` parameter to get relative frequencies:")
        st.code("series.value_counts(normalize=True)", language="python")
        st.write(series.value_counts(normalize=True))

        st.write("""
        **Explanation**:
        - Normalized values represent the proportion of each unique value in the Series.
        """)

        # Binned value counts
        st.subheader("Example 3: Binned Data")
        st.write("For numerical data, `bins` can group values into intervals. Consider the following Series:")
        numerical_data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])
        st.write(numerical_data)

        st.write("Using `value_counts()` with bins:")
        st.code("numerical_data.value_counts(bins=3)", language="python")
        st.write(numerical_data.value_counts(bins=3))

        st.write("""
        **Explanation**:
        - The values are grouped into three intervals (bins).
        - Counts represent the number of values in each bin.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `value_counts()`")
        st.write("""
        - Use it to analyze the distribution of categorical data, such as survey responses or product categories.
        - Combine it with normalization to get percentage distributions.
        - Apply `bins` for numerical data to group values into meaningful intervals.
        """)

        # Conclusion
        st.header("Conclusion")
        st.write("""
        The `value_counts()` function is an essential tool in Pandas for exploring and analyzing data distributions. 
        Its versatility allows you to count occurrences, calculate proportions, and group numerical data into intervals, making it invaluable for data analysis tasks.
        """)

    case 'unique()` and `nunique()':

        # Title
        st.title("Understanding `unique()` and `nunique()` in Pandas")

        # Introduction
        st.header("Overview of `unique()` and `nunique()`")
        st.write("""
        Pandas provides two powerful functions, `unique()` and `nunique()`, to analyze the distinct values in a Series or DataFrame column.

        - **`unique()`**: Returns an array of unique values from a Series or column.
        - **`nunique()`**: Returns the count of unique values (optionally including or excluding NaN values).

        These functions are essential for understanding the diversity of your data, especially in categorical columns.
        """)

        # Explanation for unique()
        st.header("`unique()` Function")
        st.write("""
        The `unique()` function extracts all the distinct values in a Series or column. It helps to identify what values exist in your dataset.

        **Syntax**:
        ```python
        Series.unique()
        ```

        **Returns**: A NumPy array of unique values.
        """)

        # Example for unique()
        st.subheader("Example: Using `unique()`")
        example_data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'grape', 'apple'])
        st.write("Sample Series:")
        st.write(example_data)

        st.write("Unique values in the Series:")
        st.code("example_data.unique()", language="python")
        st.write(example_data.unique())

        st.write("""
        **Explanation**:
        - The output is an array of all unique values: `['apple', 'banana', 'orange', 'grape']`.
        """)

        # Explanation for nunique()
        st.header("`nunique()` Function")
        st.write("""
        The `nunique()` function counts the number of unique values in a Series or DataFrame column. 
        It includes an optional parameter to decide whether to count `NaN` values or not.

        **Syntax**:
        ```python
        Series.nunique(dropna=True)
        ```

        **Parameters**:
        - `dropna`: If `True` (default), excludes `NaN` from the count. If `False`, includes `NaN`.

        **Returns**: An integer count of unique values.
        """)

        # Example for nunique()
        st.subheader("Example: Using `nunique()`")
        example_data_with_nan = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'grape', None])
        st.write("Sample Series with NaN values:")
        st.write(example_data_with_nan)

        st.write("Count of unique values (excluding NaN):")
        st.code("example_data_with_nan.nunique()", language="python")
        st.write(example_data_with_nan.nunique())

        st.write("Count of unique values (including NaN):")
        st.code("example_data_with_nan.nunique(dropna=False)", language="python")
        st.write(example_data_with_nan.nunique(dropna=False))

        st.write("""
        **Explanation**:
        - Excluding `NaN`: 4 unique values (`'apple'`, `'banana'`, `'orange'`, `'grape'`).
        - Including `NaN`: 5 unique values.
        """)

        # Comparison
        st.header("Key Differences Between `unique()` and `nunique()`")
        st.write("""
        - **Output Type**:
        - `unique()`: Returns an array of values.
        - `nunique()`: Returns a single integer (count of unique values).
        - **Handling NaN**:
        - `unique()`: Always includes `NaN` in the output.
        - `nunique()`: Can include or exclude `NaN` based on the `dropna` parameter.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `unique()` and `nunique()`")
        st.write("""
        - Use `unique()` to get a list of all distinct values for understanding the range of a variable.
        - Use `nunique()` when you need a quick count of unique values, such as for summarizing data.
        - Combine `unique()` or `nunique()` with filtering to explore subsets of your data.
        """)
    case 'head()` and `tail()':

        # Title
        st.title("Understanding `head()` and `tail()` in Pandas")

        # Introduction
        st.header("Overview of `head()` and `tail()`")
        st.write("""
        The `head()` and `tail()` functions in Pandas are used to quickly inspect rows of a DataFrame or Series.

        - **`head()`**: Displays the first n rows of a DataFrame or Series (default is 5 rows).
        - **`tail()`**: Displays the last n rows of a DataFrame or Series (default is 5 rows).

        These functions are particularly useful for previewing or summarizing data during exploration and debugging.
        """)

        # Explanation for head()
        st.header("`head()` Function")
        st.write("""
        The `head()` function retrieves the first n rows from a DataFrame or Series.

        **Syntax**:
        ```python
        DataFrame.head(n=5)
        Series.head(n=5)
        ```

        **Parameters**:
        - `n` (optional): Number of rows to return. Default is 5.

        **Returns**: A subset of the DataFrame or Series containing the first n rows.
        """)

        # Example for head()
        st.subheader("Example: Using `head()`")
        sample_data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
            'Age': [25, 30, 35, 40, 45, 50, 55],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio']
        })

        st.write("Sample DataFrame:")
        st.write(sample_data)

        st.write("Using `head()` (default 5 rows):")
        st.code("sample_data.head()", language="python")
        st.write(sample_data.head())

        st.write("Using `head(n=3)` (first 3 rows):")
        st.code("sample_data.head(3)", language="python")
        st.write(sample_data.head(3))

        # Explanation for tail()
        st.header("`tail()` Function")
        st.write("""
        The `tail()` function retrieves the last n rows from a DataFrame or Series.

        **Syntax**:
        ```python
        DataFrame.tail(n=5)
        Series.tail(n=5)
        ```

        **Parameters**:
        - `n` (optional): Number of rows to return. Default is 5.

        **Returns**: A subset of the DataFrame or Series containing the last n rows.
        """)

        # Example for tail()
        st.subheader("Example: Using `tail()`")
        st.write("Using `tail()` (default 5 rows):")
        st.code("sample_data.tail()", language="python")
        st.write(sample_data.tail())

        st.write("Using `tail(n=3)` (last 3 rows):")
        st.code("sample_data.tail(3)", language="python")
        st.write(sample_data.tail(3))

        # Practical Tips
        st.header("Practical Tips for Using `head()` and `tail()`")
        st.write("""
        - Use `head()` to inspect the start of your dataset and ensure data is loaded correctly.
        - Use `tail()` to check the end of your dataset, especially for time-series data.
        - Customize the `n` parameter to view a specific number of rows.
        - Combine with other methods for comprehensive data exploration (e.g., `.info()`, `.describe()`).
        """)
    case 'set_index':
        # Title
        st.title("Understanding `set_index()` in Pandas")

        # Introduction
        st.header("Overview of `set_index()`")
        st.write("""
        The `set_index()` function in Pandas is used to set one or more columns of a DataFrame as its index. 
        This is useful for reorganizing and accessing your data more efficiently.

        **Key Points**:
        - It allows you to define a specific column(s) as the row index.
        - You can choose to drop or retain the original column after setting it as the index.
        - Can handle single or multi-level indexes.

        **Why use `set_index()`?**
        - To optimize data access and organization.
        - To handle time-series data, where dates or timestamps are often set as the index.
        """)

        # Syntax
        st.header("Syntax of `set_index()`")
        st.write("""
        ```python
        DataFrame.set_index(keys, drop=True, inplace=False)
        ```

        **Parameters**:
        - `keys`: Column name(s) to set as the index. Can be a single column name or a list for multiple columns.
        - `drop`: If `True` (default), removes the column(s) being set as the index from the DataFrame.
        - `inplace`: If `True`, modifies the DataFrame in place. Default is `False`.

        **Returns**: A new DataFrame with the specified column(s) set as the index if `inplace=False`.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        sample_data = pd.DataFrame({
            'ID': [1, 2, 3, 4, 5],
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Age': [25, 30, 35, 40, 45],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
        })
        st.write("Sample DataFrame:")
        st.write(sample_data)

        # Example for setting a single column as index
        st.subheader("Setting a Single Column as Index")
        st.write("""
        Let's set the 'ID' column as the index of the DataFrame using `set_index()`:
        """)
        st.code("sample_data.set_index('ID')", language="python")
        single_index_df = sample_data.set_index('ID')
        st.write(single_index_df)

        st.write("""
        **Explanation**:
        - The 'ID' column is now the index of the DataFrame.
        - By default, the original 'ID' column is removed.
        """)

        # Example for setting multiple columns as index
        st.subheader("Setting Multiple Columns as Index")
        st.write("""
        You can also set multiple columns as a multi-level index. For example, setting 'City' and 'Name' as the index:
        """)
        st.code("sample_data.set_index(['City', 'Name'])", language="python")
        multi_index_df = sample_data.set_index(['City', 'Name'])
        st.write(multi_index_df)

        st.write("""
        **Explanation**:
        - The DataFrame now has a hierarchical index with 'City' as the primary index and 'Name' as the secondary index.
        """)

        # Example for keeping the original column
        st.subheader("Retaining the Original Column")
        st.write("""
        To keep the original column after setting it as the index, set the `drop` parameter to `False`:
        """)
        st.code("sample_data.set_index('ID', drop=False)", language="python")
        retained_column_df = sample_data.set_index('ID', drop=False)
        st.write(retained_column_df)

        st.write("""
        **Explanation**:
        - The 'ID' column is retained in the DataFrame while also being set as the index.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `set_index()`")
        st.write("""
        - Use `set_index()` for time-series data to set date or time columns as the index for easier analysis.
        - For hierarchical data, use multiple columns as a multi-level index.
        - Remember to set `inplace=True` if you want to modify the DataFrame directly.
        - Combine with `.reset_index()` to revert to the default index if needed.
        """)
    case 'groupby':

        # Title
        st.title("Understanding `groupby()` in Pandas")

        # Introduction
        st.header("Overview of `groupby()`")
        st.write("""
        The `groupby()` function in Pandas is a powerful tool for grouping and aggregating data. 
        It allows you to group your dataset by one or more columns and perform operations like summing, averaging, or counting.

        **Key Points**:
        - Groups data by a specific column or set of columns.
        - Aggregates or transforms grouped data using a variety of functions.
        - Essential for data analysis tasks, especially when summarizing or reshaping data.

        **Why use `groupby()`?**
        - To summarize data by categories (e.g., average sales by region, total revenue by product).
        - To split a dataset into groups and apply a function to each group.
        """)

        # Syntax
        st.header("Syntax of `groupby()`")
        st.write("""
        ```python
        DataFrame.groupby(by, axis=0, as_index=True, dropna=True)
        ```

        **Parameters**:
        - `by`: Column name(s) or a function to group by.
        - `axis`: Defaults to 0 (group rows). Use 1 to group columns.
        - `as_index`: If `True`, the grouping columns are used as the index of the result. Defaults to `True`.
        - `dropna`: Excludes NA/null values from group keys. Defaults to `True`.

        **Returns**: A GroupBy object, which can be further processed using aggregation functions like `sum()`, `mean()`, `count()`, etc.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        sample_data = pd.DataFrame({
            'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing'],
            'Product': ['Laptop', 'Smartphone', 'Chair', 'Table', 'Shirt', 'Pants'],
            'Sales': [1200, 800, 300, 450, 150, 200],
            'Region': ['North', 'South', 'North', 'South', 'North', 'South']
        })
        st.write("Sample DataFrame:")
        st.write(sample_data)

        # Grouping by a single column
        st.subheader("Grouping by a Single Column")
        st.write("""
        Let's group the data by the `Category` column and calculate the total sales for each category:
        """)
        st.code("sample_data.groupby('Category')['Sales'].sum()", language="python")
        group_single = sample_data.groupby('Category')['Sales'].sum()
        st.write(group_single)

        st.write("""
        **Explanation**:
        - The data is grouped by the `Category` column.
        - The `sum()` function calculates the total sales for each category.
        """)

        # Grouping by multiple columns
        st.subheader("Grouping by Multiple Columns")
        st.write("""
        You can also group data by multiple columns. For example, grouping by `Category` and `Region` to calculate total sales:
        """)
        st.code("sample_data.groupby(['Category', 'Region'])['Sales'].sum()", language="python")
        group_multi = sample_data.groupby(['Category', 'Region'])['Sales'].sum()
        st.write(group_multi)

        st.write("""
        **Explanation**:
        - The data is grouped by both `Category` and `Region`.
        - The `sum()` function calculates the total sales for each combination of `Category` and `Region`.
        """)

        # Grouping and using mean()
        st.subheader("Using Aggregation Functions")
        st.write("""
        The `groupby()` function supports various aggregation functions such as `mean()`, `count()`, and `max()`.

        For example, calculating the average sales for each category:
        """)
        st.code("sample_data.groupby('Category')['Sales'].mean()", language="python")
        group_mean = sample_data.groupby('Category')['Sales'].mean()
        st.write(group_mean)

        # Practical Tips
        st.header("Practical Tips for Using `groupby()`")
        st.write("""
        - Combine `groupby()` with aggregation functions like `sum()`, `mean()`, and `count()` for efficient summarization.
        - Use the `reset_index()` function after grouping if you want to convert the grouping columns back into regular columns.
        - Explore advanced functions like `apply()` or custom aggregation functions for more complex operations.
        - Experiment with the `as_index` parameter to control whether the grouped keys are set as an index.
        """)

    case 'Grouper':
        
        # Title
        st.title("Understanding `pd.Grouper()` in Pandas")

        # Introduction
        st.header("Overview of `pd.Grouper()`")
        st.write("""
        The `pd.Grouper()` function in Pandas is a flexible and powerful way to group data when working with time series or other data that requires custom grouping.

        **Key Features**:
        - Simplifies grouping of time series data by custom time intervals (e.g., monthly, weekly, yearly).
        - Provides flexibility in grouping by specific columns or indices.
        - Works seamlessly with the `groupby()` function.

        **Why use `pd.Grouper()`?**
        - When you need to group data by time intervals in a DateTime index or column.
        - To perform aggregations like sum, mean, or count on grouped data.
        """)

        # Syntax
        st.header("Syntax of `pd.Grouper()`")
        st.write("""
        ```python
        pd.Grouper(key=None, level=None, freq=None, axis=0, sort=False)
        ```

        **Parameters**:
        - `key`: The column name to group by (used when grouping by a DataFrame column).
        - `level`: The level to group by (used when grouping by an index).
        - `freq`: Frequency string (e.g., 'D' for daily, 'M' for monthly, 'Y' for yearly).
        - `axis`: Axis to group (default is 0, rows).
        - `sort`: Whether to sort the result. Defaults to `False`.

        **Returns**: A GroupBy object for further aggregation or transformation.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        sample_data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
            'Category': ['A', 'B'] * 6,
            'Sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
        })
        st.write("Sample DataFrame:")
        st.write(sample_data)

        # Grouping by Monthly Frequency
        st.subheader("Grouping by Monthly Frequency")
        st.write("""
        Let's group the data by the `Date` column using monthly frequency and calculate the total sales:
        """)
        st.code("""
    grouped_data = sample_data.groupby(pd.Grouper(key='Date', freq='M'))['Sales'].sum()
        """, language="python")
        grouped_monthly = sample_data.groupby(pd.Grouper(key='Date', freq='M'))['Sales'].sum()
        st.write(grouped_monthly)

        st.write("""
        **Explanation**:
        - The `pd.Grouper()` function specifies that the `Date` column should be grouped by monthly frequency (`freq='M'`).
        - The `groupby()` function applies this grouping, and the `sum()` function calculates total sales for each month.
        """)

        # Grouping by Yearly Frequency
        st.subheader("Grouping by Yearly Frequency")
        st.write("""
        You can also group data by yearly frequency. For example:
        """)
        st.code("""
    grouped_data = sample_data.groupby(pd.Grouper(key='Date', freq='Y'))['Sales'].sum()
        """, language="python")
        grouped_yearly = sample_data.groupby(pd.Grouper(key='Date', freq='Y'))['Sales'].sum()
        st.write(grouped_yearly)

        st.write("""
        **Explanation**:
        - The `freq='Y'` parameter specifies yearly frequency.
        - The result shows total sales grouped by year.
        """)

        # Grouping by Category and Monthly Frequency
        st.subheader("Grouping by Multiple Keys")
        st.write("""
        You can combine `pd.Grouper()` with other grouping keys. For instance, grouping by `Category` and monthly frequency:
        """)
        st.code("""
    grouped_data = sample_data.groupby(['Category', pd.Grouper(key='Date', freq='M')])['Sales'].sum()
        """, language="python")
        grouped_multi = sample_data.groupby(['Category', pd.Grouper(key='Date', freq='M')])['Sales'].sum()
        st.write(grouped_multi)

        st.write("""
        **Explanation**:
        - The data is grouped by both `Category` and `Date` (monthly frequency).
        - The `sum()` function calculates total sales for each combination of `Category` and month.
        """)

        # Practical Tips
        st.header("Practical Tips for Using `pd.Grouper()`")
        st.write("""
        - Use `pd.Grouper()` for time-based grouping to avoid manual date handling.
        - Combine `pd.Grouper()` with other grouping keys for more complex groupings.
        - Experiment with different frequencies (`freq`) like:
        - `'D'` for daily
        - `'W'` for weekly
        - `'Q'` for quarterly
        - Always ensure the column or index being grouped is in DateTime format.
        """)

    case 'merge':

        # Title
        st.title("Understanding `merge` in Pandas")

        # Introduction
        st.header("Overview of `merge`")
        st.write("""
        The `merge()` function in Pandas is used to combine two DataFrames based on common columns or indices.
        It is highly customizable, allowing you to specify how to join the data.

        **Key Features**:
        - Combines data from multiple DataFrames.
        - Supports various types of joins like inner, outer, left, and right.
        - Can handle complex joining conditions with custom keys.
        """)

        # Syntax
        st.header("Syntax of `merge()`")
        st.write("""
        ```python
        pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, 
                left_index=False, right_index=False, sort=False)
        ```

        **Parameters**:
        - `left`, `right`: DataFrames to merge.
        - `how`: Type of merge to perform (`'inner'`, `'outer'`, `'left'`, `'right'`). Default is `'inner'`.
        - `on`: Column(s) to join on. Must be present in both DataFrames.
        - `left_on`, `right_on`: Columns to join on for `left` and `right` DataFrames, respectively.
        - `left_index`, `right_index`: Use index for merging if set to `True`.
        - `sort`: Whether to sort the result. Default is `False`.

        **Returns**: A merged DataFrame.
        """)

        # Types of Joins
        st.header("Types of Joins")
        st.write("""
        1. **Inner Join**: Returns rows with matching values in both DataFrames.
        2. **Outer Join**: Returns all rows from both DataFrames, with `NaN` where no match is found.
        3. **Left Join**: Returns all rows from the left DataFrame, with matching rows from the right DataFrame.
        4. **Right Join**: Returns all rows from the right DataFrame, with matching rows from the left DataFrame.
        """)

        # Example DataFrames
        st.subheader("Example DataFrames")
        left_df = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40]
        })
        right_df = pd.DataFrame({
            'ID': [3, 4, 5, 6],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
            'Salary': [70000, 80000, 90000, 100000]
        })

        st.write("Left DataFrame:")
        st.write(left_df)
        st.write("Right DataFrame:")
        st.write(right_df)

        # Inner Join
        st.subheader("1. Inner Join")
        st.write("""
        **Definition**: Returns rows with matching values in both DataFrames.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='inner', on='ID')
        """, language="python")
        inner_result = pd.merge(left_df, right_df, how='inner', on='ID')
        st.write(inner_result)

        # Outer Join
        st.subheader("2. Outer Join")
        st.write("""
        **Definition**: Returns all rows from both DataFrames, filling missing matches with `NaN`.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='outer', on='ID')
        """, language="python")
        outer_result = pd.merge(left_df, right_df, how='outer', on='ID')
        st.write(outer_result)

        # Left Join
        st.subheader("3. Left Join")
        st.write("""
        **Definition**: Returns all rows from the left DataFrame, with matching rows from the right DataFrame.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='left', on='ID')
        """, language="python")
        left_result = pd.merge(left_df, right_df, how='left', on='ID')
        st.write(left_result)

        # Right Join
        st.subheader("4. Right Join")
        st.write("""
        **Definition**: Returns all rows from the right DataFrame, with matching rows from the left DataFrame.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='right', on='ID')
        """, language="python")
        right_result = pd.merge(left_df, right_df, how='right', on='ID')
        st.write(right_result)

        # Tips for Using `merge`
        st.header("Practical Tips for Using `merge()`")
        st.write("""
        - Ensure the column(s) used for merging exist in both DataFrames.
        - Use `on` for common column names or `left_on` and `right_on` for different column names.
        - Set `left_index` or `right_index` to `True` if you want to merge on indices.
        - Use `how` parameter to control the type of join based on your use case.
        """)

    case 'Joins':
        # Title
        st.title("Understanding Joins in Pandas")

        # Introduction
        st.header("What are Joins?")
        st.write("""
        Joins in Pandas are used to combine two DataFrames based on common columns or indices. 
        They allow you to merge data flexibly depending on your requirements.

        **Key Join Types**:
        1. **Inner Join**: Returns rows with matching values in both DataFrames.
        2. **Outer Join**: Returns all rows from both DataFrames, with missing values filled with `NaN`.
        3. **Left Join**: Returns all rows from the left DataFrame and matching rows from the right DataFrame.
        4. **Right Join**: Returns all rows from the right DataFrame and matching rows from the left DataFrame.
        """)

        # Syntax Section
        st.header("Syntax of `merge()` for Joins")
        st.write("""
        ```python
        pd.merge(left, right, how='join_type', on=None, left_on=None, right_on=None)
        ```

        **Parameters**:
        - `left`: First DataFrame to join.
        - `right`: Second DataFrame to join.
        - `how`: Type of join (`'inner'`, `'outer'`, `'left'`, `'right'`).
        - `on`: Column(s) to join on. Should exist in both DataFrames.
        - `left_on`, `right_on`: Specific columns to join on for left and right DataFrames if they have different column names.
        """)

        # Example DataFrames
        st.subheader("Example DataFrames")
        left_df = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40]
        })
        right_df = pd.DataFrame({
            'ID': [3, 4, 5, 6],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
            'Salary': [70000, 80000, 90000, 100000]
        })

        st.write("Left DataFrame:")
        st.write(left_df)
        st.write("Right DataFrame:")
        st.write(right_df)

        # Inner Join
        st.subheader("1. Inner Join")
        st.write("""
        **Definition**: Returns rows with matching values in both DataFrames.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='inner', on='ID')
        """, language="python")
        inner_result = pd.merge(left_df, right_df, how='inner', on='ID')
        st.write(inner_result)

        # Outer Join
        st.subheader("2. Outer Join")
        st.write("""
        **Definition**: Returns all rows from both DataFrames, with missing values filled with `NaN`.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='outer', on='ID')
        """, language="python")
        outer_result = pd.merge(left_df, right_df, how='outer', on='ID')
        st.write(outer_result)

        # Left Join
        st.subheader("3. Left Join")
        st.write("""
        **Definition**: Returns all rows from the left DataFrame and matching rows from the right DataFrame.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='left', on='ID')
        """, language="python")
        left_result = pd.merge(left_df, right_df, how='left', on='ID')
        st.write(left_result)

        # Right Join
        st.subheader("4. Right Join")
        st.write("""
        **Definition**: Returns all rows from the right DataFrame and matching rows from the left DataFrame.
        """)
        st.code("""
    result = pd.merge(left_df, right_df, how='right', on='ID')
        """, language="python")
        right_result = pd.merge(left_df, right_df, how='right', on='ID')
        st.write(right_result)

        # Tips for Using Joins
        st.header("Tips for Using Joins in Pandas")
        st.write("""
        - Use `on` to specify the common column(s) for joining.
        - Use `left_on` and `right_on` when the column names differ between DataFrames.
        - Use `how='inner'` when you only want rows with matching data in both DataFrames.
        - Use `how='outer'` to preserve all data, even if there are missing values.
        - Combine with `.fillna()` to handle missing data after joins.
        """)
    case 'reset_index':

        # Title
        st.title("Understanding `reset_index()` in Pandas")

        # Introduction
        st.header("What is `reset_index()`?")
        st.write("""
        The `reset_index()` function in Pandas is used to reset the index of a DataFrame, 
        turning the index into a column and creating a new default integer index.
        
        This is especially useful after filtering or manipulating a DataFrame, where 
        the index may not be consecutive or meaningful anymore.
        """)

        # Syntax Section
        st.header("Syntax of `reset_index()`")
        st.write("""
        ```python
        DataFrame.reset_index(drop=False, inplace=False)
        ```
        
        **Parameters**:
        - `drop`: If set to `True`, the old index is not added as a column in the DataFrame.
        - `inplace`: If `True`, modifies the DataFrame in place; if `False`, returns a new DataFrame.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40]
        })
        df.set_index('Name', inplace=True)  # Setting 'Name' as the index
        st.write("DataFrame with Custom Index (Name):")
        st.write(df)

        # Resetting the index
        st.subheader("Resetting the Index")
        df_reset = df.reset_index()  # Reset the index to default
        st.write("DataFrame after `reset_index()`:")
        st.write(df_reset)

        # Resetting index with drop=True (without keeping the old index)
        st.subheader("Resetting Index with `drop=True`")
        df_reset_drop = df.reset_index(drop=True)
        st.write("DataFrame after `reset_index(drop=True)` (old index dropped):")
        st.write(df_reset_drop)

        # Inplace Example
        st.subheader("Inplace Resetting of Index")
        st.write("""
        When `inplace=True`, the original DataFrame is modified directly without needing to assign it back.
        """)
        df.reset_index(inplace=True)
        st.write("DataFrame after `reset_index(inplace=True)` (original DataFrame modified):")
        st.write(df)

        # Conclusion
        st.header("Key Points to Remember")
        st.write("""
        - `reset_index()` is used to reset the index of a DataFrame.
        - By default, the old index becomes a new column in the DataFrame.
        - Use `drop=True` if you don’t want to retain the old index.
        - Use `inplace=True` if you want to modify the original DataFrame without creating a new one.
        """)

    case 'isnull':

        # Title
        st.title("Understanding `isnull()` in Pandas")

        # Introduction
        st.header("What is `isnull()`?")
        st.write("""
        The `isnull()` function in Pandas is used to identify missing or `NaN` (Not a Number) values in a DataFrame or Series.
        It returns a DataFrame or Series with boolean values, where `True` represents a missing value (`NaN`) and `False` indicates a non-missing value.
        """)

        # Syntax Section
        st.header("Syntax of `isnull()`")
        st.write("""
        ```python
        DataFrame.isnull()
        Series.isnull()
        ```
        This function can be applied to both DataFrames and Series. It helps in identifying missing values so you can handle them appropriately.
        """)

        # Example DataFrame with NaN Values
        st.subheader("Example DataFrame with Missing Values")
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', None],
            'Age': [25, None, 30, 35],
            'City': ['New York', 'Los Angeles', None, 'Miami']
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame with Missing Values:")
        st.write(df)

        # Using `isnull()` to Detect Missing Values
        st.subheader("Detecting Missing Values using `isnull()`")
        df_isnull = df.isnull()  # Detect missing values
        st.write("DataFrame after applying `isnull()`:")
        st.write(df_isnull)

        # Counting Missing Values in Each Column
        st.subheader("Counting Missing Values in Each Column")
        st.write("Count of missing values in each column:")
        st.write(df.isnull().sum())

        # Conclusion
        st.header("Key Points to Remember")
        st.write("""
        - `isnull()` helps in identifying missing (`NaN`) values in a DataFrame or Series.
        - It returns a DataFrame or Series with boolean values (`True` for missing values and `False` for non-missing values).
        - You can use `sum()` to count the missing values in each column or row.
        - `isnull()` is commonly used as the first step in handling missing data.
        """)
    case 'pivot':

        # Title
        st.title("Understanding `pivot()` in Pandas")

        # Introduction
        st.header("What is `pivot()`?")
        st.write("""
        The `pivot()` function in Pandas is used to reshape data where columns are pivoted into rows, based on the unique values of one or more columns. It’s a way to reorganize data and present it in a new format.
        Unlike the `pivot_table()` function, `pivot()` is mainly used when you have a unique set of values for the column you want to pivot.
        This is useful when you want to transform data from long to wide format.
        """)

        # Syntax Section
        st.header("Syntax of `pivot()`")
        st.write("""
        ```python
        DataFrame.pivot(
            index=None,
            columns=None,
            values=None
        )
        ```

        The main parameters are:

        - **`index`**: The column to use for the new DataFrame index.
        - **`columns`**: The column whose unique values will become the new columns.
        - **`values`**: The column whose values will be displayed in the new DataFrame.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        data = {
            'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
            'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
            'Temperature': [30, 22, 28, 24]
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame:")
        st.write(df)

        # Creating Pivot Table
        st.subheader("Creating a Pivot with `pivot()`")
        pivot_df = df.pivot(
            index='Date',
            columns='City',
            values='Temperature'
        )
        st.write("Pivot Table (Temperature by Date and City):")
        st.write(pivot_df)

        # Explanation of Pivot
        st.subheader("Explanation of Pivot")
        st.write("""
        In this pivot table:
        - **`index='Date'`**: The `Date` column is used to form the row indices of the pivot table.
        - **`columns='City'`**: The unique values in the `City` column (New York, Los Angeles) will become the new columns.
        - **`values='Temperature'`**: The `Temperature` values are placed in the corresponding cells.
        
        This results in a table where each row represents a unique `Date` and each column represents a city with its corresponding temperature value.
        """)

        # Handling Duplicate Values in Pivot
        st.subheader("Handling Duplicate Values in `pivot()`")
        st.write("""
        The `pivot()` function requires that the combination of `index` and `columns` must be unique. If there are duplicates, you will encounter a `ValueError`. 
        In such cases, you should consider using `pivot_table()` which can handle duplicates by applying aggregation functions.
        """)

        # Example of Duplicate Values in `pivot()`
        st.subheader("Example of Duplicate Values Causing an Error")
        data_with_duplicates = {
            'Date': ['2023-01-01', '2023-01-01', '2023-01-01'],
            'City': ['New York', 'New York', 'Los Angeles'],
            'Temperature': [30, 32, 24]
        }
        df_with_duplicates = pd.DataFrame(data_with_duplicates)
        st.write("DataFrame with Duplicates:")
        st.write(df_with_duplicates)

        try:
            pivot_with_duplicates = df_with_duplicates.pivot(
                index='Date',
                columns='City',
                values='Temperature'
            )
            st.write(pivot_with_duplicates)
        except ValueError as e:
            st.error(f"Error: {e}")
            st.write("""
            Since there are duplicate `Date` and `City` combinations, the `pivot()` function raises an error. 
            You can handle this by using `pivot_table()` with an aggregation function like `sum()` or `mean()`.
            """)

        # Key Points to Remember
        st.header("Key Points to Remember")
        st.write("""
        - **`pivot()`** is used to reshape data, turning unique values of a column into new columns.
        - It is ideal for transforming data from long to wide format.
        - The combination of the `index` and `columns` should be unique for the `pivot()` function to work.
        - If there are duplicates, `pivot()` raises a `ValueError`. In such cases, use `pivot_table()` to aggregate data.
        """)
    case 'pivot table':
    
        # Title
        st.title("Understanding `pivot_table()` in Pandas")

        # Introduction
        st.header("What is `pivot_table()`?")
        st.write("""
        The `pivot_table()` function in Pandas is an essential tool for summarizing and aggregating data. It is used to create a pivot table, which is a table that rearranges data by applying aggregation functions (such as `sum()`, `mean()`, etc.) to certain groups of data. 
        This function is an extension of the `pivot()` function, but it allows you to handle duplicate values and provides more flexibility by allowing the use of aggregation functions.

        Unlike `pivot()`, which is limited to unique combinations of `index` and `columns`, `pivot_table()` can handle duplicates and aggregate data in various ways.
        """)

        # Syntax Section
        st.header("Syntax of `pivot_table()`")
        st.write("""
        ```python
        DataFrame.pivot_table(
            data=None,
            values=None,
            index=None,
            columns=None,
            aggfunc='mean',
            fill_value=None,
            margins=False,
            dropna=True,
            margins_name='All'
        )
        ```

        The main parameters are:

        - **`values`**: The column(s) to aggregate. If None, all numeric columns are used.
        - **`index`**: The column(s) to use for the new row labels.
        - **`columns`**: The column(s) to use for the new column labels.
        - **`aggfunc`**: The aggregation function to apply (e.g., `'mean'`, `'sum'`, `'count'`, `'max'`, etc.). Defaults to `'mean'`.
        - **`fill_value`**: The value to replace missing values with in the resulting table.
        - **`margins`**: Whether to add row/column totals. Defaults to False.
        - **`dropna`**: Whether to drop columns with NaN values. Defaults to True.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        data = {
            'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01', '2023-01-02'],
            'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
            'Temperature': [30, 22, 28, 24, 32, 26],
            'Rainfall': [5, 10, 3, 7, 8, 6]
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame:")
        st.write(df)

        # Creating Pivot Table
        st.subheader("Creating a Pivot Table with `pivot_table()`")
        pivot_table_df = df.pivot_table(
            values='Temperature',
            index='Date',
            columns='City',
            aggfunc='mean'
        )
        st.write("Pivot Table (Average Temperature by Date and City):")
        st.write(pivot_table_df)

        # Explanation of Pivot Table
        st.subheader("Explanation of the Pivot Table")
        st.write("""
        - **`values='Temperature'`**: We are aggregating the `Temperature` column.
        - **`index='Date'`**: The `Date` column is used to create row labels.
        - **`columns='City'`**: The `City` column is used to create the new column labels.
        - **`aggfunc='mean'`**: We are calculating the mean temperature for each city on each date.

        The resulting table shows the average temperature for New York and Los Angeles on each day.
        """)

        # Using Multiple Aggregation Functions
        st.subheader("Using Multiple Aggregation Functions")
        pivot_table_multiple_aggfunc = df.pivot_table(
            values=['Temperature', 'Rainfall'],
            index='Date',
            columns='City',
            aggfunc={'Temperature': 'mean', 'Rainfall': 'sum'}
        )
        st.write("Pivot Table with Multiple Aggregation Functions (Temperature - mean, Rainfall - sum):")
        st.write(pivot_table_multiple_aggfunc)

        # Handling Missing Data with `fill_value`
        st.subheader("Handling Missing Data with `fill_value`")
        st.write("""
        If the pivot table contains missing data (NaN values), you can replace them using the `fill_value` parameter.

        Example:
        ```python
        pivot_table_with_fill = df.pivot_table(
            values='Temperature',
            index='Date',
            columns='City',
            aggfunc='mean',
            fill_value=0
        )
        ```
        This would replace all missing temperature values with `0`.
        """)

        # Adding Margins
        st.subheader("Adding Margins (Row/Column Totals)")
        st.write("""
        You can add row and column totals (margins) to the pivot table by setting the `margins` parameter to `True`.

        Example:
        ```python
        pivot_table_with_margins = df.pivot_table(
            values='Temperature',
            index='Date',
            columns='City',
            aggfunc='mean',
            margins=True
        )
        ```
        This will add a row/column labeled `All` that shows the overall totals.
        """)

        # Key Points to Remember
        st.header("Key Points to Remember")
        st.write("""
        - The `pivot_table()` function is used for creating pivot tables with aggregation.
        - It can handle duplicates in the data and apply aggregation functions like `mean`, `sum`, `count`, etc.
        - You can handle missing data with the `fill_value` parameter.
        - The `margins` parameter adds row/column totals.
        - The `aggfunc` parameter allows you to use multiple aggregation functions.
        """)
    case 'drop':
        # Title
        st.title("Understanding `drop()` in Pandas")

        # Introduction
        st.header("What is `drop()`?")
        st.write("""
        The `drop()` function in Pandas is used to remove rows or columns from a DataFrame. You can use it to remove unwanted data based on specific labels or indexes.
        It provides flexibility to delete rows or columns and allows you to control whether the operation modifies the original DataFrame or returns a new one.

        It is an essential function for data cleaning, allowing you to remove irrelevant or unnecessary data points from your dataset.
        """)

        # Syntax Section
        st.header("Syntax of `drop()`")
        st.write("""
        ```python
        DataFrame.drop(
            labels=None, 
            axis=0, 
            index=None, 
            columns=None, 
            level=None, 
            inplace=False, 
            errors='raise'
        )
        ```

        The main parameters are:

        - **`labels`**: The row/column labels to remove.
        - **`axis`**: Specify whether to remove rows (0) or columns (1).
        - **`index`**: The index labels to remove (used instead of `labels` when dropping rows).
        - **`columns`**: The column labels to remove (used instead of `labels` when dropping columns).
        - **`inplace`**: If `True`, modifies the original DataFrame directly. Default is `False`.
        - **`errors`**: If 'ignore', no error will be raised if the label is not found. Default is 'raise'.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame:")
        st.write(df)

        # Dropping Columns
        st.subheader("Dropping Columns")
        df_drop_columns = df.drop(columns=['B', 'C'])
        st.write("DataFrame after dropping columns 'B' and 'C':")
        st.write(df_drop_columns)

        # Dropping Rows
        st.subheader("Dropping Rows")
        df_drop_rows = df.drop(index=[0, 2])
        st.write("DataFrame after dropping rows with index 0 and 2:")
        st.write(df_drop_rows)

        # Explanation of `drop()`
        st.subheader("Explanation of the Example")
        st.write("""
        - **Dropping Columns**: We used `df.drop(columns=['B', 'C'])` to remove the columns 'B' and 'C'.
        - **Dropping Rows**: We used `df.drop(index=[0, 2])` to remove the rows at index 0 and 2.
        
        In both cases, the `drop()` function returns a new DataFrame with the specified rows or columns removed. The original DataFrame is not modified unless `inplace=True` is specified.
        """)

        # Using `inplace=True`
        st.subheader("Using `inplace=True`")
        st.write("""
        By setting `inplace=True`, you modify the original DataFrame instead of returning a new one. Here's how you can use it:
        
        Example:
        ```python
        df.drop(columns=['A'], inplace=True)
        ```
        This will remove column 'A' directly from the original DataFrame without creating a new one.
        """)

        # Handling Errors with `errors='ignore'`
        st.subheader("Handling Errors with `errors='ignore'`")
        st.write("""
        If you try to drop a label that doesn't exist in the DataFrame, the default behavior is to raise an error. You can suppress this behavior by using `errors='ignore'`.

        Example:
        ```python
        df.drop(columns=['Z'], errors='ignore')
        ```
        This will not raise an error even if the column 'Z' does not exist in the DataFrame.
        """)

        # Key Points to Remember
        st.header("Key Points to Remember")
        st.write("""
        - The `drop()` function is used to remove rows or columns from a DataFrame.
        - You can drop rows using the `index` parameter and columns using the `columns` parameter.
        - The `inplace` parameter controls whether the modification is done in place (modifying the original DataFrame) or returns a new DataFrame.
        - If `errors='ignore'`, the function will not raise an error if the label is not found.
        """)
    case 'dropna':

        # Title
        st.title("Understanding `dropna()` in Pandas")

        # Introduction
        st.header("What is `dropna()`?")
        st.write("""
        The `dropna()` function in Pandas is used to remove missing or NaN values from a DataFrame or Series. 
        It is a critical function for cleaning data by eliminating rows or columns that contain missing values, allowing for more accurate analysis.

        The function provides flexibility in how you handle missing values, whether you want to drop rows, columns, or apply specific conditions like keeping rows with a minimum number of non-null values.
        """)

        # Syntax Section
        st.header("Syntax of `dropna()`")
        st.write("""
        ```python
        DataFrame.dropna(
            axis=0, 
            how='any', 
            thresh=None, 
            subset=None, 
            inplace=False
        )
        ```

        The main parameters are:

        - **`axis`**: Drop rows (0) or columns (1). Default is 0 (rows).
        - **`how`**: 'any' (drop rows/columns with any NaN) or 'all' (drop only rows/columns with all NaNs).
        - **`thresh`**: Minimum non-null values required to keep the row/column.
        - **`subset`**: A list of rows/columns to check for NaN values.
        - **`inplace`**: If True, modifies the original DataFrame. Default is False (returns a new DataFrame).
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        data = {
            'A': [1, 2, None, 4],
            'B': [5, None, 7, 8],
            'C': [None, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame:")
        st.write(df)

        # Dropping Rows with NaN
        st.subheader("Dropping Rows with NaN Values")
        df_drop_rows = df.dropna(axis=0, how='any')
        st.write("DataFrame after dropping rows with any NaN values:")
        st.write(df_drop_rows)

        # Dropping Columns with NaN
        st.subheader("Dropping Columns with NaN Values")
        df_drop_columns = df.dropna(axis=1, how='any')
        st.write("DataFrame after dropping columns with any NaN values:")
        st.write(df_drop_columns)

        # Using `thresh` to Drop Based on Minimum Non-Null Values
        st.subheader("Using `thresh` to Drop Based on Minimum Non-Null Values")
        df_drop_thresh = df.dropna(thresh=3)
        st.write("DataFrame after dropping rows with less than 3 non-null values:")
        st.write(df_drop_thresh)

        # Explanation of `dropna()` Examples
        st.subheader("Explanation of the Examples")
        st.write("""
        - **Dropping Rows with NaN**: We used `df.dropna(axis=0, how='any')` to drop rows that contain any NaN values. 
        This removes any row that has at least one missing value.
        
        - **Dropping Columns with NaN**: We used `df.dropna(axis=1, how='any')` to drop columns that contain any NaN values. 
        This removes any column that has at least one missing value.

        - **Using `thresh`**: We used `df.dropna(thresh=3)` to drop rows with fewer than 3 non-null values. 
        This ensures that only rows with at least 3 valid (non-null) values are retained.
        """)

        # Using `inplace=True`
        st.subheader("Using `inplace=True`")
        st.write("""
        By setting `inplace=True`, the operation will modify the original DataFrame directly, without returning a new DataFrame.

        Example:
        ```python
        df.dropna(axis=0, inplace=True)
        ```
        This will drop the rows with NaN values and update the original `df` without creating a new DataFrame.
        """)

        # Handling Specific Columns with `subset`
        st.subheader("Handling Specific Columns with `subset`")
        st.write("""
        You can use the `subset` parameter to drop rows or columns based on specific columns or rows that contain NaN values.

        Example:
        ```python
        df.dropna(subset=['A', 'B'], axis=0)
        ```
        This will drop rows where the values in columns 'A' or 'B' are NaN.
        """)

        # Key Points to Remember
        st.header("Key Points to Remember")
        st.write("""
        - The `dropna()` function is used to remove rows or columns with missing (NaN) values.
        - You can drop rows or columns based on the presence of NaN values using `axis` and `how`.
        - The `thresh` parameter allows you to set a minimum number of non-null values required to retain a row/column.
        - The `subset` parameter allows you to drop NaN values from specific columns or rows only.
        - The `inplace` parameter controls whether the operation modifies the original DataFrame or returns a new one.
        """)

    case 'fillna':

        # Title
        st.title("Understanding `fillna()` in Pandas")

        # Introduction
        st.header("What is `fillna()`?")
        st.write("""
        The `fillna()` function in Pandas is used to replace missing values (`NaN`) in a DataFrame or Series with a specified value or method. 
        It helps in handling missing data by filling gaps in your dataset, ensuring the data is complete for analysis.

        You can fill missing values using a constant value, the last valid value (forward fill), or the next valid value (backward fill).
        """)

        # Syntax Section
        st.header("Syntax of `fillna()`")
        st.write("""
        ```python
        DataFrame.fillna(
            value=None, 
            method=None, 
            axis=None, 
            inplace=False, 
            limit=None, 
            downcast=None
        )
        ```

        The main parameters are:

        - **`value`**: The value to fill missing values with (e.g., 0, mean, etc.).
        - **`method`**: 'ffill' for forward fill, 'bfill' for backward fill.
        - **`axis`**: Fill along rows (0) or columns (1).
        - **`inplace`**: If True, modifies the original DataFrame.
        - **`limit`**: The maximum number of replacements to make.
        - **`downcast`**: Used for downcasting dtypes, if applicable.
        """)

        # Example DataFrame
        st.subheader("Example DataFrame")
        data = {
            'A': [1, 2, None, 4],
            'B': [None, 6, 7, None],
            'C': [None, 10, 11, 12]
        }
        df = pd.DataFrame(data)
        st.write("Original DataFrame:")
        st.write(df)

        # Filling with a Constant Value
        st.subheader("Filling with a Constant Value")
        df_fill_constant = df.fillna(value=0)
        st.write("DataFrame after filling NaN with 0:")
        st.write(df_fill_constant)

        # Forward Fill (Propagate last valid value forward)
        st.subheader("Forward Fill")
        df_fill_ffill = df.fillna(method='ffill')
        st.write("DataFrame after forward fill:")
        st.write(df_fill_ffill)

        # Backward Fill (Propagate next valid value backward)
        st.subheader("Backward Fill")
        df_fill_bfill = df.fillna(method='bfill')
        st.write("DataFrame after backward fill:")
        st.write(df_fill_bfill)

        # Filling with Mean of the Column
        st.subheader("Filling with Mean of the Column")
        df_fill_mean = df.fillna(value=df.mean())
        st.write("DataFrame after filling NaN with column mean:")
        st.write(df_fill_mean)

        # Explanation of `fillna()` Examples
        st.subheader("Explanation of the Examples")
        st.write("""
        - **Filling with a Constant Value**: We used `df.fillna(value=0)` to replace all missing values with 0.
        - **Forward Fill**: We used `df.fillna(method='ffill')` to propagate the last valid value forward to fill any missing values.
        - **Backward Fill**: We used `df.fillna(method='bfill')` to propagate the next valid value backward to fill any missing values.
        - **Filling with Mean**: We used `df.fillna(value=df.mean())` to replace missing values with the mean of each column.
        """)

        # Using `inplace=True`
        st.subheader("Using `inplace=True`")
        st.write("""
        By setting `inplace=True`, the operation will modify the original DataFrame directly, without returning a new DataFrame.

        Example:
        ```python
        df.fillna(value=0, inplace=True)
        ```
        This will fill missing values in `df` with 0 and update the original DataFrame directly.
        """)

        # Using `limit` to Control Number of Replacements
        st.subheader("Using `limit` to Control Number of Replacements")
        st.write("""
        You can limit the number of replacements made using the `limit` parameter. For example:

        ```python
        df.fillna(value=0, limit=1)
        ```

        This will fill only the first missing value with 0.
        """)

        # Key Points to Remember
        st.header("Key Points to Remember")
        st.write("""
        - The `fillna()` function is used to replace missing (`NaN`) values with a specified value or method.
        - You can fill missing values with a constant, forward fill, or backward fill using the `method` parameter.
        - The `inplace` parameter controls whether the operation modifies the original DataFrame or returns a new one.
        - You can control the number of replacements using the `limit` parameter.
        - The `value` parameter can be a scalar, dictionary, or Series, allowing for flexible filling strategies.
        """)

    case 'ffill and bfill':
        st.title("Understanding Forward Fill (`ffill`) and Backward Fill (`bfill`) in Pandas")

        # Create DataFrame with missing values
        data = {'A': [1, 2, None, 4, None, 6]}
        df = pd.DataFrame(data)
        
        st.subheader("Original DataFrame")
        st.write(df)

        st.write("""
        **Forward Fill (`ffill`)** and **Backward Fill (`bfill`)** are two methods in Pandas used to handle missing values (NaN).
        
        - **`ffill` (Forward Fill)**: 
            - The forward fill method propagates the previous valid value forward to fill in the missing values.
            - This is useful when you want to assume that the value for missing data is the same as the last valid data point.
            - For example, in time series data, it’s common to use forward fill to carry forward the last known value.

        - **`bfill` (Backward Fill)**:
            - The backward fill method propagates the next valid value backward to fill the missing values.
            - This method is helpful when you assume that the missing value will be similar to the next available value.
            - This can be useful when you know future data points can provide better estimates for the missing values.
        """)

        # Using forward fill (ffill)
        df_ffill = df.fillna(method='ffill')
        st.subheader("DataFrame after Forward Fill (`ffill`)")
        st.write(df_ffill)

        # Using backward fill (bfill)
        df_bfill = df.fillna(method='bfill')
        st.subheader("DataFrame after Backward Fill (`bfill`)")
        st.write(df_bfill)

        st.write("""
        ### Differences between `ffill` and `bfill`:
        - **`ffill`** propagates the last valid value forward (previous value).
        - **`bfill`** propagates the next valid value backward (next value).
        
        ### When to Use:
        - Use **`ffill`** when you assume that missing values are more like the previous ones (e.g., for time series where values remain constant or slowly change).
        - Use **`bfill`** when you assume the missing values should be more like the following ones (e.g., for forward-looking trends in some datasets).

        ### Example:
        - Given the original DataFrame:
        ```
            A
        0  1.0
        1  2.0
        2  NaN
        3  4.0
        4  NaN
        5  6.0
        ```
        - After **`ffill`**:
        ```
            A
        0  1.0
        1  2.0
        2  2.0
        3  4.0
        4  4.0
        5  6.0
        ```
        - After **`bfill`**:
        ```
            A
        0  1.0
        1  2.0
        2  4.0
        3  4.0
        4  6.0
        5  6.0
        ```
        """)
    case 'interpolate':

        st.title("Understanding Interpolation in Pandas")

        # Create DataFrame with missing values
        data = {'A': [1, 2, None, 4, None, 6]}
        df = pd.DataFrame(data)
        
        st.subheader("Original DataFrame")
        st.write(df)

        st.write("""
        ### What is Interpolation?
        
        **Interpolation** is a technique used to estimate missing data values by using surrounding values. It helps fill in missing data points based on other data points in the dataset. Pandas provides an `interpolate()` function to perform this task efficiently.

        ### Types of Interpolation in Pandas:
        - **Linear Interpolation (default method)**:
            - This is the default method, where missing values are filled by assuming the data points form a straight line between existing points. 
            - It works well for time series data and numerical data where the changes between data points are linear.
        
        - **Polynomial Interpolation**:
            - This method fits a polynomial curve to the data, providing a smoother interpolation compared to linear interpolation.
            - Polynomial interpolation is used when the data shows non-linear trends.

        - **Spline Interpolation**:
            - This method uses piecewise polynomial functions (splines) to interpolate the missing data points.
            - It is commonly used when smooth curves are needed, and it works well for higher-dimensional data.

        - **Time Interpolation**:
            - This is used specifically for time series data, where the interpolation is done by treating the time axis as an index.

        - **Other Methods**:
            - Pandas also supports other interpolation methods like nearest, quadratic, cubic, etc.

        ### Syntax of `interpolate()`:
        ```python
        DataFrame.interpolate(method='linear', axis=0, limit=None, inplace=False, downcast=None)
        ```

        - **`method`**: Specifies the interpolation method (`'linear'`, `'polynomial'`, `'spline'`, etc.).
        - **`axis`**: The axis to interpolate over (0 for rows, 1 for columns).
        - **`limit`**: Maximum number of missing values to fill.
        - **`inplace`**: If `True`, modifies the original DataFrame.
        - **`downcast`**: Specifies the type of the interpolated result.

        ### Example of Linear Interpolation:
        Using linear interpolation, we can estimate the missing values by assuming a straight line between two known values.

        ```python
        df_interpolated = df.interpolate(method='linear')
        st.write("DataFrame after Linear Interpolation:")
        st.write(df_interpolated)
        ```

        ### Example of Polynomial Interpolation:
        For a polynomial curve fitting, we can specify the degree of the polynomial:
        
        ```python
        df_interpolated_poly = df.interpolate(method='polynomial', order=2)
        st.write("DataFrame after Polynomial Interpolation (degree 2):")
        st.write(df_interpolated_poly)
        ```

        ### Example of Spline Interpolation:
        For spline interpolation, specify the `spline` method and optionally the order of the spline:
        
        ```python
        df_interpolated_spline = df.interpolate(method='spline', order=3)
        st.write("DataFrame after Spline Interpolation (order 3):")
        st.write(df_interpolated_spline)
        ```

        ### When to Use Interpolation:
        - **Linear Interpolation**: Suitable when data points are expected to change linearly.
        - **Polynomial/Spline Interpolation**: Use for more complex datasets where linear changes aren't a good fit.
        - **Time Series**: Use time-based interpolation for time-related data to keep consistent time intervals.

        ### Example Output for Linear Interpolation:
        - Given the original DataFrame:
        ```
            A
        0  1.0
        1  2.0
        2  NaN
        3  4.0
        4  NaN
        5  6.0
        ```
        - After Linear Interpolation:
        ```
            A
        0  1.0
        1  2.0
        2  3.0
        3  4.0
        4  5.0
        5  6.0
        ```
        """)

        # Interpolating using Linear method
        df_interpolated = df.interpolate(method='linear')
        st.subheader("DataFrame after Linear Interpolation")
        st.write(df_interpolated)

        # Interpolating using Polynomial method
        df_interpolated_poly = df.interpolate(method='polynomial', order=2)
        st.subheader("DataFrame after Polynomial Interpolation (degree 2)")
        st.write(df_interpolated_poly)

        # Interpolating using Spline method
        df_interpolated_spline = df.interpolate(method='spline', order=3)
        st.subheader("DataFrame after Spline Interpolation (order 3)")
        st.write(df_interpolated_spline)

    case 'plot':

        import numpy as np
        import matplotlib.pyplot as plt

        st.title("Plotting in Pandas")
        st.write("""
        ### Plotting in Pandas

        **Pandas** provides a convenient way to plot data directly from a DataFrame using the `.plot()` function, which utilizes `matplotlib` in the background.

        Pandas `.plot()` supports multiple types of plots such as line, bar, histogram, scatter, etc. and allows easy customization.

        ### Syntax:
        ```python
        DataFrame.plot(kind='line', x=None, y=None, title=None, xlabel=None, ylabel=None, grid=False, color=None)
        ```

        - **`kind`**: Specifies the type of plot (`'line'`, `'bar'`, `'hist'`, `'scatter'`, etc.)
        - **`x`**: Column name to be used on the x-axis.
        - **`y`**: Column name(s) to be used on the y-axis.
        - **`title`**: Title of the plot.
        - **`xlabel`**: Label for the x-axis.
        - **`ylabel`**: Label for the y-axis.
        - **`grid`**: If `True`, displays gridlines.
        - **`color`**: Specifies the color of the plot lines.

        ### Line Plot (Default)
        A line plot is the default plot type. It connects data points with lines.
        """)

        st.title("Plotting with Pandas: Different Types of Plots")

        # Create a sample DataFrame
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': [2, 3, 4, 5, 6]
        }
        df = pd.DataFrame(data)

        st.subheader("Original DataFrame")
        st.write(df)

        # Line plot
        st.subheader("Line Plot")
        st.write("""
        **Line Plot**: The line plot is used to visualize data trends over time or continuous data points. In pandas, line plots are generated by default with `plot()` when `kind='line'`.
        """)
        st.code("""
        ax = df.plot(kind='line', title="Line Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Bar plot
        st.subheader("Bar Plot")
        st.write("""
        **Bar Plot**: A bar plot is used to represent categorical data with rectangular bars. The height of each bar is proportional to the value it represents.
        """)
        st.code("""
        ax = df.plot(kind='bar', title="Bar Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Horizontal Bar plot
        st.subheader("Horizontal Bar Plot")
        st.write("""
        **Horizontal Bar Plot**: A variation of the bar plot, but the bars are horizontal instead of vertical.
        """)
        st.code("""
        ax = df.plot(kind='barh', title="Horizontal Bar Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Histogram plot
        st.subheader("Histogram Plot")
        st.write("""
        **Histogram Plot**: A histogram is used to represent the distribution of numerical data by dividing it into bins. It helps understand the distribution of data points.
        """)
        st.code("""
        ax = df['A'].plot(kind='hist', bins=5, title="Histogram Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Box plot
        st.subheader("Box Plot")
        st.write("""
        **Box Plot**: Box plots are used to show the distribution of numerical data through their quartiles. They highlight outliers, median, and the interquartile range (IQR).
        """)
        st.code("""
        ax = df.plot(kind='box', title="Box Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Scatter plot
        st.subheader("Scatter Plot")
        st.write("""
        **Scatter Plot**: A scatter plot is used to visualize the relationship between two numerical variables. Each point represents a data pair.
        """)
        st.code("""
        ax = df.plot(kind='scatter', x='A', y='B', title="Scatter Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Area plot
        st.subheader("Area Plot")
        st.write("""
        **Area Plot**: An area plot is similar to a line plot, but the area beneath the line is filled with color. It's useful for showing cumulative data.
        """)
        st.code("""
        ax = df.plot(kind='area', title="Area Plot")
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        # Pie plot
        st.subheader("Pie Plot")
        st.write("""
        **Pie Plot**: A pie plot is used to represent proportions or percentages of a whole. It’s good for categorical data where the sum is meaningful.
        """)
        st.code("""
        ax = df['A'].plot(kind='pie', title="Pie Plot", autopct='%1.1f%%')
        st.pyplot(ax.figure)  # Use the figure from the Axes object
        """)

        st.write("""
        ### Summary of Pandas Plotting Methods:
        - **`plot(kind='line')`**: Creates a line plot (default).
        - **`plot(kind='bar')`**: Creates a bar plot.
        - **`plot(kind='barh')`**: Creates a horizontal bar plot.
        - **`plot(kind='hist')`**: Creates a histogram.
        - **`plot(kind='box')`**: Creates a box plot.
        - **`plot(kind='scatter')`**: Creates a scatter plot.
        - **`plot(kind='area')`**: Creates an area plot.
        - **`plot(kind='pie')`**: Creates a pie plot.

        Pandas integrates seamlessly with Matplotlib, so you can further customize the plots with additional Matplotlib options (e.g., changing labels, titles, or styling).
        """)
