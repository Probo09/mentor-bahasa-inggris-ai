from pydantic import BaseModel

# 1. Membuat "cetakan" (Model)
class ProfilUser(BaseModel):
    nama: str
    umur: int
    is_active: bool

# 2. Menggunakan cetakan untuk membuat data
user_satu = ProfilUser(nama="Fawwaz", umur=25, is_active=True)

print(user_satu.nama) # Output: Fawwaz