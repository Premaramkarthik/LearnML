# import streamlit as st
# import re
# import pickle
# import numpy as np
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer, WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# import gensim.downloader as api
# from gensim.models import Word2Vec
# from numpy import dot
# from numpy.linalg import norm
# import matplotlib.pyplot as plt
# from gensim.models import FastText
# from sklearn.cluster import KMeans
# from gensim.utils import simple_preprocess
# from gensim.models import Word2Vec
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE
# from importlib import import_module




# def run():
#     #from glove import Corpus, Glove # type: ignore

#     #st.set_page_config(layout="wide")
#     # def run():
#     nltk.download('punkt_tab')
#     # Initialize stopwords and stemmer
#     stop_words = set(stopwords.words('english'))
#     stemmer = PorterStemmer()
#     lemmatizer = WordNetLemmatizer()
#     st.title("Text Vectorization Techniques")
#     st.info("""Vectorization of text data in machine learning is the process of converting text into numerical format so that algorithms can process it. Since machine learning models work with numbers, text data must be transformed into a format they can understand. This process is essential for NLP (Natural Language Processing) tasks like text classification, sentiment analysis, topic modeling, and more. Here are some common methods for vectorizing text data:""")

#     col1, col2 = st.columns(2)


#     ##main_selection = st.selectbox(
#         # "",
#         # ["Overview", "Explicit & Implicit", "Types of ML", "Learning Problem", "Occams Razor"]
#     with col1:

#         # Bag of Words
#         with st.expander("1. Bag of Words", expanded=True):
#             # App Title
#             st.title("Understanding the Bag of Words (BoW) Method")
#             st.write("""
#             The Bag of Words (BoW) method is a straightforward way to represent text data. Imagine treating each document as a collection of words—like a bag filled with different items—without worrying about grammar or the order in which the words appear. This approach focuses solely on the presence or frequency of words.
#             """)

#             # How It Works
#             st.header("How It Works")
#             st.subheader("1. Creating a Vocabulary")
#             st.write("""
#             First, we compile a list of all unique words found across the entire dataset. This list is known as the vocabulary.
#             """)

#             st.subheader("2. Vector Representation")
#             st.write("""
#             Each document is then transformed into a vector. In this vector, each position corresponds to a word from the vocabulary, and the value at that position indicates either how many times that word appears in the document (word count) or whether it appears at all (binary value).
#             """)

#             # When to Use BoW
#             st.header("When to Use BoW")
#             st.write("""
#             - **Document Similarity**: BoW is great for assessing how similar different documents are based on their word content.
#             - **Basic Classification**: If you need to classify documents without worrying about the order of words, BoW is a solid choice.
#             - **Smaller Datasets**: It works particularly well with smaller datasets or when you want to keep things simple from a computational standpoint.
#             """)

#             # Why Choose Bag of Words?
#             st.header("Why Choose Bag of Words?")
#             st.write("""
#             - **Simplicity**: The method is easy to understand and implement.
#             - **Effective for Basic Tasks**: It performs well in straightforward text classification tasks, such as identifying spam emails.
#             """)

#             # Limitations
#             st.header("Limitations")
#             st.write("""
#             - **Loss of Context**: One major drawback is that BoW ignores the order and context of words, which can lead to misunderstandings in meaning.
#             - **High Dimensionality**: With large vocabularies, the resulting vectors can become very sparse, making analysis more challenging.
#             - **Synonymy and Polysemy Issues**: BoW struggles with synonyms (different words that mean the same thing) and polysemy (the same word having multiple meanings), which can complicate interpretation.
#             """)

#             # Applications
#             st.header("Applications")
#             st.write("""
#             The Bag of Words method is commonly used in:
#             - **Document Classification**: Sorting documents into predefined categories.
#             - **Spam Filtering**: Identifying unwanted emails based on their content.
#             - **Basic Text Clustering**: Grouping similar documents together where context isn’t critical.
#             """)
            
#         with st.expander("2. Tf-idf", expanded=False): 

#             # Title of the page
#             st.title("Understanding TF-IDF (Term Frequency-Inverse Document Frequency)")
#             st.write(
#                 """
#                 TF-IDF, which stands for Term Frequency-Inverse Document Frequency, is a powerful technique used in text analysis to evaluate 
#                 the importance of words within a document relative to a larger collection of documents, known as a corpus. This method enhances 
#                 the basic Bag of Words approach by assigning weights to words based on their significance, allowing us to distinguish between 
#                 common words and those that carry more informative value. Essentially, it helps in highlighting unique terms that are more relevant 
#                 for understanding the content.
#                 """
#             )

#             # How It Works section
#             st.markdown("<h1 style='font-size:24px;'>How It Works</h1>", unsafe_allow_html=True)
#             st.markdown("<h2 style='font-size:18px;'>1. Term Frequency (TF)</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 This metric measures how often a word appears in a specific document. The more frequently a word appears, 
#                 the higher its term frequency.
#                 """
#             )

#             #st.subheader("2. Inverse Document Frequency (IDF)")
#             st.markdown("<h2 style='font-size:18px;'>2. Inverse Document Frequency (IDF)</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 This component assesses the importance of a word by considering how common or rare it is across all documents. 
#                 Words that appear in many documents receive a lower IDF score, while those found in fewer documents get a higher score.
#                 """
#             )

#             #st.subheader("3. Calculating TF-IDF")
#             st.markdown("<h2 style='font-size:18px;'>3. Calculating TF-IDF </h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 The TF-IDF score for each word in a document is calculated by multiplying its term frequency by its inverse document frequency:
#                 """
#             )
#             st.latex(r"\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)")
#             st.write("where \( t \) is the term and \( d \) is the document.")

#             # When to Use TF-IDF section
#             #st.header("When to Use TF-IDF")
#             st.markdown("<h2 style='font-size:24px;'>When to Use TF-IDF</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 - **Distinguishing Relevant Words**: TF-IDF is particularly useful when it’s important to differentiate significant words 
#                 from common ones, such as in information retrieval or keyword identification.
#                 - **Medium to Large Datasets**: It works well for datasets where understanding the unique importance of terms 
#                 can enhance model performance.
#                 """
#             )

#             # Why Choose TF-IDF section
#             #st.header("Why Choose TF-IDF?")
#             st.markdown("<h2 style='font-size:24px;'>Why Choose TF-IDF?</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 - **Reducing Common Word Influence**: By down-weighting frequently used words (like "the," "is," and "and"), TF-IDF helps 
#                 improve the relevance of analysis, making it effective for tasks like document categorization.
#                 - **Enhancement Over BoW**: It builds on the Bag of Words model by focusing on unique terms that are specific to individual 
#                 documents, thus providing richer insights.
#                 """
#             )

#             # Limitations section
#             #st.header("Limitations")
#             st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 - **Sparse Representation**: Like BoW, TF-IDF can still result in high-dimensional and sparse representations, especially 
#                 with large vocabularies.
#                 - **Ignoring Word Order and Context**: It does not capture the order of words or their contextual relationships, which can 
#                 limit its effectiveness in understanding nuanced meanings.
#                 - **Not Ideal for Semantic Tasks**: For applications where the semantic meaning of phrases is crucial, TF-IDF may fall short.
#                 """
#             )

#             # Applications section
#             #st.header("Applications")
#             st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

#             st.write(
#                 """
#                 TF-IDF finds diverse applications across various fields:
#                 - **Search Engines and Information Retrieval**: It helps rank search results based on how relevant documents are to user 
#                 queries by prioritizing those with higher TF-IDF scores.
#                 - **Keyword Extraction**: Identifying key terms within documents based on their significance helps summarize content effectively.
#                 - **Text Classification**: In machine learning, TF-IDF transforms text data into numerical features that models can process, 
#                 improving classification accuracy.
#                 - **Sentiment Analysis**: By focusing on significant terms, TF-IDF aids in discerning sentiments expressed within texts.
#                 """
#             )

