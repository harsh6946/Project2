from fastapi import FastAPI, UploadFile, Form
from backend.scoring import compute_scores

app = FastAPI(title="Smart Resume Analyzer")

@app.post("/analyze/")
async def analyze_resume(resume: str = Form(...), jd: str = Form(...)):
    """
    API endpoint to analyze resume text against job description.
    """
    scores = compute_scores(resume, jd)
    return scores

@app.get("/")
def home():
    return {"message": "Welcome to Smart Resume Analyzer API"}
