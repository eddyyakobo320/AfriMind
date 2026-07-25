# ==========================================
# AfriMind Knowledge Engine
# Version 18.0
# Self Learning Knowledge Management System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os


# Location of learned knowledge

KNOWLEDGE_FILE = "data/learned.json"



# ==========================================
# CREATE KNOWLEDGE FILE
# ==========================================

def create_knowledge_file():

    if not os.path.exists(KNOWLEDGE_FILE):

        with open(
            KNOWLEDGE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {},
                file,
                indent=4
            )



# ==========================================
# LOAD KNOWLEDGE
# ==========================================

def load_knowledge():

    create_knowledge_file()

    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# ==========================================
# SAVE KNOWLEDGE
# ==========================================

def save_knowledge(data):

    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



# ==========================================
# SEARCH KNOWLEDGE
# ==========================================

def search_knowledge(question):

    knowledge = load_knowledge()

    question = question.lower().strip()


    if question in knowledge:

        return knowledge[question]


    return None



# ==========================================
# TEACH AFRIMIND
# ==========================================

def add_knowledge(question, answer):

    knowledge = load_knowledge()


    question = question.lower().strip()


    knowledge[question] = answer


    save_knowledge(
        knowledge
    )


    return (
        "Thank you. "
        "I have learned this knowledge."
    )



# ==========================================
# SHOW KNOWLEDGE SIZE
# ==========================================

def knowledge_count():

    knowledge = load_knowledge()

    return len(knowledge)