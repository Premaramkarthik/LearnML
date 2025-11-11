import streamlit as st
import io
import contextlib
# CSS for styling



def Q31():
    st.title("31. Sorted Squares of an Array")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/squares-of-a-sorted-array/) for a better experience.")

    st.write("""
        **Problem**: Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number, sorted in non-decreasing order.
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `nums = [-4,-1,0,3,10]`
            - Output: `[0, 1, 9, 16, 100]`
            - Explanation: After squaring each number, the sorted squares are `[0, 1, 9, 16, 100]`.
        """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `nums = [-7,-3,2,3,11]`
            - Output: `[4, 9, 9, 49, 121]`
            - Explanation: After squaring each number, the sorted squares are `[4, 9, 9, 49, 121]`.
        """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= nums.length <= 10^4`")

    with colc1:
        st.write("- `-10^4 <= nums[i] <= 10^4`")

    with colc2:
        st.write("- `nums` is sorted in non-decreasing order.")

    # Follow-up Section
    st.write("""
        **Follow-up**: Can you optimize the solution to use less space?
    """)

    # Topics Section
    st.write("#### Topics")
    colt, colt1 = st.columns([5, 10])

    with colt:
        st.write("""
            - **Array Manipulation**
        """)
    with colt1:
        st.write("""
            - **Sorting**
        """)

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sortedSquares(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ([-4, -1, 0, 3, 10],), "expected": [0, 1, 9, 16, 100]},
                {"input": ([-7, -3, 2, 3, 11],), "expected": [4, 9, 9, 49, 121]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `sortedSquares` is defined
                        if "sortedSquares" in user_namespace:
                            sortedSquares = user_namespace['sortedSquares']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sortedSquares(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `sortedSquares` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def sortedSquares(nums):
    # Initialize two pointers: one at the beginning and one at the end of the list
    left, right = 0, len(nums) - 1
    # Initialize an empty list to store the squares of the numbers
    result = []
    
    # While the left pointer is less than or equal to the right pointer
    while left <= right:
        # Compare the absolute values of the numbers at the left and right pointers
        if abs(nums[left]) > abs(nums[right]):
            # If the left number's absolute value is greater, square it and add to the result list
            result.append(nums[left] ** 2)
            # Move the left pointer to the right
            left += 1
        else:
            # If the right number's absolute value is greater or equal, square it and add to the result list
            result.append(nums[right] ** 2)
            # Move the right pointer to the left
            right -= 1
    
    # Return the result list, reversed to make sure the squares are sorted
    return result[::-1]

            """,)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/31.png")

