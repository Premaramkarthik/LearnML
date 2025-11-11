import streamlit as st
import io
import contextlib


def Q21():

    st.title("21. Maximum Value of a String in an Array")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: The value of an alphanumeric string can be defined as:
        - The numeric representation of the string in base 10, if it comprises of digits only.
        - The length of the string, otherwise.
        
        Given an array `strs` of alphanumeric strings, return the maximum value of any string in `strs`.
    """)

    # Create columns for examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input: strs = ["alic3", "bob", "3", "4", "00000"]
                - Output: 5
                - Explanation: "alic3" consists of both letters and digits, so its value is its length (5).
                "bob" consists only of letters, so its value is its length (3). 
                "3" and "4" are digits, so their values are their numeric equivalents (3 and 4).
                "00000" is a number but evaluates to 0. Maximum value is 5.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: strs = ["1", "01", "001", "0001"]
                - Output: 1
                - Explanation: Each string in the array has value 1, so we return 1.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= strs.length <= 100`")
    with colc1:
        st.write("- `1 <= strs[i].length <= 9`")
    with colc2:
        st.write("- `strs[i]` consists of only lowercase English letters and digits")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **String Manipulation**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def max_value(strs):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": (["alic3", "bob", "3", "4", "00000"],), "expected": 5},
                {"input": (["1", "01", "001", "0001"],), "expected": 1},
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

                        if "max_value" in user_namespace:
                            max_value = user_namespace['max_value']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = max_value(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `max_value` not defined. Please define the function to proceed.")
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
    def max_value(strs):
        # Initialize a variable to track the maximum value
        max_val = 0

        # Loop over each string in the input list
        for s in strs:
            # Check if the string is numeric
            if s.isdigit():
                # Convert to integer if numeric and get its value
                value = int(s)
            else:
                # Use the length of the string if it contains letters
                value = len(s)
            
            # Update max_val if the current value is greater
            max_val = max(max_val, value)

        # Return the maximum value found
        return max_val
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/21.png")
            
            

def Q22():

    st.title("22. Replace All Digits with Characters")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/replace-all-digits-with-characters/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given a 0-indexed string `s` that has lowercase English letters in its even indices and digits in its odd indices.
        
        You must perform an operation `shift(c, x)`, where `c` is a character and `x` is a digit, that returns the x-th character after `c`.
        
        For example, `shift('a', 5) = 'f'` and `shift('x', 0) = 'x`.
        
        For every odd index `i`, you want to replace the digit `s[i]` with the result of the `shift(s[i-1], s[i])` operation.
        
        Return `s` after replacing all digits.
    """)

    # Examples section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input: s = "a1c1e1"
                - Output: "abcdef"
                - Explanation:
                - s[1] -> shift('a',1) = 'b'
                - s[3] -> shift('c',1) = 'd'
                - s[5] -> shift('e',1) = 'f'
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: s = "a1b2c3d4e"
                - Output: "abbdcfdhe"
                - Explanation:
                - s[1] -> shift('a',1) = 'b'
                - s[3] -> shift('b',2) = 'd'
                - s[5] -> shift('c',3) = 'f'
                - s[7] -> shift('d',4) = 'h'
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= s.length <= 100`")
    with colc1:
        st.write("- `s` consists only of lowercase English letters and digits")
    with colc2:
        st.write("- `shift(s[i-1], s[i]) <= 'z'` for all odd indices `i`")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Character Operations**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def replace_digits(s):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("a1c1e1",), "expected": "abcdef"},
                {"input": ("a1b2c3d4e",), "expected": "abbdcfdhe"},
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

                        if "replace_digits" in user_namespace:
                            replace_digits = user_namespace['replace_digits']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = replace_digits(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `replace_digits` not defined. Please define the function to proceed.")
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
    def replace_digits(s):
        # Initialize a list to collect the final characters
        result = []

        # Iterate through the string, two characters at a time
        for i in range(0, len(s), 2):
            # Add the character at the even index to the result
            result.append(s[i])
            
            # Check if there's a next digit (odd index)
            if i + 1 < len(s):
                # Perform the shift operation
                shift_char = chr(ord(s[i]) + int(s[i + 1]))
                result.append(shift_char)

        # Join the list of characters into a final result string
        return ''.join(result)
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/22.png")
            


def Q23():

    st.title("23. Reverse Prefix of Word")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/reverse-prefix-of-word/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given a 0-indexed string `word` and a character `ch`, reverse the segment of `word` that starts at index 0 and ends at the index of the first occurrence of `ch` (inclusive).
        
        If the character `ch` does not exist in `word`, do nothing.
        
        For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be `"dcbaefd"`.
        
        Return the resulting string.
    """)

    # Examples section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input: word = "abcdefd", ch = "d"
                - Output: "dcbaefd"
                - Explanation:
                - The first occurrence of "d" is at index 3. 
                - Reverse the part of `word` from 0 to 3 (inclusive), the resulting string is `"dcbaefd"`.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: word = "xyxzxe", ch = "z"
                - Output: "zxyxxe"
                - Explanation:
                - The first occurrence of "z" is at index 3.
                - Reverse the part of `word` from 0 to 3 (inclusive), resulting in `"zxyxxe"`.
                """)

    with col3:
        st.write("""
                **Example 3**:
                - Input: word = "abcd", ch = "z"
                - Output: "abcd"
                - Explanation: Since "z" does not exist in `word`, no reverse operation is performed.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= word.length <= 250`")
    with colc1:
        st.write("- `word` consists of lowercase English letters.")
    with colc2:
        st.write("- `ch` is a lowercase English letter.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Indexing and Slicing**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def reverse_prefix(word, ch):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("abcdefd", "d"), "expected": "dcbaefd"},
                {"input": ("xyxzxe", "z"), "expected": "zxyxxe"},
                {"input": ("abcd", "z"), "expected": "abcd"},
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

                        if "reverse_prefix" in user_namespace:
                            reverse_prefix = user_namespace['reverse_prefix']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = reverse_prefix(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `reverse_prefix` not defined. Please define the function to proceed.")
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
    def reverse_prefix(word, ch):
        # Find the index of the first occurrence of the character `ch`
        index = word.find(ch)

        # Check if `ch` exists in `word`
        if index != -1:
            # Reverse the substring from the start to the found index and concatenate with the rest of the string
            return word[:index + 1][::-1] + word[index + 1:]
        else:
            # If `ch` is not found, return the original string unchanged
            return word
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/23.png")


def Q24():

    st.title("24. Robot Return to Origin")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/robot-return-to-origin/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

        You are given a string `moves` that represents the move sequence of the robot where `moves[i]` represents its ith move. Valid moves are:
        - 'R' (right)
        - 'L' (left)
        - 'U' (up)
        - 'D' (down)

        Return `True` if the robot returns to the origin after it finishes all of its moves, or `False` otherwise.
    """)

    # Examples section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input: moves = "UD"
                - Output: True
                - Explanation: The robot moves up once, then down once, ending up at the origin.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: moves = "LL"
                - Output: False
                - Explanation: The robot moves left twice, ending up two moves left of the origin.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= moves.length <= 2 * 10^4`")
    with colc1:
        st.write("- `moves` only contains the characters 'U', 'D', 'L' and 'R'.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Coordinate System**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def judge_circle(moves):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ("UD",), "expected": True},
                {"input": ("LL",), "expected": False},
                {"input": ("RRDDUU",), "expected": False},
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

                        if "judge_circle" in user_namespace:
                            judge_circle = user_namespace['judge_circle']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = judge_circle(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `judge_circle` not defined. Please define the function to proceed.")
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
    def judge_circle(moves):
        # Initialize the starting coordinates at the origin (0, 0)
        x, y = 0, 0

        # Iterate through each move in the sequence
        for move in moves:
            # Move right: increase x-coordinate by 1
            if move == 'R':
                x += 1
            # Move left: decrease x-coordinate by 1
            elif move == 'L':
                x -= 1
            # Move up: increase y-coordinate by 1
            elif move == 'U':
                y += 1
            # Move down: decrease y-coordinate by 1
            elif move == 'D':
                y -= 1

        # Return True if the final coordinates are back at the origin
        return x == 0 and y == 0
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/24.png")


def Q25():

    st.title("25. Self Dividing Numbers")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/self-dividing-numbers/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: A self-dividing number is a number that is divisible by every digit it contains.
        
        For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
        
        A self-dividing number is not allowed to contain the digit zero.
        
        Given two integers `left` and `right`, return a list of all the self-dividing numbers in the range `[left, right]` (both inclusive).
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: left = 1, right = 22
                - Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: left = 47, right = 85
                - Output: [48,55,66,77]
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= left <= right <= 10^4`")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Number Theory**")
    with colt1:
        st.write("- **Looping through Digits**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def self_dividing_numbers(left, right):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": (1, 22), "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
                {"input": (47, 85), "expected": [48, 55, 66, 77]},
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

                        if "self_dividing_numbers" in user_namespace:
                            self_dividing_numbers = user_namespace['self_dividing_numbers']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = self_dividing_numbers(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `self_dividing_numbers` not defined. Please define the function to proceed.")
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
    def self_dividing_numbers(left, right):
        # Define a helper function to check if a number is self-dividing
        def is_self_dividing(number):
            # Convert the number to a string to access each digit
            for digit in str(number):
                # Convert digit back to integer and check divisibility, and avoid zeroes
                if digit == '0' or number % int(digit) != 0:
                    return False
            return True

        # Use a list comprehension to collect self-dividing numbers in the range [left, right]
        return [num for num in range(left, right + 1) if is_self_dividing(num)]
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/25.png")

def Q26():

    st.title("26. Unique Morse Code Words")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/unique-morse-code-words/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes.

        For example:
        - 'a' maps to ".-",
        - 'b' maps to "-...",
        - 'c' maps to "-.-.", and so on.

        Given an array of strings `words`, where each word can be written as a concatenation of the Morse code of each letter, return the number of different transformations among all words.

        For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We call such a concatenation the transformation of a word.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: words = ["gin","zen","gig","msg"]
                - Output: 2
                - Explanation: The transformation of each word is:
                    - "gin" -> "--...-."
                    - "zen" -> "--...-."
                    - "gig" -> "--...--."
                    - "msg" -> "--...--."
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: words = ["a"]
                - Output: 1
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= words.length <= 100`")
        st.write("- `1 <= words[i].length <= 12`")
        st.write("- `words[i]` consists of lowercase English letters.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Transformation**")
    with colt1:
        st.write("- **Hash Set for Unique Count**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def unique_morse_representations(words):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": (["gin", "zen", "gig", "msg"],), "expected": 2},
                {"input": (["a"],), "expected": 1},
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

                        if "unique_morse_representations" in user_namespace:
                            unique_morse_representations = user_namespace['unique_morse_representations']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = unique_morse_representations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `unique_morse_representations` not defined. Please define the function to proceed.")
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
    def unique_morse_representations(words):
        # Define the Morse code transformation for each letter in the alphabet
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
                    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", 
                    ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        # Create a dictionary to map each letter to its Morse code
        letter_to_morse = {chr(i + ord('a')): morse_codes[i] for i in range(26)}

        # Use a set to store unique transformations
        transformations = set()

        # Convert each word to its Morse code transformation
        for word in words:
            # Join the Morse codes for each letter in the word to form the transformation
            transformation = ''.join(letter_to_morse[letter] for letter in word)
            # Add the transformation to the set for uniqueness
            transformations.add(transformation)

        # Return the count of unique transformations
        return len(transformations)
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/26.png")


def Q27():
    st.title("27. Flipping an Image")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/flipping-an-image/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an n x n binary matrix `image`, flip the image horizontally, then invert it, and return the resulting image.

        - To flip an image horizontally means that each row of the image is reversed.
        - To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: image = [[1,1,0],[1,0,1],[0,0,0]]
                - Output: [[1,0,0],[0,1,0],[1,1,1]]
                - Explanation: 
                    - First, reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
                    - Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]].
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
                - Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
                - Explanation:
                    - First, reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
                    - Then, invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]].
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `n == image.length`")
        st.write("- `n == image[i].length`")
        st.write("- `1 <= n <= 20`")
        st.write("- `image[i][j]` is either 0 or 1.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Matrix Manipulation**")
    with colt1:
        st.write("- **Logical Operations**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def flip_and_invert_image(image):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ([[1, 1, 0], [1, 0, 1], [0, 0, 0]],), "expected": [[1, 0, 0], [0, 1, 0], [1, 1, 1]]},
                {"input": ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],), "expected": [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]},
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

                        if "flip_and_invert_image" in user_namespace:
                            flip_and_invert_image = user_namespace['flip_and_invert_image']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = flip_and_invert_image(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `flip_and_invert_image` not defined. Please define the function to proceed.")
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
    def flip_and_invert_image(image):
        # Iterate over each row in the matrix
        for i in range(len(image)):
            # Reverse the row and invert each element
            # (1 - value) inverts 0 to 1 and 1 to 0
            image[i] = [1 - value for value in image[i][::-1]]
        # Return the modified image
        return image
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/27.png")

def Q28():
    st.title("28. Richest Customer Wealth")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/richest-customer-wealth/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given an m x n integer grid `accounts` where `accounts[i][j]` is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

        - A customer's wealth is the total amount of money they have across all bank accounts.
        - The richest customer is the customer with the maximum wealth.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: accounts = [[1,2,3],[3,2,1]]
                - Output: 6
                - Explanation: 
                    - 1st customer has wealth = 1 + 2 + 3 = 6.
                    - 2nd customer has wealth = 3 + 2 + 1 = 6.
                    - Both customers have the same wealth of 6, so the result is 6.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: accounts = [[1,5],[7,3],[3,5]]
                - Output: 10
                - Explanation:
                    - 1st customer has wealth = 1 + 5 = 6.
                    - 2nd customer has wealth = 7 + 3 = 10.
                    - 3rd customer has wealth = 3 + 5 = 8.
                    - The 2nd customer is the richest with a wealth of 10.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `m == accounts.length`")
        st.write("- `n == accounts[i].length`")
        st.write("- `1 <= m, n <= 50`")
        st.write("- `1 <= accounts[i][j] <= 100`")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array Manipulation**")
    with colt1:
        st.write("- **Mathematical Summation**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def maximum_wealth(accounts):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ([[1, 2, 3], [3, 2, 1]],), "expected": 6},
                {"input": ([[1, 5], [7, 3], [3, 5]],), "expected": 10},
                {"input": ([[2, 8, 7], [7, 1, 3], [1, 9, 5]],), "expected": 17},
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

                        if "maximum_wealth" in user_namespace:
                            maximum_wealth = user_namespace['maximum_wealth']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = maximum_wealth(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `maximum_wealth` not defined. Please define the function to proceed.")
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
    def maximum_wealth(accounts):
        # Initialize the max_wealth variable to store the highest wealth found
        max_wealth = 0
        
        # Iterate over each customer's accounts
        for account in accounts:
            # Calculate the wealth for each customer by summing their accounts
            wealth = sum(account)
            # Update max_wealth if the current customer's wealth is greater
            max_wealth = max(max_wealth, wealth)
        
        # Return the maximum wealth found
        return max_wealth
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/28.png")

def Q29():

    st.title("29. Sort Array By Parity")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sort-array-by-parity/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: Given an integer array `nums`, move all the even integers to the beginning of the array, followed by all the odd integers.

        - Return any array that satisfies this condition.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: nums = [3,1,2,4]
                - Output: [2,4,3,1]
                - Explanation: 
                    - Possible outputs: [4,2,3,1], [2,4,1,3], and [4,2,1,3] would all be accepted.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: nums = [0]
                - Output: [0]
                - Explanation:
                    - Since there is only one element, the output is the same as the input.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 5000`")
        st.write("- `0 <= nums[i] <= 5000`")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array Manipulation**")
    with colt1:
        st.write("- **Sorting and Filtering**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sort_array_by_parity(nums):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ([3, 1, 2, 4],), "expected": [2, 4, 3, 1]},
                {"input": ([0],), "expected": [0]},
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

                        if "sort_array_by_parity" in user_namespace:
                            sort_array_by_parity = user_namespace['sort_array_by_parity']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sort_array_by_parity(*input_val)
                                    if set(result[:len([x for x in result if x % 2 == 0])]) == set(expected_val[:len([x for x in expected_val if x % 2 == 0])]) and set(result[len([x for x in result if x % 2 == 0]):]) == set(expected_val[len([x for x in expected_val if x % 2 == 0]):]):
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `sort_array_by_parity` not defined. Please define the function to proceed.")
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
    def sort_array_by_parity(nums):
        # Separate even and odd numbers using list comprehension
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        
        # Combine evens followed by odds and return the result
        return evens + odds
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/29.png")

def Q30():

    st.title("30. N-Repeated Element in Size 2N Array")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
        **Problem**: You are given an integer array `nums` with the following properties:

        - `nums.length == 2 * n`
        - `nums` contains `n + 1` unique elements.
        - Exactly one element of `nums` is repeated `n` times.
        
        Return the element that is repeated `n` times.
    """)

    # Examples section
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: nums = [1,2,3,3]
                - Output: 3
                - Explanation: 
                    - The number 3 is repeated 2 times, which is n times.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: nums = [2,1,2,5,3,2]
                - Output: 2
                - Explanation:
                    - The number 2 is repeated 3 times, which is n times.
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `2 <= n <= 5000`")
        st.write("- `nums.length == 2 * n`")
    with colc1:
        st.write("- `0 <= nums[i] <= 10^4`")
        st.write("- `nums` contains `n + 1` unique elements and one of them is repeated exactly `n` times.")

    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array Manipulation**")
    with colt1:
        st.write("- **Mathematical Operations**")

    # User code input
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def repeated_n_times(nums):
    # Your code goes here
    pass
    """)

        # Test case and Run button
        colTest, colRun = st.columns([5, 1])
        with colTest:
            test_cases = [
                {"input": ([1, 2, 3, 3],), "expected": 3},
                {"input": ([2, 1, 2, 5, 3, 2],), "expected": 2},
                {"input": ([5, 1, 5, 2, 5, 3, 5, 4],), "expected": 5},
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

                        if "repeated_n_times" in user_namespace:
                            repeated_n_times = user_namespace['repeated_n_times']

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = repeated_n_times(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `repeated_n_times` not defined. Please define the function to proceed.")
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
    def repeated_n_times(nums):
        # Use a dictionary to count the occurrences of each element in nums
        count_map = {}
        
        # Iterate through each number in the nums array
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Find the element that appears exactly n times and return it
        for num, count in count_map.items():
            if count == len(nums) // 2:
                return num
    """)

    # Flowchart section
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/30.png")

