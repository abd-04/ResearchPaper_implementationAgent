from langchain_groq import ChatGroq
from dotenv import load_dotenv
from backend.prompts.planner_prompt import PLANNER_PROMPT

import os
import re

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_title(plan_text):

    match = re.search(r"TITLE:\s*(.*)", plan_text)

    if match:
        return match.group(1).strip()

    return "Unknown Paper"


def planner_node(state):

    print("\n--- PLANNER NODE ---")

    pdf_text = state["pdf_text"][:12000]

    prompt = PLANNER_PROMPT.format(
        paper_text=pdf_text
    )

    response = llm.invoke(prompt)

    plan = response.content

    extracted_title = extract_title(plan)

    print("\nEXTRACTED TITLE:\n")
    print(extracted_title)

    return {

        "plan": plan,

        "extracted_title": extracted_title,

        "current_step": "planning_completed"
    }