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

options = [
    "square grid pat 1", "square grid num pat 2", "square grid num pat 3",
    "square grid alpha pat 4", "square grid alpha pat 5", "square grid num pat 6",
    "square grid num pat 7", "square grid alpha pat 8", "square grid alpha pat 9",
    "increasing triangular pat 10",
    
    "increasing triangular num pat 11", "increasing triangular num pat 12",
    "increasing triangular alpha pat 13", "increasing triangular alpha pat 14",
    "decreasing triangular pat 15", "decreasing triangular num pat 16",
    "decreasing triangular num pat 17", "decreasing triangular alpha pat 18",
    "decreasing triangular alpha pat 19", "decreasing triangular num pat 20",
    
    "decreasing triangular num pat 21", "decreasing triangular alpha pat 22",
    "decreasing triangular alpha pat 23", "right aligned triangular pat 24",
    "right aligned triangular num pat 25", "right aligned triangular num pat 26",
    "right aligned triangular alpha pat 27", "right aligned triangular alpha pat 28",
    "right aligned decreasing triangular pat 29", "right aligned decreasing triangular num pat 30"

    ,"right-aligned decreasing triangular num pat 31",
    "right-aligned decreasing triangular alpha pat 32",
    "right-aligned decreasing triangular alpha pat 33",
    "increasing triangular pat 34",
    "increasing triangular num pat 35",
    "increasing triangular num pat 36",
    "increasing triangular alpha pat 37",
    "increasing triangular alpha pat 38",
    "increasing triangular num pat 39",
    "increasing triangular num pat 40"
    
    , "increasing triangular alpha pat 41", "increasing triangular alpha pat 42",
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
    "diamond pat 75", "diamond num pat 76", "diamond num pat 77",
    "diamond num pat 78", "diamond alpha pat 79", "diamond alpha pat 80",
    
    "inverted v shaped pat 81", "inverted v shaped num pat 82",
    "inverted v shaped num pat 83", "inverted v shaped alpha pat 84",
    "inverted v shaped alpha pat 85", "v shaped pat 86",
    "v shaped num pat 87", "v shaped num pat 88",
    "v shaped alpha pat 89", "v shaped alpha pat 90",
    
     "hallow diamond pat 91", "hallow diamond num pat 92", "hallow diamond num pat 93",
    "hallow diamond alpha pat 94", "hallow diamond alpha pat 95","half diamond with increasing space 96",
    "decreasing space diamond pattern 97", "mirrored diamond 98","symmetrical triangular pat 99",
    "symmetrical triangular pat 100",
]

selection = st.selectbox('Choose the pattern', options)

