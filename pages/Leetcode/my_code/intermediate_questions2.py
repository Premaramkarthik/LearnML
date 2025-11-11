import streamlit as st
import contextlib
import io



def Q11():
    st.title("11. Find N Unique Integers Sum up to Zero")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) for a better experience.")


    # Left column: Display the problem description
    st.write("""
                  **Problem**: Given an integer `n`, return any array containing `n` unique integers such that they add up to `0`.
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                 **Example 1**:
            - Input: `n = 5`
            - Output: `[-7,-1,1,3,4]`
            - Explanation: These arrays also are accepted `[-5,-1,1,2,3]`, `[-3,-1,2,-2,4]`.
                """)
    with col2:
        st.write("""
                **Example 2**:
            - Input: `n = 3`
            - Output: `[-1,0,1]`
       """)
    with col3:
        st.write("""
                 **Example 3**:
            - Input: `n = 1`
            - Output: `[0]`

       """)
        
    st.write("**Constraints:**")
    st.write('- `1 <= n <= 1000`')
    
    # Topics
    st.write("#### Topics")
    st.write("""
                - **String**
                - **Hash Table**
                - **Sliding Window**
                - **Counting**
            """)

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sumZero(n):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               
            {"input": 5, "expected": {i for i in range(-2, 3) if i != 0}},
            {"input": 3, "expected": {0, -1, 1}},
            {"input": 1, "expected": {0}},
        
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

                        # Check if the function sort_people is defined
                        if "sumZero" in user_namespace:
                            sumZero = user_namespace['sumZero']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sumZero(input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        st.write(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `max_value` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def sumZero(n):
    return [i for i in range(-n // 2, n // 2 + 1) if i != 0] if n % 2 == 0 else [i for i in range(-n // 2, n // 2 + 1)]
  
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/11.png")


def Q12():
    st.title("12. substring of distinct characters")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/ )for a better experience.")


    # Left column: Display the problem description
    st.write("""
                **Problem**: A string is good if there are no repeated characters.Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
    Note that if there are multiple occurrences of the same substring, every occurrence should be counted.A substring is a contiguous sequence of characters in a string.
    """)
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
                **Example 1**:
                - Input: s="xyzzaz"
                - Output: 1
                - Explanation:There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
    #The only good substring of length 3 is "xyz".
                """)
    with col2:
        st.write("""
                 **Example 2**:

                - Input: s = "aababcabc"
                - Output: 4
                - Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
                - The good substrings are "abc", "bca", "cab", and "abc".
                 """)
        
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= s.length <= 100")
    with colc1:
        st.write("- s consists of lowercase English letters.")
    
    # Topics
    st.write("#### Topics")
    st.write("""
                - **String**
                - **Hash Table**
                - **Sliding Window**
                - **Counting**
            """)

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sumZero(s):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ("xyzzaz",), "expected": 1}
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

                        # Check if the function sort_people is defined
                        if "sumZero" in user_namespace:
                            sumZero = user_namespace['sumZero']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sumZero(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                        st.write(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `max_value` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def sumZero(s):
            c=0
            for i in range(len(s)-3+1):
            d={}
            e=0
            for j in range(i,i+3):
                if s[j] in d:
                    d[s[j]]=d[s[j]]+1
                else:
                    d[s[j]]=1
                    for k in d:
                        e=max(e,d[k])
                        if(e==1):
                            c=c+1
            return (c)
    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/12.png")



def Q13():
    st.title("13. sum of all old length subarrays")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/) for a better experience.")

    st.write("""
                **Problem**:
                Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
    #A subarray is a contiguous subsequence of the array.
    """)
    # Create columns for examples
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        **Example 1**:
        - Input: arr = [1,4,2,5,3]
        - Output: 58
        - Explanation: The odd-length subarrays of arr and their sums are:
        -[1] = 1
        -[4] = 4
        -[2] = 2
        -[5] = 5
        -[3] = 3
        -[1,4,2] = 7
        -[4,2,5] = 11
        -[2,5,3] = 10
        -[1,4,2,5,3] = 15
        -If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
        """)
    with col2:
        st.write("""
                **Example 2**:
                -Input: arr = [1,2]
                -Output: 3
                -Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
    """)
    st.write("**Constraints:**")
    colc, colc1 = st.columns([1,13])
    with colc:
        st.write("- 1 <= arr.length <= 100")
    with colc1:
        st.write("- 1 <= arr[i] <= 1000")
    
    
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Sliding Window**
                - **Prefix Sum**
            """)
        
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
                "Write your Python function here:",
                height=300,
                value="""def sumOddLengthSubarraysLengthSubarrays(arr):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": [1, 4, 2, 5, 3], "expected": 58},
                 {"input": [1, 2], "expected": 3},
                {"input": [10, 11, 12], "expected": 66},
            ]

            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function majorityElement is defined
                        if "majorityElement" in user_namespace:
                            majorityElement = user_namespace['majorityElement']  # Get the function
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = majorityElement(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passes!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `majorityElement` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
                st.code("""def sumOddLengthSubarraysLengthSubarrays(arr):
                    total_sum = 0
                    n = len(arr)

                    for i in range(n):
                        for j in range(i, n):
                            if (j - i + 1) % 2 == 1:  # Check for odd length
                                total_sum += sum(arr[i:j + 1])
                    return total_sum
    """)

        # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/13.png")
            

def Q14():
    st.title("14.  Majority Element")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/majority-element/) for a better experience.")

    st.write("""
               **Problem**: Given an array `nums` of size `n`, return the majority element.
            
            The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
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
        
    st.write("**Constraints:**")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `n == nums.length`")
    with colc1:
        st.write("- `1 <= n <= 5 * 10^4`")
    with colc2:
        st.write("- `-10^9 <= nums[i] <= 10^9`")
    
    st.write("#### Topics")
    st.write("""
                - **Array**
                - **Sliding Window**
                - **Prefix Sum**
            """)
        
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        code_input = st.text_area(
                "Write your Python function here:",
                height=300,
                value="""def majorityElement(nums):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                 {"input": [3, 2, 3], "expected": 3},
            {"input": [2, 2, 1, 1, 1, 2, 2], "expected": 2},
            ]

            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function majorityElement is defined
                        if "majorityElement" in user_namespace:
                            majorityElement = user_namespace['majorityElement']  # Get the function
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = majorityElement(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passes!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `majorityElement` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
                st.code("""def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
    """)

        # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/14.png")

def Q15():
    st.title("1742.Max number of balls in a box")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/getConcatenation-of-array/description/) for a better experience.")
    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)
    # Left column: Display the problem description
    st.write("""
                *Problem*:
                You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1),
    and an infinite number of boxes numbered from 1 to infinity.Your job at this factory is to put each ball in the box with a number equal to the
    sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and
    the ball number 10 will be put in the box number 1 + 0 = 1.Given two integers lowLimit and highLimit, return the number of balls in the box
    with the most balls.
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("""
        -Example 1:Input: lowLimit = 1, highLimit = 10
        -Output: 2
        -Explanation:
        -Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
        -Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
        -Box 1 has the most number of balls with 2 balls."""
        )
    
    with col2:
        st.write("""
       **Example 2**:
            - Input: `lowLimit = 5, highLimit = 15`
            - Output: `2`
            - Explanation: Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
            Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
            Boxes 5 and 6 have the most number of balls with 2 balls in each.
        """)
        
    with col3:
        st.write("""
       **Example 3**:
            - Input: `lowLimit = 19, highLimit = 28`
            - Output: `2`
            - Explanation: Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
            Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
            Box 10 has the most number of balls with 2 balls.
        """)
    
    
    
    # Constraints section
    st.write("**Constraints:**")
    colc = st.columns(1)
    with colc:
        st.write(" 1 <= lowLimit <= highLimit <= 10^5")

    st.write("#### Topics")
    st.write("""
                - **Hash Map**
                - **Mathematics**
            """)
        
        
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def Balls(l,h):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": (1, 10), "expected": 2},
            {"input": (5, 15), "expected": 2},
            {"input": (19, 28), "expected": 2},
            ]

            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function majorityElement is defined
                        if "majorityElement" in user_namespace:
                            majorityElement = user_namespace['majorityElement']  # Get the function
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = majorityElement(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passes!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `majorityElement` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
                    
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def majorityElement(lowLimit, highLimit):
                    box_count = {}

                    for num in range(lowLimit, highLimit + 1):
                        box_number = sum(int(digit) for digit in str(num))
                        if box_number in box_count:
                            box_count[box_number] += 1
                        else:
                            box_count[box_number] = 1

                    return max(box_count.values())
    """)

        # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/15.png")


