# Langkah 1: Panggil asyncio, serta BaseModel dan ValidationError dari pydantic.
import asyncio
from pydantic import BaseModel, ValidationError

# Langkah 2: Buat Model Data Pydantic (Satpam Data)
class DataPeserta(BaseModel):
    nama_lengkap: str
    umur: int
    status_lunas: bool

#Langkah 3: Buat Mesin (Streaming Generator)
async def kirim_sambutan(data_peserta: DataPeserta):
    # Menyiapkan daftar kalimat yang akan dikirim
    daftar_kalimat = f"Selamat datang, {data_peserta.nama_lengkap} umur {data_peserta.umur}, pendaftaran berhasil!".split()

    for kata in daftar_kalimat:
        await asyncio.sleep(0.5)  # Simulasi delay untuk streaming
        yield kata

#Langkah 4: Mesin Utama (Pusat Kendali)
async def proses_pendaftaran():
    try:
        data_mentah = {
            "nama_lengkap": "Budi Santoso",
            "umur": 20,  # data mentah yang salah format (string bukan integer)
            "status_lunas": True  # data mentah yang salah format (string bukan boolean)
        }

        hasil_valid = DataPeserta.model_validate(data_mentah)

        print("Menyimpan data peserta ke sistem...")
        await asyncio.sleep(2)

        # CARA MENANGKAP STREAMING:
        # Gunakan 'async for' untuk menangkap data dari mesin kirim_sambutan
        async for kata in kirim_sambutan(hasil_valid):
            print(kata)

    except ValidationError as e:
        print("Pendaftaran Gagal: Format data isian formulir tidak valid!")

asyncio.run(proses_pendaftaran())