import streamlit as st
import io
import contextlib




def Q41():
    st.title("41. Subtract the Product and Sum of Digits of an Integer")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    with col1:
        st.write(""" 
            **Problem**: Given an integer number n, return the difference between the product of its digits and the sum of its digits.
            \n
        """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `n = 234`\n
            - Output: `15`\n
            - Explanation: Product = 2 * 3 * 4 = 24, Sum = 2 + 3 + 4 = 9, Difference = 24 - 9 = 15
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `n = 4421`\n
            - Output: `21`
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: `n = 100`\n
            - Output: `0`
        """)

    # Use columns to display Constraints and Topics side by side
    col_constraints, col_topics = st.columns(2)

    with col_constraints:
        st.write("""
            **Constraints**:
            - `0 <= n <= 10^5`
        """)

    with col_topics:
        st.write("""
            **Topics**:
            - **Math**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def subtractProductAndSum(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 234, "expected": 15},
                {"input": 4421, "expected": 21},
                {"input": 100, "expected": -1},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function `subtractProductAndSum` is defined
                        if "subtractProductAndSum" in user_namespace:
                            subtractProductAndSum = user_namespace['subtractProductAndSum']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = subtractProductAndSum(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `subtractProductAndSum` not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
       with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
        st.code(""" 
def subtractProductAndSum(n):
    # Initialize product to 1 (for multiplication) and sum to 0 (for addition)
    product = 1
    sum = 0
    
    # Loop through each digit of the number
    while n > 0:
        # Get the last digit of n
        digit = n % 10

        # Multiply product by the current digit
        product *= digit

        # Add the current digit to sum
        sum += digit

        # Remove the last digit from n
        n //= 10

    # Return the difference between the product and the sum of digits
    return product - sum
        """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/41.png")  



def Q42():
    st.title("43. Sum of Two Integers Without Using + and -")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sum-of-two-integers/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given two integers `a` and `b`, return the sum of the two integers without using the operators + and -.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `a = 1, b = 2`\n
            - Output: `3`
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `a = 3, b = 4`\n
            - Output: `7`
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: `a = -1, b = 1`\n
            - Output: `0`
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - `-100 <= a, b <= 100`\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Bit Manipulation**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def getSum(a, b):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 2], "expected": 3},
                {"input": [3, 4], "expected": 7},
                {"input": [-1, 1], "expected": 0},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function `getSum` is defined
                        if "getSum" in user_namespace:
                            getSum = user_namespace['getSum']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = getSum(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `getSum` not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
    def subtractProductAndSum(n):
        # Initialize product to 1 (for multiplication) and sum to 0 (for addition)
        product = 1
        sum = 0
        
        # Loop through each digit of the number
        while n > 0:
            # Get the last digit of n
            digit = n % 10

            # Multiply product by the current digit
            product *= digit

            # Add the current digit to sum
            sum += digit

            # Remove the last digit from n
            n //= 10

        # Return the difference between the product and the sum of digits
        return product - sum
            """)


    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/42.png")


def Q43():
    st.title("43. Divisor Game")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/divisor-game/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Alice and Bob take turns playing a game with a positive integer `n`. In each turn, the player chooses an integer `x` such that `0 < x < n` and `n % x == 0`. The player loses the game if they cannot make a move.
        
        Determine if Alice wins the game if both players play optimally.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 2\n
            - Output: True\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 3\n
            - Output: False\n
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2 = st.columns(3)

    with colc:
        st.write("""
            - 1 <= n <= 1000\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Math**
            - **Dynamic Programming**
            - **Game Theory**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def divisorGame(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 2, "expected": True},
                {"input": 3, "expected": False},
                {"input": 4, "expected": True},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function divisorGame is defined
                        if "divisorGame" in user_namespace:
                            divisorGame = user_namespace['divisorGame']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = divisorGame(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function divisorGame not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def divisorGame(n): 
    return n % 2 == 0  #return if number is divisible by 2
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/43.png")



def Q44():
    st.title("44. Generate Fibonacci Sequence")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/generate-fibonacci-sequence/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: The Fibonacci sequence is defined by the recurrence relation: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2. Given `n`, return the first `n` Fibonacci numbers.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 5\n
            - Output: [0, 1, 1, 2, 3]
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 1\n
            - Output: [0]
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: n = 10\n
            - Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 0 <= n <= 30\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Recursion**
            - **Dynamic Programming**
            - **Math**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def fibonacci(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 5, "expected": [0, 1, 1, 2, 3]},
                {"input": 1, "expected": [0]},
                {"input": 10, "expected": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function fibonacci is defined
                        if "fibonacci" in user_namespace:
                            fibonacci = user_namespace['fibonacci']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = fibonacci(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function fibonacci not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def fibonacci(k):
    lis = []  #initialize an empty list 
    
    for i in range(k):  #loops run i = 0 to till k
        if i == 0 or i == 1: # append i to thr lis if i == 0 or i == 1
            lis.append(i)
        if i > 1: # if i>1  appending list of previous element plus list of second previous element
            lis.append(lis[i - 1] + lis[i - 2])
    
    return lis #returning the actual lis
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/44.png")



def Q45():
    st.title("45. Generate a String With Characters That Have Odd Counts")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer `n`, return a string with `n` characters such that each character occurs an odd number of times.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 7\n
            - Output: 'aabaa'\n
            - Explanation: Use 'a' and 'b' such that each character appears an odd number of times.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 3\n
            - Output: 'aaa'
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: n = 1\n
            - Output: 'a'
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= n <= 100\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **String Manipulation**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 2, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def generateTheString(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 1, "expected": "a"},
                {"input": 2, "expected": "ab"},
                {"input": 3, "expected": "aaa"},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function generateTheString is defined
                        if "generateTheString" in user_namespace:
                            generateTheString = user_namespace['generateTheString']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = generateTheString(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function generateTheString not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def generateTheString(n):
    if n % 2 == 0: # enter the if condition if n id divisible by 2
        return 'a' * (n - 1) + 'b'  # return alphabet 'a' * (n-1) + 'b' if n is even
    else:
        return 'a' * n # return if n is odd 
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/45.png")


def Q46():
    st.title("46. Sum Multiples")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sum-multiples/) for a better experience.")

    # Create two columns: left for question, right for code input
    st.write("""
        **Problem**: Given an integer `n`, return the sum of all numbers less than `n` that are multiples of 3 or 5.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 10\n
            - Output: 23 (3 + 5 + 6 + 9)
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 15\n
            - Output: 45
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: n = 20\n
            - Output: 78
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 0 <= n <= 1000\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Math**
            - **Loops**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sum_multiples(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 10, "expected": 23},
                {"input": 15, "expected": 45},
                {"input": 20, "expected": 78},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function sum_multiples is defined
                        if "sum_multiples" in user_namespace:
                            sum_multiples = user_namespace['sum_multiples']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sum_multiples(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function sum_multiples not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def sum_multiples(n):
  r=0  #initialize variable i = 0
  for i in range(1,n): # forloop runs 1 to n+1 times
    if i % 3 == 0 or i % 5 == 0 : #enter into condition if i % 3,5
        r+=i # now add i to r now r = i+r
  return r # returning r 
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/46.png")


def Q47():
    st.title("47. Find Anagram Mappings")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/find-anagram-mappings/) for a better experience.")

    # Problem description
    st.write("""
        **Problem**: Given two arrays `arr1` and `arr2`, return an array of the indices of `arr2` corresponding to the elements of `arr1`.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example**:\n
            - Input: arr1 = [12, 28, 46, 32, 50], arr2 = [50, 12, 32, 46, 28]\n
            - Output: [1, 4, 3, 2, 0]
        """)

    with col2:
        st.write("""
            **Constraints**:\n
            - 1 <= arr1.length, arr2.length <= 1000\n
            - arr1.length == arr2.length
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Hashing**
            - **Arrays**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def anagram_mappings(arr1, arr2):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[12, 28, 46, 32, 50], [50, 12, 32, 46, 28]], "expected": [1, 4, 3, 2, 0]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: arr1 = {case['input'][0]}, arr2 = {case['input'][1]}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function anagram_mappings is defined
                        if "anagram_mappings" in user_namespace:
                            anagram_mappings = user_namespace['anagram_mappings']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = anagram_mappings(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function anagram_mappings not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def anagram_mappings(arr1, arr2):
    index_map = {val: idx for idx, val in enumerate(arr2)}
    return [index_map[val] for val in arr1]
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/47.png")



def Q48():
    st.title("48. Remove Vowels from a String")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/remove-vowels-from-a-string/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    with col1:
        st.write("""
            **Problem**: Given a string s, return the string after removing all vowels.
            \n
        """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: s = 'leetcode'\n
            - Output: 'ltcd'
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: s = 'hello'\n
            - Output: 'hll'
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: s = 'aeiou'\n
            - Output: ''
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= s.length <= 100
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Strings**
            - **Set Operations**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def remove_vowels(s):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ["leetcode"], "expected": "ltcd"},
                {"input": ["hello"], "expected": "hll"},
                {"input": ["aeiou"], "expected": ""},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: s = '{case['input'][0]}'")
                    st.write(f"- Expected Output: '{case['expected']}'")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function remove_vowels is defined
                        if "remove_vowels" in user_namespace:
                            remove_vowels = user_namespace['remove_vowels']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = remove_vowels(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected '{expected_val}', but got '{result}'")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function remove_vowels not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def remove_vowels(s):
    vowels = "aeiouAEIOU"  # Define a string of vowels
    result = []
    for char in s:
        if char not in vowels:  # Check if the character is not a vowel
            result.append(char)  # Append non-vowel characters to the result
    return ''.join(result)
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/48.png")




def Q49():
    st.title("49. Alternating Digit Sum")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/alternating-digit-sum/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given a positive integer `n`. The alternating digit sum of `n` is defined as the sum of its digits at odd indices minus the sum of its digits at even indices.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 521\n
            - Output: 4 (5 - 2 + 1 = 4)
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 111\n
            - Output: 1
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: n = 123456\n
            - Output: 0
        """)

    st.write("""
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= n <= 10^9\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Mathematics**
            - **Strings**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def alternating_digit_sum(n):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [521], "expected": 4},
                {"input": [111], "expected": 1},
                {"input": [123456], "expected": -3},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: n = {case['input'][0]}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        exec_globals = {}
                        exec(code_input, exec_globals)  # Execute the user code

                        # Check if the function alternating_digit_sum is defined
                        if "alternating_digit_sum" in exec_globals:
                            alternating_digit_sum = exec_globals['alternating_digit_sum']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = alternating_digit_sum(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function alternating_digit_sum not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def alternating_digit_sum(n):
    # Convert the number to a string to access each digit individually
    n = str(n)
    
    # Initialize a variable to store the alternating sum
    sum_ = 0
    
    # Iterate through each digit in the string representation of n
    for i in range(len(n)):
        # If the index is even, add the digit to the sum
        if i % 2 == 0:
            sum_ += int(n[i])
        # If the index is odd, subtract the digit from the sum
        else:
            sum_ -= int(n[i])
    
    # Return the final alternating sum
    return sum_

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/49.png")

def Q50():
    st.title("50. Find Closest Number to Zero")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/find-closest-number-to-zero/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer array `nums`, return the number with the value closest to 0.
        If there are multiple answers, return the number with the larger absolute value.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [-4, -1, 0, 3, 10]\n
            - Output: 0
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [1, 2, -1]\n
            - Output: -1
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [-2, -1]\n
            - Output: -1
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= nums.length <= 1000\n
            - -10^5 <= nums[i] <= 10^5
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Arrays**
            - **Mathematics**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def find_closest(nums):
    # Your code goes here
    pass
"""
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [-4, -1, 0, 3, 10], "expected": 0},
                {"input": [1, 2, -1], "expected": 1},
                {"input": [-2, -1], "expected": -1},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: nums = {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                
                # Create a placeholder for the result after the expander
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)
            
            # Create a placeholder for general execution errors
            error_placeholder = st.empty()

        with colRun:
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function find_closest is defined
                        if "find_closest" in user_namespace:
                            find_closest = user_namespace['find_closest']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = find_closest(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function find_closest not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def find_closest(nums):
    # Check if zero is in the list; if so, zero is the closest number to zero
    if 0 in nums:
        return 0  
    
    # Initialize 'closest' to the first element in nums
    closest = nums[0]
    
    # Loop through each number in the list
    for i in nums:
        # Update 'closest' if the absolute value of 'i' is smaller than 'closest' 
        # or if they are the same, but 'i' is positive (we want the positive number in ties)
        if abs(i) < abs(closest) or (abs(i) == abs(closest) and i > closest):
            closest = i  # Update closest with the new value

    # Return the closest number to zero
    return closest
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/50.png")