def Q16():
    st.title("16. getConcatenation of arrays")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/getConcatenation-of-array/description/) for a better experience.")

    # Create two columns: left for question, right for code input
    col1, col2 = st.columns(2)
    # Left column: Display the problem description
    st.write("""
                **Problem**: Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where
            `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed). Specifically, `ans` is the getConcatenation of two `nums` arrays.
    """)
    col1  = st.columns(1)
    with col1:
        st.write("""
                **Example 1**:
            - Input: `nums = [1, 2, 1]`
            - Output: `[1, 2, 1, 1, 2, 1]`
            - Explanation: The array `ans` is formed as follows: `ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]`
 """)
    
        st.write("""
                 **Example 2**:
            - Input: `nums = [1, 3, 2, 1]`
            - Output: `[1, 3, 2, 1, 1, 3, 2, 1]`
            - Explanation: The array `ans` is formed as follows: `ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]`
 """)
        
    st.write("**Constraints:**")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `n == nums.length``")
    with colc1:
        st.write("- `1 <= n <= 1000`")
    with colc2:
        st.write("- `1 <= nums[i] <= 1000`")

    st.write("#### Topics")
    st.write("""
                - **Array**
                - **getConcatenation**
            """)
        
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")

            # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def getgetConcatenation(arr):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])
        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": [1, 2, 1], "expected": [1, 2, 1, 1, 2, 1]},
            {"input": [1, 3, 2, 1], "expected": [1, 3, 2, 1, 1, 3, 2, 1]},
            {"input": [5, 7, 9], "expected": [5, 7, 9, 5, 7, 9]},
            ]

            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function getConcatenation is defined
                        if "getConcatenation" in user_namespace:
                            getConcatenation = user_namespace['getConcatenation']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = getConcatenation(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `Concatination` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def getgetConcatenation(arr):
            a=list(map(int,input().split()))
            n=len(a)
            b=[0]*(2*n)
            for i in range(2*n):
                b[i]=a[(i%n)]
            return (b)

    """)

    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/16.png")
            
        
def Q17():
    st.title("17.prime number of set bits ")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/) for a better experience.")

    st.write("""
              **Problem**: Given two integers `left` and `right`, return the count of numbers in the inclusive range `[left, right]` having a prime number of set bits in their binary representation.

            Recall that the number of set bits an integer has is the number of `1's` present when written in binary.

          """)

    col1, col2 = st.columns(2)
    # Topics
    with col1:
        st.write("""
        **Example 1**:
        -Input: left = 6
        -right = 10
        -Output: 4
        -Explanation:
        -6  -> 110 (2 set bits, 2 is prime)
        -7  -> 111 (3 set bits, 3 is prime)
        -8  -> 1000 (1 set bit, 1 is not prime)
        -9  -> 1001 (2 set bits, 2 is prime)
        -10 -> 1010 (2 set bits, 2 is prime)
        -4 numbers have a prime number of set bits.""")
    
    with col2:
        st.write("""
                 
                 **Example 2**:
            - Input: `left = 10`, `right = 15`
            - Output: `5`
            - Explanation:
              - 10 -> 1010 (2 set bits, 2 is prime)
              - 11 -> 1011 (3 set bits, 3 is prime)
              - 12 -> 1100 (2 set bits, 2 is prime)
              - 13 -> 1101 (3 set bits, 3 is prime)
              - 14 -> 1110 (3 set bits, 3 is prime)
              - 15 -> 1111 (4 set bits, 4 is not prime)
              - 5 numbers have a prime number of set bits.
                 
                 """)
        
    # Constraints section
    st.write("**Constraints:**")
    st.write("""
             - 1 <= left <= right <= 10^6
            - 0 <= right - left <= 10^4
             """)

    st.write("#### Topics")
    st.write("""
                - **Bit Manipulation**
                - **Mathematics**
                - **Counting**
            """)

    

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
        "Write your Python function here:",
        height=300,
        value="""def interpret(left, right):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": (6, 10), "expected": 4},
            {"input": (10, 15), "expected": 5},
            {"input": (1, 5), "expected": 3},
            ]

            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function interpret is defined
                        if "interpret" in user_namespace:
                            interpret = user_namespace['interpret']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = interpret(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `interpret` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def interpret(left, right):
        def isPrime(n):
            count=0
            for i in range(1,n+1) :
                if n%i==0:
                    count+=1
            if count==2 :
                return True
            else:
                return False
        countp=0
        for i in range(left,right+1) :
            ans = bin(i).count("1")
            if isPrime(ans) :
                countp+=1
        return countp
    """)

        # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/17.png")

def Q18():
    st.title("509 interpretonacci number")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/interpretonacci-number/description/")
    st.write("""
                **Problem**: The interpretonacci numbers, commonly denoted F(n) form a sequence, called the interpretonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    """)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                **Example 1**:
                - Input:  n = 2
                - Output: =1
                - Explanation:
                - F(2) = F(1) + F(0) = 1 + 0 = 1.
                - l=[0,1]
                """)
    
    with col2:
        st.write("""
                **Example 2**:
            - Input: `n = 3`
            - Output: `2`
            - Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
""")
    
    with col3:
        st.write("""
                **Example 3**:
            - Input: `n = 4`
            - Output: `3`
            - Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 """)
        
    st.write("**Constraints:**")
    colc = st.columns(1)
    with colc:
        st.write("- 0 <= n <= 30")
 
    
    st.write("#### Topics")
    st.write("""
                - **Dynamic Programming**
                - **Recursion**
                - **Mathematics**
            """)
    

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
        "Write your Python function here:",
            height=300,
            value="""def interpret(n):
        # Your code goes here
        pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": 2, "expected": 1},
            {"input": 3, "expected": 2},
            {"input": 4, "expected": 3},
            {"input": 5, "expected": 5},
            {"input": 6, "expected": 8},
            ]
            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function interpret is defined
                        if "interpret" in user_namespace:
                            interpret = user_namespace['interpret']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = interpret(*input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `interpret` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def interpret(n):
    if n <= 1:
        return n
    return interpret(n - 1) + interpret(n - 2)
    """)
    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/18.png")
            

