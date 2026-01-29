from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client=OpenAI(
    api_key="AIzaSyBKVL33dqdTdEG2PWOQI56jgAE6qpbF64c",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

resp=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "can you give me about lyrynx in biology"}
    ]
)
print(resp.choices[0].message.content)