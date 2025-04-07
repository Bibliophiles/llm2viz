from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://models.inference.ai.azure.com")


app = FastAPI()

# Allow CORS (so React frontend can talk to FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_llm(question: Question):
    prompt = f"Explain the following computer science concept in simple terms:\n{question.question}"

    response = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful computer science tutor."},
        {"role": "user", "content": prompt},
    ],
     temperature=1,
    max_tokens=4096,
    top_p=1)

    answer = response.choices[0].message.content
    return {"answer": answer}
