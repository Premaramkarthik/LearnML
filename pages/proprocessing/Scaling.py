# import streamlit as st
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler, QuantileTransformer
# from scipy import stats
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # Page Configuration
# #st.set_page_config(layout="wide")
# def run():
#     st.title("Data Scaling and Transformation Techniques")

#     st.write("In the world of data analysis and machine learning, preprocessing data is crucial for building effective models. One of the key aspects of preprocessing is understanding how to properly scale and transform your data. This blog post will dive deep into these concepts, their importance, and practical applications, complete with code examples to illustrate their use.")

#     st.markdown("""
#     ### Why Scaling and Transformations Matter
#     Scaling and transforming data is crucial in data preprocessing, as it can significantly impact model performance. It helps:
#     - Normalize feature ranges for comparability, especially in distance-based algorithms.
#     - Stabilize variance and reduce skewness in data distribution.
#     - Enhance model performance and convergence speed for gradient-based algorithms.
#     """)


#     # Create columns for wider layout
#   # Adjust column sizes


#     # with col2:
#     #     # Sidebar for Input Data
#     #     st.header("Input Data")
#     #     data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")
#     #     data = np.array([float(i) for i in data_input.split(',')]).reshape(-1,1)
#     #     # Store the modified DataFrame in session state for later access
#     #     st.session_state.df_input = data

#     #     st.write("")
#     #     st.write("")


#     # Scaling Techniques
#     st.header("Scaling Techniques")

#         # 1. Min-Max Scaling
#     with st.expander("1. Min-Max Scaling (Normalization)", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:

#             st.write("""
#             Min-Max scaling rescales features to a specific range, usually [0, 1]. It is useful when features have different ranges but need to be compared on the same scale.
#             """)

#             # Formula and explanation for Min-Max Scaling
#             st.write(
#                 """- $$X_{scaled} = \\frac{X - X_{min}}{X_{max} - X_{min}}$$, where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, $$X_{min}$$ is the minimum value of the feature, and $$X_{max}$$ is the maximum value of the feature. This transformation ensures that all features are on the same scale."""
#             )

#             st.write("""
#             - **Scaling Range**: The resulting scaled values will fall within the range of 0 and 1, making it easier to compare features and aiding algorithms that require normalized input.

#             - **Sensitivity to Outliers**: Min-Max scaling is sensitive to outliers; if the minimum and maximum values are significantly influenced by outliers, the scaled values of other data points will be compressed into a small range.

#             - **Applications**: This method is commonly used in scenarios where the model expects data within a bounded range, such as in neural networks and algorithms that utilize distance measures.
#             """)

            
     
#         with col2:

#            if st.checkbox("Apply Min-Max Scaling"): 

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Standard Scaling
#                 scaler = MinMaxScaler()
#                 data_scaled = scaler.fit_transform(data)

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
#                 axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Indexes", fontsize=12)

#                 # Plot scaled data
#                 sns.scatterplot(x=data_scaled.flatten(), y=range(len(data_scaled)), ax=axes[1])
#                 axes[1].set_title("After Preprocessing", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Scaled Values", fontsize=12)
#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

#                 # st.write("")
#                 # st.write("")

#     # 2. Mean Normalization
#     with st.expander("2. Mean Normalization", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:
#             st.write("""
#             Mean normalization transforms features to center around zero, typically within a range of -1 to 1. This helps stabilize the learning process, especially for models sensitive to feature scales.
#             """)

#             # Formula and explanation for Mean Normalization
#             st.write(
#                 """- $$X_{normalized} = \\frac{X - \\mu}{X_{max} - X_{min}}$$, where $$X_{normalized}$$ is the normalized value, $$X$$ is the original value, $$\\mu$$ is the mean of the feature, $$X_{min}$$ is the minimum, and $$X_{max}$$ is the maximum. This formula ensures the data has a mean of zero and lies within a defined range.
#                 """
#             )

#             st.write("""
#             - **Centering Around Zero**: After applying mean normalization, data points will center around zero. This is particularly useful for gradient-based optimization, as it helps models converge faster.

#             - **Reducing Bias**: By adjusting features to have similar means, mean normalization minimizes biases due to differing feature scales, improving model performance in certain cases.

#             - **Applications**: Mean normalization is commonly used in linear regression and other algorithms where centering features around zero makes the model more stable.
#             """)

#         with col2:

#             # Option to apply Mean Normalization
#             if st.checkbox("Apply Mean Normalization"): 

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Mean Normalization
#                 data_mean = np.mean(data)
#                 data_range = np.max(data) - np.min(data)
#                 data_normalized = (data - data_mean) / data_range

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
#                 axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Indexes", fontsize=12)

#                 # Plot normalized data
#                 sns.scatterplot(x=data_normalized.flatten(), y=range(len(data_normalized)), ax=axes[1])
#                 axes[1].set_title("After Mean Normalization", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Normalized Values", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

#     # 3. Max Absolute Scaling
#     with st.expander("3. Max Absolute Scaling", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:

#             st.subheader("")
#             st.write("""

#             Max absolute scaling is a scaling technique that scales each feature by its maximum absolute value. This transforms the data into a range between -1 and 1 while maintaining the sparsity of the data.
#             """)

#             # Formula and explanation for Max Absolute Scaling
#             st.write(
#                 """- $$X_{scaled} = \\frac{X}{|X_{max}|}$$, where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, and $$|X_{max}|$$ is the maximum absolute value of the feature. This method scales the data to a range between -1 and 1 while maintaining the sparsity of the data."""
#             )

#             st.write("""
#             - **Handling Sparse Data**: Max absolute scaling is particularly effective for sparse data (data with many zero values) as it maintains the zero entries. 

#             - **Range of Values**: The values after max absolute scaling will fall within the range of -1 to 1, making it easier to compare features that are in different scales.

