# Basic validation functions

def validate_plan(plan: dict):
    legs = plan.get('legs', [])
    preferences = plan.get('preferences', {})
    budget = preferences.get('budget')

    total_estimate = 0
    conflicts = []
    for leg in legs:
        # Mock estimate: flight + 2 nights hotel
        flight_est = 15000
        hotel_est = 2 * 4000
        total_estimate += flight_est + hotel_est

    budget_ok = True if (budget is None or total_estimate <= budget) else False

    # Mock conflict check (no real timestamps in sample)
    conflicts = []

    return {
        'budget_ok': budget_ok,
        'es
