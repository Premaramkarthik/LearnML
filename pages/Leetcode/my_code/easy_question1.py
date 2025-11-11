import streamlit as st
import io
import contextlib



def Q1():
    st.title("1. TwoSum")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/two-sum/description/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)

    # Left column: Display the problem description

    st.write("""
        **Problem**: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    \n

    """)



    col1 , col2 , col3 = st.columns(3)

    with col1:
        st.write("""

                **Example 1**:\n
    - Input: `nums = [2,7,11,15], target = 9`\n
    - Output:`[0,1]`\n
    - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
                """)



    with col2:
        st.write("""
                **Example 2**:\n
    - Input:`nums = [3,2,4], target = 6`\n
    - Output: `[1,2]`
                """)

    with col3:
        st.write("""
                **Example 3**:\n
    - Input: nums =`[3,3], target = 6`\n
    - Output: `[0,1]`\n
                """)


    st.write("""
            \n
    **Constraints**:\n
            """)

    colc, colc1 , colc2 , colc3 = st.columns(4)
    with colc:
        st.write("""
                - `2 <= nums.length <= 10^4`\n
                """)

    with colc1:
        st.write("""
                - `-10^9 <= nums[i] <= 10^9`\n
                """)

    with colc2:
        st.write("""
                - `-10^9 <= target <= 10^9`\n
                """)

    with colc3:
        st.write("""
                - `Only one valid answer exists.`
                """)

    st.write("""
            \n
    **Follow-up**: Can you come up with an algorithm that is less than O(n^2) time complexity?
    """)
    st.write( """#### Topics""")
    colt, colt1 = st.columns([1,13])

    with colt:
        st.write("""
                    - **Array**
                        """)
    with colt1:
        st.write("""
                    - **Hash Table**""")

    colLeft, colMid, colRight = st.columns([1.8,1,1])

    with colLeft:

        st.markdown("#### Solve the Problem")

    # Display a code editor for the user to write their solution
        code_input = st.text_area(
        "Write your Python function here:",
        height=300,
        value="""def twoSum(nums, target):
    # Your code goes here
    pass
    """)


        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
                {"input": ([3, 2, 4], 6), "expected": [1, 2]},  # Fixed target
                {"input": ([3, 3], 6), "expected": [0, 1]},    # Fixed target
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

                        # Check if the function `twoSum` is defined
                        if "twoSum" in user_namespace:
                            twoSum = user_namespace['twoSum']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = twoSum(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `twoSum` not defined. Please define the function to proceed.")
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
                def twoSum(nums, target):
                    # Iterate through each element in the list using its index `i`
                    for i in range(len(nums)):
                        # For each `i`, iterate through the remaining elements using index `j`
                        # Start `j` from `i + 1` to ensure we don't use the same element twice
                        for j in range(i + 1, len(nums)):
                            # Check if the sum of the current elements at `i` and `j` equals the target
                            if nums[i] + nums[j] == target:
                                # If a valid pair is found, return their indices as a list
                                return [i, j]

                        """)


        # Right column: Provide code editor for users to solve the problem
        with colRight:
            with st.expander("Flowchart of Sample Answer", expanded=False):
                        st.image("pages/images/easy/1.png") 


def Q2():
    st.title("2. Palindrome Number")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/palindrome-number/description/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.
        A palindrome is a number that reads the same forward and backward.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `x = 121`\n
            - Output: `True`\n
            - Explanation: 121 reads as 121 from left to right and from right to left.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `x = -121`\n
            - Output: `False`\n
            - Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.
        """)

    st.write("""
        **Constraints**:
        - `-2^31 <= x <= 2^31 - 1`
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Math**")
    with colt1:
        st.write("- **String**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def isPalindrome(x: int) -> bool:
    # Your code here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": (121,), "expected": True},
            {"input": (-121,), "expected": False},
            {"input": (10,), "expected": False},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "isPalindrome" in user_namespace:
                        isPalindrome = user_namespace['isPalindrome']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = isPalindrome(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `isPalindrome` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/2.png")  # Replace with actual image path


def Q3():
    st.title("3. Roman to Integer")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/roman-to-integer/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Convert a given Roman numeral to an integer.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `s = "III"`\n
            - Output: `3`\n
            - Explanation: III = 3
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `s = "LVIII"`\n
            - Output: `58`\n
            - Explanation: L = 50, V = 5, III = 3
        """)

    # Constraints
    st.write("""
        **Constraints**:
        - `1 <= s.length <= 15`
        - `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        - It is guaranteed that s is a valid Roman numeral in the range [1, 3999].
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Math**")
    with colt1:
        st.write("- **String**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def romanToInt(s: str) -> int:
    # Your code here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": "III", "expected": 3},
            {"input": "LVIII", "expected": 58},
            {"input": "MCMXCIV", "expected": 1994},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "romanToInt" in user_namespace:
                        romanToInt = user_namespace['romanToInt']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = romanToInt(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `romanToInt` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            total += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            total += roman[s[i]]
    return total
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/3.png")  # Replace with actual image path



def Q4():
    st.title("4. Merge Sorted Array")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/merge-sorted-array/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Merge two sorted arrays, `nums1` and `nums2`, into `nums1`.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `nums1 = [1,2,3,0,0,0], m = 3`, `nums2 = [2,5,6], n = 3`\n
            - Output: `[1,2,2,3,5,6]`
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `nums1 = [1], m = 1`, `nums2 = [], n = 0`\n
            - Output: `[1]`
        """)

    # Constraints
    st.write("""
        **Constraints**:
        - `nums1.length == m + n`
        - `nums2.length == n`
        - `0 <= m, n <= 200`
        - `1 <= m + n <= 200`
        - `-109 <= nums1[i], nums2[j] <= 109`
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **Two Pointers**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def merge(nums1, m, nums2, n):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), "expected": [1, 2, 2, 3, 5, 6]},
            {"input": ([1], 1, [], 0), "expected": [1]},
            {"input": ([0], 0, [1], 1), "expected": [1]},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "merge" in user_namespace:
                        merge_func = user_namespace['merge']

                        for i, case in enumerate(test_cases):
                            nums1_copy = case["input"][0].copy()  # Make a copy of nums1 to avoid overwriting
                            m, nums2, n = case["input"][1:]
                            expected_val = case["expected"]

                            try:
                                merge_func(nums1_copy, m, nums2, n)
                                if nums1_copy == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {nums1_copy}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `merge` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/4.png")  # Replace with actual image path


def Q5():
    st.title("5. Best Time to Buy and Sell Stock")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `prices = [7, 1, 5, 3, 6, 4]`\n
            - Output: `5`\n
            - Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `prices = [7, 6, 4, 3, 1]`\n
            - Output: `0`\n
            - Explanation: No transactions are done and the max profit = 0.
        """)

    # Constraints
    st.write("""
        **Constraints**:
        - 1 <= prices.length <= 10^5
        - 0 <= prices[i] <= 10^4
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **Dynamic Programming**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def maxProfit(prices):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ([7, 1, 5, 3, 6, 4],), "expected": 5},
            {"input": ([7, 6, 4, 3, 1],), "expected": 0},
            {"input": ([5, 4, 3, 2, 1],), "expected": 0},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "maxProfit" in user_namespace:
                        maxProfit = user_namespace['maxProfit']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = maxProfit(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `maxProfit` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/5.png")  # Replace with actual image path


def Q6():
    st.title("6. Maximum Subarray")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-subarray/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given an integer array nums, find the subarray with the largest sum, and return its sum.
    """)

    # Examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`\n
            - Output: `6`\n
            - Explanation: The subarray [4,-1,2,1] has the largest sum 6.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `nums = [1]`\n
            - Output: `1`\n
            - Explanation: The subarray [1] has the largest sum 1.
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: `nums = [5,4,-1,7,8]`\n
            - Output: `23`\n
            - Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
        """)

    # Constraints
    st.write("""
        **Constraints**:
    """)

    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 10^5`")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **Dynamic Programming**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def maxSubArray(nums):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ([-2, 1, -3, 4, -1, 2, 1, -5, 4],), "expected": 6},
            {"input": ([1],), "expected": 1},
            {"input": ([5, 4, -1, 7, 8],), "expected": 23},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "maxSubArray" in user_namespace:
                        maxSubArray = user_namespace['maxSubArray']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = maxSubArray(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `maxSubArray` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/6.png")  # Update with the appropriate image path



def Q7():
    st.title("7. Plus One")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/plus-one/description/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: You are given a large integer represented as an integer array `digits`, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
        Increment the large integer by one and return the resulting array of digits.
    """)

    # Examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `digits = [1, 2, 3]`\n
            - Output: `[1, 2, 4]`\n
            - Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be `[1, 2, 4]`.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `digits = [4, 3, 2, 1]`\n
            - Output: `[4, 3, 2, 2]`\n
            - Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be `[4, 3, 2, 2]`.
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: `digits = [9]`\n
            - Output: `[1, 0]`\n
            - Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be `[1, 0]`.
        """)

    # Constraints
    st.write("""
        **Constraints**:
    """)

    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= digits.length <= 100`")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Array**")
    with colt1:
        st.write("- **Math**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def plusOne(digits):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ([1, 2, 3],), "expected": [1, 2, 4]},
            {"input": ([4, 3, 2, 1],), "expected": [4, 3, 2, 2]},
            {"input": ([9],), "expected": [1, 0]},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "plusOne" in user_namespace:
                        plusOne = user_namespace['plusOne']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = plusOne(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `plusOne` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/7.png")  # Update image path as necessary



def Q8():
    st.title("8. Climbing Stairs")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/climbing-stairs/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """)

    # Examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: n = 2\n
            - Output: 2\n
            - Explanation: There are two ways to climb to the top:\n
                1. 1 step + 1 step\n
                2. 2 steps\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: n = 3\n
            - Output: 3\n
            - Explanation: There are three ways to climb to the top:\n
                1. 1 step + 1 step + 1 step\n
                2. 1 step + 2 steps\n
                3. 2 steps + 1 step
        """)

    # Constraints
    st.write("""
        **Constraints**:
    """)

    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= n <= 45`")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Dynamic Programming**")
    with colt1:
        st.write("- **Fibonacci Sequence**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def climbStairs(n):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": 2, "expected": 2},
            {"input": 3, "expected": 3},
            {"input": 4, "expected": 5},
            {"input": 5, "expected": 8},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "climbStairs" in user_namespace:
                        climbStairs = user_namespace['climbStairs']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = climbStairs(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `climbStairs` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def climbStairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/8.png")


def Q9():
    st.title("9. Single Number")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/single-number/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
        \nYou must implement a solution with a linear runtime complexity and use only constant extra space.
    """)

    # Examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [2,2,1]\n
            - Output: 1\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [4,1,2,1,2]\n
            - Output: 4
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: nums = [1]\n
            - Output: 1
        """)

    # Constraints
    st.write("""
        **Constraints**:
    """)

    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= nums.length <= 3 * 10^4`\n")
    with colc1:
        st.write("- `-3 * 10^4 <= nums[i] <= 3 * 10^4`\n")
    with colc2:
        st.write("- Each element in the array appears twice except for one element.\n")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Bit Manipulation**")
    with colt1:
        st.write("- **Hash Table**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def singleNumber(nums):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": [2, 2, 1], "expected": 1},
            {"input": [4, 1, 2, 1, 2], "expected": 4},
            {"input": [1], "expected": 1},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "singleNumber" in user_namespace:
                        singleNumber = user_namespace['singleNumber']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = singleNumber(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `singleNumber` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/9.png")



def Q10():
    st.title("10. Check if Word Equals Summation of Two Words")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: The letter value of a letter is its position in the alphabet starting from 0 (i.e., 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
        \nThe numerical value of a string of lowercase English letters `s` is the concatenation of the letter values of each letter in `s`, which is then converted into an integer.
        \nYou are given three strings `firstWord`, `secondWord`, and `targetWord`, each consisting of lowercase English letters 'a' through 'j' inclusive.
        \nReturn true if the summation of the numerical values of `firstWord` and `secondWord` equals the numerical value of `targetWord`, or false otherwise.
        \n
    """)

    # Examples
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `firstWord = "acb", secondWord = "cba", targetWord = "cdb"`\n
            - Output: `True`\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `firstWord = "aaa", secondWord = "a", targetWord = "aab"`\n
            - Output: `False`
        """)

    with col3:
        st.write("""
            **Example 3**:\n
            - Input: `firstWord = "aaa", secondWord = "a", targetWord = "aaaa"`\n
            - Output: `True`
        """)

    # Constraints
    st.write("""
        \n**Constraints**:\n
    """)

    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `1 <= firstWord.length, secondWord.length, targetWord.length <= 8`\n")
    with colc1:
        st.write("- `firstWord`, `secondWord`, `targetWord` consist of lowercase English letters from 'a' to 'j'.\n")

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Mathematics**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def isSumEqual(firstWord, secondWord, targetWord):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ("acb", "cba", "cdb"), "expected": True},
            {"input": ("aaa", "a", "aab"), "expected": False},
            {"input": ("aaa", "a", "aaaa"), "expected": True},
        ]

        result_placeholders = []
        for i, case in enumerate(test_cases):
            with st.expander(f"View Test Case {i + 1}", expanded=False):
                st.write(f"**Test Case {i + 1}:**")
                st.write(f"- Input: {case['input']}")
                st.write(f"- Expected Output: {case['expected']}")
            result_placeholders.append(st.empty())

        error_placeholder = st.empty()

        if st.button("Run Code"):
            buffer = io.StringIO()

            try:
                with contextlib.redirect_stdout(buffer):
                    user_namespace = {}
                    exec(code_input, user_namespace)

                    if "isSumEqual" in user_namespace:
                        isSumEqual = user_namespace['isSumEqual']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = isSumEqual(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `isSumEqual` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""
def isSumEqual(firstWord, secondWord, targetWord):
    def getValue(word):
        return int(''.join(str(ord(c) - ord('a')) for c in word))

    return getValue(firstWord) + getValue(secondWord) == getValue(targetWord)
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/easy/10.png")

