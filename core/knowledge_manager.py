# ==========================================
# AfriMind AI Knowledge Manager
# Version 27.5
# Central Knowledge Intelligence System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



# ==========================================
# FILE STORAGE
# ==========================================

KNOWLEDGE_FILE = "data/knowledge.json"
LEARNED_FILE = "data/learned.json"



# ==========================================
# CREATE FILE
# ==========================================

def create_file(file_path):

    if not os.path.exists(file_path):

        with open(
            file_path,
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

def load_knowledge(file_path):

    create_file(
        file_path
    )


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



# ==========================================
# SAVE KNOWLEDGE
# ==========================================

def save_knowledge(
        file_path,
        data
):

    with open(
        file_path,
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

def find_answer(question):


    question = (
        question
        .lower()
        .strip()
    )


    # Main knowledge

    knowledge = load_knowledge(
        KNOWLEDGE_FILE
    )


    if question in knowledge:

        return knowledge[question]



    # Learned knowledge

    learned = load_knowledge(
        LEARNED_FILE
    )


    if question in learned:

        return learned[question]



    return None



# ==========================================
# ADD NEW KNOWLEDGE
# ==========================================

def add_new_knowledge(
        question,
        answer
):


    question = (
        question
        .lower()
        .strip()
    )


    learned = load_knowledge(
        LEARNED_FILE
    )


    if question not in learned:


        learned[question] = {

            "answer": answer,

            "created":
            str(datetime.now()),

            "usage": 1

        }


    else:

        learned[question]["usage"] += 1



    save_knowledge(
        LEARNED_FILE,
        learned
    )


    return True



# ==========================================
# KNOWLEDGE STATISTICS
# ==========================================

def knowledge_status():


    knowledge = load_knowledge(
        KNOWLEDGE_FILE
    )


    learned = load_knowledge(
        LEARNED_FILE
    )


    return {

        "main_knowledge":
        len(knowledge),

        "learned_knowledge":
        len(learned),

        "status":
        "AfriMind knowledge system active"

    }