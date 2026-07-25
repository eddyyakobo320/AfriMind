# ==========================================
# AfriMind Learning Memory Engine
# Version 27.1
# Automatic Knowledge Storage System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os



KNOWLEDGE_FILE = "data/learned_knowledge.json"



# ==========================================
# CREATE STORAGE
# ==========================================

def create_learning_file():


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
# SAVE NEW KNOWLEDGE
# ==========================================

def save_learned_answer(
        question,
        answer
):


    create_learning_file()


    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:


        knowledge = json.load(file)



    knowledge[question.lower()] = answer



    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(
            knowledge,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True



# ==========================================
# GET LEARNED KNOWLEDGE
# ==========================================

def get_learned_answer(
        question
):


    create_learning_file()


    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8"
    ) as file:


        knowledge = json.load(file)



    return knowledge.get(
        question.lower(),
        None
    )