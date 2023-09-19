import mysql.connector


def connect_to_database(user, password, host, port, database):
    try:
        conn = mysql.connector.connect(
            user=user, password=password, host=host, port=port, database=database
        )

        return conn

    except mysql.connector.errors.ProgrammingError:
        conn = mysql.connector.connect(
            user=user, password=password, host=host, port=port, database="db"
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {database}")
        cursor.close()

        return conn
