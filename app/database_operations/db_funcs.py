import mysql.connector


def connect_to_database(user, password, host, port, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)

        return conn

    except mysql.connector.errors.ProgrammingError:
        conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database="db")
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {database}")
        cursor.close()

        return conn


def format_table_data(names, types):
    i = 0
    data = ""

    while i < len(names) - 1:
        if i == len(names) - 2:
            data = f"{data} {names[i]} {types[i]}"
            break

        data = f"{data} {names[i]} {types[i]},"
        i += 1

    return data
