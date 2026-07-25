# ==========================================
# AfriMind AI Conversation Engine
# Version 22.0
# Conversation Intelligence System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime


CONVERSATION_FILE = "data/conversations.json"



# ==========================================
# CREATE STORAGE
# ==========================================

def initialize_conversation():

    if not os.path.exists(CONVERSATION_FILE):

        with open(
            CONVERSATION_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4,
                ensure_ascii=False
            )



# ==========================================
# SAVE CONVERSATION
# ==========================================

def save_conversation(
        user_message,
        ai_response
):

    initialize_conversation()


    with open(
        CONVERSATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        conversations = json.load(file)



    conversations.append({

        "time": str(datetime.now()),

        "user": user_message,

        "afrimind": ai_response

    })



    with open(
        CONVERSATION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            conversations,

            file,

            indent=4,

            ensure_ascii=False

        )



    return True



# ==========================================
# GET RECENT CONVERSATIONS
# ==========================================

def get_recent_conversations(limit=5):

    initialize_conversation()


    with open(
        CONVERSATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        conversations = json.load(file)



    return conversations[-limit:]



# ==========================================
# FIND PREVIOUS TOPIC
# ==========================================

def get_previous_topic():

    conversations = get_recent_conversations(1)


    if conversations:

        return conversations[0].get(
            "user"
        )


    return None



# ==========================================
# SEARCH CONVERSATION HISTORY
# ==========================================

def search_conversation(keyword):

    initialize_conversation()


    with open(
        CONVERSATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        conversations = json.load(file)



    results = []


    for conversation in conversations:

        user_message = conversation.get(
            "user",
            ""
        ).lower()


        if keyword.lower() in user_message:

            results.append(
                conversation
            )


    return results