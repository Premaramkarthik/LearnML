import streamlit as st
import numpy as np
import plotly.graph_objects as go
from numpy.linalg import eig

def apply_transformation(matrix, points):
    """Apply a linear transformation to a set of points."""
    return np.dot(matrix, points)

def generate_grid(x_range, y_range, step=1):
    """Generate a grid of points."""
    x = np.arange(x_range[0], x_range[1] + step, step)
    y = np.arange(y_range[0], y_range[1] + step, step)
    X, Y = np.meshgrid(x, y)
    grid_points = np.vstack([X.flatten(), Y.flatten()])
    return grid_points, X, Y

def plot_transformation(matrix, grid_points, X, Y, transformed_points):
    """Plot the original and transformed grid using Plotly, with better grid control."""
    fig = go.Figure()

    # Plot original grid (reduced density)
    for i in range(0, X.shape[0], 2):  # Reduce density by skipping some lines
        fig.add_trace(go.Scatter(
            x=grid_points[0, i*X.shape[1]:(i+1)*X.shape[1]],
            y=grid_points[1, i*X.shape[1]:(i+1)*X.shape[1]],
            mode='lines',
            line=dict(color='green', dash='solid'),
            showlegend=False
        ))
    for j in range(0, X.shape[1], 2):
        fig.add_trace(go.Scatter(
            x=grid_points[0, j::X.shape[1]],
            y=grid_points[1, j::X.shape[1]],
            mode='lines',
            line=dict(color='green', dash='solid'),
            showlegend=False
        ))

    fig.add_trace(go.Scatter(
        x=grid_points[0, :], y=grid_points[1, :],
        mode='markers', marker=dict(color='Green'), name='Original Grid'
    ))

    # Plot transformed grid
    for i in range(0, X.shape[0], 2):
        fig.add_trace(go.Scatter(
            x=transformed_points[0, i*X.shape[1]:(i+1)*X.shape[1]],
            y=transformed_points[1, i*X.shape[1]:(i+1)*X.shape[1]],
            mode='lines',
            line=dict(color='red'),
            showlegend=False
        ))
    for j in range(0, X.shape[1], 2):
        fig.add_trace(go.Scatter(
            x=transformed_points[0, j::X.shape[1]],
            y=transformed_points[1, j::X.shape[1]],
            mode='lines',
            line=dict(color='red'),
            showlegend=False
        ))

    fig.add_trace(go.Scatter(
        x=transformed_points[0, :], y=transformed_points[1, :],
        mode='markers', marker=dict(color='red'), name='Transformed Grid'
    ))

    # Set consistent axis range and equal aspect ratio
    fig.update_layout(
        xaxis=dict(title="X-axis", range=[-10, 10]),  # Adjust range as needed
        yaxis=dict(title="Y-axis", range=[-10, 10]),  # Adjust range as needed
        width=700, height=700,
        title="Linear Transformation of a Grid",
        legend_title="Legend",
        showlegend=True
    )

    fig.update_yaxes(scaleanchor="x", scaleratio=1)  # Maintain aspect ratio

    return fig



def matrix_to_latex(matrix):
    """Convert a matrix to a LaTeX formatted string."""
    return r"\begin{bmatrix}" + \
           r" \\ ".join([" & ".join(map(str, row)) for row in matrix]) + \
           r"\end{bmatrix}"

