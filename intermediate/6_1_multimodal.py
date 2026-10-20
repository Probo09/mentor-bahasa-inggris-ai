import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path

# Membaca file .env
load_dotenv()

# Membuka koneksi ke server Google
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  

def image_generation():
    prompt = input("Prompt image generation: \n")
    print("Sedang melukis gambar di server Google... Mohon tunggu sebentar.")

    # KITA KEMBALI MENGGUNAKAN generate_content (Standar Paling Baru!)
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL_IMAGE"),
        contents=[prompt]
    )

    file_name = "generated.jpeg"
    directory = "multimodal"

    file_path = Path(directory)
    file_path.mkdir(exist_ok=True)

    # Mengekstrak balasan AI (karena output-nya bisa berupa teks atau gambar)
    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(f"{directory}/{file_name}")

    print("Image successfully generated!")
 
def main():
    image_generation()

if __name__ == "__main__":
    main()