#         with st.expander("3. Word 2 Vec Embedding", expanded= False):
#             # Title
#             st.title("Overview of Word2Vec Embeddings")

#             st.write("""
#             Word2Vec is a powerful technique used in natural language processing (NLP) to learn word embeddings, 
#             which are dense vector representations of words. This model captures semantic relationships 
#             by analyzing the context in which words appear, positioning semantically similar words close 
#             together in a continuous vector space.
#             """)

#             #st.header("How It Works")
#             st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

#             st.write("""
#             Word2Vec employs two primary architectures to generate these embeddings:
#             - **Skip-Gram:** This model predicts surrounding context words based on a given target word. 
#             By maximizing the probability of context words appearing near the target, Skip-Gram effectively captures 
#             various meanings of words depending on their different contexts.
#             - **Continuous Bag of Words (CBOW):** In contrast, CBOW predicts a target word from a set of surrounding 
#             context words. It emphasizes local context relationships by taking multiple context words and determining 
#             the most probable target word.
#             """)

#             #st.header("When to Use Word2Vec")
#             st.markdown("<h2 style='font-size:24px;'>When to Use Word2Vec</h2>", unsafe_allow_html=True)

#             st.write("""
#             Word2Vec is particularly beneficial for tasks that require a nuanced understanding of local word contexts, such as:
#             - **Conversational AI:** Enhancing chatbots and virtual assistants by improving their understanding of user input.
#             - **Text Classification:** Enabling more accurate classification of documents based on their content.
#             It is especially effective for smaller to medium-sized datasets where computational efficiency and speed are important.
#             """)

#             #st.header("Why Choose Word2Vec?")
#             st.markdown("<h2 style='font-size:24px;'>Why Choose Word2Vec?</h2>", unsafe_allow_html=True)

#             st.write("""
#             - **High-Quality Embeddings:** Word2Vec produces embeddings that are efficient to train and can effectively represent semantic similarities.
#             - **Vector Arithmetic:** It allows for interesting calculations through vector arithmetic, such as solving analogies 
#             (e.g., "king" - "man" + "woman" = "queen").
#             - **Real-Time Training:** The model supports real-time updates, meaning embeddings can be continually refined as new data becomes available.
#             """)

#             #st.header("Limitations")
#             st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

#             st.write("""
#             Despite its strengths, Word2Vec has some limitations:
#             - **Static Embeddings:** The embeddings do not capture variations in word meanings based on context, 
#             which can be problematic for polysemous words (e.g., "bank" can refer to a financial institution or the side of a river).
#             - **Resource Intensive:** It requires significant computational resources and a large dataset to generate high-quality embeddings.
#             - **Sensitivity to Parameters:** The quality of the embeddings can be sensitive to training parameters like window size and vector dimensionality.
#             """)

#             #st.header("Applications")
#             st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

#             st.write("""
#             Word2Vec has numerous applications in NLP, including:
#             - **Sentiment Analysis:** Understanding opinions expressed in text.
#             - **Machine Translation:** Improving the accuracy of translating text from one language to another.
#             - **Text Summarization:** Condensing information while preserving key points.
#             - **Information Retrieval:** Enhancing search engines by improving how they understand queries and documents.
#             - **Analogy Detection:** Solving analogy tasks by leveraging the mathematical properties of word vectors.
#             """)
        
#         with st.expander("4. Glove Embedding",expanded = False):

#             # Title
#             st.title("Understanding GloVe Embeddings")
#             st.write("""
#             GloVe, or Global Vectors for Word Representation, is a method for learning word embeddings 
#             that focuses on capturing the global statistical information of words in a corpus. 
#             By constructing a co-occurrence matrix that records how often words appear together, 
#             GloVe aims to understand the relationships between words and represents them as 
#             dense vectors in a continuous vector space.
#             """)

#             #st.header("How It Works")
#             st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

#             st.write("""
#             GloVe generates word embeddings through a series of steps:
#             - **Co-occurrence Matrix Creation:** The process begins by creating a global co-occurrence 
#             matrix, which counts how frequently each word appears in the context of every other word 
#             across a large corpus. This matrix serves as the foundation for understanding word relationships.
#             - **Cost Function Formulation:** GloVe formulates a cost function that relates the dot product 
#             of word vectors to the logarithm of their co-occurrence probabilities. The goal is to minimize 
#             the difference between these two values, ensuring that the embeddings reflect actual word usage patterns.
#             - **Matrix Factorization:** Finally, by factorizing the co-occurrence matrix, GloVe generates 
#             dense word vectors that effectively capture semantic relationships across the entire corpus.
#             """)

#             #st.header("When to Use GloVe")
#             st.markdown("<h2 style='font-size:24px;'>When to Use GloVe</h2>", unsafe_allow_html=True)

#             st.write("""
#             GloVe is particularly effective for:
#             - **Large Datasets:** It excels in scenarios where capturing global statistical relationships 
#             significantly enhances performance.
#             - **Understanding Word Meanings:** GloVe is suitable for tasks requiring a comprehensive 
#             understanding of word meanings, especially when words have multiple meanings depending on broader context.
#             """)

#             #st.header("Why Choose GloVe?")
#             st.markdown("<h2 style='font-size:24px;'>Why Choose GloVe?</h2>", unsafe_allow_html=True)

#             st.write("""
#             - **Global Context:** GloVe embeddings are based on global co-occurrence statistics, making them 
#             effective for capturing semantic relationships across diverse contexts.
#             - **Generalization:** The embeddings often generalize well to various tasks due to their 
#             incorporation of broader word relationships.
#             - **Intuitive Interpretability:** Similar to Word2Vec, GloVe allows for intuitive interpretations 
#             of word relationships through vector operations.
#             """)

#             #st.header("Limitations")
#             st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

#             st.write("""
#             Despite its strengths, GloVe has some limitations:
#             - **Training Speed:** The need for a large co-occurrence matrix can make GloVe slower to train, 
#             particularly with very large vocabularies.
#             - **Pre-trained Embeddings:** Like Word2Vec, pre-trained embeddings may not fit specialized 
#             vocabularies or domains.
#             - **Lack of Real-Time Updates:** GloVe is not designed for continual learning, making it less effective 
#             in scenarios requiring real-time updates.
#             """)

#             #st.header("Applications")
#             st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

#             st.write("""
#             GloVe embeddings are widely used in various applications, including:
#             - **Text Classification:** Enhancing the performance of classifiers by providing rich semantic features.
#             - **Sentiment Analysis:** Understanding the sentiment of text by analyzing word relationships.
#             - **Machine Translation:** Improving translation quality by capturing contextual meanings.
#             - **Information Retrieval:** Enhancing search engines by better understanding user queries.
#             """)

#         with st.expander("5. Fast Text", expanded = False):

#             # Title
#             st.title("Understanding FastText Embeddings")

#             # Introduction
#             st.write("""
#             FastText is a sophisticated method for generating word embeddings, developed by Facebook's AI Research (FAIR). Unlike traditional models that treat words as indivisible units, FastText utilizes subword information, allowing it to analyze the internal structure of words. This capability is particularly beneficial for languages with complex morphology and for handling rare or out-of-vocabulary words.
#             """)

#             # How It Works
#             st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

#             st.write("""
#             1. **Subword Information**:  
#             FastText decomposes words into smaller components known as n-grams, which are sequences of characters. For example, the word "embedding" can be represented using 3-grams like "emb", "bme", "med", "edd", "ddi", and "ing". This approach enables FastText to capture morphological patterns and learn embeddings for similar words, even if they were not present during training.

