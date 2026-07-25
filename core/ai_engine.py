# ==========================================
# AfriMind AI Core Engine
# Version 17.1.1
# Professional Brain Optimization
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge

from core.memory_engine import remember, recall

from core.learning_engine import (
    get_learned_answer,
    teach_afrimind
)

from core.personality_engine import get_personality_response

from core.context_engine import save_context

from core.decision_engine import make_decision

from modules.business import get_business_answer



# ==========================================
# CLEAN INPUT
# ==========================================

def clean_question(question):

    return (
        question
        .lower()
        .strip()
        .replace("?", "")
    )



# ==========================================
# RESPONSE
# ==========================================

def respond(question, answer):

    save_context(
        question,
        answer
    )

    return answer



# ==========================================
# MEMORY NAME
# ==========================================

def save_name(question):

    if question.startswith("my name is"):

        name = question.replace(
            "my name is",
            ""
        ).strip()

        remember(
            "user_name",
            name
        )

        return f"Nice to meet you {name}. I will remember your name."

    return None



# ==========================================
# AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question

    question = clean_question(
        question
    )


    # Personality

    answer = get_personality_response(
        question
    )

    if answer:
        return respond(
            original,
            answer
        )



    # Save user name

    answer = save_name(
        question
    )

    if answer:
        return respond(
            original,
            answer
        )



    # Recall name

    if question == "what is my name":

        name = recall(
            "user_name"
        )

        answer = (
            f"Your name is {name}."
            if name
            else
            "I don't know your name yet."
        )

        return respond(
            original,
            answer
        )



    # Business Knowledge

    answer = get_business_answer(
        question
    )

    if answer:
        return respond(
            original,
            answer
        )



    # Decision System

    if any(word in question for word in [
        "problem",
        "failing",
        "failed",
        "challenge",
        "tatizo"
    ]):

        return respond(
            original,
            make_decision(question)
        )



    # Learned Knowledge

    answer = get_learned_answer(
        question
    )

    if answer:
        return respond(
            original,
            answer
        )



    # Main Knowledge

    if question in knowledge:

        return respond(
            original,
            knowledge[question]
        )



    return respond(
        original,
        "I don't know the answer yet. Please teach me."
    )



# ==========================================
# TEACH AFRIMIND
# ==========================================

def teach(question, answer):

    result = teach_afrimind(
        question,
        answer
    )

    return respond(
        question,
        result
    )