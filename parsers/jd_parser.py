import re
from typing import Dict


class JDParser:

    def __init__(self):

        self.skill_database = {
            "Python",
            "Django",
            "REST APIs",
            "SQL",
            "PostgreSQL",
            "Docker",
            "AWS",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Java",
            "JavaScript"
        }

    def parse_job_description(self, jd_text: str) -> Dict:

        jd_lower = jd_text.lower()

        required_skills = set()
        preferred_skills = set()
        keywords = set()

        # ---------------------------------------------------
        # Extract Required Skills
        # ---------------------------------------------------

        required_section = self._extract_section(
            jd_text,
            "Required Skills:",
            "Preferred Skills:"
        )

        for skill in self.skill_database:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, required_section.lower()):
                required_skills.add(skill)

        # ---------------------------------------------------
        # Extract Preferred Skills
        # ---------------------------------------------------

        preferred_section = self._extract_section(
            jd_text,
            "Preferred Skills:",
            "Experience:"
        )

        for skill in self.skill_database:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, preferred_section.lower()):
                preferred_skills.add(skill)

        # ---------------------------------------------------
        # Extract General Keywords
        # ---------------------------------------------------

        for skill in self.skill_database:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, jd_lower):
                keywords.add(skill)

        # ---------------------------------------------------
        # Extract Experience Requirement
        # ---------------------------------------------------

        experience_match = re.search(
            r"(\d+)\+?\s+years",
            jd_lower
        )

        experience_required = (
            int(experience_match.group(1))
            if experience_match
            else 0
        )

        return {
            "required_skills": required_skills,
            "preferred_skills": preferred_skills,
            "keywords": keywords,
            "experience_required": experience_required
        }

    def _extract_section(
        self,
        text: str,
        start_keyword: str,
        end_keyword: str
    ) -> str:

        pattern = (
            re.escape(start_keyword)
            + r"(.*?)"
            + re.escape(end_keyword)
        )

        match = re.search(
            pattern,
            text,
            re.DOTALL | re.IGNORECASE
        )

        return match.group(1) if match else ""