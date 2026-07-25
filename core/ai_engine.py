# ==========================================
# AfriMind AI Core Engine
# Version 27.3
# Clean Intelligence + Learning System
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


from core.intelligence_tracker import (
    record_knowledge
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


    local_answer = search_knowledge(
        question
    )


    if local_answer:

        answers.append({

            "answer": local_answer,
            "source": "local"

        })


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
# SAVE INTELLIGENCE
# ==========================================

def save_intelligence(question, answer):


    save_learned_answer(
        question,
        answer
    )


    record_knowledge(
        question,
        answer
    
    )

    # ==========================================
# MAIN AFRIMIND INTELLIGENCE BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # ======================================
    # 1. LEARNING MEMORY CHECK
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
    # 2. CONTEXT UNDERSTANDING
    # ======================================

    context = understand_reference(
        question
    )


    if context:

        question = context + " " + question



    # ======================================
    # 3. PERSONALITY
    # ======================================

    answer = get_personality_response(
        question
    )


    if answer:

        save_intelligence(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # ======================================
    # 4. EXPERT MODULES
    # ======================================

    answer = get_module_answer(
        question
    )


    if answer:

        save_intelligence(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # ======================================
    # 5. KNOWLEDGE DATABASE
    # ======================================

    if question in knowledge:


        answer = knowledge[question]


        save_intelligence(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # ======================================
    # 6. INTERNET SEARCH
    # ======================================

    answer = search_brain(
        question
    )


    if answer:


        add_knowledge(
            question,
            answer
        )


        save_intelligence(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # ======================================
    # 7. PROBLEM SOLVER
    # ======================================

    if any(word in question for word in [

        "problem",
        "challenge",
        "issue",
        "tatizo"

    ]):


        answer = make_decision(
            question
        )


        save_intelligence(
            question,
            answer
        )


        return respond(
            original,
            answer
        )



    # ======================================
    # UNKNOWN
    # ======================================

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


    save_intelligence(

        question,

        answer

    )


    return result