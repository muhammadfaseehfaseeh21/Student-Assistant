import streamlit as st
import os

# Groq Import
try:
    from groq import Groq
except ImportError:
    Groq = None


# =====================================================
# PAGE SETUP
# =====================================================

st.set_page_config(
    page_title="Student Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Assistant")
st.write("Your complete assistant for admission, fees, scholarships and academics.")


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📚 Student Assistant")

menu = st.sidebar.selectbox(
    "Select a Feature",
    [
        "🎓 Admission Assistant",
        "💰 Fee Structure + Fee Calculator",
        "📊 Merit/Aggregate Calculator",
        "💵 Scholarship Finder",
        "📚 Programs & Departments",
        "📅 Admission/Important Dates",
        "🧮 GPA/CGPA Calculator",
        "📄 Admission Document Checklist",
        "🤖 AI Student Chatbot"
    ]
)


# =====================================================
# 1. ADMISSION ASSISTANT
# =====================================================

if menu == "🎓 Admission Assistant":

    st.header("🎓 Admission Assistant")

    st.write(
        "Find basic admission information for school, college and university students."
    )

    level = st.selectbox(
        "Select Education Level",
        ["School", "College", "University"]
    )

    program = st.text_input(
        "Enter Program",
        placeholder="Example: BS Computer Science"
    )

    if st.button("Show Admission Information"):

        if program:

            st.subheader("Admission Information")

            st.write("**Education Level:**", level)
            st.write("**Program:**", program)

            st.write("### General Eligibility")
            st.write(
                "Eligibility depends on the institution and selected program."
            )

            st.write("### General Admission Process")

            steps = [
                "Check eligibility",
                "Select your program",
                "Prepare required documents",
                "Submit admission application",
                "Appear in entry test if required",
                "Check merit list",
                "Pay admission/semester fee",
                "Complete enrollment"
            ]

            for i, step in enumerate(steps, 1):
                st.write(f"{i}. {step}")

        else:
            st.warning("Please enter a program name.")


# =====================================================
# 2. FEE STRUCTURE + FEE CALCULATOR
# =====================================================

elif menu == "💰 Fee Structure + Fee Calculator":

    st.header("💰 Fee Structure + Fee Calculator")

    st.subheader("Fee Structure")

    tuition_fee = st.number_input(
        "Tuition Fee per Credit Hour (Rs.)",
        min_value=0,
        value=12000
    )

    admission_fee = st.number_input(
        "Admission Fee (Rs.)",
        min_value=0,
        value=15000
    )

    examination_fee = st.number_input(
        "Examination Fee (Rs.)",
        min_value=0,
        value=5000
    )

    other_fee = st.number_input(
        "Other Charges (Rs.)",
        min_value=0,
        value=3000
    )

    st.subheader("🧮 Fee Calculator")

    credit_hours = st.number_input(
        "Credit Hours",
        min_value=1,
        max_value=30,
        value=15
    )

    if st.button("Calculate Total Fee"):

        tuition_total = tuition_fee * credit_hours

        total_fee = (
            tuition_total
            + admission_fee
            + examination_fee
            + other_fee
        )

        st.write(
            f"Tuition Fee: **Rs. {tuition_total:,}**"
        )

        st.write(
            f"Admission Fee: **Rs. {admission_fee:,}**"
        )

        st.write(
            f"Examination Fee: **Rs. {examination_fee:,}**"
        )

        st.write(
            f"Other Charges: **Rs. {other_fee:,}**"
        )

        st.success(
            f"💰 Total Estimated Fee: Rs. {total_fee:,}"
        )


# =====================================================
# 3. MERIT / AGGREGATE CALCULATOR
# =====================================================

