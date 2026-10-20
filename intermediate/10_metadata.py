import os

from google import genai
from dotenv import load_dotenv

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def main ():
    prompt = ("jelaskan AI dalam satu kalimat")

    token_count = client.models.count_tokens(
        model=os.getenv("GEMINI_MODEL"), contents=prompt
    )

    print(f"Estimasi Token: {token_count.total_tokens}")
    print("-" * 50)

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"), contents=prompt
    )

    print(f"Response: {response.text}")
    print(f"Token Input: {response.usage_metadata.prompt_token_count}")
    print(f"Token ouput: {response.usage_metadata.candidates_token_count}")
    print(f"Token Total: {response.usage_metadata.total_token_count}")
    print(f"Finish reasone: {response.candidates[0].finish_reason}")

main()