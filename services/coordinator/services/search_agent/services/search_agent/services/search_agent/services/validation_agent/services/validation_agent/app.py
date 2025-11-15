from fastapi import FastAPI
from pydantic import BaseModel
from validator import validate_plan

app = FastAPI()

class ValidatePayload(BaseModel):
    plan: dict

@app.post('/validate')
async def validate(payload: ValidatePayload):
    plan = payload.plan
    results = validate_plan(plan)
    return results

@app.get('/health')
async def health():
    return {"status": "ok"}