elif menu == "📊 Merit/Aggregate Calculator":

    st.header("📊 Merit / Aggregate Calculator")

    st.write(
        "Enter your marks and weightages. Total weightage must be 100%."
    )

    matric = st.number_input(
        "Matric Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    intermediate = st.number_input(
        "Intermediate Percentage",
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

    st.subheader("Weightages")

    matric_weight = st.number_input(
        "Matric Weightage",
        min_value=0.0,
        max_value=100.0,
        value=10.0
    )

    intermediate_weight = st.number_input(
        "Intermediate Weightage",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

    test_weight = st.number_input(
        "Entry Test Weightage",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    if st.button("Calculate Aggregate"):

        total_weight = (
            matric_weight
            + intermediate_weight
            + test_weight
        )

        if total_weight != 100:

            st.error(
                f"Weightage must be 100%. Current total is {total_weight}%."
            )

        else:

            aggregate = (
                matric * matric_weight / 100
                + intermediate * intermediate_weight / 100
                + entry_test * test_weight / 100
            )

            st.success(
                f"📊 Your Aggregate is: {aggregate:.2f}%"
            )


# =====================================================
# 4. SCHOLARSHIP FINDER
# =====================================================

elif menu == "💵 Scholarship Finder":

    st.header("💵 Scholarship Finder")

    st.write(
        "Find common scholarship categories for students."
    )

    scholarships = {
        "🏆 Merit Scholarship":
            "For students with strong academic performance.",

        "💰 Need-Based Scholarship":
            "For students who need financial assistance.",

        "🎓 University Scholarship":
            "Scholarship offered according to university policy.",

        "📚 Academic Scholarship":
            "For students with excellent academic results."
    }

    for name, description in scholarships.items():

        with st.expander(name):
            st.write(description)

            st.write("### Common Requirements")

            st.write("• Academic documents")
            st.write("• Scholarship application")
            st.write("• Required financial documents if applicable")

    st.info(
        "Actual scholarship eligibility depends on the institution or scholarship provider."
    )


# =====================================================
# 5. PROGRAMS & DEPARTMENTS
# =====================================================

elif menu == "📚 Programs & Departments":

    st.header("📚 Programs & Departments")

    programs = {
        "Computer Science": [
            "BS Computer Science",
            "BS Artificial Intelligence",
            "BS Data Science"
        ],

        "Engineering": [
            "Computer Engineering",
            "Electrical Engineering",
            "Civil Engineering"
        ],

        "Business": [
            "BBA",
            "BS Accounting & Finance",
            "BS Management"
        ],

        "Medical": [
            "MBBS",
            "BDS",
            "Pharm-D"
        ]
    }

    department = st.selectbox(
        "Select Department",
        list(programs.keys())
    )

    st.subheader(department)

    for program in programs[department]:
        st.write("🎓", program)

    st.subheader("Program Information")

    selected_program = st.selectbox(
        "Select a Program",
        programs[department]
    )

    st.write("**Selected Program:**", selected_program)

    st.write(
        "Program duration, eligibility and career options can be added "
        "according to the official institution information."
    )


# =====================================================
# 6. ADMISSION / IMPORTANT DATES
# =====================================================

elif menu == "📅 Admission/Important Dates":

    st.header("📅 Admission / Important Dates")

    st.write(
        "Keep important admission events in one place."
    )

    admission_open = st.date_input(
        "Admission Opening Date"
    )

    application_deadline = st.date_input(
        "Application Deadline"
    )

    entry_test = st.date_input(
        "Entry Test Date"
    )

    merit_list = st.date_input(
        "Merit List Date"
    )

    classes_start = st.date_input(
        "Classes Start Date"
    )

    st.subheader("📋 Important Dates")

    st.write(
        "🟢 Admission Opens:",
        admission_open
    )

    st.write(
        "🔴 Application Deadline:",
        application_deadline
    )

    st.write(
        "📝 Entry Test:",
        entry_test
    )

    st.write(
        "📊 Merit List:",
        merit_list
    )

    st.write(
        "🎓 Classes Start:",
        classes_start
    )


# =====================================================
# 7. GPA / CGPA CALCULATOR
# =====================================================

elif menu == "🧮 GPA/CGPA Calculator":

    st.header("🧮 GPA / CGPA Calculator")

    st.write(
        "Enter the credit hours and grade points for your courses."
    )

    number_of_courses = st.number_input(
        "Number of Courses",
        min_value=1,
        max_value=10,
        value=5
    )

    total_quality_points = 0.0
    total_credit_hours = 0.0

    for i in range(int(number_of_courses)):

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

        gpa = (
            total_quality_points
            / total_credit_hours
        )

        st.success(
            f"🧮 Your GPA is: {gpa:.2f}"
        )


# =====================================================
# 8. ADMISSION DOCUMENT CHECKLIST
# =====================================================

elif menu == "📄 Admission Document Checklist":

    st.header("📄 Admission Document Checklist")

    st.write(
        "Check the documents that you already have."
    )

    documents = [
        "CNIC / B-Form",
        "Passport-size photographs",
        "Matric Certificate / Result Card",
        "Intermediate Certificate / Result Card",
        "Domicile",
        "Character Certificate",
        "Migration Certificate",
        "Admission Application Form",
        "Father / Guardian CNIC"
    ]

    completed = 0

    for i, document in enumerate(documents):

        checked = st.checkbox(
            document,
            key=f"document_{i}"
        )

        if checked:
            completed += 1

    total_documents = len(documents)

    st.progress(
        completed / total_documents
    )

    st.write(
        f"Completed: **{completed}/{total_documents}**"
    )

    if completed == total_documents:

        st.success(
            "🎉 All documents are checked!"
        )


# =====================================================
# 9. AI STUDENT CHATBOT
# =====================================================

elif menu == "🤖 AI Student Chatbot":

    st.header("🤖 AI Student Chatbot")

    st.write(
        "Ask questions about admissions, fees, scholarships, "
        "programs, GPA, CGPA and general student guidance."
    )

    question = st.text_area(
        "Ask your question",
        placeholder=(
            "Example: What documents are normally required "
            "for university admission?"
        )
    )

    if st.button("Ask AI"):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            api_key = os.getenv("GROQ_API_KEY")

            if not api_key:

                st.error(
                    "GROQ_API_KEY is not configured."
                )

                st.info(
                    "The other student features can still be used."
                )

            elif Groq is None:

                st.error(
                    "Groq package is not installed."
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
                                    "You are a helpful AI Student Chatbot. "
                                    "Help students with admission, fees, "
                                    "scholarships, programs, GPA, CGPA "
                                    "and general education questions. "
                                    "Use simple language. "
                                    "Do not make up official university "
                                    "information. If information depends "
                                    "on a specific institution, tell the "
                                    "student to verify it from the official "
                                    "institution."
                                )
                            },
                            {
                                "role": "user",
                                "content": question
                            }
                        ],

                        temperature=0.2
                    )

                    answer = response.choices[0].message.content

                    st.subheader("🤖 AI Answer")

                    st.write(answer)

                except Exception as error:

                    st.error(
                        f"AI Error: {error}"
                    )
