import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

# Page Configuration
#st.set_page_config(layout="wide")
def run():
    st.title("Categorical Encoding Techniques")

    # Overview of Categorical Encoding Techniques
    st.info("""
    Categorical encoding techniques are essential methods used to transform categorical data into numerical formats suitable for machine learning algorithms. Since most algorithms require numerical input, these techniques help bridge the gap between non-numeric data and model compatibility. Common encoding methods include Label Encoding, One-Hot Encoding, Binary Encoding, Frequency Encoding, Target Encoding, Ordinal Encoding, and Leave-One-Out Encoding. Each method has its specific use cases, advantages, and limitations, making the choice of technique crucial based on the data and modeling needs.
    """)


    # Create columns for layout
    col1, col2 = st.columns([2, 1])  # Adjust column sizes

    with col2:
        # Sidebar for Input Data
        st.header("Input Categorical Data")
        data_input = st.text_area("Enter your categorical data (comma-separated values):", "red, blue, green, red, blue")
        target_input = st.text_area("Enter target values (comma-separated values, same length as categorical data):", "1, 0, 1, 1, 0")

        # Convert inputs to numpy arrays
        st.session_state.cat_input = np.array([i.strip() for i in data_input.split(',')]).reshape(-1, 1)
        st.session_state.target_input = np.array([int(i.strip()) for i in target_input.split(',')])

        # Display the original data
        st.write("### Original Data")
        original_data = pd.DataFrame({
            'Category': st.session_state.cat_input.flatten(),
            'Target': st.session_state.target_input
        })
        st.write(original_data)

    with col1:

            # Types of Categorical Data
        st.write("""
        ### Types of Categorical Data
        **1. Nominal Data:** Refers to categorical variables without any inherent order. Examples include colors, animal types, and city names.

        **Applicable Encoding Techniques for Nominal Data:**
        - One-Hot Encoding
        - Label Encoding
        - Binary Encoding
        - Frequency Encoding
        - Target Encoding

        **2. Ordinal Data:** Consists of categorical variables with a clear order. Examples include size, satisfaction ratings, and educational levels.

        **Applicable Encoding Techniques for Ordinal Data:**
        - Ordinal Encoding
        - Label Encoding
        - Target Encoding
        """)

        # Encoding Techniques
        st.header("Encoding Techniques")

        # 1. One-Hot Encoding
        with st.expander("1. One-Hot Encoding", expanded=False):
            st.write("One-hot encoding creates binary columns for each category in a categorical feature. Each observation is marked with a 1 in the column of its corresponding category and 0 in all others. This technique eliminates the ordinal nature of label encoding, making it suitable for non-ordinal categories.")
            #st.write("**Example:** The 'color' feature becomes three columns: `is_red`, `is_green`, and `is_blue`. For 'red', it would be `1 | 0 | 0`, for 'green', it would be `0 | 1 | 0`, and for 'blue', it would be `0 | 0 | 1`.")
            st.write("**Advantages:** Eliminates the ordinal nature of label encoding, making it suitable for non-ordinal categories.")
            st.write("**Limitations:** Can lead to high dimensionality if the number of categories is large, which may cause issues in model training.")
            if st.checkbox("Apply One-Hot Encoding"):
                one_hot_encoder = OneHotEncoder(sparse_output=False)
                one_hot_encoded_data = one_hot_encoder.fit_transform(st.session_state.cat_input)
                one_hot_df = pd.DataFrame(one_hot_encoded_data, columns=one_hot_encoder.get_feature_names_out(['Category']))
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), one_hot_df], axis=1)

        # 2. Label Encoding
        with st.expander("2. Label Encoding", expanded=False):
            st.write("Label encoding assigns a unique integer to each category in a categorical feature. It is a straightforward approach where categories are mapped to numbers, starting from 0. While simple and memory efficient, it can create a misleading ordinal relationship between categories.")
            #st.write("**Example:** For a feature 'color' with categories 'red', 'green', and 'blue', label encoding might yield: `red = 0`, `green = 1`, `blue = 2`.")
            st.write("**Advantages:** Simple and requires less memory than one-hot encoding.")
            st.write("**Limitations:** Can create a false sense of order, implying that one category is greater or less than another.")
            if st.checkbox("Apply Label Encoding"):
                label_encoder = LabelEncoder()
                label_encoded_data = label_encoder.fit_transform(st.session_state.cat_input.flatten())
                label_encoded_df = pd.DataFrame(label_encoded_data, columns=["Label Encoded"])
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), label_encoded_df], axis=1)

        # 3. Ordinal Encoding
        with st.expander("3. Ordinal Encoding", expanded=False):
            st.write("Ordinal encoding is similar to label encoding but specifically used for categorical variables that have a clear order. This technique preserves the ordinal relationship, making it suitable for ordered categories.")
            #st.write("**Example:** For a feature 'size' with categories 'small', 'medium', and 'large': `small = 0`, `medium = 1`, `large = 2`.")
            st.write("**Advantages:** Preserves the ordinal relationship, making it suitable for ordered categories.")
            st.write("**Limitations:** May not be appropriate for non-ordinal data.")
            ordinal_categories_input = st.text_input("Enter ordinal categories (comma-separated, in the desired order):", "red, green, blue")
            ordinal_categories = [i.strip() for i in ordinal_categories_input.split(',')]

            if st.checkbox("Apply Ordinal Encoding"):
                # Apply ordinal encoding based on user-defined categories
                ordinal_encoder = OrdinalEncoder(categories=[ordinal_categories])
                try:
                    ordinal_encoded_data = ordinal_encoder.fit_transform(st.session_state.cat_input)
                    ordinal_encoded_df = pd.DataFrame(ordinal_encoded_data, columns=["Ordinal Encoded"])
                    st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), ordinal_encoded_df], axis=1)
                except ValueError as e:
                    st.error(f"Error: {e}. Make sure the input data categories match the specified ordinal categories.")

        # 4. Frequency Encoding
        with st.expander("4. Frequency Encoding", expanded=False):
            st.write("Frequency encoding replaces categories with their frequency or count in the dataset. This method highlights the distribution of categories and retains information about the size of each category, which can help improve model performance.")
            #st.write("**Example:** If 'color' has the following counts: `red: 5`, `green: 3`, `blue: 7`, the encoding would be: `red = 5`, `green = 3`, `blue = 7`.")
            st.write("**Advantages:** Retains information about the size of each category and can help improve model performance.")
            st.write("**Limitations:** Does not capture the relationship between categories and the target variable.")
            if st.checkbox("Apply Frequency Encoding"):
                # Convert the input to a pandas Series for easier manipulation
                categories_series = pd.Series(st.session_state.cat_input.flatten())
                frequency_df = categories_series.value_counts().to_dict()  # Count occurrences
                frequency_encoded_data = categories_series.map(frequency_df)  # Map frequencies
                frequency_encoded_df = pd.DataFrame(frequency_encoded_data, columns=["Frequency Encoded"])
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), frequency_encoded_df], axis=1)

        # 5. Target Encoding (Mean Encoding)
        with st.expander("5. Target Encoding", expanded=False):
            st.write("Target encoding replaces each category with the mean of the target variable for that category. This technique can provide significant insights when categories have a strong influence on the target variable, but it carries a risk of overfitting, particularly in small datasets.")
            #st.write("**Example:** If predicting house prices based on 'neighborhood': Neighborhood A: average price = $300k, Neighborhood B: average price = $500k. Encoding would replace each neighborhood with its average price.")
            st.write("**Advantages:** Can provide significant insights when categories have a strong influence on the target variable.")
            st.write("**Limitations:** Risk of overfitting, particularly in small datasets.")
            if st.checkbox("Apply Target Encoding"):
                # Calculate mean target for each category
                target_means = original_data.groupby('Category')['Target'].mean()
                target_encoded_data = original_data['Category'].map(target_means)
                target_encoded_df = pd.DataFrame({
                    'Category': original_data['Category'],
                    'Target Encoded': target_encoded_data
                })
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), target_encoded_df['Target Encoded']], axis=1)

        # 6. Binary Encoding
        with st.expander("6. Binary Encoding", expanded=False):
            st.write("Binary encoding first converts categories into integers and then into binary code. Each bit is placed in a separate column. This method is efficient in terms of memory usage compared to one-hot encoding, especially when the number of categories is large.")
            #st.write("**Example:** For three categories 'red', 'green', and 'blue' (encoded as 0, 1, 2): `red = 00`, `green = 01`, `blue = 10`. This results in two new columns: `Column 1 | Column 2` -> `0 | 0` (for red), `0 | 1` (for green), `1 | 0` (for blue).")
            st.write("**Advantages:** Reduces the number of dimensions compared to one-hot encoding.")
            st.write("**Limitations:** May still create some confusion with the ordinal interpretation of binary values.")
            if st.checkbox("Apply Binary Encoding"):
                # Map categories to integers
                category_to_int = {category: idx for idx, category in enumerate(original_data['Category'].unique())}
                binary_encoded_data = np.array([[int(x) for x in np.binary_repr(category_to_int[cat], width=2)] for cat in original_data['Category']])
                binary_encoded_df = pd.DataFrame(binary_encoded_data, columns=["Binary Column 1", "Binary Column 2"])
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), binary_encoded_df], axis=1)

        # 7. Leave-One-Out Encoding
        with st.expander("7. Leave-One-Out Encoding", expanded=False):
            st.write("Leave-One-Out Encoding is a variation of target encoding where each category is replaced with the mean of the target variable, calculated without considering the current observation. This technique reduces the risk of overfitting by accounting for the target variable without biasing the encoding.")
            st.write("**Advantages:** Reduces the risk of overfitting by accounting for the target variable without biasing the encoding.")
            st.write("**Limitations:** More complex to implement and requires careful handling to avoid data leakage.")
            if st.checkbox("Apply Leave-One-Out Encoding"):
                # Calculate leave-one-out encoding
                loo_encoded_data = []
                for index, row in original_data.iterrows():
                    category = row['Category']
                    # Calculate mean excluding the current observation
                    mean_target = original_data[original_data['Category'] == category]['Target'].mean()
                    loo_encoded_data.append(mean_target)
                loo_encoded_df = pd.DataFrame(loo_encoded_data, columns=["Leave-One-Out Encoded"])
                st.session_state.df_after = pd.concat([original_data.reset_index(drop=True), loo_encoded_df], axis=1)


    with col2:

        # Display the transformed data after applying the encoding technique
        if 'df_after' in st.session_state:
            st.write("### Transformed Data")
            st.write(st.session_state.df_after)



        # # Download the transformed data as a CSV file
        # if st.button("Download Transformed Data"):
        #     transformed_data = st.session_state.df_after.to_csv(index=False)
        #     st.download_button("Download", transformed_data, file_name="transformed_data.csv", mime="text/csv")
