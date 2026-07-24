# ==========================================
# AfriMind Brain
# Version 6.6
# Self Learning Integration
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import get_answer, add_knowledge
from memory import remember
from knowledge import knowledge

from language import detect_language, translate_greeting

from long_memory import remember_information, recall_information

from profile import (
    set_name,
    get_name,
    set_country,
    get_country,
    set_language,
    get_language
)

from interest import (
    save_interest,
    get_interest
)

from learning import learn_new_information



def clean_question(question):

    question = question.lower().strip()

    question = question.replace("?", "")

    return question





def ask_question(question, name):

    question = clean_question(question)

    language = detect_language(question)


    remember(
        "user_name",
        name
    )



    # Exit

    if question == "exit":

        return "EXIT"




    # Greetings

    if question in [
        "hello",
        "hi",
        "hey",
        "habari",
        "mambo",
        "hujambo",
        "salama"
    ]:

        return translate_greeting(
            language,
            name
        )




    # Name

    if question in [
        "what is my name",
        "jina langu ni nani"
    ]:

        saved_name = get_name()

        if saved_name:

            return f"Jina lako ni {saved_name}."

        return "Sijui jina lako bado."




    if question.startswith("my name is"):

        user_name = question.replace(
            "my name is",
            ""
        ).strip()

        set_name(user_name)

        return f"Nice to meet you {user_name}. I will remember your name."




    if question.startswith("jina langu ni"):

        user_name = question.replace(
            "jina langu ni",
            ""
        ).strip()

        set_name(user_name)

        return f"Nimefurahi kukufahamu {user_name}. Nitakumbuka jina lako."




    # Interest

    if question.startswith("i like"):

        interest = question.replace(
            "i like",
            ""
        ).strip()

        save_interest(interest)

        return f"I will remember that you like {interest}."




    if question == "what is my interest":

        interest = get_interest()

        if interest:

            return f"Your interest is {interest}."

        return "I don't know your interest yet."




    # Database search

    answer = get_answer(question)


    if answer:

        return answer




    # Knowledge search

    if question in knowledge:

        answer = knowledge[question]

        add_knowledge(
            question,
            answer
        )

        return answer




    # Learning request

    return "I don't know the answer yet. Please teach me."