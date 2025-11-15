import requests

COORD = "http://localhost:8000"

def test_sample_plan():
    payload = {
        "user_id": "testuser",
        "request": {
            "origin": "BLR",
            "destinations": ["SIN"],
            "start_date": "2026-01-10",
            "end_date": "2026-01-15",
            "preferences": {"budget": 60000}
        }
    }

    r = requests.post(f"{COORD}/plan", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert "search_results" in data
    assert "validation" in data
