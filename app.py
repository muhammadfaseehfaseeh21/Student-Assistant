python
import streamlit as st
import os

# Groq AI
try:
    from groq import Groq
except ImportError:
    Groq = None


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Assistant",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🎓 Student Assistant")

st.write(
    "A complete student assistant for admission, fees, "
    "programs, scholarships, merit, GPA and academic guidance."
)


# =========================================================
# SAMPLE PROGRAM DATA
# =========================================================

programs = {
    "BS Computer Science": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent",
        "level": "University"
    },

    "BS Software Engineering": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent",
        "level": "University"
    },

    "BS Artificial Intelligence": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent",
        "level": "University"
    },

    "BBA": {
        "duration": "4 Years",
        "eligibility": "Intermediate or equivalent",
        "level": "University"
    },

    "FSc Pre-Engineering": {
        "duration": "2 Years",
        "eligibility": "Matric or equivalent",
        "level": "College"
    },

    "FSc Pre-Medical": {
        "duration": "2 Years",
        "eligibility": "Matric or equivalent",
        "level": "College"
    },

    "ICS": {
        "duration": "2 Years",
        "eligibility": "Matric or equivalent",
        "level": "College"
    }
}


# =========================================================
# SCHOLARSHIP DATA
# =========================================================

scholarships = [
    {
        "name": "🏆 Merit Scholarship",
        "description": "For students with strong academic performance.",
        "requirements": "High academic merit and required documents."
    },

    {
        "name": "💰 Need-Based Scholarship",
        "description": "For students who need financial assistance.",
        "requirements": "Financial documents and academic record."
    },

    {
        "name": "🎓 University Scholarship",
        "description": "Scholarship offered according to an institution's policy.",
        "requirements": "Depends on the university or college."
    },

    {
        "name": "👨‍👩‍👧 Special Scholarship",
        "description": "Some institutions provide special financial support.",
        "requirements": "Depends on the institution."
    }
]


# =========================================================
# REQUIRED DOCUMENTS
# =========================================================

documents = [
    "CNIC / B-Form",
    "Passport-size photographs",
    "Matric result card / certificate",
    "Intermediate result card / certificate",
    "Domicile",
    "Character certificate",
    "Migration certificate (if required)",
    "Admission application form",
    "Father / Guardian CNIC",
    "Other documents required by institution"
]


# =========================================================
# SIDEBAR MENU
# =========================================================

st.sidebar.title("📚 Student Features")

feature = st.sidebar.radio(
    "Select Feature",
    [
        "🏠 Home",
        "📝 Admission Assistant",
        "💰 Fee Structure",
        "🧮 Fee Calculator",
        "📊 Merit / Aggregate Calculator",
        "🎓 Programs & Departments",
        "💵 Scholarship Finder",
        "📅 Important Dates",
        "📈 GPA / CGPA Calculator",
        "📄 Documents Checklist",
        "🤖 AI Student Assistant"
    ]
)


# =========================================================
# HOME
# =========================================================

if feature == "🏠 Home":

    st.header("🎓 Welcome to Student Assistant")

    st.write(
        "This app provides useful tools and information for "
        "school, college and university students."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📝 Admissions\n\n"
            "Admission requirements, eligibility and procedure."
        )

    with col2:
        st.info(
            "💰 Fees\n\n"
            "Fee structure and fee calculation."
        )

    with col3:
        st.info(
            "🎓 Scholarships\n\n"
            "Explore different scholarship options."
        )

    st.subheader("✨ Available Features")

    features = [
        "📝 Admission Assistant",
        "💰 Fee Structure",
        "🧮 Fee Calculator",
        "📊 Merit / Aggregate Calculator",
        "🎓 Programs & Departments",
        "💵 Scholarship Finder",
        "📅 Important Dates",
        "📈 GPA / CGPA Calculator",
        "📄 Documents Checklist",
        "🤖 AI Student Assistant"
    ]

    for item in features:
        st.write("✅", item)


# =========================================================
# ADMISSION ASSISTANT
# =========================================================

elif feature == "📝 Admission Assistant":

    st.header("📝 Admission Assistant")

    education_level = st.selectbox(
        "Select Education Level",
        [
            "🏫 School",
            "🎒 College",
            "🎓 University"
        ]
    )

    st.subheader("Admission Information")

    st.write(
        f"Selected Level: **{education_level}**"
    )

    program = st.selectbox(
        "Select Program",
        list(programs.keys())
    )

    data = programs[program]

    st.write("### Program Information")

    st.write("**Program:**", program)
    st.write("**Level:**", data["level"])
    st.write("**Duration:**", data["duration"])
    st.write("**Basic Eligibility:**", data["eligibility"])

    st.subheader("📋 General Admission Procedure")

    admission_steps = [
        "Check eligibility criteria",
        "Select your desired program",
        "Prepare required documents",
        "Complete the admission application",
        "Submit the application",
        "Appear in entry test if required",
        "Check merit list",
        "Pay admission / semester fee",
        "Complete enrollment"
    ]

    for number, step in enumerate(admission_steps, 1):
        st.write(f"**{number}.** {step}")


