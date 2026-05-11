from langchain_groq import ChatGroq
from dotenv import load_dotenv
from backend.prompts.summary_prompt import SUMMARY_PROMPT

import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def summary_node(state):

    print("\n--- SUMMARY NODE ---")

    prompt = SUMMARY_PROMPT.format(
        paper_text=state["pdf_text"][:12000]
    )

    response = llm.invoke(prompt)

    return {
        "paper_summary": response.content,
        "current_step": "summary_completed"
    }