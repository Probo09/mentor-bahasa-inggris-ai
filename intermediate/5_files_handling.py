import shutil

from pathlib import Path


def main ():
    file_name = "sample.txt"
    directory = "downloads"

    # Menentukan Lokasi Tujuan (Path)
    file_path = Path(f"{directory}/{file_name}")

    # Membuat Folder dengan Aman (mkdir)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    #Menulis dan Membaca File (One-Liner)
    file_path.write_text("Halo, Tulisan ini disimpan di file sample.txt")
    content = file_path.read_text(encoding="utf-8")
    print(content)

    # Bersih-bersih (Menghapus Jejak)
    file_path.unlink(missing_ok=True)
    shutil.rmtree(directory)

main()