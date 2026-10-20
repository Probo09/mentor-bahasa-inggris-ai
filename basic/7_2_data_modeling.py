from pydantic import BaseModel

class EvaluasiGrammar(BaseModel):
    skor: int
    feedback: str

hasil_ai = EvaluasiGrammar(skor=85, feedback="Tenses yang digunakan sudah tepat, tapi perhatikan pemilihan katanya.")

print(hasil_ai.skor) # Output: 85