#             - **Applications**: This method is commonly used in machine learning models where data sparsity is important, such as with some types of regression models and neural networks.
#             """)

#         with col2:
        
#             if st.checkbox("Apply Max Absolute Scaling"): 

#             # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Max Absolute Scaling
#                 max_abs_value = np.max(np.abs(data))
#                 data_max_abs_scaled = data / max_abs_value

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
#                 axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Indexes", fontsize=12)

#                 # Plot scaled data
#                 sns.scatterplot(x=data_max_abs_scaled.flatten(), y=range(len(data_max_abs_scaled)), ax=axes[1])
#                 axes[1].set_title("After Max Absolute Scaling", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Scaled Values", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)


#     # 4. Standardization (Z-score Normalization)
#     with st.expander("4. Standardization (Z-score Normalization)", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:

#             st.write("""
#             Standardization, also known as Z-score normalization, is a technique used to center and scale data. It transforms the data such that its mean is 0 and its standard deviation is 1. This is useful for datasets where the features have different units or scales.

#             - **Formula**: The formula for standardization is given by:
#             """)

#             # Centered LaTeX equation
#             st.write(
#                 """- $$Z = \\frac{X - \\mu}{\\sigma}$$, where $$Z$$ is the standardized value, $$X$$ is the original value, $$\\mu$$ is the mean of the feature, and $$\\sigma$$ is the standard deviation. This transformation helps in comparing features that are on different scales."""
#             )

#             st.write("""
#             - **Preservation of Distribution**: Unlike Min-Max scaling, which compresses data into a fixed range, standardization preserves the distribution of the data. This means that if the original data follows a Gaussian distribution, the standardized data will also follow a Gaussian distribution with a mean of 0 and a standard deviation of 1.

#             - **Robustness to Outliers**: While standardization is sensitive to outliers, as they can affect the mean and standard deviation, it is generally more robust than Min-Max scaling in terms of preserving the relationships between values in a dataset. This is particularly important in algorithms that assume normal distribution.

#             - **Applications**: Standardization is particularly useful in machine learning algorithms that rely on distance metrics (like K-Nearest Neighbors or Support Vector Machines) and in gradient-based optimization methods (like neural networks). It helps in accelerating convergence during training and improves the overall performance of the model by ensuring all features contribute equally.
#             """)


#         with col2:

#             if st.checkbox("Apply Z-Score Normalization"): 

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Z-Score Normalization
#                 mean = np.mean(data)
#                 std_dev = np.std(data)
#                 if std_dev == 0:
#                     st.error("Standard deviation is zero, Z-Score Normalization cannot be applied.")
#                     st.stop()
#                 data_z_score = (data - mean) / std_dev

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
#                 axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Indexes", fontsize=12)

#                 # Plot normalized data
#                 sns.scatterplot(x=data_z_score.flatten(), y=range(len(data_z_score)), ax=axes[1])
#                 axes[1].set_title("After Z-Score Normalization", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Z-Score Values", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

#     # 5. Robust Scaling
#     with st.expander("5. Robust Scaling", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:
#             st.write("""

#             Robust scaling is a technique that scales the features by removing the median and scaling them according to the Interquartile Range (IQR). It is particularly useful for datasets with outliers, as it reduces their influence.
#             """)

#             # Formula and explanation for Robust Scaling
#             st.write(
#                 """- $$X_{scaled} = \\frac{X - Q_2}{Q_3 - Q_1}$$, \t where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, $$Q_2$$ is the median, $$Q_1$$ is the first quartile, and $$Q_3$$ is the third quartile. This method effectively scales the data while reducing the influence of outliers."""
#             )

#             st.write("""
#             - **Robustness to Outliers**: Because it uses the median and IQR for scaling, robust scaling is less affected by outliers compared to Min-Max or standard scaling. This makes it suitable for datasets with extreme values.

#             - **Distribution Preservation**: Unlike Min-Max scaling, which compresses values into a fixed range, robust scaling maintains the relationships between the values.

#             - **Applications**: Robust scaling is particularly useful in scenarios where the dataset contains outliers or when dealing with data that follows a non-Gaussian distribution.
#             """)
        
#         with col2:

#             if st.checkbox("Apply Robust Scaling"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Robust Scaling
#                 median = np.median(data)
#                 q1 = np.percentile(data, 25)
#                 q3 = np.percentile(data, 75)
#                 iqr = q3 - q1  # Interquartile Range
#                 if iqr == 0:
#                     st.error("IQR is zero, Robust Scaling cannot be applied.")
#                     st.stop()
#                 data_robust_scaled = (data - median) / iqr

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
#                 axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Indexes", fontsize=12)

#                 # Plot scaled data
#                 sns.scatterplot(x=data_robust_scaled.flatten(), y=range(len(data_robust_scaled)), ax=axes[1])
#                 axes[1].set_title("After Robust Scaling", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Scaled Values", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

                


#     # Transformations
#     st.header("Transformations")
#     st.markdown("Transformations adjust the data distribution. Here are some common methods:")

#     # 1. Log Transformation
#     with st.expander("1. Log Transformation", expanded=False):

#         col1, col2 = st.columns([1.2, 1])

#         with col1:

#             st.write("""
#             The log transformation is used to reduce right skewness in data. It helps stabilize variance and make data more normally distributed.
#             """)
#             st.write(
#                 """- $$y = \\log(X)$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation is applicable only to positive values, as the logarithm of zero or negative numbers is undefined."""
#             )
#             st.write("""
#             **Applications**: 
#             - Useful for financial data where multiplicative relationships exist, such as income or prices.
#             - Commonly used in regression models to meet the assumption of normally distributed residuals.
            
