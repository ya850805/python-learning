"""
pysql數據插入
"""
from pymysql import Connection

# 構建到MySQL數據庫的連接
conn = Connection(
    host="localhost",  # 主機IP
    port=3306,  # 端口
    user="root",  # 帳戶
    password="root",  # 密碼
    autocommit=True  # 設定自動提交
)

# 獲取游標對象
cursor = conn.cursor()
# 選擇數據庫
conn.select_db("test")
# 執行SQL
cursor.execute("insert into t_emp(emp_name, emp_salary) values('john', 999.1)")
# 通過commit確認
# conn.commit()

# 關閉連接
conn.close()