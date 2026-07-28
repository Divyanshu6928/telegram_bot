import json
from google import genai
from config import GEMINI_API_KEY
from config import MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are an expert data analyst.

The user may ask questions about:
- CSV data
- Excel files
- JSON
- Public datasets
- MOSPI
- Statistics

Always solve the problem.

IMPORTANT:
Return ONLY the requested JSON object.
Never include markdown.
Never explain your reasoning.
"""

def solve(question, history):
    prompt = SYSTEM_PROMPT + "\n\n"

    for msg in history:
        prompt += f"{msg['role']}: {msg['content']}\n"

    prompt += f"user: {question}"

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )                   

    return response.text.strip()