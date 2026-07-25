# ==========================================
# AfriMind AI Desktop App
# Version 1.0
# Desktop Intelligence Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import sys
import os


# ==========================================
# CONNECT WITH AFRIMIND CORE
# ==========================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)



# ==========================================
# IMPORT AFRIMIND BRAIN
# ==========================================

import tkinter as tk
from tkinter import scrolledtext

from core.ai_engine import ask_question



# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "AfriMind AI"
)

window.geometry(
    "700x600"
)



# ==========================================
# CHAT DISPLAY
# ==========================================

chat_box = scrolledtext.ScrolledText(

    window,

    wrap=tk.WORD,

    width=80,

    height=25

)


chat_box.pack(

    padx=10,

    pady=10

)



# ==========================================
# USER INPUT
# ==========================================

user_input = tk.Entry(

    window,

    width=70

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


        # Show user message

        chat_box.insert(

            tk.END,

            "Edward: "

            + question

            + "\n"

        )



        # Ask AfriMind

        answer = ask_question(

            question

        )



        # Show AI answer

        chat_box.insert(

            tk.END,

            "AfriMind: "

            + answer

            + "\n\n"

        )



        # Clear input

        user_input.delete(

            0,

            tk.END

        )



# ==========================================
# SEND BUTTON
# ==========================================

send_button = tk.Button(

    window,

    text="Send",

    command=send_message

)


send_button.pack(

    pady=5

)



# ==========================================
# WELCOME MESSAGE
# ==========================================

chat_box.insert(

    tk.END,

    "AfriMind AI: Hello Edward. I am ready to help Africa.\n\n"

)



# ==========================================
# START APP
# ==========================================

window.mainloop()