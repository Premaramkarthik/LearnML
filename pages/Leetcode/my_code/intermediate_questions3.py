import streamlit as st
import io
import contextlib



def Q21():
    st.title("21. Cells in a Range on an Excel Sheet") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

        - `<col>` denotes the column number `c` of the cell, represented by alphabetical letters.
        - For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
        - `<row>` is the row number `r` of the cell, represented by the integer `r`.
        
        You are given a string `s` in the format "<col1><row1>:<col2><row2>", where:
        
        - `<col1>` represents the column `c1`, `<row1>` represents the row `r1`,
        - `<col2>` represents the column `c2`, and `<row2>` represents the row `r2`,
        - such that `r1 <= r2` and `c1 <= c2`.

        **Return** the list of cells `(x, y)` such that `r1 <= x <= r2` and `c1 <= y <= c2`. 
        The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: s = "K1:L2"
                 - Output: ["K1","K2","L1","L2"]
                 - Explanation: 
                     - The above diagram shows the cells which should be present in the list.
                     - The red arrows denote the order in which the cells should be presented.
                 """)

    with col2:
        st.write("""
                 **Example 2**:
                 - Input: s = "A1:F1"
                 - Output: ["A1","B1","C1","D1","E1","F1"]
                 - Explanation:
                     - The above diagram shows the cells which should be present in the list.
                     - The red arrow denotes the order in which the cells should be presented.
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- s.length == 5")
        st.write("- 'A' <= s[0] <= s[3] <= 'Z'")
    with colc1:
        st.write("- '1' <= s[1] <= s[4] <= '9'")
        st.write("- s consists of uppercase English letters, digits, and ':'.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Grid Traversal**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def cells_in_range(s):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("K1:L2",), "expected": ["K1", "K2", "L1", "L2"]},
                {"input": ("A1:F1",), "expected": ["A1", "B1", "C1", "D1", "E1", "F1"]},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "cells_in_range" in user_namespace:
                            cells_in_range = user_namespace['cells_in_range']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = cells_in_range(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `cells_in_range` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def cells_in_range(s):
    # Extract the column and row details from the input string
    col1, row1, col2, row2 = s[0], s[1], s[3], s[4]
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the range of columns and rows
    for col in range(ord(col1), ord(col2) + 1):
        for row in range(int(row1), int(row2) + 1):
            # Add each cell in the range to the result list
            result.append(f"{chr(col)}{row}")
    
    # Return the list of cells in lexicographically sorted order
    return result
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/21.png")

def Q22():
    st.title("22. Sorting the Sentence") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sorting-the-sentence/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
        Each word consists of lowercase and uppercase English letters.
        
        A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
        
        For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
        
        **Given** a shuffled sentence `s` containing no more than 9 words, reconstruct and return the original sentence.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: s = "is2 sentence4 This1 a3"
                 - Output: "This is a sentence"
                 - Explanation: 
                     - Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: s = "Myself2 Me1 I4 and3"
                 - Output: "Me Myself and I"
                 - Explanation:
                     - Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 2 <= s.length <= 200")
        st.write("- s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.")
    with colc1:
        st.write("- The number of words in s is between 1 and 9.")
        st.write("- The words in s are separated by a single space.")
        st.write("- s contains no leading or trailing spaces.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Sorting**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sort_sentence(s):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("is2 sentence4 This1 a3",), "expected": "This is a sentence"},
                {"input": ("Myself2 Me1 I4 and3",), "expected": "Me Myself and I"},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "sort_sentence" in user_namespace:
                            sort_sentence = user_namespace['sort_sentence']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sort_sentence(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `sort_sentence` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def sort_sentence(s):
    # Split the input string into words
    words = s.split()
    
    # Sort the words based on the number in each word (using the number as a key for sorting)
    words.sort(key=lambda word: int([ch for ch in word if ch.isdigit()][0]))
    
    # Reconstruct the sentence by joining the words back together, removing the digits
    return ' '.join([word[:-1] for word in words])
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/22.png")


def Q23():
    st.title("23. Count Number of Pairs With Absolute Difference K") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer array `nums` and an integer `k`, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
        
        The value of |x| is defined as:
        - x if x >= 0.
        - -x if x < 0.
        
        **Return** the number of such pairs in the array.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: nums = [1,2,2,1], k = 1
                 - Output: 4
                 - Explanation: 
                     - The pairs with an absolute difference of 1 are:
                     - [1,2,2,1], [1,2,2,1], [1,2,2,1], [1,2,2,1]
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: nums = [1,3], k = 3
                 - Output: 0
                 - Explanation: 
                     - There are no pairs with an absolute difference of 3.
                 """)
        
    with col1:
        st.write("""
                 **Example 3**:
                 - Input: nums = [3,2,1,5,4], k = 2
                 - Output: 3
                 - Explanation: 
                     - The pairs with an absolute difference of 2 are:
                     - [3,2,1,5,4], [3,2,1,5,4], [3,2,1,5,4]
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= nums.length <= 200")
        st.write("- 1 <= nums[i] <= 100")
    with colc1:
        st.write("- 1 <= k <= 99")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **Hash Map**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def count_pairs_with_difference(nums, k):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ([1,2,2,1], 1), "expected": 4},
                {"input": ([1,3], 3), "expected": 0},
                {"input": ([3,2,1,5,4], 2), "expected": 3},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "count_pairs_with_difference" in user_namespace:
                            count_pairs_with_difference = user_namespace['count_pairs_with_difference']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = count_pairs_with_difference(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `count_pairs_with_difference` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def count_pairs_with_difference(nums, k):
    # Initialize a counter for the pairs
    count = 0
    
    # Use a dictionary to store the frequency of each number
    freq = {}
    
    # Iterate over each number in the list
    for num in nums:
        # Check if the complement (num - k) exists in the dictionary (for |num - complement| = k)
        if num - k in freq:
            count += freq[num - k]
        
        # Check if the complement (num + k) exists in the dictionary (for |num - complement| = k)
        if num + k in freq:
            count += freq[num + k]
        
        # Update the frequency dictionary for the current number
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Return the total count of pairs
    return count
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/23.png")


def Q24():
    st.title("24. To Lower Case") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/to-lower-case/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: s = "Hello"
                 - Output: "hello"
                 - Explanation: 
                     - Convert each uppercase letter to lowercase.
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: s = "here"
                 - Output: "here"
                 - Explanation: 
                     - The string is already in lowercase.
                 """)
        
    with col1:
        st.write("""
                 **Example 3**:
                 - Input: s = "LOVELY"
                 - Output: "lovely"
                 - Explanation: 
                     - Convert all uppercase letters to lowercase.
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= s.length <= 100")
    with colc1:
        st.write("- s consists of printable ASCII characters.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Lowercase Conversion**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def to_lower_case(s):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("Hello",), "expected": "hello"},
                {"input": ("here",), "expected": "here"},
                {"input": ("LOVELY",), "expected": "lovely"},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "to_lower_case" in user_namespace:
                            to_lower_case = user_namespace['to_lower_case']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = to_lower_case(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `to_lower_case` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def to_lower_case(s):
    # Use the built-in lower() method to convert the string to lowercase
    return s.lower()
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/24.png")


def Q25():
    st.title("25. Check if Number Has Equal Digit Count and Digit Value") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given a 0-indexed string `num` of length `n` consisting of digits.
        
        Return true if for every index `i` in the range 0 <= `i` < `n`, the digit `i` occurs `num[i]` times in `num`, otherwise return false.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: num = "1210"
                 - Output: true
                 - Explanation: 
                     - num[0] = '1'. The digit 0 occurs once in num.
                     - num[1] = '2'. The digit 1 occurs twice in num.
                     - num[2] = '1'. The digit 2 occurs once in num.
                     - num[3] = '0'. The digit 3 occurs zero times in num.
                     - The condition holds true for every index in "1210", so return true.
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: num = "030"
                 - Output: false
                 - Explanation: 
                     - num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
                     - num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
                     - num[2] = '0'. The digit 2 occurs zero times in num.
                     - The indices 0 and 1 both violate the condition, so return false.
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= n <= 10")
    with colc1:
        st.write("- num consists of digits.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Digit Count**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def digit_count_equal(num):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("1210",), "expected": True},
                {"input": ("030",), "expected": False},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "digit_count_equal" in user_namespace:
                            digit_count_equal = user_namespace['digit_count_equal']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = digit_count_equal(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `digit_count_equal` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def digit_count_equal(num):
    # Initialize a count list of size 10 to store the frequency of each digit (0-9)
    count = [0] * 10
    
    # Iterate over each digit in the string num
    for digit in num:
        count[int(digit)] += 1
    
    # Check if the digit at each index i matches the count of digit i in the number
    for i in range(len(num)):
        if count[i] != int(num[i]):
            return False
    
    # If all conditions hold true, return True
    return True
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/25.png")


def Q26():
    st.title("26. Count Asterisks") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/count-asterisks/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given a string `s`, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
        
        Return the number of '*' in `s`, excluding the '*' between each pair of '|'. Note that each '|' will belong to exactly one pair.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: s = "l|*e*et|c**o|*de|"
                 - Output: 2
                 - Explanation: 
                     - The characters between the first and second '|' are excluded from the answer.
                     - The characters between the third and fourth '|' are excluded from the answer.
                     - There are 2 asterisks considered. Therefore, we return 2.
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: s = "iamprogrammer"
                 - Output: 0
                 - Explanation: 
                     - In this example, there are no asterisks in `s`. Therefore, we return 0.
                 """)
        
    with col1:
        st.write("""
                 **Example 3**:
                 - Input: s = "yo|uar|e**|b|e***au|tifu|l"
                 - Output: 5
                 - Explanation: 
                     - There are 5 asterisks considered in the string.
                     - Therefore, we return 5.
                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= s.length <= 1000")
    with colc1:
        st.write("- s consists of lowercase English letters, vertical bars '|', and asterisks '*'.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Counting Asterisks**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def count_asterisks(s):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("l|*e*et|c**o|*de|",), "expected": 2},
                {"input": ("iamprogrammer",), "expected": 0},
                {"input": ("yo|uar|e**|b|e***au|tifu|l",), "expected": 5},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "count_asterisks" in user_namespace:
                            count_asterisks = user_namespace['count_asterisks']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = count_asterisks(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `count_asterisks` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def count_asterisks(s):
    # Initialize a counter for the asterisks
    asterisk_count = 0
    
    # Track whether we are inside a '|' pair or not
    inside_pipe = False
    
    # Iterate through each character in the string
    for char in s:
        # If we encounter a '|', toggle the state of inside_pipe
        if char == '|':
            inside_pipe = not inside_pipe
        # If we encounter an asterisk and we are not inside a '|' pair, count it
        elif char == '*' and not inside_pipe:
            asterisk_count += 1
    
    # Return the total count of asterisks
    return asterisk_count
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/26.png")

def Q27():
    st.title("27. Find Words That Can Be Formed by Characters") 

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given an array of strings `words` and a string `chars`.
        
        A string is good if it can be formed by characters from `chars` (each character can only be used once).
        
        Return the sum of lengths of all good strings in `words`.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
                 - Input: words = ["cat","bt","hat","tree"], chars = "atach"
                 - Output: 6
                 - Explanation: The strings that can be formed are "cat" and "hat", so the answer is 3 + 3 = 6.
                 """)
    
    with col2:
        st.write("""
                 **Example 2**:
                 - Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
                 - Output: 10
                 - Explanation: The strings that can be formed are "hello" and "world", so the answer is 5 + 5 = 10.
                 """)
        
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= words.length <= 1000")
    with colc1:
        st.write("- 1 <= words[i].length, chars.length <= 100")
    
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Character Counting**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def count_good_words(words, chars):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": (["cat","bt","hat","tree"], "atach"), "expected": 6},
                {"input": (["hello","world","leetcode"], "welldonehoneyr"), "expected": 10},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "count_good_words" in user_namespace:
                            count_good_words = user_namespace['count_good_words']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = count_good_words(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `count_good_words` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def count_good_words(words, chars):
    # Create a frequency count of characters in chars
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Initialize a variable to store the total length of good words
    total_length = 0
    
    # Iterate through each word in words
    for word in words:
        # Create a frequency count for the characters in the current word
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
        
        # Check if the current word can be formed from chars
        can_form = True
        for char, count in word_count.items():
            if char_count.get(char, 0) < count:
                can_form = False
                break
        
        # If the word can be formed, add its length to total_length
        if can_form:
            total_length += len(word)
    
    # Return the total length of good words
    return total_length
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/27.png")

def Q28():
    st.title("28. Jewels and Stones")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/jewels-and-stones/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You're given strings `jewels` representing the types of stones that are jewels,
        and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. 
        You want to know how many of the stones you have are also jewels.

        Letters are case sensitive, so "a" is considered a different type of stone from "A".
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: jewels = "aA", stones = "aAAbbbb"
                - Output: 3
                - Explanation: The stones "a", "A", and "A" are jewels, so the answer is 3.
                """)
    
    with col2:
        st.write("""
                **Example 2**:
                - Input: jewels = "z", stones = "ZZ"
                - Output: 0
                - Explanation: No stones in the input are jewels, so the answer is 0.
                """)
        
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= jewels.length, stones.length <= 50")
    with colc1:
        st.write("- jewels and stones consist of only English letters.")
    
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Character Matching**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def num_jewels_in_stones(jewels, stones):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("aA", "aAAbbbb"), "expected": 3},
                {"input": ("z", "ZZ"), "expected": 0},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "num_jewels_in_stones" in user_namespace:
                            num_jewels_in_stones = user_namespace['num_jewels_in_stones']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = num_jewels_in_stones(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `num_jewels_in_stones` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def num_jewels_in_stones(jewels, stones):
    # Convert jewels to a set for faster lookup
    jewels_set = set(jewels)
    
    # Initialize a counter for the number of jewels found in stones
    jewel_count = 0
    
    # Iterate through each stone in the stones string
    for stone in stones:
        # If the stone is in the jewels set, it's a jewel, so increment the counter
        if stone in jewels_set:
            jewel_count += 1
    
    # Return the total count of jewels found in the stones
    return jewel_count
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/28.png")



def Q29():
    st.title("29. Divide a String in Groups of Size k")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/divide-a-string-in-groups-of-size-k/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: A string `s` can be partitioned into groups of size `k` using the following procedure:
        
        The first group consists of the first `k` characters of the string, the second group consists of the next `k` characters, and so on. Each character can be a part of exactly one group.
        
        For the last group, if the string does not have `k` characters remaining, a `fill` character is used to complete the group.
        
        After removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be `s`.
        
        You are given a string `s`, the size of each group `k`, and the character `fill`. Your task is to return a list of strings representing each group.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: s = "abcdefghi", k = 3, fill = "x"
                - Output: ["abc", "def", "ghi"]
                - Explanation: The first 3 characters "abc" form the first group. The next 3 characters "def" form the second group. The last 3 characters "ghi" form the third group.
                """)
    
    with col2:
        st.write("""
                **Example 2**:
                - Input: s = "abcdefghij", k = 3, fill = "x"
                - Output: ["abc", "def", "ghi", "jxx"]
                - Explanation: Similar to the previous example, we form the first three groups "abc", "def", and "ghi". For the last group, we use "j" and add "x" twice to complete the group.
                """)
        
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= s.length <= 100")
    with colc1:
        st.write("- s consists of lowercase English letters only.")
    
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Group Division**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def divide_string_in_groups(s, k, fill):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("abcdefghi", 3, "x"), "expected": ["abc", "def", "ghi"]},
                {"input": ("abcdefghij", 3, "x"), "expected": ["abc", "def", "ghi", "jxx"]},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "divide_string_in_groups" in user_namespace:
                            divide_string_in_groups = user_namespace['divide_string_in_groups']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = divide_string_in_groups(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `divide_string_in_groups` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def divide_string_in_groups(s, k, fill):
    # Initialize a list to store the resulting groups
    groups = []
    
    # Iterate over the string `s` in steps of `k`
    for i in range(0, len(s), k):
        # Take a slice of the string `s` from index `i` to `i+k`
        group = s[i:i+k]
        
        # If the group is smaller than `k`, we need to pad it with the `fill` character
        if len(group) < k:
            group = group + fill * (k - len(group))
        
        # Append the completed group to the result list
        groups.append(group)
    
    # Return the list of groups
    return groups
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/29.png")


def Q30():
    st.title("30. Truncate Sentence")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/truncate-sentence/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: A sentence is a list of words separated by a single space with no leading or trailing spaces.
        Each word consists of only uppercase and lowercase English letters (no punctuation).
        
        You are given a sentence `s` and an integer `k`. You want to truncate `s` such that it contains only the 
        first `k` words. Return `s` after truncating it.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: s = "Hello how are you Contestant", k = 4
                - Output: "Hello how are you"
                - Explanation: The words in `s` are ["Hello", "how", "are", "you", "Contestant"]. The first 4 words are ["Hello", "how", "are", "you"].
                """)
    
    with col2:
        st.write("""
                **Example 2**:
                - Input: s = "What is the solution to this problem", k = 4
                - Output: "What is the solution"
                - Explanation: The words in `s` are ["What", "is", "the", "solution", "to", "this", "problem"]. The first 4 words are ["What", "is", "the", "solution"].
                """)
        
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= s.length <= 500")
    with colc1:
        st.write("- k is in the range [1, the number of words in `s`].")
    
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Word Processing**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def truncate_sentence(s, k):
# Your code goes here
pass
""")

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("Hello how are you Contestant", 4), "expected": "Hello how are you"},
                {"input": ("What is the solution to this problem", 4), "expected": "What is the solution"},
                {"input": ("chopper is not a tanuki", 5), "expected": "chopper is not a tanuki"},
            ]

            result_placeholders = []
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

            error_placeholder = st.empty()

        with colRun:
            if st.button("Run Code"):
                buffer = io.StringIO()

                try:
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)

                        if "truncate_sentence" in user_namespace:
                            truncate_sentence = user_namespace['truncate_sentence']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = truncate_sentence(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `truncate_sentence` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    # Sample answer with comments
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def truncate_sentence(s, k):
    # Split the sentence into a list of words
    words = s.split()
    
    # Get the first `k` words and join them back into a sentence
    truncated_sentence = ' '.join(words[:k])
    
    # Return the truncated sentence
    return truncated_sentence
""")

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/30.png")

