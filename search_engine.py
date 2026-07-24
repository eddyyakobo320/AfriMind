# ==========================================
# AfriMind Search Engine
# Version 8.0 Professional
# Smart Search + Typo Correction
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

import re
import difflib


# ==========================
# CLEAN TEXT
# ==========================

def normalize_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        "",
        text
    )

    return text


# ==========================
# GET IMPORTANT WORDS
# ==========================

def get_keywords(text):

    words = normalize_text(text).split()

    stop_words = [

        # English question words
        "what",
        "who",
        "where",
        "when",
        "why",
        "how",

        # Common verbs
        "is",
        "are",
        "was",
        "were",
        "do",
        "does",
        "did",
        "can",
        "could",
        "would",
        "will",
        "shall",

        # Articles
        "the",
        "a",
        "an",
        "of",
        "to",
        "for",
        "about",

        # Request words
        "tell",
        "describe",
        "define",
        "explain",
        "meaning",
        "give",
        "me",
        "please",

        # Swahili
        "ni",
        "nini",
        "maana",
        "ya",
        "kwa"

    ]

    keywords = []

    for word in words:

        if word not in stop_words:

            keywords.append(word)

    return keywords


# ==========================
# WORD SIMILARITY
# ==========================

def word_similarity(word1, word2):

    if word1 == word2:
        return 1.0

    if word1 in word2 or word2 in word1:
        return 0.9

    similarity = difflib.SequenceMatcher(
        None,
        word1,
        word2
    ).ratio()

    return similarity


# ==========================
# SCORE SYSTEM
# ==========================

def calculate_score(question, knowledge_question):

    question_words = get_keywords(question)
    knowledge_words = get_keywords(knowledge_question)

    if not question_words:
        return 0

    total_score = 0

    for q_word in question_words:

        best_score = 0

        for k_word in knowledge_words:

            score = word_similarity(
                q_word,
                k_word
            )

            if score > best_score:
                best_score = score

        total_score += best_score

    return total_score / len(question_words)


# ==========================
# FIND BEST MATCH
# ==========================

def find_best_match(question, knowledge_dict):

    best_match = None
    highest_score = 0

    for item in knowledge_dict:

        score = calculate_score(
            question,
            item
        )

        if score > highest_score:
            highest_score = score
            best_match = item

    if highest_score >= 0.60:
        return best_match

    return None