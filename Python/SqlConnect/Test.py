import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(host="localhost", user='root', password='root', use_pure=True)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    print("Connection is established!")
    # cnx.close()

my_cursor = cnx.cursor()
my_cursor.execute("show databases")
for x in my_cursor:
    print(x)



