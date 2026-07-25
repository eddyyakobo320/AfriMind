# ==========================================
# AfriMind AI Core Engine
# Version 17.4
# Automatic Modular Intelligence System
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


from core.module_manager import (
    get_module_answer
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
# RESPONSE SYSTEM
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
# PROBLEM DETECTION
# ==========================================

def is_problem(question):


    keywords = [

        "problem",
        "failing",
        "failed",
        "challenge",
        "tatizo",
        "issue"

    ]


    return any(
        word in question
        for word in keywords
    )



# ==========================================
# AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # 1. Personality Intelligence

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 2. Memory Intelligence

    answer = handle_memory(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 3. Automatic Knowledge Modules

    answer = get_module_answer(
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



    # 5. Learning Memory

    answer = get_learned_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 6. Main Knowledge

    if question in knowledge:


        return respond(
            original,
            knowledge[question]
        )



    # 7. Unknown

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