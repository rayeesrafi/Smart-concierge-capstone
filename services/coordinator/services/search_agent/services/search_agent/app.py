from fastapi import FastAPI
from pydantic import BaseModel
from search_tools import mock_search

app = FastAPI()

class SearchPayload(BaseModel):
    plan: dict

@app.post('/search')
async def search(payload: SearchPayload):
    plan = payload.plan
    results = {}
    for leg in plan.get('legs', []):
        flights = mock_search('flights', leg)[:3]
        hotels = mock_search('hotels', leg)[:3]
        activities = mock_search('activities', leg)[:3]
        results[leg['dest']] = {'flights': flights, 'hotels': hotels, 'activities': activities}
    return {'results': results}

@app.get('/health')
async def health():
    return {"status": "ok"}
