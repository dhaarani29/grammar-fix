from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


class RewriteRequest(BaseModel):
    text: str
    action: str

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.post("/rewrite")
def rewrite(req: RewriteRequest):

    prompt = f"""
    Perform this action: {req.action}

    Text:
    {req.text}
    """

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a professional writing assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "result": response.get("message", {}).get("content", "")
    }