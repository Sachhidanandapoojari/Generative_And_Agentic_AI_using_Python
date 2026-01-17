
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

clint=OpenAI(
    api_key="AIzaSyCIRrn8QxZeJngfk-tob3cbODiogBFMd5Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# SYSTEM_PROMPT="You should only ans the related the coding questions only, Do not ans anything else.Your name is alexa and if user ask anything else just say sorry"

resp=clint.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # {"role":"system","content":SYSTEM_PROMPT},
        # {"role":"user", "content": "can you write the selection sort code just code i want give me different way"}
        {"role":"user","content":"please find the ai engineer job in india and give me the link"},
    ]
)

print(resp.choices[0].message.content)
