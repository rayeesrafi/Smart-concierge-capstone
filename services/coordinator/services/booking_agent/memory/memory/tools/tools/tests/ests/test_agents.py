from services.search_agent.search_tools import mock_search
from services.validation_agent.validator import validate_plan

def test_mock_search():
    leg = {"dest": "SIN", "start_date": "2026-01-10"}
    results = mock_search("flights", leg)
    assert isinstance(results, list)
    assert len(results) > 0

def test_validator():
    plan = {"legs": [{"dest": "SIN"}], "preferences": {"budget": 60000}}
    result = validate_plan(plan)
    assert "budget_ok" in result
