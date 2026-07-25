# ==========================================
# AfriMind AI Context Engine
# Version 16.9
# Short Term Conversation Memory
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



# ==========================================
# CONTEXT FILE
# ==========================================

CONTEXT_FILE = "data/context.json"



# ==========================================
# CREATE CONTEXT STORAGE
# ==========================================

def create_context_file():

    if not os.path.exists(CONTEXT_FILE):

        with open(
            CONTEXT_FILE,
            "w"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )



# ==========================================
# SAVE CONVERSATION CONTEXT
# ==========================================

def save_context(user_message, afrimind_response):


    create_context_file()


    with open(
        CONTEXT_FILE,
        "r"
    ) as file:

        context = json.load(file)



    context.append(

        {
            "time": str(datetime.now()),
            "user": user_message,
            "afrimind": afrimind_response
        }

    )


    # Keep latest 20 conversations

    context = context[-20:]


    with open(
        CONTEXT_FILE,
        "w"
    ) as file:

        json.dump(
            context,
            file,
            indent=4
        )



# ==========================================
# GET LAST CONTEXT
# ==========================================

def get_last_context():

    create_context_file()


    with open(
        CONTEXT_FILE,
        "r"
    ) as file:

        context = json.load(file)


    if context:

        return context[-1]


    return None



# ==========================================
# SEARCH PREVIOUS CONTEXT
# ==========================================

def search_context(keyword):


    create_context_file()


    with open(
        CONTEXT_FILE,
        "r"
    ) as file:

        context = json.load(file)



    results = []


    for item in context:

        if keyword.lower() in item["user"].lower():

            results.append(item)



    return results