# ==========================================
# AfriMind AI User Profile System
# Version 25.0
# User Intelligence & Personalization
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import json
import os



PROFILE_FILE = "data/user_profile.json"



# ==========================================
# CREATE PROFILE STORAGE
# ==========================================

def initialize_profile():

    if not os.path.exists(PROFILE_FILE):

        with open(
            PROFILE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {},
                file,
                indent=4
            )



# ==========================================
# SAVE USER INFORMATION
# ==========================================

def save_profile(key, value):

    initialize_profile()


    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        profile = json.load(file)



    profile[key] = value



    with open(
        PROFILE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True



# ==========================================
# GET USER INFORMATION
# ==========================================

def get_profile(key):

    initialize_profile()


    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        profile = json.load(file)



    return profile.get(key)



# ==========================================
# GET FULL PROFILE
# ==========================================

def get_full_profile():

    initialize_profile()


    with open(
        PROFILE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)