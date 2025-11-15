import os
import httpx
from llm_client import LLMClient
from memory.memory_store import MemoryStore

llm = LLMClient()
memory = MemoryStore()

SEARCH_AGENT_URL = os.getenv('SEARCH_AGENT_URL', 'http://localhost:8001')
VALIDATION_AGENT_URL = os.getenv('VALIDATION_AGENT_URL', 'http://localhost:8002')
BOOKING_AGENT_URL = os.getenv('BOOKING_AGENT_URL', 'http://localhost:8003')

async def handle_request(user_id: str, user_request: dict):
    # Load session
    session = memory.load_session(user_id) or {}
    context = {'user_request': user_request, 'session': session}

    # Ask LLM for plan
    plan = llm.plan(context)

    # Dispatch search and validation in parallel
    async with httpx.AsyncClient(timeout=30.0) as client:
        search_task = client.post(f"{SEARCH_AGENT_URL}/search", json={'plan': plan})
        validate_task = client.post(f"{VALIDATION_AGENT_URL}/validate", json={'plan': plan})
        search_resp, validate_resp = await search_task, await validate_task

        search_results = search_resp.json()
        validation_results = validate_resp.json()

    # Merge results
    itinerary = {
        'plan': plan,
        'search_results': search_results,
        'validation': validation_results
    }

    # Save to session memory
    memory.save_session(user_id, itinerary)

    return itinerary
