import streamlit as st
import contextlib
import io


def Q11():
        st.title("11. Build Array from Permutation")
        st.markdown("[Visit Leetcode](https://leetcode.com/problems/build-array-from-permutation/) for a better experience.")
        # Create two columns: left for question, right for code input


        # Left column: Display the problem description
        st.write("""
                    **Problem**: Given a **zero-based permutation** `nums` (0-indexed), build an array `ans` of the same length where `ans[i] = nums[nums[i]]` for each valid index `i` and return it.

                A zero-based permutation is an array of **distinct integers** from `0` to `nums.length - 1` (inclusive).
    """)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("""
                    **Example 1**:
                - Input: `nums = [0, 2, 1, 5, 3, 4]`
                - Output: `[0, 1, 2, 4, 5, 3]`
                - Explanation:
                ```plaintext
                ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
                    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
                    = [0, 1, 2, 4, 5, 3]
                ```
    """)

        with col2:
            st.write("""
                    **Example 2**:
                - Input: `nums = [5, 0, 1, 2, 3, 4]`
                - Output: `[4, 5, 0, 1, 2, 3]`
    """)

        # Constraints section
        st.write("**Constraints:**")
        colc, colc1, colc2, colc3 = st.columns(4)
        with colc:
            st.write("- `1 <= nums.length <= 1000`")
        with colc1:
            st.write("- `0 <= nums[i] < nums.length")
        with colc2:
            st.write("- All elements in `nums` are distinct.")

        # Topics
        st.write("#### Topics")
        
        st.write("""
                    - **Array Manipulation**
                    - **Permutation Handling**
                """)

        colLeft, colMid, colRight = st.columns([1.8, 2, 1])

        with colLeft:
            st.markdown("#### Solve the Problem")

            # Code input box for the user to write their solution
            code_input = st.text_area(
                "Write your Python function here:",
                height=300,
                value="""def can_construct(nums):
        # Your code goes here
        pass
        """)

            colTest, colRun = st.columns([5, 1])

            with colTest:
                # Predefined test cases to evaluate the user's function
                test_cases = [
                    {"input": [0, 2, 1, 5, 3, 4], "expected": [0, 1, 2, 4, 5, 3]},
                    {"input": [5, 0, 1, 2, 3, 4], "expected": [4, 5, 0, 1, 2, 3]},
                    {"input": [2, 0, 1], "expected": [1, 2, 0]},
                ]
                result_placeholders = []
                # Display the test cases in expanders
                for i, case in enumerate(test_cases):
                    with st.expander(f"View Test Case {i + 1}", expanded=False):
                        st.write(f"**Test Case {i + 1}:**")
                        st.write(f"- Input: {case['input']}")
                        st.write(f"- Expected Output: {case['expected']}")
                    result_placeholder = st.empty()
                    result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)

        with colMid:
            with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
                st.code("""def can_construct(nums):
        return [nums[nums[i]] for i in range(len(nums))]
        """)

        # Right column: Display flowchart of sample answer
        with colRight:
            with st.expander("Flowchart of Sample Answer", expanded=False):
                st.image("pages/images/easy/11.png")

