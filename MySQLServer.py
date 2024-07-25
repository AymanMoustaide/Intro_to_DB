import mysql.connector


mydb = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    user = 'root',
    password = 'Root00root',
    database = 'alx_book_store',
)

if mydb.is_connected():
    print('Database alx_book_store is connected!')

else:
    #* EXECUTE COMMAND TO DB
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')








