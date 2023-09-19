from .db_funcs import connect_to_database


class DatabaseHandler:
    def __init__(self, user, password, host, port, database):
        self.conn = connect_to_database(user, password, host, port, database)
        self.cursor = self.conn.cursor()
        self.column_names = []

    def create_table(self, table_name, df):
        self.column_names = [header for header in list(df)]

        columns_with_types = ", ".join(
            [f"{name} VARCHAR(255)" for name in self.column_names]
        )

        query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {columns_with_types})"

        self.cursor.execute(query)

    def insert(self, df, table):
        for _, row in df.iterrows():
            columns = ", ".join(self.column_names)
            placeholders = ", ".join(["%s"] * len(self.column_names))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            self.cursor.execute(query, tuple(row))

        self.conn.commit()

    def view_table(self, table):
        select = f"SELECT * FROM {table}"
        self.cursor.execute(select)
        rows = self.cursor.fetchall()
        column_names = [column[0] for column in self.cursor.description]

        print(", ".join(column_names))
        [print(row) for row in rows]
