import mysql.connector as driver

try:
    conn = driver.connect(
        user = 'root',
        password = 'Nitesh@5414',
        host = 'localhost',
        port = 3306,
        database = 'customers'
    )

    if conn.is_connected():
        print("Connected")

except:
    print("Failed to connect")

cursor = conn.cursor()

sql_query = '''CREATE TABLE customers(
    CUSTOMERS_NAME CHAR(20) NOT NULL,
    PRODUCT_NAME CHAR(30),
    ORDER_VALUE INT

) '''

cursor.execute(sql_query)


conn.close()
cursor.close()