#             **When to Use**: 
#             - When the data is positively skewed and contains outliers.
#             - When multiplicative relationships exist in the data.
            
#             **Limitations**: 
#             - Cannot be applied to zero or negative values.
#             - May not be effective if the data is normally distributed.
#             """)

#         with col2:

#             if st.checkbox("Apply Log Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')])
#                     if any(data <= 0):
#                         st.error("Log transformation requires all values to be greater than 0. Please modify your input.")
#                         st.stop()
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Log Transformation
#                 data_log_transformed = np.log(data)

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#                 axes[0].set_title("Before Log Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot log-transformed data
#                 sns.histplot(data_log_transformed, kde=True, ax=axes[1], color='green', bins=10)
#                 axes[1].set_title("After Log Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Log-Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)


#     # 2. Square Root Transformation
#     with st.expander("2. Square Root Transformation", expanded=False):

#         col1, col2 = st.columns([1, 1])

#         with col1:

#             st.write("""
#             The square root transformation is used to reduce right skewness in data and is often applied to count data or data with Poisson distribution characteristics.
#             """)
#             st.write(
#                 """- $$y = \\sqrt{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation can only be applied to non-negative values."""
#             )
#             st.write("""
#             **Applications**: 
#             - Effective for stabilizing variance in count data, such as the number of events occurring.
#             - Used in fields such as ecology and epidemiology to normalize skewed data distributions.
            
#             **When to Use**: 
#             - When dealing with count data or data that is right-skewed.
            
#             **Limitations**: 
#             - Cannot be applied to negative values.
#             - May not adequately normalize heavily skewed data.
#             """)

#         with col2:

#             if st.checkbox("Apply Square Root Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')])
#                     if any(data < 0):
#                         st.error("Square root transformation requires all values to be non-negative. Please modify your input.")
#                         st.stop()
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Square Root Transformation
#                 data_sqrt_transformed = np.sqrt(data)

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#                 axes[0].set_title("Before Square Root Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot square root-transformed data
#                 sns.histplot(data_sqrt_transformed, kde=True, ax=axes[1], color='purple', bins=10)
#                 axes[1].set_title("After Square Root Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Square Root-Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

#     # 3. Reciprocal Transformation
#     with st.expander("3. Reciprocal Transformation", expanded=False):

#         col1, col2 = st.columns([1,1])

#         with col1:

#             st.write("""
#             The reciprocal transformation is used to reduce right skewness and is effective for data with outliers. It can drastically change the distribution.
#             """)
#             st.write(
#                 """- $$y = \\frac{1}{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation is valid for positive values only, and it can create extreme values for values near zero."""
#             )
#             st.write("""
#             **Applications**: 
#             - Commonly used in situations where the data contains extreme values or outliers, such as in financial datasets.
#             - Helpful in normalization for certain statistical analyses and regression models.
            
#             **When to Use**: 
#             - When extreme values exist in the data that need to be minimized.
            
#             **Limitations**: 
#             - Cannot be applied to zero or negative values, which can lead to undefined or infinite results.
#             - The transformation may introduce more variability into the data.
#             """)

#         with col2:
            
#             if st.checkbox("Apply Reciprocal Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area(
#                     "Enter your data (comma-separated positive values):",
#                     "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10"
#                 )

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                     # Ensure all values are positive (required for reciprocal transformation)
#                     if np.any(data <= 0):
#                         st.error("Reciprocal transformation requires all input values to be strictly positive.")
#                         st.stop()
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Reciprocal Transformation
#                 data_transformed = 1 / data.flatten()

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#                 axes[0].set_title("Before Reciprocal Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot Reciprocal Transformed data
#                 sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
#                 axes[1].set_title("After Reciprocal Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Reciprocal Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)



#     # 4. Exponential Transformation
#     with st.expander("4. Exponential Transformation", expanded=False):

#         col1, col2 = st.columns([2, 1])

#         with col1:

#             st.write("""
#             The exponential transformation can be used to transform data to a higher scale, which can be useful for models that require positive data.
#             """)
#             st.write(
#                 """- $$y = e^{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation increases the values, making it suitable for certain modeling contexts."""
#             )
#             st.write("""
#             **Applications**: 
#             - Used in growth models, such as population growth or compound interest calculations.
#             - Can help in transforming linear relationships into exponential ones for regression analysis.
            
#             **When to Use**: 
#             - When modeling processes that exhibit exponential growth.
            
#             **Limitations**: 
#             - Can cause overflow with large values of $$X$$.
#             - Does not address skewness in the data.
#             """)
            
#         with col2:

#             if st.checkbox("Apply Exponential Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')])
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Exponential Transformation
#                 data_exp_transformed = np.exp(data)

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='green', bins=10)
#                 axes[0].set_title("Before Exponential Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot exponential-transformed data
#                 sns.histplot(data_exp_transformed, kde=True, ax=axes[1], color='red', bins=10)
#                 axes[1].set_title("After Exponential Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Exponentially Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)


#     # 5. Box-Cox Transformation
#     with st.expander("5. Box-Cox Transformation", expanded=False):

#         col1, col2 = st.columns([2, 1])

#         with col1:

#             st.subheader("")
#             st.write("""
#             The Box-Cox transformation is a family of power transformations that is defined for positive values. It helps stabilize variance and make the data more closely resemble a normal distribution.
#             """)
#             st.write(
#                 """- $$y(\\lambda) = \\begin{cases} \\frac{y^{\\lambda} - 1}{\\lambda} & \\text{if } \\lambda \\neq 0 \\\\ \\log(y) & \\text{if } \\lambda = 0 \\end{cases}$$, where $$y$$ is the original value and $$\\lambda$$ is the transformation parameter that can be optimized. This transformation is applicable only to positive values."""
#             )
#             st.write("""
#             **Applications**: 
#             - Frequently used in linear regression to satisfy the assumptions of normality and homoscedasticity.
#             - Effective in transforming highly skewed data to meet model requirements.
            
