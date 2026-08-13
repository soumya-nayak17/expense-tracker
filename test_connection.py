import mysql.connector
conn=mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="expense_tracker"
 )

if conn.is_connected():
    print("Connected successfully")
else:
    print("Connection failed")