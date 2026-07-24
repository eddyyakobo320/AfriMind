# ==========================================
# AfriMind Brain
# Version 5.4
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import get_answer, add_knowledge
from memory import remember, recall
from knowledge import knowledge
from language import detect_language



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



    # Remember user name

    remember(
        "user_name",
        name
    )



    # Exit

    if question == "exit":

        return "EXIT"



    # English greetings

    if question in ["hello", "hi", "hey"]:

        return f"Hello {name}! Welcome to AfriMind AI."



    # Swahili greetings

    if language == "swahili" and question in [
        "habari",
        "mambo",
        "hujambo",
        "salama"
    ]:

        return f"Habari {name}! Karibu AfriMind AI."



    # User name

    if question == "what is my name":


        saved_name = recall("user_name")


        if saved_name:

            return f"Your name is {saved_name}."


        return "I don't know your name yet."



    # Language memory

    if question == "what is my language":


        saved_language = recall("language")


        if saved_language:

            return f"Your preferred language is {saved_language}."


        return "I don't know your preferred language yet."



    # Search database

    answer = get_answer(question)


    if answer:

        return answer



    # Search knowledge base

    if question in knowledge:


        answer = knowledgess[question]


        add_knowledge(
            question,
            answer
        )


        return answer



    # Unknown question

    return Nones