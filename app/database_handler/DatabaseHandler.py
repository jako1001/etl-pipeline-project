from .db_funcs import connect_to_database
import mysql.connector


class DatabaseHandler:
    def __init__(self, user, password, host, port, database):
        self.conn = connect_to_database(user, password, host, port, database)
        self.cursor = self.conn.cursor()
        self.column_names = []

    def create_table(self, table_name, df):
        """Create a named table with named columns from
        the headers of a DataFrame in the connected MySQL database

        Keyword Arguements: \n
        table_name -- Name that you want the table to be \n
        df -- Pandas DataFrame with headers
        """
        self.column_names = [header for header in list(df)]
        columns_with_types = ", ".join(
            [f"{name} VARCHAR(255)" for name in self.column_names]
        )
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {columns_with_types})"

            self.cursor.execute(query)

        except mysql.connector.errors.ProgrammingError:
            raise mysql.connector.errors.ProgrammingError(
                "Error while creating a table. Did you make sure the CSV file you are using has headers without spaces? (ex: first_name)"
            )

    def insert(self, df, table):
        """Insert data from a DataFrame into a table
        in the connected MySQL database

        Keyword arguements: \n
        df -- Pandas DataFrame \n
        table -- Name of the table in the database
        you want to add data to
        """
        try:
            for _, row in df.iterrows():
                columns = ", ".join(self.column_names)
                placeholders = ", ".join(["%s"] * len(self.column_names))
                query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

                self.cursor.execute(query, tuple(row))

            self.conn.commit()
        except Exception as e:
            print(f"An error occured: {e}")
            self.conn.rollback()
            self.conn.close()
            return "exit"

    def view_table(self, table) -> None:
        """Print the column names and data from a
        specific table in the connected MySQL
        database

        Keyword Arguments: \n
        table -- Name of the table in the database
        you want to view
        """
        try:
            select = f"SELECT * FROM {table}"
            self.cursor.execute(select)
            rows = self.cursor.fetchall()
            column_names = [column[0] for column in self.cursor.description]

            print(", ".join(column_names))
            [print(row) for row in rows]
        except Exception as e:
            print(f"An error occured: {e}")
