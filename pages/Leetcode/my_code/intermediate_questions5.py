import streamlit as st
import io
import contextlib


def Q41():
    st.title("Number of Common Factors")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/number-of-common-factors/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given two positive integers, return the number of common factors of the two numbers.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: a = 12, b = 6\n
            - Output: 4\n
            - Explanation: Common factors are 1, 2, 3, and 6
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: a = 15, b = 5\n
            - Output: 3
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: a = 9, b = 3\n
            - Output: 3
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= a, b <= 1000\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Math**
            - **Number Theory**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def common_factors(a, b):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [12, 6], "expected": 4},
                {"input": [15, 5], "expected": 2},
                {"input": [9, 3], "expected": 2},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: a = {case['input'][0]}, b = {case['input'][1]}")
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

                        # Check if the function common_factors is defined
                        if "common_factors" in user_namespace:
                            common_factors = user_namespace['common_factors']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = common_factors(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function common_factors not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: every question has different solutions)", expanded=False):
            st.code("""
def common_factors(a, b):
    count = 0  # Initialize the count of common factors to zero
    k = min(a, b)  # Find the smaller of the two numbers, as a factor cannot be greater than this value
    
    for i in range(1, k + 1):  # Loop through all numbers from 1 to k
        # Check if both a and b are divisible by i, indicating a common factor
        if a % i == 0 and b % i == 0:
            count += 1  # Increment the count for each common factor found
            
    return count  # Return the total count of common factors

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")



def Q42():
    st.title("Minimum Common Value")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/minimum-common-value/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given two integer arrays, return the minimum common value. If there is no common value, return -1.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: array1 = [1, 2, 3], array2 = [2, 4]\n
            - Output: 2
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: array1 = [1, 2], array2 = [3, 4]\n
            - Output: -1
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: array1 = [5, 6, 7], array2 = [6, 7, 8]\n
            - Output: 6
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= array1.length, array2.length <= 1000\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Arrays**
            - **Hashing**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minimum_common_value(array1, array2):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[1, 2, 3], [2, 4]], "expected": 2},
                {"input": [[1, 2], [3, 4]], "expected": -1},
                {"input": [[5, 6, 7], [6, 7, 8]], "expected": 6},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: array1 = {case['input'][0]}, array2 = {case['input'][1]}")
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

                        # Check if the function minimum_common_value is defined
                        if "minimum_common_value" in user_namespace:
                            minimum_common_value = user_namespace['minimum_common_value']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minimum_common_value(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function minimum_common_value not defined. Please define the function to proceed.")
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
def minimum_common_value(nums1, nums2):
    i, j = 0, 0  # Initialize pointers for both lists at the start
    
    # Iterate up to the combined length of nums1 and nums2
    for _ in range(len(nums1) + len(nums2)):
        # If either pointer exceeds its list's length, exit the loop
        if i >= len(nums1) or j >= len(nums2):
            break
        
        # Check if the current elements in both lists are equal
        if nums1[i] == nums2[j]:
            return nums1[i]  # Return the common element if found
        elif nums1[i] < nums2[j]:
            i += 1  # Move the pointer in nums1 forward if its element is smaller
        else:
            j += 1  # Otherwise, move the pointer in nums2 forward
    
    return -1  # Return -1 if no common element is found

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")


def Q43():
    st.title("Average Value of Even Numbers that are Divisible by Three")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) for more details.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer array, return the average value of all even numbers that are divisible by three, rounded down to the nearest integer.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [1, 2, 3, 4, 6, 9]\n
            - Output: 6
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [2, 4, 6]\n
            - Output: 6
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [3, 5, 10, 12]\n
            - Output: 12
        """)

    st.write("""
        **Constraints**:
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= nums.length <= 1000\n
            - -100 <= nums[i] <= 100
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Math**
            - **Array**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def average_value(nums):\n    # Your code goes here\n    pass\n"""
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 2, 3, 4, 6, 9], "expected": 6},
                {"input": [2, 4, 6], "expected": 6},
                {"input": [3, 5, 10, 12], "expected": 12}
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

                        # Check if the function average_value is defined
                        if "average_value" in user_namespace:
                            average_value = user_namespace['average_value']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = average_value(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function average_value not defined. Please define the function to proceed.")
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
def average_value(nums):
    # Initialize an empty list to store numbers that meet the criteria
    lis = []

    # Iterate through each number in the input list
    for i in nums:
        # Check if the number is even and divisible by 3
        if i % 2 == 0 and i % 3 == 0:
            # If it meets both conditions, add it to the list
            lis.append(i)

    # Calculate the sum of all numbers in the list
    s = sum(lis)
    # Calculate the count of numbers in the list
    d = len(lis)

    # Return the average value, rounded down to the nearest integer
    # If there are no numbers that meet the criteria, return 0
    return s // d if d > 0 else 0

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")



def Q44():
    st.title("Convert Binary Number in a Linked List to Integer")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given a binary number represented as a linked list, convert it to an integer.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: head = [1, 0, 1]\n
            - Output: 5\n
            - Explanation: The binary number 101 corresponds to the decimal number 5.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: head = [0]\n
            - Output: 0
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: head = [1, 1, 1]\n
            - Output: 7
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - The linked list will have at most length 30.\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Linked Lists**
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
            value="""def getDecimalValue(head):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 0, 1], "expected": 5},
                {"input": [0], "expected": 0},
                {"input": [1, 1, 1], "expected": 7},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: head = {case['input']}")
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

                        # Check if the function getDecimalValue is defined
                        if "getDecimalValue" in user_namespace:
                            getDecimalValue = user_namespace['getDecimalValue']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                # Build linked list from input
                                head = ListNode(input_val[0])
                                current = head
                                for value in input_val[1:]:
                                    current.next = ListNode(value)
                                    current = current.next

                                try:
                                    result = getDecimalValue(head)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function getDecimalValue not defined. Please define the function to proceed.")
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
def getDecimalValue(head):
    # Initialize the result as 0
    num = 0

    # Traverse through the linked list
    while head:
        # Shift the current result one bit to the left and add the current node's value
        num = (num << 1) | head.val
        # Move to the next node in the list
        head = head.next

    # Return the final decimal value
    return num

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Q45():
    st.title("Minimum Number of Movies to Seat Everyone")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/minimum-number-of-movies-to-seat-everyone/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You have n friends, each of them will be seated in a movie theater. Given the maximum capacity of the theater and the list of friends' group sizes, return the minimum number of movies needed to seat all friends.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: groups = [1, 2, 3], capacity = 4\n
            - Output: 2\n
            - Explanation: First movie seats 1 and 3, second movie seats 2.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: groups = [4, 5, 1, 1], capacity = 6\n
            - Output: 3
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: groups = [10, 20, 30], capacity = 25\n
            - Output: 3
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= groups.length <= 1000\n
            - 1 <= groups[i] <= 100
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Greedy**
            - **Sorting**
            - **Array**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def min_movies(groups, capacity):
    # Your code goes here
    pass
            """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[1, 2, 3], 4], "expected": 2},
                {"input": [[4, 5, 1, 1], 6], "expected": 2},
                {"input": [[6, 5, 1, 7], 8], "expected": 3}
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: groups = {case['input'][0]}, capacity = {case['input'][1]}")
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

                        # Check if the function min_movies is defined
                        if "min_movies" in user_namespace:
                            min_movies = user_namespace['min_movies']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = min_movies(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function min_movies not defined. Please define the function to proceed.")
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
def min_movies(groups, capacity):
    # Sort the groups in ascending order to fit smaller groups first
    groups.sort()
    # Initialize a counter for the number of movies required
    movies = 0

    # Loop until all groups are accommodated
    while groups:
        # Set the remaining capacity for the current movie
        remaining_capacity = capacity

        # Check each group in a copy of the list (to allow removal)
        for group in groups[:]:
            # If the group fits within the remaining capacity
            if group <= remaining_capacity:
                # Deduct the group size from the remaining capacity
                remaining_capacity -= group
                # Remove the group from the original list as it is now accommodated
                groups.remove(group)
        
        # Increment the movie count after each round of seating groups
        movies += 1

    # Return the total number of movies required to accommodate all groups
    return movies

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")




def Q46():
    st.title("How Many Numbers are Smaller than the Current Number")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer array nums, for each element nums[i], return how many numbers are smaller than it in the array.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [8, 1, 2, 2, 3]\n
            - Output: [4, 0, 1, 1, 3]\n
            - Explanation: For each element in the array, the output represents how many numbers are smaller than it.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [1, 2, 3, 4]\n
            - Output: [0, 1, 2, 3]
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [10, 10, 10, 10]\n
            - Output: [0, 0, 0, 0]
        """)

    st.write("""
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= nums.length <= 100\n
            - 0 <= nums[i] <= 100\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Sorting**
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
            value="""def smallerNumbersThanCurrent(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[8, 1, 2, 2, 3]], "expected": [4, 0, 1, 1, 3]},
                {"input": [[1, 2, 3, 4]], "expected": [0, 1, 2, 3]},
                {"input": [[3, 4, 5, 7, 9]], "expected":  [0, 1, 2, 3, 4]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: nums = {case['input'][0]}")
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

                        # Check if the function smallerNumbersThanCurrent is defined
                        if "smallerNumbersThanCurrent" in user_namespace:
                            smallerNumbersThanCurrent = user_namespace['smallerNumbersThanCurrent']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = smallerNumbersThanCurrent(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function smallerNumbersThanCurrent not defined. Please define the function to proceed.")
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
def smallerNumbersThanCurrent(nums):
    # Initialize an empty list to store the results
    lis = []
    
    # Iterate over each element in the 'nums' list
    for i in range(len(nums)):
        count = 0  # Initialize a counter to keep track of how many numbers are smaller than the current number
        
        # Compare the current number (nums[i]) with every other number (nums[j]) in the list
        for j in range(len(nums)):
            # If nums[i] is greater than nums[j] (and they are not the same number)
            if nums[i] != nums[j] and nums[i] > nums[j]:
                count += 1  # Increment the count for each smaller number found
        
        # Append the count for the current number to the 'lis' list
        lis.append(count)
    
    # Return the final list containing the count of smaller numbers for each element in 'nums'
    return lis

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")




def Q47():
    st.title("Running Sum of 1d Array")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/running-sum-of-1d-array/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an array nums, return the running sum of the array.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [1, 2, 3, 4]\n
            - Output: [1, 3, 6, 10]\n
            - Explanation: The running sum is calculated by accumulating the sum of elements as we go through the array.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [1, 1, 1]\n
            - Output: [1, 2, 3]
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [3, 1, 2, 10]\n
            - Output: [3, 4, 6, 16]
        """)

    st.write("""
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= nums.length <= 1000\n
            - -10^6 <= nums[i] <= 10^6
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Array**
            - **Prefix Sum**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def running_sum(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[1, 2, 3, 4]], "expected": [1, 3, 6, 10]},
                {"input": [[1, 1, 1]], "expected": [1, 2, 3]},
                {"input": [[3, 1, 2, 10]], "expected": [3, 4, 6, 16]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: nums = {case['input'][0]}")
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

                        # Check if the function running_sum is defined
                        if "running_sum" in exec_globals:
                            running_sum = exec_globals['running_sum']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = running_sum(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function running_sum not defined. Please define the function to proceed.")
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
def running_sum(nums):
    # Initialize the list with the first element of nums
    lis = [nums[0]]
    
    # Start with the sum equal to the first element of nums
    sum_ = nums[0]
    
    # Iterate through the remaining elements of nums
    for i in range(1, len(nums)):
        # Add the current element to the sum
        sum_ += nums[i]
        
        # Append the current running sum to the list
        lis.append(sum_)
    
    # Return the list containing the running sum
    return lis

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")




def Q48():
    st.title("Apply Transform Over Each Element in Array")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    with col1:
        st.write("""
            **Problem**: Given an array nums, apply the transformation arr[i] = arr[i] * 2 + 3 for each element and return the new array.
            \n
        """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [1, 2, 3]\n
            - Output: [5, 7, 9]\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [0]\n
            - Output: [3]
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [-1, 0, 1]\n
            - Output: [1, 3, 5]
        """)

    st.write("""
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= nums.length <= 1000\n
            - -100 <= nums[i] <= 100\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
            - **Arrays**
            - **List Comprehension**
        """)

    # Columns for solving the problem
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Display a code editor for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def transform_array(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[1, 2, 3]], "expected": [5, 7, 9]},
                {"input": [[0]], "expected": [3]},
                {"input": [[-1, 0, 1]], "expected": [1, 3, 5]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: nums = {case['input'][0]}")
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

                        # Check if the function transform_array is defined
                        if "transform_array" in exec_globals:
                            transform_array = exec_globals['transform_array']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = transform_array(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function transform_array not defined. Please define the function to proceed.")
                except Exception as e:
                    # Display the error at the bottom of all expanders
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: every question has different solutions)", expanded=False):
            st.code(""" 
def transform_array(nums):
    return [num * 2 + 3 for num in nums]
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")



def Q49():
    st.title("Convert The Temperature")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/convert-the-temperature/) for more details.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given a temperature in Celsius, return it in both Celsius and Fahrenheit.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: celsius = 36.50\n
            - Output: [36.50, 97.70]\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: celsius = 0\n
            - Output: [0, 32]\n
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: celsius = -40\n
            - Output: [-40, -40]\n
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - -100 <= celsius <= 1000\n
        """)

    # Topics section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("""
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
            value="""def convert_temperature(celsius):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [36.50], "expected": [36.50, 97.70]},
                {"input": [0], "expected": [0, 32]},
                {"input": [-40], "expected": [-40, -40]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: celsius = {case['input'][0]}")
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

                        # Check if the function convert_temperature is defined
                        if "convert_temperature" in user_namespace:
                            convert_temperature = user_namespace['convert_temperature']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = convert_temperature(input_val[0])
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function convert_temperature not defined. Please define the function to proceed.")
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
def convert_temperature(celsius):
    return [celsius, celsius * 9 / 5 + 32]
            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/41.png")


def Q50():
    st.title("Remove Vowels from a String")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/remove-vowels-from-a-string/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given a string s, return the string after removing all vowels.
        \n
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: s = 'leetcode'\n
            - Output: 'ltcd'\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: s = 'hello'\n
            - Output: 'hll'\n
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: s = 'aeiou'\n
            - Output: ''\n
        """)

    st.write("""
        \n
        **Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)

    with colc:
        st.write("""
            - 1 <= s.length <= 100\n
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
                    st.write(f"- Input: '{case['input'][0]}'")
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
    # Define a string containing all vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Initialize an empty list to store characters that are not vowels
    result = []
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is not a vowel, append it to the result list
        if char not in vowels:
            result.append(char)
    
    # Join the characters in the result list into a string and return it
    return ''.join(result)

            """)

    # Right column: Flowchart of the sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/51.png")


