# ==========================================
# AfriMind AI Learning Engine
# Version 16.7
# Self Learning System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os



# ==========================
# KNOWLEDGE FILE
# ==========================

KNOWLEDGE_FILE = "data/knowledge.json"



# ==========================
# CREATE KNOWLEDGE DATABASE
# ==========================

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



# ==========================
# LOAD KNOWLEDGE
# ==========================

def load_knowledge():

    create_knowledge_file()


    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# ==========================
# SAVE KNOWLEDGE
# ==========================

def save_knowledge(data):

    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



# ==========================
# TEACH AFRIMIND
# ==========================

def teach_afrimind(question, answer):


    knowledge = load_knowledge()


    knowledge[question.lower()] = answer


    save_knowledge(
        knowledge
    )


    return (
        "Thank you. I have learned this information."
    )



# ==========================
# SEARCH LEARNED KNOWLEDGE
# ==========================

def get_learned_answer(question):


    knowledge = load_knowledge()


    question = question.lower()


    if question in knowledge:

        return knowledge[question]


    return None