# =========================================================
# FEE STRUCTURE
# =========================================================

elif feature == "💰 Fee Structure":

    st.header("💰 Fee Structure")

    st.info(
        "Enter the fee information of your institution "
        "to view an estimated structure."
    )

    tuition = st.number_input(
        "Tuition Fee per Credit Hour (Rs.)",
        min_value=0,
        value=12000,
        step=500
    )

    admission = st.number_input(
        "Admission Fee (Rs.)",
        min_value=0,
        value=15000,
        step=1000
    )

    examination = st.number_input(
        "Examination Fee (Rs.)",
        min_value=0,
        value=5000,
        step=500
    )

    library = st.number_input(
        "Library / Other Charges (Rs.)",
        min_value=0,
        value=3000,
        step=500
    )

    st.subheader("Fee Information")

    st.write(f"**Tuition Fee / Credit Hour:** Rs. {tuition:,}")
    st.write(f"**Admission Fee:** Rs. {admission:,}")
    st.write(f"**Examination Fee:** Rs. {examination:,}")
    st.write(f"**Library / Other Charges:** Rs. {library:,}")


# =========================================================
# FEE CALCULATOR
# =========================================================

elif feature == "🧮 Fee Calculator":

    st.header("🧮 Fee Calculator")

    fee_per_credit = st.number_input(
        "Fee per Credit Hour (Rs.)",
        min_value=0,
        value=12000,
        step=500
    )

    credit_hours = st.number_input(
        "Credit Hours",
        min_value=1,
        max_value=30,
        value=15
    )

    admission_fee = st.number_input(
        "Admission / Other Fee (Rs.)",
        min_value=0,
        value=15000,
        step=1000
    )

    examination_fee = st.number_input(
        "Examination Fee (Rs.)",
        min_value=0,
        value=5000,
        step=500
    )

    if st.button("Calculate Total Fee"):

        tuition_fee = fee_per_credit * credit_hours

        total_fee = (
            tuition_fee
            + admission_fee
            + examination_fee
        )

        st.subheader("💰 Fee Summary")

        st.write(
            f"Tuition Fee: **Rs. {tuition_fee:,}**"
        )

        st.write(
            f"Admission / Other Fee: **Rs. {admission_fee:,}**"
        )

        st.write(
            f"Examination Fee: **Rs. {examination_fee:,}**"
        )

        st.success(
            f"Estimated Total Fee: Rs. {total_fee:,}"
        )


# =========================================================
# MERIT / AGGREGATE CALCULATOR
# =========================================================

