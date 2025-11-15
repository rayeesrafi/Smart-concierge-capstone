from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import httpx
from coordinator import handle_request

app = FastAPI()

SEARCH_AGENT_URL = os.getenv("SEARCH_AGENT_URL", "http://localhost:8001")
VALIDATION_AGENT_URL = os.getenv("VALIDATION_AGENT_URL", "http://localhost:8002")
BOOKING_AGENT_URL = os.getenv("BOOKING_AGENT_URL", "http://localhost:8003")

class PlanRequest(BaseModel):
    user_id: str
    request: dict

@app.post('/plan')
async def plan(req: PlanRequest):
    try:
        itinerary = await handle_request(req.user_id, req.request)
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/health')
async def health():
    return {"status": "ok"}
