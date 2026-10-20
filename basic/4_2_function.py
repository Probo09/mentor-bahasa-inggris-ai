def hitung_pembayaran(harga_satuan:int, jumlah_beli:int, status_member:bool ):
    total:int = harga_satuan * jumlah_beli

    # Mengecek apakah dia member (Jika True, potong 10 ribu)
    if status_member:
        total = total - 10_000

    return total

result:int = hitung_pembayaran(
    harga_satuan=50_000,
    jumlah_beli=2,
    status_member=False
)

print(result)

def hitung_pembayaran(harga_satuan:int, jumlah_beli:int, status_member:bool):
    total:int = harga_satuan * jumlah_beli
    
    # Mengecek apakah dia member (Jika True, potong 10 ribu)
    if status_member:
        total = total - 10_000
        
    return total


# Menguji 1: Untuk Member
bayar_member:int = hitung_pembayaran(
    harga_satuan=50_000,
    jumlah_beli=2,
    status_member=True
)

# Menguji 2: Untuk Non-Member
bayar_non_member:int = hitung_pembayaran(
    harga_satuan=50_000,
    jumlah_beli=2,
    status_member=False
)

print(f"Total bayar Member: Rp.{bayar_member}")
print(f"Total bayar Non-Member: Rp.{bayar_non_member}")