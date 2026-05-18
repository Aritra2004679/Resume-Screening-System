import streamlit as st
from pathlib import Path
import tempfile

from parsers.resume_parser import ResumeParser
from extractors.keyword_extractor import KeywordExtractor
from matcher.scorer import ResumeScorer


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Screening System")


# ---------------------------------------------------
# Input Section
# ---------------------------------------------------

jd_text = st.text_area(
    "Paste the Job Description Here:",
    height=300
)

uploaded_files = st.file_uploader(
    "Upload Resume Files:",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)


# ---------------------------------------------------
# Initialize Components
# ---------------------------------------------------

resume_parser = ResumeParser()
keyword_extractor = KeywordExtractor()
resume_scorer = ResumeScorer()


# ---------------------------------------------------
# Resume Screening Logic
# ---------------------------------------------------

if st.button("Screen Resumes", type="primary"):

    if not jd_text.strip():
        st.warning("Please enter a job description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()


    st.info("Processing resumes...")


    # Example JD Skills
    # Later this can come from jd_parser.py
    required_skills = {
        "Python",
        "SQL",
        "Machine Learning"
    }

    preferred_skills = {
        "TensorFlow",
        "PyTorch",
        "Deep Learning"
    }


    results = []


    for uploaded_file in uploaded_files:

        # Save uploaded file temporarily
        suffix = Path(uploaded_file.name).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(uploaded_file.read())

            temp_path = temp_file.name


        try:
            # Parse Resume
            resume_text = resume_parser.extract_text(temp_path)

            # Extract Skills
            extracted_skills = keyword_extractor.extract_skills(
                resume_text
            )

            # Dummy Experience & Keyword Counts
            experience_matches = 5
            keyword_matches = len(extracted_skills)

            # Calculate Score
            score_data = resume_scorer.calculate_score(
                resume_skills=extracted_skills,
                required_skills=required_skills,
                preferred_skills=preferred_skills,
                experience_matches=experience_matches,
                keyword_matches=keyword_matches
            )

            results.append({
                "Resume": uploaded_file.name,
                "Score": score_data["final_score"],
                "Skills": ", ".join(sorted(extracted_skills))
            })

        except Exception as error:

            st.error(
                f"Error processing {uploaded_file.name}: {error}"
            )


    # ---------------------------------------------------
    # Ranking Results
    # ---------------------------------------------------

    results = sorted(
        results,
        key=lambda x: x["Score"],
        reverse=True
    )


    st.subheader("Ranked Candidates")

    for rank, result in enumerate(results, start=1):

        st.markdown(f"### #{rank} - {result['Resume']}")

        st.write(f"Score: {result['Score']}")

        st.write(f"Skills: {result['Skills']}")

        st.divider()