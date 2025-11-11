import streamlit as st
import io
import contextlib
from collections import defaultdict
from collections import Counter


def Q1():
    st.title("58. Length of Last Word")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/length-of-last-word/description/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given a string `s` consisting of words and spaces, return the length of the last word in the string.
        A word is a maximal substring consisting of non-space characters only.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `s = "Hello World"`
            - Output: `5`
            - Explanation: The last word is "World" with length 5.
        """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `s = "   fly me   to   the moon  "`
            - Output: `4`
            - Explanation: The last word is "moon" with length 4.
        """)

    st.write("""
        **Constraints**:
        - `1 <= s.length <= 10^4`
        - `s` consists of only English letters and spaces ' '.
        - There will be at least one word in `s`.
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **String Manipulation**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 2, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def lengthOfLastWord(s):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": ("Hello World",), "expected": 5},
            {"input": ("   fly me   to   the moon  ",), "expected": 4},
            {"input": ("luffy is still joyboy",), "expected": 6},
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

                    if "lengthOfLastWord" in user_namespace:
                        lengthOfLastWord = user_namespace['lengthOfLastWord']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = lengthOfLastWord(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `lengthOfLastWord` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def lengthOfLastWord(s):
    return len(s.strip().split(" ")[-1])
""")

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/1.png")  # Replace with actual image path