def linear_transformation_app():
    st.title("Matrix as Linear Transformation")
    
    st.write("""
        In linear algebra, a matrix represents a linear transformation, which is a function that maps vectors to other vectors while preserving the operations of vector addition and scalar multiplication. Linear transformations are fundamental in fields like computer graphics, physics, and machine learning.

        ### Key Concepts
        - **Transformation Matrix**: A matrix \( A \) defines a transformation that can scale, rotate, shear, or reflect points in a space.
        - **Basis Vectors**: The columns of a transformation matrix show how the standard basis vectors are transformed.
        - **Grid Transformation**: Applying a matrix to all points in a grid allows us to visualize its effect on the space.
        """)
    st.latex(r"""
    \mathbf{T}(\mathbf{v}) = A \mathbf{v}
    """)

    # Example matrices for transformation
    st.write("### Select a Transformation Matrix")
    transformation_options = {
        "Identity Matrix": np.array([[1, 0], [0, 1]]),
        "Scaling Matrix (2x)": np.array([[2, 0], [0, 2]]),
        "Rotation Matrix (45°)": np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)], 
                                           [np.sin(np.pi/4), np.cos(np.pi/4)]]),
        "Shear Matrix": np.array([[1, 1], [0, 1]]),
        "Reflection Matrix": np.array([[1, 0], [0, -1]]),
    }

    transformation_name = st.selectbox("Choose a transformation:", list(transformation_options.keys()))
    transformation_matrix = transformation_options[transformation_name]

    # Display matrix in LaTeX format
    st.write("**Selected Transformation Matrix:**")
    st.latex(matrix_to_latex(transformation_matrix))

    # Generate original grid
    grid_points, X, Y = generate_grid((-5, 5), (-5, 5), step=1)

    # Apply transformation
    transformed_points = apply_transformation(transformation_matrix, grid_points)

    # Plot original and transformed grids
    fig = plot_transformation(transformation_matrix, grid_points, X, Y, transformed_points)
    st.plotly_chart(fig)

linear_transformation_app()



st.title("Exploring Eigenvalues and Eigenvectors")

# Detailed Introduction
st.markdown("""
### What Are Eigenvalues and Eigenvectors?

At the heart of linear algebra lies the concept of **eigenvalues** and **eigenvectors**. These terms might seem intimidating at first, but they have a simple geometric interpretation:

- **Eigenvectors** are special directions that remain unchanged (except for scaling) under a given linear transformation.
- **Eigenvalues** represent the factor by which the eigenvector is stretched or compressed.

#### Why Are They Important?

In **machine learning**, eigenvalues and eigenvectors play a crucial role in:
- **Dimensionality Reduction (PCA)**: Eigenvectors help find the directions of maximum variance in data.
- **Feature Selection**: By understanding variance, we can retain only the most important features.
- **Graph Analysis**: Eigenvalues can describe the structure of networks.
- **Optimization Problems**: They help in solving linear systems and analyzing Hessians for convexity.

This tutorial explores their geometric meaning and visualizes their behavior in **2D** and **3D**.
""")

# Matrix Input Section
st.markdown("""
### Input a 2x2 Matrix
To understand eigenvalues and eigenvectors, we'll start by allowing you to input a simple 2x2 matrix. This matrix represents a linear transformation that acts on vectors in 2D space.

A 2x2 matrix can be written as:
\\[
A = \\begin{bmatrix}
a & b \\\\
c & d
\\end{bmatrix}
\\]
""")

# User Input for Matrix
a = st.number_input("Element [0,0]:", value=1.0, format="%.2f")
b = st.number_input("Element [0,1]:", value=2.0, format="%.2f")
c = st.number_input("Element [1,0]:", value=3.0, format="%.2f")
d = st.number_input("Element [1,1]:", value=4.0, format="%.2f")

matrix = np.array([[a, b], [c, d]])

st.markdown("### Your Matrix in LaTeX Form:")
st.latex(f"""
\\begin{{bmatrix}}
{a} & {b} \\\\
{c} & {d}
\\end{{bmatrix}}
""")

# Compute Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = eig(matrix)

