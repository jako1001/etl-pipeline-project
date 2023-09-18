import mysql.connector


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = False

    def connect(self) -> str:
        """
        Attempt to connect to MySQL database with given name.
        If database is not found, create one with the given
        name.
        """
        try:
            self.conn = mysql.connector.connect(
                user="root",
                password="root",
                host="mysql",
                port="3306",
                database=self.database_name,
            )

            return f"Successfully connected to database {self.database_name}."

        except mysql.connector.errors.ProgrammingError:
            try:
                self.conn = mysql.connector.connect(
                    user="root",
                    password="root",
                    host="mysql",
                    port="3306",
                    database="db",
                )
                cursor = self.conn.cursor()
                cursor.execute(f"CREATE DATABASE {self.database_name}")

                return f"Successfully connected to database {self.database_name}."

            except:
                return "Something went wrong while attempting to connect to database."