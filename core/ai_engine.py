# ==========================================
# AfriMind AI Core Engine
# Version 27.7
# Learning Brain Integration System
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


from core.learning_brain import (
    learning_process
)


from core.knowledge_manager import (
    add_new_knowledge
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
# MAIN AFRIMIND BRAIN
# ==========================================

def ask_question(question):


    original = question


    question = clean_question(
        question
    )



    # 1. CONTEXT MEMORY

    context = understand_reference(
        question
    )


    if context:

        question = context



    # 2. PERSONALITY

    answer = get_personality_response(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 3. MODULE KNOWLEDGE

    answer = get_module_answer(
        question
    )


    if answer:

        return respond(
            original,
            answer
        )



    # 4. OLD KNOWLEDGE BASE

    if question in knowledge:

        return respond(
            original,
            knowledge[question]
        )



    # 5. LEARNING BRAIN

    answer = learning_process(
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



    # 6. DECISION SYSTEM

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


    return (
        "Thank you. I have learned new knowledge."
    )