
import streamlit as st
import sys
import os

# Ensure the path is correct and consistent (fix capitalization if needed)
sys.path.append(os.path.abspath('pages/Leetcode/my_code'))

# Import the question functions from the correct module path
from pages.Leetcode.my_code.easy_question1 import Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
from pages.Leetcode.my_code.easy_question2 import Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20
from pages.Leetcode.my_code.easy_question3 import Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30
from pages.Leetcode.my_code.easy_question4 import Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40
from pages.Leetcode.my_code.easy_question5 import Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50



def app():
    # Set title with the custom color
    st.markdown("<h2>Welcome to Easy LeetCode Questions</h2>", unsafe_allow_html=True)
    
    # List of available questions with the same style
    options = [
        '1. Two Sum', '2. Palindrome Number', '3. Roman to Integer', "4. Merge Sorted Array","5. Best Time to Buy and Sell Stock", "6. Maximum Subarray", "7. Plus One", "8. Climbing Stairs", "9. Single Number", "10. Check if Word Equals Summation of Two Words",
        
        "11. Build Array from Permutation","12. Valid Parentheses" ,"13. Maximum Number of Vowels in a Substring of Given Length","14. Excel sheet column number","15. Majority elements","16. Contain Duplicates","17. Zero permutation" ,"18. Build Array from Permutation","19. Moves Zeroes","20. Ransom Note"
        
        '21. Maximum value of a string in an array', '22. Replace all digit with characters', '23. Reverse prefix of word',  '24. Robot return to Origin',
        '25. Self Dividing Numbers', '26. Unique Morse Code Words', '27. Flipping an Image',  '28. Richest customer wealth',
        '29. Sort Array By Parity', '30. N-Repeated Element in Size 2N Array', 
        
        '31. Squares of a Sorted Array', '32. Three Consecutive Odds', '33. Find Common Characters',
        "34. Check If It Is a Straight", "35. Decompress Run-Length Encoded List",
        "36. How Many Numbers Are Smaller Than the Current Number","37. Create Target Array in the Given Order",
        "38. Check if the Sentence Is Pangram","39. Maximum Product Difference Between Two Pairs",
        "40. Count Good Triplets", 
        
        
        '41. Subtract the product and sum of digits of an integer','42. Add Two Integers', '43. Divisor Game',
        '44. Generate Fibonacci Sequence', '45.Generate a String With Characters That Have Odd Counts', '46. Sum Multiples', '47. Find Anagram Mappings',
        '48. Sum of Unique Elements', '49. Alternating digit sum', '50. Find closest number to zero'
    ]
    
    # Styled selectbox for selecting a question
    selected_question = st.selectbox("Check out the question", options=options)

    # Use match-case to display questions and their solutions
    match selected_question:
        case '1. Two Sum':
            #st.markdown("<h3 style='color:#064747;'> 1. Two Sum</h3>", unsafe_allow_html=True)
            Q1()  # Call the corresponding function
            
        case '2. Palindrome Number':
            #st.markdown("<h3 style='color:#064747;'> 9. Palindrome</h3>", unsafe_allow_html=True)
            Q2()  # Call the corresponding 
            
        case '3. Roman to Integer':
            #st.markdown("<h3 style='color:#064747;'>13. Roman to Integer</h3>", unsafe_allow_html=True)
            Q3()  # Call the corresponding function
            
        case "4. Merge Sorted Array":
            Q4()
            
        case "5. Best Time to Buy and Sell Stock":
            Q5()
            
        case "6. Maximum Subarray":
            Q6()
            
        case "7. Plus One":
            Q7()
            
        case "8. Climbing Stairs":
            Q8()
            
        case "9. Single Number":
            Q9()
            
        case "10. Check if Word Equals Summation of Two Words":
            Q10()
            
        case "11. Build Array from Permutation":
            Q11()
        
        case "12. Valid Parentheses":
            Q12()
        case "13. Maximum Number of Vowels in a Substring of Given Length":
            Q13()
        
        case "14. Excel sheet column number":
            Q14()
        
        case "15. Majority elements":
            Q15()
        
        case "16. Contain Duplicates":
            Q16()
        
        case "17. Zero permutation":
            Q17()
        
        case  "18. Build Array from Permutation":
            Q18()
        
        case "19. Moves Zeroes":
            Q19()
        
        case "20. Ransom Note":
            Q20
        
        case "21. Maximum value of a string in an array":
            Q21()
             
        case "22. Replace all digit with characters":
            Q22()
            
        case "23. Reverse prefix of word":
            Q23()
            
        case "24. Robot return to Origin":
            Q24()
            
        case "25. Self Dividing Numbers":
            Q25()
            
        case "26. Unique Morse Code Words":
            Q26()
            
        case "27. Flipping an Image":
            Q27()
            
        case "28. Richest customer wealth":
            Q28()
            
        case "29. Sort Array By Parity":
            Q29()
            
        case "30. N-Repeated Element in Size 2N Array":
            Q30()
            
        case "31. Squares of a Sorted Array":
            #st.markdown("<h3 style='color:#064747;'>977. Squares of a Sorted Array</h3>", unsafe_allow_html=True)
            Q31()  # Call the corresponding function
            
        case '32. Three Consecutive Odds':
            #st.markdown("<h3 style='color:#064747;'>1550. Three Consecutive Odds</h3>", unsafe_allow_html=True)
            Q32()  # Call the corresponding function
            
        case '33. Find Common Characters':
            #st.markdown("<h3 style='color:#064747;'>1002. Find Common Characters</h3>", unsafe_allow_html=True)
            Q33()  # Call the corresponding function
            
        case "34. Check If It Is a Straight":
            #st.markdown("<h3 style='color:#064747;'>1002. Find Common Characters</h3>", unsafe_allow_html=True)
            Q34()  # Call the corresponding function
            
        case "35. Decompress Run-Length Encoded List":
            #st.markdown("<h3 style='color:#064747;'>1313. Decompress Run-Length Encoded List</h3>", unsafe_allow_html=True)
            Q35()  # Call the corresponding function
            
        case "36. How Many Numbers Are Smaller Than the Current Number":
            #st.markdown("<h3 style='color:#064747;'>1365. How Many Numbers Are Smaller Than the Current Number</h3>", unsafe_allow_html=True)
            Q36()  # Call the corresponding function
            
        case "37. Create Target Array in the Given Order":
            #st.markdown("<h3 style='color:#064747;'>1389. Create Target Array in the Given Order</h3>", unsafe_allow_html=True)
            Q37()  # Call the corresponding function
            
        case "38. Check if the Sentence Is Pangram":
            st.markdown("<h3 style='color:#064747;'>1832. Check if the Sentence Is Pangram</h3>", unsafe_allow_html=True)
            Q38()  # Call the corresponding function
            
        case "39. Maximum Product Difference Between Two Pairs":      
            #st.markdown("<h3 style='color:#064747;'>1913. Maximum Product Difference Between Two Pairs</h3>", unsafe_allow_html=True)
            Q39()  # Call the corresponding function
            
        case "40. Count Good Triplets":
            #st.markdown("<h3 style='color:#064747;'>1534. Count Good Triplets </h3>", unsafe_allow_html=True)
            Q40()  # Call the corresponding function
            
        case "41. Subtract the product and sum of digits of an integer":
            Q41()
             
        case "42. Add Two Integers":
            Q42()
            
        case "43. Divisor Game":
            Q43()
            
        case "44. Generate Fibonacci Sequence":
            Q44()
            
        case "45.Generate a String With Characters That Have Odd Counts":
            Q45()
            
        case "46. Sum Multiples":
            Q46()
            
        case "47. Find Anagram Mappings":
            Q47()
            
        case "48. Sum of Unique Elements":
            Q48()
            
        case "49. Alternating digit sum":
            Q49()
            
        case "50. Find closest number to zero":
            Q50()

    
# Call the app function to render the content
app()
