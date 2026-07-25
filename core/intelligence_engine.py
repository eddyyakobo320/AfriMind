# ==========================================
# AfriMind AI Intelligence Router
# Version 19.0
# Central Decision Layer
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
# LOCAL INTELLIGENCE SEARCH
# ==========================================

def search_local_knowledge(question):

    # Learned knowledge

    answer = get_learned_answer(
        question
    )

    if answer:

        return answer



    # Knowledge engine

    answer = search_knowledge(
        question
    )

    if answer:

        return answer



    return None



# ==========================================
# MAIN INTELLIGENCE ROUTER
# ==========================================

def get_intelligent_answer(question):


    # 1. Search modules

    answer = get_module_answer(
        question
    )


    if answer:

        return answer



    # 2. Search local memory

    answer = search_local_knowledge(
        question
    )


    if answer:

        return answer



    # 3. Search internet

    answer = get_web_answer(
        question
    )


    if answer:


        # Save new knowledge

        add_knowledge(
            question,
            answer
        )


        return answer



    return None