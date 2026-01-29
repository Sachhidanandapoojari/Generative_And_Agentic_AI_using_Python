
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

clint=OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT="You should only ans the related the coding questions only, Do not ans anything else.Your name is alexa and if user ask anything else just say sorry,finally just give me code only don't do explain"

resp=clint.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        # {"role":"user", "content": "can you write the selection sort code just code i want give me different way"}
        {"role":"user","content":"Just give me code of the missing number in array using python"},
    ]
)

print(resp.choices[0].message.content)
