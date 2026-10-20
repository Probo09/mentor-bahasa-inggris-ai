def baca_pesan_ai(data_respon:dict):
    try:
        # Mencoba mencetak jawaban
        print("Pesan AI:", data_respon["jawaban"])

    except KeyError:
        # Menangkap error jika key "jawaban" tidak ada
        print("Maaf, sistem AI sedang mengalami gangguan. Tolong ulangi pesan Anda.")


# --- AREA PENGUJIAN ---

# Respon 1: Normal dan sukses
respon_normal = {
    "status": 200,
    "intent": "grammar_check",
    "jawaban": "Your grammar is almost perfect! Just change 'goes' to 'went'."
}

# Respon 2: Cacat (Server AI glitch, key "jawaban" hilang)
respon_cacat = {
    "status": 500,
    "intent": "unknown",
    "error_message": "Internal Server Error"
}

# Menguji fungsi
print("--- Tes Respon Normal ---")
baca_pesan_ai(respon_normal)

print("\n--- Tes Respon Cacat ---")
baca_pesan_ai(respon_cacat)