match selection:
    case "square grid pat 1":
        st.code("""
def square_grid_pat_1(n):
    i = 0  # Initializing i to zero
    while i < n:  # Using a while loop to iterate as long as i is less than n
        print("* " * n)  # Printing a row of asterisks '*' multiplied by the value of 'n'
        i += 1  # Incrementing the value of i by 1 in each iteration
        """)

    case "square grid num pat 2":
        st.code("""
def square_grid_num_pat_2(n):
    i = 1  # initializing i value for outer loop
    while i in range(1, n + 1):  # loop for n number of rows
        j = 1  # initializing j value for inner loop
        while j in range(1, n + 1):  # loop for n number of rows
            print(i, end=' ')  # printing the i value and all the elements in a row are separated with space
            j += 1  # incrementing j value
        i += 1  # incrementing i value
        print()  # An empty print() method for next line
        """)

    case "square grid num pat 3":
        st.code("""
def square_grid_num_pat_3(n):
    i = 1  # initializing i value for outer loop
    while i in range(1, n + 1):  # loop for n number of rows
        j = 1  # initializing j value for inner loop
        while j in range(1, n + 1):  # loop for n number of rows
            print(j, end=' ')  # printing the j value and all the elements in a row are separated with space
            j += 1  # incrementing j value
        i += 1  # incrementing i value
        print()  # An empty print() method for next line
        """)

    case "square grid alpha pat 4":
        st.code("""
def square_grid_alpha_pat_4(n):
    i = 65  # Initializing i value for the outer loop with ASCII value 'A'
    while i <= 65 + n - 1:  # Outer loop to iterate through each line
        j = 0  # Initializing z for the inner loop
        while j <= n - 1:  # Inner loop to print characters in each line
            print(chr(i), end=" ")  # Printing the character corresponding to the ASCII value of i
            j += 1  # Incrementing j to move to the next character in the line
        print()  # Moving to the next line after completing the inner loop
        i += 1  # Incrementing i to move to the next character for the next line.
        """)

    case "square grid alpha pat 5":
        st.code("""
def square_grid_alpha_pat_5(n):
    i = 0  # Initializing a variable i with value 0
    while i < n:  # Outer while loop iterating as long as i is less than n
        j = 0  # Initializing a variable j with value 0 for each row
        while j < n:  # Inner while loop iterating as long as j is less than n
            print(chr(65 + j), end=" ")  # Printing the uppercase letter corresponding to the ASCII value
            j += 1  # Incrementing the value of j by 1 in each iteration
        i += 1
        print()  # Moving to the next line after each inner loop completes
        """)

    case "square grid num pat 6":
        st.code("""
def square_grid_num_pat_6(n):
    i = n  # initializing i value to n
    while i != 0:  # loop for n number of columns
        j = n  # initializing j value to n
        while j != 0:  # loop for n number of columns
            print(i, end=' ')  # printing i value
            j -= 1  # decrementing j value
        i -= 1  # decrementing i value
        print()  # An empty print() method for next line
        """)

    case "square grid num pat 7":
        st.code("""
def square_grid_num_pat_7(n):
    i = n  # initializing i value to n
    while i != 0:  # loop for n number of columns
        j = n  # initializing j value to n
        while j != 0:  # loop for n number of columns
            print(j, end=' ')  # printing j value
            j -= 1  # decrementing j value
        i -= 1  # decrementing i value
        print()  # An empty print() method for next line
        """)

    case "square grid alpha pat 8":
        st.code("""
def square_grid_alpha_pat_8(n):
    i = 65 + n - 1  # Initializing i value for the outer loop with ASCII value of 'A' + n - 1
    while i >= 65:  # Outer loop to iterate through each line
        j = 0  # Initializing j for the inner loop
        while j <= n - 1:  # Inner loop to print the characters in each line
            print(chr(i), end=" ")  # Printing the character corresponding to the ASCII value of i
            j += 1  # Incrementing j to move to the next character in the line
        print()  # Moving to the next line after completing the inner loop
        i -= 1  # Decrementing i to move to the next character for the next line.
        """)

    case "square grid alpha pat 9":
        st.code("""
def square_grid_alpha_pat_9(n):
    i = 0  # Initializing a variable i with value 0
    while i < n:  # Outer while loop iterating as long as i is less than n
        j = 0  # Initializing a variable j with value 0 for each row
        while j < n:  # Inner while loop iterating as long as j is less than n
            print(chr(64 + n - j), end=" ")  # Printing the uppercase letter corresponding to the ASCII value
            j += 1  # Incrementing the value of j by 1 in each iteration
        print()  # Moving to the next line after each inner loop completes
        i += 1  # Incrementing the value of i by 1 after each outer loop iteration
        """)

    case "increasing triangular pat 10":
        st.code("""
def increasing_triangular_pat_10(n):
    i = 1  # initializing i value as 1
    while i <= n:  # loop for n number of rows
        j = 1  # initializing j value as 1
        while j <= i:  # loop for i number of columns for each row
            print("*", end=' ')  # printing * separated by space
            j += 1  # incrementing j value
        i += 1  # incrementing i value
        print()  # An empty print() method for next line
        """)

    case "increasing triangular num pat 11":
        st.code("""
def increasing_triangular_num_pat_11(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(i, end=' ')
            j += 1
        i += 1
        print()""")

    case "increasing triangular num pat 12":
        st.code("""
def increasing_triangular_num_pat_12(n):
    i = 0
    while i < n:
        j = 0
        while j <= i:
            print(j + 1, end=' ')
            j += 1
        i += 1
        print()""")

    case "increasing triangular alpha pat 13":
        st.code("""
def increasing_triangular_alpha_pat_13(n):
    i = 0
    while i < n:
        j = 0
        while j <= i:
            print(chr(65 + i), end=' ')
            j += 1
        i += 1
        print()""")

    case "increasing triangular alpha pat 14":
        st.code("""
def increasing_triangular_alpha_pat_14(n):
    i = 0
    while i < n:
        j = 0
        while j <= i:
            print(chr(65 + j), end=' ')
            j += 1
        i += 1
        print()""")

    case "decreasing triangular pat 15":
        st.code("""
def decreasing_triangular_pat_15(n):
    i = n
    while i > 0:
        j = 0
        while j < i:
            print("*", end=' ')
            j += 1
        i -= 1
        print()""")

    case "decreasing triangular num pat 16":
        st.code("""
def decreasing_triangular_num_pat_16(n):
    i = n - 1
    c = 1
    while i > 0:
        j = 0
        while j < i:
            print(c, end=' ')
            j += 1
        i -= 1
        c += 1
        print()""")

    case "decreasing triangular num pat 17":
        st.code("""
def decreasing_triangular_num_pat_17(n):
    i = 0
    while i < n:
        j = 0
        while j < n - i:
            print(j + 1, end=' ')
            j += 1
        i += 1
        print()""")

    case "decreasing triangular alpha pat 18":
        st.code("""
def decreasing_triangular_alpha_pat_18(n):
    i = n
    c = 0
    while i > 0:
        j = 0
        while j < i:
            print(chr(65 + c), end=' ')
            j += 1
        i -= 1
        c += 1
        print()""")

    case "decreasing triangular alpha pat 19":
        st.code("""
def decreasing_triangular_alpha_pat_19(n):
    i = n
    while i > 0:
        j = 0
        while j < i:
            print(chr(65 + j), end=' ')
            j += 1
        i -= 1
        print()""")

    case "decreasing triangular num pat 20":
        st.code("""
def decreasing_triangular_num_pat_20(n):
    i = n
    while i > 0:
        j = 0
        while j < i:
            print(i, end=' ')
            j += 1
        i -= 1
        print()""")
    
    
    case "decreasing triangular num pat 21":
        st.code("""
def decreasing_triangular_num_pat_21(n):
    c = n
    i = n
    while i > -1:
        j = 0
        while j < i:
            print(c - j, end=' ')
            j += 1
        print()
        i -= 1
        """)
    case "decreasing triangular alpha pat 22":
        st.code("""
def decreasing_triangular_alpha_pat_22(n):
    i = n
    while i > 0:
        j = 0
        while j < i:
            print(chr(65 + i - 1), end=' ')
            j += 1
        i -= 1
        print()
        """)
    case "decreasing triangular alpha pat 23":
        st.code("""
def decreasing_triangular_alpha_pat_23(n):
    ch = 65 + n
    i = n
    while i >= 0:
        j = 0
        while j <= i:
            print(chr(ch - j), end=' ')
            j += 1
        i -= 1
        print()
        """)
    case "right aligned triangular pat 24":
        st.code("""
def right_aligned_triangular_pat_24(n):
    i = 0
    while i < n + 1:
        j, k = 0, 0
        while j < n - i:
            print(' ', end=' ')
            j += 1
        while k < i:
            print('*', end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned triangular num pat 25":
        st.code("""
def right_aligned_triangular_num_pat_25(n):
    i = 0
    while i < n + 1:
        j, k = 0, 0
        while j < n - i:
            print(' ', end=' ')
            j += 1
        while k < i:
            print(i, end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned triangular num pat 26":
        st.code("""
def right_aligned_triangular_num_pat_26(n):
    i = 1
    while i in range(1, n + 1):
        j, k = 0, 1
        while j in range(n - i):
            print(' ', end=' ')
            j += 1
        while k in range(1, i + 1):
            print(k, end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned triangular alpha pat 27":
        st.code("""
def right_aligned_triangular_alpha_pat_27(n):
    i = 1
    while i in range(1, n + 1):
        j, k = 0, 1
        while j in range(n - i):
            print(' ', end=' ')
            j += 1
        while k in range(1, i + 1):
            print(chr(64 + i), end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned triangular alpha pat 28":
        st.code("""
def right_aligned_triangular_alpha_pat_28(n):
    i = 0
    while i in range(n + 1):
        j, k = 0, 65
        while j in range(n - i):
            print(' ', end=' ')
            j += 1
        while k in range(65, 65 + i):
            print(chr(k), end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned decreasing triangular pat 29":
        st.code("""
def right_aligned_decreasing_triangular_pat_29(n):
    i = 0
    while i < n:
        j, k = 0, 0
        while j < i:
            print(' ', end=' ')
            j += 1
        while k < n - i:
            print('*', end=' ')
            k += 1
        i += 1
        print()
        """)
    case "right aligned decreasing triangular num pat 30":
        st.code("""
def right_aligned_decreasing_triangular_num_pat_30(n):
    i = n
    while i > 0:
        j, k = 0, 0
        while j in range(n - i):
            print(' ', end=' ')
            j += 1
        while k in range(i):
            print(i, end=' ')
            k += 1
        i -= 1
        print()
        """)
       
    case "right-aligned decreasing triangular num pat 31":
        st.code("""
def right_aligned_decreasing_triangular_num_pat_31(n):
    i = n
    while i > 0:
        j, k = 0, 1
        while j in range(n - i):
            print(" ", end=' ')
            j += 1
        while k in range(i + 1):
            print(k, end=' ')
            k += 1
        i -= 1
        print()
""")

    case "right-aligned decreasing triangular alpha pat 32":
        st.code("""
def right_aligned_decreasing_triangular_alpha_pat_32(n):
    i = n
    while i in range(n, 0, -1):
        j, k = 0, 65
        while j in range(n - i + 1):
            print(" ", end=' ')
            j += 1
        m = 65
        while k in range(65, 65 + i):
            print(chr(m + i - 1), end=' ')
            k += 1
        i -= 1
        print()
""")

    case "right-aligned decreasing triangular alpha pat 33":
        st.code("""
def right_aligned_decreasing_triangular_alpha_pat_33(n):
    i = n
    while i > 0:
        j, k = 0, 0
        while j < n - i:
            print(" ", end=" ")
            j += 1
        while k < i:
            print(chr(65 + k), end=" ")
            k += 1
        print()
        i -= 1
""")

    case "increasing triangular pat 34":
        st.code("""
def increasing_triangular_pat_34(n):
    i = 1
    while i <= n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print("*", end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 35":
        st.code("""
def increasing_triangular_num_pat_35(n):
    i = 1
    while i <= n:
        k, j = 0, 0
        while j < n - i:
            print(" ", end=' ')
            j += 1
        while k < i * 2 - 1:
            print(i, end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 36":
        st.code("""
def increasing_triangular_num_pat_36(n):
    i, j, m = 1, 0, 1
    while i < n // 2 + 2:
        j, k = 0, 0
        while j < n - i:
            print(" ", end=' ')
            j += 1
        while k < 2 * i - 1:
            print(m, end=' ')
            k += 1
        m += 2
        i += 1
        print()
""")

    case "increasing triangular alpha pat 37":
        st.code("""
def increasing_triangular_alpha_pat_37(n):
    i = 0
    while i < n:
        j, k = 0, 0
        while j < n - i:
            print(" ", end=" ")
            j += 1
        while k < i * 2 + 1:
            print(chr(65 + i), end=" ")
            k += 1
        print()
        i += 1
""")

    case "increasing triangular alpha pat 38":
        st.code("""
def increasing_triangular_alpha_pat_38(n):
    i, x = 0, 0
    while i < n // 2:
        j, k = 0, 0
        while j < n - i:
            print(" ", end=' ')
            j += 1
        while k < i * 2 + 1:
            print(chr(65 + x), end=' ')
            k += 1
        x += 2
        i += 1
        print()
""")

    case "increasing triangular num pat 39":
        st.code("""
def increasing_triangular_num_pat_39(n):
    i = 1
    while i <= n // 2:
        k, j = 1, 0
        while j < n - i:
            print(" ", end=' ')
            j += 1
        while k <= i * 2 - 1:
            print(k, end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 40":
        st.code("""
def increasing_triangular_num_pat_40(n):
    i, x = 0, 1
    while i <= n // 2:
        k, j = 0, 0
        while j < n - i - n // 2 - 1:
            print(" ", end=" ")
            j += 1
        while k < 2 * i + 1:
            print(x - k, end=" ")
            k += 1
        x += 2
        i += 1
        print()
""") 
    
    case "increasing triangular alpha pat 41":
        st.code("""
def increasing_triangular_alpha_pat_41(self):
    i = 0
    while i < self.n // 2 + 1:
        j, k = 0, 0
        while j < self.n - i - self.n // 2:
            print(" ", end=" ")
            j += 1
        while k < i * 2 + 1:
            print(chr(65 + k), end=" ")
            k += 1
        print()
        i += 1
""")

    case "increasing triangular alpha pat 42":
        st.code("""
def increasing_triangular_alpha_pat_42(self):
    i = x = 0
    while i <= self.n // 2:
        k, j = 0, 0
        while j < self.n - i:
            print(" ", end=' ')
            j += 1
        while k < i * 2 + 1:
            print(chr(65 + x - k), end=' ')
            k += 1
        i += 1
        x += 2
        print()
""")

    case "increasing triangular num pat 43":
        st.code("""
def increasing_triangular_num_pat_43(self):
    i = 0
    while i <= self.n:
        j, m = 0, 1
        k = i
        while j < self.n - i:
            print(" ", end=' ')
            j += 1
        while k >= 0:
            print(k, end=' ')
            k -= 1
        while m <= i:
            print(m, end=' ')
            m += 1
        i += 1
        print()
""")

    case "increasing triangular alpha pat 44":
        st.code("""
def increasing_triangular_alpha_pat_44(self):
    i = 1
    while i <= self.n:
        j, k, m = 0, i - 1, 0
        while j < self.n - i:
            print(" ", end=" ")
            j += 1
        while k > 0:
            print(chr(65 + k), end=" ")
            k -= 1
        while m < i:
            print(chr(65 + m), end=" ")
            m += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 45":
        st.code("""
def increasing_triangular_num_pat_45(self):
    i = 1
    while i < self.n + 1:
        j, k, l = 1, 1, i - 1
        while j <= self.n - i:
            print(" ", end=" ")
            j += 1
        while k < i + 1:
            print(k, end=" ")
            k += 1
        while l > 0:
            print(l, end=" ")
            l -= 1
        print()
        i += 1
""")

    case "increasing triangular alpha pat 46":
        st.code("""
def increasing_triangular_alpha_pat_46(self):
    i = 0
    while i <= self.n:
        j = k = 0
        m = i - 1
        while j < self.n - i:
            print(" ", end=' ')
            j += 1
        while k < i:
            print(chr(65 + k), end=' ')
            k += 1
        while m > 0:
            print(chr(65 + m - 1), end=' ')
            m -= 1
        i += 1
        print()
""")

    case "left aligned decreasing triangular pat 47":
        st.code("""
def left_aligned_decreasing_triangular_pat_47(self):
    i = self.n // 2 + 1
    while i > 0:
        j, k = 0, 1
        while j < self.n - i:
            print(" ", end=' ')
            j += 1
        while k < i * 2:
            print("*", end=' ')
            k += 1
        i -= 1
        print()
""")

    case "left aligned decreasing triangular num pat 48":
        st.code("""
def left_aligned_decreasing_triangular_num_pat_48(self):
    m = 2
    i = self.n - 1
    while i > -1:
        j, k = 0, 0
        while j < self.n - i:
            print(" ", end=" ")
            j += 1
        while k < self.n + i - m:
            print(i, end=" ")
            k += 1
        m += 1
        i -= 1
        print()
""")

    case "left aligned decreasing triangular num pat 49":
        st.code("""
def left_aligned_decreasing_triangular_num_pat_49(self):
    i = self.n
    while i > 0:
        j, k = 0, 0
        while j < self.n - i // 2 - self.n // 2 + 1:
            print(" ", end=" ")
            j += 1
        while k < i:
            print(i, end=" ")
            k += 1
        print()
        i -= 2
""")

    case "inverted pyramid num pat 50":
        st.code("""
def inverted_pyramid_num_pat_50(self):
    i = self.n // 2 + 1
    while i > 0:
        j, k = 0, 1
        while j < self.n - i:
            print(" ", end=' ')
            j += 1
        while k < i * 2:
            print(k, end=' ')
            k += 1
        i -= 1
        print()
""")
    
    case "inverted pyramid alpha pat 51":
        st.code("""
def inverted_pyramid_alpha_pat_51(n):
    i=n
    while i>0:
        j,k=0,1
        while j<n-i:
            print(" ",end=' ')
            j+=1
        while k <i*2:
            print(chr(64+i),end=' ')
            k+=1
        i-=1
        print()
""")
    case "inverted pyramid alpha pat 52":
        st.code("""
def inverted_pyramid_alpha_pat_52(n):
    p=65+n*2-2
    m=1
    i=n
    while i>0:
        j,k=0,0
        while j<n-i+1:
            print(" ",end=" ")
            j+=1
        while k<n+i-m:
            print(chr(p),end=" ")
            k+=1
        p-=2
        m+=1
        i-=1
        print()
""")
    case "inverted pyramid alpha pat 53":
        st.code("""
def inverted_pyramid_alpha_pat_53(n):
    m=0
    i=n//2+1
    while i>0:
        print(" "*m,end=" ")
        j=0
        while j<i*2-1:
            print(chr(65+j),end=" ")
            j+=1
        m+=2
        print()
        i-=1
""")
    case "alternating triangular pat 54":
        st.code("""
def alternating_triangular_pat_54(n):
    i=0
    while i<n:
        j=0
        while j<i:
            print("*",end=' ')
            j+=1
        i+=1
        print()
    while i>0:
        j=0
        while j<i:
            print("*",end=' ')
            j+=1
        i-=1
        print()
""")
    case "alternating triangular num pat 55":
        st.code("""
def alternating_triangular_num_pat_55(n):
    i=0
    while i<=n:
        j=0
        while j<i:
            print(n-j,end=' ')
            j+=1
        i+=1
        print()

    while i>0:
        j=0
        while j<i:
            print(n-j,end=' ')
            j+=1
        i-=1
        print()
""")
    case "alternating triangular num pat 56":
        st.code("""
def alternating_triangular_num_pat_56(n):
    i=0
    while i<n:
        j=i
        while j>-1:
            print(n-j,end=' ')
            j-=1
        i+=1
        print()
    while i>=0:
        j=i
        while j>-1:
            print(n-j,end=' ')
            j-=1
        i-=1
        print()
""")
    case "alternating triangular alpha pat 57":
        st.code("""
def alternating_triangular_alpha_pat_57(n):
    i=0
    while i<=n:
        j=0
        while j<i:
            print(chr(65+n-j),end=' ')
            j+=1
        i+=1
        print()

    while i>0:
        j=0
        while j<i:
            print(chr(65+n-j),end=' ')
            j+=1
        i-=1
        print()
""")
    case "alternating triangular alpha pat 58":
        st.code("""
def alternating_triangular_alpha_pat_58(n):
    i=0
    while i<n:
        j=i
        while j>-1:
            print(chr(65+n-j),end=' ')
            j-=1
        i+=1
        print()

    while i>=0:
        j=i
        while j>-1:
            print(chr(65+n-j),end=' ')
            j-=1
        i-=1
        print()
""")
    case "left pascal triangle pat 59":
        st.code("""
def left_pascal_triangle_pat_59(n):
    i=0
    while i<n:
        x=0
        j=k=0
        while k<n-i:
            print(' ',end=' ')
            k+=1
            x+=1
        while j<i:
            print("*",end=' ')
            j+=1
            x+=1
        i+=1
        print()

    while i>0:
        x=0
        j=k=0
        while k<n-i:
            print(' ',end=' ')
            k+=1
            x+=1
        while j<i:
            print("*",end=' ')
            j+=1
            x+=1
        i-=1
        print()
""")
    case "left pascal triangle num pat 60":
        st.code("""
def left_pascal_triangle_num_pat_60(n):
    i=0
    while i<n:
        j=k=0
        while k<n-i:
            print(' ',end=' ')
            k+=1
        while j<i+1:
            print(n-j,end=' ')
            j+=1
        i+=1
        print()
    
    i=n
    while i>-1:
        j=k=0
        while k<n-i:
            print(' ',end=' ')
            k+=1
        while j<i+1:
            print(n-j,end=' ')
            j+=1
        i-=1
        print()
""")
        
    case "left pascal triangle num pat 61":
        st.code("""
def left_pascal_triangle_num_pat_61(n):
    i = 0
    while i < n:
        x, j, k = 0, 0, 0
        while j < n - i:
            print(" ", end=' ')
            x += 1
            j += 1
        while k < i + 1:
            print(x, end=' ')
            x += 1
            k += 1
        print()
        i += 1
    i = n
    while i > -1:
        x, j, k = 0, 0, 0
        while j < n - i:
            print(" ", end=' ')
            x += 1
            j += 1
        while k < i + 1:
            print(x, end=' ')
            k += 1
            x += 1
        print()
        i -= 1
""")
        
    case "left pascal triangle alpha pat 62":
        st.code("""
def left_pascal_triangle_alpha_pat_62(n):
    i = 0
    while i < n:
        x = 0
        j = k = 0
        while k < n - i:
            print(' ', end=' ')
            k += 1
            x += 1
        while j < i:
            print(chr(ord('A') + x), end=' ')
            j += 1
            x += 1
        i += 1
        print()
    while i > 0:
        x = 0
        j = k = 0
        while k < n - i:
            print(' ', end=' ')
            k += 1
            x += 1
        while j < i:
            print(chr(ord('A') + x), end=' ')
            j += 1
            x += 1
        i -= 1
        print()
""")

    case "left pascal triangle alpha pat 63":
        st.code("""
def left_pascal_triangle_alpha_pat_63(n):
    i = 0
    while i < n:
        x = 0
        j = k = 0
        while k < n - i:
            print(' ', end=' ')
            k += 1
            x += 1
        while j <= i:
            print(chr(65 + n - j), end=' ')
            j += 1
            x += 1
        i += 1
        print()
    while i >= 0:
        x = 0
        j = k = 0
        while k < n - i:
            print(' ', end=' ')
            k += 1
            x += 1
        while j <= i:
            print(chr(65 + n - j), end=' ')
            j += 1
            x += 1
        i -= 1
        print()
""")

    case "increasing triangular pat 64":
        st.code("""
def increasing_triangular_pat_64(n):
    i = 0
    while i <= n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print("*", end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 65":
        st.code("""
def increasing_triangular_num_pat_65(n):
    i = 0
    while i <= n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(i, end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular num pat 66":
        st.code("""
def increasing_triangular_num_pat_66(n):
    i = 1
    while i <= n:
        j = 0
        k = 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(k, end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular alpha pat 67":
        st.code("""
def increasing_triangular_alpha_pat_67(n):
    i = 0
    while i <= n:
        j = 0
        k = 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(chr(64 + i), end=' ')
            k += 1
        i += 1
        print()
""")

    case "increasing triangular alpha pat 68":
        st.code("""
def increasing_triangular_alpha_pat_68(n):
    i = 0
    while i <= n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(chr(64 + k), end=' ')
            k += 1
        i += 1
        print()
""")

    case "decreasing triangular pat 69":
        st.code("""
def decreasing_triangular_pat_69(n):
    i = n
    while i > -1:
        j, k = 0, 0
        while j < n - i:
            print(end=" ")
            j += 1
        while k < i:
            print("*", end=" ")
            k += 1
        print()
        i -= 1
""")

    case "decreasing triangular num pat 70":
        st.code("""
def decreasing_triangular_num_pat_70(n):
    i = n
    while i > 0:
        j = k = 0
        while j < n - i:
            print(" ", end='')
            j += 1
        while k < i:
            print(i, end=' ')
            k += 1
        i -= 1
        print()
""")
        
    case "decreasing triangular num pat 71":
        st.code("""
def decreasing_triangular_num_pat_71(n):
    i = n
    while i > 0:
        j = k = 0
        while j < n - i:
            print(" ", end='')
            j += 1
        while k < i:
            print(i - k, end=' ')
            k += 1
        i -= 1
        print()""")

    case "decreasing triangular alpha pat 72":
        st.code("""
def decreasing_triangular_alpha_pat_72(n):
    i = n
    while i > 0:
        j = k = 0
        while j < n - i + 1:
            print(" ", end='')
            j += 1
        while k < i:
            print(chr(64 + i), end=' ')
            k += 1
        i -= 1
        print()""")

    case "decreasing triangular alpha pat 73":
        st.code("""
def decreasing_triangular_alpha_pat_73(n):
    i = n
    while i > 0:
        j = k = 0
        while j < n - i + 1:
            print(" ", end="")
            j += 1
        while k < i:
            print(chr(64 + i - k), end=" ")
            k += 1
        print()
        i -= 1""")

    case "decreasing triangular alpha pat 74":
        st.code("""
def decreasing_triangular_alpha_pat_74(n):
    i = n
    while i > 0:
        j = k = 0
        while j < n - i:
            print(" ", end='')
            j += 1
        while k < i:
            print(chr(65 + k), end=' ')
            k += 1
        i -= 1
        print()""")

    case "diamond pat 75":
        st.code("""
def diamond_pat_75(n):
    i = 1
    while i < n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print("*", end=' ')
            k += 1
        i += 1
        print()
    while i > 0:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print("*", end=' ')
            k += 1
        i -= 1
        print()""")

    case "diamond num pat 76":
        st.code("""
def diamond_num_pat_76(n):
    i = 0
    while i < n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(i, end=' ')
            k += 1
        i += 1
        print()
    while i > 0:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(i, end=' ')
            k += 1
        i -= 1
        print()""")

    case "diamond num pat 77":
        st.code("""
def diamond_num_pat_77(n):
    i = 0
    while i < n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(k, end=' ')
            k += 1
        i += 1
        print()
    m = 1
    while i > 0:
        j, k = 0, 0
        while j < n - i:
            print(" ", end='')
            j += 1
        while k < i:
            print(k + m, end=' ')
            k += 1
        m += 1
        i -= 1
        print()""")

    case "diamond num pat 78":
        st.code("""
def diamond_num_pat_78(n):
    i = 1
    while i < n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(k, end=' ')
            k += 1
        i += 1
        print()
    while i > 0:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(k, end=' ')
            k += 1
        i -= 1
        print()""")

    case "diamond alpha pat 79":
        st.code("""
def diamond_alpha_pat_79(n):
    i = 1
    while i < n:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(chr(64 + i), end=' ')
            k += 1
        i += 1
        print()
    while i > 0:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(chr(64 + i), end=' ')
            k += 1
        i -= 1
        print()""")

    case "diamond alpha pat 80":
        st.code("""
def diamond_alpha_pat_80(n):
    i = 1
    while i < n + 1:
        j, k = 0, 1
        while j < n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            print(chr(64 + k), end=' ')
            k += 1
        i += 1
        print()
    i = 1
    m = 1
    while i < n:
        j, k = 0, 1
        while j < i:
            print(" ", end='')
            j += 1
        while k < n - i + 1:
            print(chr(64 + k + m), end=' ')
            k += 1
        m += 1
        i += 1
        print()""")
    
    case "inverted v shaped pat 81":
        st.code("""
def inverted_v_shaped_pat_81(self):
    i = 1
    while i <= self.n + 1:
        j, k = 0, 1
        while j <= self.n - i + 1:
            print(' ', end='')
            j += 1
        while k < i + 1:
            if k == 1 or k == i:
                print("*", end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i += 1
        print()
""")
    
    case "inverted v shaped num pat 82":
        st.code("""
def inverted_v_shaped_num_pat_82(self):
    i = 1
    while i <= self.n:
        j, k = 0, 1
        while j < self.n - i:
            print(' ', end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(i, end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i += 1
        print()
""")

    case "inverted v shaped num pat 83":
        st.code("""
def inverted_v_shaped_num_pat_83(self):
    i = 0
    while i < self.n:
        j, k = 0, 0
        while j < self.n - i:
            print(' ', end='')
            j += 1
        while k <= i:
            if k == 0 or k == i:
                print(self.n - i, end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i += 1
        print()
""")

    case "inverted v shaped alpha pat 84":
        st.code("""
def inverted_v_shaped_alpha_pat_84(self):
    i = 1
    while i <= self.n:
        j, k = 0, 1
        while j < self.n - i + 2:
            print(' ', end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(chr(64 + i), end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i += 1
        print()
""")

    case "inverted v shaped alpha pat 85":
        st.code("""
def inverted_v_shaped_alpha_pat_85(self):
    i = 1
    while i <= self.n:
        j, k = 0, 1
        while j <= self.n - i:
            print(' ', end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(chr(65 + self.n - i), end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i += 1
        print()
""")

    case "v shaped pat 86":
        st.code("""
def v_shaped_pat_86(self):
    i = self.n
    while i >= 0:
        j, k = 0, 0
        while j < self.n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            if k == 0 or k == i:
                print("*", end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i -= 1
        print()
""")

    case "v shaped num pat 87":
        st.code("""
def v_shaped_num_pat_87(self):
    i = self.n
    while i > 0:
        j, k = 0, 0
        while j < self.n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(self.n - i + 1, end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i -= 1
        print()
""")

    case "v shaped num pat 88":
        st.code("""
def v_shaped_num_pat_88(self):
    i = self.n
    while i > 0:
        j, k = 0, 1
        while j < self.n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(i, end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i -= 1
        print()
""")

    case "v shaped alpha pat 89":
        st.code("""
def v_shaped_alpha_pat_89(self):
    i = self.n
    m = 1
    while i > 0:
        j, k = 0, 0
        while j < self.n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(chr(64 + m), end=' ')
            else:
                print(" ", end=' ')
            k += 1
        m += 1
        i -= 1
        print()
""")

    case "v shaped alpha pat 90":
        st.code("""
def v_shaped_alpha_pat_90(self):
    i = self.n
    while i > 0:
        j, k = 0, 1
        while j < self.n - i:
            print(" ", end='')
            j += 1
        while k <= i:
            if k == 1 or k == i:
                print(chr(64 + i), end=' ')
            else:
                print(" ", end=' ')
            k += 1
        i -= 1
        print()
""")    
    
    case "hallow diamond pat 91":
        st.code("""
def hallow_diamond_pat_91(self):
    i = 0  # initializing i value with 0
    while i < self.n:  # loop for n number of rows
        j, k = 0, 0  # initializing j and k values with 0
        while j < self.n - i:  # loop for n-i number of spaces in each row
            print(" ", end='')  # printing n-i spaces
            j += 1  # incrementing j value
        while k <= i:  # loop for i number of columns
            if k == 0 or k == i:  # Checking whether the value of k is equal to 0 or i.
                print("*", end=' ')  # printing alphabetic pattern if the k value is either 0 or i
            else:  # else block will execute if k value is neither 0 nor i
                print(" ", end=' ')  # printing spaces
            k += 1  # incrementing k value
        i += 1  # incrementing i value
        print()  # an empty print() for next line

    while i >= 0:  # loop for n number of rows
        j, k = 0, 0  # initializing j and k value with 0
        while j < self.n - i:  # loop for n-i number of spaces in each row
            print(" ", end='')  # printing n-i spaces
            j += 1  # incrementing j value
        while k <= i:  # loop for i number of columns
            if k == 0 or k == i:  # Checking whether the value of k is equal to 0 or i.
                print("*", end=' ')  # printing alphabetic pattern if the k value is either 0 or i
            else:  # else block will execute if k value is neither 0 nor i
                print(" ", end=' ')  # printing spaces
            k += 1  # incrementing k value
        i -= 1  # decrementing i value
        print()  # an empty print() for next line
        """)

    case "hallow diamond num pat 92":
        st.code("""
def hallow_diamond_num_pat_92(self):
    i = 0  # Initializing i to 0
    while i < self.n:  # Loop for no. of rows
        j, k = 0, 1  # Initializing variables for the first and second inner loops
        while j < self.n - i:  # First inner loop to print spaces before the numbers in each line
            print(" ", end='')
            j += 1
        while k <= i:  # Second inner loop to print numbers in the shape of an isosceles triangle
            if k == 1 or k == i:
                print(i, end=' ')  # Printing the number 'i' at the beginning and end of each line
            else:
                print(" ", end=' ')  # Printing a space for the inner numbers
            k += 1
        i += 1  # Incrementing i for the next line
        print()  # Moving to the next line after completing the inner loops
        """)

    case "hallow diamond num pat 93":
        st.code("""
def hallow_diamond_num_pat_93(self):
    # Upper part of the pyramid
    i = 0
    while i < self.n:  # Loop to iterate through no. of lines
        j, k = 0, 1
        while j < self.n - i:  # Loop to add leading spaces for formatting
            print(' ', end='')
            j += 1
        while k <= i + 1:  # Loop to print numbers for the current row
            if k == 1 or k == i:
                print(self.n + 1 - i, end=' ')
            else:
                print(' ', end=' ')
            k += 1
        print()  # Move to the next line after completing the row
        i += 1
    # Lower part of the pyramid
    i = self.n
    while i > 0:  # Loop to iterate through no. of lines
        j, k = 0, 1
        while j < self.n - i:  # Loop to add leading spaces for formatting
            print(' ', end='')
            j += 1
        while k <= i + 1:  # Loop to print numbers for the current row
            if k == 1 or k == i:
                print(self.n + 1 - i, end=' ')
            else:
                print(' ', end=' ')
            k += 1
        print()  # Move to the next line after completing the row
        i -= 1
        """)

    case "hallow diamond alpha pat 94":
        st.code("""
def hallow_diamond_alpha_pat_94(self):
    i = 0  # initializing i value with 0
    while i < self.n:  # loop for n number of rows
        j, k = 0, 1  # initializing j and k values with 0 and 1
        while j < self.n - i:  # loop for n-i number of spaces in each row
            print(" ", end='')  # printing n-i spaces
            j += 1  # incrementing j value
        while k <= i:  # loop for i number of columns
            if k == 1 or k == i:  # Checking whether the value of k is equal to 1 or i.
                print(chr(64 + i), end=' ')  # printing alphabetic pattern if the k value is either 1 or i
            else:  # else block will execute if k value is neither 1 nor i
                print(" ", end=' ')  # printing spaces
            k += 1  # incrementing k value
        i += 1  # incrementing i value
        print()  # an empty print() for next line

    while i > 0:  # loop for n number of rows
        j, k = 0, 1  # initializing j and k value with 0 and 1
        while j < self.n - i:  # loop for n-i number of spaces in each row
            print(" ", end='')  # printing n-i spaces
            j += 1  # incrementing j value
        while k <= i:  # loop for i number of columns
            if k == 1 or k == i:  # Checking whether the value of k is equal to 1 or i.
                print(chr(64 + i), end=' ')  # printing alphabetic pattern if the k value is either 1 or i
            else:  # else block will execute if k value is neither 1 nor i
                print(" ", end=' ')  # printing spaces
            k += 1  # incrementing k value
        i -= 1  # decrementing i value
        print()  # an empty print() for next line
        """)

    case "hallow diamond alpha pat 95":
        st.code("""
def hallow_diamond_alpha_pat_95(self):
    # Upper part of the pyramid
    i = 0
    while i < self.n:  # Loop to iterate through no. of lines
        j, k = 0, 1
        while j < self.n - i:  # Loop to add leading spaces for formatting
            print(' ', end='')
            j += 1
        while k <= i + 1:  # Loop to print numbers for the current row
            if k == 1 or k == i:  # Print the alphabet chr(65+n+1-i) at the first and last position in the row, otherwise print a space
                print(chr(65 + self.n - i), end=' ')
            else:
                print(' ', end=' ')
            k += 1
        print()  # Move to the next line after completing the row
        i += 1
    # Lower part of the pyramid
    i = self.n
    while i > 0:  # Loop to iterate through no. of lines
        j, k = 0, 1
        while j < self.n - i:  # Loop to add leading spaces for formatting
            print(' ', end='')
            j += 1
        while k <= i + 1:  # Loop to print numbers for the current row
            if k == 1 or k == i:  # Print the alphabet chr(65+n+1-i) at the first and last position in the row, otherwise print a space
                print(chr(65 + self.n - i), end=" ")
            else:
                print(' ', end=' ')
            k += 1
        print() """)
    
    case "half diamond with increasing space 96":
        st.code("""
def half_diamond_with_increasing_space_96(n):
    i = n  # Initializing i for the outer loop
    while i > -1:  # Outer loop to print the pattern in descending order
        j = k = m = 0  # Initializing variables for the first, second, and third inner loops
        while j < i:  # First inner loop to print left-aligned asterisks
            print("*", end='')
            j += 1
        while k <= n - i - 1:  # Second inner loop to print spaces, aligning to the right
            print(' ', end=' ')
            k += 1
        while m < i:  # Third inner loop to print right-aligned asterisks
            print("*", end='')
            m += 1
        i -= 1  # Decrementing i for the next line
        print()  # Moving to the next line after completing the inner loops
        """)

    case "decreasing space diamond pattern 97":
        st.code("""
def decreasing_space_diamond_pattern_97(n):
    i = 0  # initializing i value with 0
    while i < n:  # loop for n number of rows
        j = k = m = 0  # initializing j, k, and m with 0
        while j <= i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            j += 1  # incrementing j value
        while k < n - i - 1:  # loop for n-i-1 number of spaces in each row
            print(" ", end=' ')  # printing n-i-1 spaces
            k += 1  # incrementing k value
        while m <= i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            m += 1  # incrementing m value
        i += 1  # incrementing i value
        print()  # an empty print() for the next line
        """)

    case "mirrored diamond 98":
        st.code("""
def mirrored_diamond_98(n):
    i = 0  # initializing i value with 0
    while i < n:  # loop for n number of rows
        j = k = m = 0  # initializing j, k, and m with 0
        while j <= i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            j += 1  # incrementing j value
        while k < n - i - 1:  # loop for n-i-1 number of spaces in each row
            print(" ", end=' ')  # printing n-i-1 spaces
            k += 1  # incrementing k value
        while m <= i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            m += 1  # incrementing m value
        i += 1  # incrementing i value
        print()  # an empty print() for the next line

    i = n - 1  # initializing i value with n-1
    while i > 0:  # loop for n-1 number of rows
        j = k = m = 0
        while j < i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            j += 1  # incrementing j value
        while k <= n - i - 1:  # loop for n-i-1 number of spaces in each row
            print(' ', end=' ')  # printing n-i-1 spaces
            k += 1  # incrementing k value
        while m < i:  # loop for i number of columns
            print("*", end='')  # printing i number of *'s separated by space
            m += 1  # incrementing m value
        i -= 1  # decrementing i value
        print()  # an empty print() for the next line
        """)

    case "symmetrical triangular pat 99":
        st.code("""
def symmetrical_triangular_pat_99(n):
    if n % 2 == 0:  # checking whether the number is even or odd
        n = n - 1  # If the number is odd decrement it by 1
        
    i = 1  # initializing i
    while i < n // 2 + 2:  # loop for n/2+2 rows
        j = m = 0  # initializing j and m with 0
        k = l = 1  # initializing k and l with 1
        while j < n - i - n // 2:  # loop for n-i-n/2 spaces in each row
            print(" ", end=' ')  # printing spaces
            j += 1  # incrementing j value
        while k < i * 2:  # loop for i*2 columns
            print("*", end=' ')  # printing *'s pattern separated by space
            k += 1  # incrementing k value
        while m < 2 * (n - i - n // 2):  # loop for 2*(n-i-n//2) spaces in each row
            print(" ", end=' ')  # printing spaces
            m += 1  # incrementing m value
        while l < i * 2:  # loop for i*2 columns
            print("*", end=' ')  # printing *'s pattern separated by space
            l += 1  # incrementing l value

        i += 1  # incrementing i value
        print()  # an empty print() for the next line
        """)

    case "symmetrical triangular pat 100":
        st.code("""
def symmetrical_triangular_pat_100(n):
    i = 1  # Initializing i for the outer loop
    while i < n + 1:  # Outer loop to print the pattern in ascending order
        j, k = 0, 1  # Initializing variables for the first and second inner loops
        while j < n - i:  # First inner loop to print spaces, aligning to the left
            print(" ", end="")
            j += 1
        while k < i + 1:  # Second inner loop to print left-aligned asterisks
            print("*", end=" ")
            k += 1
        j, k = 0, 1  # Resetting variables for the third and fourth inner loops
        while j < n - i:  # Third inner loop to print spaces, aligning to the left
            print(" ", end=" ")
            j += 1
        while k < i + 1:  # Fourth inner loop to print right-aligned asterisks
            print("*", end=" ")
            k += 1
        print()  # Moving to the next line after completing the inner loops
        i += 1  # Incrementing i for the next line
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





        