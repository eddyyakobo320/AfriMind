# ==========================================
# AfriMind Language Intelligence
# Version 7.2
# Language Understanding Module
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


# ==========================
# LANGUAGE DETECTION
# ==========================

def detect_language(text):

    text = text.lower()


    swahili_words = [

        "nini",
        "maana",
        "ni",
        "ya",
        "kwa",
        "habari",
        "asante",
        "tafadhali",
        "msaada",
        "kilimo",
        "maendeleo",
        "jamii",
        "janga",
        "elimu"

    ]


    english_words = [

        "what",
        "is",
        "the",
        "how",
        "who",
        "why",
        "help",
        "define",
        "explain"

    ]


    sw_score = 0
    en_score = 0



    for word in swahili_words:

        if word in text:

            sw_score += 1



    for word in english_words:

        if word in text:

            en_score += 1



    if sw_score > en_score:

        return "sw"



    return "en"





# ==========================
# COMMON GREETINGS
# ==========================

# ==========================
# COMMON GREETINGS
# ==========================

def get_greeting(text):

    text = text.lower().strip()


    greetings = {

        "habari": "Habari! Karibu kwenye AfriMind AI.",

        "hello": "Hello! Welcome to AfriMind AI.",

        "hi": "Hi! I am AfriMind AI."

    }


    words = text.split()


    for word in words:

        if word in greetings:

            return greetings[word]


    return None