chat_history = [
    {"role": "system", "content": "You are an English mentor."},
    {"role": "user", "content": "Hello!", "tokens_used": 5},
    {"role": "assistant", "content": "Hi! How can I help your English?", "tokens_used": 15},
    {"role": "user", "content": "Please explain simple past tense.", "tokens_used": 10},
    {"role": "assistant", "content": "Simple past tense is used for past events...", "tokens_used": 40}
]

# TUGAS 1: Menghitung total token
total_token = 0

for message in chat_history:
    # Cek apakah key "tokens_used" ada di dalam dictionary pesan ini
    if "tokens_used" in message:
        # Jika ada, tambahkan angkanya ke variabel total_token
        total_token = total_token + message["tokens_used"]
        # Bisa juga disingkat menjadi: total_token += message["tokens_used"]

print(f"Total token yang digunakan: {total_token}")


# TUGAS 2: Menambahkan fitur "Centang Biru" (is_read: True) untuk pesan user
for message in chat_history:
    # Cari pesan yang role-nya adalah user
    if message["role"] == "user":
        # Tambahkan key dan value baru ke dictionary tersebut
        message["is_read"] = True

# Cetak hasil akhirnya untuk melihat perubahan
print(chat_history)