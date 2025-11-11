import streamlit as st

def display_tiles():
    st.markdown(
        """
        <style>
            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-bottom: 50px;
            }
            .box {
                background-color: rgba(0, 0, 0, 0.4); /* Darker semi-transparent box */
                width: 250px;
                height: 250px;
                color: white;
                border-radius: 15px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                transition: transform 0.3s, box-shadow 0.3s;
                cursor: pointer;
                text-align: center;
                padding: 15px; /* Added padding for symmetry */
                text-decoration: none; /* Remove underline */
            }
            /* Remove default link styling */
            .box a {
                color: inherit; /* Inherit color from parent */
                text-decoration: none; /* Remove underline */
                width: 100%; /* Full width for clickable area */
                height: 100%; /* Full height for clickable area */
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
            }
            .box:hover {
                transform: translateY(-10px);
                box-shadow: 0px 10px 20px rgba(255, 255, 255, 0.6);
            }
            .box h3 {
                margin: 10px 0 0 0;
                font-size: 1.5em;
            }
            .box i {
                font-size: 3em;
                margin-bottom: 10px;
            }
        </style>

        <div class="container">
            <div class="box">
                <a href="/IntroToML" target="_self">
                    <i class="fas fa-brain"></i>
                    <h3>Intro to ML</h3>
                </a>
            </div>
            <div class="box">
                <a href="/MathsForML" target="_self">
                    <i class="fas fa-square-root-alt"></i>
                    <h3>Maths for ML</h3>
                </a>
            </div>
            <div class="box">
                <a href="/DimensionalityReduction" target="_self">
                    <i class="fas fa-compress"></i>
                    <h3>Dimensionality Reduction</h3>
                </a>
            </div>
            <div class="box">
                <a href="/Clustering" target="_self">
                    <i class="fas fa-project-diagram"></i>
                    <h3>Clustering</h3>
                </a>
            </div>
            <div class="box">
                <i class="fas fa-clock"></i>
                <h3>Future Additions</h3>
                <p style="font-size: 0.9em; color: #ECD46A;">Stay tuned as I continue to learn and expand this journey.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
