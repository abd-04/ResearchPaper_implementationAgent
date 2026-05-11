from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from backend.tools.pdf_tool import extract_pdf_text
from backend.graph.graph import graph


app = FastAPI(
    title="PaperToCode API"
)


# ---------------- CORS ---------------- #

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- HEALTH CHECK ---------------- #

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# ---------------- ANALYZE ENDPOINT ---------------- #

@app.post("/analyze")
async def analyze_paper(file: UploadFile = File(...)):

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        file.filename
    )

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf_text = extract_pdf_text(pdf_path)

    initial_state = {

        "pdf_text": pdf_text,

        "paper_title": file.filename.replace(".pdf", ""),

        "extracted_title": "",

        "plan": "",

        "github_repos": [],

        "generated_code": "",

        "paper_summary": "",

        "explanation": "",

        "output_package": {},

        "current_step": "started"
    }

    result = graph.invoke(initial_state)

    output_folder = result["output_package"]["folder"]


    # ---------------- LOAD GENERATED FILES ---------------- #

    summary_path = os.path.join(
        output_folder,
        "paper_summary.md"
    )

    explanation_path = os.path.join(
        output_folder,
        "explanation.md"
    )

    implementation_path = os.path.join(
        output_folder,
        "implementation.py"
    )

    references_path = os.path.join(
        output_folder,
        "references.md"
    )


    with open(summary_path, "r", encoding="utf-8") as f:
        summary = f.read()

    with open(explanation_path, "r", encoding="utf-8") as f:
        explanation = f.read()

    with open(implementation_path, "r", encoding="utf-8") as f:
        implementation = f.read()

    with open(references_path, "r", encoding="utf-8") as f:
        references = f.read()


    # ---------------- RETURN RESPONSE ---------------- #

    return {

        "paper_title": result.get(
            "extracted_title",
            file.filename
        ),

        "summary": summary,

        "implementation": implementation,

        "explanation": explanation,

        "references": references
    }