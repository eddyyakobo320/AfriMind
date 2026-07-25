# ==========================================
# AfriMind AI Desktop App
# Version 23.2
# Enhanced Desktop Intelligence Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import sys
import os
import tkinter as tk
from tkinter import scrolledtext


# ==========================================
# CONNECT AFRIMIND CORE
# ==========================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from core.ai_engine import ask_question
from core.conversation_engine import (
    save_conversation,
    get_recent_conversations
)



# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "AfriMind AI - Building Intelligence for Africa"
)

window.geometry(
    "750x650"
)



# ==========================================
# CHAT AREA
# ==========================================

chat_box = scrolledtext.ScrolledText(

    window,

    wrap=tk.WORD,

    width=85,

    height=30,

    font=("Arial", 11)

)

chat_box.pack(

    padx=10,

    pady=10

)



# ==========================================
# LOAD PREVIOUS MEMORY
# ==========================================

chat_box.insert(

    tk.END,

    "AfriMind AI: Hello Edward. I am ready to help Africa.\n\n"

)


history = get_recent_conversations()


for chat in history:

    if "user" in chat:

        chat_box.insert(

            tk.END,

            "Edward: "

            + chat["user"]

            + "\n"

        )


    if "assistant" in chat:

        chat_box.insert(

            tk.END,

            "AfriMind: "

            + chat["assistant"]

            + "\n\n"

        )



# ==========================================
# USER INPUT
# ==========================================

user_input = tk.Entry(

    window,

    width=70,

    font=("Arial", 12)

)

user_input.pack(

    padx=10,

    pady=5

)



# ==========================================
# SEND MESSAGE
# ==========================================

def send_message():

    question = user_input.get()


    if question.strip():


        chat_box.insert(

            tk.END,

            "Edward: "

            + question

            + "\n"

        )


        answer = ask_question(

            question

        )


        chat_box.insert(

            tk.END,

            "AfriMind: "

            + answer

            + "\n\n"

        )


        save_conversation(

            question,

            answer

        )


        user_input.delete(

            0,

            tk.END

        )



# ==========================================
# ENTER KEY SUPPORT
# ==========================================

def enter_pressed(event):

    send_message()



user_input.bind(

    "<Return>",

    enter_pressed

)



# ==========================================
# CLEAR CHAT
# ==========================================

def clear_chat():

    chat_box.delete(

        "1.0",

        tk.END

    )


    chat_box.insert(

        tk.END,

        "AfriMind AI: Chat cleared. I am ready.\n\n"

    )



# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(window)

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



# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()