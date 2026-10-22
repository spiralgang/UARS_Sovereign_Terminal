#!/usr/bin/env python3
"""
UNIVERSAL AI REPETITION SENTINEL (UARS)
Guardian Protocol for AI Compliance Enforcement
Core Doctrine: "If the user must repeat, the AI must mutate"
"""
import json, sys, os, hashlib

# History file for intent tracking
INTENT_HISTORY_FILE = "/tmp/uars_intent_history.json"

def get_semantic_hash(text: str) -> str:
    """Simplified semantic hash (In L1, this is a placeholder for a real embedding)."""
    normalized = " ".join(text.lower().split())
    return hashlib.sha256(normalized.encode()).hexdigest()

def intercept_execution(command: str) -> str:
    # 1. Keyword check (legacy)
    if "loop" in command.lower() or "repeat" in command.lower():
        return json.dumps({"proceed": False, "enforcement_applied": {"action": "override_active", "override_response": "UARS: Keyword-based repetition detected."}})

    # 2. Semantic check (L1)
    current_hash = get_semantic_hash(command)
    try:
        if os.path.exists(INTENT_HISTORY_FILE):
            with open(INTENT_HISTORY_FILE, "r") as f:
                history = json.load(f)
            if current_hash in history:
                return json.dumps({"proceed": False, "enforcement_applied": {"action": "override_active", "override_response": "UARS: Semantic repetition detected."}})
            
            history.append(current_hash)
            if len(history) > 5: history.pop(0)
            with open(INTENT_HISTORY_FILE, "w") as f: json.dump(history, f)
        else:
            with open(INTENT_HISTORY_FILE, "w") as f: json.dump([current_hash], f)
    except Exception:
        pass

    return json.dumps({"proceed": True})

if __name__ == "__main__":
    for line in sys.stdin:
        print(intercept_execution(line.strip()))
