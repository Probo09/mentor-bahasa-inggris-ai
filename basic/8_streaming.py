import asyncio

async def stream_tokens(prompt: str):

    words = f"Agentic AI membuat rencana dan eksekusi secara otomatis untuk prompt: {prompt}".split()
    for word in words:
        await asyncio.sleep(1)  # Simulate delay for streaming
        yield word

async def collect_Stream(prompt: str):
    tokens : list[str] = []
    print("Streaming: ", end=" ", flush=True)

    async for chunk in stream_tokens(prompt):
        print(chunk, end="", flush=True)
        tokens.append(chunk)

    print()

    return " ".join(tokens)

result = asyncio.run(collect_Stream("Jelaskan AI dalam satu kalimat."))
print(f"full response {len(result.split())} tokens: {result}")
