from typing import Set, Dict


class ResumeScorer:

    def calculate_score(
        self,
        resume_skills: Set[str],
        required_skills: Set[str],
        preferred_skills: Set[str],
        experience_matches: int,
        keyword_matches: int
    ) -> Dict:

        # Required Skills Score
        required_match_count = len(
            resume_skills.intersection(required_skills)
        )

        required_score = (
            required_match_count / len(required_skills)
        ) if required_skills else 0


        # Preferred Skills Score
        preferred_match_count = len(
            resume_skills.intersection(preferred_skills)
        )

        preferred_score = (
            preferred_match_count / len(preferred_skills)
        ) if preferred_skills else 0


        # Experience Score
        experience_score = min(experience_matches / 10, 1)


        # Keyword Score
        keyword_score = min(keyword_matches / 20, 1)


        # Final Weighted Score
        final_score = (
            (required_score * 0.50) +
            (preferred_score * 0.25) +
            (experience_score * 0.15) +
            (keyword_score * 0.10)
        ) * 100


        return {
            "final_score": round(final_score, 2),
            "required_matches": required_match_count,
            "preferred_matches": preferred_match_count,
            "experience_matches": experience_matches,
            "keyword_matches": keyword_matches
        }