# Data pesan dari user yang sudah dianalisis intent-nya
pesan_user = {
    "role": "user",
    "content": "I goes to market yesterday.",
    "intent": "curhat" 
}

if pesan_user["intent"] == "grammar_check":
    print("Sistem Agentic: Mengaktifkan mode koreksi Grammar...")
elif pesan_user["intent"] == "translate":
    print("Sistem Agentic: Mengaktifkan mode Translate...")
else :
    print("Sistem Agentic: Mengaktifkan mode Obrolan Biasa...")