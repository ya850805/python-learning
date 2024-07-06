"""
pymysql入門
"""

from pymysql import Connection

# 構建到MySQL數據庫的連接
conn = Connection(
    host="localhost",  # 主機IP
    port=3306,  # 端口
    user="root",  # 帳戶
    password="root"  # 密碼
)

# print(conn.get_server_info())

# 執行非查詢性質SQL
cursor = conn.cursor()  # 獲取游標對象
# 選擇數據庫
conn.select_db("test")
# 執行sql
# cursor.execute("create table test_pymysql2(id int)")

# 執行查詢性質SQL
cursor.execute("select * from t_emp")
results = cursor.fetchall()
for r in results:
    print(r)

# 關閉連接
conn.close()