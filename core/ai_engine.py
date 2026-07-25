# ==========================================
# AfriMind AI Core Engine
# Version 16.8
# Personality Integration System
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


    if question.startswith("my name is"):


        name = question.replace(
            "my name is",
            ""
        ).strip()


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
    # PERSONALITY CHECK
    # ==========================

    personality = get_personality_response(
        question
    )


    if personality:

        return personality



    # ==========================
    # MEMORY LEARNING
    # ==========================

    memory_learning = check_memory_learning(
        question
    )


    if memory_learning:

        return memory_learning



    # ==========================
    # REMEMBER USER NAME
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
    # LEARNED KNOWLEDGE
    # ==========================

    learned_answer = get_learned_answer(
        question
    )


    if learned_answer:

        return learned_answer



    # ==========================
    # MAIN KNOWLEDGE
    # ==========================

    if question in knowledge:

        return knowledge[question]



    # ==========================
    # UNKNOWN
    # ==========================

    return (
        "I don't know the answer yet. "
        "Please teach me."
    )



# ==========================================
# TEACH FUNCTION
# ==========================================

def teach(question, answer):


    return teach_afrimind(
        question,
        answer
    )