#             2. **Training Process**:  
#             FastText employs training techniques similar to Word2Vec, using either the **Skip-gram** or **Continuous Bag of Words (CBOW)** models:
#             - **Skip-gram**: Predicts context words given a target word (e.g., predicting "feline" and "pet" from "cat").
#             - **CBOW**: Predicts the target word from a set of context words (e.g., predicting "cat" from "feline" and "pet").

#             3. **Embedding Calculation**:  
#             The final embedding for a word is computed as the sum of the embeddings of its constituent n-grams. This allows FastText to generate embeddings for out-of-vocabulary words based on their character-level representations. For instance, the embedding for "unkown" can be derived from its n-grams like "unk", "kno", "now", and "own".
#             """)

#             # When to Use FastText
#             st.markdown("<h2 style='font-size:24px;'>When to Use FastText</h2>", unsafe_allow_html=True)

#             st.write("""
#             FastText is particularly advantageous in scenarios involving:
#             - **Morphologically Rich Languages**: It effectively captures the meanings of words based on their morphological structure.
#             - **Handling Rare Words**: FastText generates embeddings for rare terms that may not be included in the training corpus, making it useful in specialized domains.
#             """)

#             # Why Choose FastText?
#             st.markdown("<h2 style='font-size:24px;'>Why Choose FastText?</h2>", unsafe_allow_html=True)

#             st.write("""
#             - **Character-Level Information**: By incorporating subword information, FastText produces robust embeddings that reflect semantic nuances, enhancing performance in various natural language processing (NLP) tasks.
#             - **Robustness**: The embeddings can accommodate variations such as misspellings or different word forms, making them resilient in noisy data environments.
#             - **Improved Generalization**: FastText embeddings generalize better across tasks and domains due to their understanding of word structure and semantics.
#             """)

#             # Limitations
#             st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

#             st.write("""
#             Despite its strengths, FastText has some limitations:
#             - **Memory Usage**: Storing embeddings for both words and n-grams can increase memory requirements.
#             - **Training Time**: The model may require longer training times compared to simpler embedding models due to its complexity.
#             - **Interpretability**: The resulting embeddings may be less intuitive compared to traditional embeddings since they incorporate multiple n-grams rather than whole words.
#             """)

#             # Applications
#             st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

#             st.write("""
#             FastText embeddings are widely used in various NLP tasks, including:
#             - **Text Classification**: Enhancing classifiers' performance in sentiment analysis, topic detection, and spam detection by providing rich semantic features.
#             - **Named Entity Recognition (NER)**: Improving recognition rates for rare entities by leveraging its character-level approach.
#             - **Sentiment Analysis**: Effectively analyzing sentiment by capturing nuances in language relationships.
#             - **Machine Translation**: Enhancing translation quality by better managing morphologically complex words.
#             """)

#             # Conclusion
#             st.write("""
#             FastText represents a significant advancement in word embedding techniques, enabling more nuanced natural language processing capabilities. Its subword approach not only improves performance on traditional NLP tasks but also opens new avenues for understanding and generating language.
#             """)

        

#     with col2:



#         def preprocess_text(text):
#             # 1. Lowercasing
#             text = text.lower()
            
#             # 2. Removing Punctuation
#             text = re.sub(r'[^\w\s]', '', text)
            
#             # 3. Removing Stop Words 
#             words = word_tokenize(text)

#             # 4. Remove stopwords and apply either stemming or lemmatization
#             if use_stemmer:
#                 processed_words = [stemmer.stem(word) for word in words if word not in stop_words]
#             else:
#                 processed_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
            
#             # Join the processed words back into a single string
#             return ' '.join(processed_words)

#         st.subheader("**Sample text from e - books for understanding Vectorization Methods**")
#         selection_1 = st.radio("Select one text data :", options = ["Harry potter", "Narnia"], key='book_selector')

#         if selection_1 == "Harry potter":
#             text_input = """
#                                 Harry was bleeding. Clutching his right hand in his left and sweating under his breath, he shouldered open his bedroom door. 
#                                 There was a crunch of breaking china. He had trodden on a cup of cold tea that had been sitting on the floor outside his bedroom door.
                                
#                                 “What the—?” He looked around, the landing of number four, Privet Drive, was deserted. 
#                                 Possibly the cup of tea was Dudley’s idea of a clever booby trap. Keeping his bleeding hand elevated, 
#                                 Harry scraped the fragments of cup together with the other hand and threw them into the already crammed bin just visible inside his bedroom door.
#                                 Then he tramped across to the bathroom to run his finger under the tap."""
                                


#         elif selection_1 == "Narnia":
#             text_input = """
#                                 WHAT an extraordinary place!” cried Lucy. “All those stone animals — and people too! It’s — it’s like a museum.” 

#                                 “Hush,” said Susan, “Aslan’s doing something He was indeed. He had bounded up to the stone lion and breathed on him. 
                                
#                                 Then without waiting a moment he whisked round — almost as if he had been a cat chasing its tail -and breathed also on the stone dwarf, which (as you remember) was standing a few feet from the lion with his back to it. 
                                
#                                 Then he pounced on a tall stone dryad which stood beyond the dwarf, turned rapidly aside to deal with a stone rabbit on his right, and rushed on to two centaurs. 
                                
#                                 But at that moment Lucy said, “Oh, Susan! Look! Look at the lion.” I expect you’ve seen someone put a lighted match to a bit of newspaper which is propped up in a grate against an unlit fire. And for a second nothing seems to have happened; and then you notice a tiny streak of flame creeping along the edge of the newspaper. It was like that now. 
#                                                 """

        
        
#         # Number of documents selector
#         num_docs = st.slider("Select the number of documents to split into:", 1, 5, 1)

#         # Split the text_input into the selected number of parts
#         text_split = text_input.strip().split()
#         split_length = len(text_split) // num_docs
#         splitted_docs = [" ".join(text_split[i*split_length:(i+1)*split_length]) for i in range(num_docs)]

#         # Adjust for any remaining words in the final part
#         if len(text_split) % num_docs != 0:
#             splitted_docs[-1] += " " + " ".join(text_split[num_docs * split_length:])

#         st.write(splitted_docs)

#         # Create an option to choose between stemming and lemmatization
#         method = st.selectbox("Choose a normalization technique:", ["Stemming", "Lemmatization"])

#         # Determine which method to use based on user selection
#         use_stemmer = method == "Stemming"

#         # Preprocess each document
#         processed_docs = [preprocess_text(doc) for doc in splitted_docs]



#     # ------------------------------------------------------------------------------------------

#         if splitted_docs:
#             # Preprocess each text entry
#             processed_texts = list(filter(lambda x: x != "", processed_docs))

#         # Join the processed texts into a single string with commas
#         formatted_text = ' '.join(processed_texts).replace(" "," , ")

#         # Display the formatted text
#         st.write(f"**Processed Texts**:")
#         st.write(formatted_text)
        

#     # -----------------------------------------------------------------------------------------------

#         # Define the keywords
#         keywords = ["Bag of Words", "Tf-idf", "Word2Vec", "Glove", "Fast Text"]

#         # Create a dropdown for selecting a keyword
#         selected_keyword = st.selectbox("Select a Method", options=keywords)

#         # Display the selected keyword
#         if selected_keyword == "Bag of Words":
#             # N-gram selection
#             ngram_choice = st.radio("Choose N-gram type:", ["Unigram", "Bigram"], key='unigram_selector')

#             # Set n-gram range based on selection
#             if ngram_choice == "Unigram":
#                 ngram_range = (1, 1)
#             else:
#                 ngram_range = (1, 2)  # Unigrams + Bigrams for more detail

