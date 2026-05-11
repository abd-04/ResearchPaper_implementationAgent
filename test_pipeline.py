from backend.tools.pdf_tool import extract_pdf_text
from backend.graph.graph import graph


pdf_text = extract_pdf_text("sample_pdf.pdf")

initial_state = {
    "pdf_text": pdf_text,
    "paper_title": "Sample Paper",

    "plan": "",

    "github_repos": [],

    "generated_code": "",

    "output_package": {},

    "paper_summary": "",
    "explanation": "",

    "current_step": "started"
}

result = graph.invoke(initial_state)

print("\nFINAL RESULT:\n")
print(result["output_package"])