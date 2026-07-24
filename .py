# ==========================================
# AfriMind AI
# GUI Version 5.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

import tkinter as tk
from brain import ask_question
from database import add_knowledge
from memory import remember, recall


# Main window
window = tk.Tk()

window.title("AfriMind AI")
window.geometry("700x550")
window.resizable(False, False)


# Get user name from memory
user_name = recall("user_name")


# If no name found
if not user_name:
    user_name = "Guest"
    remember("user_name", user_name)


# Title
title = tk.Label(
    window,
    text="AfriMind AI",
    font=("Arial", 22, "bold")
)

title.pack(pady=10)


# Subtitle
subtitle = tk.Label(
    window,
    text="Building Intelligence for Africa",
    font=("Arial", 12)
)

subtitle.pack()


# Chat area
chat_box = tk.Text(
    window,
    width=80,
    height=22,
    font=("Arial", 11)
)

chat_box.pack(pady=10)


chat_box.insert(
    tk.END,
    f"AfriMind: Welcome back {user_name}!\n"
)

chat_box.insert(
    tk.END,
    "AfriMind: I am ready to help you.\n"
)



# Function to send message
def send_message():

    question = entry.get().strip()

    if question == "":
        return


    chat_box.insert(
        tk.END,
        f"\nYou: {question}\n"
    )


    answer = ask_question(
        question,
        user_name
    )


    if answer:

        chat_box.insert(
            tk.END,
            f"AfriMind: {answer}\n"
        )


    else:

        chat_box.insert(
            tk.END,
            "AfriMind: I don't know the answer yet.\n"
        )


        teach_window = tk.Toplevel(window)

        teach_window.title("Teach AfriMind")

        teach_window.geometry(
            "400x200"
        )


        label = tk.Label(
            teach_window,
            text="Please teach me the answer:"
        )

        label.pack(pady=10)


        answer_box = tk.Entry(
            teach_window,
            width=40
        )

        answer_box.pack()



        def save_answer():

            new_answer = answer_box.get().strip()


            if new_answer:

                add_knowledge(
                    question.lower(),
                    new_answer
                )


                chat_box.insert(
                    tk.END,
                    "AfriMind: Thank you! I have learned something new.\n"
                )


                teach_window.destroy()



        save_button = tk.Button(
            teach_window,
            text="Save",
            command=save_answer
        )

        save_button.pack(pady=10)



    entry.delete(
        0,
        tk.END
    )



# Input box
entry = tk.Entry(
    window,
    width=50,
    font=("Arial", 12)
)

entry.pack(pady=5)



# Send button
send_button = tk.Button(
    window,
    text="Send",
    width=15,
    command=send_message
)

send_button.pack(pady=5)



# Exit button
exit_button = tk.Button(
    window,
    text="Exit",
    width=15,
    command=window.destroy
)

exit_button.pack(pady=5)



# Start application
window.mainloop()