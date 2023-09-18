from transform_data.Transform import Transform
from database_operations.DatabaseOp import DatabaseOp

db = DatabaseOp("userinfo")
print(db.connect())

csv = Transform("./csv/MOCK_DATA.csv", "csv")
converted = csv.csv_to_dataframe()

print(converted)

db.connection_data()
