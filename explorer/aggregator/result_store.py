"""
Simple persistent result store for the Parallel Idea Engine.
For now uses JSON; can be upgraded to SQLite later.
"""

import json
import os
from typing import List, Dict

STORE_PATH = "/var/lib/parallella-idea-engine/results.json"

def load_results() -> List[Dict]:
    if not os.path.exists(STORE_PATH):
        return []
    with open(STORE_PATH, "r") as f:
        return json.load(f)

def save_results(results: List[Dict]):
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    with open(STORE_PATH, "w") as f:
        json.dump(results, f, indent=2)

def add_result(idea: Dict):
    results = load_results()
    results.append(idea)
    save_results(results)