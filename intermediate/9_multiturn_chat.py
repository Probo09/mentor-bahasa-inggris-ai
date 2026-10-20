import os
import json

from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel, Field 
from typing import Literal

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conversation_history: list[types.Content] = []

def save_message(role: str, message_text: str):
    conversation_history.append(
        types.Content(role=role, parts=[types.Part(text=message_text)])
    )

def load_history() -> list[types.Content]:
    return conversation_history

def main():
    while True:
        prompt = input("Kamu: ")

        if prompt.lower() == "/exit":
            break

        save_message(role="user", message_text=prompt)

        history = load_history()

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"), contents=history
        )

        save_message(role="model", message_text=response.text)

        print(f"AI: {response.text}")

main()