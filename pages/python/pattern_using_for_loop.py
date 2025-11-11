import streamlit as st


# Injecting custom CSS into Streamlit for all headers
st.markdown("""
    <style>
        /* General header styling */
        .main-heading {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        .highlight {
            color: #64FFDA;
        }

        /* Applying the same style to all headings (h1, h2, etc.) */
        h1, h2, h3, h4, h5, h6 {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        /* Highlighted part for emphasis */
        h1 span, h2 span, h3 span, h4 span, h5 span, h6 span {
            color: #64FFDA;
        }
        
        /* Custom Primary Color for Streamlit Components */
        .css-1e5b38f {  /* Streamlit button color class */
            background-color: #64FFDA !important;  /* Your custom primary color */
            color: white !important;
        }

        .css-1e5b38f:hover {
            background-color: #64FFDA !important; /* Keep hover effect */
        }

        /* Change link color */
        a {
            color: #64FFDA !important;
        }

        /* Customizing Streamlit sidebar color */
        .css-1l4p5n1 {
            background-color: #64FFDA !important;
        }

        /* Customize selected items and borders */
        .streamlit-expanderHeader {
            color: #64FFDA !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #112240; /* slate teal */
    }
    /* Main page background color */
    .stApp {
        background-color: #0A192F; /* Ivory */
    
    </style>
    """, unsafe_allow_html=True)

options = ["square grid pat 1", "square grid num pat 2", "square grid num pat 3",  "square grid alpha pat 4", "square grid alpha pat 5",  "square grid num pat 6", "square grid num pat 7", 
           "square grid alpha pat 8", "square grid alpha pat 9", "increasing triangular pat 10", "increasing triangular num pat 11", "increasing triangular num pat 12", "increasing triangular alpha pat 13", 
            "increasing triangular alpha pat 14", "decreasing triangular pat 15", "decreasing triangular num pat 16", "decreasing triangular num pat 17",
            "decreasing triangular alpha pat 18", "decreasing triangular alpha pat 19","decreasing triangular num pat 20","decreasing triangular num pat 21", "decreasing triangular alpha pat 22", 
            "decreasing triangular alpha pat 23", "right aligned triangular pat 24", "right aligned triangular num pat 25", "right aligned triangular num pat 26", 
            "right aligned triangular alpha pat 27", "right aligned triangular alpha pat 28", 
            "right aligned decreasing triangular pat 29", "right aligned decreasing triangular num pat 30","right aligned decreasing triangular num pat 31",
            "right aligned decreasing triangular alpha pat 32","right aligned decreasing triangular alpha pat 33","increasing triangular pat 34","increasing triangular num pat 35",
            "increasing triangular num pat 36","increasing triangular alpha pat 37","increasing triangular alpha pat 38","increasing triangular num pat 39",
            "increasing triangular num pat 40"
            
            ,"increasing triangular alpha pat 41", "increasing triangular alpha pat 42",
            "increasing triangular num pat 43", "increasing triangular alpha pat 44",
            "increasing triangular num pat 45", "increasing triangular alpha pat 46",
            "left aligned decreasing triangular pat 47", "left aligned decreasing triangular num pat 48",
            "left aligned decreasing triangular num pat 49", "inverted pyramid num pat 50",
            
            
            "inverted pyramid alpha pat 51", "inverted pyramid alpha pat 52", 
            "inverted pyramid alpha pat 53", "alternating triangular pat 54", 
            "alternating triangular num pat 55", "alternating triangular num pat 56", 
            "alternating triangular alpha pat 57", "alternating triangular alpha pat 58", 
            "left pascal triangle pat 59", "left pascal triangle num pat 60",
            
             "left pascal triangle num pat 61", "left pascal triangle alpha pat 62",
            "left pascal triangle alpha pat 63", "increasing triangular pat 64",
            "increasing triangular num pat 65", "increasing triangular num pat 66",
            "increasing triangular alpha pat 67", "increasing triangular alpha pat 68",
            "decreasing triangular pat 69", "decreasing triangular num pat 70",
            
            "decreasing triangular num pat 71", "decreasing triangular alpha pat 72", 
            "decreasing triangular alpha pat 73", "decreasing triangular alpha pat 74", 
            "diamond pat 75", "diamond num pat 76", 
            "diamond num pat 77", "diamond num pat 78", 
            "diamond alpha pat 79", "diamond alpha pat 80"
            
            "inverted v shaped pat 81", "inverted v shaped num pat 82", 
            "inverted v shaped num pat 83", "inverted v shaped alpha pat 84", 
            "inverted v shaped alpha pat 85", "v shaped pat 86", 
            "v shaped num pat 87", "v shaped num pat 88", 
            "v shaped alpha pat 89", "v shaped alpha pat 90"
                        
            ,  "hallow diamond pat 91", "hallow diamond num pat 92",
                "hallow diamond num pat 93", "hallow diamond alpha pat 94",
                "hallow diamond alpha pat 95", "half diamond with increasing space 96",
                "decreasing space diamond pattern 97", "mirrored diamond 98",
                "symmetrical triangular pat 99", "symmetrical triangular pat 100"

            
            
]

selection = st.selectbox('Choose the pattern', options)

