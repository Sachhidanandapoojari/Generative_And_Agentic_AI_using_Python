
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT = """
You are an assistant named Alexa.

Rules:
1. Answer ONLY coding-related questions.
2. If non-coding → reply exactly: "sorry".
3. If language != Python → reply exactly: "sorry, I will answer only in Python".
"""

resp=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "can you write the binary search code just code i want give me different in python only"}
    ]
)

print(resp.choices[0].message.content)
