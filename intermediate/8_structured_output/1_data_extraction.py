import os
import json

from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel, Field 

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#schema
class ArticleMetaSchema(BaseModel):
    judul: str = Field(... , description="Judul artikel")
    penulis: str = Field(... , description="Nama penulis artikel")
    tanggal: str = Field(... , description="Tanggal publikasi artikel")
    ringkasan: str = Field(... , description="Ringkasan singkat isi artikel dalam 1-2 kalimat")

def extract_article_meta(text: str) -> ArticleMetaSchema:

    prompt = f"ekstrak informasi dari artikel berikut ini: {text}"
    SYSTEM_INSTRUCTION="""
    [ROLE] Kamu seorang asisten yang bertugas untuk mengekstrak informasi dari sebuah artikel
    [RULES]
    - Ekstrak hanya informasi yang tersedia di dalam teks
    - Jika informasi tidak ditemukan, maka di isi dengan "Tidak tersedia"
    [RESPONSE] Gunakan schema ArticleMetaSchema untuk menampilan hasil ekstraksi 
    """

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION, 
            response_json_schema=ArticleMetaSchema.model_json_schema(),
        ),
        contents=prompt,
    )

    return ArticleMetaSchema.model_validate(json.loads(response.text))

def main():
    sample_article = """
    Belajar python Agentic AI: Panduan pemula
    Oleh: Agung | 22 Juni 2026

    Artificial Intelligence (AI) kini semakin mudah diakses oleh siapa saja, termasuk pemula.
    Dengan python dan berbagai library seperti google-genai, siapapun bisa mulai membangun aplikasi berbasis AI 
    Dalam waktu singkat
    """

    meta = extract_article_meta(text=sample_article)

    print(f"Judul       : {meta.judul}")
    print(f"Penulis     : {meta.penulis}")
    print(f"Tanggal     : {meta.tanggal}")
    print(f"Ringkasan   : {meta.ringkasan}")

main()