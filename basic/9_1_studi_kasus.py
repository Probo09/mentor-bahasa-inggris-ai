# Langkah 1 perlengkapan bawaan Python Pydantic dan Asyncio:
import asyncio
from pydantic import BaseModel, ValidationError

# Langkah 2: Pembuatan Cetakan Data (Satpam) Model Data Pydantic
class PesananKasir(BaseModel):
    nama_produk: str
    harga_satuan: int
    kuantitas: int

# Langkah 3: Mesin Cetak Animasi
async def animasi_struk(data_pesanan: PesananKasir):
    # Menghitung total.
    # Karena data_pesanan sudah divalidasi oleh Pydantic, 
    # kita memanggil datanya menggunakan TITIK (dot notation), bukan kurung siku!
    total_harga = data_pesanan.harga_satuan * data_pesanan.kuantitas

    # Menyiapkan daftar kalimat yang akan dicetak
    daftar_kalimat = [
        "Menyiapkan struk...",
        f"Item: {data_pesanan.nama_produk} x {data_pesanan.kuantitas}",
        f"Total Tagihan: Rp {total_harga}"
    ]

    # Melakukan perulangan untuk menelusuri daftar kalimat
    for kalimat in daftar_kalimat:
        # 1. Berikan jeda istirahat selama 1 detik (ingat cara merebus air / simulasi delay)
        await asyncio.sleep(1)
        
        # 2. Lemparkan kalimatnya ke luar mesin satu per satu (ingat mesin pelempar bola tenis)
        yield(kalimat)

# Langkah 4: Sistem Kasir dengan Penanganan Error
async def proses_struk():
    try:
        data_mentah ={
                "nama_produk": "Beras",
                "harga_satuan": 15000,
                "kuantitas": "13"  # data mentah yang salah format (string bukan integer)
            }

        # validasi data mentah menjadi model Pydantic
        hasil_valid = PesananKasir.model_validate(data_mentah)

        print("Mengirim pesan ke database")
        await asyncio.sleep(2)

        # CARA MENANGKAP STREAMING:
        # Gunakan 'async for' untuk menangkap data dari mesin animasi_struk
        async for baris_teks in animasi_struk(hasil_valid):
            print(baris_teks)

    except ValidationError as e:
            print("Peringatan: Scanner barcode membaca format yang salah. Transaksi dibatalkan!")

asyncio.run(proses_struk())