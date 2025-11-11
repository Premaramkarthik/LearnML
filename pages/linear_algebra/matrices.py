import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def matrices():
    # Set up page title
    st.title("Understanding Matrices in Machine Learning")

    # Section 1: Introduction to Matrices
    with st.expander("What is a Matrix?", expanded=True):
        st.subheader("Matrix Fundamentals")
        
        st.write("""
            A matrix is a rectangular array of numbers arranged in rows and columns. In data science, matrices are essential for 
            representing and manipulating data, enabling efficient computations and transformations. Here’s an example of a \(2 \times 3\) matrix:
        """)
        
        st.latex(r"""
            \mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}
        """)

        st.write("""
            **Key Terms:**
            - **Dimensions**: Matrices have dimensions defined by the number of rows and columns. A \(2 \times 3\) matrix has 2 rows and 3 columns.
            - **Square Matrix**: A matrix with an equal number of rows and columns, like a \(3 \times 3\) matrix.
            - **Identity Matrix**: A special square matrix with 1s on its diagonal and 0s elsewhere, useful in many machine learning algorithms.
        """)

    # Example visualization of a matrix
    matrix_example = np.array([[1, 2, 3], [4, 5, 6]])
    fig, ax = plt.subplots()
    ax.matshow(matrix_example, cmap="Blues")
    for (i, j), val in np.ndenumerate(matrix_example):
        ax.text(j, i, f'{val}', ha='center', va='center', color="black")

    plt.title("Example Matrix Visualization")
    st.pyplot(fig)


    # Section 2: Importance of Matrices in ML
    with st.expander("Why Do We Use Matrices in Machine Learning?", expanded=True):
        st.subheader("The Role of Matrices in ML")
        
        st.write("""
            Matrices provide a powerful way to handle and manipulate data in machine learning:
            
            - **Data Representation**: Datasets, images, and other structured data can be represented as matrices, making it easier to work with large amounts of data.
            - **Efficient Computation**: Matrix operations, such as addition and multiplication, allow for faster and more efficient calculations.
            - **Transformation and Scaling**: Matrices help scale and transform data, crucial in techniques like Principal Component Analysis (PCA).
        """)

        # Add columns to illustrate examples
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Tabular Data**")
            st.write("""
                For tabular datasets, each row is a sample, and each column is a feature. For example, a dataset with age, height, and weight 
                as features can be represented as a \(N \times 3\) matrix, where \(N\) is the number of samples.
            """)
            data_matrix = np.array([[25, 180, 75], [30, 175, 80], [22, 168, 65]])
            st.write("Example Data Matrix:")
            st.write(data_matrix)

        with col2:
            st.markdown("**Image Data**")
            st.write("""
                For images, each pixel's intensity can be represented as an element in a matrix. A grayscale image can be stored 
                as a \(M \times N\) matrix, where each value represents the pixel intensity.
            """)

            # Example grayscale image matrix visualization
            image_matrix = np.random.rand(5, 5) * 255
            fig, ax = plt.subplots()
            ax.imshow(image_matrix, cmap="gray")
            plt.title("Example Grayscale Image Matrix")
            st.pyplot(fig)
    # Section 3: How Matrices are Used in ML Models
    with st.expander("Matrices in Model Computations and Neural Networks", expanded=True):
        st.subheader("How Matrices Power Machine Learning Models")

        st.write("""
            Matrices enable complex mathematical operations required in ML models, such as:
            
            - **Linear Algebra for Model Computations**: Operations like matrix multiplication help simplify model equations, especially in algorithms like linear regression.
            - **Neural Networks**: Matrices represent input vectors, weight matrices, and outputs in neural networks.
        """)

        # Visualizing a small neural network layer matrix multiplication
        try:
            input_vector = np.array([[2], [3]])  # Sample input
            weight_matrix = np.array([[0.5, 1.0], [1.5, -0.5]])  # Weights
            output = weight_matrix @ input_vector


            st.write("Matrix Multiplication in Neural Networks:")
            st.write("Input Vector:")
            st.write(input_vector)
            st.write("Weight Matrix:")
            st.write(weight_matrix)
            st.write("Output (after matrix multiplication):")
            st.write(output)
        except TypeError:
            print('Complex Roots')

        

        st.write("""
            This example shows how matrices handle the transformation of inputs to outputs, crucial in neural network layers.
        """)

    import plotly.graph_objects as go

    # Section 4: Matrices as Linear Transformations
    with st.expander("Matrices as Linear Transformations", expanded=True):
        st.subheader("Using Matrices for Data Transformation")

        st.write("""
            In machine learning, we often need to transform data. Matrices allow us to rotate, scale, or project data points in space. 
            This concept of linear transformation is the foundation of methods like Principal Component Analysis (PCA).
        """)

        # User input for transformation matrix
        st.write("Experiment with a 2D transformation matrix:")
        a = st.slider("a (scaling on x-axis)", -2.0, 2.0, 1.0, key="a")
        b = st.slider("b (shearing on x-axis)", -2.0, 2.0, 0.0, key="b")
        c = st.slider("c (shearing on y-axis)", -2.0, 2.0, 0.0, key="c")
        d = st.slider("d (scaling on y-axis)", -2.0, 2.0, 1.0, key="d")

        # Define the transformation matrix
        transformation_matrix = np.array([[a, b], [c, d]])

        # Original grid points
        x, y = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
        points = np.vstack([x.flatten(), y.flatten()])

        # Transformed points
        transformed_points = transformation_matrix @ points

        # Plot before and after transformation
        fig = go.Figure()

        # Original points
        fig.add_trace(go.Scatter(x=points[0], y=points[1], mode="markers", name="Original Points"))
        # Transformed points
        fig.add_trace(go.Scatter(x=transformed_points[0], y=transformed_points[1], mode="markers", name="Transformed Points"))

        fig.update_layout(
            title="2D Linear Transformation",
            xaxis_title="X-axis",
            yaxis_title="Y-axis",
            showlegend=True
        )
        st.plotly_chart(fig)

        st.write("""
            By adjusting the values in the transformation matrix, you can observe different transformations, 
            such as rotations, scalings, and shear transformations. In the next section, we’ll explore eigenvalues and eigenvectors, 
            which allow us to understand how transformations impact data and find the best-fitting axes.
        """)


matrices()