def Q19():
    st.title("19. Goal Parser Interpretation")

    st.markdown("[Visit Leetcode](https://leetcode.com/problems/goal-parser-interpretation/) for better experience.")

    st.write("""
               **Problem**: You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

            Given the string command, return the Goal Parser's interpretation of the command.
    """)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
                   **Example 1**:
            - Input: `command = "G()(al)"`
            - Output: `"Goal"`
            - Explanation: The Goal Parser interprets the command as follows:
              - `G` -> G
              - `()` -> o
              - `(al)` -> al
              - The final concatenated result is "Goal".

                """)
    
    with col2:
        st.write("""
               
            **Example 2**:
            - Input: `command = "G()()()()(al)"`
            - Output: `"Gooooal"`
            """)
    
    with col3:
        st.write("""
                **Example 3**:
            - Input: `command = "(al)G(al)()()G"`
            - Output: `"alGalooG"`
 """)
        
    st.write("**Constraints:**")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- 1 <= command.length <= 100")
    
    with colc1:
        st.write('- command consists of "G", "()", and/or "(al)" in some order.')
 
    
    st.write("#### Topics")
    st.write("""
                - **String Manipulation**
                - **Parsing**
            """)
    

    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
        # Code input box for the user to write their solution
        code_input = st.text_area(
        "Write your Python function here:",
            height=300,
            value="""def interpret(command):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": "G()(al)", "expected": "Goal"},
            {"input": "G()()()()(al)", "expected": "Gooooal"},
            {"input": "(al)G(al)()()G", "expected": "alGalooG"},
            ]
            # Display the test cases in expanders
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
            # Button to execute the code
            if st.button("Run Code"):
                buffer = io.StringIO()

                # Try to safely execute the user code
                try:
                    # Redirect stdout to buffer and run the code
                    with contextlib.redirect_stdout(buffer):
                        user_namespace = {}
                        exec(code_input, user_namespace)  # Execute the user code

                        # Check if the function interpret is defined
                        if "interpret" in user_namespace:
                            interpret = user_namespace['interpret']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = interpret(input_val)  # Unpack input for the function
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `interpret` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)
    with colMid:
        with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
            st.code("""def interpret(n):
    if n <= 1:
        return n
    return interpret(n - 1) + interpret(n - 2)
    """)
    # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/19.png")
            
            
