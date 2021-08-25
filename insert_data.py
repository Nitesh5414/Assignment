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

sql_query = '''INSERT INTO customers(CUSTOMERS_NAME, PRODUCT_NAME, ORDER_VALUE)
            VALUES('sonu', 'Tyre', 30)'''

try:
    cursor.execute(sql_query)
    conn.commit()
except:
    conn.rollback()


conn.close()
cursor.close()