def Q12():
    st.title("12. Valid Parentheses")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/valid-parentheses/) for a better experience.")


    # Left column: Display the problem description
    st.write("""
                           **Problem**: Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

            **A valid string must meet the following conditions**:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.
            - Every close bracket has a corresponding open bracket of the same type.
    """)

    # Right column: Display example and constraints
    col1, col2, col3, col4= st.columns(4)

    with col1:
        st.write(""" **Example 1**:
            - Input: `s = "()"`
            - Output: `true`""")

    with col2:
        st.write("""**Example 2**:
            - Input: `s = "()[]{}"`
            - Output: `true`""")

    with col3:
        st.write(""" **Example 3**:
            - Input: `s = "(]"`
            - Output: `false`""")
    with col4:
        st.write("""
            **Example 4**:
            - Input: `s = "([])"`
            - Output: `true`""")
        
        
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1= st.columns(2)
    with colc:
        st.write("- `1 <= s.length <= 10^4`")
    with colc1:
        st.write("- `s` consists of parentheses only `'()[]{}'`.")

    # Topics
    st.write("#### Topics")
    st.write("""
                - **String Manipulation**
                - **Stack Data Structure**
            """)


    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(s):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": "()", "expected": True},
            {"input": "()[]{}", "expected": True},
            {"input": "(]", "expected": False},
            {"input": "([])", "expected": True},
            ]
            result_placeholders = []
            # Display the test cases in expanders

            # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                        # Check if the function `can_construct` is defined
                        if "can_construct" in user_namespace:
                            can_construct= user_namespace['can_construct']  # Get the function

                            # Run the function on all test cases

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = can_construct(input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")
                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/12.png")

def Q13():
    st.title("13. Maximum Number of Vowels in a Substring of Given Length")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) for a better experience.")


    # Left column: Display the problem description
    st.write("""
              **Problem**: Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

            **Vowels** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
    """)

    # Right column: Display example and constraints
    col1, col2= st.columns(2)

    with col1:
        st.write("""  **Example 1**:
            - Input: `s = "abciiidef"`, `k = 3`
            - Output: `3`
            - Explanation: The substring `"iii"` contains 3 vowel letters.
""")
        st.write("""
                **Example 3**:
            - Input: `s = "leetcode"`, `k = 3`
            - Output: `2`
            - Explanation: `"lee"`, `"eet"`, and `"ode"` contain 2 vowels.

                 """)

    with col2:
        st.write(""" **Example 2**:
            - Input: `s = "aeiou"`, `k = 2`
            - Output: `2`
            - Explanation: Any substring of length 2 contains 2 vowels.
`""")


    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2= st.columns(3)
    with colc:
        st.write(" `1 <= s.length <= 10^5`")
    with colc1:
        st.write("- `s` consists of lowercase English letters.")
    with colc2:
        st.write("- `1 <= k <= s.length`")
    # Topics
    st.write("#### Topics")
    st.write("""
                - **Sliding Window**
                - **String Manipulation**
            """)


    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(s, k):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ("abciiidef", 3), "expected": 3},
            {"input": ("aeiou", 2), "expected": 2},
            {"input": ("leetcode", 3), "expected": 2},
            {"input": ("abcde", 1), "expected": 1},
            ]
            result_placeholders = []
            # Display the test cases in expanders
            # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                        # Check if the function `can_construct` is defined
                        if "can_construct" in user_namespace:
                            can_construct= user_namespace['can_construct']  # Get the function

                            # Run the function on all test cases

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = can_construct(input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")
                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = current_count = sum(1 for i in range(k) if s[i] in vowels)

    for i in range(k, len(s)):
        current_count += (s[i] in vowels) - (s[i - k] in vowels)
        max_count = max(max_count, current_count)

    return max_count
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/13.png")


def Q14():
    st.title("14. Excel sheet column number")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/excel-sheet column-number /description/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
                **Problem**:14.Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
    For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
    """)

    # Right column: Example and constraints
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""**Example 1**:
            - Input: `columntitle="A"`
            - Output: `1`""")

    with col2:
        st.write("""**Example 2**:
            - Input: `columntitle="AB"`
            - Output: `28`""")

    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= columnTitle.length <= 7`")
    with colc1:
        st.write("-`columnTitle consists only of uppercase English letters.` ")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1,13])
    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Hashing**")

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(columnTitle):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": "A", "expected": 1},
            {"input": "AB", "expected": 28},
            {"input": "ZY", "expected": 701},
            {"input": "AAA", "expected": 703},

            ]
            result_placeholders = []
            # Display the test cases in expanders
            # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                        # Check if the function `can_construct` is defined
                        if "can_construct" in user_namespace:
                            can_construct= user_namespace['can_construct']  # Get the function

                            # Run the function on all test cases

                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = can_construct(input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")
                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(columnTitle):
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/14.png")


def Q15():
        
    st.title("15. Majority elements")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/majority-element/) for a better experience.")


    # Left column: Display the problem description
    st.write("""
                **Problem**: Given an array `nums` of size `n`, return the majority element.

            The **majority element** is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    """)
    # Create columns for examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                 **Example 1**:
            - Input: `nums = [3,2,3]`
            - Output: `3`
                """)

    with col2:
        st.write("""
                
            **Example 2**:
            - Input: `nums = [2,2,1,1,1,2,2]`
            - Output: `2`
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `n == nums.length`")
    with colc1:
        st.write("- `1 <= n <= 5 * 10^4`")
    with colc2:
        st.write("- `-10^9 <= nums[i] <= 10^9`")

    # Topics
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Hash Table**
                - **Divide and Conquer**
                - **Sorting**
                - **Voting Algorithm**
            """)

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                 {"input": [3, 2, 3], "expected": 3},
            {"input": [2, 2, 1, 1, 1, 2, 2], "expected": 2},
            {"input": [1, 1, 1, 2, 2], "expected": 1},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(nums):
    count, candidate = 0, None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/15.png")

def Q16():

    st.title("16. Contain Duplicates")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/contains-duplicate/description/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    with col1:
        st.write("""
                **Problem**: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    """)
    # Create columns for examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input: nums = [1,2,3,4]
                - Output: true
                - Explanation: All elements are distinct.
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: nums = [1,2,3,4]
                - Output: false
                - Explanation: All elements are distinct.
                """)
    
    with col3:
        st.write("""
                  **Example 3**:
            - Input: `nums = [1,1,1,3,3,4,3,2,4,2]`
            - Output: `true`
                 """)
    # Constraints section
    st.write("**Constraints:**")
    colc, colc1= st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 10^5`")
    with colc1:
        st.write("- `-10^9 <= nums[i] <= 10^9`")


    # Topics
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Hash Table**
                - **Sorting**
            """)

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 2, 3, 1], "expected": True},
            {"input": [1, 2, 3, 4], "expected": False},
            {"input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(nums):
    return len(nums) != len(set(nums))

    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/16.png")


def Q17():
    st.title("17. Zero permutation")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/missing-number/) for a better experience.")

    # Left column: Display the problem description
    st.write("""
                **Problem**: Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
    """)
    # Create columns for examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `nums = [3,0,1]`
            - Output: `2`
            - **Explanation**: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
 """)

    with col2:
        st.write("""
                  **Example 2**:
            - Input: `nums = [0,1]`
            - Output: `2`
            - **Explanation**: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
""")
    with col3:
        st.write("""       
                 **Example 3**:
            - Input: `nums = [9,6,4,2,3,5,7,0,1]`
            - Output: `8`
            - **Explanation**: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `n == nums.length``")
        st.write("- All the numbers of `nums` are unique.")
    with colc1:
        st.write("- `1 <= n <= 10^4``")
    with colc2:
        st.write("- `0 <= nums[i] <= n`")

    # Topics
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Bit Manipulation**
                - **Mathematical**
            """)

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""ddef can_construct(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [3, 0, 1], "expected": 2},
            {"input": [0, 1], "expected": 2},
            {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/17.png")

def Q18():
    
    st.title("18. Build Array from Permutation")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/build-array-from-permutation/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description
    st.write("""
                **Problem**: Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length
    and return it.A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
    """)
    # Create columns for examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
               **Example 1**:
            - Input: `nums = [0, 2, 1, 5, 3, 4]`
            - Output: `[0, 1, 2, 4, 5, 3]`
            - Explanation:
              ```plaintext
              ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
                  = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
                  = [0, 1, 2, 4, 5, 3]
              ``` """)

    with col2:
        st.write("""
                 **Example 2**:
            - Input: `nums = [5, 0, 1, 2, 3, 4]`
            - Output: `[4, 5, 0, 1, 2, 3]`

                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= nums.length <= 1000`")
    with colc1:
        st.write("- `0 <= nums[i] < nums.length`")
    with colc2:
        st.write("- All elements in `nums` are distinct.")

    # Topics
    st.write("#### Topics")
    st.write("""
                - **Array Manipulation**
                - **Permutation Handling**
            """)
    
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [0, 2, 1, 5, 3, 4], "expected": [0, 1, 2, 4, 5, 3]},
            {"input": [5, 0, 1, 2, 3, 4], "expected": [4, 5, 0, 1, 2, 3]},
            {"input": [2, 0, 1], "expected": [1, 2, 0]},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(nums):
    return [nums[nums[i]] for i in range(len(nums))]
    """)
    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/18.png")


def Q19():
    st.title("19. Moves Zeroes")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/move-zeroes/) for a better experience.")

    # Left column: Display the problem description
    st.write("""**Problem**: Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

            **Note**: You must do this in-place without making a copy of the array.
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input:nums=[0,1,0,3,12]
                - Output: [1,3,12,0,0]
                """)

    with col2:
        st.write("""
                **Example 2**:
                - Input: nums = [0]
                - Output: [0]
                """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 10^4`")
    with colc1:
        st.write("- `-2^31 <= nums[i] <= 2^31 - 1")


    # Topics
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Two Pointers**
                - **In-Place**
            """)
        
        
    colLeft, colMid, colRight = st.columns([1.8, 2, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [0, 1, 0, 3, 12], "expected": [1, 3, 12, 0, 0]},
            {"input": [0], "expected": [0]},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(nums):
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/19.png")
            


def Q20():
    st.title("20. Ransom Note")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/ransom-note/) for a better experience.")

    # Left column: Display the problem description
    st.write(""" **Problem**: Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

            **Note**: Each letter in `magazine` can only be used once in `ransomNote`.
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
            - Input: `ransomNote = "a"`, `magazine = "b"`
            - Output: `false`
  """)

    with col2:
        st.write("""
                 **Example 2**:
            - Input: `ransomNote = "aa"`, `magazine = "ab"`
            - Output: `false`
  """)
        
    with col3:
        st.write("""
                 **Example 3**:
            - Input: `ransomNote = "aa"`, `magazine = "aab"`
            - Output: `true`

                 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= ransomNote.length, magazine.length <= 10^5`")
    with colc1:
        st.write("- `ransomNote` and `magazine` consist of lowercase English letters.")


    # Topics
    st.write("#### Topics")
    st.write("""
                - **Hash Table**
                - **String Manipulation**
            """)
        
        
    colLeft, colMid, colRight = st.columns([1.8, 2, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def can_construct(ransomNote, magazine):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ("a", "b"), "expected": False},
            {"input": ("aa", "ab"), "expected": False},
            {"input": ("aa", "aab"), "expected": True},
            ]
            result_placeholders = []
                # Display the test cases in expanders
                # Display the test cases in expanders
            for i, case in enumerate(test_cases):
                with st.expander(f"View Test Case {i + 1}", expanded=False):
                    st.write(f"**Test Case {i + 1}:**")
                    st.write(f"- Input: {case['input']}")
                    st.write(f"- Expected Output: {case['expected']}")
                result_placeholder = st.empty()
                result_placeholders.append(result_placeholder)

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

                            # Check if the function `can_construct` is defined
                            if "can_construct" in user_namespace:
                                can_construct= user_namespace['can_construct']  # Get the function

                                # Run the function on all test cases

                                for i, case in enumerate(test_cases):
                                    input_val = case["input"]
                                    expected_val = case["expected"]

                                    try:
                                        result = can_construct(*input_val)  # Unpack input for the function
                                        if result == expected_val:
                                            result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        else:
                                            result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                    except Exception as e:
                                        result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                            else:
                                error_placeholder.error("Function `can_construct` not defined. Please define the function to proceed.")
                    except Exception as e:
                        error_placeholder.error(f"Error executing code: {e}")
                    # Display any print outputs or errors captured
                    output = buffer.getvalue()
                    if output:
                        st.subheader("Execution Output:")
                        st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def can_construct(ransomNote, magazine):
    from collections import Counter
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char in ransom_count:
        if ransom_count[char] > magazine_count.get(char, 0):
            return False
    return True
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/20.png")