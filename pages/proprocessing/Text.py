import streamlit as st
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import random

import streamlit as st
import re
import random
from nltk.corpus import wordnet
from nltk import download






# Download required NLTK resources
download('punkt')
download('stopwords')
download('wordnet')


#st.set_page_config(layout="wide")
def run():
    # Initialize preprocessors
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    vectorizer = TfidfVectorizer()

    # Streamlit layout
    st.title("Text Preprocessing Techniques")
    st.info("""
            - Text preprocessing is a fundamental process in natural language processing (NLP) that involves cleaning and transforming raw text data into a structured format suitable for analysis and modeling. This step is crucial for various applications, including sentiment analysis, language translation, and information retrieval.
            - Text preprocessing refers to a series of techniques applied to raw text data to refine it and make it more amenable to machine learning algorithms. The goal is to eliminate noise, standardize the text, and extract meaningful features that can be effectively processed. Raw text is often unstructured and diverse, containing inconsistencies, irrelevant information, and various formats that can hinder accurate analysis.
            """)

    col1, col2 = st.columns(2)

    # Text input from user
    with col2:
        st.write("**Text before preprocessing**:")
        text_input = st.text_area("Enter some text to preprocess:", "Streamlit is an open-source app framework for Machine Learning and Data Science.")
        st.session_state.txt = text_input


    # Function to display results for each preprocessing step
    def display_preprocessing(text, step):
        st.subheader(step)
        st.write(text)

    with col1:

        # 1. Tokenization
        
        with st.expander("1. Tokenization", expanded=False):
                st.subheader("Tokenization")
                st.write("""
                Tokenization is the process of breaking down text into smaller pieces, usually words or phrases. 
                This helps models interpret text as discrete elements, making it easier to identify patterns.
                """)
                st.write("""
                **Applications**: Common in NLP tasks to transform raw text into tokenized formats for further processing.
                
                **When to Use**: When breaking down sentences into words or phrases for analysis.
                
                **Limitations**: Does not capture context on its own and may split meaningful phrases.
                """)
                tokens = word_tokenize(text_input)
                # Checkbox to trigger tokenization
                apply_tokenization = st.checkbox("Apply Tokenization")
                if apply_tokenization:
                    tokens = word_tokenize(text_input)
                    st.session_state.str_input = tokens

        
        # 2. Lowercasing
        with st.expander("2. Lowercasing", expanded=False):

                st.subheader("Lowercasing")
                st.write("""
                Lowercasing converts all text to lowercase, standardizing text and preventing models from treating the 
                same word differently based on capitalization, like "Machine" vs "machine".
                """)
                st.write("""
                **Applications**: Reduces vocabulary size in tasks like text classification.
                
                **When to Use**: When case information is irrelevant to analysis.
                
                **Limitations**: May lose important case distinctions, such as in proper nouns or abbreviations.
                """)
                if st.checkbox("Lowercasing"):

                    lowercased_text = text_input.lower()
                    st.session_state.str_input = lowercased_text

        
        # 3. Removing Stop Words
        with st.expander("3. Removing Stop Words", expanded=False):
                st.subheader("Removing Stop Words")
                st.write("""
                Stop Words Removal filters out common words that don't add significant meaning, like 'the', 'is', and 'and',
                helping to focus on relevant words.
                """)
                st.write("""
                **Applications**: Used in sentiment analysis and summarization to focus on meaningful words.

                **When to Use**: When irrelevant words might dilute meaningful information.

                **Limitations**: Some "stop words" may add contextual meaning and should be removed selectively.
                """)

                if st.checkbox("Removing Stop Words"):

                    tokens = word_tokenize(text_input)
                    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
                    st.session_state.str_input = filtered_tokens
            
        
        # 4. Stemming   
        with st.expander("4. Stemming", expanded=False):
                st.subheader("Stemming")
                st.write("""
                Stemming reduces words to their root form by removing prefixes and suffixes, e.g., "running" to "run." 
                This step reduces vocabulary size and captures the core meaning.
                """)
                st.write("""
                **Applications**: Used in search engines and topic modeling to unify word variations.
                
                **When to Use**: Suitable when basic word normalization is needed.
                
                **Limitations**: Can lead to non-standard words and ambiguity.
                    """)
                if st.checkbox("Stemming"):

                    tokens = word_tokenize(text_input)
                    stemmed_tokens = [ps.stem(word) for word in tokens]
                    st.session_state.str_input = stemmed_tokens

        # 5. Lemmatization
        with st.expander("5. Lemmatization", expanded=False):
                st.subheader("Lemmatization")
                st.write("""
                Lemmatization is similar to stemming but returns the base form of a word (its "lemma") with context,
                making the text more interpretable.
                """)
                st.write("""
                **Applications**: Useful in applications where grammatical integrity is essential, like sentiment analysis.
                
                **When to Use**: When context and part of speech are important for retaining meaning.
                
                **Limitations**: Slower than stemming and may still lose some context.
                """)
                if st.checkbox("Lemmatization"):
                    tokens = word_tokenize(text_input)
                    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
                    st.session_state.str_input = lemmatized_tokens

        # 6. Text Vectorization (TF-IDF)
        with st.expander("6. TF-IDF Vectorization", expanded=False):
                st.subheader("TF-IDF Vectorization")
                st.write("""
                TF-IDF (Term Frequency-Inverse Document Frequency) transforms words into numerical values based on their importance
                in a document, emphasizing unique terms.
                """)


                # Set up Streamlit layout
                st.write("""
                ### Term Frequency-Inverse Document Frequency (TF-IDF) Analysis
                This app calculates TF, IDF, and TF-IDF scores for all terms across multiple documents.
                TF-IDF scores highlight the importance of terms within a document relative to other documents in the corpus.
                """)

                # Input: Multiple documents as text areas
                num_docs = st.number_input("How many documents?", min_value=1, max_value=5, value=1)
                documents = [st.text_area(f"Document {i+1}", "") for i in range(num_docs)]

                # Button to calculate TF-IDF scores
                if st.button("Calculate TF-IDF for All Terms"):
                    # Filter out empty documents
                    documents = [doc for doc in documents if doc.strip()]
                    
                    # Recreate doc_names to match the actual number of non-empty documents
                    doc_names = [f"Document {i+1}" for i in range(len(documents))]
                    
                    if documents:
                        # Initialize TfidfVectorizer and calculate TF-IDF matrix
                        vectorizer = TfidfVectorizer()
                        tfidf_matrix = vectorizer.fit_transform(documents)
                        
                        # Get feature names (i.e., terms)
                        terms = vectorizer.get_feature_names_out()
                        
                        # Create DataFrame with TF-IDF scores
                        df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), index=doc_names, columns=terms)
                        
                        st.session_state.str_input = df_tfidf.T
                        # # Display TF-IDF matrix
                        # st.write("### TF-IDF Scores for All Terms")
                        # st.write(df_tfidf)
                        
                        # Explanation of TF-IDF calculation
                        st.write("#### Explanation")
                        st.write("""
                        - **Term Frequency (TF)**: Number of occurrences of a term in a document, divided by the total terms in that document.
                        - **Inverse Document Frequency (IDF)**: Logarithmic measure of how common or rare a term is across the corpus.
                        - **TF-IDF**: Product of TF and IDF, emphasizing terms that are unique to a document but common within it.
                        """)
                    else:
                        st.write("Please enter at least one non-empty document.")



        # Ensure WordNet is downloaded
        download("wordnet")

        # Data Augmentation - Synonym Replacement
        with st.expander("Data Augmentation - Synonym Replacement", expanded=False):
            st.subheader("Data Augmentation - Synonym Replacement")
            st.write("""
            **Data Augmentation** in Natural Language Processing (NLP) is a method used to artificially increase the size and diversity of the dataset.
            It involves creating modified versions of existing text data to improve model performance and generalization.
            
            **Types of Text Data Augmentation Techniques**:
            - **Synonym Replacement**: Replacing certain words with their synonyms to create variations.
            - **Random Insertion**: Adding random synonyms into the text.
            - **Random Deletion**: Randomly deleting words to mimic informal or casual text.
            - **Random Swap**: Swapping the positions of words to introduce structural diversity.
            """)

            st.write("""
            In this example, we will use **synonym replacement** to replace words in the input text with their synonyms from the WordNet lexicon.
            """)

            # Synonym Replacement Function
            def synonym_replacement(text):
                words = text.split()
                augmented_text = []
                
                for word in words:
                    synonyms = wordnet.synsets(word)
                    if synonyms:
                        # Get a list of synonyms and choose one randomly
                        synonym_words = [lemma.name() for syn in synonyms for lemma in syn.lemmas()]
                        if synonym_words:
                            new_word = random.choice(synonym_words)
                            augmented_text.append(new_word)
                        else:
                            augmented_text.append(word)
                    else:
                        augmented_text.append(word)
                        
                return " ".join(augmented_text)

            # # Input and augmentation process
            # text_input = st.text_area("Enter text for synonym replacement:")
            
            # if st.checkbox("Apply Synonym Replacement"):
            #     # Apply synonym replacement and store in session state
            #     st.session_state.str_input = synonym_replacement(text_input)


    with col2:
            # Display tokens if present in session state
            if 'str_input' in st.session_state:
                st.write("**Text after preprocessing**:")
                st.write(st.session_state.str_input)
