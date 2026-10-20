import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

# bertugas memindai foldermu untuk mencari file bernama .env.
load_dotenv()

# menggunakan kunci rahasia untuk membuka pintu gerbang ke server Google.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  

def image_generation():
    prompt = input("Prompt image generation: \n")

    response = client.models.generate_content(  
        model=os.getenv("GEMINI_MODEL_IMAGE"), contents=[prompt]
    )

    file_name = "generated.jpeg"
    directory = "multimodal"

    file_path = Path(directory)
    file_path.mkdir(exist_ok=True)

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(f"{directory}/{file_name}")

    print("image successfully generated!")

def image_understanding():
    with open("multimodal/sample-image.png", "rb") as f:
        image_bytes = f.read()

    prompt = input("Prompt image understanding: \n")

    response = client.models.generate_content(  
        model=os.getenv("GEMINI_MODEL"), contents=[prompt, types.part.from_bytes(data=image_bytes, mime_types="image/png"),],
    )

    print(response.text)

def video_genertation():
    prompt = input("Prompt video generation: \n")
    
    operation = client.models.generate_videos(  
        model=os.getenv("GEMINI_MODEL_VIDEO"), prompt=prompt
    )

    while not operation.done:
        print("Menunggu proses video generation selesai ..")
        time.sleep(10)
        operation = client.operations.get(operation)

    generated_video = operation.response.generated_videos[0]
    client.files.download(file=generated_video)

    generated_video.video.save("multimodal/generated-video.mp4")
    print("Video berhasil disimpan ke multimodal/generated-video.mp4")

def video_understanding():
    prompt = input("Prompt video understanding: \n")
    file_video_path = "multimodal/sample-video.mp4"

    file_video = client.files.upload(file=file_video_path)

    while file_video.state.name == "PROCESSING":
        print("Video sedang diproses")
        time.sleep(5)
        file_video = client.files.get(name=file_video.name)

    if file_video.state.name == "FAILED":
     raise ValueError("Gagal upload video")

    print("video berhasil diupload.")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents=[
            file_video,
            prompt
        ]
    )

    print(response.text)

def document_understanding():
    prompt = input("Prompt document understanding: \n")
    file_document_path = "multimodal/cv.mp4"

    file_document = client.files.upload(file=file_document_path)

    while file_document.state.name == "PROCESSING":
        print("Document sedang diproses")
        time.sleep(5)
        file_document = client.files.get(name=file_document.name)

    if file_document.state.name == "FAILED":
     raise ValueError("Gagal upload document")

    print("document berhasil diupload.")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents=[
            file_document,
            prompt
        ]
    )

    print(response.text)

def audio_understanding():
    prompt = input("Prompt audio understanding: \n")
    file_audio_path = "multimodal/sample-audio.mp3"

    file_audio = client.files.upload(file=file_audio_path)

    while file_audio.state.name == "PROCESSING":
        print("Audio sedang diproses")
        time.sleep(5)
        file_audio = client.files.get(name=file_audio.name)

    if file_audio.state.name == "FAILED":
     raise ValueError("Gagal upload audio")

    print("audio berhasil diupload.")

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents=[
            file_audio,
            prompt
        ]
    )

    print(response.text)

 
def main():
    # image_generation()
    # image_understanding()
    # video_genertation()
    # video_understanding()
    # document_understanding()
    audio_understanding()

main()