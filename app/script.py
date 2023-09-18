import mysql.connector
from funcs.read_data_from_csv import read_csv_data

try:
  mydb = mysql.connector.connect(user="root", password="root", host="mysql", port="3306", database="userinfo")
  mycursor = mydb.cursor()

except mysql.connector.errors.ProgrammingError:
  try:
    mydb = mysql.connector.connect(user="root", password="root", host="mysql", port="3306", database="db")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE userinfo")

  except:
    print("Something went wrong while connecting to database.")

print(read_csv_data("./csv/MOCK_DATA.csv"))
