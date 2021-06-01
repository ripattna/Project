import pymysql as MySQLdb

# Open database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="root")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("show databases")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print(data)

for x in data:
    print("The database available are:", x)

# disconnect from server
db.close()
