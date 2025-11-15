def sync_to_calendar(user_id: str, itinerary: dict):
    # Mock: pretend to add events to a calendar
    count = len(itinerary.get("plan", {}).get("legs", []))
    return {"status": "synced", "events_added": count}
