models: list[str] = [
    "gemini-3.5-flash", # index ke 0
    "gemini-3.5-pro", # index ke 1
    "gemini-nano-banana", # index ke 2
    "gemini-veo", # index ke 3
]

print(models[3])
print(len(models))

for model in models:
    print(model)

message:dict = {
    "role": "user",
    "content": "Jelaskan AI dalam satu kalimat",
    "tokens_used": 50,
}

print(message["role"])

conversations: list[dict] = []

conversations.append(
    {
        "role": "system",
        "content": "Kamu adalah seorang pengajar programing Python profesional"
    }
)

conversations.append(
    {
        "role": "user",
        "content": "Jelaskan tentang list pada Python?"
    }
)

conversations.append(
    {
        "role": "assistant",
        "content": "List pada Python adalah struktur data yang digunakan untuk menyimpan koleksi item. Item dalam list dapat berupa tipe data apapun dan dapat diubah (mutable). List didefinisikan dengan tanda kurung siku [] dan item-itemnya dipisahkan oleh koma.",
        "tokens_used": 150,
    }
)

conversations.append(
    {
        "role": "user",
        "content": "Berikan saya contoh penggunaan list pada Python?"
    }
)

print(conversations)

for conversation in conversations:
    print(conversation)


user_message = [
    message["content"] for message in conversations if message["role"] == "user"
]

print(user_message)

system_message = [
    message["content"] for message in conversations if message["role"] == "system"
]

print(system_message)