# ==========================================
# AfriMind AI Core Engine
# Version 20.0
# Autonomous Modular Intelligence System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge


from core.memory_engine import (
    remember,
    recall
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
# RESPONSE HANDLER
# ==========================================

def respond(question, answer):

    save_context(
        question,
        answer
    )

    return answer



# ==========================================
# MEMORY HANDLER
# ==========================================

def memory_system(question):


    if question.startswith("my name is"):


        name = question.replace(
            "my name is",
            ""
        ).strip()


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

            return f"Your name is {name}."


        return (
            "I don't know your name yet."
        )


    return None



# ==========================================
# DECISION CHECK
# ==========================================

def check_problem(question):


    keywords = [

        "problem",
        "challenge",
        "failed",
        "failing",
        "tatizo"

    ]


    return any(
        word in question
        for word in keywords
    )



# ==========================================
# AUTONOMOUS SEARCH BRAIN
# ==========================================

def autonomous_search(question):


    # Search saved knowledge

    answer = search_knowledge(
        question
    )


    if answer:

        return answer



    # Search internet

    answer = get_search_answer(
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

    answer = memory_system(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 3. Expert Modules

    answer = get_module_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 4. Problem Solver

    if check_problem(question):


        answer = make_decision(
            question
        )


        return respond(
            original,
            answer
        )



    # 5. Learned Knowledge

    answer = get_learned_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 6. Knowledge Database

    if question in knowledge:


        return respond(
            original,
            knowledge[question]
        )



    # 7. Autonomous Internet Intelligence

    answer = autonomous_search(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 8. Unknown

    return respond(
        original,
        "I don't know the answer yet."
    )



# ==========================================
# TEACH AFRIMIND
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