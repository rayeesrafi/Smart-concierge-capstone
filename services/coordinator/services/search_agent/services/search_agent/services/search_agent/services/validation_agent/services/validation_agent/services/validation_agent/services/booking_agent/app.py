from fastapi import FastAPI
from pydantic import BaseModel
from booking import start_booking, resume_booking

app = FastAPI()

class BookingRequest(BaseModel):
    booking_request: dict

class BookingAction(BaseModel):
    booking_id: str
    action: str

@app.post("/start")
async def start(req: BookingRequest):
    return start_booking(req.booking_request)

@app.post("/resume")
async def resume(action: BookingAction):
    return resume_booking(action.booking_id, action.action)

@app.get("/health")
async def health():
    return {"status": "ok"}
