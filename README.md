# 📄 Resume Screening System using Python

An AI-inspired Resume Screening System built with Python and Streamlit.
The system automatically parses resumes, extracts technical skills, analyzes job descriptions, calculates weighted scores, and ranks candidates based on relevance.

---

# 🌐 Live Demo

https://idfitoasczbvfcw9cqmpma.streamlit.app

---

# 🚀 Features

✅ Resume Parsing (PDF & DOCX)
✅ Job Description Parsing
✅ Rule-Based Skill Extraction
✅ Weighted Resume Scoring Engine
✅ Candidate Ranking System
✅ Streamlit Web Interface
✅ Dataset Analysis using Jupyter Notebook
✅ Modular Project Architecture

---

# 🏗️ Project Architecture

```text
Resume Upload
      ↓
📄 Resume Parser
      ↓
🧾 JD Parser
      ↓
🧠 Keyword Extractor
      ↓
📊 Scoring Engine
      ↓
🏆 Candidate Ranking
      ↓
🌐 Streamlit Web Interface
```

---

# 🛠️ Tech Stack

* 🐍 Python
* 🌐 Streamlit
* 📊 Pandas
* 🔢 NumPy
* 📄 PyPDF2
* 📝 python-docx
* 📈 Matplotlib
* 📓 Jupyter Notebook

---

# 📁 Project Structure

```text
RESUME_SCREENING_SYSTEM/
│
├── data/
│   ├── Resume.csv
│   ├── cleaned_resume_dataset.csv
│   └── sample_resumes/
│
├── extractors/
│   └── keyword_extractor.py
│
├── matcher/
│   └── scorer.py
│
├── notebooks/
│   └── data_extraction.ipynb
│
├── parsers/
│   ├── jd_parser.py
│   └── resume_parser.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── app.py
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd Resume_Screening_System
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows PowerShell

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Run Streamlit Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# ☁️ Deployment

This project is deployed using Streamlit Community Cloud.

Live Application:

https://idfitoasczbvfcw9cqmpma.streamlit.app

---

# 💼 Sample Job Description

```text
Job Title: AI/ML Engineer Intern

Required Skills:
- Python
- Machine Learning
- SQL
- Pandas
- NumPy

Preferred Skills:
- NLP
- Streamlit
- Docker
- TensorFlow

Experience:
- Internship/project experience in AI or Machine Learning
```

---

# 📊 Scoring Formula

The system calculates candidate scores using weighted scoring logic:

* 🎯 Required Skills → 50%
* ⭐ Preferred Skills → 25%
* 💼 Experience → 15%
* 🔑 Keywords → 10%

Final Formula:

Total Score =
(S_req × 0.50) +
(S_pref × 0.25) +
(E_exp × 0.15) +
(K_key × 0.10)

---

# 📚 Dataset

Dataset used in this project:

Resume Dataset from Kaggle:
https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

---

# 🧪 Sample Output

```text
============================================================
SCREENING RESULTS
============================================================

🏆 Rank #1: Alice Johnson | Score: 85.42/100
Matched Skills: Python, Django, PostgreSQL

🥈 Rank #2: Carol Davis | Score: 72.50/100
Matched Skills: Python, Django
```

---

# 🔮 Future Improvements

* 🤖 NLP-based semantic matching
* 📐 TF-IDF similarity scoring
* 🧠 spaCy skill extraction
* 🚀 AI-powered resume understanding
* 📅 Experience duration extraction
* 📊 Dashboard analytics
* 🗄️ Database integration
* 💡 LLM-based candidate evaluation

---

# 👨‍💻 Author

Developed using Python and Streamlit as a modular Resume Screening and Candidate Ranking System.
