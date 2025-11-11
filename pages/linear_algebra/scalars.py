import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function for Scalars Section with Detailed Examples and Interactive Plotly Visualizations
def scalars_section():
    st.header("Scalars")
    
    st.write("""
    ### What is a Scalar?
    In mathematics and machine learning, a scalar is a single number. Unlike vectors, which have both magnitude and direction, 
    scalars only represent magnitude. Scalars can be positive, negative, or zero and serve as constants in equations, modifying 
    the magnitude of other values without introducing any directional component.
    """)

    st.write("""
    ### The Role of Scalars in Machine Learning
    Scalars are crucial in many machine learning algorithms. They adjust the scale of vectors or matrices, acting as multipliers 
    in many operations. For example, in gradient descent, the **learning rate** is a scalar that controls the step size for 
    updates, determining how fast or slow an algorithm learns. A well-chosen scalar (learning rate) can help a model converge 
    quickly and accurately.
    
    Scalars are also used to **scale features** in preprocessing, helping to normalize the data for better model performance. 
    Scaling helps models to learn more effectively by standardizing the magnitude of different features, especially when they 
    have varying ranges.
    """)

    # Examples
    st.write("### Examples:")
    st.write("- **Example 1**: Multiplying a vector `[2, 3]` by scalar `5` to get `[10, 15]` — here, `5` amplifies the magnitude without changing direction.")
    st.write("- **Example 2**: In gradient descent, the learning rate is a scalar that adjusts how large each update step should be in the optimization process.")

    # Sidebar for interactive scalar input
    st.sidebar.header("Scalar and Vector Input")
    scalar = st.sidebar.slider("Select a Scalar (Scale Factor)", min_value=-10.0, max_value=10.0, value=5.0, step=0.5)
    x_component = st.sidebar.number_input("Vector X Component", value=2.0)
    y_component = st.sidebar.number_input("Vector Y Component", value=3.0)
    
    # Define the vector and scaled vector
    vector = np.array([x_component, y_component])
    scaled_vector = scalar * vector

    # Interactive Plot for Scalar and Vector Scaling
    fig = go.Figure()

    # Original vector
    fig.add_trace(go.Scatter(
        x=[0, vector[0]], 
        y=[0, vector[1]], 
        mode="lines+markers+text", 
        name="Original Vector",
        text=["", f"({vector[0]}, {vector[1]})"],
        textposition="top center",
        line=dict(color="green", width=3)
    ))

    # Scaled vector
    fig.add_trace(go.Scatter(
        x=[0, scaled_vector[0]], 
        y=[0, scaled_vector[1]], 
        mode="lines+markers+text", 
        name="Scaled Vector",
        text=["", f"({scaled_vector[0]}, {scaled_vector[1]})"],
        textposition="top center",
        line=dict(color="red", width=3, dash="dot")
    ))

    fig.update_layout(
        title="Scalar Multiplication on a Vector",
        xaxis_title="X",
        yaxis_title="Y",
        width=500,
        height=400,
        showlegend=True,
        xaxis=dict(range=[-20, 20]),
        yaxis=dict(range=[-20, 20])
    )

    st.plotly_chart(fig)

    st.write(f"**Selected Scalar**: {scalar}")
    st.write(f"**Original Vector**: {vector}")
    st.write(f"**Scaled Vector (Result)**: {scaled_vector}")

    st.write("""
    ### Intuition Behind Scaling Vectors
    - **Scaling Up**: When the scalar is greater than 1, the vector's magnitude increases. Imagine a model where feature values 
      need to be more pronounced—scaling can emphasize their importance.
    - **Scaling Down**: When the scalar is between 0 and 1, it reduces the magnitude, effectively "shrinking" the vector. This 
      is useful for downplaying certain features or in **regularization** techniques where smaller coefficients are desired to 
      avoid overfitting.
    - **Negative Scalars**: If the scalar is negative, it flips the vector's direction. In machine learning, a flipped vector 
      may indicate an inverse relationship between features. For instance, in linear models, a negative coefficient (scalar) 
      for a feature indicates a decrease in the target variable as the feature increases.
      
    ### Why Scalars Matter in Data Science and Machine Learning
    - **Learning Rate**: Scalars like learning rates are crucial for optimizing model training. A high learning rate (large 
      scalar) speeds up learning but may overshoot optimal solutions, while a low learning rate can slow learning but lead to 
      better convergence.
    - **Normalization**: In feature scaling, scalars standardize feature ranges, improving model training by reducing 
      dependencies on specific feature magnitudes.
    - **Regularization**: Scalars apply penalties to model weights, encouraging simpler models that generalize better.
    
    These concepts are fundamental to understanding how different scalar values affect model behavior and performance.
    """)

scalars_section()
