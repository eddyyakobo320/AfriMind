# ==========================================
# AfriMind AI Core Engine
# Version 16.4
# Memory Integration System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge

from core.memory_engine import (
    remember,
    recall
)



# ==========================================
# CLEAN QUESTION
# ==========================================

def clean_question(question):

    question = question.lower()

    question = question.strip()

    question = question.replace("?", "")

    return question



# ==========================================
# MEMORY LEARNING
# ==========================================

def check_memory_learning(question):


    # Example:
    # my name is Edward


    if question.startswith("my name is"):


        name = question.replace(
            "my name is",
            ""
        ).strip()


        # Make first letter capital

        name = name.capitalize()


        remember(
            "user_name",
            name
        )


        return (
            f"Nice to meet you {name}. "
            "I will remember your name."
        )


    return None



# ==========================================
# ASK AFRIMIND
# ==========================================

def ask_question(question):


    question = clean_question(
        question
    )



    # ==========================
    # CHECK NEW MEMORY
    # ==========================

    memory_learning = check_memory_learning(
        question
    )


    if memory_learning:

        return memory_learning



    # ==========================
    # RECALL MEMORY
    # ==========================

    if question == "what is my name":


        name = recall(
            "user_name"
        )


        if name:

            return (
                f"Your name is {name}."
            )


        return (
            "I don't know your name yet."
        )



    # ==========================
    # KNOWLEDGE SEARCH
    # ==========================

    if question in knowledge:


        return knowledge[question]



    # ==========================
    # UNKNOWN QUESTION
    # ==========================

    return (
        "I don't know the answer yet. "
        "Please teach me."
    )