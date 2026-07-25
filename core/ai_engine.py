# ==========================================
# AfriMind AI Core Engine
# Version 27.4
# Self Learning Integrated Intelligence System
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


from core.self_learning import (
    get_new_knowledge,
    save_new_knowledge
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
# SEARCH BRAIN
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



    # ======================================
    # 1. SELF LEARNING MEMORY
    # ======================================

    learned = get_new_knowledge(
        question
    )


    if learned:

        return respond(
            original,
            learned
        )



    # ======================================
    # 2. OLD LEARNING MEMORY
    # ======================================

    learned = get_learned_answer(
        question
    )


    if learned:

        return respond(
            original,
            learned
        )



    # ======================================
    # 3. CONTEXT UNDERSTANDING
    # ======================================

    context = understand_reference(
        question
    )


    if context:

        question = context + " " + question



    # ======================================
    # 4. PERSONALITY
    # ======================================

    answer = get_personality_response(
        question
    )


    if answer:

        save_new_knowledge(
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



    # ======================================
    # 5. MODULES
    # ======================================

    answer = get_module_answer(
        question
    )


    if answer:

        save_new_knowledge(
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



    # ======================================
    # 6. INTERNAL KNOWLEDGE
    # ======================================

    if question in knowledge:


        answer = knowledge[question]


        save_new_knowledge(
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



    # ======================================
    # 7. INTERNET SEARCH
    # ======================================

    answer = search_brain(
        question
    )


    if answer:


        add_knowledge(
            question,
            answer
        )


        save_new_knowledge(
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



    # ======================================
    # 8. PROBLEM SOLVER
    # ======================================

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


    result = teach_afrimind(
        question,
        answer
    )


    add_knowledge(
        question,
        answer
    )


    save_new_knowledge(
        question,
        answer
    )


    record_knowledge(
        question,
        answer
    )


    return result