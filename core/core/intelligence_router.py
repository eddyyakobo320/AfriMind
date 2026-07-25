# ==========================================
# AfriMind AI Intelligence Router
# Version 19.0
# Advanced Knowledge Decision System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.module_manager import (
    get_module_answer
)


from core.learning_engine import (
    get_learned_answer
)


from core.knowledge_engine import (
    search_knowledge,
    add_knowledge
)


from core.web_engine import (
    get_web_answer
)



# ==========================================
# LOCAL KNOWLEDGE SEARCH
# ==========================================

def search_local(question):


    # 1. Learned Memory

    answer = get_learned_answer(
        question
    )


    if answer:

        return answer



    # 2. Knowledge Database

    answer = search_knowledge(
        question
    )


    if answer:

        return answer



    return None




# ==========================================
# INTERNET INTELLIGENCE
# ==========================================

def search_web(question):


    answer = get_web_answer(
        question
    )


    if answer:


        # Store new information

        add_knowledge(
            question,
            answer
        )


        return answer



    return None




# ==========================================
# AFRIMIND INTELLIGENCE BRAIN
# ==========================================

def get_intelligent_answer(question):


    # Layer 1:
    # Professional Modules

    answer = get_module_answer(
        question
    )


    if answer:

        return answer



    # Layer 2:
    # Local Brain

    answer = search_local(
        question
    )


    if answer:

        return answer



    # Layer 3:
    # Internet Search

    answer = search_web(
        question
    )


    if answer:

        return answer



    # Nothing found

    return (
        "I could not find the answer yet. "
        "I am still learning."
    )