# Detailed Explanation
st.markdown("""
### **What Do These Values Mean?**

When we decompose a matrix into its eigenvalues and eigenvectors, we essentially solve the equation:
\\[
A \\mathbf{v} = \\lambda \\mathbf{v}
\\]
Where:
- \\(A\\) is our transformation matrix.
- \\(\\mathbf{v}\\) is an eigenvector (unchanged direction under transformation).
- \\(\\lambda\\) is an eigenvalue (scaling factor for \\(\\mathbf{v}\\)).

#### Steps to Find Eigenvalues and Eigenvectors:
1. **Solve the Characteristic Equation**:
   \\[
   \\text{det}(A - \\lambda I) = 0
   \\]
   This gives us the eigenvalues \\(\\lambda\\).

2. **Substitute Each Eigenvalue to Solve**:
   For each eigenvalue, solve \\((A - \\lambda I) \\mathbf{v} = 0\\) to find its eigenvector.

### **Results for Your Matrix**:
""")

# Display Computed Results
st.markdown(f"**Eigenvalues**: {eigenvalues}")
st.markdown("**Eigenvectors (in columns):**")
st.latex(f"""
\\begin{{bmatrix}}
{eigenvectors[0,0]:.2f} & {eigenvectors[0,1]:.2f} \\\\
{eigenvectors[1,0]:.2f} & {eigenvectors[1,1]:.2f}
\\end{{bmatrix}}
""")
# 2D Visualization of Eigenvectors and Transformation
st.markdown("""
### Geometric Interpretation in 2D

Eigenvectors point in directions that do not rotate under transformation. In the following plot:
- **Blue dots** represent the original grid.
- **Red dots** represent the transformed grid.
- **Green lines** are eigenvectors showing invariant directions.
""")

# Generate a grid for visualization
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)
grid_points = np.c_[X.flatten(), Y.flatten()]
transformed_points = grid_points @ matrix.T

# Plot using Plotly
fig = go.Figure()

# Original Grid
fig.add_trace(go.Scatter(x=grid_points[:, 0], y=grid_points[:, 1], mode='markers', name='Original Grid', marker=dict(size=5, color='blue')))
# Transformed Grid
fig.add_trace(go.Scatter(x=transformed_points[:, 0], y=transformed_points[:, 1], mode='markers', name='Transformed Grid', marker=dict(size=5, color='red')))

# Eigenvectors
for i in range(2):
    eig_vec = eigenvectors[:, i] * 10  # Scale eigenvector for display
    fig.add_trace(go.Scatter(x=[0, eig_vec[0]], y=[0, eig_vec[1]], mode='lines+markers', name=f'Eigenvector {i+1}', line=dict(color='green', width=4)))

fig.update_layout(title="2D Transformation with Eigenvectors", xaxis_title="X", yaxis_title="Y", legend_title="Legend")
st.plotly_chart(fig)
st.markdown("""
### Extending the Concept to 3D

Just like in 2D, eigenvectors in 3D remain invariant in direction under transformation, though now they operate in a higher-dimensional space. Below, we show a random 3D matrix with its eigenvectors and transformations.
""")

# Generate random 3D matrix and compute its eigenvalues/vectors
matrix_3d = np.random.rand(3, 3)
eigenvalues_3d, eigenvectors_3d = eig(matrix_3d)

fig3d = go.Figure()

# Plot 3D unit vectors and transformed vectors
unit_vectors = np.eye(3)

for i in range(3):
    # Original unit vectors
    fig3d.add_trace(go.Scatter3d(
        x=[0, unit_vectors[i, 0]],
        y=[0, unit_vectors[i, 1]],
        z=[0, unit_vectors[i, 2]],
        mode='lines',
        name=f'Axis {i+1}',
        line=dict(color='blue', width=3)
    ))
    # Eigenvectors in 3D
    eig_vec = eigenvectors_3d[:, i]
    fig3d.add_trace(go.Scatter3d(
        x=[0, eig_vec[0] * eigenvalues_3d[i]],
        y=[0, eig_vec[1] * eigenvalues_3d[i]],
        z=[0, eig_vec[2] * eigenvalues_3d[i]],
        mode='lines+markers',
        name=f'Eigenvector {i+1}',
        line=dict(color='green', width=4)
    ))

fig3d.update_layout(title="3D Transformation with Eigenvectors", scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
), legend_title="Legend")

st.plotly_chart(fig3d)
