import uuid
from typing import Dict

# Simple in-memory booking store
BOOKINGS: Dict[str, dict] = {}

def start_booking(booking_request: dict) -> dict:
    booking_id = str(uuid.uuid4())
    
    state = {
        "id": booking_id,
        "request": booking_request,
        "status": "pending",
        "steps": ["preconfirm", "payment", "finalize"],
        "current_step": 0,
        "result": None
    }

    BOOKINGS[booking_id] = state
    return {"booking_id": booking_id, "status": "pending"}

def resume_booking(booking_id: str, action: str) -> dict:
    state = BOOKINGS.get(booking_id)
    
    if not state:
        return {"error": "booking not found"}

    # Already finished
    if state["status"] == "complete":
        return {"status": "complete", "details": state["result"]}

    # Payment confirmation action
    if action == "confirm_payment" and state["current_step"] == 1:
        state["current_step"] += 1
        state["status"] = "complete"
        state["result"] = {"confirmation": f"CONF-{booking_id[:8]}"}
        return {"status": "complete", "details": state["result"]}

    # Otherwise move to next step
    state["current_step"] += 1
    if state["current_step"] >= len(state["steps"]):
        state["status"] = "waiting_for_payment"

    return {"status": state["status"], "current_step": state["current_step"]}
