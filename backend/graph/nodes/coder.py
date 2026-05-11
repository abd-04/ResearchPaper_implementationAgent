from langchain_groq import ChatGroq
from dotenv import load_dotenv
from backend.prompts.coder_prompt import CODER_PROMPT

import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def coder_node(state):

    print("\n--- CODER NODE ---")

    prompt = CODER_PROMPT.format(
        plan=state["plan"],
        repos=state["github_repos"]
    )

    response = llm.invoke(prompt)

    return {
        "generated_code": response.content,
        "current_step": "code_generated"
    }