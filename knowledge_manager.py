from database import connect_database


def count_knowledge():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM knowledge")

    result = cursor.fetchone()

    connection.close()

    return result[0]


def knowledge_exists(question):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT question FROM knowledge WHERE question = ?",
        (question,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None


def add_managed_knowledge(question, answer):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO knowledge(question, answer)
        VALUES(?, ?)
        """,
        (question, answer)
    )

    connection.commit()

    connection.close()

    return True