def Q2():
    st.title("88. Merge Sorted Array II")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/merge-sorted-array/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.
        Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.
        The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`\n
            - Output: `[1,2,2,3,5,6]`\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `nums1 = [1], m = 1, nums2 = [], n = 0`\n
            - Output: `[1]`\n
        """)

    st.write("""
        **Constraints**:
        - `nums1.length == m + n`\n
        - `1 <= m + n <= 200`\n
        - `nums2.length == n`\n
        - `0 <= m, n <= 200`\n
        - `10^9 <= nums1[i], nums2[j] <= 10^9`
        
    """)


    # Topics
    st.write("#### Topics")
    st.write("""
             - **Array**
             - **Two Pointers**
             - **Sorting**
             """)
    

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
                        merge = user_namespace['merge']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                nums1 = input_val[0].copy()
                                merge(nums1, *input_val[1:])

                                if nums1 == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {nums1}")
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
            st.code("""def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []
    p1, p2 = 0, 0
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1
    if p1 < m:
        nums1.extend(nums1_copy[p1:])
    if p2 < n:
        nums1.extend(nums2[p2:])
""")

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/2.png")  # Replace with actual image path


def Q3():
    st.title("83. Remove Duplicates from Sorted List")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
        Return the linked list sorted as well.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: head = [1,1,2]\n
            - Output: [1,2]\n
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: head = [1,1,2,3,3]\n
            - Output: [1,2,3]\n
        """)

    st.write("""
        **Constraints**:\n
        - The number of nodes in the list is in the range [0, 300].
        - -100 <= Node.val <= 100
        - The list is guaranteed to be sorted in non-decreasing order.
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Linked List**")
    with colt1:
        st.write("- **Two Pointers**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def deleteDuplicates(head):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": [1, 1, 2], "expected": [1, 2]},
            {"input": [1, 1, 2, 3, 3], "expected": [1, 2, 3]},
            {"input": [], "expected": []},  # Edge case for empty list
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

                    if "deleteDuplicates" in user_namespace:
                        deleteDuplicates = user_namespace['deleteDuplicates']

                        # Helper function to convert input list to linked list
                        class ListNode:
                            def __init__(self, val=0, next=None):
                                self.val = val
                                self.next = next

                        def list_to_linkedlist(elements):
                            dummy = ListNode()
                            current = dummy
                            for element in elements:
                                current.next = ListNode(element)
                                current = current.next
                            return dummy.next

                        for i, case in enumerate(test_cases):
                            input_val = list_to_linkedlist(case["input"])
                            expected_val = case["expected"]

                            try:
                                result = deleteDuplicates(input_val)

                                # Collect the output from the result linked list
                                output = []
                                while result:
                                    output.append(result.val)
                                    result = result.next

                                if output == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {output}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `deleteDuplicates` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
""")

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/3.png")  # Replace with actual image path


def Q4():
    st.title("1207. Unique Number of Occurrences")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/unique-number-of-occurrences/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: arr = [1,2,2,1,1,3]\n
            - Output: true\n
            - Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1. No two values have the same number of occurrences.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: arr = [1,2]\n
            - Output: false
        """)

    st.write("""
        **Constraints**:\n
        - 1 <= arr.length <= 1000
        - -1000 <= arr[i] <= 1000
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Hash Table**")
    with colt1:
        st.write("- **Counting**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def uniqueOccurrences(arr):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": [1, 2, 2, 1, 1, 3], "expected": True},
            {"input": [1, 2], "expected": False},
            {"input": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], "expected": True},
            {"input": [1, 1, 2, 2, 3, 3, 4], "expected": False},  # Example with duplicates
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

                    if "uniqueOccurrences" in user_namespace:
                        uniqueOccurrences = user_namespace['uniqueOccurrences']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = uniqueOccurrences(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `uniqueOccurrences` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def uniqueOccurrences(arr):
    occurrences = Counter(arr)
    return len(occurrences.values()) == len(set(occurrences.values()))
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/4.png")  # Replace with actual image path


def Q5():
    st.title("2103. Rings and Rods")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/rings-and-rods/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: There are n rings and each ring is either red, green, or blue.
        The rings are distributed across ten rods labeled from 0 to 9.

        You are given a string rings of length 2n that describes the n rings that are placed onto the rods.
        Every two characters in rings forms a color-position pair that is used to describe each ring,
        where the first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
        The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: rings = "B0B6G0R6R0R6G9"\n
            - Output: 1\n
            - Explanation: The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: rings = "B0R0G0R9R0B0G0"\n
            - Output: 1\n
            - Explanation: The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
        """)

    st.write("""
        **Constraints**:\n
        - rings.length == 2 * n
        - 1 <= n <= 100
        - rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
        - rings[i] where i is odd is a digit from '0' to '9' (0-indexed).
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Hash Table**")
    with colt1:
        st.write("- **Counting**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def countRods(rings):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": "B0B6G0R6R0R6G9", "expected": 1},
            {"input": "B0R0G0R9R0B0G0", "expected": 1},
            {"input": "G4", "expected": 0},
            {"input": "R0G0B0R1G1B1R2G2B2", "expected": 3},  # All rods have all colors
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

                    if "countRods" in user_namespace:
                        countRods = user_namespace['countRods']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = countRods(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `countRods` not defined. Please define the function to proceed.")
            except Exception as e:
                error_placeholder.error(f"Error executing code: {e}")

            output = buffer.getvalue()
            if output:
                st.subheader("Execution Output:")
                st.text(output)

    # Sample Answer and Flowchart
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def countRods(rings):
    rod_colors = defaultdict(set)
    for i in range(0, len(rings), 2):
        color = rings[i]
        rod = rings[i + 1]
        rod_colors[rod].add(color)
    return sum(1 for colors in rod_colors.values() if len(colors) == 3)
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/5.png")  # Replace with actual image path



def Q6():
    st.title("2574. Left and Right Sum Differences")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/left-and-right-sum-differences/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
        - answer.length == nums.length.
        - answer[i] = |leftSum[i] - rightSum[i]|.

        Where:
        - leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
        - rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: nums = [10,4,8,3]\n
            - Output: [15,1,11,22]\n
            - Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: nums = [1]\n
            - Output: [0]\n
            - Explanation: The array leftSum is [0] and the array rightSum is [0].
        """)

    st.write("""
        **Constraints**:\n
        - 1 <= nums.length <= 1000
        - 1 <= nums[i] <= 10^5
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Prefix Sum**")
    with colt1:
        st.write("- **Absolute Difference**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def leftRightDifference(nums):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": [10, 4, 8, 3], "expected": [15, 1, 11, 22]},
            {"input": [1], "expected": [0]},
            {"input": [5, 2, 6], "expected": [1, 3, 1]},
            {"input": [7, 1, 3, 9, 4], "expected": [17, 9, 7, 3, 0]},
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

                    if "leftRightDifference" in user_namespace:
                        leftRightDifference = user_namespace['leftRightDifference']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = leftRightDifference(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `leftRightDifference` not defined. Please define the function to proceed.")
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
def leftRightDifference(nums):
    n = len(nums)
    leftSum = [0] * n
    rightSum = [0] * n
    answer = [0] * n

    # Calculate left sums
    for i in range(1, n):
        leftSum[i] = leftSum[i - 1] + nums[i - 1]

    # Calculate right sums
    for i in range(n - 2, -1, -1):
        rightSum[i] = rightSum[i + 1] + nums[i + 1]

    # Calculate answer
    for i in range(n):
        answer[i] = abs(leftSum[i] - rightSum[i])

    return answer
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/6.png")  # Replace with actual image path



def Q7():
    st.title("1342. Calculate Delayed Arrival Time for a Train")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/calculate-delayed-arrival-time/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: You are given a positive integer `arrivalTime` denoting the arrival time of a train in hours, and another positive integer `delayedTime` denoting the amount of delay in hours.
        Return the time when the train will arrive at the station. Note that the time in this problem is in 24-hours format.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `arrivalTime = 15`, `delayedTime = 5`\n
            - Output: `20`\n
            - Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15 + 5 = 20 (20:00 hours).
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `arrivalTime = 13`, `delayedTime = 11`\n
            - Output: `0`\n
            - Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13 + 11 = 24 (which is denoted by 00:00 in 24 hours format so return 0).
        """)

    st.write("""
        **Constraints**:\n
        - `1 <= arrivalTime < 24`
        - `1 <= delayedTime <= 24`
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Modulo Operations**")
    with colt1:
        st.write("- **Basic Arithmetic**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def calculateDelayedArrivalTime(arrivalTime, delayedTime):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": (15, 5), "expected": 20},
            {"input": (13, 11), "expected": 0},
            {"input": (1, 24), "expected": 1},
            {"input": (23, 1), "expected": 0},
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

                    if "calculateDelayedArrivalTime" in user_namespace:
                        calculateDelayedArrivalTime = user_namespace['calculateDelayedArrivalTime']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = calculateDelayedArrivalTime(*input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `calculateDelayedArrivalTime` not defined. Please define the function to proceed.")
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
def calculateDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/7.png")  # Replace with actual image path


def Q8():
    st.title("1342. Number of Steps to Reduce a Number to Zero")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given an integer num, return the number of steps to reduce it to zero.
        In one step, if the current number is even, you have to divide it by 2; otherwise, you have to subtract 1 from it.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `num = 14`\n
            - Output: `6`\n
            - Explanation:\n
              Step 1) 14 is even; divide by 2 to get 7.\n
              Step 2) 7 is odd; subtract 1 to get 6.\n
              Step 3) 6 is even; divide by 2 to get 3.\n
              Step 4) 3 is odd; subtract 1 to get 2.\n
              Step 5) 2 is even; divide by 2 to get 1.\n
              Step 6) 1 is odd; subtract 1 to get 0.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `num = 8`\n
            - Output: `4`\n
            - Explanation:\n
              Step 1) 8 is even; divide by 2 to get 4.\n
              Step 2) 4 is even; divide by 2 to get 2.\n
              Step 3) 2 is even; divide by 2 to get 1.\n
              Step 4) 1 is odd; subtract 1 to get 0.
        """)

    st.write("""
        **Example 3**:\n
        - Input: `num = 123`\n
        - Output: `12`
    """)

    # Constraints
    st.write("""
        **Constraints**:
        - `0 <= num <= 10^6`
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 = st.columns([1, 13])

    with colt:
        st.write("- **Loops**")
    with colt1:
        st.write("- **Conditional Statements**")
    with colt1:
        st.write("- **Bit Manipulation (for efficiency)**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def numberOfSteps(num):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": 14, "expected": 6},
            {"input": 8, "expected": 4},
            {"input": 123, "expected": 12},
            {"input": 0, "expected": 0},  # Edge case
            {"input": 1, "expected": 1},  # Edge case
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

                    if "numberOfSteps" in user_namespace:
                        numberOfSteps = user_namespace['numberOfSteps']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = numberOfSteps(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `numberOfSteps` not defined. Please define the function to proceed.")
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
def numberOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/8.png")  # Replace with actual image path



def Q9():
    st.title("2520. Count the Digits That Divide a Number")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) for a better experience.")

    # Problem Description
    st.write("""
        **Problem**: Given an integer num, return the number of digits in num that divide num.
        An integer val divides num if num % val == 0.
    """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            **Example 1**:\n
            - Input: `num = 7`\n
            - Output: `1`\n
            - Explanation: 7 divides itself, hence the answer is 1.
        """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: `num = 121`\n
            - Output: `2`\n
            - Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
        """)

    st.write("""
        **Example 3**:\n
        - Input: `num = 1248`\n
        - Output: `4`\n
        - Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
    """)

    # Constraints
    st.write("""
        **Constraints**:
        - `1 <= num <= 10^9`
        - `num` does not contain 0 as one of its digits.
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 , colt2= st.columns(3)

    with colt:
        st.write("- **Loops**")
    with colt1:
        st.write("- **String Manipulation**")
    with colt2:
        st.write("- **Mathematical Operations**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def reverseWords(num):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": 7, "expected": 1},
            {"input": 121, "expected": 2},
            {"input": 1248, "expected": 4},
            {"input": 100, "expected": 2},  # Edge case
            {"input": 999999999, "expected": 9},  # Edge case
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

                    if "reverseWords" in user_namespace:
                        reverseWords = user_namespace['reverseWords']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = reverseWords(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `reverseWords` not defined. Please define the function to proceed.")
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
def reverseWords(num):
    count = 0
    for digit in str(num):
        if num % int(digit) == 0:
            count += 1
    return count
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/9.png")  # Replace with actual image path



def Q10():
    st.title("10. Reverse Words in a String III")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/reverse-words-in-a-string-iii/) for a better experience.")

    # Problem Description
    st.write("""
**Problem**: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
               """)

    # Examples
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
           **Example 1**:\n
            - Input: s = "Let's take LeetCode contest"\n
            - Output: "s'teL ekat edoCteeL tsetnoc"\n
               """)

    with col2:
        st.write("""
            **Example 2**:\n
            - Input: s = "Mr Ding"\n
            - Output: "rM gniD"\n
                   """)

    # Constraints
    st.write("""
         **Constraints**:\n
            - 1 <= s.length <= 5 * 10^4\n
            - s contains printable ASCII characters.\n
            - s does not contain any leading or trailing spaces.\n
            - There is at least one word in s.\n
            - All the words in s are separated by a single space.
    """)

    # Topics
    st.write("#### Topics")
    colt, colt1 , colt2= st.columns(3)

    with colt:
        st.write("- **String Manipulation**")
    with colt1:
        st.write("- **Two Pointers**")
    with colt2:
        st.write("- **In-place Operations**")

    # Solve the Problem Section
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def reverseWords(s):
    # Your code goes here
    pass
"""
        )

        # Test Cases
        test_cases = [
            {"input": 7, "expected": 1},
            {"input": 121, "expected": 2},
            {"input": 1248, "expected": 4},
            {"input": 100, "expected": 2},  # Edge case
            {"input": 999999999, "expected": 9},  # Edge case
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

                    if "reverseWords" in user_namespace:
                        reverseWords = user_namespace['reverseWords']

                        for i, case in enumerate(test_cases):
                            input_val = case["input"]
                            expected_val = case["expected"]

                            try:
                                result = reverseWords(input_val)
                                if result == expected_val:
                                    result_placeholders[i].success(f"Test case {i + 1} passed!")
                                else:
                                    result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                            except Exception as e:
                                result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                    else:
                        error_placeholder.error("Function `reverseWords` not defined. Please define the function to proceed.")
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
def reverseWords(s):
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/10.png")  # Replace with actual image path

