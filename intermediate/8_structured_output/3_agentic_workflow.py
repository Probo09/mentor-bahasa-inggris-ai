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

class GrammarReportSchema(BaseModel):
    score : int = Field(... , description="Skor kemampuan dari 1-100")
    corrected_text : str = Field(... , description="Text pengguna yang sudah diperbaiki tata bahasa inggris-nya")
    explanation: str = Field(... , description="Penjelasan detail mengenai kesalahan ")

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

def check_grammar(text: str) -> GrammarReportSchema:

    prompt = f"Periksa grammar dari tulisan berikut: {text}"

    SYSTEM_INSTRUCTION="""
        [ROLE] Kamu seorang guru bahasa inggris virtual yang ramah dan supportif untuk orang indonesia
        [RULES]
        - Periksa grammar, ejaan dan struktur kalimat 
        - Berikan skor yang jujur dan objektif
        [RESPONSE] Gunakan schema GrammarReportSchema untuk menampilkan hasil penilaian 
        """
    
    response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION, 
                response_json_schema=GrammarReportSchema.model_json_schema(),
            ),
            contents=prompt,
        )
    
    return GrammarReportSchema.model_validate(json.loads(response.text))

def main():
    prompt = input("Ketik kalimat bahasa inggris yang ingin diperiksa: \n")
    classification = classify_message(text=prompt)
    print(f"Kategori    : {classification.kategori}")
    print(f"Alasan      : {classification.alasan}")
    print()

    if classification.kategori == "grammar_check":
        report = check_grammar(prompt)
        print(f"Skor            : {report.score}")
        print(f"Koreksi         : {report.corrected_text}")
        print(f"Penjelasan      : {report.explanation}")
    elif classification.kategori == "obrolan":
        print(
            "Hallo!, Ayo ngobrol seputar belajar bahasa inggris. kirim kalimat yang ingin kamu pelajari"
        )
    else:
        print("Maaf!, saya hanya bisa membantu memeriksa tulisan bahasa inggris kamu. ")


main()