def call_llm():
    raise ValueError("terjadi kesalahan pada function call_llm")

try: # 'ruang' untuk mengeksekusi function atau logika program
    call_llm()
    print("sukses")
except ValueError as e:
    # 'ruang' untuk mengendalikan kesalahan 
    print(f"Error: {e}")
finally:
    # opsional
    print("sesi berakhir")