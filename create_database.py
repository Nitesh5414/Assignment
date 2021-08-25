import mysql.connector as driver

try:
    conn = driver.connect(
        user = 'root',
        password = 'Nitesh@5414',
        host = 'localhost',
        port = 3306
    )

    if conn.is_connected():
        print("Connected")

except:
    print("Failed to connect")

cursor = conn.cursor()

sql_query = 'CREATE DATABASE customers'

cursor.execute(sql_query)

conn.close()
cursor.close()
