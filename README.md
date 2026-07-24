# ==========================================
# AfriMind Memory System
# Created by Edward Yakobo Mganga
# ==========================================

import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    else:
        return {}


def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key)

    ### Version 3.0
- Added SQLite database system
- Added database.py
- Added setup_database.py
- Connected brain.py with afrimind.db
- Added AI learning through database

### Version 3.1
- Added user memory system
- Added welcome back feature
- Improved memory.py functions
- Connected Main.py with memory system
- Added personal assistant capability