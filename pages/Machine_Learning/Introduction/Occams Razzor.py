import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from mlxtend.evaluate import bias_variance_decomp
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor

def run():
    
    # Set up for reproducibility
    np.random.seed(42)


    # Set up the Streamlit app layout for wider view
    # st.set_page_config(layout="wide")


    # Introduction Section
    st.title("Understanding Occam's Razor in Machine Learning")
    st.header("1. Introduction to Occam's Razor")
    st.write("""
    Occam's Razor is a philosophical principle stating that, when presented with competing hypotheses,
    the one with the fewest assumptions should be preferred. In machine learning, this translates to choosing
    simpler models that adequately explain the data, as complex models may overfit and perform poorly on unseen data.
    """)


    # Occam's Razor Explanation
    st.header("2. What is Occam's Razor?")
    st.write("""
    In machine learning, Occam's Razor encourages us to avoid overly complex models.
    While complex models can capture intricate patterns in the training data, they may not generalize well to new data.
    A simpler model with fewer parameters often provides a better balance between bias and variance.
    """)


    # Bias-Variance Tradeoff
    st.header("3. Bias-Variance Tradeoff and Occam's Razor")
    st.write("""
    The bias-variance tradeoff is central to applying Occam's Razor in machine learning. It describes how model complexity
    affects performance:
    - **Bias**: The error introduced by approximating the true data with a simplified model. High bias can lead to underfitting.
    - **Variance**: The error due to sensitivity to fluctuations in the training set. High variance can lead to overfitting.


    An optimal model minimizes both bias and variance, leading to a 'best fit' that Occam's Razor would support.
    """)


    # Synthetic Data for Visualization (New Dataset)
    X = np.linspace(0, 10, 100)
    y = 0.5 * X + 0.2 * (X ** 3) + np.random.normal(0, 20, size=X.shape)  # Adding cubic trend and noise
    X_reshaped = X.reshape(-1, 1)


    # Visualization of Underfitting, Overfitting, and Best Fit
    st.header("4. Visualizing Underfitting, Overfitting, and Best Fit")
    st.write("""
    Let's visualize three different models: one that underfits, one that overfits, and one that achieves the 'best fit.'
    This demonstrates the bias-variance tradeoff in action and highlights the principle of Occam's Razor.
    """)


    # Underfitting Example
    #st.subheader("Underfitting: High Bias, Low Variance")
    model_underfit = LinearRegression()
    model_underfit.fit(X_reshaped, y)
    y_pred_underfit = model_underfit.predict(X_reshaped)


    # Overfitting Example
    #st.subheader("Overfitting: Low Bias, High Variance")
    model_overfit = make_pipeline(PolynomialFeatures(degree=15), LinearRegression())
    model_overfit.fit(X_reshaped, y)
    y_pred_overfit = model_overfit.predict(X_reshaped)


    # Best Fit Example (Moderate Complexity)
    #st.subheader("Best Fit (Occam's Razor): Balanced Bias and Variance")
    model_bestfit = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
    model_bestfit.fit(X_reshaped, y)
    y_pred_bestfit = model_bestfit.predict(X_reshaped)


    # Plotting the three scenarios
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))


    # Plot underfitting
    ax[0].scatter(X, y, color='blue', label='Data')
    ax[0].plot(X, y_pred_underfit, color='red', label='Underfitting (Linear)')
    ax[0].set_title("Underfitting Example")
    ax[0].legend()


    # Plot overfitting
    ax[1].scatter(X, y, color='blue', label='Data')
    ax[1].plot(X, y_pred_overfit, color='orange', label='Overfitting (Polynomial Degree 15)')
    ax[1].set_title("Overfitting Example")
    ax[1].legend()


    # Plot best fit
    ax[2].scatter(X, y, color='blue', label='Data')
    ax[2].plot(X, y_pred_bestfit, color='green', label="Best Fit (Polynomial Degree 3)")
    ax[2].set_title("Best Fit (Occam's Razor)")
    ax[2].legend()


    st.pyplot(fig)


    # Bias-Variance Tradeoff Visualization
    st.header("5. Bias-Variance Tradeoff Visualization")
    st.write("""
    This plot shows the relationship between model complexity and error. As model complexity increases:
    - **Bias** decreases, as the model fits the data better.
    - **Variance** increases, as the model becomes more sensitive to training data fluctuations.


    The total error curve helps us identify the 'sweet spot' where the model has optimal complexity.
    """)


    complexity = np.linspace(1, 10, 100)
    bias_squared = (complexity - 3) ** 2
    variance = np.log(complexity) * 3
    total_error = bias_squared + variance


    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(complexity, bias_squared, label='Bias^2', color='blue')
    ax.plot(complexity, variance, label='Variance', color='red')
    ax.plot(complexity, total_error, label='Total Error', color='green')
    ax.axvline(x=3.5, color='purple', linestyle='--', label='Optimal Complexity')
    ax.set_xlabel('Model Complexity')
    ax.set_ylabel('Error')
    ax.set_title('Bias-Variance Tradeoff')
    ax.legend()
    st.pyplot(fig)


    # Practical Example with Bias Variance Decomposition
    st.header("6. Practical Example: Bias-Variance Decomposition")
    st.write("""
    To further understand the bias-variance tradeoff, we decompose error into bias and variance components
    using a simple model. This helps highlight how different models vary in their bias and variance,
    offering a practical example of Occam's Razor in model selection.
    """)


    # Generate data
    X, y = make_regression(n_samples=1000, n_features=10, noise=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    # Bias-Variance Decomposition
    knn = KNeighborsRegressor(n_neighbors=5)
    avg_error, avg_bias, avg_variance = bias_variance_decomp(knn, X_train, y_train, X_test, y_test, loss="mse", random_seed=42)


    st.write(f"Total Error: {avg_error:.3f}")
    st.write(f"Bias^2: {avg_bias:.3f}")
    st.write(f"Variance: {avg_variance:.3f}")


    st.write("""
    In this example:
    - A simpler model would increase bias (and reduce variance), possibly leading to underfitting.
    - A more complex model would increase variance (and reduce bias), potentially leading to overfitting.
    The best model balances these two components, following Occam's Razor for optimal model performance.
    """)


    # Conclusion
    st.header("7. Conclusion")
    st.write("""
    Occam's Razor serves as a guiding principle in machine learning, advocating for simplicity in model selection
    to avoid overfitting while achieving high predictive performance. By balancing bias and variance, we create
    models that generalize well to new data, underscoring the importance of the bias-variance tradeoff and
    Occam's Razor in developing effective, robust machine learning models.
    """)


