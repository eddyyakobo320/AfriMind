# ==========================================
# AfriMind AI Core Engine
# Version 21.2
# Autonomous Ranked Intelligence System
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


from core.ranking_engine import (
    rank_answers
)

from core.conversation_engine import (
    save_conversation
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


    save_conversation(
        question,
        answer
    )


    return answer



# ==========================================
# MEMORY SYSTEM
# ==========================================

def memory_system(question):


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
# PROBLEM DETECTOR
# ==========================================

def check_problem(question):


    keywords = [

        "problem",
        "challenge",
        "failed",
        "failing",
        "tatizo",
        "issue"

    ]


    return any(
        word in question
        for word in keywords
    )



# ==========================================
# INTELLIGENT SEARCH SYSTEM
# ==========================================

def autonomous_search(question):


    answers = []



    # Local Knowledge

    local_answer = search_knowledge(
        question
    )


    if local_answer:


        answers.append({

            "answer": local_answer,

            "source": "knowledge"

        })



    # Internet Intelligence

    web_answer = get_search_answer(
        question
    )


    if web_answer:


        answers.append({

            "answer": web_answer,

            "source": "internet"

        })



    # Ranking Decision

    if answers:


        best_answer = rank_answers(
            answers
        )


        add_knowledge(
            question,
            best_answer
        )


        return best_answer



    return None



# ==========================================
# AFRIMIND MAIN BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # 1 Personality

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 2 Memory

    answer = memory_system(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 3 Expert Modules

    answer = get_module_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 4 Problem Solving

    if check_problem(question):


        answer = make_decision(
            question
        )


        return respond(
            original,
            answer
        )



    # 5 Learned Intelligence

    answer = get_learned_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 6 Main Knowledge

    if question in knowledge:


        return respond(
            original,
            knowledge[question]
        )



    # 7 Ranked Autonomous Search

    answer = autonomous_search(
        question
    )


    if answer:


        return respond(
            original,
            answer
        )



    # 8 Unknown

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


    return respond(
        question,
        result
    )