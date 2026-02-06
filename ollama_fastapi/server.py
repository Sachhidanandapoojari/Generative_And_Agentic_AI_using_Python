from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client

app = FastAPI()

client = Client(host="http://127.0.0.1:11434")


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(payload: ChatRequest):
    response = client.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a coding assistant. "
                    "Return ONLY the complete code. "
                    "No explanation. No markdown. No examples."
                )
            },
            {
                "role": "user",
                "content": payload.message
            }
        ]
    )

    code = response.message.content
    code = code.replace("```python", "").replace("```", "").strip()

    return {"response": code}

@app.get("/")
def read():
    return {"hello": "world"}

@app.get("/contact-us")
def contact():
    return {"email": "sachin@gmail.com"}
