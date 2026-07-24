# ==========================================
# AfriMind AI Core Engine
# Version 16.1
# Professional Intelligence Architecture
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


"""
This file contains the main intelligence
engine of AfriMind AI.

It manages:
- Question processing
- Answer generation
- Future AI modules
"""


# ==========================
# CLEAN QUESTION
# ==========================

def clean_question(question):

    """
    Prepare user question
    """

    question = question.lower()

    question = question.strip()

    question = question.replace("?", "")

    return question



# ==========================
# MAIN AI ENGINE
# ==========================

def ask_question(question):

    """
    Main AfriMind thinking function
    """

    question = clean_question(
        question
    )


    # Temporary response
    # Will connect with:
    # database
    # knowledge
    # memory
    # modules

    if question == "hello":

        return "Hello! I am AfriMind AI."


    return (
        "AfriMind Core Engine Version 16.1 "
        "is running successfully."
    )