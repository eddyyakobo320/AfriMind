# ==========================================
# AfriMind AI Core Engine
# Version 27.0
# Clean Intelligence Controller
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge


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


from core.learning_engine import (
    get_learned_answer,
    teach_afrimind
)


from core.knowledge_engine import (
    search_knowledge,
    add_knowledge
)


from core.search_engine import (
    get_search_answer
)


from core.ranking_engine import (
    rank_answers
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
# RESPONSE
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
# SEARCH INTELLIGENCE
# ==========================================

def search_brain(question):


    answers = []


    local = search_knowledge(
        question
    )


    if local:

        answers.append({
            "answer": local,
            "source": "local"
        })



    web = get_search_answer(
        question
    )


    if web:

        answers.append({
            "answer": web,
            "source": "web"
        })



    if answers:

        return rank_answers(
            answers
        )


    return None



# ==========================================
# MAIN BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )


    # Context

    context = understand_reference(
        question
    )


    if context:

        question = context



    # Personality

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # Modules

    answer = get_module_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # Knowledge

    if question in knowledge:

        return respond(
            original,
            knowledge[question]
        )



    # Search

    answer = search_brain(
        question
    )


    if answer:

        add_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # Decision

    answer = make_decision(
        question
    )


    return respond(
        original,
        answer
    )



# ==========================================
# TEACH
# ==========================================

def teach(question, answer):


    result = teach_afrimind(
        question,
        answer
    )


    add_knowledge(
        question,
        answer
    )


    return result