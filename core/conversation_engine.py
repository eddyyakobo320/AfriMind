# ==========================================
# AfriMind AI Conversation Engine
# Version 16.5
# Conversation Management System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



# ==========================================
# CONVERSATION MEMORY FILE
# ==========================================

MEMORY_FILE = "data/conversations.json"



# ==========================================
# CREATE CONVERSATION STORAGE
# ==========================================

def create_conversation_file():

    if not os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )



# ==========================================
# SAVE CONVERSATION
# ==========================================

def save_conversation(user_message, afrimind_reply):


    create_conversation_file()


    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        conversations = json.load(file)



    conversations.append(
        {
            "time": str(datetime.now()),
            "user": user_message,
            "afrimind": afrimind_reply
        }
    )



    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            conversations,
            file,
            indent=4
        )



# ==========================================
# BASIC CONVERSATION ENGINE
# ==========================================

def chat(message):


    message = message.lower().strip()



    # Greetings

    if message in [
        "hello",
        "hi",
        "hey",
        "habari"
    ]:

        reply = (
            "Hello! I am AfriMind AI. "
            "How can I help you today?"
        )


    # Thanks

    elif message in [
        "thank you",
        "thanks",
        "asante"
    ]:

        reply = (
            "You are welcome. "
            "I am always ready to help."
        )


    # Identity

    elif message in [
        "who are you",
        "what are you"
    ]:

        reply = (
            "I am AfriMind AI, "
            "an intelligent assistant built "
            "to provide knowledge and solutions for Africa."
        )


    else:

        reply = (
            "I am still learning. "
            "Please ask me another question."
        )



    save_conversation(
        message,
        reply
    )


    return reply



# ==========================================
# START TEST
# ==========================================

if __name__ == "__main__":

    print(
        "AfriMind Conversation Engine Version 16.5 is running."
    )