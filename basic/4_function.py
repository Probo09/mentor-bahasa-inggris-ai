def print_message_hello():
    print("Hello ini function 'my_function'")

def penambahan(a: int,  b:int):
    result: int = a + b
    return result

# argumen -> parameter
# proses -> logika, algoritrma -> 1 tanggung jawab
# return value -> tipe data 

result_penambahan:int = penambahan(5, 10) # argumen
print(result_penambahan)
print_message_hello()

# prompt: str
# model: str
# max_tokens: int

# menghitung biaya penggunaan token dari suatu model
# dict -> {}
# input_token: int
# output_token: int
# estimeted_cost: float

def estimate_cost(prompt: str, model: str, max_tokens: int):

    # "model": {"input": 0, "output": 0}
    pricing: dict = {
        "gemin-flash": {
            "input": 0.0005,
            "output": 0.0006
        }
    }

    rates: dict = pricing[model] # {"input": 0, "output": 0}

    input_tokens: int = len(prompt.split())

    input_cost = (input_tokens/1000) * rates["input"]
    output_cost = (max_tokens/1000) * rates["output"]

    estimated_cost = input_cost + output_cost

    return {
        "input_tokens": input_tokens,
        "output_tokens": max_tokens,
        "estimated_cost": round(estimated_cost, 5)
    }

# result:dict = estimate_cost("Jelaskan tentang AI dalam satu kalimat", "gemini-3.5-flash", 256)

result:dict = estimate_cost(
    prompt="Jelaskan tentang AI dalam satu kalimat",
    model="gemin-flash",
    max_tokens=512,
)

print(result)