def Q32():
    st.title("32. Three Consecutive Odds")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/three-consecutive-odds/description/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    with col1:
        st.write("""
            **Problem**: Given an integer array `arr`, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
        """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `arr = [2, 6, 4, 1]`
            - Output: `false`
            - Explanation: There are no three consecutive odds.
        """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]`
            - Output: `true`
            - Explanation: [5, 7, 23] are three consecutive odds.
        """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= arr.length <= 1000`")

    with colc1:
        st.write("- `1 <= arr[i] <= 1000`")

    with colc2:
        st.write("- Check for three consecutive odd numbers in the array.")

    # Follow-up Section
    st.write("""
        **Follow-up**: Can you optimize the solution to check the array in fewer iterations?
    """)

    # Topics Section
    st.write("#### Topics")
    colt,  = st.columns(1)

    with colt:
        st.write("""
            - **Array Manipulation**
        """)
   

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def three_consecutive_odds(arr):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ([2, 6, 4, 1],), "expected": False},
                {"input": ([1, 2, 34, 3, 4, 5, 7, 23, 12],), "expected": True},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `three_consecutive_odds` is defined
                        if "three_consecutive_odds" in user_namespace:
                            three_consecutive_odds = user_namespace['three_consecutive_odds']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = three_consecutive_odds(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `three_consecutive_odds` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def three_consecutive_odds(arr):
    # Initialize a counter to keep track of consecutive odd numbers
    counter = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element is odd
        if arr[i] % 2 != 0:
            # Increment the counter if it's an odd number
            counter += 1
            
            # If three consecutive odd numbers are found, return True
            if counter == 3:
                return True
        else:
            # Reset the counter if the current number is not odd
            counter = 0
    
    # Return False if no three consecutive odd numbers are found
    return False

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/32.png")  # Update with the correct path if needed

def Q33():
    st.title("1002. Find Common Characters")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/find-common-characters/description/) for a better experience.")

    st.write("""
        **Problem**: Given a string array `words`, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `words = ["bella","label","roller"]`
            - Output: `["e","l","l"]`
        """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `words = ["cool","lock","cook"]`
            - Output: `["c","o"]`
        """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= words.length <= 100`")

    with colc1:
        st.write("- `1 <= words[i].length <= 100`")

    with colc2:
        st.write("- `words[i]` consists of lowercase English letters.")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
        - **Array**
        - **Hash Table**
        - **String**
    """)

    

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def common_chars(words):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ["bella", "label", "roller"], "expected": ["e", "l", "l"]},
                {"input": ["cool", "lock", "cook"], "expected": ["c", "o"]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `common_chars` is defined
                        if "common_chars" in user_namespace:
                            common_chars = user_namespace['common_chars']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = common_chars(input_val)
                                    if sorted(result) == sorted(expected_val):  # Sorting to compare unordered outputs
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `common_chars` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
from collections import Counter

def common_chars(words):
    # Initialize the counter with the character counts from the first word
    cnt = Counter(words[0])
    
    # Iterate through the remaining words in the list
    for w in words:
        # Get the character counts for the current word
        cur_cnt = Counter(w)
        
        # Update the count of each character in 'cnt' to be the minimum 
        # between the previous count and the current word's count
        for c in cnt:
            cnt[c] = min(cnt[c], cur_cnt[c])

    # Initialize a list to store the common characters
    res = []
    
    # Append each character to the result list based on its count
    for c in cnt:
        for i in range(cnt[c]):
            res.append(c)
    
    # Return the list of common characters
    return res

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/33.png")  # Update with the correct path if needed


def Q34():
    st.title("1232. Check If It Is a Straight Line")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/check-if-it-is-a-straight-line/description/) for better experience.")


    st.write("""
        **Problem**: You are given an array `coordinates`, where `coordinates[i] = [x, y]`, represents the coordinate of a point. Check if these points make a straight line in the XY plane.
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
            - Output: `true`
            - Explanation: The points form a straight line in the XY plane.
        """)
        st.image("pages/images/easy/1232_ques.jpg", caption="Points forming a straight line", width=250)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
            - Output: `false`
            - Explanation: The points do not form a straight line in the XY plane.
        """)
        st.image("pages/images/easy/1232_ques_2jpg.jpg", caption="Points not forming a straight line", width=250)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `2 <= coordinates.length <= 1000`")

    with colc1:
        st.write("- `coordinates[i].length == 2`")

    with colc2:
        st.write("- `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4`")
    
    st.write("- `coordinates` contains no duplicate point.")

    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: If there're only 2 points, return true.
    """)
    st.write("""
        **Hint 2**: Check if all other points lie on the line defined by the first 2 points.
    """)
    st.write("""
        **Hint 3**: Use cross product to check collinearity.
    """)

    # Topics Section
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write(""" 
            - **Geometry**
        """)
    with colt1:
        st.write(""" 
            - **Mathematics**
        """)

        
                

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def checkStraightLine(coordinates):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], "expected": True},
                {"input": [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], "expected": False},
                {"input": [[0, 0], [1, 1], [2, 2]], "expected": True},
                {"input": [[1, 1], [2, 2], [3, 3], [4, 5]], "expected": False},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `checkStraightLine` is defined
                        if "checkStraightLine" in user_namespace:
                            checkStraightLine = user_namespace['checkStraightLine']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = checkStraightLine(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `checkStraightLine` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def checkStraightLine(coordinates):
    # Get the first two points from the list of coordinates
    (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
    
    # Iterate through the remaining points starting from the third point
    for x3, y3 in coordinates[2:]:
        # Check if the slope between (x1, y1) and (x2, y2) is equal to the slope between (x1, y1) and (x3, y3)
        # The slopes are equivalent if the cross multiplication holds true:
        # (y2 - y1) / (x2 - x1) == (y3 - y1) / (x3 - x1)
        # Which is the same as: (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)
        if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
            return False  # If the slopes are not equal, return False (not a straight line)
    
    # If all points satisfy the condition, return True (points are collinear)
    return True

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/34.png")  # Update with the correct path if needed


def Q35():
    st.title("1313. Decompress Run-Length Encoded List")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/decompress-run-length-encoded-list/description/) for better experience.")

    # Create two columns: left for question, right for code input

    st.write("""
        **Problem**: We are given a list `nums` of integers representing a list compressed with run-length encoding.
        
        Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`). For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
        
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
           **Example 1**:
            - Input: `nums = [1, 2, 3, 4]`
            - Output: `[2, 4, 4, 4]`
            - Explanation: The first pair `[1, 2]` means we have `freq = 1` and `val = 2`, so we generate the array `[2]`. The second pair `[3, 4]` means we have `freq = 3` and `val = 4`, so we generate `[4, 4, 4]`. At the end, the concatenation `[2] + [4, 4, 4]` is `[2, 4, 4, 4]`.
        """)
       
    with col2:
        st.write("""
            **Example 2**:
            - Input: `nums = [1, 1, 2, 3]`
            - Output: `[1, 3, 3]`
        """)
       
    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- 2 <= nums.length <= 100")

    with colc1:
        st.write("- `nums.length % 2 == 0`")

    with colc2:
        st.write("- 1 <= `nums[i] <= 100`")

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: If there're only 2 points, return true.
    """)
    st.write("""
        **Hint 2**: Check if all other points lie on the line defined by the first 2 points.
    """)
    st.write("""
        **Hint 3**: Use cross product to check collinearity.
    """)

    # Topics Section
    st.write("#### Topics")
   
    st.write(""" 
        - **Array**
    """)

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def decompressRLElist(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 2, 3, 4], "expected": [2, 4, 4, 4]},
                {"input": [1, 1, 2, 3], "expected": [1, 3, 3]},
                {"input": [2, 5, 3, 1], "expected": [5, 5, 1, 1, 1]},
                {"input": [4, 2, 1, 3], "expected": [2, 2, 2, 2, 3]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `decompressRLElist` is defined
                        if "decompressRLElist" in user_namespace:
                            decompressRLElist = user_namespace['decompressRLElist']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = decompressRLElist(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `decompressRLElist` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def decompressRLElist(nums):
    # Get the length of the input list
    n = len(nums)
    # Initialize an empty list to store the decompressed result
    res = []
    
    # Iterate through the list in steps of 2, as each pair (freq, val) is processed together
    for i in range(0, n, 2):
        # The frequency is the first element of the pair
        freq = nums[i]
        # The value to be repeated is the second element of the pair
        val = nums[i + 1]
        
        # Append 'val' to 'res' 'freq' number of times
        while freq:
            res.append(val)
            freq -= 1  # Decrease the frequency count by 1 each iteration
    
    # Return the fully decompressed list
    return res

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/35.png")  # Update with the correct path if needed


def Q36():
    st.title("36. How Many Numbers Are Smaller Than the Current Number")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/) for better experience.")


    st.write("""
        **Problem**: Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` and `nums[j] < nums[i]`.
        **Return the answer in an array.**
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
           **Example 1**:
            - Input: `nums = [8, 1, 2, 2, 3]`
            - Output: `[4, 0, 1, 1, 3]`
            - Explanation: 
              - For `nums[0]=8` there exist four smaller numbers than it (1, 2, 2, and 3). 
              - For `nums[1]=1` there does not exist any smaller number than it.
              - For `nums[2]=2` there exists one smaller number than it (1). 
              - For `nums[3]=2` there exists one smaller number than it (1). 
              - For `nums[4]=3` there exist three smaller numbers than it (1, 2, and 2).
            """)
        

    with col2:
        st.write("""
            **Example 2**:
            - Input: `nums = [6, 5, 4, 8]`
            - Output: `[2, 1, 0, 3]`
            **Example 3**:
            - Input: `nums = [7, 7, 7, 7]`
            - Output: `[0, 0, 0, 0]`
            **Constraints**:
            - 2 <= nums.length <= 500
            - 0 <= nums[i] <= 100
         """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1 = st.columns([1,5])
    with colc:
        st.write("- 2 <= nums.length <= 500")

    with colc1:
        st.write("- 0 <= nums[i] <= 100")

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: In order to improve the time complexity, we can sort the array and get the answer for each array element..
    """)
    st.write("""
        **Hint 2**: Brute force for each array element.
    """)

    # Topics Section
    st.write("#### Topics")
    colt , colt1, colt2, colt3   = st.columns(4)

    with colt:
        st.write(""" 
            - **Array**
        """)
 
    with colt:
        st.write(""" 
            - **Hash Table**
        """)
    
    with colt:
        st.write(""" 
            - **Sorting**
        """)
    
    with colt:
        st.write(""" 
            - **Counting**
        """)
    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

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
                {"input": [8, 1, 2, 2, 3], "expected": [4, 0, 1, 1, 3]},
                 {"input": [6, 5, 4, 8], "expected": [2, 1, 0, 3]},
                 {"input": [7, 7, 7, 7], "expected": [0, 0, 0, 0]},
                {"input": [1, 2, 3, 4, 5], "expected": [0, 1, 2, 3, 4]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `smallerNumbersThanCurrent` is defined
                        if "smallerNumbersThanCurrent" in user_namespace:
                            smallerNumbersThanCurrent = user_namespace['smallerNumbersThanCurrent']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = smallerNumbersThanCurrent(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `smallerNumbersThanCurrent` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
        def smallerNumbersThanCurrent(nums):
    # Create a sorted version of the input list
    arr = sorted(nums)
    # Initialize an empty dictionary to store the first occurrence index of each number in the sorted list
    d = {}
    
    # Iterate through the sorted list and store the index of each unique number
    for i in range(len(arr)):
        if not arr[i] in d:
            d[arr[i]] = i  # Store the index only if the number is not already in the dictionary
    
    # Initialize an empty list to store the result
    res = []
    # Iterate through the original list and use the dictionary to find how many numbers are smaller
    for i in range(len(nums)):
        res.append(d[nums[i]])  # Append the index from the dictionary, which represents the count of smaller numbers
    
    # Return the result list
    return res


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/36.png")  # Update with the correct path if needed


def Q37():
    st.title("37. Create Target Array in the Given Order")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/create-target-array-in-the-given-order/description/) for better experience.")


    st.write("""
            **Problem**: Given two arrays of integers `nums` and `index`, your task is to create a target array under the following rules:
            - Initially, the target array is empty.
            - From left to right, read `nums[i]` and `index[i]`, inserting the value `nums[i]` at index `index[i]` in the target array.
            - Repeat until there are no elements to read in `nums` and `index`.
            - Return the target array.
            It is guaranteed that the insertion operations will be valid.
    """)

    # Examples Section with two columns
    col1, col2, col3  = st.columns(3)

    with col1:
        st.write("""
          **Example 1**:
            - Input: `nums = [0, 1, 2, 3, 4]`, `index = [0, 1, 2, 2, 1]`
            - Output: `[0, 4, 1, 3, 2]`
            - Explanation:
            ```
            nums       index     target
            0            0        [0]
            1            1        [0, 1]
            2            2        [0, 1, 2]
            3            2        [0, 1, 3, 2]
            4            1        [0, 4, 1, 3, 2]
            ```
            """)
        

    with col2:
        st.write("""
           **Example 2**:
            - Input: `nums = [1, 2, 3, 4, 0]`, `index = [0, 1, 2, 3, 0]`
            - Output: `[0, 1, 2, 3, 4]`
            - Explanation:
            ```
            nums       index     target
            1            0        [1]
            2            1        [1, 2]
            3            2        [1, 2, 3]
            4            3        [1, 2, 3, 4]
            0            0        [0, 1, 2, 3, 4]
            ```
            """)
    
    with col3:
        st.write("""
            **Example 3**:
            - Input: `nums = [1]`, `index = [0]`
            - Output: `[1]`
                 """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= nums.length, index.length <= 100`")

    with colc1:
        st.write("- `nums.length == index.length`")
        
    with colc2:
        st.write("- `0 <= nums[i] <= 100")
    
    with colc3:
        st.write("- `0 <= index[i] <= i`")
        

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: Simulate the process and fill corresponding numbers in the designated spots.""")

    # Topics Section
    st.write("#### Topics")
    colt , colt1,    = st.columns(2)

    with colt:
        st.write(""" 
            - **Array**
        """)
 
    with colt:
        st.write(""" 
            - **Insertion**
        """)
    

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def countGoodTriplets(nums, index):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
            {"input": ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]), "expected": [0, 4, 1, 3, 2]},
            {"input": ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]), "expected": [0, 1, 2, 3, 4]},
            {"input": ([1], [0]), "expected": [1]},
            {"input": ([2, 3, 4], [0, 0, 1]), "expected": [3, 4, 2]},
            ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `countGoodTriplets` is defined
                        if "countGoodTriplets" in user_namespace:
                            countGoodTriplets = user_namespace['countGoodTriplets']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = countGoodTriplets(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `countGoodTriplets` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def countGoodTriplets(nums, index):
    # Initialize an empty list to store the target array
    arr = []
    
    # Iterate through pairs of elements from nums and index
    for n, i in zip(nums, index):
        # Insert each element 'n' at the position 'i' in the array
        arr.insert(i, n)
    
    # Return the constructed target array
    return arr

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/37.png")  # Update with the correct path if needed


def Q38():
    st.title("38. Check if the Sentence Is Pangram")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/) for better experience.")


    st.write("""
           **Problem**: A pangram is a sentence where every letter of the English alphabet appears at least once.
            Given a string `sentence` containing only lowercase English letters, return `true` if the sentence is a pangram, or `false` otherwise.
    """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
         **Example 1**:
            - Input: `sentence = "thequickbrownfoxjumpsoverthelazydog"`
            - Output: `true`
            - Explanation: The sentence contains at least one of every letter of the English alphabet.
             """)
        

    with col2:
        st.write("""
          **Example 2**:
            - Input: `sentence = "leetcode"`
            - Output: `false`
            """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= sentence.length <= 1000`")

    with colc1:
        st.write("- `sentence` consists of lowercase English letters.`")
        

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: Iterate over the string and mark each character as found (using a boolean array, bitmask, or any other similar way)""")
    
    st.write("""
        **Hint 2**: Check if the number of found characters equals the alphabet length.""")  
    # Topics Section
    st.write("#### Topics")
    colt , colt1,    = st.columns(2)

    with colt:
        st.write(""" 
            - **String**
        """)
 
    with colt1:
        st.write(""" 
            - **Hash Table**
        """)
    

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def countGoodTriplets(sentence):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": "thequickbrownfoxjumpsoverthelazydog", "expected": True},
                {"input": "leetcode", "expected": False},
                {"input": "abcdefghijklmnopqrstuvwxyz", "expected": True},
                {"input": "hello world", "expected": False},
                ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `countGoodTriplets` is defined
                        if "countGoodTriplets" in user_namespace:
                            countGoodTriplets = user_namespace['countGoodTriplets']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = countGoodTriplets(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `countGoodTriplets` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def countGoodTriplets(sentence):
    # Convert the sentence to lowercase (though this is not necessary as we're not modifying the original string)
    sentence.lower()
    
    # Iterate over the ASCII values for lowercase English letters (97 = 'a', 122 = 'z')
    for i in range(97, 123):
        # Check if the current letter (converted using chr(i)) is not in the sentence
        if chr(i) not in sentence:
            return False  # If any letter is missing, return False immediately
    
    # If all letters are present, return True
    return True


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/38.png")  # Update with the correct path if needed


def Q39():
    st.title("39. Maximum Product Difference Between Two Pairs")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/) for a better experience.")


    st.write("""
           **Problem**: The product difference between two pairs `(a, b)` and `(c, d)` is defined as `(a * b) - (c * d)`.
            Given an integer array `nums`, choose four distinct indices `w`, `x`, `y`, and `z` such that the product difference between pairs `(nums[w], nums[x])` and `(nums[y], nums[z])` is maximized.
            Return the maximum such product difference. """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
          **Example 1**:
            - Input: `nums = [5,6,2,7,4]`
            - Output: `34`
            - Explanation: We can choose indices `1` and `3` for the first pair `(6, 7)` and indices `2` and `4` for the second pair `(2, 4)`. The product difference is `(6 * 7) - (2 * 4) = 34`.
            """)
        

    with col2:
        st.write("""
         **Example 2**:
            - Input: `nums = [4,2,5,9,7,4,8]`
            - Output: `64`
            - Explanation: We can choose indices `3` and `6` for the first pair `(9, 8)` and indices `1` and `5` for the second pair `(2, 4)`. The product difference is `(9 * 8) - (2 * 4) = 64`.
            """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `4 <= nums.length <= 10^4`")

    with colc1:
        st.write("- `1 <= nums[i] <= 10^4`")
        

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: If you only had to find the maximum product of 2 numbers in an array, which 2 numbers should you choose?""")
    
    st.write("""
        **Hint 2**: We only need to worry about 4 numbers in the array.""")  
    # Topics Section
    st.write("#### Topics")
  
    colt , colt1,  colt3  = st.columns(3)

    with colt:
        st.write(""" 
            - **Array**
        """)
 
    with colt1:
        st.write(""" 
            - **Mathematics**
        """)
        
    with colt3:
        st.write(""" 
            - **Sorting**
        """)
    
    

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def countGoodTriplets(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
            {"input": [5, 6, 2, 7, 4], "expected": 34},
            {"input": [4, 2, 5, 9, 7, 4, 8], "expected": 64},
                ]

            # Display the test cases in expanders and create placeholders for results
            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

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
                        exec(code_input, user_namespace)

                        # Check if the function `countGoodTriplets` is defined
                        if "countGoodTriplets" in user_namespace:
                            countGoodTriplets = user_namespace['countGoodTriplets']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = countGoodTriplets(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `countGoodTriplets` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def countGoodTriplets(nums):
    # Initialize variables to track the two largest and two smallest numbers
    max1, max2, min1, min2 = 0, 0, 10001, 10001
    
    # Iterate through each number in the list
    for n in nums:
        # Update the two largest numbers (max1 is the largest, max2 is the second largest)
        if n > max1:
            max2, max1 = max1, n  # max2 becomes the old max1, max1 is updated to the new number
        elif n > max2:
            max2 = n  # Only update max2 if the number is larger than the current max2
        
        # Update the two smallest numbers (min1 is the smallest, min2 is the second smallest)
        if n < min1:
            min2, min1 = min1, n  # min2 becomes the old min1, min1 is updated to the new number
        elif n < min2:
            min2 = n  # Only update min2 if the number is smaller than the current min2
    
    # Calculate and return the difference between the product of the two largest and two smallest numbers
    return (max1 * max2) - (min1 * min2)


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/39.png")  # Update with the correct path if needed


def Q40():
    st.title("40. Count Good Triplets")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/count-good-triplets/description/) for a better experience.")


    st.write("""
           **Problem**: Given an array of integers `arr`, and three integers `a`, `b`, and `c`, 
            you need to find the number of good triplets. A triplet `(arr[i], arr[j], arr[k])` is good 
            if the following conditions are true:
            - `0 <= i < j < k < arr.length`
            - `|arr[i] - arr[j]| <= a`
            - `|arr[j] - arr[k]| <= b`
            - `|arr[i] - arr[k]| <= c`
            
            Where `|x|` denotes the absolute value of `x`. Return the number of good triplets.
            """)

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3`
            - Output: `4`
            - Explanation: There are 4 good triplets: `[(3,0,1), (3,0,1), (3,1,1), (0,1,1)]`.
           """)
        

    with col2:
        st.write("""
         **Example 2**:
            - Input: `arr = [1,1,2,2,3], a = 0, b = 0, c = 1`
            - Output: `0`
            - Explanation: No triplet satisfies all conditions.
            """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc3 = st.columns(3)
    with colc:
        st.write("- `3 <= arr.length <= 100`")

    with colc1:
        st.write("- `0 <= arr[i] <= 1000`")
    
    with colc3:
        st.write("- `0 <= a, b, c <= 1000`")
        

    st.write("**Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: Notice that the constraints are small enough for a brute force solution to pass.""")
    
    st.write("""
        **Hint 2**: Loop through all triplets, and count the ones that are good.""")  
    # Topics Section
    st.write("#### Topics")
  
    colt , colt1  = st.columns([1,16])

    with colt:
        st.write(""" 
            - **Array**
        """)
 
    with colt1:
        st.write(""" 
            - **Enumeration**
        """)
        

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def countGoodTriplets(arr, a, b, c):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

    
        # Define the test cases
        test_cases = [
            {"input": ([3, 0, 1, 1, 9, 7], 7, 2, 3), "expected": 4},
            {"input": ([1, 1, 2, 2, 3], 0, 0, 1), "expected": 0},
            {"input": ([1, 2, 3], 2, 2, 2), "expected": 1},
            {"input": ([1, 5, 2, 4, 3], 3, 1, 2), "expected": 5},
        ]

        # Initialize placeholders for test results
        result_placeholders = []
        error_placeholder = st.empty()

        # Create columns for layout (colTest, colRun)

        with colTest:
            # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")

                # Create a placeholder for each result
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

        # Button to execute the code and handle output
        with colRun:
            if st.button("Run Code"):
                # Capture output
                buffer = io.StringIO()

                try:
                    # Safely execute user code
                    with contextlib.redirect_stdout(buffer):
                        # Assume the user has input their code in 'code_input' (this variable should be defined elsewhere)
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute user code in the provided context

                        # Check if 'countGoodTriplets' is in the user namespace
                        if "countGoodTriplets" in user_namespace:
                            countGoodTriplets = user_namespace["countGoodTriplets"]

                            # Run the function on each test case and check results
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = countGoodTriplets(*input_val)  # Pass input correctly
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `countGoodTriplets` not defined. Please define the function to proceed.")

                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                # Display execution output
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code(""" 
def countGoodTriplets(arr, a, b, c):
    # Initialize a counter to store the number of good triplets
    count = 0
    # Get the length of the array
    n = len(arr)
    
    # Iterate through each triplet (i, j, k) where i < j < k
    for i in range(n-2):
        for j in range(i+1, n-1):  # j must be greater than i
            # Check if the absolute difference between arr[i] and arr[j] is less than or equal to 'a'
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, n):  # k must be greater than j
                    # Check if the absolute difference between arr[j] and arr[k] is less than or equal to 'b'
                    # and if the absolute difference between arr[i] and arr[k] is less than or equal to 'c'
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1  # If all conditions are satisfied, increment the count
    
    # Return the total count of good triplets
    return count

            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/40.png")  # Update with the correct path if needed
