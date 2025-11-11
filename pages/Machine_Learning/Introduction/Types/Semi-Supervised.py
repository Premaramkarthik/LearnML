# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import make_blobs

def run():
    
    # Page title
    st.title("Semi-Supervised Learning")


    # Introduction section
    st.write("""
    Imagine you have a box of assorted candies. You know the flavors of some candies but not all. By tasting a few and analyzing their characteristics, you can make educated guesses about the flavors of the remaining candies.
    Similarly, in semi-supervised learning, a model learns from a small amount of labeled data combined with a large amount of unlabeled data, enhancing its learning capability.
    """)


    # Explanation of Semi-Supervised Learning
    st.subheader("What is Semi-Supervised Learning?")
    st.write("""
    Semi-supervised learning is a machine learning approach that uses both labeled and unlabeled data for training. The primary goal is to improve learning accuracy by leveraging the abundant unlabeled data alongside the limited labeled data.
    """)


    # How Semi-Supervised Learning Works
    st.subheader("How Semi-Supervised Learning Works")
    st.markdown("""
    1. **Initial Training**: The model begins learning from the small amount of labeled data.
    2. **Pattern Discovery**: It uses unsupervised methods on the unlabeled data to discover additional patterns and clusters.
    3. **Self-Labeling**: The model may make educated guesses on the unlabeled data, treating them as pseudo-labels.
    4. **Improved Learning**: The model continues refining its predictions with the combined labeled and pseudo-labeled data.
    """)


    # Types of Semi-Supervised Learning Problems
    st.subheader("Types of Semi-Supervised Learning Problems")
    st.write("Semi-supervised learning problems can generally be categorized into the following types:")


    # Define a table to differentiate types of semi-supervised learning
    types_data = {
        'Type': ['Self-Training', 'Co-Training'],
        'Description': [
            'The model is trained on labeled data, then predicts labels for the unlabeled data iteratively, refining its predictions over time.',
            'Two or more models are trained on different views of the same data and share their predictions to improve each other’s performance.'
        ],
        'Example': [
            'Using a model to label a larger dataset and retrain on the new labels.',
            'Training one model on images and another on text descriptions to classify web pages.'
        ]
    }
    types_df = pd.DataFrame(types_data)


    # Display table without row indexes
    st.write(types_df.to_html(index=False), unsafe_allow_html=True)
    st.write("")


    # Visualization with make_blobs
    st.subheader("Semi-Supervised Learning Visualization with Make Blobs")


    # Generate synthetic data
    def create_blob_data(n_samples=200, n_clusters=3, n_labeled=30, random_state=42):
        X, y = make_blobs(n_samples=n_samples, centers=n_clusters, random_state=random_state)
        labeled_idx = np.random.choice(range(n_samples), size=n_labeled, replace=False)
        unlabeled_idx = np.setdiff1d(range(n_samples), labeled_idx)
    
        y_combined = np.full(n_samples, -1)
        y_combined[labeled_idx] = y[labeled_idx]
        return X, y, y_combined, labeled_idx, unlabeled_idx


    X, y, y_combined, labeled_idx, unlabeled_idx = create_blob_data()


    # Create consistent color palette for labeled data points
    palette = sns.color_palette("deep", len(np.unique(y)))
    label_colors = {label: palette[label] for label in np.unique(y)}


    fig, axs = plt.subplots(1, 2, figsize=(12, 6))


    # Plot before labeling, with labeled data in specific colors and unlabeled data in gray
    for label in np.unique(y_combined[labeled_idx]):
        label_points = labeled_idx[y[labeled_idx] == label]
        axs[0].scatter(X[label_points, 0], X[label_points, 1], color=label_colors[label], label=f'Class {label}')
    axs[0].scatter(X[unlabeled_idx, 0], X[unlabeled_idx, 1], color='gray', label='Unlabeled', alpha=0.5)
    axs[0].set_title("Before Labeling (Unlabeled Data in Gray)")
    axs[0].set_xlabel("Feature 1")
    axs[0].set_ylabel("Feature 2")
    axs[0].legend()


    # Simulate labeling process: assign pseudo-labels to unlabeled data
    pseudo_labels = np.array([y[np.random.choice(labeled_idx)] for _ in range(len(unlabeled_idx))])
    y_combined[unlabeled_idx] = pseudo_labels


    # Plot after labeling, maintaining consistent colors for labeled points
    for label in np.unique(y):
        all_points = np.where(y_combined == label)[0]
        axs[1].scatter(X[all_points, 0], X[all_points, 1], color=label_colors[label], label=f'Class {label}')
    axs[1].set_title("After Labeling (Pseudo-Labels Assigned)")
    axs[1].set_xlabel("Feature 1")
    axs[1].set_ylabel("Feature 2")
    axs[1].legend()


    plt.tight_layout()
    st.pyplot(fig)


    # Explanation of the plots
    st.write("""
    ### Explanation
    - **Before Labeling**: The plot shows the original labeled data points (colored) and unlabeled data points (gray). The model can only learn from the labeled data.
    - **After Labeling**: In this plot, pseudo-labels are assigned to the previously unlabeled data, illustrating how the model can improve its understanding by utilizing both labeled and unlabeled data.
    """)


    # Advantages and Disadvantages of Semi-Supervised Learning
    st.subheader("Advantages of Semi-Supervised Learning")
    st.markdown("""
    - Combines the strengths of both supervised and unsupervised learning
    - Utilizes large amounts of unlabeled data, reducing the need for extensive labeled datasets
    - Can significantly improve model performance with fewer labeled examples
    """)


    st.subheader("Disadvantages of Semi-Supervised Learning")
    st.markdown("""
    - The quality of unlabeled data can adversely affect model performance
    - Requires careful selection of labeled data to ensure effective learning
    - May lead to overfitting if the model relies too much on uncertain labels
    """)


    # Summary
    st.subheader("Summary")
    st.write("""
    Semi-supervised learning is a powerful technique that leverages both labeled and unlabeled data to enhance model performance. It finds applications in various domains, including text and image classification, where obtaining labeled data can be challenging.
    By effectively utilizing a mix of data, semi-supervised learning can improve accuracy while reducing the labeling effort required.
    """)


