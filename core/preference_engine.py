# ==========================================
# AfriMind Preference Engine
# Version 26.0
# Personal Intelligence Layer
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os


PREFERENCE_FILE = "data/preferences.json"



def initialize_preferences():

    if not os.path.exists(PREFERENCE_FILE):

        with open(
            PREFERENCE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {},
                file,
                indent=4
            )



def save_preference(key, value):

    initialize_preferences()

    with open(
        PREFERENCE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        preferences = json.load(file)


    preferences[key] = value


    with open(
        PREFERENCE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            preferences,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True



def get_preference(key):

    initialize_preferences()

    with open(
        PREFERENCE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        preferences = json.load(file)


    return preferences.get(
        key,
        None
    )



def add_interest(interest):

    initialize_preferences()


    with open(
        PREFERENCE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        preferences = json.load(file)



    if "interests" not in preferences:

        preferences["interests"] = []



    if interest not in preferences["interests"]:

        preferences["interests"].append(
            interest
        )



    with open(
        PREFERENCE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            preferences,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True

# ==========================================
# GET ALL INTERESTS
# ==========================================

def get_interests():

    initialize_preferences()

    with open(
        PREFERENCE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        preferences = json.load(file)

    return preferences.get(
        "interests",
        []
    )