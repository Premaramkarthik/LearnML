import streamlit as st
import io
import contextlib



def Q31():
    st.title("31. Calculate Digit Sum of a String")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/) for a better experience.")

    st.write("""
         **Problem**: You are given a string `s` consisting of digits and an integer `k`.
            
            A round can be completed if the length of `s` is greater than `k`. In one round, do the following:
            
            1. Divide `s` into consecutive groups of size `k` such that the first `k` characters are in the first group, 
               the next `k` characters are in the second group, and so on. Note that the size of the last group can 
               be smaller than `k`.
            2. Replace each group of `s` with a string representing the sum of all its digits. 
               For example, `"346"` is replaced with `"13"` because `3 + 4 + 6 = 13`.
            3. Merge consecutive groups together to form a new string. If the length of the string is greater than `k`, 
               repeat from step 1.

            Return `s` after all rounds have been completed.""")

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
             **Example 1**:
            - Input: `s = "11111222223", k = 3`
            - Output: `"135"`
            - Explanation: 
                - For the first round, we divide `s` into groups of size 3: `"111"`, `"112"`, `"222"`, and `"23"`.
                - Then we calculate the digit sum of each group: 
                    - `1 + 1 + 1 = 3`, 
                    - `1 + 1 + 2 = 4`, 
                    - `2 + 2 + 2 = 6`, 
                    - `2 + 3 = 5`. 
                - So, `s` becomes `"3" + "4" + "6" + "5" = "3465"` after the first round.
                - For the second round, we divide `s` into `"346"` and `"5"`.
                - Then we calculate the digit sum of each group: 
                    - `3 + 4 + 6 = 13`, 
                    - `5 = 5`. 
                - So, `s` becomes `"13" + "5" = "135"` after the second round. 
                - Now, `s.length <= k`, so we return `"135"` as the answer.
 """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `s = "00000000", k = 3`
            - Output: `"000"`
            - Explanation: 
                - We divide `s` into `"000"`, `"000"`, and `"00"`.
                - Then we calculate the digit sum of each group: 
                    - `0 + 0 + 0 = 0`, 
                    - `0 + 0 + 0 = 0`, 
                    - `0 + 0 = 0`. 
                - `s` becomes `"0" + "0" + "0" = "000"`, whose length is equal to `k`, so we return `"000"`.
       """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= s.length <= 100`")

    with colc1:
        st.write("- `2 <= k <= 100`")

    with colc2:
        st.write("- `s` consists of digits only.")

    # Topics Section
    st.write("#### Topics")
    colt, colt1 = st.columns([5, 10])

    with colt:
        st.write("""
            - **String**
        """)
    with colt1:
        st.write("""
            - **Simulation**
        """)
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: ITry simulating the entire process to find the final answer.
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(s, k):
    # Your code goes here
    passpass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ("11111222223", 3), "expected": "135"},
                {"input": ("00000000", 3), "expected": "000"},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(s, k):
    # Helper function to divide the string into parts of length 'k'
    def divideString(s, k):
        l, n = [], len(s)
        for i in range(0, n, k):  # Split string into parts of size 'k'
            l.append(s[i:min(i + k, n)])  # Add parts of string to list
        return l

    # Repeat the process while the length of 's' is greater than 'k'
    while len(s) > k:
        # Divide the string into parts
        arr, temp = divideString(s, k), [] 

        # Compute the digit sum of each group
        for group in arr: 
            group_sum = 0
            for digit in group:
                group_sum += int(digit)  # Sum digits in the group
            temp.append(str(group_sum))  # Store the sum as a string

        # Join the sums into a new string to continue the process
        s = ''.join(temp)

    # Return the resulting string when its length is <= k
    return s


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/31.png")


def Q32():
    st.title("32. minOperations the Array")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/minOperations-the-array/) for a better experience.")

    st.write("""
            **Problem**: Given the array `nums` consisting of `2n` elements in the form 
            `[x1,x2,...,xn,y1,y2,...,yn]`, return the array in the form `[x1,y1,x2,y2,...,xn,yn]`.
""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
              **Example 1**:
            - Input: `nums = [2,5,1,3,4,7], n = 3`
            - Output: `[2,3,5,4,1,7]` 
            - Explanation: Since `x1=2`, `x2=5`, `x3=1`, `y1=3`, `y2=4`, `y3=7`, then the answer is `[2,3,5,4,1,7]`.

 """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `nums = [1,2,3,4,4,3,2,1], n = 4`
            - Output: `[1,4,2,3,3,2,4,1]`
            """)
    with col3:
        st.write("""
                 **Example 3**:
            - Input: `nums = [1,1,2,2], n = 2`
            - Output: `[1,2,1,2]`
                 """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2 = st.columns(3)
    with colc:
        st.write("- `1 <= n <= 500`")

    with colc1:
        st.write("- `nums.length == 2n`")

    with colc2:
        st.write("- `1 <= nums[i] <= 10^3")

    # Topics Section
    st.write("#### Topics")
    st.write("""
        - **Array**
    """)
  
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other starting at (n+1)th position. Alternate between them and create the new array..
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(nums, n) :
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
            {"input": ([2,5,1,3,4,7], 3), "expected": [2,3,5,4,1,7]},
            {"input": ([1,2,3,4,4,3,2,1], 4), "expected": [1,4,2,3,3,2,4,1]},
            {"input": ([1,1,2,2], 2), "expected": [1,2,1,2]},
            {"input": ([10,20,30,40,50,60], 3), "expected": [10,40,20,50,30,60]},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(nums, n):
    # Initialize pointers for the left and right halves
    left = 0
    right = n
    ans = []

    # Iterate while left half has elements to be paired with the right half
    while left < n:
        ans.append(nums[left])  # Add element from the left half
        ans.append(nums[right])  # Add element from the right half
        left += 1  # Move to the next element in the left half
        right += 1  # Move to the next element in the right half
    
    return ans


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/32.png")
        

