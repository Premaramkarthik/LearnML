import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Helper function to plot small matrix with values inside
def plot_matrix_with_numbers(matrix, title):
    fig, ax = plt.subplots(figsize=(1.5, 1.5))  # Small plot size
    ax.matshow(np.ones_like(matrix), cmap="gray")  # Gray grid background for layout

    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, f"{val}", ha="center", va="center", color="black", fontsize=8)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10)
    return fig

def matrix_operations():
    st.title("Matrix Operations: The Heart of Machine Learning")

    with st.expander("Matrix Addition and Subtraction", expanded=True):
        st.subheader("Matrix Addition and Subtraction")

        st.write("""
            **The Intuition**: Imagine you’re blending two recipes. Each matrix represents the quantities of ingredients for a recipe. 
            Adding the matrices gives you a combined recipe, while subtracting them shows their differences.

            **In Machine Learning**:
            - **Addition**: Combine different datasets, aggregate information, or update parameters.
            - **Subtraction**: Compute differences, such as errors between predictions and actual values.
        """)

        # Define example matrices
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])

        # Display matrices in columns
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix A:")
            plot_matrix_with_numbers(A, "Matrix A")
        with col2:
            st.latex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix B:")
            plot_matrix_with_numbers(B, "Matrix B")
        with col2:
            st.latex(r"B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")

        # Perform addition and subtraction
        sum_matrix = A + B
        diff_matrix = A - B

        st.write("### Results:")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix A + Matrix B:")
            plot_matrix_with_numbers(sum_matrix, "Addition Result")
        with col2:
            st.latex(r"A + B = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix A - Matrix B:")
            plot_matrix_with_numbers(diff_matrix, "Subtraction Result")
        with col2:
            st.latex(r"A - B = \begin{bmatrix} -4 & -4 \\ -4 & -4 \end{bmatrix}")

    # Scalar Multiplication Section
    with st.expander("Scalar Multiplication: Scaling Matrices", expanded=True):
        st.subheader("Scaling with Scalars")

        st.write("""
            **The Intuition**: Imagine you’re doubling the quantities in a recipe. Every ingredient (matrix element) gets multiplied 
            by the same number (scalar). 

            **In Machine Learning**:
            - Scale features to normalize data (e.g., all values between 0 and 1).
            - Control the learning rate during optimization.
        """)

        # Define matrix and scalar
        C = np.array([[2, 4], [6, 8]])
        scalar = st.slider("Choose a scalar value to multiply with:", 1, 10, 2)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Original Matrix:")
            plot_matrix_with_numbers(C, "Original Matrix")
        with col2:
            st.latex(r"C = \begin{bmatrix} 2 & 4 \\ 6 & 8 \end{bmatrix}")

        scaled_matrix = scalar * C

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write(f"Matrix scaled by {scalar}:")
            plot_matrix_with_numbers(scaled_matrix, f"Matrix Scaled by {scalar}")
        with col2:
            st.latex(rf"\times C = \begin{{bmatrix}} {scaled_matrix[0, 0]} & {scaled_matrix[0, 1]} \\ {scaled_matrix[1, 0]} & {scaled_matrix[1, 1]} \end{{bmatrix}}")


    # Dot Product Section
    with st.expander("Matrix Multiplication (Dot Product)", expanded=True):
        st.subheader("Matrix Multiplication: Combining Information")

        st.write("""
            **The Intuition**: Suppose you’re matching job candidates to projects. 
            - Rows in the first matrix (candidates) represent their skills.
            - Columns in the second matrix (projects) represent skill requirements.

            By multiplying these matrices, you can determine how well each candidate matches each project.
        """)

        # Define matrices for multiplication
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix A:")
            plot_matrix_with_numbers(A, "Matrix A")
        with col2:
            st.latex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Matrix B:")
            plot_matrix_with_numbers(B, "Matrix B")
        with col2:
            st.latex(r"B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}")

        result = A @ B

        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("Result of A @ B:")
            plot_matrix_with_numbers(result, "Matrix Multiplication Result")
        with col2:
            st.latex(r"A \times B = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}")

matrix_operations()
