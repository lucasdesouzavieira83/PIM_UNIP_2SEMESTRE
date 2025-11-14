import json, os
from threading import RLock
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.abspath(os.path.join(BASE, '..', 'data'))
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, 'data.json')
_lock = RLock()
DEFAULT = {"turmas":{}, "alunos":{}, "aulas":{}, "atividades":{}}

def load_db():
    with _lock:
        if not os.path.exists(DB_PATH):
            with open(DB_PATH, 'w', encoding='utf-8') as f:
                json.dump(DEFAULT, f, indent=2, ensure_ascii=False)
            return DEFAULT.copy()
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception:
                return DEFAULT.copy()

def save_db(db):
    with _lock:
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(db, f, indent=2, ensure_ascii=False)
