# ==========================================
# AfriMind AI Core Engine
# Version 16.2 Professional
# Main Intelligence Processing System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from knowledge import knowledge



# ==========================================
# QUESTION CLEANER
# ==========================================

def clean_question(question):
    """
    Cleans user input before processing.
    """

    if not isinstance(question, str):
        return ""

    question = question.lower()

    question = question.strip()

    question = question.replace("?", "")

    return question



# ==========================================
# KNOWLEDGE SEARCH ENGINE
# ==========================================

def search_knowledge(question):
    """
    Searches AfriMind knowledge base.
    """

    if question in knowledge:

        return knowledge[question]

    return None



# ==========================================
# MAIN AFRIMIND BRAIN
# ==========================================

def ask_question(question):
    """
    Main function that receives user questions
    and generates AfriMind responses.
    """


    question = clean_question(question)


    if question == "":

        return "Please enter a valid question."



    answer = search_knowledge(question)


    if answer:

        return answer



    return (
        "I don't know the answer yet. "
        "Please teach me so I can learn."
    )



# ==========================================
# SYSTEM TEST
# ==========================================

if __name__ == "__main__":

    print(
        "AfriMind Core Engine Version 16.2 is running successfully."
    )

    print(
        ask_question("what is afrimind")
    )