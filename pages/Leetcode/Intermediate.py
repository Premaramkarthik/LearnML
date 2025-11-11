import streamlit as st
import sys
import os

# Ensure the path is correct and consistent (fix capitalization if needed)
sys.path.append(os.path.abspath('pages/Leetcode/my_code'))

# Import the question functions from the correct module path
from pages.Leetcode.my_code.intermediate_questions1 import Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
from pages.Leetcode.my_code.intermediate_questions2 import Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20
from pages.Leetcode.my_code.intermediate_questions3 import Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30
from pages.Leetcode.my_code.intermediate_questions4 import Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40
from pages.Leetcode.my_code.intermediate_questions5 import Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50

st.title("Welcome to Intermediate Questions")
    
options = ['1. Length of Last Word', '2. Merge Sorted Array II', '3. Remove duplicates from sorted list', '4. Unique number of occurrences', '5. Rings and Rods',
 '6. Left and Right Sum Differences', '7. Calculate Delayed Arrival Time for a train', '8. Number of Steps to Reduce a Number to Zero', '9. Count the Digits That Divide a Number',
 '10. Reverse words in a string III',
 
 '11. Find N Unique Integers Sum up to Zero', '12. Substrings of Size Three with Distinct Characters', '13. Sum of All Odd Length Subarrays',
 "14. Majority Element", '15. Maximum Number of Balls in a Box', '16. Concatenation of Array', '17. Prime Number of Set Bits in Binary Representation',
 '18. Fibonacci Number',  '19. Goal Parser Interpretation', '20. Sort the People',
 
 '21. Cells in a Range on an Excel Sheet', '22. Sorting the Sentence', '23. Count Number of Pairs With Absolute Difference K',
 '24. To Lower Case', '25. Check if Number Has Equal Digit Count and Digit Value', '26. Count Asterisks', '27. Find Words That Can Be Formed by Characters', '28. Jewels and stones',
 '29. Divide a string in group of size k','30. Truncate sentence', 
 
 '31. Calculate digit sum of string', '32. Shuffle the Array', '33. Kids With the Greatest Number of Candies', '34. Number of Good Pairs',
 '35. Count the Number of Consistent Strings', '36. Maximum Nesting Depth of the Parentheses', '37. Determine if String Halves Are Alike',
 '38. Max num of words found in sentences', '39. Check if All Characters Have Equal Number of Occurrences', '40. Minimum Operations to Make the Array Increasing',
 
 '41. Number of Common Factors', '42. Minimum Common Value','43. Average Value of Even Numbers that are divisible by Three','44. Convert Binary Number in a Linked List to I', '45. Minimum Number of Movies to Seat Everyone',
 '46. How Many Numbers are smaller than the current number', '47. Running Sum of 1d Array', '48. Apply Transform Over Each Element in Array','49. Convert The Temperature', 
 '50. Remove Vowels from a String']

selected_question = st.selectbox("Check out the question", options=options)

match selected_question:
    
    case '1. Length of Last Word':
        Q1()
    
    case '2. Merge Sorted Array II':
        Q2()
    
    case '3. Remove duplicates from sorted list':
        Q3()
    
    case '4. Unique number of occurrences':
        Q4()
    
    case '5. Rings and Rods':
        Q5()
    
    case '6. Left and Right Sum Differences':
        Q6()
    
    case '7. Calculate Delayed Arrival Time for a train':
        Q7()
    
    case '8. Number of Steps to Reduce a Number to Zero':
        Q8()
    
    case '9. Count the Digits That Divide a Number':
        Q9()
    
    case '10. Reverse words in a string III':
        Q10()
        
    case '11. Find N Unique Integers Sum up to Zero':
        Q11()
    
    case '12. Substrings of Size Three with Distinct Characters':
        Q12()
    
    case '13. Sum of All Odd Length Subarrays':
        Q13()
    
    case '14. Majority Element':
        Q14()
    
    case '15. Maximum Number of Balls in a Box':
        Q15()
    
    case '16. Concatenation of Array':
        Q16()
    
    case '17. Prime Number of Set Bits in Binary Representation':
        Q17()
    
    case '18. Fibonacci Number':
        Q18()
    
    case '19. Goal Parser Interpretation':
        Q19()
    
    case '20. Sort the People':
        Q20()

        
    case '21. Cells in a Range on an Excel Sheet':
        Q21()
    
    case '22. Sorting the Sentence':
        Q22()
    
    case '23. Count Number of Pairs With Absolute Difference K':
        Q23()
    
    case '24. To Lower Case':
        Q24()
    
    case '25. Check if Number Has Equal Digit Count and Digit Value':
        Q25()
    
    case '26. Count Asterisks':
        Q26()
    
    case '27. Find Words That Can Be Formed by Characters':
        Q27()
    
    case '28. Jewels and stones':
        Q28()
    
    case '29. Divide a string in group of size k':
        Q29()
    
    case '30. Truncate sentence':
        Q30()


    case '31. Calculate digit sum of string':
        Q31()  
    
    case '32. Shuffle the Array':
        Q32()
    
    case '33. Kids With the Greatest Number of Candies':
        Q33()
    
    case '34. Number of Good Pairs':
        Q34()
        
    case "35. Count the Number of Consistent Strings":
        Q35()
        
    case '36. Maximum Nesting Depth of the Parentheses':
        Q36()        
    
    case '37. Determine if String Halves Are Alike':
        Q37()
        
    case '38. Max num of words found in sentences':
        Q38()
        
    case '39. Check if All Characters Have Equal Number of Occurrences':
        Q39()
        
    case '40. Minimum Operations to Make the Array Increasing':
        Q40()
    
    case '41. Number of Common Factors':
        Q41()
    
    case '42. Minimum Common Value':
        Q42()
    
    case '43. Average Value of Even Numbers that are divisible by Three':
        Q43()
    
    case '44. Convert Binary Number in a Linked List to I':
        Q44()
    
    case '45. Minimum Number of Movies to Seat Everyone':
        Q45()
    
    case '46. How Many Numbers are smaller than the current number':
        Q46()
    
    case '47. Running Sum of 1d Array':
        Q47()
    
    case '48. Apply Transform Over Each Element in Array':
        Q48()
    
    case '49. Convert The Temperature':
        Q49()
    
    case '50. Remove Vowels from a String':
        Q50()
