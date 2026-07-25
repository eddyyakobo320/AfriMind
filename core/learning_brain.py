# ==========================================
# AfriMind Learning Brain
# Version 27.6
# Unified Self Learning Intelligence
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.knowledge_manager import (
    find_answer,
    add_new_knowledge
)

from core.intelligence_tracker import (
    record_knowledge
)

from core.search_engine import (
    get_search_answer
)



# ==========================================
# FIND KNOWLEDGE
# ==========================================

def think(question):

    """
    AfriMind first checks existing knowledge
    """

    answer = find_answer(
        question
    )


    if answer:

        if isinstance(answer, dict):

            return answer["answer"]


        return answer


    return None



# ==========================================
# LEARN NEW INFORMATION
# ==========================================

def learn(
        question,
        answer
):


    add_new_knowledge(
        question,
        answer
    )


    record_knowledge(
        question,
        answer
    )


    return True



# ==========================================
# AUTONOMOUS LEARNING
# ==========================================

def learn_from_unknown(question):


    # Search internet

    answer = get_search_answer(
        question
    )


    if answer:


        learn(
            question,
            answer
        )


        return answer



    return None



# ==========================================
# MAIN LEARNING FUNCTION
# ==========================================

def learning_process(question):


    # Step 1:
    # Check memory

    answer = think(
        question
    )


    if answer:

        return answer



    # Step 2:
    # Search and learn

    answer = learn_from_unknown(
        question
    )


    if answer:

        return answer



    return None



# ==========================================
# STATUS
# ==========================================

def brain_status():

    return {

        "system":
        "AfriMind Unified Learning Brain",

        "version":
        "27.6",

        "status":
        "Learning system active"

    }