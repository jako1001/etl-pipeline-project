from transform_data.Transform import Transform
from database_handler.DatabaseHandler import DatabaseHandler
import sys


def script(file_name, table_name) -> None:
    db = DatabaseHandler("root", "root", "mysql", "3306", "userdata")

    file_path = f"./external_data/{file_name}"

    df = ""
    structure_input = file_name[-3:]

    if structure_input == "csv":
        df = Transform(file_path).csv_to_dataframe()

    else:
        df = Transform(file_path).unstructured_email_and_number_to_dataframe()

    print("Creating database table...")
    db.create_table(table_name, df)

    print("Inserting data into table...")
    db.insert(df, table_name)

    print("Done! Here is the data in your database!: ")
    db.view_table(table_name)

    db.conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <file_name> <table_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    table_name = sys.argv[2]
    script(file_name , table_name)
