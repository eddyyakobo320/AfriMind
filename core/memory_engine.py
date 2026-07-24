# ==========================================
# AfriMind Memory Engine
# Version 16.3
# Intelligent Memory System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os


# Memory file location

MEMORY_FILE = "data/memory.json"



# ==========================================
# CREATE MEMORY FILE
# ==========================================

def create_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:

            json.dump({}, file, indent=4)



# ==========================================
# LOAD MEMORY
# ==========================================

def load_memory():

    create_memory()

    with open(MEMORY_FILE, "r") as file:

        return json.load(file)



# ==========================================
# SAVE MEMORY
# ==========================================

def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:

        json.dump(
            memory,
            file,
            indent=4
        )



# ==========================================
# REMEMBER INFORMATION
# ==========================================

def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return "Memory saved successfully."



# ==========================================
# RECALL INFORMATION
# ==========================================

def recall(key):

    memory = load_memory()

    return memory.get(key)



# ==========================================
# TEST MEMORY SYSTEM
# ==========================================

if __name__ == "__main__":

    print(
        "AfriMind Memory Engine Version 16.3 is running."
    )

    remember(
        "creator",
        "Edward Yakobo Mganga"
    )


    print(
        recall("creator")
    )