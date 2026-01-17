from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client=OpenAI(
    api_key="AIzaSyCIRrn8QxZeJngfk-tob3cbODiogBFMd5Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

resp=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hey, I am Sachin! Nice to meet you"}
    ]
)
print(resp.choices[0].message.content)