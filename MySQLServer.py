import mysql.connector

mydb = mysql.connector.connect(
    host = '127.0.0.1',
    port = '3306',
    user = 'root',
    password = 'Root00root',
    database = 'alx_book_store',
)


print(mydb.get_server_info())

print('Database alx_book_store created successfully!')
