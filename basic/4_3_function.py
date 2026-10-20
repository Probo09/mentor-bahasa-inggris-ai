# Ini adalah data profil user yang dikirim ke fungsi

data_user:dict = {
    "nama": "Fawwaz",
    "role": "user",
    "kuota_token": 100,
    "pesan": "Tolong perbaiki grammar saya.",
}

def proses_pesan_ai(data_user:dict, biaya_token:int):

    if data_user["kuota_token"] >= biaya_token:
        data_user["kuota_token"] -= biaya_token
        data_user["status"] = "sukses"
    else:
        data_user["status"] = "Gagal - Kuota Habis"
    return data_user

hasil_satu = proses_pesan_ai(data_user, 30)

print(hasil_satu)