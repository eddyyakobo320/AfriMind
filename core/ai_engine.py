# ==========================================
# AfriMind AI Core Engine
# Version 27.2
# Clean Intelligence + Learning Memory
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
    teach_afrimind
)


from core.learning_memory import (
    save_learned_answer,
    get_learned_answer
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
# SEARCH SYSTEM
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
# MAIN AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # 1. CHECK LEARNING MEMORY

    learned = get_learned_answer(
        question
    )


    if learned:

        return respond(
            original,
            learned
        )



    # 2. CONTEXT

    context = understand_reference(
        question
    )


    if context:

        question = context + " " + question



    # 3. PERSONALITY

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 4. MODULES

    answer = get_module_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 5. KNOWLEDGE BASE

    if question in knowledge:


        answer = knowledge[question]


        save_learned_answer(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 6. SEARCH INTERNET

    answer = search_brain(
        question
    )


    if answer:


        save_learned_answer(
            question,
            answer
        )


        add_knowledge(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # 7. PROBLEM SOLVER

    if any(word in question for word in [
        "problem",
        "challenge",
        "issue",
        "tatizo"
    ]):


        answer = make_decision(
            question
        )


        return respond(
            original,
            answer
        )



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


    save_learned_answer(
        question,
        answer
    )


    add_knowledge(
        question,
        answer
    )


    return result