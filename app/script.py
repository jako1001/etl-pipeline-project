import mysql.connector
from transform_data.read_data_from_csv import read_csv_data

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

print(read_csv_data("./csv/MOCK_DATA.csv"))