def Q33():
    st.title("33. Kids With the Greatest Number of Candies")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/) for a better experience.")

    st.write("""
             **Problem**: There are n kids with candies. You are given an integer array `candies`, 
            where `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`, 
            denoting the number of extra candies that you have.

            Return a boolean array `result` of length n, where `result[i]` is true if, after giving the ith kid all 
            the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise.
""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
             **Example 1**:
            - Input: `candies = [2,3,5,1,3], extraCandies = 3`
            - Output: `[true,true,true,false,true]` 

 """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `candies = [4,2,1,1,2], extraCandies = 1`
            - Output: `[true,false,false,false,false]` 
 """)
    with col3:
        st.write("""
            **Example 3**:
            - Input: `candies = [12,1,12], extraCandies = 10`
            - Output: `[true,false,true]`
   """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2, colc3 = st.columns(4)
    with colc:
        st.write("- `n == candies.length`")

    with colc1:
        st.write("- `2 <= n <= 100`")

    with colc2:
        st.write("- `1 <= candies[i] <= 100`")
    
    with colc3:
        st.write("""
                 
                 """)

    # Topics Section
    st.write("#### Topics")
    st.write("""
        - **Array**
    """)
  
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i].
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(candies, extraCandies):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
            {"input": ([2,3,5,1,3], 3), "expected": [True, True, True, False, True]},
            {"input": ([4,2,1,1,2], 1), "expected": [True, False, False, False, False]},
            {"input": ([12,1,12], 10), "expected": [True, False, True]},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
            def minOperations(candies, extraCandies):
                max_val = max(candies) 
                result = [] 

                for i in range(len(candies)):
                    result.append(candies[i] + extraCandies >= max_val)

                return result


            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/33.png")
            


def Q34():
    st.title("34. Number of Good Pairs")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/number-of-good-pairs/description/) for a better experience.")

    st.write("""
             **Problem**: Given an array of integers `nums`, return the number of good pairs.

            A pair (i, j) is called good if `nums[i] == nums[j]` and `i < j`.
""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
              **Example 1**:
            - Input: `nums = [1,2,3,1,1,3]`
            - Output: `4` 
            - Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

 """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `nums = [1,1,1,1]`
            - Output: `6` 
            - Explanation: Each pair in the array are good.
 """)
    with col3:
        st.write("""
            **Example 3**:
            - Input: `nums = [1,2,3]`
            - Output: `0` 
 """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1 = st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 100")

    with colc1:
        st.write("- `1 <= nums[i] <= 100")



    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Array**
                - **Hash Table**
                - **Math**
                - **counting**
            """)
  
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
            {"input": [1, 2, 3, 1, 1, 3], "expected": 4},
            {"input": [1, 1, 1, 1], "expected": 6},
            {"input": [1, 2, 3], "expected": 0},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
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

def minOperations(nums):
    frequency = Counter(nums)  
    counter = 0 
    for count in frequency.values():
        if count > 1:
            counter += (count * (count - 1)) // 2  
    return counter
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/34.png")
            


def Q35():
    st.title("35. Count the Number of Consistent Strings")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/count-the-number-of-consistent-strings/description/) for a better experience.")

    st.write("""
            **Problem**: You are given a string `allowed` consisting of distinct characters and an array of strings `words`. 
            A string is consistent if all characters in the string appear in the string `allowed`.

            Return the number of consistent strings in the array `words`.
""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
              **Example 1**:
            - Input: `allowed = "ab", words = ["ad","bd","aaab","baa","badab"]`
            - Output: `2` 
            - Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

 """)

    with col2:
        st.write("""
            **Example 2**:
            - Input: `allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]`
            - Output: `7` 
            - Explanation: All strings are consistent.
 """)
    with col3:
        st.write("""
            **Example 3**:
            - Input: `allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]`
            - Output: `4` 
            - Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2, colc3  = st.columns(4)
    with colc:
        st.write("- `1 <= words.length <= 10^4`")
        st.write("- `words[i]` and `allowed` contain only lowercase English letters.")


    with colc1:
        st.write("- `1 <= allowed.length <= 26")
    
    with colc2:
        st.write("- `1 <= words[i].length <= 10`")
        
    with colc3:
        st.write("- The characters in `allowed` are distinct.")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Strings**
                - **Hash Table**
                - **Array**
                - **Bit Manipullation**
                - **Counting**  
            """)
  
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
        **Hint 1**: A string is incorrect if it contains a character that is not allowed.
    """)
    st.write("""
        **Hint 2**: Constraints are small enough for brute force.
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(allowed, words):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
              {"input": ("ab", ["ad", "bd", "aaab", "baa", "badab"]), "expected": 2},
            {"input": ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]), "expected": 7},
            {"input": ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]), "expected": 4},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(allowed, words):
        ans = 0
        allowed = set(allowed) 
        
        for word in words:  
            word = set(word) 
            flag = True
            for ch in word:
                if ch not in allowed: 
                    flag = False
                    break
            ans += flag  
        
        return ans
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/35.png")
            


def Q36():
    st.title("36. Maximum Nesting Depth of the Parentheses")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/) for a better experience.")

    st.write("""
            **Problem**: Given a valid parentheses string `s`, return the nesting depth of `s`. 
            The nesting depth is the maximum number of nested parentheses.
""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
            **Example 1**:
            - Input: `s = "(1+(2*3)+((8)/4))+1"`
            - Output: `3`
            - Explanation: Digit 8 is inside of 3 nested parentheses in the string.

 """)

    with col2:
        st.write("""
             **Example 2**:
            - Input: `s = "(1)+((2))+(((3)))"`
            - Output: `3`
            - Explanation: Digit 3 is inside of 3 nested parentheses in the string.
 """)
    with col3:
        st.write("""
             **Example 3**:
            - Input: `s = "()(())((()()))"`
            - Output: `3`
 """)

    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1  = st.columns(2)
    with colc:
        st.write("- `1 <= s.length <= 100`")
        st.write(" - It is guaranteed that parentheses expression `s` is a VPS (valid parentheses string).")

    with colc1:
        st.write("- `s` consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Strings**
                - **Stack**
            """)
  
    
    st.write("#### **Hint :** ")
    # Follow-up Section
    st.write("""
        The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it ).
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(s):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                       {"input": "(1+(2*3)+((8)/4))+1", "expected": 3},
                        {"input": "(1)+((2))+(((3)))", "expected": 3},
                        {"input": "()(())((()()))", "expected": 3},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(s):
    stk = []
    ans=0
    for x in s:
        if x=='(':
            stk.append(x)
        elif x==')' and stk and stk[-1] == '(':
            ans=max(ans,len(stk))
            stk.pop()
    return ans
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/36.png")
            


def Q37():
    st.title("37. Determine if String Halves Are Alike")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/determine-if-string-halves-are-alike/description/) for a better experience.")

    st.write("""
             **Problem**: Given a string `s` of even length, split this string into two halves of equal lengths, 
            and let `a` be the first half and `b` be the second half.

            Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
            Return `true` if `a` and `b` are alike. Otherwise, return `false`.

""")

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
             **Example 1**:
            - Input: `s = "book"`
            - Output: `true`
            - Explanation: `a = "bo"` and `b = "ok"`. `a` has 1 vowel and `b` has 1 vowel. Therefore, they are alike.

 """)

    with col2:
        st.write("""
             **Example 2**:
            - Input: `s = "textbook"`
            - Output: `false`
            - Explanation: `a = "text"` and `b = "book"`. `a` has 1 vowel whereas `b` has 2. Therefore, they are not alike.

 """)


    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1, colc2  = st.columns(3)
    with colc:
        st.write("- `2 <= s.length <= 1000`")
      

    with colc1:
        st.write("- `s.length` is even.")

    with colc2:
        st.write("""
                 - `s` consists of uppercase and lowercase letters.
                 """)
    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Strings**
                - **Counting**
            """)
  
    
    st.write("#### **Hint :** ")
    # Follow-up Section
    st.write("""
        Create a function that checks if a character is a vowel, either uppercase or lowercase..
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(s):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": "book", "expected": True},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(s):
    cnt, cnt2, ln = 0, 0, len(s)
    vowels = set('aeiouAEIOU')
    for i in range(ln//2):
        if s[i] in vowels: cnt += 1
        if s[i+ln//2] in vowels: cnt2 += 1
    return cnt == cnt
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/37.png")
            


def Q38():
    st.title("38. Maximum Number of Words Found in Sentences")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/) for a better experience.")

    st.write("""
             **Problem**: A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
            You are given an array of strings `sentences`, where each `sentences[i]` represents a single sentence.
            
            Return the maximum number of words that appear in a single sentence.

""")

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
             **Example 1**:
            - Input: `sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]`
            - Output: `6`
            - Explanation: The first sentence has 5 words, the second has 4, and the third has 6 words. The maximum is 6.

 """)

    with col2:
        st.write("""
             **Example 2**:
            - Input: `sentences = ["please wait", "continue to fight", "continue to win"]`
            - Output: `3`
            - Explanation: The second and third sentences contain the same number of words, which is 3.

 """)


    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1  = st.columns(2)
    with colc:
        st.write("- `1 <= sentences.length <= 100`")
        st.write("""- `sentences[i]` does not have leading or trailing spaces.""")
      

    with colc1:
        st.write("- `sentences[i]` consists only of lowercase English letters and ' ' only.")
        st.write("""- All the words in `sentences[i]` are separated by a single space.""")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Strings**
                - **Array**
            """)
  
    
    st.write("#### **Hint :** ")
    # Follow-up Section
    st.write("""
       Process each sentence separately and count the number of words by looking for the number of space characters in the sentence and adding it by 1.
    """)


    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(sentences):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
                {"input": ["alice and bob love leetcode", "i think so too", "this is great thanks very much"], "expected": 6},
                {"input": ["please wait", "continue to fight", "continue to win"], "expected": 3},
                {"input": ["one", "two three", "four five six seven"], "expected": 4},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(*input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(sentences):
    m=0
    for i in sentences:
        c=0
        for j in i:
            if j == ' ':
                c+=1
        m=max(m,c+1)
    return m
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/38.png")
            


def Q39():
    st.title("39. Maximum Number of Words Found in Sentences")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/) for a better experience.")

    st.write("""
            **Problem**: Given a string `s`, return true if `s` is a good string, or false otherwise.
            
            A string `s` is good if all the characters that appear in `s` have the same number of occurrences.

""")

    # Examples Section with two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
             **Example 1**:
            - Input: `s = "abacbc"`
            - Output: `true`
            - Explanation: The characters that appear in `s` are 'a', 'b', and 'c'. All characters occur 2 times in `s`.

 """)

    with col2:
        st.write("""
           
            **Example 2**:
            - Input: `s = "aaabb"`
            - Output: `false`
            - Explanation: The characters that appear in `s` are 'a' and 'b'. 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

 """)


    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1  = st.columns(2)
    with colc:
        st.write("- `1 <= s.length <= 1000`")
     
    with colc1:
        st.write("- `s` consists of lowercase English letters.")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Strings**
                - **Hash Table**
                - **Counting**
            """)
  
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
       -**Hint 1:** Build a dictionary containing the frequency of each character appearing in s
    """)
    st.write("""
       -**Hint 2:** Check if all values in the dictionary are the same.""")

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(s):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": "abacbc", "expected": True},
                {"input": "aaabb", "expected": False},
                {"input": "abcabc", "expected": True},
                {"input": "aabbcc", "expected": True},
                {"input": "abc", "expected": True},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(s):
        d = {}

        for i in s:
            d[i] = d.get(i,0) + 1

        values = list(d.values())

        first_value = values[0]
        
        index = 0
        length = len(values)

        while index < length:
            if first_value != values[index]:
                return False
            index+=1
        return True
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/39.png")
        

def Q40():
    st.title("40. Minimum Operations to Make the Array Increasing")
    
    st.markdown("[Visit Leetcode](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/) for a better experience.")

    st.write("""
           **Problem**: You are given an integer array `nums` (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

            Return the minimum number of operations needed to make `nums` strictly increasing.

            An array `nums` is strictly increasing if `nums[i] < nums[i+1]` for all `0 <= i < nums.length - 1`. An array of length 1 is trivially strictly increasing.

""")

    # Examples Section with two columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
           **Example 1**:
            - Input: `nums = [1,1,1]`
            - Output: `3`
            - Explanation: Increment operations to make it strictly increasing.

 """)

    with col2:
        st.write("""
           
           **Example 2**:
            - Input: `nums = [1,5,2,4,1]`
            - Output: `14`

 """)
    with col3:
        st.write("""
           
           **Example 3**:
            - Input: `nums = [8]`
            - Output: `0`

 """)


    # Constraints Section with Subheading
    st.subheader("Constraints")
    colc, colc1  = st.columns(2)
    with colc:
        st.write("- `1 <= nums.length <= 5000`")
     
    with colc1:
        st.write("- `1 <= nums[i] <= 10^4")

    # Topics Section
    st.write("#### Topics")
    st.write(""" 
                - **Array**
                - **Greedy**
            """)
    
    st.write("#### **Hints :** ")
    # Follow-up Section
    st.write("""
       -**Hint 1:** nums[i+1] must be at least equal to nums[i] + 1.
    """)
    st.write("""
       -**Hint 2:** Think greedily. You don't have to increase nums[i+1] beyond nums[i]+1.""")
    st.write("""
       -**Hint 3:** Iterate on i and set nums[i] = max(nums[i-1]+1, nums[i]).""")

    # Solution Section with updated column widths
    colLeft, colMid, colRight = st.columns([1.8, 1, 1])

    with colLeft:
        st.markdown("#### Solve the Problem")

        code_input = st.text_area(
            "Write your Python function here:",
            height=300,
            value="""def minOperations(nums):
    # Your code goes here
    pass
    """
        )

        colTest, colRun = st.columns([5, 1])

        with colTest:
            # Predefined test cases to evaluate the user's function
            test_cases = [
               {"input": [1, 1, 1], "expected": 3},
                {"input": [1, 5, 2, 4, 1], "expected": 14},
                {"input": [8], "expected": 0},
                {"input": [1, 2, 3], "expected": 0},
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

                        # Check if the function `minOperations` is defined
                        if "minOperations" in user_namespace:
                            minOperations = user_namespace['minOperations']

                            # Run the function on all test cases
                            for i, case in enumerate(test_cases):
                                input_val = case["input"]
                                expected_val = case["expected"]

                                try:
                                    result = minOperations(input_val)
                                    if result == expected_val:
                                        result_placeholders[i].success(f"Test case {i + 1} passed!")
                                    else:
                                        result_placeholders[i].error(f"Test case {i + 1} failed: Expected {expected_val}, but got {result}")
                                except Exception as e:
                                    result_placeholders[i].error(f"Test case {i + 1} raised an error: {e}")
                        else:
                            error_placeholder.error("Function `minOperations` not defined. Please define the function to proceed.")
                except Exception as e:
                    error_placeholder.error(f"Error executing code: {e}")

                output = buffer.getvalue()
                if output:
                    st.subheader("Execution Output:")
                    st.text(output)

    with colMid:
        with st.expander("Sample Answer (NOTE: Each question can have different solutions)", expanded=False):
            st.code("""
def minOperations(nums):

        n = len(nums)
        if n == 1:
            return 0  
        
        ans = 0
        index = 1  

        while index < n:
            if nums[index] <= nums[index - 1]:
                ans += nums[index - 1] - nums[index] + 1
                nums[index] = nums[index - 1] + 1
            
            index += 1  
        return ans
            """)

    with colRight:
        with st.expander("Flowchart of Sample Answer", expanded=False):
            st.image("pages/images/intermediate/40.png")