#             **When to Use**: 
#             - When data is strictly positive and requires normalization for statistical tests.
            
#             **Limitations**: 
#             - Only applicable to positive values; cannot handle zero or negative values.
#             - Requires careful selection of the $$\\lambda$$ parameter.
#             """)

#     with col2:

#         if st.checkbox("Apply Box-Cox Transformation"):

#             # Sidebar for Input Data
#             st.header("Input Data")
#             data_input = st.text_area(
#                 "Enter your data (comma-separated positive values):",
#                 "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10"
#             )

#             # Convert input data to a NumPy array
#             try:
#                 data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 # Ensure all values are positive (required for Box-Cox)
#                 if np.any(data <= 0):
#                     st.error("Box-Cox transformation requires all input values to be strictly positive.")
#                     st.stop()
#             except ValueError:
#                 st.error("Please enter valid comma-separated numerical values.")
#                 st.stop()

#             # Preprocessing: Box-Cox Transformation
#             from scipy.stats import boxcox

#             data = data.flatten()  # Flatten for Box-Cox function
#             data_transformed, lambda_val = boxcox(data)

#             # Create a single figure with two subplots
#             fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

#             # Plot original data
#             sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#             axes[0].set_title("Before Box-Cox Transformation", fontsize=14, fontweight='bold')
#             axes[0].set_xlabel("Original Values", fontsize=12)
#             axes[0].set_ylabel("Density", fontsize=12)

#             # Plot Box-Cox Transformed data
#             sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
#             axes[1].set_title("After Box-Cox Transformation", fontsize=14, fontweight='bold')
#             axes[1].set_xlabel("Box-Cox Transformed Values", fontsize=12)
#             axes[1].set_ylabel("Density", fontsize=12)

#             # Display the plots in Streamlit
#             st.pyplot(fig)

#             # Display lambda value used in the transformation
#             st.write(f"Lambda value used for Box-Cox Transformation: {lambda_val:.4f}")


#     # Yeo-Johnson Transformation
#     with st.expander("6. Yeo-Johnson Transformation", expanded=False):

#         col1, col2 = st.columns([2, 1])

#         with col1:

#             st.write("""
#             ### 

#             - **Definition**: The Yeo-Johnson transformation is a modification of the Box-Cox transformation that allows for both positive and negative values. It is designed to handle data that includes zero or negative numbers.
#             """)
#             st.write(
#                 """- $$y(\\lambda) = \\begin{cases} \\frac{(y + 1)^{\\lambda} - 1}{\\lambda} & \\text{if } y \\geq 0 \text{ and } \\lambda \\neq 0 \\\\ \\log(y + 1) & \\text{if } y \\geq 0 \text{ and } \\lambda = 0 \\\\ -\\frac{(-y + 1)^{2 - \\lambda} - 1}{2 - \\lambda} & \\text{if } y < 0 \text{ and } \\lambda \\neq 2 \\\\ -\\log(-y + 1) & \\text{if } y < 0 \text{ and } \\lambda = 2 \\end{cases}$$, where $$y$$ is the original value and $$\\lambda$$ is the transformation parameter."""
#             )
#             st.write("""
#             **Applications**: 
#             - Used in regression modeling where the dataset contains both positive and negative values, allowing for a more flexible transformation.
#             - Common in machine learning preprocessing steps to improve model performance.
            
#             **When to Use**: 
#             - When working with data that contains both positive and negative values and requires normalization.
            
#             **Limitations**: 
#             - Requires tuning of the $$\\lambda$$ parameter, which may complicate the modeling process.
#             - May not be effective for data that is already normally distributed.
#             """)

#         with col2:

#             if st.checkbox("Apply Yeo-Johnson Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values) : ", "\n 1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Yeo-Johnson Transformation
#                 from sklearn.preprocessing import PowerTransformer

#                 scaler = PowerTransformer(method='yeo-johnson')  # 'yeo-johnson' transformation
#                 data_transformed = scaler.fit_transform(data)

#                 # Flatten for visualization
#                 data = data.flatten()
#                 data_transformed = data_transformed.flatten()

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#                 axes[0].set_title("Before Yeo-Johnson Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot Yeo-Johnson transformed data
#                 sns.histplot(data_transformed, kde=True, ax=axes[1], color='orange', bins=10)
#                 axes[1].set_title("After Yeo-Johnson Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Yeo-Johnson Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

#     # Quantile Transformation
#     with st.expander("7. Quantile Transformation", expanded=False):

#         col1, col2 = st.columns([2, 1])

#         with col1:

#             st.write("""
#             ### 
#             - **Definition**: Quantile transformation transforms features to follow a uniform or normal distribution by ranking the data and assigning values based on quantiles.
#             """)
#             st.write(
#                 """- The transformation maps the original data to quantile values of the desired distribution, which can be uniform or normal."""
#             )
#             st.write("""
#             **Applications**: 
#             - Effective in preprocessing for machine learning algorithms that assume normally distributed data.
#             - Helps improve model performance, particularly for algorithms sensitive to data distribution.
            
#             **When to Use**: 
#             - When the data has a non-Gaussian distribution and you want to transform it to resemble a Gaussian distribution.
            
#             **Limitations**: 
#             - Can distort the relationships between features.
#             - May not be effective on datasets with outliers, though it can mitigate their effects.
#             """)

#         with col2:

#             if st.checkbox("Apply Quantile Transformation"):

#                 # Sidebar for Input Data
#                 st.header("Input Data")
#                 data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10")

#                 # Convert input data to a NumPy array
#                 try:
#                     data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
#                 except ValueError:
#                     st.error("Please enter valid comma-separated numerical values.")
#                     st.stop()

