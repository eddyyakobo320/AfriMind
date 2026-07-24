# ==========================================
# AfriMind GUI
# Version 7.1 Learning System
# User Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import tkinter as tk

from brain import ask_question
from learning import teach_afrimind


learning_question = None



# ==========================
# SEND MESSAGE
# ==========================

def send_message():

    global learning_question


    question = user_input.get()


    if question.strip() == "":

        return



    # If AfriMind is learning

    if learning_question:


        teach_afrimind(
            learning_question,
            question
        )


        chat_box.insert(
            tk.END,
            "AfriMind: Thank you. I have learned this information.\n\n"
        )


        learning_question = None


        user_input.delete(
            0,
            tk.END
        )


        return



    chat_box.insert(
        tk.END,
        "You: " + question + "\n"
    )


    answer = ask_question(
        question
    )



    # Activate learning mode

    if answer == "I don't know the answer yet. Please teach me.":

        learning_question = question



    chat_box.insert(
        tk.END,
        "AfriMind: " + answer + "\n\n"
    )


    user_input.delete(
        0,
        tk.END
    )





# ==========================
# WINDOW
# ==========================

window = tk.Tk()


window.title(
    "AfriMind AI"
)


window.geometry(
    "700x500"
)




# ==========================
# TITLE
# ==========================

title = tk.Label(
    window,
    text="AfriMind AI - Building Intelligence for Africa",
    font=("Arial", 16)
)


title.pack(
    pady=10
)




# ==========================
# CHAT AREA
# ==========================

chat_box = tk.Text(
    window,
    height=20,
    width=80
)


chat_box.pack()




# ==========================
# INPUT
# ==========================

user_input = tk.Entry(
    window,
    width=60,
    font=("Arial", 12)
)


user_input.pack(
    pady=10
)




# ==========================
# BUTTON
# ==========================

send_button = tk.Button(
    window,
    text="Send",
    command=send_message
)


send_button.pack()




# ==========================
# WELCOME MESSAGE
# ==========================

chat_box.insert(
    tk.END,
    "AfriMind: Welcome! I am AfriMind AI.\n\n"
)

chat_box.insert(
    tk.END,
    "AfriMind: Welcome! I am AfriMind AI.\n\n"
)


# ==========================
# START PROGRAM
# ==========================

window.mainloop()