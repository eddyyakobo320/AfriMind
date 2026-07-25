# ==========================================
# AfriMind AI Core Engine
# Version 17.0
# Advanced Brain Integration
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


from core.decision_engine import (
    make_decision
)



# ==========================================
# CLEAN QUESTION
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
# MEMORY NAME SYSTEM
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



    # Recall user name

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



    # Decision Engine 🧠

    if any(word in question for word in [
        "problem",
        "business",
        "biashara",
        "failing",
        "failed",
        "challenge",
        "tatizo"
    ]):


        response = make_decision(
            question
        )


        return send_response(
            original,
            response
        )



    # Learning Engine

    response = get_learned_answer(
        question
    )


    if response:

        return send_response(
            original,
            response
        )



    # Knowledge Base

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
# TEACH AFRIMIND
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