#                 # Preprocessing: Quantile Transformation
#                 quantile_transformer = QuantileTransformer(output_distribution='normal', random_state=42)
#                 data_transformed = quantile_transformer.fit_transform(data)

#                 # Flatten for visualization
#                 data = data.flatten()
#                 data_transformed = data_transformed.flatten()

#                 # Create a single figure with two subplots
#                 fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

#                 # Plot original data
#                 sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
#                 axes[0].set_title("Before Quantile Transformation", fontsize=14, fontweight='bold')
#                 axes[0].set_xlabel("Original Values", fontsize=12)
#                 axes[0].set_ylabel("Density", fontsize=12)

#                 # Plot Quantile Transformed data
#                 sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
#                 axes[1].set_title("After Quantile Transformation", fontsize=14, fontweight='bold')
#                 axes[1].set_xlabel("Quantile Transformed Values", fontsize=12)
#                 axes[1].set_ylabel("Density", fontsize=12)

#                 # Display the plots in Streamlit
#                 st.pyplot(fig)

   



import streamlit as st
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler, QuantileTransformer
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Page Configuration
# st.set_page_config(layout="wide")

def run():
    st.title("Data Scaling and Transformation Techniques")

    st.write("In the world of data analysis and machine learning, preprocessing data is crucial for building effective models. One of the key aspects of preprocessing is understanding how to properly scale and transform your data. This blog post will dive deep into these concepts, their importance, and practical applications, complete with code examples to illustrate their use.")

    st.markdown("""
    ### Why Scaling and Transformations Matter
    Scaling and transforming data is crucial in data preprocessing, as it can significantly impact model performance. It helps:
    - Normalize feature ranges for comparability, especially in distance-based algorithms.
    - Stabilize variance and reduce skewness in data distribution.
    - Enhance model performance and convergence speed for gradient-based algorithms.
    """)

    # Scaling Techniques
    st.header("Scaling Techniques")

    # 1. Min-Max Scaling
    with st.expander("1. Min-Max Scaling (Normalization)", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.write("""
            Min-Max scaling rescales features to a specific range, usually [0, 1]. It is useful when features have different ranges but need to be compared on the same scale.
            """)

            # Formula and explanation for Min-Max Scaling
            st.write(
                """- $$X_{scaled} = \\frac{X - X_{min}}{X_{max} - X_{min}}$$, where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, $$X_{min}$$ is the minimum value of the feature, and $$X_{max}$$ is the maximum value of the feature. This transformation ensures that all features are on the same scale."""
            )

            st.write("""
            - **Scaling Range**: The resulting scaled values will fall within the range of 0 and 1, making it easier to compare features and aiding algorithms that require normalized input.

            - **Sensitivity to Outliers**: Min-Max scaling is sensitive to outliers; if the minimum and maximum values are significantly influenced by outliers, the scaled values of other data points will be compressed into a small range.

            - **Applications**: This method is commonly used in scenarios where the model expects data within a bounded range, such as in neural networks and algorithms that utilize distance measures.
            """)

        with col2:
            if st.checkbox("Apply Min-Max Scaling", key='min_max_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='min_max_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Min-Max Scaling
                scaler = MinMaxScaler()
                data_scaled = scaler.fit_transform(data)

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
                axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Indexes", fontsize=12)

                # Plot scaled data
                sns.scatterplot(x=data_scaled.flatten(), y=range(len(data_scaled)), ax=axes[1])
                axes[1].set_title("After Preprocessing", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Scaled Values", fontsize=12)
                # Display the plots in Streamlit
                st.pyplot(fig)

    # 2. Mean Normalization
    with st.expander("2. Mean Normalization", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.write("""
            Mean normalization transforms features to center around zero, typically within a range of -1 to 1. This helps stabilize the learning process, especially for models sensitive to feature scales.
            """)

            # Formula and explanation for Mean Normalization
            st.write(
                """- $$X_{normalized} = \\frac{X - \\mu}{X_{max} - X_{min}}$$, where $$X_{normalized}$$ is the normalized value, $$X$$ is the original value, $$\\mu$$ is the mean of the feature, $$X_{min}$$ is the minimum, and $$X_{max}$$ is the maximum. This formula ensures the data has a mean of zero and lies within a defined range.
                """
            )

            st.write("""
            - **Centering Around Zero**: After applying mean normalization, data points will center around zero. This is particularly useful for gradient-based optimization, as it helps models converge faster.

            - **Reducing Bias**: By adjusting features to have similar means, mean normalization minimizes biases due to differing feature scales, improving model performance in certain cases.

            - **Applications**: Mean normalization is commonly used in linear regression and other algorithms where centering features around zero makes the model more stable.
            """)

        with col2:
            if st.checkbox("Apply Mean Normalization", key='mean_norm_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='mean_norm_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Mean Normalization
                data_mean = np.mean(data)
                data_range = np.max(data) - np.min(data)
                data_normalized = (data - data_mean) / data_range

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
                axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Indexes", fontsize=12)

                # Plot normalized data
                sns.scatterplot(x=data_normalized.flatten(), y=range(len(data_normalized)), ax=axes[1])
                axes[1].set_title("After Mean Normalization", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Normalized Values", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 3. Max Absolute Scaling
    with st.expander("3. Max Absolute Scaling", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.subheader("")
            st.write("""
            Max absolute scaling is a scaling technique that scales each feature by its maximum absolute value. This transforms the data into a range between -1 and 1 while maintaining the sparsity of the data.
            """)

            # Formula and explanation for Max Absolute Scaling
            st.write(
                """- $$X_{scaled} = \\frac{X}{|X_{max}|}$$, where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, and $$|X_{max}|$$ is the maximum absolute value of the feature. This method scales the data to a range between -1 and 1 while maintaining the sparsity of the data."""
            )

            st.write("""
            - **Handling Sparse Data**: Max absolute scaling is particularly effective for sparse data (data with many zero values) as it maintains the zero entries. 

            - **Range of Values**: The values after max absolute scaling will fall within the range of -1 to 1, making it easier to compare features that are in different scales.

            - **Applications**: This method is commonly used in machine learning models where data sparsity is important, such as with some types of regression models and neural networks.
            """)

        with col2:
            if st.checkbox("Apply Max Absolute Scaling", key='max_abs_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='max_abs_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Max Absolute Scaling
                max_abs_value = np.max(np.abs(data))
                data_max_abs_scaled = data / max_abs_value

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
                axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Indexes", fontsize=12)

                # Plot scaled data
                sns.scatterplot(x=data_max_abs_scaled.flatten(), y=range(len(data_max_abs_scaled)), ax=axes[1])
                axes[1].set_title("After Max Absolute Scaling", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Scaled Values", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 4. Standardization (Z-score Normalization)
    with st.expander("4. Standardization (Z-score Normalization)", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.write("""
            Standardization, also known as Z-score normalization, is a technique used to center and scale data. It transforms the data such that its mean is 0 and its standard deviation is 1. This is useful for datasets where the features have different units or scales.

            - **Formula**: The formula for standardization is given by:
            """)

            # Centered LaTeX equation
            st.write(
                """- $$Z = \\frac{X - \\mu}{\\sigma}$$, where $$Z$$ is the standardized value, $$X$$ is the original value, $$\\mu$$ is the mean of the feature, and $$\\sigma$$ is the standard deviation. This transformation helps in comparing features that are on different scales."""
            )

            st.write("""
            - **Preservation of Distribution**: Unlike Min-Max scaling, which compresses data into a fixed range, standardization preserves the distribution of the data. This means that if the original data follows a Gaussian distribution, the standardized data will also follow a Gaussian distribution with a mean of 0 and a standard deviation of 1.

            - **Robustness to Outliers**: While standardization is sensitive to outliers, as they can affect the mean and standard deviation, it is generally more robust than Min-Max scaling in terms of preserving the relationships between values in a dataset. This is particularly important in algorithms that assume normal distribution.

            - **Applications**: Standardization is particularly useful in machine learning algorithms that rely on distance metrics (like K-Nearest Neighbors or Support Vector Machines) and in gradient-based optimization methods (like neural networks). It helps in accelerating convergence during training and improves the overall performance of the model by ensuring all features contribute equally.
            """)

        with col2:
            if st.checkbox("Apply Z-Score Normalization", key='z_score_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='z_score_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Z-Score Normalization
                mean = np.mean(data)
                std_dev = np.std(data)
                if std_dev == 0:
                    st.error("Standard deviation is zero, Z-Score Normalization cannot be applied.")
                    st.stop()
                data_z_score = (data - mean) / std_dev

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
                axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Indexes", fontsize=12)

                # Plot normalized data
                sns.scatterplot(x=data_z_score.flatten(), y=range(len(data_z_score)), ax=axes[1])
                axes[1].set_title("After Z-Score Normalization", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Z-Score Values", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 5. Robust Scaling
    with st.expander("5. Robust Scaling", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.write("""
            Robust scaling is a technique that scales the features by removing the median and scaling them according to the Interquartile Range (IQR). It is particularly useful for datasets with outliers, as it reduces their influence.
            """)

            # Formula and explanation for Robust Scaling
            st.write(
                """- $$X_{scaled} = \\frac{X - Q_2}{Q_3 - Q_1}$$, where $$X_{scaled}$$ is the scaled value, $$X$$ is the original value, $$Q_2$$ is the median, $$Q_1$$ is the first quartile, and $$Q_3$$ is the third quartile. This method effectively scales the data while reducing the influence of outliers."""
            )

            st.write("""
            - **Robustness to Outliers**: Because it uses the median and IQR for scaling, robust scaling is less affected by outliers compared to Min-Max or standard scaling. This makes it suitable for datasets with extreme values.

            - **Distribution Preservation**: Unlike Min-Max scaling, which compresses values into a fixed range, robust scaling maintains the relationships between the values.

            - **Applications**: Robust scaling is particularly useful in scenarios where the dataset contains outliers or when dealing with data that follows a non-Gaussian distribution.
            """)

        with col2:
            if st.checkbox("Apply Robust Scaling", key='robust_scaling_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='robust_scaling_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Robust Scaling
                median = np.median(data)
                q1 = np.percentile(data, 25)
                q3 = np.percentile(data, 75)
                iqr = q3 - q1  # Interquartile Range
                if iqr == 0:
                    st.error("IQR is zero, Robust Scaling cannot be applied.")
                    st.stop()
                data_robust_scaled = (data - median) / iqr

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.scatterplot(x=data.flatten(), y=range(len(data)), ax=axes[0])
                axes[0].set_title("Before Preprocessing", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Indexes", fontsize=12)

                # Plot scaled data
                sns.scatterplot(x=data_robust_scaled.flatten(), y=range(len(data_robust_scaled)), ax=axes[1])
                axes[1].set_title("After Robust Scaling", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Scaled Values", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # Transformations
    st.header("Transformations")
    st.markdown("Transformations adjust the data distribution. Here are some common methods:")

    # 1. Log Transformation
    with st.expander("1. Log Transformation", expanded=False):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.write("""
            The log transformation is used to reduce right skewness in data. It helps stabilize variance and make data more normally distributed.
            """)
            st.write(
                """- $$y = \\log(X)$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation is applicable only to positive values, as the logarithm of zero or negative numbers is undefined."""
            )
            st.write("""
            **Applications**: 
            - Useful for financial data where multiplicative relationships exist, such as income or prices.
            - Commonly used in regression models to meet the assumption of normally distributed residuals.

            **When to Use**: 
            - When the data is positively skewed and contains outliers.
            - When multiplicative relationships exist in the data.

            **Limitations**: 
            - Cannot be applied to zero or negative values.
            - May not be effective if the data is normally distributed.
            """)

        with col2:
            if st.checkbox("Apply Log Transformation", key='log_transform_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='log_transform_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')])
                    if any(data <= 0):
                        st.error("Log transformation requires all values to be greater than 0. Please modify your input.")
                        st.stop()
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Log Transformation
                data_log_transformed = np.log(data)

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Log Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot log-transformed data
                sns.histplot(data_log_transformed, kde=True, ax=axes[1], color='green', bins=10)
                axes[1].set_title("After Log Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Log-Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 2. Square Root Transformation
    with st.expander("2. Square Root Transformation", expanded=False):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.write("""
            The square root transformation is used to reduce right skewness in data and is often applied to count data or data with Poisson distribution characteristics.
            """)
            st.write(
                """- $$y = \\sqrt{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation can only be applied to non-negative values."""
            )
            st.write("""
            **Applications**: 
            - Effective for stabilizing variance in count data, such as the number of events occurring.
            - Used in fields such as ecology and epidemiology to normalize skewed data distributions.

            **When to Use**: 
            - When dealing with count data or data that is right-skewed.

            **Limitations**: 
            - Cannot be applied to negative values.
            - May not adequately normalize heavily skewed data.
            """)

        with col2:
            if st.checkbox("Apply Square Root Transformation", key='sqrt_transform_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='sqrt_transform_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')])
                    if any(data < 0):
                        st.error("Square root transformation requires all values to be non-negative. Please modify your input.")
                        st.stop()
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Square Root Transformation
                data_sqrt_transformed = np.sqrt(data)

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Square Root Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot square root-transformed data
                sns.histplot(data_sqrt_transformed, kde=True, ax=axes[1], color='purple', bins=10)
                axes[1].set_title("After Square Root Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Square Root-Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 3. Reciprocal Transformation
    with st.expander("3. Reciprocal Transformation", expanded=False):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.write("""
            The reciprocal transformation is used to reduce right skewness and is effective for data with outliers. It can drastically change the distribution.
            """)
            st.write(
                """- $$y = \\frac{1}{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation is valid for positive values only, and it can create extreme values for values near zero."""
            )
            st.write("""
            **Applications**: 
            - Commonly used in situations where the data contains extreme values or outliers, such as in financial datasets.
            - Helpful in normalization for certain statistical analyses and regression models.

            **When to Use**: 
            - When extreme values exist in the data that need to be minimized.

            **Limitations**: 
            - Cannot be applied to zero or negative values, which can lead to undefined or infinite results.
            - The transformation may introduce more variability into the data.
            """)

        with col2:
            if st.checkbox("Apply Reciprocal Transformation", key='reciprocal_transform_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area(
                    "Enter your data (comma-separated positive values):",
                    "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10",
                    key='reciprocal_transform_data_input'
                )

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                    # Ensure all values are positive (required for reciprocal transformation)
                    if np.any(data <= 0):
                        st.error("Reciprocal transformation requires all input values to be strictly positive.")
                        st.stop()
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Reciprocal Transformation
                data_transformed = 1 / data.flatten()

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Plot original data
                sns.histplot(data.flatten(), kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Reciprocal Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot Reciprocal Transformed data
                sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
                axes[1].set_title("After Reciprocal Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Reciprocal Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 4. Exponential Transformation
    with st.expander("4. Exponential Transformation", expanded=False):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.write("""
            The exponential transformation can be used to transform data to a higher scale, which can be useful for models that require positive data.
            """)
            st.write(
                """- $$y = e^{X}$$, where $$y$$ is the transformed value and $$X$$ is the original value. This transformation increases the values, making it suitable for certain modeling contexts."""
            )
            st.write("""
            **Applications**: 
            - Used in growth models, such as population growth or compound interest calculations.
            - Can help in transforming linear relationships into exponential ones for regression analysis.

            **When to Use**: 
            - When modeling processes that exhibit exponential growth.

            **Limitations**: 
            - Can cause overflow with large values of $$X$$.
            - Does not address skewness in the data.
            """)

        with col2:
            if st.checkbox("Apply Exponential Transformation", key='exp_transform_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='exp_transform_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')])
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Exponential Transformation
                data_exp_transformed = np.exp(data)

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='green', bins=10)
                axes[0].set_title("Before Exponential Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot exponential-transformed data
                sns.histplot(data_exp_transformed, kde=True, ax=axes[1], color='red', bins=10)
                axes[1].set_title("After Exponential Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Exponentially Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 5. Box-Cox Transformation
    with st.expander("5. Box-Cox Transformation", expanded=False):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("")
            st.write("""
            The Box-Cox transformation is a family of power transformations that is defined for positive values. It helps stabilize variance and make the data more closely resemble a normal distribution.
            """)
            st.write(
                """- $$y(\\lambda) = \\begin{cases} \\frac{y^{\\lambda} - 1}{\\lambda} & \\text{if } \\lambda \\neq 0 \\\\ \\log(y) & \\text{if } \\lambda = 0 \\end{cases}$$, where $$y$$ is the original value and $$\\lambda$$ is the transformation parameter that can be optimized. This transformation is applicable only to positive values."""
            )
            st.write("""
            **Applications**: 
            - Frequently used in linear regression to satisfy the assumptions of normality and homoscedasticity.
            - Effective in transforming highly skewed data to meet model requirements.

            **When to Use**: 
            - When data is strictly positive and requires normalization for statistical tests.

            **Limitations**: 
            - Only applicable to positive values; cannot handle zero or negative values.
            - Requires careful selection of the $$\\lambda$$ parameter.
            """)

        with col2:
            if st.checkbox("Apply Box-Cox Transformation", key='box_cox_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area(
                    "Enter your data (comma-separated positive values):",
                    "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10",
                    key='box_cox_data_input'
                )

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                    # Ensure all values are positive (required for Box-Cox)
                    if np.any(data <= 0):
                        st.error("Box-Cox transformation requires all input values to be strictly positive.")
                        st.stop()
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Box-Cox Transformation
                from scipy.stats import boxcox

                data = data.flatten()  # Flatten for Box-Cox function
                data_transformed, lambda_val = boxcox(data)

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Box-Cox Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot Box-Cox Transformed data
                sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
                axes[1].set_title("After Box-Cox Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Box-Cox Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

                # Display lambda value used in the transformation
                st.write(f"Lambda value used for Box-Cox Transformation: {lambda_val:.4f}")

    # 6. Yeo-Johnson Transformation
    with st.expander("6. Yeo-Johnson Transformation", expanded=False):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.write("""
            ### 

            - **Definition**: The Yeo-Johnson transformation is a modification of the Box-Cox transformation that allows for both positive and negative values. It is designed to handle data that includes zero or negative numbers.
            """)
            st.write(
                """- $$y(\\lambda) = \\begin{cases} \\frac{(y + 1)^{\\lambda} - 1}{\\lambda} & \\text{if } y \\geq 0 \text{ and } \\lambda \\neq 0 \\\\ \\log(y + 1) & \\text{if } y \\geq 0 \text{ and } \\lambda = 0 \\\\ -\\frac{(-y + 1)^{2 - \\lambda} - 1}{2 - \\lambda} & \\text{if } y < 0 \text{ and } \\lambda \\neq 2 \\\\ -\\log(-y + 1) & \\text{if } y < 0 \text{ and } \\lambda = 2 \\end{cases}$$, where $$y$$ is the original value and $$\\lambda$$ is the transformation parameter."""
            )
            st.write("""
            **Applications**: 
            - Used in regression modeling where the dataset contains both positive and negative values, allowing for a more flexible transformation.
            - Common in machine learning preprocessing steps to improve model performance.

            **When to Use**: 
            - When working with data that contains both positive and negative values and requires normalization.

            **Limitations**: 
            - Requires tuning of the $$\\lambda$$ parameter, which may complicate the modeling process.
            - May not be effective for data that is already normally distributed.
            """)

        with col2:
            if st.checkbox("Apply Yeo-Johnson Transformation", key='yeo_johnson_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='yeo_johnson_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Yeo-Johnson Transformation
                from sklearn.preprocessing import PowerTransformer

                scaler = PowerTransformer(method='yeo-johnson')  # 'yeo-johnson' transformation
                data_transformed = scaler.fit_transform(data)

                # Flatten for visualization
                data = data.flatten()
                data_transformed = data_transformed.flatten()

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Yeo-Johnson Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot Yeo-Johnson transformed data
                sns.histplot(data_transformed, kde=True, ax=axes[1], color='orange', bins=10)
                axes[1].set_title("After Yeo-Johnson Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Yeo-Johnson Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

    # 7. Quantile Transformation
    with st.expander("7. Quantile Transformation", expanded=False):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.write("""
            ### 
            - **Definition**: Quantile transformation transforms features to follow a uniform or normal distribution by ranking the data and assigning values based on quantiles.
            """)
            st.write(
                """- The transformation maps the original data to quantile values of the desired distribution, which can be uniform or normal."""
            )
            st.write("""
            **Applications**: 
            - Effective in preprocessing for machine learning algorithms that assume normally distributed data.
            - Helps improve model performance, particularly for algorithms sensitive to data distribution.

            **When to Use**: 
            - When the data has a non-Gaussian distribution and you want to transform it to resemble a Gaussian distribution.

            **Limitations**: 
            - Can distort the relationships between features.
            - May not be effective on datasets with outliers, though it can mitigate their effects.
            """)

        with col2:
            if st.checkbox("Apply Quantile Transformation", key='quantile_transform_checkbox'):
                # Input Data
                st.header("Input Data")
                data_input = st.text_area("Enter your data (comma-separated values):", "1, 2, 3, 3.6, 4.2, 4.7, 5, 7, 10", key='quantile_transform_data_input')

                # Convert input data to a NumPy array
                try:
                    data = np.array([float(i.strip()) for i in data_input.split(',')]).reshape(-1, 1)
                except ValueError:
                    st.error("Please enter valid comma-separated numerical values.")
                    st.stop()

                # Preprocessing: Quantile Transformation
                quantile_transformer = QuantileTransformer(output_distribution='normal', random_state=42)
                data_transformed = quantile_transformer.fit_transform(data)

                # Flatten for visualization
                data = data.flatten()
                data_transformed = data_transformed.flatten()

                # Create a single figure with two subplots
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))

                # Plot original data
                sns.histplot(data, kde=True, ax=axes[0], color='blue', bins=10)
                axes[0].set_title("Before Quantile Transformation", fontsize=14, fontweight='bold')
                axes[0].set_xlabel("Original Values", fontsize=12)
                axes[0].set_ylabel("Density", fontsize=12)

                # Plot Quantile Transformed data
                sns.histplot(data_transformed, kde=True, ax=axes[1], color='green', bins=10)
                axes[1].set_title("After Quantile Transformation", fontsize=14, fontweight='bold')
                axes[1].set_xlabel("Quantile Transformed Values", fontsize=12)
                axes[1].set_ylabel("Density", fontsize=12)

                # Display the plots in Streamlit
                st.pyplot(fig)

if __name__ == '__main__':
    run()
