# ==========================================
# AfriMind Memory System
# Created by Edward Yakobo Mganga
# ==========================================

import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    """Load memory from memory.json"""

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {}


def save_memory(memory):
    """Save memory into memory.json"""

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):
    """Save one value"""

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):
    """Read one value"""

    memory = load_memory()

    return memory.get(key)

def forget(key):
    """Delete one memory"""

    memory = load_memory()

    if key in memory:
        del memory[key]

        save_memory(memory)


def get_all_memory():
    """Return all saved memory"""

    return load_memory()

def update_memory(key, value):
    """Update existing memory"""

    memory = load_memory()

    memory[key] = value

    save_memory(memory)