import asyncio

async def stream_proses_berpikir ():
    langkah_langkah = [
        "Menganalisa Prompt...",
        "Mencari Konnteks..",
        "Menyusun Kalimat...",
        "Selesai"
    ]

    for Langkah in langkah_langkah:
        await asyncio.sleep(1)  # Simulate delay for streaming
        yield Langkah

async def jalankan_sistem():
    async for proses in stream_proses_berpikir():
        print(proses)

result = asyncio.run(jalankan_sistem())