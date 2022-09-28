import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="gha93lo22",
  database="antipest"
)

print(mydb)
