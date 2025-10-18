from .llm import _ensure_profile, build_system_prompt, client
import os
from typing import List, Dict

def _sanitize_history(history: List[Dict]) -> List[Dict]:
    """Garde seulement role/user|assistant et content (strings). Coupe à 5 max."""
    if not history:
        return []
    out = []
    for m in history[-5:]:
        role = m.get("role", "")
        content = m.get("content", "")
        if role in ("user", "assistant") and isinstance(content, str):
            out.append({"role": role, "content": content})
    return out

def generate_reply(user_text: str, profile_or_path="profile.json", history: List[Dict]=None) -> str:
    profile = _ensure_profile(profile_or_path)
    system = build_system_prompt(profile)

    # Mode MOCK si pas de vraie clé (ou si LLM_MOCK=1)
    k = os.getenv("OPENAI_API_KEY", "")
    mock_mode = os.getenv("LLM_MOCK") == "1" or (not k) or k.startswith("sk-PLACE")

    # Historique nettoyé (max 5)
    hist_msgs = _sanitize_history(history or [])

    if mock_mode:
        name = profile.get("name", "Companion")
        # Indice discret que l'historique est pris en compte (taille)
        return f"[MOCK] {name}: {user_text}"

    # Appel réel : system + history + user
    messages = [{"role": "system", "content": system}] + hist_msgs + [
        {"role": "user", "content": user_text}
    ]

    rsp = client().chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    return rsp.choices[0].message.content