#             # Convert preprocessed text to Bag of Words representation
#             vectorizer = CountVectorizer(ngram_range=ngram_range)
#             bow_matrix = vectorizer.fit_transform(processed_docs)  # Input as list for consistency

#             # Convert to DataFrame for display
#             bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())
            
#             st.subheader("Bag of Words Matrix")
#             st.write(bow_df)

#     # -------------------------------------------------------------------------------------------------------------------

#         elif selected_keyword == "Tf-idf":

#             if processed_docs:  # Check if the input is not empty
#                 # Split the input into a list of documents
#                 documents = processed_docs

#                 # N-gram selection
#                 ngram_choice = st.radio("Choose N-gram type:", ["Unigram", "Bigram"], key='bigram')

#                 # Set n-gram range based on selection
#                 if ngram_choice == "Unigram":
#                     ngram_range = (1, 1)
#                 else:
#                     ngram_range = (1, 2)  # Unigrams + Bigrams for more detail            

#                 # Create a TfidfVectorizer instance
#                 vectorizer = TfidfVectorizer(ngram_range=ngram_range)

#                 # Fit and transform the documents to create the TF-IDF matrix
#                 tfidf_matrix = vectorizer.fit_transform(documents)

#                 # Convert the TF-IDF matrix to a DataFrame for better visualization
#                 tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

#                 # Display the TF-IDF DataFrame
#                 st.subheader("TF-IDF Matrix:")
#                 st.dataframe(tfidf_df)
#             else:
#                 st.warning("Please enter at least one document.")
                
#     # ---------------------------------------------------------------------------------------------------------------

#         elif selected_keyword == "Word2Vec":
                
#             sentences = [sentence.split() for sentence in processed_docs if sentence]

#             # Train Word2Vec model
#             st.subheader("Training Word2Vec Model...")
#             model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
#             st.success("Word2Vec model trained!")

#             # Get vocabulary and vectors
#             words = list(model.wv.index_to_key)
#             word_vectors = model.wv[words]

#             # Create a DataFrame for the transformed word vectors
#             df = pd.DataFrame(word_vectors, index=words, columns=[f'Component {i+1}' for i in range(word_vectors.shape[1])])

#             # Display the transformed DataFrame
#             st.subheader("Word2Vec Transformed DataFrame")
#             st.write(df)

#             # Explanation of the analogy example
#             st.subheader("Understanding Word Relationships with Analogy")
#             st.write('''
#                 An important feature of Word2Vec is its ability to perform vector arithmetic on words. 
#                 For example, the analogy "king" - "man" + "woman" = "queen" demonstrates how Word2Vec 
#                 captures gender relationships. The mathematical representation can be visualized as follows:
#                 - Each word is represented as a vector in a high-dimensional space.
#                 - The operation involves subtracting the vector for "man" from "king" and then adding the vector for "woman".
#                 - The resulting vector points to the location of "queen" in this space, illustrating the relationship.
#             ''')
#             # Train Word2Vec model
#             # Sample sentences; replace with your processed_docs
#             processed_docs = [
#                 "king man woman queen",
#                 "the king is a powerful figure",
#                 "the queen is wise and fair",
#                 "a man must protect his family",
#                 "a woman can be strong and independent"
#             ]

#             # Prepare the data as a list of lists of words
#             sentences = [sentence.split() for sentence in processed_docs]

#             # Train Word2Vec model
#             st.subheader("Training Word2Vec Model...")
#             model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
#             st.success("Word2Vec model trained!")


#             # Define the words for the analogy
#             analogy_words = ["king", "man", "woman", "queen"]

#             # Check vocabulary
#             vocab = model.wv.index_to_key
#             st.write("Vocabulary:", vocab)

#             # Define the words for the analogy
#             missing_words = [word for word in analogy_words if word in vocab]

#             if missing_words:
#                 # Get vectors for analogy words
#                 vectors = [model.wv[word] for word in analogy_words]

#                 # Apply PCA for 2D visualization
#                 pca = PCA(n_components=2)
#                 reduced_vectors = pca.fit_transform(vectors)

#                 # Create a scatter plot of the vectors
#                 plt.figure(figsize=(10, 6))
#                 plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1])

#                 # Annotate the points with the words
#                 for i, word in enumerate(analogy_words):
#                     plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]), fontsize=12)

#                 plt.title("Word2Vec Analogy Example Visualization")
#                 plt.xlabel("PCA Component 1")
#                 plt.ylabel("PCA Component 2")
#                 plt.grid()
#                 st.pyplot(plt)
                
#             else:
#                 st.warning(f"Missing words from vocabulary: {missing_words}")

#     # ------------------------------------------------------------------------------------------------------
                
#         elif selected_keyword == "Glove":

 

#             # Load GloVe model
#             @st.cache
#             def load_glove_model():
#                 with open(r'pages\proprocessing\glove_model.pkl', 'rb') as f:
#                     return pickle.load(f)

#             glove_model = load_glove_model()

#             # Function to tokenize input text
#             def tokenize(text):
#                 return text.lower().split()

#             # Function to retrieve word vectors
#             def get_vectors(tokens, model):
#                 return [model[token] for token in tokens if token in model]

#             # Function to calculate cosine similarity
#             def cosine_similarity(vec_a, vec_b):
#                 return dot(vec_a, vec_b) / (norm(vec_a) * norm(vec_b))

#             # Function for vector arithmetic
#             def vector_arithmetic(vec_a, vec_b, vec_c):
#                 return vec_a - vec_b + vec_c

#             # Function to visualize words
#             def visualize_words(vectors, words):
#                 pca = PCA(n_components=2)
#                 reduced = pca.fit_transform(vectors)

#                 plt.figure(figsize=(10, 10))
#                 for i, word in enumerate(words):
#                     plt.scatter(reduced[i, 0], reduced[i, 1])
#                     plt.annotate(word, (reduced[i, 0], reduced[i, 1]), fontsize=12)
#                 plt.title("Word Embedding Visualization")
#                 plt.grid()
#                 st.pyplot(plt)  # Display the plot in Streamlit

#             # Streamlit app layout
#             st.title("GloVe Word Embeddings Demo")

#             # User input for sentence
#             user_input = st.text_input("Enter a sentence:", "Your example text goes here.")
#             tokens = tokenize(user_input)
#             vectors = get_vectors(tokens, glove_model)

#             if vectors:
#                 # Convert tokens and their first five dimensions of vectors into a DataFrame
#                 df = pd.DataFrame([vector[:5] for vector in vectors], index=tokens, columns=["Dimension 1", "Dimension 2", "Dimension 3", "Dimension 4", "Dimension 5"])
                
#                 st.write("Tokens and their vectors (first five dimensions):")
#                 st.dataframe(df)  # Display the DataFrame in Streamlit

#                 # Calculate similarity between the first two tokens (if available)
#                 if len(vectors) >= 2:
#                     similarity = cosine_similarity(vectors[0], vectors[1])
#                     st.write(f"Cosine Similarity between '{tokens[0]}' and '{tokens[1]}': {similarity:.4f}")

#                 # Example of vector arithmetic (king - man + woman = queen)
#                 if all(word in glove_model for word in ['king', 'man', 'woman']):
#                     result_vector = vector_arithmetic(glove_model['king'], glove_model['man'], glove_model['woman'])
#                     st.write("Result of 'king - man + woman':", result_vector[:5])  # Show only the first five dimensions

#                 # Visualization
#                 if len(vectors) > 0:
#                     st.subheader("Word Visualization")
#                     visualize_words(vectors, tokens)
#             else:
#                 st.write("No valid words found in the input.")
#     # ---------------------------------------------------------------------------------------------------------------

#         elif selected_keyword == "Fast Text":


            

