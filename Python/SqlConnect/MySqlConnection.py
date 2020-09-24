import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    use_pure=True)

my_cursor = conn.cursor()
my_cursor.execute("show databases")

for x in my_cursor:
    print(x)

