# ==========================================
# AfriMind AI Core Engine
# Version 27.5
# Knowledge Manager Integrated Brain
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.context_engine import (
    save_context,
    understand_reference
)


from core.conversation_engine import (
    save_conversation
)


from core.personality_engine import (
    get_personality_response
)


from core.module_manager import (
    get_module_answer
)


from core.decision_engine import (
    make_decision
)


from core.knowledge_manager import (
    find_answer,
    add_new_knowledge
)


from core.search_engine import (
    get_search_answer
)


from core.ranking_engine import (
    rank_answers
)


from core.intelligence_tracker import (
    record_knowledge
)



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
# SAVE RESPONSE
# ==========================================

def respond(question, answer):

    save_context(
        question,
        answer
    )


    save_conversation(
        question,
        answer
    )


    return answer



# ==========================================
# SEARCH SYSTEM
# ==========================================

def search_brain(question):


    answers = []


    web_answer = get_search_answer(
        question
    )


    if web_answer:

        answers.append({

            "answer": web_answer,
            "source": "internet"

        })



    if answers:

        return rank_answers(
            answers
        )


    return None



# ==========================================
# MAIN AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )


    # 1. CONTEXT UNDERSTANDING

    context = understand_reference(
        question
    )


    if context:

        question = context



    # 2. KNOWLEDGE MANAGER

    answer = find_answer(
        question
    )


    if answer:


        if isinstance(answer, dict):

            answer = answer["answer"]


        record_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 3. PERSONALITY

    answer = get_personality_response(
        question
    )


    if answer:

        add_new_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 4. MODULES

    answer = get_module_answer(
        question
    )


    if answer:

        add_new_knowledge(
            question,
            answer
        )


        record_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 5. INTERNET SEARCH

    answer = search_brain(
        question
    )


    if answer:


        add_new_knowledge(
            question,
            answer
        )


        record_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 6. DECISION ENGINE

    answer = make_decision(
        question
    )


    return respond(
        original,
        answer
    )



# ==========================================
# TEACH AFRIMIND
# ==========================================

def teach(question, answer):


    add_new_knowledge(
        question,
        answer
    )


    record_knowledge(
        question,
        answer
    )


    return respond(
        question,
        "I have learned this new information."
    )