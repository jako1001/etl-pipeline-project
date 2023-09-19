from transform_data.Transform import Transform
from database_handler.DatabaseHandler import DatabaseHandler

db = DatabaseHandler("root", "root", "mysql", "3306", "userinfo")

txt = Transform("./unstructured/unstructured.txt").unstructured_to_dataframe()

# csv = Transform("./csv/MOCK_DATA.csv")

# df = csv.csv_to_dataframe()

# db.create_table("users", df)

# db.insert(df, "users")

# db.view_table("users")
