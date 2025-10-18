from __future__ import annotations
from collections import deque
from typing import Deque, Dict, List, Literal, TypedDict
import json, os

Role = Literal["user", "assistant", "system"]

class Msg(TypedDict):
    role: Role
    content: str

# ------------------ Mémoire courte RAM (FIFO) ------------------
MEM_MAX = int(os.getenv("MEMORY_MAX", "5"))
_store: Dict[str, Deque[Msg]] = {}

def _bucket(user_id: str) -> Deque[Msg]:
    if user_id not in _store:
        _store[user_id] = deque(maxlen=MEM_MAX)
    return _store[user_id]

def add_message(user_id: str, role: Role, content: str) -> int:
    b = _bucket(user_id)
    b.append({"role": role, "content": content})
    return len(b)

def get_history(user_id: str) -> List[Msg]:
    return list(_bucket(user_id))

def clear(user_id: str) -> None:
    _store.pop(user_id, None)

# ------------------ Classe Memory (profil) ------------------
class Memory:
    def __init__(self, profile_path: str = "profile.json"):
        self.profile_path = profile_path
        self.example_path = "profile.example.json"

    def get_profile(self) -> dict:
        path = self.profile_path
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            if os.path.exists(self.example_path):
                with open(self.example_path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        # Fallback raisonnable
        return {"name": "Companion", "tone": "fr-chaleureux", "timezone": os.getenv("TIMEZONE", "Europe/Paris")}