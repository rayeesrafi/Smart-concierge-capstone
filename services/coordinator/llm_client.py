# Mock LLM client to keep this repo runnable without external keys.
# Replace with real model adapter when you want to use a real LLM.

class LLMClient:
    def plan(self, context: dict) -> dict:
        # Very simple deterministic plan: break into legs for each destination
        user_req = context.get('user_request', {})
        # Example plan shape
        plan = {
            'legs': [
                {
                    'origin': user_req.get('origin'),
                    'dest': d,
                    'start_date': user_req.get('start_date'),
                    'end_date': user_req.get('end_date')
                } for d in user_req.get('destinations', [])
            ],
            'preferences': user_req.get('preferences', {})
        }
        return plan
