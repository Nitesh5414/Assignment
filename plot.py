import mysql.connector as driver
import pandas as pd
from pandas.core.reshape import tile
import plotly.graph_objs as go

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

sql_query =''' SELECT * FROM customers'''

df = pd.read_sql_query(sql_query, conn)

data = [go.Bar(
    x = df['CUSTOMERS_NAME'],
    y = df['ORDER_VALUE']
)]

fig = go.Figure(data=data)
fig.update_layout(
    title = "Customer Record",
    xaxis_title = 'Customer',
    yaxis_title = 'Order',
    
)
fig.show()
print(df)
