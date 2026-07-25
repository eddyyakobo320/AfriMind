# ==========================================
# AfriMind AI Core Engine
# Version 17.3
# Professional Modular Intelligence System
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
# KNOWLEDGE MODULES
# ==========================================

from modules.business import (
    get_business_answer
)


from modules.agriculture import (
    get_agriculture_answer
)


from modules.health import (
    get_health_answer
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
# RESPONSE MANAGER
# ==========================================

def respond(question, answer):

    save_context(
        question,
        answer
    )

    return answer



# ==========================================
# MEMORY SYSTEM
# ==========================================

def handle_memory(question):


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


    return None



# ==========================================
# DOMAIN INTELLIGENCE
# ==========================================

def get_domain_answer(question):


    modules = [

        get_business_answer,

        get_agriculture_answer,

        get_health_answer

    ]


    for module in modules:


        answer = module(
            question
        )


        if answer:

            return answer


    return None



# ==========================================
# DECISION CHECK
# ==========================================

def is_problem(question):


    keywords = [

        "problem",
        "failing",
        "failed",
        "challenge",
        "tatizo"

    ]


    return any(
        word in question
        for word in keywords
    )



# ==========================================
# AFRIMIND MAIN BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # 1. Personality

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 2. Memory

    answer = handle_memory(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 3. Expert Modules

    answer = get_domain_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 4. Decision Intelligence

    if is_problem(question):


        return respond(
            original,
            make_decision(question)
        )



    # 5. Learning System

    answer = get_learned_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 6. General Knowledge

    if question in knowledge:


        return respond(
            original,
            knowledge[question]
        )



    # 7. Unknown Question

    return respond(
        original,
        "I don't know the answer yet. Please teach me."
    )



# ==========================================
# TEACH AFRIMIND
# ==========================================

def teach(question, answer):


    result = teach_afrimind(
        question,
        answer
    )


    return respond(
        question,
        result
    )