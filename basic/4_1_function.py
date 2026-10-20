# 1. Mendefinisikan fungsi
def proses_intent(intent_user):
    # 2 & 3. Logika if/elif/else menjorok ke dalam fungsi
    # Evaluasi menggunakan parameter 'intent_user'
    if intent_user == "grammar_check":
        return "Sistem Agentic: Mengaktifkan mode koreksi Grammar..."
    
    elif intent_user == "translate":
        return "Sistem Agentic: Mengaktifkan mode Translate..."
    
    else:
        return "Sistem Agentic: Mengaktifkan mode Obrolan Biasa..." 

# 4. Menguji fungsi (berada di luar fungsi, sejajar di garis paling kiri)
hasil_satu = proses_intent("grammar_check")
hasil_dua = proses_intent("translate")
hasil_tiga = proses_intent("curhat")

print(hasil_satu)
print(hasil_dua)
print(hasil_tiga)