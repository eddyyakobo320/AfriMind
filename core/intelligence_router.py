# ==========================================
# AfriMind AI Intelligence Router
# Version 19.0
# Central Intelligence Decision Layer
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.module_manager import get_module_answer

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


    # Learned answers

    answer = get_learned_answer(
        question
    )

    if answer:

        return answer



    # Knowledge database

    answer = search_knowledge(
        question
    )

    if answer:

        return answer



    return None




# ==========================================
# INTERNET INTELLIGENCE
# ==========================================

def search_online(question):


    answer = get_web_answer(
        question
    )


    if answer:


        add_knowledge(
            question,
            answer
        )


        return answer


    return None




# ==========================================
# MAIN INTELLIGENCE ROUTER
# ==========================================

def get_intelligent_answer(question):


    # 1. Expert Modules

    answer = get_module_answer(
        question
    )


    if answer:

        return answer



    # 2. Local Brain

    answer = search_local(
        question
    )


    if answer:

        return answer



    # 3. Internet Brain

    answer = search_online(
        question
    )


    if answer:

        return answer



    return None