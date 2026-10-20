# 1. Import library asyncio
import asyncio

# 2. Mendefinisikan fungsi async (Garis bawah diganti dengan 'async')
async def proses_pesan_ai(pesan: str):
    print(f"User: {pesan}")
    print("AI sedang berpikir secara Asynchronous...")
    
    # 3. Buat simulasi delay selama 3 detik (Garis bawah diganti dengan 'await')
    await asyncio.sleep(3)
    
    # 4. Kembalikan jawaban
    return "Yes, your grammar is getting better!"

# 5. Fungsi utama (entry point)
async def main():
    print("--- Memulai Aplikasi Chatbot ---")
    
    # 6. Memanggil fungsi async HARUS menggunakan await (Garis bawah diganti dengan 'await')
    jawaban = await proses_pesan_ai("Did I write this correctly?")
    
    print(f"AI: {jawaban}")

# 7. Menjalankan seluruh program async
asyncio.run(main())