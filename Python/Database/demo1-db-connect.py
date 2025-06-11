import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='customer_db',
    port=3306
)
if conn.is_connected():
    print('Connected to MySQL database')
conn.close()