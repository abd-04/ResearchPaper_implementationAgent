from langchain_groq import ChatGroq
from dotenv import load_dotenv
from backend.prompts.explanation_prompt import EXPLANATION_PROMPT

import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def explanation_node(state):

    print("\n--- EXPLANATION NODE ---")

    prompt = EXPLANATION_PROMPT.format(
        plan=state["plan"],
        code=state["generated_code"][:12000]
    )

    response = llm.invoke(prompt)

    return {
        "explanation": response.content,
        "current_step": "explanation_completed"
    }