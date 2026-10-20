# 1. Membuat jenis error buatan kita sendiri
class SaldoTidakCukupError(Exception): 
    pass

# 2. Membuat fungsi untuk mengecek dan memotong saldo
def bayar_tagihan(saldo:int, tagihan:int):
    # Jika saldo kurang dari tagihan, hentikan paksa (raise error)
    if saldo < tagihan:
        raise SaldoTidakCukupError("Maaf, Saldo anda kurang.")

    # Jika tidak error (saldo cukup), potong saldonya
    saldo = saldo - tagihan
    return saldo

# 3. Area Uji Coba (Pertunjukan Akrobat)
try:
    print("Mencoba melakukan pembayaran...")
    # Kita sengaja memasukkan saldo 50.000, tapi tagihannya 75.000
    sisa_saldo = bayar_tagihan(50000, 75000) 
    
    # Baris di bawah ini TIDAK AKAN dieksekusi karena keburu error di atasnya
    print(f"Pembayaran sukses. Sisa saldo: {sisa_saldo}")

except SaldoTidakCukupError as e:
    # Jaring pengaman menangkap error dari fungsi bayar_tagihan
    print(f"Transaksi Gagal: {e}")

finally:
    # Selalu dieksekusi di akhir
    print("Sesi transaksi ditutup.")
