# ==========================================
# AfriMind Brain
# Version 6.6.1
# Learning Conversation Mode
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
    get_name
)

from interest import (
    save_interest,
    get_interest
)



# Temporary memory for learning
learning_question = None



def clean_question(question):

    question = question.lower().strip()

    question = question.replace("?", "")

    return question





def ask_question(question, name):

    global learning_question


    question = clean_question(question)

    language = detect_language(question)


    remember(
        "user_name",
        name
    )



    # ==========================
    # LEARNING MODE
    # ==========================


    if learning_question:


        add_knowledge(
            learning_question,
            question
        )


        learning_question = None


        return "Thank you. I have learned this information."




    # ==========================
    # EXIT
    # ==========================

    if question == "exit":

        return "EXIT"




    # ==========================
    # GREETING
    # ==========================


    if question in [
        "hello",
        "hi",
        "hey",
        "habari",
        "mambo",
        "hujambo"
    ]:

        return translate_greeting(
            language,
            name
        )




    # ==========================
    # NAME
    # ==========================


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


        set_name(
            user_name
        )


        return f"Nice to meet you {user_name}. I will remember your name."




    # ==========================
    # INTEREST
    # ==========================


    if question.startswith("i like"):


        interest = question.replace(
            "i like",
            ""
        ).strip()


        save_interest(
            interest
        )


        return f"I will remember that you like {interest}."




    if question == "what is my interest":


        interest = get_interest()


        if interest:

            return f"Your interest is {interest}."


        return "I don't know your interest yet."




    # ==========================
    # SEARCH DATABASE
    # ==========================


    answer = get_answer(question)


    if answer:

        return answer




    # ==========================
    # SEARCH KNOWLEDGE
    # ==========================


    if question in knowledge:


        answer = knowledge[question]


        add_knowledge(
            question,
            answer
        )


        return answer




    # ==========================
    # ASK USER TO TEACH
    # ==========================


    learning_question = question


    return "I don't know the answer yet. Please teach me."