import json
import os

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

DEFAULTS: dict = {
    "snake_color": [0, 200, 0], # RGB list (JSON-serialisable)
    "grid_overlay": True
}

def load_settings() -> dict:
    settings = dict(DEFAULTS)
    
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            settings.update(data)
        except (json.JSONDecodeError, OSError):
            pass  # corrupt file = use defaults
        
    return settings


def save_settings(settings: dict) -> None:
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as fh:
            json.dump(settings, fh, indent=2)
    except OSError as exc:
        print(f"[settings] save failed: {exc}")