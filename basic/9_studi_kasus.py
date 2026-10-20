# 1.untuk memanggil Pydantic dan Asyncio:
import asyncio
from pydantic import BaseModel, ValidationError

# 2. Buat Model Data Pydantic (Satpam Data)
class AnalisaTransaksi(BaseModel):
    status_aman: bool
    pesan_ai: str

# 3. Buat Fungsi AI Asynchronous
async def cek_transaksi_ai(nominal: int):
    await asyncio.sleep(2)  # jeda waktu berpikir
    if nominal > 1_000_000:
        return{"status_aman": False, "pesan_ai": "Nominal terlalu besar" }
    else:
        return {"status_aman": True, "pesan_ai": "Transaksi aman"}
    
# 4. Buat Sistem POS dengan Error Handling
async def proses_pembayaran(nominal: int):
    try:
        data_mentah = await cek_transaksi_ai(nominal)  # memanggil fungsi AI

        # validasi data mentah menjadi model Pydantic
        hasil_valid = AnalisaTransaksi.model_validate(data_mentah)

        print(f"Transaksi disetujui. kata AI: {hasil_valid.pesan_ai}")

    # ini adalah error khusus jika Pydantic menolak data).
    except ValidationError as e:
        print("Sistem AI mengembalikan format data yang salah! Transaksi ditunda.")

print("--- Tes Transaksi Normal ---")
asyncio.run(proses_pembayaran(50_000))

print("\n--- Tes Transaksi Mencurigakan ---")
asyncio.run(proses_pembayaran(2_000_000))
