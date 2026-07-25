# ==========================================
# AfriMind Personal Awareness Engine
# Version 26.1
# User Understanding Intelligence
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.user_profile import get_profile

from core.preference_engine import (
    get_preference,
    get_interests
)



# ==========================================
# USER AWARENESS MESSAGE
# ==========================================

def get_user_awareness():


    name = get_profile(
        "name"
    )


    language = get_preference(
        "language"
    )


    interests = get_interests()



    message = ""



    if name:

        message += (
            f"Hello {name} 👋\n"
        )

    else:

        message += (
            "Hello 👋\n"
        )



    if language:

        message += (
            f"Your preferred language is {language}.\n"
        )



    if interests:

        message += (
            "Your interests include: "
            + ", ".join(interests)
            + ".\n"
        )



    return message