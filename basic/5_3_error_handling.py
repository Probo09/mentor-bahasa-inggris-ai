angka = int("10")

try:
    angka = int("sepuluh")
    print("berhasil diubah")

except ValueError:
    print("Error: Yang Anda masukkan bukan angka!")

finally:
    print("Program selesai.")