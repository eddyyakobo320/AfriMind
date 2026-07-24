# ==========================================
# AfriMind Conversation System
# Version 1.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

conversation_history = []


def save_message(speaker, message):
    """
    Save a conversation message.
    """

    conversation_history.append({
        "speaker": speaker,
        "message": message
    })


def get_history():
    """
    Return all conversation history.
    """

    return conversation_history


def clear_history():
    """
    Clear the conversation history.
    """

    conversation_history.clear()