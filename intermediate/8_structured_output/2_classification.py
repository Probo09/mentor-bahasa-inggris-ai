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

class MessageClassSchema(BaseModel):
    kategori: Literal["grammar_check", "obrolan", "diluar_topik"]= Field(
        ... , description="kategori pesan: grammar_check jika ingin memeriksa tulisan bahasa inggris, obrolan jika percakapan biasa, dilluar_topik jika tidak relevan"  )
    alasan: str = Field(..., description="Alasan mengapa pesan tersebut masuk kategori demikian")

def classify_message(text: str) -> MessageClassSchema:

    prompt = f"Klasifikasikan pesan berikut: {text}"
    SYSTEM_INSTRUCTION="""
    [ROLE] Kamu adalah classifier pesan untuk aplikasi guru bahasa inggris virtual 
    [RULES]
    - Kategorikan pesan ke salah satu dari: grammar_check, obrolan dan diluar_topik 
    - grammar_check: pengguna mengirim kalimat bahasa inggris yang ingin diperiksa
    - obrolan: pengguna mengajak ngobrol seputar belajar bahasa inggris 
    - diluar_topik: pesan tidak ada hubungannya dengan bahasa ingggris
    [RESPONSE] Gunakan schema MessageClassSchema
    """

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION, 
            response_json_schema=MessageClassSchema.model_json_schema(),
        ),
        contents=prompt,
    )

    return MessageClassSchema.model_validate(json.loads(response.text))

def main():
    prompt = input("Ketik pesan apa saja: \n")
    result = classify_message(text=prompt)
    print(f"Kategori    : {result.kategori}")
    print(f"Alasan      : {result.alasan}")

main()