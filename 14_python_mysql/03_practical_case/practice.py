"""
練習題
"""

from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders")
all_data = cursor.fetchall()

f = open("practice.txt", "w", encoding="UTF-8")

for record in all_data:
    date = str(record[0])
    order_id = str(record[1])
    money = str(record[2])
    province = str(record[3])
    data_str = f"{{\"date\": \"{date}\", \"order_id\": \"{order_id}\", \"money\": {money}, \"province\": \"{province}\"}}\n"
    f.write(data_str)

f.close()

