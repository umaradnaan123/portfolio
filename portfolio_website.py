import streamlit as st
import os
import plotly.express as px
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="S.B.MD.UMAR ADNAAN FAIZ - Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        font-family: 'Arial', sans-serif;
        background-attachment: fixed;
        color: #333;
        background: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcqm0gvD8UIe6TmVLSBiqSfqbwWw7BMd-0iQ&s') no-repeat center center fixed;
        background-size: cover;
    }
    .header {
        font-size: 36px;
        color: #fff;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 24px;
        color: #fff;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .contact-info {
        font-size: 16px;
        margin-bottom: 10px;
        color: #fff;

    }
    .button {
        background-color: #2E86C1;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #1A5276;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 3])
with col1:
    # Replace the local image with a URL
    profile_image_url = "data:image/jpeg;base64,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"  # Replace with your actual image URL
    st.image(profile_image_url, width=200)

with col2:
    st.markdown('<div class="header">S.B.MD.UMAR ADNAAN FAIZ</div>', unsafe_allow_html=True)
    st.markdown("**Data Science Enthusiast | AI Developer**")
    st.markdown('<div class="contact-info">📱 +91-7993698361 | +91-9360631792<br>📍 Chennai, India<br>📧 adnaanaddu1929@gmail.com</div>', unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/mohammed-umar-adnaan-faiz/) | [GitHub](https://github.com/umaradnaan123) | [Kaggle](https://www.kaggle.com/umeradnaan)")

# About Section
st.markdown('<div class="subheader">Career Objective</div>', unsafe_allow_html=True)
st.write("""
Aspiring data scientist with strong foundation in data visualization, machine learning, and statistical analysis.
Proficient in Python and SQL. Eager to leverage academic knowledge and analytical skills in forward-thinking companies.
""")

# Education Section
st.markdown('<div class="subheader">Education</div>', unsafe_allow_html=True)
edu_col1, edu_col2, edu_col3 = st.columns(3)
with edu_col1:
    st.write("**B.Tech Computer Science**")
    st.write("Vel Tech Rangarajan Dr. Sagunthala R&D Institute")
    st.write("CGPA: 8.1 | YOP: 2025")

with edu_col2:
    st.write("**Intermediate(XII)**")
    st.write("Narayana Junior College, Kurnool")
    st.write("CGPA: 8.5 | YOP: 2021")

with edu_col3:
    st.write("**High School (X)**")
    st.write("Keshava Reddy School, Kurnool")
    st.write("CGPA: 8.3 | YOP: 2019")

# Skills Section with Interactive Chart
st.markdown('<div class="subheader">Technical Skills</div>', unsafe_allow_html=True)

# Sample data for skills
skills_data = {
    'Skills': ['Python', 'SQL', 'Deep Learning', 'Power BI', 'Web Development', 'NumPy', 'Pandas', 'Matplotlib', 'Seaborn', 'Problem Solving', 'Time Management', 'Communication', 'Multi-tasking'],
    'Proficiency': [90, 80, 75, 70, 65, 85, 90, 80, 75, 85, 80, 70, 75]
}
skills_df = pd.DataFrame(skills_data)

fig = px.bar(skills_df, x='Skills', y='Proficiency', title='Technical Skills Proficiency', color='Proficiency', text='Proficiency')
st.plotly_chart(fig)

# Projects Section with Filtering
st.markdown('<div class="subheader">Projects</div>', unsafe_allow_html=True)

project_filter = st.selectbox("Filter by Project Type", ["All", "Mobile App", "Machine Learning", "Data Analysis"])

projects = [
    {
        "title": "Farmers Marketplace Mobile App",
        "date": "June 2024",
        "link": "https://umaradnaan123.github.io/login/",
        "description": "Facilitates direct farmer-buyer transactions without intermediaries. Features online ordering and price listing capabilities. Built using modern mobile development frameworks.",
        "type": "Mobile App"
    },
    {
        "title": "Titanic Survival Prediction",
        "date": "May 2024",
        "link": "https://www.kaggle.com/code/umeradnaan/titanic",
        "description": "Machine learning model to predict passenger survival. Utilized Pandas for data preprocessing. Achieved 85% accuracy using ensemble methods.",
        "type": "Machine Learning"
    },
    {
        "title": "Remote Sensing Satellite Analysis",
        "date": "January 2024",
        "link": "https://umaradnaan123.github.io/index/",
        "description": "Analyzed electromagnetic spectrum data for environmental monitoring. Implemented image processing techniques for land cover classification. Used Python for data visualization and analysis.",
        "type": "Data Analysis"
    }
]

for project in projects:
    if project_filter == "All" or project["type"] == project_filter:
        with st.container():
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.write(f"**{project['title']}**")
            st.caption(f"{project['date']} | [Link]({project['link']})")
            st.write(project['description'])
            st.markdown('</div>', unsafe_allow_html=True)

# Experience Section
st.markdown('<div class="subheader">Work Experience</div>', unsafe_allow_html=True)
st.write("**Data Science Intern** | CodSoft")
st.write("June 2023 - Present")
st.write("""
- Developed machine learning models for various business use cases
- Conducted statistical analysis and data visualization projects
- Collaborated on team projects using Agile methodologies
""")

# Certifications Section
st.markdown('<div class="subheader">Certifications & Achievements</div>', unsafe_allow_html=True)
st.write("- Data Analysis with Python - [View Certificate](https://courses.cognitiveclass.ai/certificates/dac8b59717cc403f9d2382d59f74e4d5)")
st.write("- IBM Data Science Tools - [View Certificate](https://courses.cognitiveclass.ai/certificates/e3a292559537487595ddfa722e4d72ab)")
st.write("- Kaggle Dataset Expert (Global Rank 607) - [Profile](https://www.kaggle.com/umeradnaan)")
st.write("- Naukri Campus Young Turks Competition (98.18%) - [Certificate](https://drive.google.com/file/d/1Rwpf6MDo8djl6JDc9aAspST_xkO7n5YV/view)")

# Contact Form
st.markdown('<div class="subheader">Contact Me</div>', unsafe_allow_html=True)
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Send Message")
    
    if submit_button:
        st.success("Thank you for your message! I'll respond within 24 hours.")