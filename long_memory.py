# ==========================================
# AfriMind Long Term Memory System
# Version 1.0
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from database import connect_database



def create_memory_table():

    """
    Create user memory table
    """

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_memory (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        key TEXT UNIQUE,

        value TEXT

    )
    """)


    connection.commit()

    connection.close()





def remember_information(key, value):

    """
    Save information in long memory
    """

    connection = connect_database()

    cursor = connection.cursor()


    try:

        cursor.execute(
            """
            INSERT INTO user_memory(key, value)
            VALUES(?, ?)
            """,
            (key, value)
        )


        connection.commit()


    except:

        cursor.execute(
            """
            UPDATE user_memory
            SET value = ?
            WHERE key = ?
            """,
            (value, key)
        )


        connection.commit()


    connection.close()





def recall_information(key):

    """
    Get information from memory
    """

    connection = connect_database()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT value
        FROM user_memory
        WHERE key = ?
        """,
        (key,)
    )


    result = cursor.fetchone()


    connection.close()


    if result:

        return result[0]


    return None





# Create memory table automatically

create_memory_table()