#             ft_model = FastText.load_fasttext_format(r'pages\proprocessing\Harry_Potter_SkipGram.bin')


#             lemmatizer = WordNetLemmatizer()
#             stop_words = set(stopwords.words('english'))

#             # Preprocess function for multi-word queries
#             def preprocess_text(text):
#                 text = text.lower()
#                 text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
#                 tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
#                 return tokens

#             # Calculate the average vector for the entire query
#             def get_avg_vector(words, model):
#                 vectors = [model.wv[word] for word in words if word in model.wv]
#                 if vectors:
#                     return np.mean(vectors, axis=0)
#                 else:
#                     return np.zeros(model.vector_size)
            
            
#             # App layout
#             st.title("Performing FastText")

#             # Choose a task
#             task = st.radio("Choose an NLP Task", ["Text Classification", "Named Entity Recognition", "Semantic Search", "Spell Correction", "Topic Modeling"], key='nlp_task')

#             # Text input area
#             text_input = st.text_area("Enter text (one document per line):")

#             # Train FastText model
#             def train_fasttext_model(processed_docs):
#                 processed_corpus = [simple_preprocess(doc) for doc in processed_docs]
#                 model = FastText(sentences=processed_corpus, vector_size=50, window=3, min_count=1, sg=1, epochs=10)
#                 return model
            

#             import spacy
#             # import streamlit as st

#             # Load spaCy model for NER
#             nlp = spacy.load("en_core_web_sm")

#             if text_input:
#                 processed_docs = text_input.splitlines()
#                 fasttext_model = train_fasttext_model(processed_docs)

#             # Text Classification
#             if task == "Text Classification":
#                 st.header("Text Classification with FastText")
#                             # Split input into documents

#                 if st.button("Classify Text"):
#                     doc_vector = np.mean([fasttext_model.wv[word] for word in processed_docs[0].split() if word in fasttext_model.wv], axis=0)
#                     st.write(f"Text Vector: {doc_vector[:10]}")  # Show first 10 elements for simplicity




#             # Named Entity Recognition with FastText
#             elif task == "Named Entity Recognition":
#                 st.header("Named Entity Recognition with FastText")
                
#                 # Button to trigger NER
#                 if st.button("Identify Entities"):
#                     # Use spaCy to process the first document
#                     doc = nlp(processed_docs[0])
                    
#                     # Loop through each identified entity
#                     for ent in doc.ents:
#                         # Display the entity text and its label
#                         st.write(f"Entity: {ent.text}, Label: {ent.label_}")
                        
#                         # Retrieve FastText vector if entity text is in the FastText vocabulary
#                         if ent.text in fasttext_model.wv:  # Replace `.wv` if you’re using a newer FastText version
#                             vector = fasttext_model.wv[ent.text]
#                             st.write(f"FastText Vector for '{ent.text}': {vector[:10]}")  # Show first 10 elements
#                         else:
#                             st.write(f"No FastText vector available for '{ent.text}'")






#             # Streamlit Semantic Search Code
#             elif task == "Semantic Search":
#                 st.header("Semantic Search with FastText")
#                 query = st.text_input("Enter search query:")
#                 if st.button("Find Similar Words"):
#                     # Preprocess the input query and get the average vector
#                     processed_query = preprocess_text(query)
#                     query_vector = get_avg_vector(processed_query, ft_model)
                    
#                     # Find similar words using the averaged vector
#                     similar_words = ft_model.wv.similar_by_vector(query_vector, topn=10)
                    
#                     # Display the similar words with similarity scores
#                     st.write("Words similar to your query:")
#                     for word, similarity in similar_words:
#                         st.write(f"Word: {word}, Similarity: {similarity:.4f}")



# run()


import streamlit as st
import re
import pickle
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec, FastText
from numpy import dot
from numpy.linalg import norm
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import spacy

