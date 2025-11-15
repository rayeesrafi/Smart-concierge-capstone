import os
import json
from pathlib import Path

DB_PATH = os.getenv("MEMORY_DB", "memory/db.json")
Path(os.path.dirname(DB_PATH) or ".").mkdir(parents=True, exist_ok=True)

class MemoryStore:
    def __init__(self, path=DB_PATH):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def load_session(self, user_id: str):
        with open(self.path, "r") as f:
            db = json.load(f)
        return db.get(user_id)

    def save_session(self, user_id: str, data: dict):
        with open(self.path, "r") as f:
            db = json.load(f)
        db[user_id] = data
        with open(self.path, "w") as f:
            json.dump(db, f, indent=2)
