# ==========================================
# AfriMind AI GUI
# Version 1.0 Professional Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

import tkinter as tk
from tkinter import scrolledtext

from brain import ask_question
from learning import teach_afrimind


learning_question = None


# ==========================
# SEND MESSAGE FUNCTION
# ==========================

def send_message():

    global learning_question

    question = user_input.get().strip()


    if question == "":
        return


    chat_box.insert(
        tk.END,
        "You: " + question + "\n\n"
    )


    # Learning mode

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


    else:


        answer = ask_question(
            question
        )


        chat_box.insert(
            tk.END,
            "AfriMind: " + answer + "\n\n"
        )


        if answer == "I don't know the answer yet. Please teach me.":

            learning_question = question


    user_input.delete(
        0,
        tk.END
    )


    chat_box.see(
        tk.END
    )



# ==========================
# CLEAR CHAT
# ==========================

def clear_chat():

    chat_box.delete(
        "1.0",
        tk.END
    )



# ==========================
# MAIN WINDOW
# ==========================

window = tk.Tk()

window.title(
    "AfriMind AI - Building Intelligence for Africa"
)


window.geometry(
    "850x600"
)


window.resizable(
    False,
    False
)



# ==========================
# TITLE
# ==========================

title = tk.Label(
    window,
    text="🤖 AfriMind AI",
    font=("Arial", 24, "bold")
)

title.pack(
    pady=5
)



subtitle = tk.Label(
    window,
    text="Building Intelligence for Africa",
    font=("Arial", 12)
)

subtitle.pack()



# ==========================
# CHAT BOX
# ==========================

chat_box = scrolledtext.ScrolledText(

    window,

    width=90,

    height=25,

    font=("Arial", 11)

)


chat_box.pack(
    padx=10,
    pady=10
)



# ==========================
# INPUT AREA
# ==========================

user_input = tk.Entry(

    window,

    width=70,

    font=("Arial", 12)

)


user_input.pack(
    pady=5
)



# Press ENTER to send

user_input.bind(
    "<Return>",
    lambda event: send_message()
)



# ==========================
# BUTTONS
# ==========================


button_frame = tk.Frame(
    window
)


button_frame.pack()



send_button = tk.Button(

    button_frame,

    text="Send",

    width=15,

    command=send_message

)


send_button.grid(
    row=0,
    column=0,
    padx=5
)



clear_button = tk.Button(

    button_frame,

    text="Clear",

    width=15,

    command=clear_chat

)


clear_button.grid(
    row=0,
    column=1,
    padx=5
)



# ==========================
# WELCOME MESSAGE
# ==========================


chat_box.insert(

    tk.END,

    "AfriMind: Welcome! I am AfriMind AI.\n"

)


chat_box.insert(

    tk.END,

    "AfriMind: How can I help you today?\n\n"

)


chat_box.insert(

    tk.END,

    "Version 1.0\n"

)


chat_box.insert(

    tk.END,

    "Created by Edward Yakobo Mganga\n\n"

)



# ==========================
# START APPLICATION
# ==========================

window.mainloop()