# ==========================================
# AfriMind Database System
# Version 8.1 Stable
# SQLite Knowledge Storage
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

import sqlite3


DATABASE_NAME = "afrimind.db"


# ==========================
# CLEAN TEXT
# ==========================

def clean_text(text):

    text = text.lower()

    text = text.strip()

    text = text.replace("?", "")

    return text



# ==========================
# CONNECT DATABASE
# ==========================

def connect_database():

    return sqlite3.connect(
        DATABASE_NAME
    )



# ==========================
# CREATE DATABASE
# ==========================

def create_database():

    conn = connect_database()

    cursor = conn.cursor()


    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS knowledge (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        question TEXT UNIQUE,

        answer TEXT

    )

    """)


    conn.commit()

    conn.close()



# ==========================
# GET ANSWER
# ==========================

def get_answer(question):

    question = clean_text(question)


    conn = connect_database()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT answer
        FROM knowledge
        WHERE question = ?
        """,
        (question,)
    )


    result = cursor.fetchone()


    conn.close()


    if result:

        return result[0]


    return None



# ==========================
# ADD KNOWLEDGE
# ==========================

def add_knowledge(question, answer):

    question = clean_text(question)


    conn = connect_database()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT OR IGNORE INTO knowledge
        (question, answer)
        VALUES (?, ?)
        """,
        (
            question,
            answer
        )
    )


    conn.commit()

    conn.close()



# ==========================
# COUNT KNOWLEDGE
# ==========================

def count_knowledge():

    conn = connect_database()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM knowledge"
    )


    total = cursor.fetchone()[0]


    conn.close()


    return total