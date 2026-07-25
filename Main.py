# ==========================================
# AfriMind AI
# Version 16.6
# Main Application Engine
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from core.ai_engine import ask_question
from core.conversation_engine import chat



# ==========================================
# START MESSAGE
# ==========================================

print("================================")
print("🤖 AfriMind AI")
print("Building Intelligence for Africa")
print("Version 16.6")
print("Created by Edward Yakobo Mganga")
print("================================")

print(
    "AfriMind: Hello! I am ready to help you."
)

print(
    "Type 'exit' to close AfriMind."
)



# ==========================================
# MAIN CHAT LOOP
# ==========================================

while True:


    user_input = input(
        "\nYou: "
    )


    user_input = user_input.strip()



    # EXIT SYSTEM

    if user_input.lower() == "exit":

        print(
            "AfriMind: Goodbye. Thank you for using AfriMind AI."
        )

        break



    # ==========================
    # TRY AI ENGINE FIRST
    # ==========================

    answer = ask_question(
        user_input
    )



    # ==========================
    # IF UNKNOWN USE CONVERSATION
    # ==========================

    if answer == "I don't know the answer yet. Please teach me.":

        answer = chat(
            user_input
        )



    print(
        "AfriMind:",
        answer
    )