import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Samriddhi Saxena - Data Scientist Portfolio",
    layout="wide",
    page_icon="📊"
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .header {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            padding: 20px;
            background: linear-gradient(90deg, #2E86C1, #3498DB);
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1;
            border-bottom: 3px solid #2E86C1;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        .subsection-title {
            font-size: 28px;
            font-weight: bold;
            color: #2E86C1;
            margin-top: 20px;
        }
        .content {
            font-size: 20px;
            color: #34495E;
            margin-left: 20px;
            line-height: 1.6;
        }
        .footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            font-size: 18px;
            color: #7F8C8D;
            background: #ECF0F1;
            border-radius: 10px;
        }
        .emoji {
            font-size: 24px;
            margin-right: 10px;
        }
        .contact-details {
            font-size: 22px;
            color: #34495E;
            margin-left: 20px;
            line-height: 1.8;
        }
        .contact-details a {
            color: #2E86C1;
            text-decoration: none;
        }
        .contact-details a:hover {
            text-decoration: underline;
        }
        .project-card {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .project-card h3 {
            color: #2E86C1;
        }
    </style>
""", unsafe_allow_html=True)

# Header with emoji
st.markdown('<div class="header">📊 Samriddhi Saxena - Data Scientist Portfolio</div>', unsafe_allow_html=True)

# About Me Section
st.markdown('<div class="section-title">👋 About Me</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">👩‍💻</span> Hi, I'm Samriddhi Saxena, a passionate Data Scientist with expertise in Machine Learning, Data Visualization, and Natural Language Processing.<br>
        <span class="emoji">🎯</span> I love solving real-world problems using data-driven approaches and building intelligent systems.<br>
        <span class="emoji">🚀</span> My goal is to leverage data to create impactful solutions that drive business growth and innovation.
    </div>
""", unsafe_allow_html=True)

# Contact Details
st.markdown('<div class="section-title">📞 Contact Me</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="contact-details">
        <span class="emoji">📧</span> <strong>Email:</strong> <a href="mailto:samaishsax@gmail.com">samaishsax@gmail.com</a><br>
        <span class="emoji">🔗</span> <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/samriddhiasaxena/" target="_blank">linkedin.com/in/samriddhiasaxena</a><br>
        <span class="emoji">🐱</span> <strong>GitHub:</strong> <a href="https://github.com/samsaxas" target="_blank">github.com/samsaxas</a><br>
        <span class="emoji">📞</span> <strong>Phone:</strong> +91 8209401982
    </div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-title">🚀 Projects</div>', unsafe_allow_html=True)

# Project 1
with st.container():
    st.markdown("""
        <div class="project-card">
            <h3>Integrated Intelligent Traffic Management System</h3>
            <p><span class="emoji">🚦</span> Built a solution using ML, boosting safety and efficiency by 30%.</p>
            <p><span class="emoji">🛠️</span> <strong>Tech Stack:</strong> MongoDB, Google Cloud, Python (Matplotlib, Pandas, NumPy)</p>
            <p><span class="emoji">🎯</span> <strong>Achievements:</strong> Improved accuracy by 95%, reduced violations, and enabled data-driven decisions.</p>
        </div>
    """, unsafe_allow_html=True)

# Project 2
with st.container():
    st.markdown("""
        <div class="project-card">
            <h3>Sentiment Analysis using NLP</h3>
            <p><span class="emoji">🧠</span> Designed a system using NLP, achieving 90% accuracy on 10,000+ data points.</p>
            <p><span class="emoji">📊</span> Presented sentiment insights with Seaborn visualizations and robust data pipelines.</p>
        </div>
    """, unsafe_allow_html=True)

# Project 3
with st.container():
    st.markdown("""
        <div class="project-card">
            <h3>Automated Parking System using Machine Learning</h3>
            <p><span class="emoji">🅿</span> Optimized parking allocation with ML algorithms, reducing search time by 99%.</p>
            <p><span class="emoji">🤖</span> Automated business processes, cutting labor expenses by 80% and enhancing user experience.</p>
        </div>
    """, unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <span class="emoji">🐍</span> <strong>Programming Languages:</strong> Python, SQL, MongoDB (NoSQL), R Programming, Java<br>
        <span class="emoji">📊</span> <strong>Technical Skills:</strong> Data Analysis, Machine Learning, NLP, Data Visualization, Big Data Analysis<br>
        <span class="emoji">🛠️</span> <strong>Tools & Others:</strong> Power BI, Tableau, Flask, Streamlit, DSA, Git/GitHub, Jupyter Notebook, VS Code
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2023 Samriddhi Saxena | Made with ❤️</div>', unsafe_allow_html=True)
