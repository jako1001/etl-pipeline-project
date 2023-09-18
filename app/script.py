from transform_data.Transform import Transform
from database_operations.Database import Database

db = Database("userinfo")

csv = Transform("./csv/MOCK_DATA.csv", "csv")
