# ==========================================
# AfriMind Brain
# Version 6.2
# Long Term Memory Integration
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import get_answer, add_knowledge
from memory import remember, recall
from knowledge import knowledge
from language import detect_language
from long_memory import remember_information, recall_information



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



    # Remember user name

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




    # Remember favorite color

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




    # User name

    if question == "what is my name":


        saved_name = recall(
            "user_name"
        )


        if saved_name:

            return f"Your name is {saved_name}."


        return "I don't know your name yet."




    # Language

    if question == "what is my language":


        saved_language = recall(
            "language"
        )


        if saved_language:

            return f"Your preferred language is {saved_language}."


        return "I don't know your preferred language yet."




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




    return None