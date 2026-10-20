from pydantic import BaseModel

class ScoreData(BaseModel):
    score: int
    feedback: str

class AgentResponse(BaseModel):
    intent: str
    result_data: ScoreData # nested inheritance

raw_evaluation = {
    "intent": "grammar_scoring",
    "result_data": {
        "score": 95,
        "feedback": "Excellent use of past tense!"
    }
}

valid_response =  AgentResponse.model_validate(raw_evaluation) # memvalidasi data mentah "raw" menjadi model Pydantic

print(valid_response.result_data.score) # mengakses data dari model Pydantic
print(valid_response.result_data.feedback) # mengakses data dari model Pydantic