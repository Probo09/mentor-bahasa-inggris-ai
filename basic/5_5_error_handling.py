# Riwayat chat (List of strings untuk menyederhanakan)
riwayat_chat = [
    "Hello Mentor!",                         # Indeks 0
    "Hi! How can I help?",                   # Indeks 1
    "Tolong jelaskan simple past tense.",    # Indeks 2
]

def ambil_pesan(urutan:int):
    try:
        pesan = riwayat_chat[urutan]
        print("pesan ditemukan:", pesan)

    except IndexError:
        print("Error: Pesan tidak ditemukan. Nomor urutan terlalu besar!")


ambil_pesan(1)
ambil_pesan(10)
