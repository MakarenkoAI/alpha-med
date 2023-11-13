import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'bbs4285ast_T1'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE IF NOT EXISTS first_db')
