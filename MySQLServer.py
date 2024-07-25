import mysql.connector



mydb = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    user = 'root',
    password = 'Root00root',
    database = 'alx_book_store',
)

#* EXECUTE COMMAND TO DB
if mydb.is_connected():
    print('DATABASE AlX_STORE_STORE WORK SUCCESSFULLY!')

else:
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE')





