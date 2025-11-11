# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run():
    # Page title
    st.title("Supervised Learning")


    # Introduction section
    #st.subheader("Introduction to Supervised Learning")
    st.info("""
    Imagine you're training a dog to follow commands like sitting or rolling over. You give it a command (input), and when it performs correctly, you reward it (output).
    Similarly, in supervised learning, a model learns to map inputs (X) to desired outputs (Y) using labeled data. The goal is for the model to make accurate predictions when it encounters similar data.
    """)


    # # Labeled Data Explanation
    # st.subheader("How Labeled Data Works in Supervised Learning")
    # st.write("Labeled data is essential in supervised learning. Here’s a sample dataset representing a loan approval task with labeled data:")


    # # Create sample data to illustrate labeled data
    # data = {
    #     'Applicant Income': [50000, 30000, 70000, 40000, 100000],
    #     'Credit Score': [750, 600, 800, 550, 900],
    #     'Loan Approved (Y/N)': ['Yes', 'No', 'Yes', 'No', 'Yes']
    # }
    # df = pd.DataFrame(data)
    # st.table(df)


    # Explanation of Supervised Learning Steps
    st.subheader("How Supervised Learning Works")
    st.markdown("""
    1. **Training with Labeled Data**: The model learns patterns from inputs and outputs in labeled data.
    2. **Mapping Inputs to Outputs**: It identifies relationships (e.g., higher income and credit score relate to loan approval).
    3. **Testing and Prediction**: The model is evaluated on new data to ensure accuracy.
    4. **Continuous Improvement**: Models can improve with parameter tuning, refined data, or advanced algorithms.
    """)


    # Types of Supervised Learning Problems
    st.subheader("Types of Supervised Learning Problems")
    st.write("Supervised learning generally addresses two main types of problems: classification and regression.")


    # Create a table to differentiate classification and regression
    types_data = {
        'Type': ['Classification', 'Regression'],
        'Goal': [
            'Categorize data into classes (e.g., spam or not spam)',
            'Predict continuous values (e.g., housing prices based on features)'
        ],
        'Example': [
            'Email classification, image recognition',
            'Predicting stock prices, housing prices'
        ]
    }
    types_df = pd.DataFrame(types_data)
    st.table(types_df)


    # Title for the section
    st.subheader("Classification & Regression: Visual Representation")


    # Title of the app
    st.title("Supervised Learning Classification and Regression Visualizations")

    # Create a figure with two subplots arranged in 1 row, 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(3.6, 1.2))  # Decreased figure size by 40%
    fig.subplots_adjust(wspace=0.4)  # Adjust space between columns

    # Define new font sizes after a 40% reduction
    title_fontsize = 4.2  # 40% decrease from 6
    label_fontsize = 3.5  # 40% decrease from 5
    tick_fontsize = 3.5  # 40% decrease from 5

    # Classification Visualization
    ax1.bar(["Spam", "Not Spam"], [30, 70], color=["#FF6F61", "#6BAED6"])
    ax1.set_title("Classification: Email Spam Detection", fontweight='bold', fontsize=title_fontsize)  # Adjusted title fontsize
    ax1.tick_params(axis='x', labelsize=tick_fontsize)  # Set x ticks fontsize
    ax1.tick_params(axis='y', labelsize=tick_fontsize)  # Set y ticks fontsize

    # Regression Visualization
    x = [1000, 1500, 2000, 2500, 3000]  # Square footage
    y = [150000, 200000, 250000, 300000, 350000]  # House Prices
    ax2.plot(x, y, marker='o', color="#4C72B0")
    ax2.set_xlabel("Square Footage", fontsize=label_fontsize)  # Adjusted xlabel fontsize
    ax2.set_ylabel("House Price ($)", fontsize=label_fontsize)  # Adjusted ylabel fontsize
    ax2.set_title("Regression: Predicting House Prices", fontsize=title_fontsize, fontweight='bold')  # Adjusted title fontsize
    ax2.tick_params(axis='x', labelsize=tick_fontsize)  # Set x ticks fontsize
    ax2.tick_params(axis='y', labelsize=tick_fontsize) 


    # Show the plot in Streamlit
    st.pyplot(fig)


    # Real-World Example
    st.subheader("Real-World Example: Predicting Loan Approvals")
    st.write("""
    Imagine a bank wants to automate loan approvals. Using historical data on applicants and loan outcomes, a model can learn to predict whether a loan should be approved or denied.
    """)


    # Example table for real-world use case
    loan_example_data = {
        'Applicant Income': [30000, 40000, 60000, 80000],
        'Credit Score': [620, 680, 720, 810],
        'Loan Status (Predicted)': ['Denied', 'Approved', 'Approved', 'Approved']
    }
    loan_df = pd.DataFrame(loan_example_data)
    st.table(loan_df)


    # Advantages of Supervised Learning
    st.subheader("Advantages of Supervised Learning")
    st.markdown("""
    - High accuracy with labeled data
    - Effective for predictive tasks based on historical data
    - Widely applicable across various industries
    """)


    # Disadvantages of Supervised Learning
    st.subheader("Disadvantages of Supervised Learning")
    st.markdown("""
    - Requires large, accurately labeled datasets
    - Risk of overfitting on training data
    - May need substantial computation and tuning
    """)


    # Summary
    st.subheader("Summary")
    st.write("""
    Supervised learning involves training a model on labeled data to make predictions on new data. It's used widely for classification and regression tasks across industries,
    from spam detection to financial forecasting. While powerful, it relies on high-quality labeled data and tuning for optimal performance.
    """)



