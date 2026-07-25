# ==========================================
# AfriMind AI Context Engine
# Version 26.4
# Advanced Conversation Memory System
# Topic Understanding Layer
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os
from datetime import datetime



CONTEXT_FILE = "data/context.json"



# ==========================================
# CREATE STORAGE
# ==========================================

def create_context_file():


    if not os.path.exists(CONTEXT_FILE):


        with open(
            CONTEXT_FILE,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                [],
                file,
                indent=4
            )




# ==========================================
# LOAD MEMORY SAFELY
# ==========================================

def load_context():


    create_context_file()


    try:

        with open(
            CONTEXT_FILE,
            "r",
            encoding="utf-8"
        ) as file:


            return json.load(file)



    except:


        return []




# ==========================================
# SAVE CONTEXT MEMORY
# ==========================================

def save_context(
        user_message,
        afrimind_response
):


    context = load_context()



    context.append({

        "time":
        str(datetime.now()),


        "user":
        user_message,


        "afrimind":
        afrimind_response,


        "topic":
        extract_topic(user_message)

    })



    # Keep latest 50 conversations

    context = context[-50:]



    with open(
        CONTEXT_FILE,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )




# ==========================================
# GET LAST MEMORY
# ==========================================

def get_last_context():


    context = load_context()



    if context:


        return context[-1]



    return None




# ==========================================
# TOPIC EXTRACTION
# ==========================================

def extract_topic(message):


    words = message.lower().split()



    remove = [

        "what",
        "is",
        "are",
        "the",
        "a",
        "an",
        "my",
        "its",
        "it",
        "this",
        "that",
        "about",
        "please",
        "tell",
        "me"

    ]



    clean_words = []



    for word in words:


        if word not in remove:


            clean_words.append(word)



    if clean_words:


        return clean_words[-1]



    return None




# ==========================================
# GET PREVIOUS TOPIC
# ==========================================

def get_previous_topic():


    last = get_last_context()



    if last:


        return last.get(
            "topic"
        )



    return None




# ==========================================
# UNDERSTAND REFERENCES
# ==========================================

def understand_reference(question):


    references = [

        "it",
        "its",
        "this",
        "that",
        "those",
        "they",
        "yake",
        "hiyo",
        "hilo"

    ]



    words = question.lower().split()



    found = False



    for word in references:


        if word in words:


            found = True



    if found:


        topic = get_previous_topic()



        if topic:


            return topic



    return None




# ==========================================
# SEARCH OLD MEMORY
# ==========================================

def search_context(keyword):


    context = load_context()


    results = []



    for item in context:


        if keyword.lower() in item["user"].lower():


            results.append(item)



    return results