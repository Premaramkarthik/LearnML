import streamlit as st
import numpy as np
import math
import itertools
import string
import random
import regex as re


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

options = ['Encryption','Decryption']
selection = st.selectbox('choose the option', options)

match selection:
    case 'Decryption':
        # Streamlit app
        st.title("Decryption in a Streamlit App")

        # Overview section
        st.header("Overview")
        st.write(
            "Decryption is the process of converting ciphertext back into plaintext. "
            "This process is crucial in various applications, including secure communication, "
            "data integrity, and privacy. In this app, users can select different decryption "
            "methods to decode their ciphertext."
        )

        # Key Concepts section
        st.header("Key Concepts of Decryption")

        st.subheader("1. Ciphertext")
        st.write("The encrypted text that needs to be converted back to its original form.")

        st.subheader("2. Plaintext")
        st.write("The original text before encryption.")

        st.subheader("3. Decryption Algorithms")
        st.write("Specific methods used to decrypt the ciphertext. Common algorithms include:")
        st.markdown("""
        - **Substitution Cipher**: Each letter in the plaintext is replaced with a letter from a fixed substitution alphabet.
        - **Rail Fence Cipher**: The text is arranged in a zigzag pattern on rails and then read off row by row.
        - **Route Cipher**: The text is arranged in a grid, and the key determines the order in which the characters are read.
        - **KK Cipher**: Each character is represented by its position in a grid defined by a key.
        """)
        
        class Decryption:
            def __init__(self):
                pass
            
            def kk_cipher_decrypt(self, ciphertext, kk):
                plaintext = ''
                i = 0
                while i < len(ciphertext):
                    if ciphertext[i] != ' ':
                        row = int(ciphertext[i])
                        col = int(ciphertext[i + 1])
                        for char, (r, c) in kk.items():
                            if r == row and c == col:
                                plaintext += char
                                break
                        i += 2
                    else:
                        plaintext += ' '
                        i += 1
                return plaintext.strip()
            
            def substitutionDecrypt(self, ciphertext):
                decrypted_text = ''
                for char in ciphertext:
                    if char in self.decrypt_dict:
                        decrypted_text += self.decrypt_dict[char.lower()]
                    else:
                        decrypted_text += char
                return decrypted_text
            
            def prep_ciphertext(self, ciphertext):
                return "".join(ciphertext.split())

            def split_rails(self, message):
                row_1_len = math.ceil(len(message)/2)
                row1 = (message[:row_1_len])
                row2 = (message[row_1_len:])
                return row1, row2

            def railFenceDecrypt(self, row1, row2):
                plaintext = []
                for r1, r2 in itertools.zip_longest(row1, row2, fillvalue=''): 
                    plaintext.append(r1)
                    plaintext.append(r2)
                return ''.join(plaintext)

            def routeCipherDecrypt(self, r_f_d, p):
                reversed_even_rows_matrix = r_f_d.copy()
                reversed_even_rows_matrix[1::2] = reversed_even_rows_matrix[1::2, ::-1]
                plaintext = ''
                for i in range(1, p + 1):
                    for row in reversed_even_rows_matrix:
                        plaintext += row[-i] + ' '
                return plaintext

        # Create an instance of the Decryption class
        decryption = Decryption()

        # Streamlit app
        st.title("Cipher Decryption App")

        # Select decryption method
        method = st.selectbox("Choose the decryption method", ["KK Cipher", "Substitution Cipher", "Rail Fence Cipher", "Route Cipher"])

        # Input for ciphertext
        ciphertext = st.text_area("Enter the ciphertext")

        if method == "KK Cipher":
            # Example key for demonstration
            kk = {'A': (1, 1), 'B': (1, 2), 'C': (1, 3)}  # Modify this with your actual key
            if st.button("Decrypt with KK Cipher"):
                plaintext = decryption.kk_cipher_decrypt(ciphertext, kk)
                st.success(f"Decrypted text: {plaintext}")

        elif method == "Substitution Cipher":
            # Example decryption dictionary for demonstration
            decryption.decrypt_dict = {'a': 'z', 'b': 'y', 'c': 'x'}  # Modify this with your actual decryption dictionary
            if st.button("Decrypt with Substitution Cipher"):
                plaintext = decryption.substitutionDecrypt(ciphertext)
                st.success(f"Decrypted text: {plaintext}")

        elif method == "Rail Fence Cipher":
            if st.button("Decrypt with Rail Fence Cipher"):
                row1, row2 = decryption.split_rails(ciphertext)
                plaintext = decryption.railFenceDecrypt(row1, row2)
                st.success(f"Decrypted text: {plaintext}")

        elif method == "Route Cipher":
            p = st.number_input("Enter the number of columns", min_value=1, value=1)
            if st.button("Decrypt with Route Cipher"):
                # Assuming r_f_d is a 2D array, adjust it accordingly
                r_f_d = np.array([[char for char in ciphertext]])  # Modify this to reflect the actual matrix
                plaintext = decryption.routeCipherDecrypt(r_f_d, p)
                st.success(f"Decrypted text: {plaintext}")
    case 'Encryption':
        # Streamlit app
        st.title("Encryption in a Streamlit App")

        # Overview section
        st.header("Overview")
        st.write(
            "Encryption is the process of converting plaintext into ciphertext to protect the "
            "information from unauthorized access. It is widely used in secure communications, "
            "data protection, and privacy. In this app, users can select different encryption "
            "methods to encode their plaintext."
        )

        # Key Concepts section
        st.header("Key Concepts of Encryption")

        st.subheader("1. Plaintext")
        st.write("The original text that needs to be encrypted.")

        st.subheader("2. Ciphertext")
        st.write("The encrypted text that is generated from plaintext.")

        st.subheader("3. Encryption Algorithms")
        st.write("Specific methods used to encrypt plaintext. Common algorithms include:")
        st.markdown("""
        - **Substitution Cipher**: Each letter in the plaintext is replaced with a letter from a fixed substitution alphabet.
        - **Rail Fence Cipher**: The text is arranged in a zigzag pattern on rails and then read off row by row.
        - **Route Cipher**: The text is arranged in a grid, and a key determines the order in which the characters are read.
        - **KK Cipher**: Each character is represented by its position in a grid defined by a key.
        """)
                
        import streamlit as st
        import numpy as np
        import math
        import itertools
        import string
        import random

        class Encryption:
            def __init__(self):
                plaintext_alphabet = list(string.ascii_lowercase)
                ciphertext_alphabet = list(string.ascii_lowercase)
                random.shuffle(ciphertext_alphabet)
                self.encrypt_dict = dict(zip(plaintext_alphabet, ciphertext_alphabet))
                self.decrypt_dict = dict(zip(ciphertext_alphabet, plaintext_alphabet))
            
            def capitalize_first_letter(self, sentence):
                words = sentence.split()
                modified_words = [word[0].upper() + word[1:].lower() for word in words]
                return ' '.join(modified_words)

            def route_cipher_encrypt(self, plaintext, key, rows, cols):
                cipherlist = list(plaintext.split())
                key_int = [int(i) for i in key.split()]
                translation_matrix = self.build_matrix(key_int, cipherlist, rows, cols)
                ciphertext = self.encrypt1(translation_matrix)
                return ciphertext
            
            def build_matrix(self, key_int, cipherlist, rows, cols):
                matrix = np.array(cipherlist).reshape(rows, cols)
                transposed_matrix = matrix.T
                adjusted_matrix = np.empty_like(transposed_matrix)
                for i, row in enumerate(transposed_matrix):
                    if key_int[i] < 0:
                        adjusted_matrix[i] = row[::-1]
                    else:
                        adjusted_matrix[i] = row
                return adjusted_matrix

            def encrypt1(self, translation_matrix):
                plaintext = ''
                for row in translation_matrix:
                    for word in row:
                        plaintext += word + ' '
                return plaintext

            def rail_fence_cipher_encrypt(self, plaintext, p):
                message = "".join(plaintext.split())
                rails = self.build_rails(message)
                ciphertext = self.encrypt(rails, p)
                return ciphertext
            
            def build_rails(self, message):
                evens = message[::2]
                odds = message[1::2]
                rails = evens + odds
                return rails

            def encrypt(self, rails, p):
                ciphertext = ' '.join([rails[i:i + p] for i in range(0, len(rails), p)])
                return ciphertext

            def substitution_cipher_encrypt(self, plaintext):
                encrypted_text = ''
                for char in plaintext:
                    if char in self.encrypt_dict:
                        encrypted_text += self.encrypt_dict[char]
                    else:
                        encrypted_text += char
                return encrypted_text

            def kk_cipher_encrypt(self, plaintext, kk):
                ciphertext = ''
                for char in plaintext:
                    if char in kk:
                        ciphertext += str(kk[char][0]) + str(kk[char][1])
                    else:
                        ciphertext += char
                return ciphertext

        # Create an instance of the Encryption class
        encryption = Encryption()

        # Streamlit app
        st.title("Cipher Encryption App")

        # Select encryption method
        method = st.selectbox("Choose the encryption method", ["Route Cipher", "Rail Fence Cipher", "Substitution Cipher", "KK Cipher"])

        # Input for plaintext
        plaintext = st.text_area("Enter the plaintext")

        if method == "Route Cipher":
            key = st.text_input("Enter the key (space-separated integers)")
            rows = st.number_input("Enter the number of rows", min_value=1, value=3)
            cols = st.number_input("Enter the number of columns", min_value=1, value=3)
            if st.button("Encrypt with Route Cipher"):
                encryption = Encryption()
                ciphertext = encryption.route_cipher_encrypt(plaintext, key, rows, cols)
                if ciphertext:
                    st.success(f"Encrypted text: {ciphertext}")

        elif method == "Rail Fence Cipher":
            p = st.number_input("Enter the number of rails", min_value=1, value=2)
            if st.button("Encrypt with Rail Fence Cipher"):
                ciphertext = encryption.rail_fence_cipher_encrypt(plaintext, p)
                st.success(f"Encrypted text: {ciphertext}")

        elif method == "Substitution Cipher":
            if st.button("Encrypt with Substitution Cipher"):
                ciphertext = encryption.substitution_cipher_encrypt(plaintext)
                st.success(f"Encrypted text: {ciphertext}")

        elif method == "KK Cipher":
            kk = {
                'A': (1, 1), 'B': (1, 2), 'C': (1, 3)  # Modify this with your actual key
            }
            if st.button("Encrypt with KK Cipher"):
                ciphertext = encryption.kk_cipher_encrypt(plaintext, kk)
                st.success(f"Encrypted text: {ciphertext}")
