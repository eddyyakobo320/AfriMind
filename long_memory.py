# ==========================================
# AfriMind Long Term Memory System
# Version 2.0
# Intelligent Memory Architecture
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import connect_database
from datetime import datetime



# ==========================
# CREATE MEMORY TABLE
# ==========================

def create_memory_table():

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_memory (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        key TEXT UNIQUE,

        value TEXT,

        memory_type TEXT,

        created_at TEXT

    )
    """)


    connection.commit()

    connection.close()



# ==========================
# SAVE MEMORY
# ==========================

def remember_information(key, value, memory_type="knowledge"):

    connection = connect_database()

    cursor = connection.cursor()


    date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    try:

        cursor.execute(
            """
            INSERT INTO user_memory
            (key,value,memory_type,created_at)

            VALUES(?,?,?,?)
            """,

            (
                key,
                value,
                memory_type,
                date
            )
        )


    except:

        cursor.execute(
            """
            UPDATE user_memory

            SET value=?,
                memory_type=?,
                created_at=?

            WHERE key=?
            """,

            (
                value,
                memory_type,
                date,
                key
            )
        )


    connection.commit()

    connection.close()



# ==========================
# READ MEMORY
# ==========================

def recall_information(key):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT value
        FROM user_memory

        WHERE key=?
        """,

        (key,)
    )


    result = cursor.fetchone()


    connection.close()


    if result:

        return result[0]


    return None



# ==========================
# SEARCH MEMORY
# ==========================

def search_memory(word):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT key,value
        FROM user_memory

        WHERE key LIKE ?
        OR value LIKE ?
        """,

        (
            "%" + word + "%",
            "%" + word + "%"
        )
    )


    results = cursor.fetchall()


    connection.close()


    return results



# ==========================
# DELETE MEMORY
# ==========================

def forget_information(key):

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM user_memory

        WHERE key=?
        """,

        (key,)
    )


    connection.commit()

    connection.close()



# ==========================
# GET ALL MEMORY
# ==========================

def get_all_information():

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT * FROM user_memory
        """
    )


    results = cursor.fetchall()


    connection.close()


    return results



# CREATE TABLE AUTOMATICALLY

create_memory_table()