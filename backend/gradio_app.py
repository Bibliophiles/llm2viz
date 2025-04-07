import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load OpenAI API Key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://models.inference.ai.azure.com")

# Main function to query OpenAI
def ask_cs_llm(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're a helpful computer science tutor."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Gradio Interface
interface = gr.Interface(
    fn=ask_cs_llm,
    inputs=gr.Textbox(lines=2, placeholder="Ask a computer science question...", label="Your Question"),
    outputs=gr.Textbox(label="LLM Answer"),
    title="💡 CS Visualizer (Text-Only Layer 1)",
    description="Ask a computer science question and get a natural language answer from GPT-4."
)

interface.launch(share=True)
