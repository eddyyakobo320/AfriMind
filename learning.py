# ==========================================
# AfriMind Learning System
# Version 7.1
# Knowledge Learning Module
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import add_knowledge, get_answer



# ==========================
# TEACH AFRIMIND
# ==========================

def teach_afrimind(question, answer):

    add_knowledge(
        question,
        answer
    )

    return "Thank you. I have learned this information."



# ==========================
# CHECK MEMORY
# ==========================

def remember_knowledge(question):

    answer = get_answer(
        question
    )

    return answer