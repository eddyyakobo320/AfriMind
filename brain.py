# ==========================================
# AfriMind Brain
# Version 9.0 Intelligent Module System
# Main Intelligence Engine
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import (
    get_answer,
    add_knowledge,
    create_database
)

from knowledge import knowledge

from swahili_knowledge import swahili_knowledge

from modules.module_manager import (
    get_all_module_knowledge
)

from search_engine import find_best_match

from language import get_greeting



# Create database when brain starts

create_database()



# ==========================
# LOAD ALL MODULES
# ==========================

module_knowledge = get_all_module_knowledge()



# ==========================
# CLEAN QUESTION
# ==========================

def clean_question(question):

    question = question.lower()

    question = question.strip()

    question = question.replace("?", "")

    return question



# ==========================
# ASK AFRIMIND
# ==========================

def ask_question(question):


    question = clean_question(question)



    # ======================
    # GREETING SYSTEM
    # ======================

    greeting = get_greeting(question)


    if greeting:

        return greeting



    # ======================
    # DATABASE SEARCH
    # ======================

    answer = get_answer(question)


    if answer:

        return answer



    # ======================
    # ENGLISH KNOWLEDGE
    # ======================

    if question in knowledge:


        answer = knowledge[question]

        add_knowledge(
            question,
            answer
        )

        return answer



    # ======================
    # SWAHILI KNOWLEDGE
    # ======================

    if question in swahili_knowledge:


        answer = swahili_knowledge[question]


        add_knowledge(
            question,
            answer
        )

        return answer



    # ======================
    # MODULE KNOWLEDGE
    # ======================

    if question in module_knowledge:


        answer = module_knowledge[question]


        add_knowledge(
            question,
            answer
        )

        return answer



    # ======================
    # SMART SEARCH MODULES
    # ======================

    best_match = find_best_match(
        question,
        module_knowledge
    )


    if best_match:


        answer = module_knowledge[best_match]


        add_knowledge(
            best_match,
            answer
        )


        return answer



    # ======================
    # SMART SEARCH GENERAL
    # ======================

    best_match = find_best_match(
        question,
        knowledge
    )


    if best_match:


        answer = knowledge[best_match]


        add_knowledge(
            best_match,
            answer
        )


        return answer



    # ======================
    # LEARNING MODE
    # ======================

    return (
        "I don't know the answer yet. "
        "Please teach me."
    )