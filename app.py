import streamlit as st

# Set page configuration
st.set_page_config(page_title="My ML Journey", layout="wide")

# Hide Streamlit's sidebar
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# CSS styling for the homepage with a cohesive color palette
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        /* App background */
        .stApp {
            background-color: #0A192F; /* Dark background */
            color: #CCD6F6; /* Light text */
            font-family: 'Inter', sans-serif;
        }

        /* Navbar styling */
        .navbar {
            position: absolute;
            top: 0px;
            right: 0px;
            font-size: 0.9em;
            display: flex;
            gap: 10px;
            color: #64FFDA; /* Accent color */
        }
        .navbar a {
            color: #64FFDA;
            text-decoration: none;
            font-weight: 600;
        }
        .navbar a:hover {
            text-decoration: underline;
        }

        /* Main content container */
        .content-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        /* Heading styling */
        .main-heading {
            font-size: 2em;
            font-weight: 600;
            color: #CCD6F6;
            margin-bottom: 8px;
        }

        .highlight {
            color: #64FFDA;
        }

        /* Subheading styling */
        .subheading {
            font-size: 1.5em;
            color: #8892B0;
            margin-bottom: 20px;
        }

        /* Overview styling */
        .overview {
            font-size: 1.2em;  /* Increased font size */
            color: #8892B0;
            line-height: 1.6;
            margin: 10px 0 20px;
        }

        /* List styling */
        .overview ul {
            color: #8892B0;
            font-size: 1.1em;
            line-height: 2.0;
            margin-top: 10px;
        }

        /* Button styling */
        .button {
            display: inline-block;
            font-size: 1em;
            color: #64FFDA;
            border: 1px solid #64FFDA;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s, color 0.3s;
            margin-top: 10px;
        }
        .button:hover {
            background: #64FFDA;
            color: #0A192F;
        }

        /* Footer styling */
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #8892B0;
            margin: 30px 0;
        }

        /* Container for the tiles */
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px; /* Increased gap for space between tiles */
            margin-bottom: 30px;
        }

        /* Individual tile box */
        .box {
            position: relative;
            background: linear-gradient(135deg, #B9E5E8, #DFF2EB); /* Adjusted tile color palette */
            width: 180px;
            height: 180px;
            color: #4A628A;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: transform 0.3s, box-shadow 0.3s, background 0.3s;
            cursor: pointer;
            padding: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            animation: pulse 2s infinite; /* Continuous animation effect */
        }

        /* Animation effect */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Tooltip styling */
        .tooltip {
            visibility: hidden;
            position: absolute;
            top: 110%; /* Position the tooltip above the container */
            left: 50%; /* Center tooltip relative to the container */
            transform: translateX(-50%); /* Centers tooltip horizontally */
            width: 600px; /* Fixed width for uniform appearance */
            padding: 15px;
            background-color: #DFF2EB;
            color: #4A628A;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            font-size: 1em;
            text-align: left;
            transition: visibility 0.3s, opacity 0.3s ease-in-out;
            opacity: 0;
            z-index: 10;
            display: flex;
        }

        /* Tooltip arrow styling */
        .tooltip::before {
            content: "";
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-width: 10px;
            border-style: solid;
            border-color: #DFF2EB transparent transparent transparent;
        }
 
        /* Show tooltip on hover */
        .box:hover .tooltip {
            visibility: visible;
            opacity: 1;
        }

        /* Left and right sections of the tooltip */
        .tooltip-left,
        .tooltip-right {
            flex: 1;
            padding: 10px;
        }

        /* Remove underline from link text */
        .box a {
            color: inherit;
            text-decoration: none;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        /* Hover effect for the tiles */
        .box:hover {
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
        }

        /* Title styling inside the tiles */
        .box h3 {
            margin: 8px 0 0 0;
            font-size: 1.2em;
            font-weight: 600;
            text-align: center;
            color: #4A628A;
        }

        /* Icon styling inside the tiles */
        .box i {
            font-size: 2em; /* Increased icon size */
            margin-bottom: 5px;
            color: #4A628A;
        }

        .text-red {
            color: #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Navbar
st.markdown(
    """
    <div class='navbar'>
        <a href='#' class='button'>About</a>
        <a href='#' class='button'>Experience</a>
        <a href='#' class='button'>Work</a>
        <a href='#' class='button'>Contact</a>
        <a href='#' class='button'>Resume</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Main content section with centered summary
st.markdown(
    """
    <div class='content-container'>
        <!-- Summary Section -->
        <div>
            <div class='main-heading'>Welcome to <span class='highlight'>My ML Journey</span></div>
            <div class='subheading'>Embark on a transformative journey through the fascinating world of Machine Learning!</div>
            <div class="overview">
                This platform is dedicated to sharing my comprehensive machine learning experience. My goal is to guide others through the fascinating world of machine learning, from the basics to advanced topics, while showcasing my personal projects. Here’s what you can expect:
            </div>
            <ul style="color: #8892B0; font-size:1em; line-height:1.5; margin-top: 5px;">
                <li><strong>In-Depth Learning:</strong> A structured approach that covers foundational concepts in machine learning, providing a solid base for beginners.</li>
                <li><strong>Advanced Topics:</strong> Insights into advanced algorithms, techniques, and methodologies in machine learning, including supervised and unsupervised learning.</li>
                <li><strong>Mathematical Foundations:</strong> Detailed explanations of essential mathematical concepts, like calculus, linear algebra, and probability.</li>
                <li><strong>Personal Projects:</strong> A showcase of my projects demonstrating practical applications of ML techniques.</li>
                <li><strong>Interactive Learning:</strong> Engaging content that encourages exploration and practical application of ML concepts.</li>
                <li><strong>Community Engagement:</strong> An open invitation to collaborate and share ideas in a supportive learning environment.</li>
            </ul>
            <a href='/Introduction_to_Machine_Learning' target="_self" class='button' style="display: inline-block;">Explore Content!</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Tile section
st.markdown(
    """
    <div class="container">
        <div class="box">
            <a href='/python' target='_self'>
                <i class="fas fa-brain"></i>
                <h3>python</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Introduction to Machine Learning</strong>
                        <h4 class = "text-red">What is ML?</h4>
                        <p>Discover the foundations of machine learning, including key concepts, terminology, and how machines learn from data.</p>
                        <h4 class = "text-red">Applications</h4>
                        <p>Explore various applications of ML across different industries, including finance, healthcare, and more.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Examples</strong>
                        <h4 class = "text-red">Use Cases</h4>
                        <p>Real-world applications such as recommendation systems and fraud detection.</p>
                        <h4 class = "text-red">Tools</h4>
                        <p>Common tools used in ML, including Python libraries like scikit-learn and TensorFlow.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href='/leetcode' target='_self'>
                <i class="fas fa-brain"></i>
                <h3>leetcode</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Introduction to Machine Learning</strong>
                        <h4 class = "text-red">What is ML?</h4>
                        <p>Discover the foundations of machine learning, including key concepts, terminology, and how machines learn from data.</p>
                        <h4 class = "text-red">Applications</h4>
                        <p>Explore various applications of ML across different industries, including finance, healthcare, and more.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Examples</strong>
                        <h4 class = "text-red">Use Cases</h4>
                        <p>Real-world applications such as recommendation systems and fraud detection.</p>
                        <h4 class = "text-red">Tools</h4>
                        <p>Common tools used in ML, including Python libraries like scikit-learn and TensorFlow.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href='/dataAnalytics' target='_self'>
                <i class="fas fa-brain"></i>
                <h3>Data Analysis</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Introduction to Machine Learning</strong>
                        <h4 class = "text-red">What is ML?</h4>
                        <p>Discover the foundations of machine learning, including key concepts, terminology, and how machines learn from data.</p>
                        <h4 class = "text-red">Applications</h4>
                        <p>Explore various applications of ML across different industries, including finance, healthcare, and more.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Examples</strong>
                        <h4 class = "text-red">Use Cases</h4>
                        <p>Real-world applications such as recommendation systems and fraud detection.</p>
                        <h4 class = "text-red">Tools</h4>
                        <p>Common tools used in ML, including Python libraries like scikit-learn and TensorFlow.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href="/Introduction_to_Machine_Learning" target="_self">
                <i class="fas fa-brain"></i>
                <h3>Intro to ML</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Introduction to Machine Learning</strong>
                        <h4 class = "text-red">What is ML?</h4>
                        <p>Discover the foundations of machine learning, including key concepts, terminology, and how machines learn from data.</p>
                        <h4 class = "text-red">Applications</h4>
                        <p>Explore various applications of ML across different industries, including finance, healthcare, and more.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Examples</strong>
                        <h4 class = "text-red">Use Cases</h4>
                        <p>Real-world applications such as recommendation systems and fraud detection.</p>
                        <h4 class = "text-red">Tools</h4>
                        <p>Common tools used in ML, including Python libraries like scikit-learn and TensorFlow.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href="/Mathematics_for_ML" target="_self">
                <i class="fas fa-square-root-alt"></i>
                <h3>Math for ML</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Mathematics for Machine Learning</strong>
                        <h4 class = "text-red">Essential Concepts</h4>
                        <p>Learn essential mathematics for machine learning, including calculus, linear algebra, and probability theory.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Applications</strong>
                        <h4class = "text-red">Real-World Usage</h4>
                        <p>Understanding how math underpins machine learning algorithms and model performance.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href="/Dimensionality_Reduction_Techniques" target="_self">
                <i class="fas fa-compress"></i>
                <h3>Dimensionality Reduction Techniques</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Dimensionality Reduction Techniques</strong>
                        <h4 class = "text-red">Why Reduce Dimensions?</h4>
                        <p>Explore techniques like PCA and t-SNE to reduce dataset dimensions for better performance and visualization.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>How to Implement</strong>
                        <h4 class = "text-red">Using Libraries</h4>
                        <p>Learn how to implement these techniques using popular ML libraries.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href="/Clustering_Techniques" target="_self">
                <i class="fas fa-project-diagram"></i>
                <h3>Clustering Techniques</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Clustering Techniques</strong>
                        <h4 class = "text-red">Understanding Clustering</h4>
                        <p>Group data points based on similarity using techniques like K-means, hierarchical clustering, and DBSCAN.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Applications</strong>
                        <h4 class = "text-red">Use Cases</h4>
                        <p>See how clustering is used in customer segmentation and data analysis.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <a href="/Preprocessing_Techniques" target="_self">
                <i class="fas fa-filter"></i>
                <h3>Preprocessing Techniques</h3>
                <div class="tooltip">
                    <div class="tooltip-left">
                        <strong>Preprocessing Techniques</strong>
                        <h4 class = "text-red">Data Cleaning</h4>
                        <p>Learn how to clean and prepare your data, handle missing values, and encoding techniques.</p>
                    </div>
                    <div class="tooltip-right">
                        <strong>Feature Engineering</strong>
                        <h4 class = "text-red">Transforming Data</h4>
                        <p>Explore feature scaling, normalization, and extraction to enhance model performance.</p>
                    </div>
                </div>
            </a>
        </div>
        <div class="box">
            <i class="fas fa-clock"></i>
            <h3>Future Additions</h3>
            <div class="tooltip">
                <div class="tooltip-left">
                    <strong>Coming Soon</strong>
                    <h4 class = "text-red">Stay Tuned!</h4>
                    <p>New topics and advanced techniques will be added here to further your ML journey.</p>
                </div>
                <div class="tooltip-right">
                    <strong>Suggestions?</strong>
                    <h4 class = "text-red">Have Ideas?</h4>
                    <p>Let us know what topics you'd like to see covered in the future.</p>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
