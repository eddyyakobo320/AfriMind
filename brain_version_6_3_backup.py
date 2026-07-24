# ==========================================
# AfriMind Brain
# Version 6.3
# User Profile Integration
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import get_answer, add_knowledge
from memory import remember, recall
from knowledge import knowledge
from language import detect_language
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
    Clean user question
    """

    question = question.lower().strip()

    question = question.replace("?", "")

    return question





def ask_question(question, name):


    question = clean_question(question)

    language = detect_language(question)



    # Save current user name

    remember(
        "user_name",
        name
    )



    # Exit

    if question == "exit":

        return "EXIT"




    # Greetings

    if question in ["hello", "hi", "hey"]:

        return f"Hello {name}! Welcome to AfriMind AI."



    if language == "swahili" and question in [
        "habari",
        "mambo",
        "hujambo",
        "salama"
    ]:

        return f"Habari {name}! Karibu AfriMind AI."




    # Save name

    if question.startswith("my name is"):


        user_name = question.replace(
            "my name is",
            ""
        ).strip()


        set_name(
            user_name
        )


        return f"Nice to meet you {user_name}. I will remember your name."




    # Recall name

    if question == "what is my name":


        saved_name = get_name()


        if saved_name:

            return f"Your name is {saved_name}."


        return "I don't know your name yet."




    # Save country

    if question.startswith("i live in"):


        country = question.replace(
            "i live in",
            ""
        ).strip()


        set_country(
            country
        )


        return f"I will remember that you live in {country}."




    # Recall country

    if question in [
        "where do i live",
        "what is my country"
    ]:


        country = get_country()


        if country:

            return f"You live in {country}."


        return "I don't know where you live yet."




    # Save language

    if question.startswith("my language is"):


        lang = question.replace(
            "my language is",
            ""
        ).strip()


        set_language(
            lang
        )


        return f"I will remember that your language is {lang}."




    # Recall language

    if question == "what is my language":


        lang = get_language()


        if lang:

            return f"Your preferred language is {lang}."


        return "I don't know your language yet."




    # Save favorite color

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




    # Recall favorite color

    if question == "what is my favorite color":


        color = recall_information(
            "favorite_color"
        )


        if color:

            return f"Your favorite color is {color}."


        return "I don't know your favorite color yet."




    # Search database

    answer = get_answer(question)


    if answer:

        return answer




    # Search knowledge

    if question in knowledge:


        answer = knowledge[question]


        add_knowledge(
            question,
            answer
        )


        return answer




    return None