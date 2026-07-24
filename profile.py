# ==========================================
# AfriMind User Profile System
# Version 1.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from long_memory import remember_information, recall_information



def save_profile(key, value):
    """
    Save user profile information
    """

    remember_information(
        key,
        value
    )



def get_profile(key):
    """
    Get user profile information
    """

    return recall_information(
        key
    )



def set_name(name):
    """
    Save user's name
    """

    save_profile(
        "name",
        name
    )



def get_name():
    """
    Get user's name
    """

    return get_profile(
        "name"
    )



def set_country(country):
    """
    Save user's country
    """

    save_profile(
        "country",
        country
    )



def get_country():
    """
    Get user's country
    """

    return get_profile(
        "country"
    )



def set_language(language):
    """
    Save user's language
    """

    save_profile(
        "language",
        language
    )



def get_language():
    """
    Get user's language
    """

    return get_profile(
        "language"
    )