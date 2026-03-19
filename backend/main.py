from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import analyze_code

app = FastAPI()

class CodeRequest(BaseModel):
    code: str
    task: str

@app.post("/analyze")
def analyze(request: CodeRequest):

    result = analyze_code(request.code, request.task)

    return {"result": result}