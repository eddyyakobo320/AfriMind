# ==========================================
# AfriMind Brain
# Version 6.4.1
# Language Intelligence Bug Fix
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



def clean_question(question):

    """
    Clean user input
    """

    question = question.lower().strip()

    question = question.replace("?", "")

    return question





def ask_question(question, name):


    question = clean_question(question)

    language = detect_language(question)



    # Remember current user

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




    # ==========================
    # USER NAME SYSTEM
    # ==========================


    # Ask name first

    if question in [
        "what is my name",
        "jina langu ni nani"
    ]:


        saved_name = get_name()


        if saved_name:

            if language == "swahili":

                return f"Jina lako ni {saved_name}."


            return f"Your name is {saved_name}."


        return "I don't know your name yet."




    # Save name English

    if question.startswith("my name is"):


        user_name = question.replace(
            "my name is",
            ""
        ).strip()


        set_name(
            user_name
        )


        return f"Nice to meet you {user_name}. I will remember your name."




    # Save name Swahili

    if question.startswith("jina langu ni"):


        user_name = question.replace(
            "jina langu ni",
            ""
        ).strip()


        set_name(
            user_name
        )


        return f"Nimefurahi kukufahamu {user_name}. Nitakumbuka jina lako."





    # ==========================
    # COUNTRY SYSTEM
    # ==========================


    if question in [
        "where do i live",
        "naishi wapi"
    ]:


        country = get_country()


        if country:

            if language == "swahili":

                return f"Unaishi {country}."


            return f"You live in {country}."


        return "I don't know where you live yet."




    if question.startswith("i live in"):


        country = question.replace(
            "i live in",
            ""
        ).strip()


        set_country(
            country
        )


        return f"I will remember that you live in {country}."




    if question.startswith("ninaishi"):


        country = question.replace(
            "ninaishi",
            ""
        ).strip()


        set_country(
            country
        )


        return f"Nitakumbuka kuwa unaishi {country}."




    # ==========================
    # LANGUAGE MEMORY
    # ==========================


    if question.startswith("my language is"):


        lang = question.replace(
            "my language is",
            ""
        ).strip()


        set_language(
            lang
        )


        return f"I will remember that your language is {lang}."




    if question == "what is my language":


        lang = get_language()


        if lang:

            return f"Your preferred language is {lang}."


        return "I don't know your language yet."




    # ==========================
    # FAVORITE COLOR MEMORY
    # ==========================


    if "my favorite color is" in question:


        color = question.replace(
            "my favorite color is",
            ""
        ).strip()


        remember_information(
            "favorite_color",
            color
        )


        return f"Okay {name}, I will remember that your favorite color is {color}."




    if question == "what is my favorite color":


        color = recall_information(
            "favorite_color"
        )


        if color:

            return f"Your favorite color is {color}."


        return "I don't know your favorite color yet."




    # ==========================
    # DATABASE SEARCH
    # ==========================


    answer = get_answer(question)


    if answer:

        return answer




    # ==========================
    # KNOWLEDGE SEARCH
    # ==========================


    if question in knowledge:


        answer = knowledge[question]


        add_knowledge(
            question,
            answer
        )


        return answer




    return None