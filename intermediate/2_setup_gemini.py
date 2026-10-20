import os

from google import genai

from dotenv import load_dotenv

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# mengirimkan teks ke model yang kamu tentukan.
def main():
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents="Jelaskan apa itu AI Agentic dalam bahasa Indonesia dengan singkat dan jelas.",
    )

    # menampilkan hasilnya
    print(response.text)


main()