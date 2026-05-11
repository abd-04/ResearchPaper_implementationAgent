from typing import TypedDict, List


class PaperState(TypedDict):
    pdf_text: str
    paper_title: str

    plan: str

    github_repos: List[dict]

    generated_code: str

    output_package: dict

    current_step: str
    extracted_title: str
    paper_summary: str
    explanation: str