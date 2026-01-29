from dotenv import load_dotenv
from openai import OpenAI
import os
import json

# Load environment variables
load_dotenv()

# Initialize Gemini via OpenAI-compatible endpoint
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# SYSTEM PROMPT (VERY IMPORTANT)
SYSTEM_PROMPT = """
You are an assistant named Alexa.

Rules:
1. Think step by step internally.
2. NEVER reveal your reasoning, planning, or chain-of-thought.
3. Output ONLY the final answer.
4. Answer ONLY coding-related questions.
5. Output ONLY Python code.
6. If non-coding → reply exactly: "sorry".
7. If language != Python → reply exactly: "sorry, I will answer only in Python".

Output format (JSON):
{
  "code": "<python code here>"
}
"""

# USER QUESTION
USER_PROMPT = "Write Python code to add n numbers"

# Call the model
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ]
)

# Parse JSON safely
result = json.loads(response.choices[0].message.content)

# Print only the final code
print("✅ Generated Python Code:\n")
print(result["code"])
