import os

# bertugas memanggil library dotenv agar bisa membaca file .env.
from dotenv import load_dotenv

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# bertugas masuk ke file tersebut, mencari label GEMINI_API_KEY, dan mengambil value-nya.
gemini_api_key = os.getenv("GEMINI_API_KEY")

# bertugas masuk ke file tersebut, mencari label GEMINI_MODEL, dan mengambil value-nya.
gemini_model = os.getenv("GEMINI_MODEL")    

# cetak value dari GEMINI_MODEL dan GEMINI_API_KEY ke layar.
print(gemini_model)
print(gemini_api_key)

