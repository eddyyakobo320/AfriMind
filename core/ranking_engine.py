# ==========================================
# AfriMind AI Ranking Engine
# Version 21.1
# Improved Intelligence Evaluation System
# Created by Edward Yakobo Mganga
# ==========================================


def calculate_score(answer, source="unknown"):


    if not answer:

        return 0


    score = 0


    answer = answer.lower()



    # 1. Existence

    score += 20



    # 2. Useful length

    if len(answer) >= 40:

        score += 20


    if len(answer) >= 100:

        score += 10



    # 3. Source trust

    trusted_sources = [

        "module",
        "knowledge",
        "learned",
        "internet",
        "web"

    ]


    if source in trusted_sources:

        score += 25



    # 4. Definition quality

    definition_words = [

        "is",

        "means",

        "refers",

        "ability",

        "process",

        "practice"

    ]


    for word in definition_words:

        if word in answer:

            score += 5



    return score



# ==========================================
# RANK MULTIPLE ANSWERS
# ==========================================

def rank_answers(answers):


    best_answer = None

    best_score = 0



    for item in answers:


        score = calculate_score(

            item["answer"],

            item.get("source","unknown")

        )


        if score > best_score:

            best_score = score

            best_answer = item["answer"]



    return best_answer



# ==========================================
# CONFIDENCE
# ==========================================

def confidence_level(answer):


    score = calculate_score(
        answer
    )


    if score >= 70:

        return "High confidence"


    elif score >= 40:

        return "Medium confidence"


    else:

        return "Low confidence"