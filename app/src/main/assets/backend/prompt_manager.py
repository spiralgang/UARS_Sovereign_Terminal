import json
import requests
import os

REMOTE_PROMPTS_URL = os.getenv("SOVEREIGN_PROMPTS_URL", "https://sovereign.spiralgang.com/prompts.json")
LOCAL_PROMPTS_PATH = "assets/backend/prompts.json"

def load_prompts():
    """
    Loads prompt configurations. Prefers remote source, falls back to local assets.
    """
    # 1. Try Remote
    try:
        response = requests.get(REMOTE_PROMPTS_URL, timeout=5)
        if response.status_code == 200:
            remote_prompts = response.json()
            print(f"Successfully fetched remote prompts from {REMOTE_PROMPTS_URL}")
            return remote_prompts
    except Exception as e:
        print(f"Remote prompt fetch failed: {e}")

    # 2. Fallback to Local
    try:
        with open(LOCAL_PROMPTS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Local prompt load failed: {e}")
        return {}

def get_prompt_config(agent_id):
    """
    Returns the configuration for a specific agent ID.
    """
    prompts = load_prompts()
    return prompts.get(agent_id, {})

if __name__ == "__main__":
    # Testing the mechanism
    import sys
    agent = sys.argv[1] if len(sys.argv) > 1 else "UARS_SENTINEL"
    print(json.dumps(get_prompt_config(agent), indent=2))
