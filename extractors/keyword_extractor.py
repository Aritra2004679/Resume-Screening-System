import re
from typing import Set, Dict, List


class KeywordExtractor:

    def __init__(self):
        self.skills_taxonomy = {
            "Programming": {
                "Python": ["python"],
                "Java": ["java"],
                "JavaScript": ["javascript", "js"],
                "C++": ["c++", "cpp"],
            },

            "Data Science": {
                "Machine Learning": [
                    "machine learning",
                    "ml"
                ],
                "Deep Learning": [
                    "deep learning",
                    "dl"
                ],
                "TensorFlow": ["tensorflow"],
                "PyTorch": ["pytorch"],
            },

            "Database": {
                "SQL": ["sql"],
                "MongoDB": ["mongodb"],
                "MySQL": ["mysql"],
            }
        }

    def extract_skills(self, text: str) -> Set[str]:

        text_lower = text.lower()

        found_skills = set()

        for category, skills_dict in self.skills_taxonomy.items():

            for skill_name, variations in skills_dict.items():

                for variation in variations:

                    # Prevent partial matching
                    pattern = r"\b" + re.escape(variation.lower()) + r"\b"

                    if re.search(pattern, text_lower):
                        found_skills.add(skill_name)
                        break

        return found_skills