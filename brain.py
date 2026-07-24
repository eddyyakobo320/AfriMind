# ==========================================
# AfriMind Brain
# Version 8.1 Intelligent System
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

from modules.agriculture import agriculture_knowledge
from modules.business import business_knowledge
from modules.health import health_knowledge

from search_engine import find_best_match
from language import get_greeting


# ==========================
# CREATE DATABASE
# ==========================

create_database()


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
    # GREETING
    # ======================

    greeting = get_greeting(question)

    if greeting:
        return greeting

    # ======================
    # DATABASE
    # ======================

    answer = get_answer(question)

    if answer:
        return answer

    # ======================
    # ENGLISH KNOWLEDGE
    # ======================

    if question in knowledge:

        answer = knowledge[question]

        add_knowledge(question, answer)

        return answer

    # ======================
    # SWAHILI KNOWLEDGE
    # ======================

    if question in swahili_knowledge:

        answer = swahili_knowledge[question]

        add_knowledge(question, answer)

        return answer

    # ======================
    # AGRICULTURE MODULE
    # ======================

    if question in agriculture_knowledge:

        answer = agriculture_knowledge[question]

        add_knowledge(question, answer)

        return answer

    # ======================
    # BUSINESS MODULE
    # ======================

    if question in business_knowledge:

        answer = business_knowledge[question]

        add_knowledge(question, answer)

        return answer

    # ======================
    # HEALTH MODULE
    # ======================

    if question in health_knowledge:

        answer = health_knowledge[question]

        add_knowledge(question, answer)

        return answer

    # ======================
    # SMART SEARCH ENGLISH
    # ======================

    best_match = find_best_match(question, knowledge)

    if best_match:

        answer = knowledge[best_match]

        add_knowledge(best_match, answer)

        return answer

    # ======================
    # SMART SEARCH SWAHILI
    # ======================

    best_match = find_best_match(question, swahili_knowledge)

    if best_match:

        answer = swahili_knowledge[best_match]

        add_knowledge(best_match, answer)

        return answer

    # ======================
    # SMART SEARCH AGRICULTURE
    # ======================

    best_match = find_best_match(question, agriculture_knowledge)

    if best_match:

        answer = agriculture_knowledge[best_match]

        add_knowledge(best_match, answer)

        return answer

    # ======================
    # SMART SEARCH BUSINESS
    # ======================

    best_match = find_best_match(question, business_knowledge)

    if best_match:

        answer = business_knowledge[best_match]

        add_knowledge(best_match, answer)

        return answer

    # ======================
    # SMART SEARCH HEALTH
    # ======================

    best_match = find_best_match(question, health_knowledge)

    if best_match:

        answer = health_knowledge[best_match]

        add_knowledge(best_match, answer)

        return answer

    # ======================
    # LEARNING MODE
    # ======================

    return (
        "I don't know the answer yet. "
        "Please teach me."
    )