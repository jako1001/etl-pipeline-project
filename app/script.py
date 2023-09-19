from transform_data.Transform import Transform
from database_operations.DatabaseHandler import DatabaseHandler

db = DatabaseHandler("root", "root", "mysql", "3306", "userinfo")

csv = Transform("./csv/MOCK_DATA.csv", "csv")

df = csv.csv_to_dataframe()

db.create_table("users", df)

db.insert(df, "users")

db.view_table("users")
