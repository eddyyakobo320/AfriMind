# ==========================================
# AfriMind AI
# Main Version 5.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import load_initial_knowledge
from memory import remember, recall
from config import APP_NAME, VERSION, CREATOR, SLOGAN, WELCOME_MESSAGE


# Load AfriMind knowledge
load_initial_knowledge()


print("================================")
print(WELCOME_MESSAGE)
print(SLOGAN)
print("Created by", CREATOR)
print("Version", VERSION)
print("================================")


# Check user memory

saved_name = recall("user_name")


if saved_name:

    name = saved_name

    print(f"Welcome back {name}!")


else:

    name = input("What is your name? ").strip()

    remember(
        "user_name",
        name
    )

    print(f"Hello {name}!")


print(
    f"I am {APP_NAME}. You can ask me anything."
)


print(
    "Please open gui.py to start AfriMind interface."
)