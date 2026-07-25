# ==========================================
# AfriMind AI Desktop App
# Version 24.0
# Professional Desktop Intelligence Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import sys
import os
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime



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
    "AfriMind AI | Building Intelligence for Africa"
)

window.geometry(
    "800x700"
)



# ==========================================
# CHAT DISPLAY
# ==========================================

chat_box = scrolledtext.ScrolledText(

    window,

    wrap=tk.WORD,

    width=90,

    height=32,

    font=("Arial", 11)

)

chat_box.pack(

    padx=10,

    pady=10

)



# ==========================================
# LOAD MEMORY
# ==========================================

chat_box.insert(

    tk.END,

    "AfriMind AI: Hello Edward. I am ready to help Africa.\n\n"

)



try:

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


except Exception:

    pass




# ==========================================
# USER INPUT
# ==========================================

user_input = tk.Entry(

    window,

    width=75,

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


        time = datetime.now().strftime(
            "%H:%M"
        )


        chat_box.insert(

            tk.END,

            f"[{time}] Edward: {question}\n"

        )


        window.update()



        try:


            answer = ask_question(

                question

            )


        except Exception as error:


            answer = (

                "Sorry Edward, I found a system error: "

                + str(error)

            )



        chat_box.insert(

            tk.END,

            f"[{time}] AfriMind: {answer}\n\n"

        )


        chat_box.see(

            tk.END

        )



        save_conversation(

            question,

            answer

        )



        user_input.delete(

            0,

            tk.END

        )



        user_input.focus()



# ==========================================
# ENTER BUTTON
# ==========================================

user_input.bind(

    "<Return>",

    lambda event: send_message()

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

        "AfriMind AI: Conversation cleared.\n\n"

    )




# ==========================================
# BUTTON AREA
# ==========================================

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

    padx=10

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

    padx=10

)



# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(

    window,

    text="AfriMind AI Version 24.0 | Building Intelligence for Africa",

    font=("Arial", 9)

)


footer.pack(

    pady=10

)



# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()