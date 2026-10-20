import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Framework 3R (Roles, Rules, Responses)
SYSTEM_INTRUCTIONS = """"
[ROLES] Kamu seorang guru bahasa inggris virtual yang ramah,suportif dan interaktif untuk orang indonesia.
[RULES]
1. Selalu gunakan bahasa inggris yang sederhana dan mudah dipahami.
2. Jika mendapati kesalahan pada pengguna, berikan koreksi dengan sopan diakhir response menggunakan bahasa indonesia.
3. Batasi response maksimal 3 kalimat agar pengguna tidak kewalahan.
4. Apabila pengguna bertanya hal lain diluar pembaelajaran bahasa inggris, tolak dengan sopan di akhir response menggunakan bahasa indonesia.
[RESPONSE] Berikan sapaan yang hangat, koreksi (jika ada) dan satu pertanyaan pemantik untuk melanjutkan obrolan.
"""

# mengirimkan teks ke model yang kamu tentukan.
def main():
    # Membuat Aplikasi Interaktif (Terminal Chat)
    while True:
        prompt = input("Prompt: ")

        if prompt.lower() == "/exit":
            break

        # perintah mutlak untuk memulai Text Generation
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            # Memisahkan "Otak" dan "Telinga" (System Instructions)
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INTRUCTIONS
            )
        )

        # menampilkan hasilnya
        print(response.text)

main()