def Q20():
    st.title("20. sort the people")
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/sort-the-people/description/) for a better experience.")

    st.write("""
                **Problem**: You are given an array of strings `names`, and an array `heights` that consists of distinct positive integers. Both arrays are of length `n`.

            For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i`th person.

            Return `names` sorted in descending order by the people's heights.
    """)
    
    col1 = st.columns(1)
    with col1:
        st.write("""
               **Example 1**:
            - Input: `names = ["Mary","John","Emma"], heights = [180,165,170]`
            - Output: `["Mary","Emma","John"]`
            - Explanation: Mary is the tallest, followed by Emma and John.
 """)

        st.write("""
                 **Example 2**:
            - Input: `names = ["Alice","Bob","Bob"], heights = [155,185,150]`
            - Output: `["Bob","Alice","Bob"]`
            - Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 """)

    # Constraints section
    st.write("**Constraints:**")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `n == names.length == heights.length`")
        st.write("- `1 <= heights[i] <= 10^5`")
    with colc1:
        st.write("- `1 <= n <= 10^3`")
        st.write("- `names[i]` consists of lower and upper case English letters.`")
    with colc2:
        st.write("- `1 <= names[i].length <= 20`")
        st.write(" All the values of heights are distinct.")

    # Topics
    st.write("#### Topics")
    st.write("""
                - **Sorting**
                - **Array**
                - **String**
            """)
        
        
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])
    with colLeft:
        st.markdown("#### Solve the Problem")
    # Code input box for the user to write their solution
        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def sort_people(names, heights):
    # Your code goes here
    pass
    """)

        colTest, colRun = st.columns([5, 1])
        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": (["Mary","John","Emma"],[180,165,170],), "expected": ["Marry","Emma","John"]}]
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

                        # Check if the function sort_people is defined
                        if "sort_people" in user_namespace:
                            sort_people = user_namespace['sort_people']  # Get the function

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = sort_people(*input_val)  # Unpack input for the function
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
                # Display any print outputs or errors captured
                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

        with colMid:
            with st.expander("Sample Answer (NOTE: Every question has different solutions)", expanded=False):
                st.code("""def sort_people(names, heights):
                    combined = sorted(zip(heights, names), reverse=True)
                    return [name for height, name in combined]
    """)

        # Right column: Display flowchart of sample answer
    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/20.png")