elif feature == "📊 Merit / Aggregate Calculator":

    st.header("📊 Merit / Aggregate Calculator")

    st.write(
        "Enter your percentages and their weightages."
    )

    matric = st.number_input(
        "Matric Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    intermediate = st.number_input(
        "Intermediate / FSc Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    entry_test = st.number_input(
        "Entry Test Percentage",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    matric_weight = st.number_input(
        "Matric Weightage (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0
    )

    intermediate_weight = st.number_input(
        "Intermediate Weightage (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

    test_weight = st.number_input(
        "Entry Test Weightage (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    if st.button("Calculate Merit"):

        total_weight = (
            matric_weight
            + intermediate_weight
            + test_weight
        )

        if total_weight != 100:

            st.error(
                f"Total weightage must be 100%. "
                f"Current weightage is {total_weight}%."
            )

        else:

            aggregate = (
                (matric * matric_weight / 100)
                + (intermediate * intermediate_weight / 100)
                + (entry_test * test_weight / 100)
            )

            st.success(
                f"🎯 Your Aggregate is {aggregate:.2f}%"
            )


# =========================================================
# PROGRAMS & DEPARTMENTS
# =========================================================

elif feature == "🎓 Programs & Departments":

    st.header("🎓 Programs & Departments")

    selected_program = st.selectbox(
        "Select Program",
        list(programs.keys())
    )

    data = programs[selected_program]

    st.subheader(selected_program)

    st.write(
        "**Education Level:**",
        data["level"]
    )

    st.write(
        "**Duration:**",
        data["duration"]
    )

    st.write(
        "**Eligibility:**",
        data["eligibility"]
    )

    st.subheader("💼 Possible Career Areas")

    career_options = {

        "BS Computer Science": [
            "Software Developer",
            "Web Developer",
            "Data Analyst",
            "AI Engineer"
        ],

        "BS Software Engineering": [
            "Software Engineer",
            "QA Engineer",
            "Web Developer",
            "Application Developer"
        ],

        "BS Artificial Intelligence": [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "AI Developer"
        ],

        "BBA": [
            "Business Analyst",
            "Marketing",
            "Finance",
            "Management"
        ],

        "FSc Pre-Engineering": [
            "Engineering",
            "Computer Science",
            "Architecture",
            "Technology"
        ],

        "FSc Pre-Medical": [
            "Medicine",
            "Dentistry",
            "Pharmacy",
            "Biological Sciences"
        ],

        "ICS": [
            "Computer Science",
            "Software Engineering",
            "IT",
            "Artificial Intelligence"
        ]
    }

    for career in career_options[selected_program]:
        st.write("•", career)


# =========================================================
# SCHOLARSHIP FINDER
# =========================================================

elif feature == "💵 Scholarship Finder":

    st.header("💵 Scholarship Finder")

    st.write(
        "Explore common scholarship categories "
        "for students."
    )

    for scholarship in scholarships:

        with st.expander(scholarship["name"]):

            st.write(
                "**Description:**",
                scholarship["description"]
            )

            st.write(
                "**Basic Requirements:**",
                scholarship["requirements"]
            )


# =========================================================
# IMPORTANT DATES
# =========================================================

elif feature == "📅 Important Dates":

    st.header("📅 Important Dates")

    st.info(
        "These are sample dates. Actual dates depend "
        "on the institution."
    )

    dates = {
        "Admission Opens": "01 September",
        "Application Deadline": "30 September",
        "Entry Test": "10 October",
        "Merit List": "20 October",
        "Fee Submission Deadline": "25 October",
        "Classes Begin": "01 November"
    }

    for event, date in dates.items():

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"📌 **{event}**")

        with col2:
            st.write(date)


# =========================================================
# GPA / CGPA CALCULATOR
# =========================================================

elif feature == "📈 GPA / CGPA Calculator":

    st.header("📈 GPA / CGPA Calculator")

    st.write(
        "Enter credit hours and grade points "
        "for each course."
    )

    courses = st.number_input(
        "Number of Courses",
        min_value=1,
        max_value=10,
        value=5
    )

    total_quality_points = 0
    total_credit_hours = 0

    for i in range(int(courses)):

        col1, col2 = st.columns(2)

        with col1:

            credit_hours = st.number_input(
                f"Course {i + 1} Credit Hours",
                min_value=1.0,
                max_value=10.0,
                value=3.0,
                key=f"credit_{i}"
            )

        with col2:

            grade_point = st.number_input(
                f"Course {i + 1} Grade Point",
                min_value=0.0,
                max_value=4.0,
                value=3.0,
                step=0.1,
                key=f"grade_{i}"
            )

        total_quality_points += (
            credit_hours * grade_point
        )

        total_credit_hours += credit_hours

    if st.button("Calculate GPA"):

        if total_credit_hours > 0:

            gpa = (
                total_quality_points
                / total_credit_hours
            )

            st.success(
                f"📈 Your GPA is {gpa:.2f}"
            )


# =========================================================
# DOCUMENT CHECKLIST
# =========================================================

elif feature == "📄 Documents Checklist":

    st.header("📄 Admission Documents Checklist")

    st.write(
        "Check the documents you already have."
    )

    completed = 0

    for index, document in enumerate(documents):

        checked = st.checkbox(
            document,
            key=f"document_{index}"
        )

        if checked:
            completed += 1

    total_documents = len(documents)

    progress = (
        completed / total_documents
    )

    st.progress(progress)

    st.write(
        f"Completed: **{completed}/{total_documents}**"
    )

    if completed == total_documents:

        st.success(
            "🎉 All documents are ready!"
        )


# =========================================================
# AI STUDENT ASSISTANT
# =========================================================

elif feature == "🤖 AI Student Assistant":

    st.header("🤖 AI Student Assistant")

    st.write(
        "Ask questions about admissions, fees, "
        "scholarships, programs, GPA, CGPA and "
        "general education."
    )

    question = st.text_area(
        "Ask your question",
        placeholder=(
            "Example: What documents are normally "
            "required for university admission?"
        )
    )

    if st.button("Ask AI"):

        if not question.strip():

            st.error(
                "Please enter a question."
            )

        else:

            api_key = os.getenv("GROQ_API_KEY")

            if not api_key:

                st.warning(
                    "AI API key is not configured."
                )

                st.info(
                    "You can still use all the "
                    "non-AI features of this app."
                )

            elif Groq is None:

                st.error(
                    "Groq package is not available."
                )

            else:

                try:

                    client = Groq(
                        api_key=api_key
                    )

                    response = client.chat.completions.create(

                        model="openai/gpt-oss-120b",

                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are an AI Student Assistant. "
                                    "Help students with admissions, "
                                    "fees, scholarships, programs, "
                                    "GPA, CGPA, merit and general "
                                    "education questions. "
                                    "Use simple and clear language. "
                                    "Do not invent official university "
                                    "information. If information "
                                    "depends on a specific institution, "
                                    "tell the student to verify it "
                                    "from the official institution."
                                )
                            },

                            {
                                "role": "user",
                                "content": question
                            }
                        ],

                        temperature=0.2
                    )

                    answer = (
                        response
                        .choices[0]
                        .message
                        .content
                    )

                    st.subheader("🤖 AI Answer")

                    st.write(answer)

                except Exception as error:

                    st.error(
                        f"Error: {error}"
                    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 Student Assistant — Admission, Fees, "
    "Scholarships, Merit, GPA and Student Guidance"
)

