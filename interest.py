# ==========================================
# AfriMind Interest Memory System
# Version 1.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from long_memory import remember_information, recall_information



def save_interest(interest):

    """
    Save user's interest
    """

    remember_information(
        "interest",
        interest
    )



def get_interest():

    """
    Get user's interest
    """

    return recall_information(
        "interest"
    )



def save_hobby(hobby):

    """
    Save user's hobby
    """

    remember_information(
        "hobby",
        hobby
    )



def get_hobby():

    """
    Get user's hobby
    """

    return recall_information(
        "hobby"
    )



def save_favorite_topic(topic):

    """
    Save favorite learning topic
    """

    remember_information(
        "favorite_topic",
        topic
    )



def get_favorite_topic():

    """
    Get favorite learning topic
    """

    return recall_information(
        "favorite_topic"
    )