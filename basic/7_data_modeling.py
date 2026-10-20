from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str
    token_used: int

class LLMResponse(BaseModel):
    message: ChatMessage # nested inheritance

# simulasi data mentah "raw" dari LLM Provider
raw = {
    "message": {
        "role": "user",
        "content": "Jelaskan AI dalam satu kalimat",
        "token_used": 50,
    }
}


result = LLMResponse.model_validate(raw) # memvalidasi data mentah "raw" menjadi model Pydantic
print(result.message.content) # mengakses data dari model Pydantic