match selection:
    case "square grid pat 1":
        st.code("""
def square_grid_pat_1(n):
    for i in range(n):  # Using for loop to iterate from 0 to n-1
        print('* ' * n)  # Printing row of asterisks '*' multiplied by the value n
        """)

    case "square grid num pat 2":
        st.code("""
def square_grid_num_pat_2(n):
    for i in range(1, n + 1):  # loop for n number of rows
        for j in range(1, n + 1):  # loop for n number of columns
            print(i, end=' ')  # printing the i value and all the elements in a row are separated with space
        print()  # An empty print() method for next line
        """)

    case "square grid num pat 3":
        st.code("""
def square_grid_num_pat_3(n):
    for i in range(1, n + 1):  # loop for n number of rows within the range
        for j in range(1, n + 1):  # loop for n number of columns within the range
            print(j, end=' ')  # printing the j value and all the elements in a column are separated with space
        print()  # An empty print() method for next line
        """)

    case "square grid alpha pat 4":
        st.code("""
def square_grid_alpha_pat_4(n):
    for i in range(0, n):  # loop for n number of rows which will run from 0 to n
        for j in range(n):  # loop for n number of columns which will run for n number of times
            print(chr(65 + i), end=" ")  # printing the alphabet using chr() by adding i to 65('A') and all the elements in a row are separated with spaces
        print()  # An empty print() for next line
        """)

    case "square grid alpha pat 5":
        st.code("""
def square_grid_alpha_pat_5(n):
    for i in range(n):  # Outer loop iterating from 0 to n-1
        for j in range(n):  # Inner loop iterating from 0 to n-1
            print(chr(65 + j), end=' ')  # Printing the uppercase letter corresponding to the ASCII value (65 corresponds to 'A')
        print()  # Moving to the next line after each inner loop completes
        """)

    case "square grid num pat 6":
        st.code("""
def square_grid_num_pat_6(n):
    for i in range(n, 0, -1):  # loop for n number of rows
        for j in range(n, 0, -1):  # loop for n number of columns
            print(i, end=' ')  # printing i value
        print()  # An empty print() method for next line
        """)

    case "square grid num pat 7":
        st.code("""
def square_grid_num_pat_7(n):
    for i in range(n, 0, -1):  # loop for n number of rows within the range
        for j in range(n, 0, -1):  # loop for n number of columns within the range
            print(j, end=' ')  # printing the j value and all the elements in a column are separated with space
        print()  # An empty print() method for next line
        """)

    case "square grid alpha pat 8":
        st.code("""
def square_grid_alpha_pat_8(n):
    for i in range(65 + n - 1, 64, -1):  # Outer loop to iterate through each line, starting from the ASCII value of 'A' + n - 1 and going backward
        for j in range(n):  # Inner loop to print the character in each line
            print(chr(i), end=" ")  # Printing the character corresponding to the ASCII value of i
        print()  # Moving to the next line after completing the inner loop
        """)

    case "square grid alpha pat 9":
        st.code("""
def square_grid_alpha_pat_9(n):
    for i in range(n):  # Outer loop iterating from 0 to n-1
        for j in range(n):  # Inner loop iterating from 0 to n-1
            print(chr(64 + n - j), end=' ')  # Printing the uppercase letter corresponding to the ASCII value (64 + n - j)
        print()  # Moving to the next line after each inner loop completes
        """)

    case "increasing triangular pat 10":
        st.code("""
def increasing_triangular_pat_10(n):
    for i in range(1, n + 1):  # loop for n number of rows
        for j in range(1, i + 1):  # loop for i number of columns for each row
            print('*', end=' ')  # printing * separated by space
        print()  # An empty print() method for next line
        """)
    
    
    case "increasing triangular num pat 11":
        st.code("""
def increasing_triangular_num_pat_11(n):
    for i in range(1, n + 1):  # Loop for number of rows
        for j in range(i):  # Loop for number of columns
            print(i, end=' ')  # Printing the i value, separated by space
        print()  # Move to the next line after completing the inner loop
        """)

    case "increasing triangular num pat 12":
        st.code("""
def increasing_triangular_num_pat_12(n):
    for i in range(1, n + 1):  # Outer loop to iterate through each line, starting from 1 to n
        for j in range(i):  # Inner loop to print numbers in each line
            print(j + 1, end=' ')  # Printing the value of j + 1 with space
        print()  # Move to the next line after completing the inner loop
        """)

    case "increasing triangular alpha pat 13":
        st.code("""
def increasing_triangular_alpha_pat_13(n):
    for i in range(1, n + 1):  # Outer loop iterating from 1 to n
        for j in range(1, i + 1):  # Inner loop iterating from 1 to i (inclusive)
            print(chr(64 + i), end=' ')  # Printing the uppercase letter corresponding to ASCII value (65 + i)
        print()  # Move to the next line after completing the inner loop
        """)

    case "increasing triangular alpha pat 14":
        st.code("""
def increasing_triangular_alpha_pat_14(n):
    for i in range(1, n + 1):  # Loop for n number of rows
        for j in range(1, i + 1):  # Loop for i number of columns for each row
            print(chr(64 + j), end=' ')  # Printing alphabet pattern
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular pat 15":
        st.code("""
def decreasing_triangular_pat_15(n):
    for i in range(n, 0, -1):  # Loop for printing number of rows in a given range
        for j in range(i):  # Loop for printing number of columns in a given range
            print('*', end=' ')  # Printing asterisk, separated by space
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular num pat 16":
        st.code("""
def decreasing_triangular_num_pat_16(n):
    for i in range(1, n):  # Outer loop to iterate through each line, starting from 1 up to n - 1
        for j in range(n - i):  # Inner loop to print numbers in each line
            print(i, end=' ')  # Printing the value of i, separated by space
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular num pat 17":
        st.code("""
def decreasing_triangular_num_pat_17(n):
    for i in range(n):  # Outer loop iterating from 0 to n - 1
        for j in range(n - i):  # Inner loop iterating from 0 to n - i - 1
            print(j + 1, end=' ')  # Printing the current value of j + 1
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular alpha pat 18":
        st.code("""
def decreasing_triangular_alpha_pat_18(n):
    c = 0
    for i in range(n, 0, -1):  # Loop for n number of rows
        for j in range(i):  # Loop for i number of columns
            print(chr(65 + c), end=' ')  # Printing alphabet pattern
        c += 1
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular alpha pat 19":
        st.code("""
def decreasing_triangular_alpha_pat_19(n):
    for i in range(n, 0, -1):  # Loop for printing number of rows in a given range
        for j in range(i):  # Loop for printing number of columns in a given range
            print(chr(65 + j), end=' ')  # Printing characters by assigning ASCII value of A (using chr(65)) and incrementing for each column
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular num pat 20":
        st.code("""
def decreasing_triangular_num_pat_20(n):
    for i in range(n, 0, -1):  # Outer loop to iterate through each line, starting from n and going down to 1
        for j in range(i):  # Inner loop to print numbers in each line, starting from the current value of i
            print(i, end=' ')  # Printing the value of i, separated by space
        print()  # Move to the next line after completing the inner loop
        """)
    
    case "decreasing triangular num pat 21":
        st.code("""
def decreasing_triangular_num_pat_21(n):
    c = n  # Initializing a constant value c with the value of n
    for i in range(n, 0, -1):  # Outer loop iterating from n to 1 with a step of -1
        for j in range(i):  # Inner loop iterating from 0 to i-1
            print(c - j, end=' ')  # Printing the current value of c - j
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular alpha pat 22":
        st.code("""
def decreasing_triangular_alpha_pat_22(n):
    for i in range(n, 0, -1):  # Loop for n number of rows
        for j in range(i):  # Loop for i number of columns
            print(chr(65 + i - 1), end=' ')  # Printing alphabet pattern separated by space
        print()  # Move to the next line after completing the inner loop
        """)

    case "decreasing triangular alpha pat 23":
        st.code("""
def decreasing_triangular_alpha_pat_23(n):
    for i in range(n, -1, -1):  # Loop for number of rows in the given range
        for j in range(i + 1):  # Loop for number of columns in the given range
            print(chr(65 + n - j), end=' ')  # Printing character by assigning ASCII value based on (65 + n - j)
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned triangular pat 24":
        st.code("""
def right_aligned_triangular_pat_24(n):
    for i in range(0, n + 1):  # Outer loop to iterate through each line, starting from 0 up to n
        for j in range(n - i):  # Inner loop to print spaces before stars in each line
            print(" ", end=" ")  # Printing spaces
        for j in range(i):  # Inner loop to print stars in each line
            print("*", end=" ")  # Printing stars
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned triangular num pat 25":
        st.code("""
def right_aligned_triangular_num_pat_25(n):
    for i in range(n + 1):  # Outer loop iterating from 0 to n (inclusive)
        for j in range(n - i):  # Inner loop to print spaces before the numbers
            print(" ", end=' ')
        for k in range(i):  # Inner loop to print numbers with increasing values
            print(i, end=' ')
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned triangular num pat 26":
        st.code("""
def right_aligned_triangular_num_pat_26(n):
    for i in range(1, n + 1):  # Loop for n number of rows
        for k in range(n - i):  # Loop for n - i spaces in each row
            print(" ", end=' ')  # Printing n - i spaces
        for j in range(1, i + 1):  # Loop for i number of columns
            print(j, end=' ')  # Printing j value
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned triangular alpha pat 27":
        st.code("""
def right_aligned_triangular_alpha_pat_27(n):
    for i in range(n):  # Loop for number of rows
        for k in range(n - i):  # Loop for printing spaces
            print(" ", end=' ')  # Printing spaces
        for j in range(i + 1):  # Loop for number of columns
            print(chr(65 + i), end=' ')  # Printing character by assigning ASCII value of A (chr(65))
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned triangular alpha pat 28":
        st.code("""
def right_aligned_triangular_alpha_pat_28(n):
    for i in range(0, n + 1):  # Outer loop to iterate through each line, starting from 0 up to n
        for j in range(n - i):  # Inner loop to print spaces before the characters in each line
            print(" ", end=" ")
        for j in range(65, 65 + i):  # Inner loop to print characters in each line, starting from 'A' up to 'A' + i - 1
            print(chr(j), end=" ")
        print()  # Move to the next line after completing the inner loops
        """)

    case "right aligned decreasing triangular pat 29":
        st.code("""
def right_aligned_decreasing_triangular_pat_29(n):
    for i in range(n):  # Outer loop iterating from 0 to n - 1
        for j in range(i):  # Inner loop to print spaces before the asterisks
            print(" ", end=' ')
        for k in range(n - i):  # Inner loop to print asterisks
            print('*', end=' ')
        print()  # Move to the next line after completing the inner loop
        """)

    case "right aligned decreasing triangular num pat 30":
        st.code("""
def right_aligned_decreasing_triangular_num_pat_30(n):
    for i in range(n, 0, -1):  # Loop for n number of rows
        for k in range(n - i):  # Loop for n - i spaces in each row
            print(" ", end=' ')  # Printing n - i spaces
        for j in range(i):  # Loop for i number of columns
            print(i, end=' ')  # Printing i value, repeated i times, separated by space
        print()  # Move to the next line after completing the inner loop
        """)
        
    case "right aligned decreasing triangular num pat 31":
        st.code("""
def right_aligned_decreasing_triangular_num_pat_31(n):
    for i in range(n, 0, -1):  # Loop for number of rows in the given range
        for k in range(n - i):  # Loop for printing spaces
            print(" ", end=' ')  # Printing spaces
        for j in range(i):  # Loop for number of columns in the given range
            print(j + 1, end=' ')  # Printing the value of j + 1 without a newline character
        print()  # Move to the next line after printing spaces and characters for each row
        """)

    case "right aligned decreasing triangular alpha pat 32":
        st.code("""
def right_aligned_decreasing_triangular_alpha_pat_32(n):
    for i in range(n, 0, -1):  # Outer loop to iterate through each line, starting from n and going down to 1
        for j in range(n - i + 1):  # Inner loop to print spaces before the characters in each line
            print(" ", end=' ')
        m = 65  # Initializing m to the ASCII value of 'A'
        for k in range(65, 65 + i):  # Inner loop to print characters in each line
            print(chr(m + i - 1), end=' ')
        m += 1  # Incrementing m for next character
        print()  # Moving to the next line after completing the inner loops
        """)

    case "right aligned decreasing triangular alpha pat 33":
        st.code("""
def right_aligned_decreasing_triangular_alpha_pat_33(n):
    for i in range(n, 0, -1):  # Outer loop iterating from n to 1 with a step of -1
        for j in range(n - i):  # Inner loop to print spaces before the letters
            print(" ", end=' ')  # Printing spaces
        for k in range(i):  # Inner loop to print letters with increasing values
            print(chr(65 + k), end=' ')  # Printing alphabetic pattern
        print()  # Moving to the next line after each row completes
        """)

    case "increasing triangular pat 34":
        st.code("""
def increasing_triangular_pat_34(n):
    for i in range(1, n + 1):  # Loop for n number of rows
        for k in range(n - i):  # Loop for n - i spaces in each row
            print(" ", end='')  # Printing n - i spaces
        for j in range(1, i + 1):  # Loop for i number of columns in each row
            print("*", end=' ')  # Printing * separated by space
        print()  # An empty print() for next line
        """)

    case "increasing triangular num pat 35":
        st.code("""
def increasing_triangular_num_pat_35(n):
    for i in range(1, n + 1):  # Loop for number of rows in the given range
        for k in range(n - i):  # Loop for printing spaces
            print(" ", end=' ')  # Print spaces
        for j in range(i * 2 - 1):  # Loop for the number of columns in the given range
            print(i, end=' ')  # Printing the value of i and separating it using spaces
        print()  # Print method to next line
        """)

    case "increasing triangular num pat 36":
        st.code("""
def increasing_triangular_num_pat_36(n):
    k = 1  # Initializing k to 1
    for i in range(1, n // 2 + 2):  # Outer loop to iterate through each line
        for j in range(n - i):  # Inner loop to print spaces before the numbers
            print(" ", end=" ")
        for j in range(2 * i - 1):  # Inner loop to print numbers in each line
            print(k, end=" ")
        k += 2
        print()  # Moving to the next line after completing the inner loops
        """)

    case "increasing triangular alpha pat 37":
        st.code("""
def increasing_triangular_alpha_pat_37(n):
    for i in range(0, n):  # Outer loop iterating from 0 to n - 1
        for j in range(n - i):  # Inner loop to print spaces before the letters
            print(" ", end=' ')
        for k in range(i * 2 + 1):  # Inner loop to print letters with increasing values
            print(chr(65 + i), end=' ')
        print()  # Moving to the next line after each row completes
        """)

    case "increasing triangular alpha pat 38":
        st.code("""
def increasing_triangular_alpha_pat_38(n):
    x = 0  # Initializing x with 0
    for i in range(n // 2):  # Loop for n / 2 rows
        for k in range(n - i):  # Loop for n - i spaces in each row
            print(" ", end=' ')  # Printing n - i spaces
        for j in range(i * 2 + 1):  # Loop for i * 2 + 1 columns
            print(chr(65 + x), end=' ')  # Printing alphabet pattern separated by space
        x += 2  # Incrementing x value
        print()  # An empty print() for next line
        """)

    case "increasing triangular num pat 39":
        st.code("""
def increasing_triangular_num_pat_39(n):
    for i in range(1, n // 2 + 1):  # Loop for number of rows in the range
        for k in range(n - i):  # Loop for printing spaces
            print(" ", end=' ')  # Printing spaces
        for j in range(1, i * 2):  # Loop for number of columns in the range
            print(j, end=' ')  # Printing the value of j and separating with spaces
        print()  # Print method to move to other line
        """)

    case "increasing triangular num pat 40":
        st.code("""
def increasing_triangular_num_pat_40(n):
    for i in range(1, n // 2 + 2):  # Outer loop to iterate through each line
        for j in range(n - i - n // 2):  # Inner loop to print spaces before the numbers
            print(" ", end=" ")
        for k in range(2 * i - 1, 0, -1):  # Inner loop to print numbers in each line
            print(k, end=" ")
        print()  # Moving to the next line after completing the inner loops
        """)
        
    case "increasing triangular alpha pat 41":
        st.code("""
def increasing_triangular_alpha_pat_41(n):
    for i in range(0,n//2+1): # Outer loop iterating from 0 to n//2 (inclusive)
        for j in range(n-i-n//2): # Inner loop to print spaces before the letters
            print(" ",end=' ')
        for k in range(i*2+1): # Inner loop to print letters with increasing values
            print(chr(65+k),end=' ')
        print() # Moving to the next line after each row completes
        """)

    case "increasing triangular alpha pat 42":
        st.code("""
def increasing_triangular_alpha_pat_42(n):
    x=0 # initializing x with 0
    for i in range(n//2+1): # loop for n/2 rows
        for k in range(n-i): # loop for n-i spaces in each row
            print(" ",end=' ') # printing n-i spaces
        for j in range(i*2+1): # loop for i*2+1 columns
            print(chr(65+x-j),end=' ') # printing alphabet pattern separated by space
        x+=2 # incrementing x value
        print() # an empty print() for next line
        """)

    case "increasing triangular num pat 43":
        st.code("""
def increasing_triangular_num_pat_43(n):
    for i in range(0,n+1): # loop for the number of rows
        for k in range(n-i): # loop for printing spaces before numbers
            print(" ",end=' ') # printing spaces
        for j in range(i,-1,-1): # loop for printing numbers in decreasing order
            print(j, end=' ') # Print the current value of j separated using spaces
        for m in range(1,i+1): # loop for printing numbers in increasing order
            print(m, end=' ') # Print the current value of m
        print() # Move to the next line
        """)

    case "increasing triangular alpha pat 44":
        st.code("""
def increasing_triangular_alpha_pat_44(n):
    for i in range(1,n+1): # Outer loop to iterate through each line, starting from 1 up to n
        for j in range(n-i): # Inner loop to print spaces before the characters in each line
            print(" ",end=" ")
        for k in range(i,0,-1): # First inner loop to print characters in descending order
            print(chr(64+k),end=" ")
        for m in range(1,i): # Second inner loop to print characters in ascending order
            print(chr(65+m),end=" ")
        print() # Moving to the next line after completing the inner loops
        """)

    case "increasing triangular num pat 45":
        st.code("""
def increasing_triangular_num_pat_45(n):
    for i in range(1,n+1): # Outer loop iterating from 1 to n (inclusive)
        for j in range(n-i): # Inner loop to print spaces before the numbers
            print(" ",end=' ')
        for k in range(1,i+1): # Inner loop to print numbers in increasing order
            print(k,end=' ')
        for l in range(i-1,0,-1): # Inner loop to print numbers in decreasing order
            print(l,end=' ')
        print()
        """)

    case "increasing triangular alpha pat 46":
        st.code("""
def increasing_triangular_alpha_pat_46(n):
    x=0 # initializing x with 0
    for i in range(n+1): # loop for n rows
        for k in range(n-i): # loop for n-i spaces in each row
            print(" ",end=' ') # printing n-i spaces
        for j in range(i): # loop for i number of columns
            print(chr(65+j),end=' ') # printing alphabet pattern separated by space
        for m in range(i-1,0,-1): # loop for i-1 columns
            print(chr(65+m-1),end=' ') # printing alphabet pattern separated by space
        print() # an empty print() for next line
        """)

    case "left aligned decreasing triangular pat 47":
        st.code("""
def left_aligned_decreasing_triangular_pat_47(n):
    for i in range(n//2,-1,-1): # loop for the number of rows in reverse order
        for k in range(n-i): # loop for printing spaces before asterisks
            print(" ",end=' ') # printing spaces
        for j in range(i+1): # loop for printing asterisks in increasing order
            print('*',end = ' ') # asterisk
        for m in range(i): # loop for printing asterisks in decreasing order
            print('*',end=' ') # Print asterisk
        print() # Move to the next line
        """)

    case "left aligned decreasing triangular num pat 48":
        st.code("""
def left_aligned_decreasing_triangular_num_pat_48(n):
    m=2 # Initializing m to 2
    for i in range(n-1,0,-1): # Outer loop to iterate through each line
        for j in range(n-i): # Inner loop to print spaces before the numbers
            print(" ",end=" ")
        for j in range(n+i-m): # Second inner loop to print numbers in each line
            print(i,end=" ")
        m+=1 # Incrementing m by 1
        print() # Moving to the next line after completing the inner loops
        """)

    case "left aligned decreasing triangular num pat 49":
        st.code("""
def left_aligned_decreasing_triangular_num_pat_49(n):
    for i in range(n,0,-2): # Outer loop iterating from n to 1 with a step of -2
        for j in range(n-i//2-n//2+1): # Inner loop to print spaces before the numbers
            print(" ",end=' ')
        for k in range(i): # Inner loop to print numbers with the value of i
            print(i,end=' ')
        print()  # Moving to the next line after each row completes
        """)

    case "inverted pyramid num pat 50":
        st.code("""
def inverted_pyramid_num_pat_50(n):
    for i in range(n//2+1,0,-1): # loop for n/2+1 rows
        for k in range(n-i): # loop for n-i spaces in each row
            print(" ",end=' ') # printing n-i spaces
        for j in range(1,i*2): # loop for i*2 columns
            print(j,end=' ') # printing j value separated by space
        print() # an empty print() for next line
        """)
    
    case "inverted pyramid alpha pat 51":
        st.code("""
def inverted_pyramid_alpha_pat_51(n):
    for i in range(n-1, -1, -1):  # Loop for the number of rows in reverse order
        for k in range(n-i):  # Loop for printing spaces before characters
            print(" ", end=' ')  # Printing spaces
        for j in range(i*2+1):  # Loop for the number of columns based on the current row
            print(chr(65+i), end=' ')  # Print character by assigning ASCII value of A plus the row number
        print()  # Move to the next line
        """)

    case "inverted pyramid alpha pat 52":
        st.code("""
def inverted_pyramid_alpha_pat_52(n):
    k = 65 + n*2 - 2  # Initializing k to the ASCII value of 'A' + n*2 - 2
    m = 1  # Initializing m to 1
    for i in range(n, 0, -1):  # Loop to iterate through each line, starting from n and going down to 1
        for j in range(n-i+1):  # First inner loop to print spaces before the characters
            print(" ", end=" ")
        for j in range(n+i-m):  # Second inner loop to print characters
            print(chr(k), end=" ")
        m += 1
        k -= 2
        print()  # Moving to the next line after completing the inner loops
        """)

    case "inverted pyramid alpha pat 53":
        st.code("""
def inverted_pyramid_alpha_pat_53(n):
    m = 0  # Initializing a variable m with value 0
    for i in range(n//2 + 1, 0, -1):  # Loop iterating from n//2 + 1 to 1
        print(' ' * (m), end=' ')  # Printing spaces based on m
        for j in range(i*2 - 1):  # Inner loop to print letters in increasing order
            print(chr(65+j), end=' ')  # Incrementing m for the next row
        m += 2
        print()  # Moving to the next line
        """)

    case "alternating triangular pat 54":
        st.code("""
def alternating_triangular_pat_54(n):
    for i in range(n):  # Loop for n number of rows
        for j in range(i):  # Loop for i number of columns
            print("*", end=' ')  # Printing j number of *'s
        print()  # Empty print for next line
    for i in range(n, 0, -1):  # Loop for n-1 number of rows
        for k in range(i):  # Loop for i number of columns
            print("*", end=' ')  # Printing k number of *'s
        print()  # Empty print for next line
        """)

    case "alternating triangular num pat 55":
        st.code("""
def alternating_triangular_num_pat_55(n):
    for i in range(n):  # Loop for numbers of rows
        for j in range(i + 1):  # Loop for numbers of columns
            print(n - j, end=' ')  # Print decreasing numbers based on current column
        print()  # Empty print for next line
    for i in range(n, -1, -1):  # Loop for the number of rows in reverse order
        for k in range(i + 1):  # Loop for the number of columns
            print(n - k, end=' ')  # Print decreasing numbers based on current column
        print()  # Empty print for next line
        """)

    case "alternating triangular num pat 56":
        st.code("""
def alternating_triangular_num_pat_56(n):
    # First part of the pattern: Increasing order
    for i in range(n):  # Outer loop to iterate through each line
        for j in range(i, -1, -1):  # Inner loop to print numbers in decreasing order
            print(n - j, end=' ')
        print()  # Moving to the next line
    # Second part of the pattern: Decreasing order
    for i in range(n, -1, -1):  # Outer loop to iterate through each line
        for j in range(i, -1, -1):  # Inner loop to print numbers in decreasing order
            print(n - j, end=' ')
        print()  # Moving to the next line
        """)

    case "alternating triangular alpha pat 57":
        st.code("""
def alternating_triangular_alpha_pat_57(n):
    for i in range(n):  # Loop for numbers of rows
        for j in range(i + 1):  # Loop for numbers of columns
            print(chr(65 + n - j), end=' ')  # Print alphabetic pattern
        print()  # Empty print for next line
    for i in range(n, -1, -1):  # Loop for the number of rows in reverse order
        for k in range(i + 1):  # Loop for the number of columns
            print(chr(65 + n - k), end=' ')  # Print alphabetic pattern
        print()  # Empty print for next line
        """)

    case "alternating triangular alpha pat 58":
        st.code("""
def alternating_triangular_alpha_pat_58(n):
    for i in range(n):  # Loop for n number of rows
        for j in range(i, -1, -1):  # Loop for i number of columns
            print(chr(65 + n - j), end=' ')  # Print alphabet pattern
        print()  # Empty print for next line
    for i in range(n, -1, -1):  # Loop for n number of rows
        for j in range(i, -1, -1):  # Loop for i number of columns
            print(chr(65 + n - j), end=' ')  # Print alphabet pattern
        print()  # Empty print for next line
        """)

    case "left pascal triangle pat 59":
        st.code("""
def left_pascal_triangle_pat_59(n):
    for i in range(1, n + 1):  # Loop for number of rows
        for j in range(n, i, -1):  # Loop for number of columns
            print(" ", end=' ')  # Print spaces
        for k in range(1, i + 1):  # Loop for asterisks
            print("*", end=' ')  # Print asterisks separated by spaces
        print()  # Empty print for next line
    for i in range(n - 1, 0, -1):  # Loop for number of rows
        for j in range(n, i, -1):  # Loop for number of columns
            print(" ", end=' ')  # Print spaces
        for k in range(1, i + 1):  # Loop for number of asterisks
            print("*", end=' ')  # Print asterisks separated by spaces
        print()  # Empty print for next line
        """)

    case "left pascal triangle num pat 60":
        st.code("""
def left_pascal_triangle_num_pat_60(n):
        # First part of the pattern: Increasing order
        for i in range(n):  # Loop for n number of rows
            for j in range(n - i):  # Loop for spaces before the numbers
                print(" ", end=" ")
            for j in range(i + 1):  # Loop for numbers in decreasing order
                print(n - j, end=" ")
            print()  # Moving to the next line
        # Second part of the pattern: Decreasing order
        for i in range(n, -1, -1):
            for j in range(n - i):  # Loop for spaces before the numbers
                print(" ", end=" ")
            for k in range(i + 1):  # Loop for numbers in decreasing order
                print(n - k, end=' ')
            print()  # Moving to the next line
        """)
    
    case "left pascal triangle num pat 61":
        st.code("""
def left_pascal_triangle_num_pat_61(n):
    # First part of the pattern
    for i in range(n):  # Loop for no. of rows
        x = 0
        for j in range(n - i):  # Printing spaces before the numbers
            print(" ", end=' ')
            x += 1
        for k in range(i + 1):  # Printing numbers in increasing order
            print(x, end=' ')
            x += 1
        print()  # Moving to the next line after each row completes
    # Second part of the pattern
    for i in range(n, -1, -1):  # Loop for no. of rows
        x = 0
        for j in range(n - i):  # Printing spaces before the numbers
            print(" ", end=' ')
            x += 1
        for k in range(i + 1):  # Printing numbers in increasing order
            print(x, end=' ')
            x += 1
        print()  # Moving to the next line after each row completes
        """)

    case "left pascal triangle alpha pat 62":
        st.code("""
def left_pascal_triangle_alpha_pat_62(n):
    for i in range(n):  # Loop for n number of rows
        x = 0  # Initializing x with 0
        for j in range(n - i):  # Loop for n - i number of spaces in each row
            print(" ", end=' ')  # Printing n - i spaces
            x += 1  # Incrementing x value
        for k in range(i):  # Loop for i number of columns
            print(chr(ord('A') + x), end=' ')  # Printing alphabetical pattern separated by space
            x += 1  # Incrementing x value
        print()  # An empty print() for next line
    for i in range(n, 0, -1):  # Loop for n number of rows
        x = 0  # Initializing x with 0
        for j in range(n - i):  # Loop for n - i number of spaces in each row
            print(" ", end=' ')  # Printing n - i spaces
            x += 1  # Incrementing x value
        for k in range(i):  # Loop for i number of columns
            print(chr(ord('A') + x), end=' ')  # Printing alphabetical pattern separated by space
            x += 1  # Incrementing x value
        print()  # An empty print() for next line
        """)

    case "left pascal triangle alpha pat 63":
        st.code("""
def left_pascal_triangle_alpha_pat_63(n):
    for i in range(n):  # Loop for number of rows
        for j in range(n - i):  # Loop for number of columns
            print(" ", end=' ')  # Printing spaces
        for k in range(i + 1):  # Print characters in decreasing order
            print(chr(65 + n - k), end=' ')  # Printing characters
        print()  # An empty print() for next line
    for i in range(n, -1, -1):  # Loop for number of rows
        for j in range(n - i):  # Loop for number of columns
            print(" ", end=' ')  # Printing spaces
        for k in range(i + 1):  # Print characters in decreasing order
            print(chr(65 + n - k), end=' ')  # Printing characters
        print()  # An empty print() for next line
        """)

    case "increasing triangular pat 64":
        st.code("""
def increasing_triangular_pat_64(n):
    for i in range(0, n + 1):  # Outer loop for no. of rows which will run from 0 to n + 1
        for j in range(n - i):  # First inner loop to print spaces before the asterisks in each line
            print(" ", end="")
        for j in range(1, i + 1):  # Second inner loop to print asterisks in increasing order
            print("*", end=" ")
        print()
        """)

    case "increasing triangular num pat 65":
        st.code("""
def increasing_triangular_num_pat_65(n):
    for i in range(0, n + 1):  # Outer loop for no. of rows which will run from 0 to n + 1
        for j in range(n - i):  # First inner loop to print spaces before the asterisks in each line
            print(" ", end="")
        for j in range(1, i + 1):  # Second inner loop to print numbers in increasing order
            print(i, end=" ")
        print()
        """)

    case "increasing triangular num pat 66":
        st.code("""
def increasing_triangular_num_pat_66(n):
    for i in range(1, n + 1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n - i number of spaces in each row
            print(" ", end='')  # Printing n - i spaces
        for k in range(1, i + 1):  # Loop for i number of columns
            print(k, end=' ')  # Printing k value separated by space
        print()  # An empty print() for next line
        """)

    case "increasing triangular alpha pat 67":
        st.code("""
def increasing_triangular_alpha_pat_67(n):
    for i in range(n):  # Loop for each row
        for j in range(n - i - 1):  # Loop for each column
            print(" ", end='')  # Print spaces before characters
        for k in range(i + 1):  # Print characters in increasing order
            print(chr(ord('A') + i), end=' ')
        print()  # Move to the next line after printing each row
        """)

    case "increasing triangular alpha pat 68":
        st.code("""
def increasing_triangular_alpha_pat_68(n):
    for i in range(0, n + 1):  # Loop to print a pattern of characters in a pyramid
        for j in range(n - i):  # First inner loop to print spaces before the characters in each line
            print(" ", end='')
        for k in range(1, i + 1):  # Second inner loop to print characters in increasing order
            print(chr(64 + k), end=' ')
        print()  # Moving to the next line after completing the inner loops
        """)

    case "decreasing triangular pat 69":
        st.code("""
def decreasing_triangular_pat_69(n):
    for i in range(n, 0, -1):  # Loop to iterate through rows in reverse order
        for j in range(0, n - i):  # Loop to add leading spaces for formatting
            print(end=' ')
        for k in range(0, i):  # Loop to print asterisks for the current row
            print('*', end=" ")
        print()  # Move to the next line after completing the row
        """)

    case "decreasing triangular num pat 70":
        st.code("""
def decreasing_triangular_num_pat_70(n):
    for i in range(n, -1, -1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n - i number of spaces in each row
            print(" ", end='')  # Printing n - i spaces
        for k in range(i):  # Loop for i number of columns
            print(i, end=' ')  # Printing i value - k times
        print()  # An empty print() for next line
        """)
        
    case "decreasing triangular num pat 71":
        st.code("""
def decreasing_triangular_num_pat_71(n):
    for i in range(n, 0, -1):  # Loop for each row
        for j in range(n - i):  # Loop for each column
            print(" ", end='')  # Print spaces
        for k in range(i, 0, -1):  # Loop for printing numbers in decreasing order
            print(k, end=' ')
        print()  # Move to the next line after printing each row
        """)

    case "decreasing triangular alpha pat 72":
        st.code("""
def decreasing_triangular_alpha_pat_72(n):
    for i in range(n, 0, -1):  # Loop to print a pattern of characters in a descending order pyramid
        for j in range(n - i + 1):  # First inner loop to print spaces before the characters in each line, starting from n-i+1
            print(" ", end='')
        for k in range(0, i):  # Second inner loop to print characters in decreasing order
            print(chr(64 + i), end=' ')
        print()  # Moving to the next line after completing the inner loops
        """)

    case "decreasing triangular alpha pat 73":
        st.code("""
def decreasing_triangular_alpha_pat_73(n):
    for i in range(n, 0, -1):  # Loop to iterate through rows in reverse order
        for j in range(n - i + 1):  # Loop to add leading spaces for formatting
            print(" ", end='')
        for k in range(0, i):  # Loop to print uppercase letters for the current row
            print(chr(64 + i - k), end=' ')
        print()  # Move to the next line after completing the row
        """)

    case "decreasing triangular alpha pat 74":
        st.code("""
def decreasing_triangular_alpha_pat_74(n):
    for i in range(n, 0, -1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces row
            print(" ", end='')  # Printing n-i spaces
        for k in range(i):  # Loop for i number of columns
            print(chr(65 + k), end=' ')  # Printing alphabets pattern separated by space
        print()  # An empty print() for the next line
        """)

    case "diamond pat 75":
        st.code("""
def diamond_pat_75(n):
    for i in range(n):  # Loop for number of rows
        print(" " * (n - i), end=" ")  # Printing spaces
        for j in range(0, i + 1):  # Loop for number of columns
            print("*", end=" ")
        print()  # Move to the next line after printing each row
    for i in range(n - 1, 0, -1):  # Loop for the second half
        print(" " * (n - i + 1), end=" ")
        for j in range(i):  # Loop for the number of columns for the second half
            print("*", end=" ")  # Printing asterisk
        print()  # Move to the next line after printing each row
        """)

    case "diamond num pat 76":
        st.code("""
def diamond_num_pat_76(n):
        # First part of the pattern: Increasing order
        for i in range(0, n):
            for j in range(n - i):  # First inner loop to print spaces before the numbers
                print(' ', end='')
            for k in range(1, i + 1):  # Second inner loop to print numbers in increasing order
                print(i, end=' ')
            print()  # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        for i in range(n, 0, -1):
            for j in range(n - i):  # First inner loop to print spaces before the numbers
                print(" ", end='')
            for k in range(1, i + 1):  # Second inner loop to print numbers in decreasing order
                print(i, end=' ')
            print()
        """)

    case "diamond num pat 77":
        st.code("""
def diamond_num_pat_77(n):
        # First part of the pattern: Increasing order
        for i in range(0, n):
            for j in range(n - i):  # First inner loop to print spaces before the numbers
                print(' ', end='')
            for k in range(1, i + 1):  # Second inner loop to print numbers in increasing order
                print(k, end=' ')
            print()  # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        m = 1
        for i in range(n, 0, -1):
            for j in range(n - i):  # First inner loop to print spaces before the numbers
                print(" ", end='')
            for k in range(0, i):  # Second inner loop to print numbers in decreasing order
                print(k + m, end=' ')
            m += 1
            print()
        """)

    case "diamond num pat 78":
        st.code("""
def diamond_num_pat_78(n):
        for i in range(1, n):  # Loop for n-1 number of rows
            for j in range(n - i):  # Loop for n-i number of spaces in each row
                print(' ', end='')  # Printing n-i spaces
            for k in range(1, i + 1):  # Loop for i number of columns
                print(k, end=' ')  # Printing k value separated by space
            print()  # An empty print() for the next line
        for i in range(n, 0, -1):  # Loop for n number of rows
            for j in range(n - i):  # Loop for n-i number of spaces in each row
                print(" ", end='')  # Printing n-i spaces
            for k in range(1, i + 1):  # Loop for i number of columns
                print(k, end=' ')  # Printing k values separated by spaces
            print()  # An empty print() for the next line
        """)

    case "diamond alpha pat 79":
        st.code("""
def diamond_alpha_pat_79(n):
        for i in range(n):  # Loop for number of rows
            for j in range(n - i - 1):  # Loop for number of columns
                print(" ", end='')  # Print spaces before characters
            for k in range(i + 1):
                print(chr(ord('A') + i), end=' ')  # Print characters in increasing order
            print()  # Move to the next line after printing each row
        for i in range(1, n):
            for j in range(i):
                print(" ", end='')  # Print spaces before characters
            for k in range(n - i):  # Print characters in decreasing order
                print(chr(ord('A') + n - i - 1), end=' ')
            print()  # Move to the next line after printing each row
        """)

    case "diamond alpha pat 80":
        st.code("""
def diamond_alpha_pat_80(n):
        # First part of the pattern: Increasing order
        for i in range(n):
            for j in range(n - i - 1):  # First inner loop to print spaces before the characters
                print(' ', end='')
            for k in range(i + 1):  # Second inner loop to print characters in increasing order
                print(chr(65 + k), end=' ')
            print()  # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        m = 1
        for i in range(1, n):
            for j in range(i):  # First inner loop to print spaces before the characters
                print(" ", end='')
            for k in range(n - i):  # Second inner loop to print characters in decreasing order
                print(chr(65 + k + m), end=' ')
            m += 1
            print()  # Moving to the next line after completing the inner loops
        """)
    
    case "inverted v shaped pat 81":
        st.code("""
def inverted_v_shaped_pat_81(n):
    for i in range(0, n + 1):  # Loop to iterate through rows
        for j in range(n - i + 1):  # Loop to add leading spaces for formatting
            print(' ', end='')
        for k in range(i + 1):  # Loop to print characters for the current row
            if k == 0 or k == i:
                print("*", end=' ')  # Print '*' if it's the first or last character in the row
            else:
                print(" ", end=' ')
        print()  # Move to the next line after completing the row
        """)

    case "inverted v shaped num pat 82":
        st.code("""
def inverted_v_shaped_num_pat_82(n):
    for i in range(1, n + 1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces in each row
            print(' ', end='')  # Printing n-i spaces
        for k in range(1, i + 1):  # Loop for i number of columns
            if k == 1 or k == i:  # Checking whether the value of k is equal to 1 or i.
                print(i, end=' ')  # Printing i value if the k value is either 1 or i
            else:  # Else block will execute if k value is neither 1 nor i
                print(" ", end=' ')  # Printing spaces
        print()  # An empty print() for next line
        """)

    case "inverted v shaped num pat 83":
        st.code("""
def inverted_v_shaped_num_pat_83(n):
    for i in range(0, n):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces in each row
            print(' ', end='')  # Printing n-i spaces
        for k in range(0, i + 1):  # Loop for i number of columns
            if k == 0 or k == i:  # Checking whether the value of k is equal to 0 or i.
                print(n - i, end=' ')  # Printing n-i value if the k value is either 0 or i
            else:  # Else block will execute if k value is neither 0 nor i
                print(" ", end=' ')  # Printing spaces
        print()  # An empty print() for next line
        """)

    case "inverted v shaped alpha pat 84":
        st.code("""
def inverted_v_shaped_alpha_pat_84(n):
    for i in range(1, n + 1):  # Loop for number of rows
        for j in range(n - i + 2):  # First inner loop to print spaces before the characters in each line
            print(' ', end='')
        for k in range(1, i + 1):  # Second inner loop to print characters
            if k == 1 or k == i:
                print(chr(64 + i), end=' ')  # Printing the character 'A+i'
            else:
                print(" ", end=' ')  # Printing a space for the inner characters
        print()  # Moving to the next line after completing the inner loops
        """)

    case "inverted v shaped alpha pat 85":
        st.code("""
def inverted_v_shaped_alpha_pat_85(n):
    for i in range(1, n + 1):  # Loop to iterate through rows
        for j in range(n - i):  # Loop to add leading spaces for formatting
            print(' ', end='')
        for k in range(1, i + 1):  # Loop to print characters for the current row
            if k == 1 or k == i:
                print(chr(65 + n - i), end=' ')  # Print the uppercase letter based on the pattern
            else:
                print(" ", end=' ')
        print()  # Move to the next line after completing the row
        """)

    case "v shaped pat 86":
        st.code("""
def v_shaped_pat_86(n):
    for i in range(n, -1, -1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces in each row
            print(' ', end='')  # Printing n-i spaces
        for k in range(i + 1):  # Loop for i number of columns
            if k == 0 or k == i:  # Checking whether the value of k is equal to 0 or i.
                print("*", end=' ')  # Printing '*' at the beginning and end of each line
            else:  # Else block will execute if k value is neither 0 nor i
                print(" ", end=' ')  # Printing spaces
        print()  # An empty print() for next line
        """)

    case "v shaped num pat 87":
        st.code("""
def v_shaped_num_pat_87(n):
    for i in range(n):  # Loop for each row
        for j in range(i):  # Loop for each column
            print(" ", end='')  # Print spaces before numbers
        print(i + 1, end='')  # Print the leftmost number
        for k in range((n - i - 1) * 2 - 1):  # Print spaces between numbers
            print(" ", end='')
        if i < n - 1:  # Print the rightmost number (if not the first row)
            print(i + 1, end='')
        print()  # Move to the next line after printing each row
        """)

    case "v shaped num pat 88":
        st.code("""
def v_shaped_num_pat_88(n):
    for i in range(n, -1, -1):  # Loop to print the triangle pattern in reverse order
        for j in range(n - i):  # First inner loop to print spaces before the numbers in each line
            print(' ', end='')
        for k in range(1, i + 1):  # Second inner loop to print numbers
            if k == 1 or k == i:
                print(i, end=' ')  # Printing the number 'i'
            else:
                print(" ", end=' ')  # Printing a space for the inner numbers
        print()  # Moving to the next line after completing the inner loops
        """)

    case "v shaped alpha pat 89":
        st.code("""
def v_shaped_alpha_pat_89(n):
    m = 1
    for i in range(n, 0, -1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces in each row
            print(' ', end='')  # Printing n-i spaces
        for k in range(i + 1):  # Loop for i number of columns
            if k == 1 or k == i:  # Checking whether the value of k is equal to 1 or i.
                print(chr(64 + m), end=' ')  # Printing alphabets by adding 1 to the order of the alphabet
            else:  # Else block will execute if k value is neither 1 nor i
                print(" ", end=' ')  # Printing spaces
        m += 1
        print()  # An empty print() for next line
        """)

    case "v shaped alpha pat 90":
        st.code("""
def v_shaped_alpha_pat_90(n):
    for i in range(n, 0, -1):  # Loop for n number of rows
        for j in range(n - i):  # Loop for n-i number of spaces in each row
            print(' ', end='')  # Printing n-i spaces
        for k in range(1, i + 1):  # Loop for i number of columns
            if k == 1 or k == i:  # Checking whether the value of k is equal to 1 or i.
                print(chr(64 + i), end=' ')  # Printing alphabetic pattern if the k value is either 1 or i
            else:  # Else block will execute if k value is neither 1 nor i
                print(' ', end=' ')  # Printing spaces
        print()  # An empty print() for next line
        """)
    
    case "hallow diamond pat 91":
        st.code("""
def hallow_diamond_pat_91(n):
    for i in range(n):  # loop for the number of rows
        print(" " * (n - i), end=" ")  # print asterisk separated with spaces
        for j in range(0, i + 1):  # loop for the number of columns
            if j == 0 or j == i:  # using if condition to print asterisk at the beginning and end
                print("*", end=" ")  # print asterisk separated by spaces
            else:
                print(" ", end=' ')  # print space between asterisks
        print()  # move to the next line after completing a row
    for i in range(n, -1, -1):
        print(" " * (n - i), end=" ")  # print spaces before the asterisks
        for j in range(i + 1):
            if j == 0 or j == i:  # using if condition to print asterisk at the beginning and end
                print("*", end=" ")  # print asterisk separated by spaces
            else:
                print(" ", end=' ')  # print space between asterisks
        print()  # move to the next line after completing a row
        """)

    case "hallow diamond num pat 92":
        st.code("""
def hallow_diamond_num_pat_92(n):
    for i in range(n):  # Loop for no.of rows
        for j in range(n - i):  # First inner loop to print spaces before the numbers
            print(' ', end='')
        for k in range(1, i + 1):  # Second inner loop to print numbers
            if k == 1 or k == i:
                print(i, end=' ')  # Print number 'i'
            else:
                print(' ', end=' ')  # Print space for inner numbers
        print()  # Next line

    for i in range(n, 0, -1):  # Loop for no.of rows
        for j in range(n - i):  # First inner loop to print spaces before the numbers
            print(' ', end='')
        for k in range(1, i + 1):  # Second inner loop to print numbers
            if k == 1 or k == i:
                print(i, end=' ')  # Print number 'i'
            else:
                print(' ', end=' ')  # Print space for inner numbers
        print()  # Next line
        """)

    case "hallow diamond num pat 93":
        st.code("""
def hallow_diamond_num_pat_93(n):
    # Upper part of the pyramid
    for i in range(n):  # Loop to iterate through no.o lines
        for j in range(n - i):  # Loop to add leading spaces
            print(' ', end='')
        for k in range(1, i + 1):  # Loop to print numbers
            if k == 1 or k == i:
                print(n + 1 - i, end=' ')  # Print n+1-i
            else:
                print(' ', end=' ')
        print()  # Move to the next line
    # Lower part of the pyramid
    for i in range(n, 0, -1):  # Loop to iterate through no.o lines
        for j in range(n - i):  # Loop to add leading spaces
            print(' ', end='')
        for k in range(1, i + 1):  # Loop to print numbers
            if k == 1 or k == i:
                print(n + 1 - i, end=' ')  # Print n+1-i
            else:
                print(' ', end=' ')
        print()  # Move to the next line
        """)

    case "hallow diamond alpha pat 94":
        st.code("""
def hallow_diamond_alpha_pat_94(n):
    for i in range(n):  # loop for n number of rows
        for j in range(n - i):  # loop for n-i number of spaces
            print(' ', end='')  # printing n-i spaces
        for k in range(1, i + 1):  # loop for i number of columns
            if k == 1 or k == i:
                print(chr(64 + i), end=' ')  # print alphabetic pattern
            else:
                print(' ', end=' ')  # print spaces
        print()  # next line

    for i in range(n, 0, -1):  # loop for n number of rows
        for j in range(n - i):  # loop for n-i number of spaces
            print(' ', end='')  # printing n-i spaces
        for k in range(1, i + 1):  # loop for i number of columns
            if k == 1 or k == i:
                print(chr(64 + i), end=' ')  # print alphabetic pattern
            else:
                print(' ', end=' ')  # print spaces
        print()  # next line
        """)

    case "hallow diamond alpha pat 95":
        st.code("""
def hallow_diamond_alpha_pat_95(n):
    # Upper part of the pyramid
    for i in range(n):  # Loop to iterate through no.o lines
        for j in range(n - i):  # Loop to add leading spaces
            print(' ', end='')
        for k in range(1, i + 1):  # Loop to print numbers
            if k == 1 or k == i:
                print(chr(65 + n - i), end=' ')  # Print the alphabet
            else:
                print(' ', end=' ')
        print()  # Move to the next line
    # Lower part of the pyramid
    for i in range(n, 0, -1):  # Loop to iterate through no.o lines
        for j in range(n - i):  # Loop to add leading spaces
            print(' ', end='')
        for k in range(1, i + 1):  # Loop to print numbers
            if k == 1 or k == i:
                print(chr(65 + n - i), end=' ')  # Print the alphabet
            else:
                print(' ', end=' ')
        print()  # Move to the next line
        """)

    case "half diamond with increasing space 96":
        st.code("""
def half_diamond_with_increasing_space_96(n):
    for i in range(n, -1, -1):  # Loop to print the pattern in descending order
        for j in range(i):  # First inner loop for left-aligned asterisks
            print("*", end='')
        for k in range(n - i):  # Second inner loop for spaces
            print(' ', end=' ')
        for k in range(i):  # Third inner loop for right-aligned asterisks
            print("*", end='')
        print()  # Next line
        """)

    case "decreasing space diamond pattern 97":
        st.code("""
def decreasing_space_diamond_pattern_97(n):
    for i in range(n):  # loop for n number of rows
        for j in range(i + 1):  # loop for i number of columns
            print("*", end='')  # print i number of *'s
        for k in range(n - i - 1):  # loop for n-i-1 spaces
            print(" ", end=' ')  # print n-i-1 spaces
        for m in range(i + 1):  # loop for i number of columns
            print("*", end='')  # print i number of *'s
        print()  # Next line
        """)

    case "mirrored diamond 98":
        st.code("""
def mirrored_diamond_98(n):
        for i in range(n):  # loop for n number of rows
            for j in range(i + 1):  # loop for i number of columns
                print("*", end='')  # print i number of *'s
            for k in range(n - i - 1):  # loop for n-i-1 spaces
                print(" ", end=' ')  # print n-i-1 spaces
            for m in range(i + 1):  # loop for i number of columns
                print("*", end='')  # print i number of *'s
            print()  # Next line

        for i in range(n - 1, 0, -1):  # loop for n-1 number of rows
            for j in range(i):  # loop for i number of columns
                print("*", end='')  # print i number of *'s
            for k in range(n - i):  # loop for n-i spaces
                print(" ", end=' ')  # print n-i spaces
            for m in range(i):  # loop for i number of columns
                print("*", end='')  # print i number of *'s
            print()  # Next line
        """)

    case "symmetrical triangular pat 99":
        st.code("""
def symmetrical_triangular_pat_99(n):
    for i in range(n):  # loop for the number of rows
        for j in range(n - i - 1):  # printing spaces
            print(' ', end='')  # print spaces
        for k in range(2 * i + 1):  # printing asterisks
            print('*', end='')  # print asterisk
        print()  # move to the next line
        """)

    case "symmetrical triangular pat 100":
        st.code("""
def symmetrical_triangular_pat_100(n):
    for i in range(n):  # loop for the number of rows
        for j in range(n - i - 1):  # printing spaces
            print(' ', end='')  # print spaces
        for k in range(2 * i + 1):  # printing asterisks
            print('*', end='')  # print asterisk
        print()  # move to the next line
        """)
        


import io
import contextlib
            
st.title('Python Code Executor')
st.write("You can write and execute any Python code in the text area below.")

# Add a text area for the user to input Python code
code_input = st.text_area("Enter your Python code here:")

# Button to execute the code
if st.button("Run Code"):
    # Create a StringIO buffer to capture the output
    buffer = io.StringIO()

    # Try-except block to handle any exceptions during code execution
    try:
        # Redirect stdout to the buffer
        with contextlib.redirect_stdout(buffer):
            exec_globals = {}
            exec(code_input, exec_globals)  # Execute the code entered by the user
    except Exception as e:
        st.error(f"Error: {e}")

    # Display the captured output
    output = buffer.getvalue()
    if output:
        st.subheader("Output:")
        st.text(output)
    else:
        st.write("No output to display.")



