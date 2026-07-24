# ==========================================
# AfriMind Conversation Memory
# Version 14.0
# Conversation Intelligence System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

conversation = {

    "user_name": "",

    "last_topic": "",

    "last_question": "",

    "last_answer": ""

}


# ==========================
# USER NAME
# ==========================

def remember_user_name(name):

    conversation["user_name"] = name


def get_user_name():

    return conversation["user_name"]


# ==========================
# TOPIC
# ==========================

def remember_topic(topic):

    conversation["last_topic"] = topic


def get_last_topic():

    return conversation["last_topic"]


# ==========================
# QUESTION
# ==========================

def remember_question(question):

    conversation["last_question"] = question


def get_last_question():

    return conversation["last_question"]


# ==========================
# ANSWER
# ==========================

def remember_answer(answer):

    conversation["last_answer"] = answer


def get_last_answer():

    return conversation["last_answer"]


# ==========================
# CLEAR MEMORY
# ==========================

def clear_conversation():

    conversation["user_name"] = ""

    conversation["last_topic"] = ""

    conversation["last_question"] = ""

    conversation["last_answer"] = ""