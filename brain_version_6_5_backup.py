# ==========================================
# AfriMind Brain
# Version 6.5
# Interest Memory Integration
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
    get_interest,
    save_hobby,
    get_hobby,
    save_favorite_topic,
    get_favorite_topic
)



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



    # ==========================
    # NAME SYSTEM
    # ==========================


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




    # ==========================
    # INTEREST MEMORY
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




    if question.startswith("napenda"):


        interest = question.replace(
            "napenda",
            ""
        ).strip()


        save_interest(
            interest
        )


        return f"Nitakumbuka kuwa unapenda {interest}."




    if question in [
        "what is my interest",
        "what are my interests",
        "ninapenda nini"
    ]:


        interest = get_interest()


        if interest:

            if language == "swahili":

                return f"Unapenda {interest}."

            return f"Your interest is {interest}."


        return "I don't know your interest yet."




    # ==========================
    # HOBBY MEMORY
    # ==========================


    if question.startswith("my hobby is"):


        hobby = question.replace(
            "my hobby is",
            ""
        ).strip()


        save_hobby(
            hobby
        )


        return f"I will remember that your hobby is {hobby}."




    if question == "what is my hobby":


        hobby = get_hobby()


        if hobby:

            return f"Your hobby is {hobby}."


        return "I don't know your hobby yet."




    # ==========================
    # FAVORITE TOPIC
    # ==========================


    if question.startswith("i like learning"):


        topic = question.replace(
            "i like learning",
            ""
        ).strip()


        save_favorite_topic(
            topic
        )


        return f"I will remember that you like learning {topic}."




    if question == "what do i like learning":


        topic = get_favorite_topic()


        if topic:

            return f"You like learning {topic}."


        return "I don't know your favorite topic yet."




    # ==========================
    # DATABASE
    # ==========================


    answer = get_answer(question)


    if answer:

        return answer




    # ==========================
    # KNOWLEDGE
    # ==========================


    if question in knowledge:


        answer = knowledge[question]


        add_knowledge(
            question,
            answer
        )


        return answer




    return None