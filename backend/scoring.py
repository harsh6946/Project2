import re
from collections import Counter

def compute_scores(resume_text: str, job_description: str) -> dict:
    # Clean and tokenize
    resume_words = re.findall(r"\w+", resume_text.lower())
    jd_words = re.findall(r"\w+", job_description.lower())

    resume_counts = Counter(resume_words)
    jd_counts = Counter(jd_words)

    # Keyword overlap
    matched_keywords = set(resume_counts.keys()) & set(jd_counts.keys())
    keyword_score = (len(matched_keywords) / max(len(jd_counts), 1)) * 100

    # Length score (just a demo logic)
    length_score = min(len(resume_words) / 200 * 100, 100)

    # Overall score
    overall_score = round((keyword_score * 0.7 + length_score * 0.3), 2)

    return {
        "overall_score": overall_score,
        "keyword_score": round(keyword_score, 2),
        "length_score": round(length_score, 2),
        "matched_keywords": list(matched_keywords)
    }
