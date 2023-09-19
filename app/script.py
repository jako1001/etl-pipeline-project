from transform_data.Transform import Transform
from database_handler.DatabaseHandler import DatabaseHandler

db = DatabaseHandler("root", "root", "mysql", "3306", "userinfo")

csv = Transform("./csv/MOCK_DATA.csv")

df = csv.csv_to_dataframe()

db.create_table("users", df)

csv.ppp()

db.insert(df, "users")

db.view_table("users")
