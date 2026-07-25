# ==========================================
# AfriMind AI Desktop App
# Version 28.2
# Professional Intelligence Interface
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

import sys
import os
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


# Connect AfriMind Core

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


from core.ai_engine import ask_question


# ==========================================
# WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "AfriMind AI - Building Intelligence for Africa"
)

window.geometry(
    "900x650"
)



# ==========================================
# HEADER
# ==========================================

header = tk.Label(
    window,
    text=
    "🌍 AfriMind AI\n"
    "Building Intelligence for Africa\n"
    "Version 28.2",
    font=("Arial", 16, "bold")
)

header.pack(
    pady=10
)



# ==========================================
# STATUS
# ==========================================

status = tk.Label(
    window,
    text="Status: Online 🟢 Learning Brain Active",
    font=("Arial", 11)
)

status.pack()



# ==========================================
# CHAT BOX
# ==========================================

chat_box = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial", 12)
)

chat_box.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)


chat_box.insert(
    tk.END,
    "🤖 AfriMind: Hello Edward. I am ready to help Africa.\n\n"
)



# ==========================================
# INPUT
# ==========================================

frame = tk.Frame(window)

frame.pack(
    fill=tk.X,
    padx=10
)


entry = tk.Entry(
    frame,
    font=("Arial",12)
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True
)



# ==========================================
# SEND
# ==========================================

def send_message():

    question = entry.get()


    if question.strip():


        time = datetime.now().strftime("%H:%M")


        chat_box.insert(
            tk.END,
            f"👤 Edward [{time}]: {question}\n"
        )


        window.update()


        try:

            answer = ask_question(
                question
            )

        except Exception as e:

            answer = (
                "System error: "
                + str(e)
            )



        chat_box.insert(
            tk.END,
            f"🤖 AfriMind [{time}]: {answer}\n\n"
        )


        chat_box.see(
            tk.END
        )


        entry.delete(
            0,
            tk.END
        )



# ==========================================
# BUTTON
# ==========================================

button = tk.Button(
    frame,
    text="Ask AfriMind",
    command=send_message,
    width=15
)


button.pack(
    side=tk.RIGHT,
    padx=5
)



entry.bind(
    "<Return>",
    lambda event: send_message()
)



# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    window,
    text=
    "AfriMind AI v28.2 | Created by Edward Yakobo Mganga"
)

footer.pack(
    pady=5
)



# START

window.mainloop()