def run():
    # Download necessary NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # Initialize stopwords and stemmer/lemmatizer
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    st.title("Text Vectorization Techniques")
    st.info("""
    Vectorization of text data in machine learning is the process of converting text into numerical format so that algorithms can process it. Since machine learning models work with numbers, text data must be transformed into a format they can understand. This process is essential for NLP (Natural Language Processing) tasks like text classification, sentiment analysis, topic modeling, and more. Here are some common methods for vectorizing text data:
    """)

    col1, col2 = st.columns(2)

    with col1:
        # Bag of Words
        with st.expander("1. Bag of Words", expanded=True):
            # App Title
            st.header("Understanding the Bag of Words (BoW) Method")
            st.write("""
            The Bag of Words (BoW) method is a straightforward way to represent text data. Imagine treating each document as a collection of words—like a bag filled with different items—without worrying about grammar or the order in which the words appear. This approach focuses solely on the presence or frequency of words.
            """)

            # How It Works
            st.subheader("How It Works")
            st.markdown("**1. Creating a Vocabulary**")
            st.write("""
            First, we compile a list of all unique words found across the entire dataset. This list is known as the vocabulary.
            """)

            st.markdown("**2. Vector Representation**")
            st.write("""
            Each document is then transformed into a vector. In this vector, each position corresponds to a word from the vocabulary, and the value at that position indicates either how many times that word appears in the document (word count) or whether it appears at all (binary value).
            """)

            # When to Use BoW
            st.subheader("When to Use BoW")
            st.write("""
            - **Document Similarity**: BoW is great for assessing how similar different documents are based on their word content.
            - **Basic Classification**: If you need to classify documents without worrying about the order of words, BoW is a solid choice.
            - **Smaller Datasets**: It works particularly well with smaller datasets or when you want to keep things simple from a computational standpoint.
            """)

            # Why Choose Bag of Words?
            st.subheader("Why Choose Bag of Words?")
            st.write("""
            - **Simplicity**: The method is easy to understand and implement.
            - **Effective for Basic Tasks**: It performs well in straightforward text classification tasks, such as identifying spam emails.
            """)

            # Limitations
            st.subheader("Limitations")
            st.write("""
            - **Loss of Context**: One major drawback is that BoW ignores the order and context of words, which can lead to misunderstandings in meaning.
            - **High Dimensionality**: With large vocabularies, the resulting vectors can become very sparse, making analysis more challenging.
            - **Synonymy and Polysemy Issues**: BoW struggles with synonyms (different words that mean the same thing) and polysemy (the same word having multiple meanings), which can complicate interpretation.
            """)

            # Applications
            st.subheader("Applications")
            st.write("""
            The Bag of Words method is commonly used in:
            - **Document Classification**: Sorting documents into predefined categories.
            - **Spam Filtering**: Identifying unwanted emails based on their content.
            - **Basic Text Clustering**: Grouping similar documents together where context isn’t critical.
            """)

        # Other methods (Tf-idf, Word2Vec, etc.) can be similarly included here with their respective content.
          
        with st.expander("2. Tf-idf", expanded=False): 

            # Title of the page
            st.title("Understanding TF-IDF (Term Frequency-Inverse Document Frequency)")
            st.write(
                """
                TF-IDF, which stands for Term Frequency-Inverse Document Frequency, is a powerful technique used in text analysis to evaluate 
                the importance of words within a document relative to a larger collection of documents, known as a corpus. This method enhances 
                the basic Bag of Words approach by assigning weights to words based on their significance, allowing us to distinguish between 
                common words and those that carry more informative value. Essentially, it helps in highlighting unique terms that are more relevant 
                for understanding the content.
                """
            )

            # How It Works section
            st.markdown("<h1 style='font-size:24px;'>How It Works</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='font-size:18px;'>1. Term Frequency (TF)</h2>", unsafe_allow_html=True)

            st.write(
                """
                This metric measures how often a word appears in a specific document. The more frequently a word appears, 
                the higher its term frequency.
                """
            )

            #st.subheader("2. Inverse Document Frequency (IDF)")
            st.markdown("<h2 style='font-size:18px;'>2. Inverse Document Frequency (IDF)</h2>", unsafe_allow_html=True)

            st.write(
                """
                This component assesses the importance of a word by considering how common or rare it is across all documents. 
                Words that appear in many documents receive a lower IDF score, while those found in fewer documents get a higher score.
                """
            )

            #st.subheader("3. Calculating TF-IDF")
            st.markdown("<h2 style='font-size:18px;'>3. Calculating TF-IDF </h2>", unsafe_allow_html=True)

            st.write(
                """
                The TF-IDF score for each word in a document is calculated by multiplying its term frequency by its inverse document frequency:
                """
            )
            st.latex(r"\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)")
            st.write("where \( t \) is the term and \( d \) is the document.")

            # When to Use TF-IDF section
            #st.header("When to Use TF-IDF")
            st.markdown("<h2 style='font-size:24px;'>When to Use TF-IDF</h2>", unsafe_allow_html=True)

            st.write(
                """
                - **Distinguishing Relevant Words**: TF-IDF is particularly useful when it’s important to differentiate significant words 
                from common ones, such as in information retrieval or keyword identification.
                - **Medium to Large Datasets**: It works well for datasets where understanding the unique importance of terms 
                can enhance model performance.
                """
            )

            # Why Choose TF-IDF section
            #st.header("Why Choose TF-IDF?")
            st.markdown("<h2 style='font-size:24px;'>Why Choose TF-IDF?</h2>", unsafe_allow_html=True)

            st.write(
                """
                - **Reducing Common Word Influence**: By down-weighting frequently used words (like "the," "is," and "and"), TF-IDF helps 
                improve the relevance of analysis, making it effective for tasks like document categorization.
                - **Enhancement Over BoW**: It builds on the Bag of Words model by focusing on unique terms that are specific to individual 
                documents, thus providing richer insights.
                """
            )

            # Limitations section
            #st.header("Limitations")
            st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

            st.write(
                """
                - **Sparse Representation**: Like BoW, TF-IDF can still result in high-dimensional and sparse representations, especially 
                with large vocabularies.
                - **Ignoring Word Order and Context**: It does not capture the order of words or their contextual relationships, which can 
                limit its effectiveness in understanding nuanced meanings.
                - **Not Ideal for Semantic Tasks**: For applications where the semantic meaning of phrases is crucial, TF-IDF may fall short.
                """
            )

            # Applications section
            #st.header("Applications")
            st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

            st.write(
                """
                TF-IDF finds diverse applications across various fields:
                - **Search Engines and Information Retrieval**: It helps rank search results based on how relevant documents are to user 
                queries by prioritizing those with higher TF-IDF scores.
                - **Keyword Extraction**: Identifying key terms within documents based on their significance helps summarize content effectively.
                - **Text Classification**: In machine learning, TF-IDF transforms text data into numerical features that models can process, 
                improving classification accuracy.
                - **Sentiment Analysis**: By focusing on significant terms, TF-IDF aids in discerning sentiments expressed within texts.
                """
            )

        with st.expander("3. Word 2 Vec Embedding", expanded= False):
            # Title
            st.title("Overview of Word2Vec Embeddings")

            st.write("""
            Word2Vec is a powerful technique used in natural language processing (NLP) to learn word embeddings, 
            which are dense vector representations of words. This model captures semantic relationships 
            by analyzing the context in which words appear, positioning semantically similar words close 
            together in a continuous vector space.
            """)

            #st.header("How It Works")
            st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

            st.write("""
            Word2Vec employs two primary architectures to generate these embeddings:
            - **Skip-Gram:** This model predicts surrounding context words based on a given target word. 
            By maximizing the probability of context words appearing near the target, Skip-Gram effectively captures 
            various meanings of words depending on their different contexts.
            - **Continuous Bag of Words (CBOW):** In contrast, CBOW predicts a target word from a set of surrounding 
            context words. It emphasizes local context relationships by taking multiple context words and determining 
            the most probable target word.
            """)

            #st.header("When to Use Word2Vec")
            st.markdown("<h2 style='font-size:24px;'>When to Use Word2Vec</h2>", unsafe_allow_html=True)

            st.write("""
            Word2Vec is particularly beneficial for tasks that require a nuanced understanding of local word contexts, such as:
            - **Conversational AI:** Enhancing chatbots and virtual assistants by improving their understanding of user input.
            - **Text Classification:** Enabling more accurate classification of documents based on their content.
            It is especially effective for smaller to medium-sized datasets where computational efficiency and speed are important.
            """)

            #st.header("Why Choose Word2Vec?")
            st.markdown("<h2 style='font-size:24px;'>Why Choose Word2Vec?</h2>", unsafe_allow_html=True)

            st.write("""
            - **High-Quality Embeddings:** Word2Vec produces embeddings that are efficient to train and can effectively represent semantic similarities.
            - **Vector Arithmetic:** It allows for interesting calculations through vector arithmetic, such as solving analogies 
            (e.g., "king" - "man" + "woman" = "queen").
            - **Real-Time Training:** The model supports real-time updates, meaning embeddings can be continually refined as new data becomes available.
            """)

            #st.header("Limitations")
            st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

            st.write("""
            Despite its strengths, Word2Vec has some limitations:
            - **Static Embeddings:** The embeddings do not capture variations in word meanings based on context, 
            which can be problematic for polysemous words (e.g., "bank" can refer to a financial institution or the side of a river).
            - **Resource Intensive:** It requires significant computational resources and a large dataset to generate high-quality embeddings.
            - **Sensitivity to Parameters:** The quality of the embeddings can be sensitive to training parameters like window size and vector dimensionality.
            """)

            #st.header("Applications")
            st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

            st.write("""
            Word2Vec has numerous applications in NLP, including:
            - **Sentiment Analysis:** Understanding opinions expressed in text.
            - **Machine Translation:** Improving the accuracy of translating text from one language to another.
            - **Text Summarization:** Condensing information while preserving key points.
            - **Information Retrieval:** Enhancing search engines by improving how they understand queries and documents.
            - **Analogy Detection:** Solving analogy tasks by leveraging the mathematical properties of word vectors.
            """)
        
        with st.expander("4. Glove Embedding",expanded = False):

            # Title
            st.title("Understanding GloVe Embeddings")
            st.write("""
            GloVe, or Global Vectors for Word Representation, is a method for learning word embeddings 
            that focuses on capturing the global statistical information of words in a corpus. 
            By constructing a co-occurrence matrix that records how often words appear together, 
            GloVe aims to understand the relationships between words and represents them as 
            dense vectors in a continuous vector space.
            """)

            #st.header("How It Works")
            st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

            st.write("""
            GloVe generates word embeddings through a series of steps:
            - **Co-occurrence Matrix Creation:** The process begins by creating a global co-occurrence 
            matrix, which counts how frequently each word appears in the context of every other word 
            across a large corpus. This matrix serves as the foundation for understanding word relationships.
            - **Cost Function Formulation:** GloVe formulates a cost function that relates the dot product 
            of word vectors to the logarithm of their co-occurrence probabilities. The goal is to minimize 
            the difference between these two values, ensuring that the embeddings reflect actual word usage patterns.
            - **Matrix Factorization:** Finally, by factorizing the co-occurrence matrix, GloVe generates 
            dense word vectors that effectively capture semantic relationships across the entire corpus.
            """)

            #st.header("When to Use GloVe")
            st.markdown("<h2 style='font-size:24px;'>When to Use GloVe</h2>", unsafe_allow_html=True)

            st.write("""
            GloVe is particularly effective for:
            - **Large Datasets:** It excels in scenarios where capturing global statistical relationships 
            significantly enhances performance.
            - **Understanding Word Meanings:** GloVe is suitable for tasks requiring a comprehensive 
            understanding of word meanings, especially when words have multiple meanings depending on broader context.
            """)

            #st.header("Why Choose GloVe?")
            st.markdown("<h2 style='font-size:24px;'>Why Choose GloVe?</h2>", unsafe_allow_html=True)

            st.write("""
            - **Global Context:** GloVe embeddings are based on global co-occurrence statistics, making them 
            effective for capturing semantic relationships across diverse contexts.
            - **Generalization:** The embeddings often generalize well to various tasks due to their 
            incorporation of broader word relationships.
            - **Intuitive Interpretability:** Similar to Word2Vec, GloVe allows for intuitive interpretations 
            of word relationships through vector operations.
            """)

            #st.header("Limitations")
            st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

            st.write("""
            Despite its strengths, GloVe has some limitations:
            - **Training Speed:** The need for a large co-occurrence matrix can make GloVe slower to train, 
            particularly with very large vocabularies.
            - **Pre-trained Embeddings:** Like Word2Vec, pre-trained embeddings may not fit specialized 
            vocabularies or domains.
            - **Lack of Real-Time Updates:** GloVe is not designed for continual learning, making it less effective 
            in scenarios requiring real-time updates.
            """)

            #st.header("Applications")
            st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

            st.write("""
            GloVe embeddings are widely used in various applications, including:
            - **Text Classification:** Enhancing the performance of classifiers by providing rich semantic features.
            - **Sentiment Analysis:** Understanding the sentiment of text by analyzing word relationships.
            - **Machine Translation:** Improving translation quality by capturing contextual meanings.
            - **Information Retrieval:** Enhancing search engines by better understanding user queries.
            """)

        with st.expander("5. Fast Text", expanded = False):

            # Title
            st.title("Understanding FastText Embeddings")

            # Introduction
            st.write("""
            FastText is a sophisticated method for generating word embeddings, developed by Facebook's AI Research (FAIR). Unlike traditional models that treat words as indivisible units, FastText utilizes subword information, allowing it to analyze the internal structure of words. This capability is particularly beneficial for languages with complex morphology and for handling rare or out-of-vocabulary words.
            """)

            # How It Works
            st.markdown("<h2 style='font-size:24px;'>How It Works</h2>", unsafe_allow_html=True)

            st.write("""
            1. **Subword Information**:  
            FastText decomposes words into smaller components known as n-grams, which are sequences of characters. For example, the word "embedding" can be represented using 3-grams like "emb", "bme", "med", "edd", "ddi", and "ing". This approach enables FastText to capture morphological patterns and learn embeddings for similar words, even if they were not present during training.

            2. **Training Process**:  
            FastText employs training techniques similar to Word2Vec, using either the **Skip-gram** or **Continuous Bag of Words (CBOW)** models:
            - **Skip-gram**: Predicts context words given a target word (e.g., predicting "feline" and "pet" from "cat").
            - **CBOW**: Predicts the target word from a set of context words (e.g., predicting "cat" from "feline" and "pet").

            3. **Embedding Calculation**:  
            The final embedding for a word is computed as the sum of the embeddings of its constituent n-grams. This allows FastText to generate embeddings for out-of-vocabulary words based on their character-level representations. For instance, the embedding for "unkown" can be derived from its n-grams like "unk", "kno", "now", and "own".
            """)

            # When to Use FastText
            st.markdown("<h2 style='font-size:24px;'>When to Use FastText</h2>", unsafe_allow_html=True)

            st.write("""
            FastText is particularly advantageous in scenarios involving:
            - **Morphologically Rich Languages**: It effectively captures the meanings of words based on their morphological structure.
            - **Handling Rare Words**: FastText generates embeddings for rare terms that may not be included in the training corpus, making it useful in specialized domains.
            """)

            # Why Choose FastText?
            st.markdown("<h2 style='font-size:24px;'>Why Choose FastText?</h2>", unsafe_allow_html=True)

            st.write("""
            - **Character-Level Information**: By incorporating subword information, FastText produces robust embeddings that reflect semantic nuances, enhancing performance in various natural language processing (NLP) tasks.
            - **Robustness**: The embeddings can accommodate variations such as misspellings or different word forms, making them resilient in noisy data environments.
            - **Improved Generalization**: FastText embeddings generalize better across tasks and domains due to their understanding of word structure and semantics.
            """)

            # Limitations
            st.markdown("<h2 style='font-size:24px;'>Limitations</h2>", unsafe_allow_html=True)

            st.write("""
            Despite its strengths, FastText has some limitations:
            - **Memory Usage**: Storing embeddings for both words and n-grams can increase memory requirements.
            - **Training Time**: The model may require longer training times compared to simpler embedding models due to its complexity.
            - **Interpretability**: The resulting embeddings may be less intuitive compared to traditional embeddings since they incorporate multiple n-grams rather than whole words.
            """)

            # Applications
            st.markdown("<h2 style='font-size:24px;'>Applications</h2>", unsafe_allow_html=True)

            st.write("""
            FastText embeddings are widely used in various NLP tasks, including:
            - **Text Classification**: Enhancing classifiers' performance in sentiment analysis, topic detection, and spam detection by providing rich semantic features.
            - **Named Entity Recognition (NER)**: Improving recognition rates for rare entities by leveraging its character-level approach.
            - **Sentiment Analysis**: Effectively analyzing sentiment by capturing nuances in language relationships.
            - **Machine Translation**: Enhancing translation quality by better managing morphologically complex words.
            """)

            # Conclusion
            st.write("""
            FastText represents a significant advancement in word embedding techniques, enabling more nuanced natural language processing capabilities. Its subword approach not only improves performance on traditional NLP tasks but also opens new avenues for understanding and generating language.
            """)

    with col2:
        def preprocess_text(text, use_stemmer):
            # 1. Lowercasing
            text = text.lower()
            # 2. Removing Punctuation
            text = re.sub(r'[^\w\s]', '', text)
            # 3. Tokenization
            words = word_tokenize(text)
            # 4. Remove stopwords and apply stemming or lemmatization
            if use_stemmer:
                processed_words = [stemmer.stem(word) for word in words if word not in stop_words]
            else:
                processed_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
            # Join the processed words back into a single string
            return ' '.join(processed_words)

        st.subheader("Sample Text for Vectorization Methods")
        selection_1 = st.radio("Select one text data:", options=["Harry Potter", "Narnia"], key='book_selector')

        if selection_1 == "Harry Potter":
            text_input = """
            Harry was bleeding. Clutching his right hand in his left and sweating under his breath, he shouldered open his bedroom door. 
            There was a crunch of breaking china. He had trodden on a cup of cold tea that had been sitting on the floor outside his bedroom door.

            “What the—?” He looked around, the landing of number four, Privet Drive, was deserted. 
            Possibly the cup of tea was Dudley’s idea of a clever booby trap. Keeping his bleeding hand elevated, 
            Harry scraped the fragments of cup together with the other hand and threw them into the already crammed bin just visible inside his bedroom door.
            Then he tramped across to the bathroom to run his finger under the tap.
            """
        elif selection_1 == "Narnia":
            text_input = """
            WHAT an extraordinary place!” cried Lucy. “All those stone animals — and people too! It’s — it’s like a museum.” 

            “Hush,” said Susan, “Aslan’s doing something He was indeed. He had bounded up to the stone lion and breathed on him. 

            Then without waiting a moment he whisked round — almost as if he had been a cat chasing its tail -and breathed also on the stone dwarf, which (as you remember) was standing a few feet from the lion with his back to it. 

            Then he pounced on a tall stone dryad which stood beyond the dwarf, turned rapidly aside to deal with a stone rabbit on his right, and rushed on to two centaurs. 

            But at that moment Lucy said, “Oh, Susan! Look! Look at the lion.” I expect you’ve seen someone put a lighted match to a bit of newspaper which is propped up in a grate against an unlit fire. And for a second nothing seems to have happened; and then you notice a tiny streak of flame creeping along the edge of the newspaper. It was like that now. 
            """

        # Number of documents selector
        num_docs = st.slider("Select the number of documents to split into:", 1, 5, 1, key='num_docs_slider')

        # Split the text_input into the selected number of parts
        text_split = text_input.strip().split()
        split_length = len(text_split) // num_docs
        splitted_docs = [" ".join(text_split[i*split_length:(i+1)*split_length]) for i in range(num_docs)]

        # Adjust for any remaining words
        if len(text_split) % num_docs != 0:
            splitted_docs[-1] += " " + " ".join(text_split[num_docs * split_length:])

        # Display the documents
        st.write("**Splitted Documents:**")
        for i, doc in enumerate(splitted_docs):
            st.write(f"Document {i+1}: {doc}")

        # Choose normalization technique
        method = st.selectbox("Choose a normalization technique:", ["Stemming", "Lemmatization"], key='normalization_technique')

        # Determine which method to use based on user selection
        use_stemmer = method == "Stemming"

        # Preprocess each document
        processed_docs = [preprocess_text(doc, use_stemmer) for doc in splitted_docs]

        st.write("**Processed Documents:**")
        for i, doc in enumerate(processed_docs):
            st.write(f"Document {i+1}: {doc}")

        # Define the keywords
        keywords = ["Bag of Words", "Tf-idf", "Word2Vec", "Glove", "FastText"]

        # Create a dropdown for selecting a method
        selected_keyword = st.selectbox("Select a Vectorization Method", options=keywords, key='vectorization_method')

        # Display the selected method
        if selected_keyword == "Bag of Words":
            # N-gram selection
            ngram_choice = st.radio("Choose N-gram type:", ["Unigram", "Bigram"], key='ngram_choice_bow')

            # Set n-gram range based on selection
            if ngram_choice == "Unigram":
                ngram_range = (1, 1)
            else:
                ngram_range = (1, 2)  # Unigrams + Bigrams

            # Convert preprocessed text to Bag of Words representation
            vectorizer = CountVectorizer(ngram_range=ngram_range)
            bow_matrix = vectorizer.fit_transform(processed_docs)

            # Convert to DataFrame for display
            bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

            st.subheader("Bag of Words Matrix")
            st.write(bow_df)

        elif selected_keyword == "Tf-idf":
            if processed_docs:
                # N-gram selection
                ngram_choice = st.radio("Choose N-gram type:", ["Unigram", "Bigram"], key='ngram_choice_tfidf')

                # Set n-gram range based on selection
                if ngram_choice == "Unigram":
                    ngram_range = (1, 1)
                else:
                    ngram_range = (1, 2)  # Unigrams + Bigrams

                # Create a TfidfVectorizer instance
                vectorizer = TfidfVectorizer(ngram_range=ngram_range)

                # Fit and transform the documents to create the TF-IDF matrix
                tfidf_matrix = vectorizer.fit_transform(processed_docs)

                # Convert the TF-IDF matrix to a DataFrame
                tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

                # Display the TF-IDF DataFrame
                st.subheader("TF-IDF Matrix")
                st.dataframe(tfidf_df)
            else:
                st.warning("Please enter at least one document.")

        elif selected_keyword == "Word2Vec":
            # Prepare data
            sentences = [doc.split() for doc in processed_docs if doc]

            # Train Word2Vec model
            st.subheader("Training Word2Vec Model...")
            model = Word2Vec(sentences, vector_size=50, window=5, min_count=1, workers=4)
            st.success("Word2Vec model trained!")

            # Display word vectors
            words = list(model.wv.index_to_key)
            word_vectors = model.wv[words]

            # Create a DataFrame for the word vectors
            df_vectors = pd.DataFrame(word_vectors, index=words)

            st.subheader("Word Vectors")
            st.write(df_vectors.head())

            # Visualization
            st.subheader("Word Embedding Visualization")
            pca = PCA(n_components=2)
            result = pca.fit_transform(word_vectors)

            plt.figure(figsize=(10, 6))
            plt.scatter(result[:, 0], result[:, 1])

            for i, word in enumerate(words):
                plt.annotate(word, xy=(result[i, 0], result[i, 1]))
            st.pyplot(plt)

        elif selected_keyword == "Glove":
            # Load GloVe model
            @st.cache(allow_output_mutation=True)
            def load_glove_model():
                with open('pages\proprocessing\glove_model.pkl', 'rb') as f:
                    return pickle.load(f)

            glove_model = load_glove_model()

            # User input for sentence
            user_input = st.text_input("Enter a sentence:", "Your example text goes here.", key='glove_user_input')
            tokens = user_input.lower().split()
            vectors = [glove_model[word] for word in tokens if word in glove_model]

            if vectors:
                df_glove = pd.DataFrame(vectors, index=[tokens], columns=[f'Dim {i+1}' for i in range(len(vectors[0]))])
                st.write("Word Vectors:")
                st.dataframe(df_glove)

                # Visualization
                st.subheader("Word Embedding Visualization")
                pca = PCA(n_components=2)
                result = pca.fit_transform(vectors)

                plt.figure(figsize=(10, 6))
                plt.scatter(result[:, 0], result[:, 1])

                for i, word in enumerate(tokens):
                    plt.annotate(word, xy=(result[i, 0], result[i, 1]))
                st.pyplot(plt)
            else:
                st.warning("No valid words found in the input.")

        elif selected_keyword == "FastText":
            # Text input area
            text_input_fasttext = st.text_area("Enter text (one document per line):", key='fasttext_text_input')

            # Choose a task
            task = st.radio("Choose an NLP Task", ["Text Classification", "Named Entity Recognition", "Semantic Search", "Spell Correction", "Topic Modeling"], key='fasttext_task')

            if text_input_fasttext:
                processed_docs_ft = text_input_fasttext.splitlines()
                sentences_ft = [doc.split() for doc in processed_docs_ft if doc]

                # Train FastText model
                st.subheader("Training FastText Model...")
                model_ft = FastText(sentences=sentences_ft, vector_size=50, window=3, min_count=1, sg=1, epochs=10)
                st.success("FastText model trained!")

                if task == "Semantic Search":
                    query = st.text_input("Enter search query:", key='fasttext_query')
                    if st.button("Find Similar Words"):
                        query_tokens = query.lower().split()
                        query_vector = np.mean([model_ft.wv[word] for word in query_tokens if word in model_ft.wv], axis=0)
                        similar_words = model_ft.wv.similar_by_vector(query_vector, topn=10)
                        st.write("Words similar to your query:")
                        for word, similarity in similar_words:
                            st.write(f"Word: {word}, Similarity: {similarity:.4f}")

                elif task == "Named Entity Recognition":
                    st.header("Named Entity Recognition with FastText")
                    nlp = spacy.load("en_core_web_sm")

                    if st.button("Identify Entities"):
                        doc = nlp(' '.join(processed_docs_ft))
                        for ent in doc.ents:
                            st.write(f"Entity: {ent.text}, Label: {ent.label_}")
                            if ent.text in model_ft.wv:
                                vector = model_ft.wv[ent.text]
                                st.write(f"FastText Vector for '{ent.text}': {vector[:10]}")
                            else:
                                st.write(f"No FastText vector available for '{ent.text}'")
                # Other tasks can be implemented similarly

    # Run the app
    # Note: This should be outside the run() function
if __name__ == '__main__':
    run()