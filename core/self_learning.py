# ==========================================
# AfriMind Self Learning Engine
# Version 27.4
# Autonomous Knowledge Improvement System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



LEARNING_FILE = "data/self_learning.json"



# ==========================================
# CREATE STORAGE
# ==========================================

def create_learning_file():


    if not os.path.exists(LEARNING_FILE):

        with open(
            LEARNING_FILE,
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

def save_new_knowledge(question, answer):


    create_learning_file()


    with open(
        LEARNING_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)



    key = question.lower()



    if key in data:


        data[key]["times_used"] += 1



    else:


        data[key] = {

            "answer": answer,

            "learned_date":
            str(datetime.now()),

            "times_used":
            1

        }



    with open(
        LEARNING_FILE,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



    return True



# ==========================================
# GET LEARNED KNOWLEDGE
# ==========================================

def get_new_knowledge(question):


    create_learning_file()


    with open(
        LEARNING_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)



    key = question.lower()


    if key in data:

        return data[key]["answer"]



    return None



# ==========================================
# LEARNING STATUS
# ==========================================

def learning_status():


    create_learning_file()


    with open(
        LEARNING_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)



    return {

        "knowledge_count":
        len(data),

        "message":
        "AfriMind self learning is active"

    }