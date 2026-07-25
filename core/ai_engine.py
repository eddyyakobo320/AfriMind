# ==========================================
# AfriMind AI Core Engine
# Version 16.9.2
# Professional Brain Refactor
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge

from core.memory_engine import (
    remember,
    recall
)

from core.learning_engine import (
    get_learned_answer,
    teach_afrimind
)

from core.personality_engine import (
    get_personality_response
)

from core.context_engine import (
    save_context
)



# ==========================================
# TEXT PROCESSING
# ==========================================

def clean_question(question):

    return (
        question
        .lower()
        .strip()
        .replace("?", "")
    )



# ==========================================
# RESPONSE HANDLER
# ==========================================

def send_response(question, answer):

    save_context(
        question,
        answer
    )

    return answer



# ==========================================
# MEMORY SYSTEM
# ==========================================

def remember_name(question):


    if question.startswith("my name is"):


        name = (
            question
            .replace("my name is", "")
            .strip()
        )


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
# AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )


    # Personality

    response = get_personality_response(
        question
    )

    if response:
        return send_response(
            original,
            response
        )



    # Memory learning

    response = remember_name(
        question
    )

    if response:
        return send_response(
            original,
            response
        )



    # User memory

    if question == "what is my name":


        name = recall(
            "user_name"
        )


        response = (
            f"Your name is {name}."
            if name
            else
            "I don't know your name yet."
        )


        return send_response(
            original,
            response
        )



    # Learned knowledge

    response = get_learned_answer(
        question
    )

    if response:
        return send_response(
            original,
            response
        )



    # Main knowledge

    if question in knowledge:

        return send_response(
            original,
            knowledge[question]
        )



    # Unknown

    return send_response(
        original,
        "I don't know the answer yet. Please teach me."
    )



# ==========================================
# LEARNING FUNCTION
# ==========================================

def teach(question, answer):


    response = teach_afrimind(
        question,
        answer
    )


    return send_response(
        question,
        response
    )