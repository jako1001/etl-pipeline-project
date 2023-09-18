from .db_funcs import connect_to_database, format_table_data


class DatabaseHandler:
    def __init__(self, user, password, host, port, database):
        self.conn = connect_to_database(user, password, host, port, database)

    def create_table(self, table_name, df):
        cursor = self.conn.cursor()
        column_names = [header for header in list(df)]
        column_types = ["VARCHAR(255)"] * len(column_names)

        query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY,{format_table_data(column_names, column_types)})"

        if table_name:
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)


    # def insert(self, df, table):
    #     cursor = self.conn.cursor()

    #     df.to_sql(table, con=self.conn, if_exists="append", index=False)

    #     print(df)
    #     # query = f"INSERT INTO {table} "
