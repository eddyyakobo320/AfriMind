# ==========================================
# AfriMind AI Core Engine
# Version 28.1
# Fast Intelligence Brain
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge

from core.context_engine import save_context, understand_reference
from core.conversation_engine import save_conversation
from core.personality_engine import get_personality_response
from core.module_manager import get_module_answer
from core.learning_brain import learning_process
from core.knowledge_manager import add_new_knowledge



def clean_question(text):

    return (
        text.lower()
        .strip()
        .replace("?", "")
    )



def respond(question, answer):

    save_context(question, answer)

    save_conversation(question, answer)

    return answer



def ask_question(question):


    original = question

    question = clean_question(question)



    # Context memory

    context = understand_reference(question)

    if context:

        question = context



    # Personality

    answer = get_personality_response(question)

    if answer:

        return respond(original, answer)



    # Modules

    answer = get_module_answer(question)

    if answer:

        return respond(original, answer)



    # Direct knowledge search

    if question in knowledge:

        return respond(
            original,
            knowledge[question]
        )



    # Learning brain

    answer = learning_process(question)

    if answer:

        add_new_knowledge(
            question,
            answer
        )

        return respond(
            original,
            answer
        )



    # Topic fallback

    for key in knowledge:

        if any(word in question for word in key.split()):

            return respond(
                original,
                knowledge[key]
            )



    return respond(
        original,
        "I am still learning. Please teach me more about this topic."
    )



def teach(question, answer):

    add_new_knowledge(
        question.lower(),
        answer
    )

    return "Thank you. I have learned new knowledge."