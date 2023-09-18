import mysql.connector
from transform_data.Transform import Transform

try:
	conn = mysql.connector.connect(user="root", password="root", host="mysql", port="3306", database="userinfo")
	cursor = conn.cursor()

except mysql.connector.errors.ProgrammingError:
	try:
		conn = mysql.connector.connect(user="root", password="root", host="mysql", port="3306", database="db")
		cursor = conn.cursor()
		cursor.execute("CREATE DATABASE userinfo")

	except:
		print("Something went wrong while connecting to database.")

csv = Transform("./csv/MOCK_DATA.csv", "csv")
converted = csv.csv_to_dataframe()

print(converted)
