from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PLAYERS_FILE = DATA_DIR / "players.json"
ENEMIES_FILE = DATA_DIR / "enemies.json"
ROOMS_FILE = DATA_DIR / "rooms.json"