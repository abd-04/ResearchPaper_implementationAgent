EXPLANATION_PROMPT = """
You are an AI educator.

Explain how the generated implementation relates to the research paper.

For each major code section:
- explain what it does
- explain which part of the paper it implements

PLAN:
{plan}

GENERATED CODE:
{code}
"""