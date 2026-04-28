import json

from pathlib import Path

BASE_DIR = Path(__file__).parent
LEADERBOARD_FILE = BASE_DIR / "leaderboard.json"

MAX_ENTRIES = 10


def load_leaderboard() -> list[dict]:
    if not LEADERBOARD_FILE.exists():
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)
            
        # Validate basic structure
        if isinstance(data, list):
            return data[:MAX_ENTRIES]
    except (json.JSONDecodeError, OSError):
        pass
    return []


def save_leaderboard(entries: list[dict]) -> None:
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(entries[:MAX_ENTRIES], f, indent=2)


def add_entry(name: str, score: int, distance: int, coins: int) -> list[dict]:
    entries = load_leaderboard()
    
    entries.append({
        "name":     name,
        "score":    score,
        "distance": distance,
        "coins":    coins,
    })
    
    entries.sort(key=lambda e: e["score"], reverse=True)
    entries = entries[:MAX_ENTRIES]
    
    save_leaderboard(entries)
    
    return entries


def calculate_score(coins: int, distance: int, powerup_bonuses: int = 0) -> int:
    return coins * 10 + distance + powerup_bonuses