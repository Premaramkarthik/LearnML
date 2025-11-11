import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def vectors_section():
    st.header("Vectors")
    st.write("""
    **Definition**: A vector is an ordered collection of numbers that can represent a data point or a feature in 
    machine learning. Vectors are mathematical objects that exist in a space defined by dimensions. In 2D, a vector can be represented as an ordered pair \([x, y]\), while in 3D, it is represented as \([x, y, z]\).

    Vectors are often used to represent data points in machine learning models, where each component corresponds to a feature value or a coordinate in some space. A vector not only has a magnitude (length) but also a direction.

    **Vector Notation**: A vector in \(n\)-dimensional space can be represented as:
    """)
    
    st.latex(r'\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}')

    st.write("""
    where \(v_1, v_2, ..., v_n\) are the components of the vector.

    In machine learning, vectors help describe everything from individual data points to weights in models.
    """)

    st.write("### Examples of Vectors:")
    st.write("- **Example 1**: A 2D vector \([3, 4]\) can represent the position of a point in 2-dimensional space.")
    st.write("- **Example 2**: A 3D vector \([1, -2, 5]\) could represent the RGB color components of a pixel.")
    
    # Using Columns for side-by-side plots
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 2D Vector Visualization:")
        st.write("This plot shows a 2D vector with components [3, 4], represented as an arrow in a 2-dimensional space.")
        
        # Plotting a 2D vector with Plotly
        fig_2d = go.Figure(data=[go.Scatter(x=[0, 3], y=[0, 4], mode='lines+markers', marker=dict(color='blue', size=10))])
        fig_2d.update_layout(
            title="2D Vector [3, 4]",
            xaxis_title="X",
            yaxis_title="Y",
            showlegend=False,
            plot_bgcolor="white",
            width=300,
            height=300
        )
        st.plotly_chart(fig_2d)

    with col2:
        st.write("### 3D Vector Visualization:")
        st.write("This plot shows a 3D vector with components [1, -2, 5], represented as an arrow in 3-dimensional space.")
        
        # Plotting a 3D vector with Plotly
        fig_3d = go.Figure(data=[go.Cone(x=[0], y=[0], z=[0], u=[1], v=[-2], w=[5], colorscale='Viridis', sizemode="absolute", sizeref=10)])  # Updated sizeref
        fig_3d.update_layout(
            title="3D Vector [1, -2, 5]",
            scene=dict(
                xaxis_title="X",
                yaxis_title="Y",
                zaxis_title="Z",
            ),
            showlegend=False,
            width=300,
            height=300
        )
        st.plotly_chart(fig_3d)

    st.write("""
    These visualizations show the 2D and 3D representations of vectors. In machine learning, such vectors represent individual data points or features in a high-dimensional space. Understanding how vectors are plotted helps in visualizing the data in feature space.
    """)

    # # Expander for deeper understanding
    # with st.expander("What is the Magnitude of a Vector?"):
    #     st.write("""
    #     The magnitude (or length) of a vector is a measure of how far the vector extends from the origin. For a 2D vector \(\mathbf{v} = [v_1, v_2]\), the magnitude is calculated as:
    #     """)

    #     st.latex(r'\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2}')
    #     st.write("""
    #     In 3D, for a vector \(\mathbf{v} = [v_1, v_2, v_3]\), the magnitude is:
    #     """)
    #     st.latex(r'\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}')
    #     st.write("""
    #     Magnitude is important in machine learning when normalizing data or calculating distances between points.
    #     """)

    with st.expander("What is the Magnitude of a Vector?"):
        col1, col2 = st.columns(2)
        
        with col1:
            # Explanation text
            st.write("The magnitude (or length) of a vector is a measure of how far the vector extends from the origin. "
                    "For a 2D vector ")
            
            # Inline LaTeX with `st.latex`
            st.latex(r'\mathbf{v} = [v_1, v_2]')
            
            # Continue the explanation
            st.write("the magnitude is calculated as:")
            
            # Display formula with `st.latex`
            st.latex(r'\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2}')

            # Explanation for 3D
            st.write("In 3D, for a vector ")
            
            # Inline LaTeX with `st.latex`
            st.latex(r'\mathbf{v} = [v_1, v_2, v_3]')
            
            # Continue explanation
            st.write("the magnitude is:")
            
            # Display 3D magnitude formula
            st.latex(r'\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}')

            # Final explanation
            st.write("Magnitude is important in machine learning when normalizing data or calculating distances between points.")
        
        with col2:
            # Plotting 2D vector with triangle and magnitude illustration
            fig, ax = plt.subplots()
            
            # Define the vector
            v1, v2 = 3, 4  # Example 2D vector (3, 4)
            
            # Plot the vector as an arrow
            ax.quiver(0, 0, v1, v2, angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\vec{v}$')
            ax.text(v1, v2, f'({v1}, {v2})', color="blue", ha="left", va="bottom")
            
            # Add dotted lines to form the triangle
            ax.plot([0, v1], [v2, v2], 'r--', linewidth=1)  # Horizontal line to the x-component
            ax.plot([v1, v1], [0, v2], 'r--', linewidth=1)  # Vertical line to the y-component

            # Label triangle legs and hypotenuse
            ax.text(v1/2, v2, f'v1={v1}', color="red", ha="center", va="bottom")
            ax.text(v1, v2/2, f'v2={v2}', color="red", ha="right", va="center")
            
            # Calculate and label the magnitude on the hypotenuse
            magnitude = np.sqrt(v1**2 + v2**2)
            ax.annotate(f"||v|| = {magnitude:.2f}", xy=(v1/2, v2/2), xytext=(10, -10),
                        textcoords="offset points", arrowprops=dict(arrowstyle="->", color='green'),
                        color='green')

            # Set limits and grid
            ax.set_xlim(-1, 5)
            ax.set_ylim(-1, 5)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            
            # Label the plot
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_title("2D Vector Representation with Magnitude and Triangle Intuition")

            # Show plot in Streamlit
            st.pyplot(fig)

    st.sidebar.header("Vector Inputs")
    v1_x = st.sidebar.number_input("Vector v1: x-component", value=3.0)
    v1_y = st.sidebar.number_input("Vector v1: y-component", value=2.0)
    v2_x = st.sidebar.number_input("Vector v2: x-component", value=1.0)
    v2_y = st.sidebar.number_input("Vector v2: y-component", value=4.0)

    # Define vectors
    v1 = np.array([v1_x, v1_y])
    v2 = np.array([v2_x, v2_y])

    with st.expander("Operations on Vectors"):
        st.write("### 1. Vector Addition")

        st.write("Vector addition combines two vectors. In machine learning, this operation can represent the accumulation of multiple features or data points, enhancing their influence on a prediction.")

        # Vector addition formula in LaTeX
        st.latex(r'\mathbf{v} + \mathbf{u} = [v_1 + u_1, v_2 + u_2]')

        # Vector addition calculation
        addition_result = v1 + v2

        # Interactive Plot for Vector Addition
        fig_add = go.Figure()
        fig_add.add_trace(go.Scatter(x=[0, v1[0]], y=[0, v1[1]], mode='lines+markers', name='Vector v1', line=dict(color='blue')))
        fig_add.add_trace(go.Scatter(x=[v1[0], addition_result[0]], y=[v1[1], addition_result[1]], mode='lines+markers', name='Vector v2', line=dict(color='red')))
        fig_add.add_trace(go.Scatter(x=[0, addition_result[0]], y=[0, addition_result[1]], mode='lines+markers', name='Resultant v1 + v2', line=dict(color='green')))

        fig_add.update_layout(title="Vector Addition", xaxis_title="X", yaxis_title="Y", width=500, height=400)
        st.plotly_chart(fig_add)

        st.write(f"**Result of vector addition**: {addition_result}")

        st.write("""
        The resultant vector represents the combined effect of both vectors. In data science, vector addition is useful in feature engineering, where multiple features may be combined to strengthen a particular signal in data.
        
        **Special Case**: If vectors are opposite in direction, the result may approach zero. This behavior is important when understanding patterns in data where opposing features cancel each other out.
        """)
            # Dot Product Section
        st.write("### 2. Dot Product")

        st.write("The dot product of two vectors provides a measure of their alignment, which is crucial for similarity metrics in ML and data science.")

        # Dot Product formula in LaTeX
        st.latex(r'\mathbf{v} \cdot \mathbf{u} = v_1 \cdot u_1 + v_2 \cdot u_2')

        # Dot Product Calculation
        dot_product_result = np.dot(v1, v2)

        st.write(f"**Dot product result**: {dot_product_result}")

        # Projection calculation
        projection = (dot_product_result / np.linalg.norm(v2)**2) * v2  # Projection of v1 onto v2

        # Interactive Plot for Dot Product and Projection
        fig_dot = go.Figure()
        fig_dot.add_trace(go.Scatter(x=[0, v1[0]], y=[0, v1[1]], mode='lines+markers', name='Vector v1', line=dict(color='blue')))
        fig_dot.add_trace(go.Scatter(x=[0, v2[0]], y=[0, v2[1]], mode='lines+markers', name='Vector v2', line=dict(color='red')))
        fig_dot.add_trace(go.Scatter(x=[0, projection[0]], y=[0, projection[1]], mode='lines+markers', name='Projection of v1 on v2', line=dict(color='purple', dash='dash')))

        fig_dot.update_layout(title="Dot Product and Projection", xaxis_title="X", yaxis_title="Y", width=500, height=400)
        st.plotly_chart(fig_dot)

        st.write(f"**Projection of v1 onto v2**: {projection}")

        st.write("""
        The projection represents the extent to which one vector aligns in the direction of another. In machine learning, the projection is vital in understanding the contribution of one feature to another. For instance, in natural language processing (NLP), the dot product can determine word similarity by projecting one word vector onto another.

        **Special Case**: If vectors are orthogonal, the dot product is zero, indicating no similarity. This property is exploited in ML to create independent features, thereby improving model generalization and interpretability.
        """)

            # Cross Product Section
        st.write("### 3. Cross Product")

        st.write("The cross product of two 3D vectors results in a vector perpendicular to both input vectors. This operation is often used in 3D geometry applications within ML, such as when representing orientations or rotations in computer vision.")

        # Cross Product formula in LaTeX
        st.latex(r'\mathbf{v} \times \mathbf{u} = \begin{bmatrix} v_2 \cdot u_3 - v_3 \cdot u_2 \\ v_3 \cdot u_1 - v_1 \cdot u_3 \\ v_1 \cdot u_2 - v_2 \cdot u_1 \end{bmatrix}')

        # Adding z-components for 3D vectors
        v1_z = st.sidebar.number_input("Vector v1: z-component", value=1.0)
        v2_z = st.sidebar.number_input("Vector v2: z-component", value=2.0)
        v1_3d = np.array([v1_x, v1_y, v1_z])
        v2_3d = np.array([v2_x, v2_y, v2_z])

        # Cross Product Calculation
        cross_product_result = np.cross(v1_3d, v2_3d)

        st.write(f"**Cross product result**: {cross_product_result}")

        st.write("""
        The result vector is perpendicular to both `v1` and `v2`. In machine learning, cross products help represent transformations, such as rotations in 3D data.

        **Special Case**: If two vectors are parallel, the cross product is zero, indicating no perpendicular component. This behavior is essential for algorithms where orientations or alignments matter.
""")




    with st.expander("Summary and Machine Learning Context"):
        st.write("""
        Understanding these operations gives a foundation for many machine learning techniques:

        - **Addition** helps in feature engineering, merging information, and data transformations.
        - **Dot Product** is a foundation for similarity measures, which is essential in text similarity and recommendation engines.
        - **Cross Product** (3D) finds use in computer vision for spatial orientation.

        Through this interactive module, you’ve seen how changing vector values impacts operations, making these concepts 
        essential tools in your data science and ML toolkit.
        """)



    st.write("""
    - **Data Representation**: Vectors are used to represent data points in datasets, where each feature corresponds to a component in the vector.
    - **Feature Space**: In machine learning models, each vector corresponds to a position in feature space, and operations like distance calculations help classify or cluster data points.
    - **Operations on Vectors**: Operations such as addition, subtraction, dot products, and cross products are fundamental to machine learning algorithms.
    """)

vectors_section()