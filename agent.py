from google import genai

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


SYSTEM_PROMPT = """
You are an expert data analyst.

You receive questions from Telegram.

Some questions include:

CSV

Tables

Government datasets

MOSPI URLs

GitHub URLs

JSON

Excel

Analyze them carefully.

IMPORTANT

Your final output MUST be only the requested JSON.

No markdown.

No explanations.

No extra text.
"""


def solve(question, history):

    prompt = SYSTEM_PROMPT

    for item in history:
        prompt += f"\n{item['role']}: {item['content']}"

    prompt += f"\nUser: {question}"

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text