```python
import streamlit as st
import os

# Optional Groq import
try:
    from groq import Groq
except ImportError:
    Groq = None


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Student Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Student Assistant")
st.write(
    "A student-friendly assistant for admissions, fees, scholarships, "
    "merit, GPA/CGPA and university information."
)


# ---------------------------------------------------------
# SAMPLE DATA
# ---------------------------------------------------------

PROGRAMS = {
    "BS Computer Science": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent with required marks",
        "type": "Undergraduate"
    },
    "BS Software Engineering": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent with required marks",
        "type": "Undergraduate"
    },
    "BS Artificial Intelligence": {
        "duration": "4 Years",
        "eligibility": "FSc / ICS or equivalent with required marks",
        "type": "Undergraduate"
    },
    "BBA": {
        "duration": "4 Years",
        "eligibility": "Intermediate or equivalent",
        "type": "Undergraduate"
    }
}


SCHOLARSHIPS = [
    {
        "name": "Merit Scholarship",
        "criteria": "Good academic performance / high merit",
        "documents": "Academic certificates and application form"
    },
    {
        "name": "Need-Based Scholarship",
        "criteria": "Financial need and academic requirements",
        "documents": "Income proof, academic documents and application form"
    },
    {
        "name": "University Scholarship",
        "criteria": "Depends on the university's scholarship policy",
        "documents": "Academic documents and required university forms"
    }
]


DOCUMENTS = [
    "CNIC / B-Form",
    "Passport-size photographs",
    "Matric certificate / result card",
    "Intermediate certificate / result card",
    "Domicile",
    "Character certificate",
    "Migration certificate (if required)",
    "Admission application form"
]


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("📚 Student Menu")

page = st.sidebar.radio(
    "Select a feature:",
    [
        "🏠 Home",
        "📝 Admissions",
        "💰 Fee Structure",
        "🧮 Fee Calculator",
        "📊 Merit Calculator",
        "🎓 Programs",
        "💵 Scholarships",
        "📅 Important Dates",
        "📈 GPA / CGPA Calculator",
        "📄 Documents Checklist",
        "🤖 AI Student Assistant"
    ]
)


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if page == "🏠 Home":

    st.header("Welcome to AI Student Assistant 👋")

    st.write(
        "This app helps students with common admission, academic "
        "and university-related tasks."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📝 Admissions\n\nCheck admission requirements and procedure.")

    with col2:
        st.info("💰 Fees\n\nCalculate estimated semester fees.")

    with col3:
        st.info("🎓 Scholarships\n\nExplore common scholarship types.")

    st.subheader("Available Features")

    features = [
        "📝 Admission Assistant",
        "💰 Fee Structure",
        "🧮 Fee Calculator",
        "📊 Merit / Aggregate Calculator",
        "🎓 Programs & Departments",
        "💵 Scholarship Information",
        "📅 Important Dates",
        "📈 GPA / CGPA Calculator",
        "📄 Admission Documents Checklist",
        "🤖 AI Student Assistant"
    ]

    for feature in features:
        st.write("✅ " + feature)

    st.warning(
        "Note: Sample university information is used in this starter version. "
        "For real admissions, always verify information from the institution's official website."
    )


# ---------------------------------------------------------
# ADMISSIONS
# ---------------------------------------------------------

elif page == "📝 Admissions":

    st.header("📝 Admission Assistant")

    st.write("Select a program to see basic admission information.")

    program = st.selectbox(
        "Select Program",
        list(PROGRAMS.keys())
    )

    data = PROGRAMS[program]

    st.subheader(program)

    st.write("**Program Type:**", data["type"])
    st.write("**Duration:**", data["duration"])
    st.write("**Basic Eligibility:**", data["eligibility"])

    st.subheader("Admission Process")

    steps = [
        "Check eligibility",
        "Select your desired program",
        "Prepare required documents",
        "Complete the online/offline application",
        "Submit the application before the deadline",
        "Appear in entry test/interview if required",
        "Check merit list",
        "Pay admission/semester fee",
        "Complete enrollment"
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"**{i}.** {step}")


# ---------------------------------------------------------
# FEE STRUCTURE
# ---------------------------------------------------------

elif page == "💰 Fee Structure":

    st.header("💰 Fee Structure")

    st.info(
        "The following is sample fee information. Replace it with the official "
        "fee structure of your target institution."
    )

    fee_data = {
        "Admission Fee": 15000,
        "Tuition Fee / Credit Hour": 12000,
        "Examination Fee": 5000,
        "Library / Other Charges": 3000
    }

    for name, amount in fee_data.items():
        st.write(f"**{name}:** Rs. {amount:,}")

    st.subheader("Example")

    st.write(
        "If a student takes 15 credit hours:"
    )

    st.code("15 × Rs. 12,000 = Rs. 180,000")

    st.success(
        "Estimated tuition fee = Rs. 180,000"
    )


# ---------------------------------------------------------
# FEE CALCULATOR
# ---------------------------------------------------------

elif page == "🧮 Fee Calculator":

    st.header("🧮 Fee Calculator")

    fee_per_credit = st.number_input(
        "Fee per credit hour (Rs.)",
        min_value=0,
        value=12000,
        step=500
    )

    credit_hours = st.number_input(
        "Number of credit hours",
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

    exam_fee = st.number_input(
        "Examination Fee (Rs.)",
        min_value=0,
        value=5000,
        step=500
    )

    if st.button("Calculate Fee"):

        tuition = fee_per_credit * credit_hours
        total = tuition + admission_fee + exam_fee

        st.subheader("Fee Summary")

        st.write(f"Tuition Fee: **Rs. {tuition:,}**")
        st.write(f"Admission / Other Fee: **Rs. {admission_fee:,}**")
        st.write(f"Examination Fee: **Rs. {exam_fee:,}**")

        st.success(f"Estimated Total Fee: Rs. {total:,}")


# ---------------------------------------------------------
# MERIT CALCULATOR
# ---------------------------------------------------------

elif page == "📊 Merit Calculator":

    st.header("📊 Merit / Aggregate Calculator")

    st.write(
        "This is a simple weighted aggregate calculator. "
        "Enter the marks and their weightages."
    )

    matric = st.number_input(
        "Matric Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    fsc = st.number_input(
        "FSc / Intermediate Percentage",
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

    fsc_weight = st.number_input(
        "FSc Weightage (%)",
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

    if st.button("Calculate Aggregate"):

        total_weight = matric_weight + fsc_weight + test_weight

        if total_weight != 100:
            st.error(
                f"Weightages must total 100%. Current total = {total_weight}%"
            )
        else:

            aggregate = (
                matric * matric_weight / 100
                + fsc * fsc_weight / 100
                + entry_test * test_weight / 100
            )

            st.success(
                f"Your estimated aggregate is: {aggregate:.2f}%"
            )


# ---------------------------------------------------------
# PROGRAMS
# ---------------------------------------------------------

elif page == "🎓 Programs":

    st.header("🎓 Programs & Departments")

    selected = st.selectbox(
        "Select a program",
        list(PROGRAMS.keys())
    )

    data = PROGRAMS[selected]

    st.subheader(selected)

    st.write("**Duration:**", data["duration"])
    st.write("**Type:**", data["type"])
    st.write("**Eligibility:**", data["eligibility"])

    st.subheader("Possible Career Areas")

    careers = {
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
        ]
    }

    for career in careers[selected]:
        st.write("•", career)


# ---------------------------------------------------------
# SCHOLARSHIPS
# ---------------------------------------------------------

elif page == "💵 Scholarships":

    st.header("💵 Scholarship Finder")

    st.write(
        "Below are common scholarship categories. Actual eligibility "
        "depends on the institution and scholarship provider."
    )

    for scholarship in SCHOLARSHIPS:

        with st.expander(scholarship["name"]):

            st.write(
                "**Basic Criteria:**",
                scholarship["criteria"]
            )

            st.write(
                "**Possible Documents:**",
                scholarship["documents"]
            )


# ---------------------------------------------------------
# IMPORTANT DATES
# ---------------------------------------------------------

elif page == "📅 Important Dates":

    st.header("📅 Important Admission Dates")

    st.info(
        "Replace these sample dates with the official dates of your university, "
        "college or school."
    )

    dates = {
        "Admissions Open": "01 September",
        "Application Deadline": "30 September",
        "Entry Test": "10 October",
        "Merit List": "20 October",
        "Fee Submission Deadline": "25 October",
        "Classes Begin": "01 November"
    }

    for event, date in dates.items():

        col1, col2 = st.columns([2, 1])

        with col1:
            st.write(f"**{event}**")

        with col2:
            st.write(date)


# ---------------------------------------------------------
# GPA / CGPA CALCULATOR
# ---------------------------------------------------------

elif page == "📈 GPA / CGPA Calculator":

    st.header("📈 GPA / CGPA Calculator")

    st.write(
        "Enter your courses, credit hours and grade points."
    )

    number_of_courses = st.number_input(
        "Number of courses",
        min_value=1,
        max_value=10,
        value=4
    )

    total_quality_points = 0.0
    total_credit_hours = 0.0

    for i in range(int(number_of_courses)):

        col1, col2 = st.columns(2)

        with col1:
            credit = st.number_input(
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

        total_quality_points += credit * grade_point
        total_credit_hours += credit

    if st.button("Calculate GPA"):

        if total_credit_hours > 0:

            gpa = total_quality_points / total_credit_hours

            st.success(f"Your GPA is: {gpa:.2f}")

        else:
            st.error("Please enter valid credit hours.")


# ---------------------------------------------------------
# DOCUMENT CHECKLIST
# ---------------------------------------------------------

elif page == "📄 Documents Checklist":

    st.header("📄 Admission Documents Checklist")

    st.write(
        "Tick the documents that you already have."
    )

    completed = 0

    for i, document in enumerate(DOCUMENTS):

        if st.checkbox(document, key=f"document_{i}"):
            completed += 1

    total = len(DOCUMENTS)

    st.progress(completed / total)

    st.write(
        f"Completed: **{completed}/{total}**"
    )

    if completed == total:
        st.success("🎉 All documents are ready!")


# ---------------------------------------------------------
# AI STUDENT ASSISTANT
# ---------------------------------------------------------

elif page == "🤖 AI Student Assistant":

    st.header("🤖 AI Student Assistant")

    st.write(
        "Ask questions about admissions, fees, scholarships, programs, "
        "GPA/CGPA or general student guidance."
    )

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:

        st.warning(
            "GROQ_API_KEY is not configured. Add your Groq API key "
            "to Streamlit Secrets to use the AI assistant."
        )

        st.info(
            "The other features of this application can still be used "
            "without the AI API."
        )

    question = st.text_area(
        "Ask your question:",
        placeholder="Example: What documents are normally required for admission?"
    )

    if st.button("Ask AI"):

        if not question.strip():

            st.error("Please enter a question.")

        elif not api_key:

            st.error(
                "Please configure GROQ_API_KEY in Streamlit Secrets first."
            )

        elif Groq is None:

            st.error(
                "Groq package is not installed. Check requirements.txt."
            )

        else:

            try:

                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful student assistant. "
                                "Answer questions about education, admissions, "
                                "fees, scholarships, programs, GPA and student "
                                "life in simple language. Do not invent official "
                                "university information. If information can vary "
                                "by institution, clearly tell the student to "
                                "verify it from the official institution."
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

                st.subheader("AI Answer")
                st.write(answer)

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "🎓 AI Student Assistant | Always verify official admission and fee information "
    "from the relevant institution."
)
```

### `requirements.txt`

:::writing{variant="standard" id="74106" title="requirements.txt"}
```txt
streamlit
groq
```

### ⚠️ ایک important بات

Is version mein **sample fee, dates, programs aur scholarship information** rakhi gayi hai. Real app mein kisi specific university/college/school ki **official information** add karni hogi.

Aur AI Assistant ke liye Streamlit Cloud mein:

**App → Settings → Secrets**

mein:

```text
GROQ_API_KEY = "your_groq_api_key"
```

add karna hoga.

### 🚀 Streamlit deployment

GitHub repository mein sirf ye 2 files upload karke bhi start kar sakte ho:

```text
student-assistant/
│
├── app.py
└── requirements.txt
```

Phir **Streamlit Community Cloud → Create app → GitHub repository → `app.py` → Deploy**.

Baad mein hum is app ko **real university data + PDF/RAG + FAISS** ke saath upgrade kar sakte hain, jisse student official prospectus/fee-policy PDFs se questions pooch sake.
