# ==========================================
# AfriMind Intelligence Tracker
# Version 27.3
# Knowledge Growth Monitoring System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



TRACKER_FILE = "data/intelligence_tracker.json"



# ==========================================
# CREATE TRACKER STORAGE
# ==========================================

def create_tracker_file():


    if not os.path.exists(TRACKER_FILE):

        with open(
            TRACKER_FILE,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                {},
                file,
                indent=4
            )



# ==========================================
# RECORD NEW KNOWLEDGE
# ==========================================

def record_knowledge(question, answer):


    create_tracker_file()


    with open(
        TRACKER_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)



    key = question.lower()



    if key not in data:


        data[key] = {

            "answer": answer,

            "learned_date":
            str(datetime.now()),

            "usage":
            1

        }


    else:


        data[key]["usage"] += 1



    with open(
        TRACKER_FILE,
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
# GET KNOWLEDGE STATISTICS
# ==========================================

def get_learning_stats():


    create_tracker_file()


    with open(
        TRACKER_FILE,
        "r",
        encoding="utf-8"
    ) as file:


        data = json.load(file)



    return {

        "total_knowledge":
        len(data),

        "status":
        "AfriMind is learning"

    }