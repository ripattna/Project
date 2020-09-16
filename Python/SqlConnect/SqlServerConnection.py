import pyodbc

server = 'DESKTOP-BGG3J7Q'
database = 'rissan_db'

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=YES;')

cnxn_1 = pyodbc.connect(Driver="{SQL Server Native Client 11.0}",
                        Server="DESKTOP-BGG3J7Q",
                        Database="rissan_db",
                        Trusted_Connection="YES")

cnxn_2 = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                        'Server=DESKTOP-BGG3J7Q;'
                        'Database=rissan_db;'
                        'Trusted_Connection=Yes;')

my_cursor = cnxn.cursor()
my_cursor.execute('select * from Persons')

for row in my_cursor:
    print(row)
