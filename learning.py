# ==========================================
# AfriMind Learning System
# Version 8.0
# Self Learning + Long Memory Integration
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import add_knowledge, get_answer

from long_memory import remember_information



# ==========================
# TEACH AFRIMIND
# ==========================

def teach_afrimind(question, answer):


    # Save in knowledge database

    add_knowledge(
        question,
        answer
    )


    # Save in long term memory

    remember_information(
        question,
        answer,
        "knowledge"
    )


    return (
        "Thank you. I have learned "
        "and remembered this information."
    )



# ==========================
# CHECK KNOWLEDGE
# ==========================

def remember_knowledge(question):


    answer = get_answer(
        question
    )


    return answer



# ==========================
# TEACH FROM USER
# ==========================

def learn_from_user(question, answer):


    return teach_afrimind(
        question,
        answer
    )