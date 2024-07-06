"""
面向對象，數據分析案例，主業務邏輯代碼
實現步驟：
1. 設計一個類，可以完成數據的封裝
2. 設計一個抽象類，定義文件讀取的相關功能，並使用子類實現具體功能
3. 讀取文件，生產數據對象
4. 進行數據需求的邏輯計算(計算每一天的銷售額)
5. 通過pyecharts進行圖形繪製
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 將兩個月份的數據合併為1個list來存儲
all_data: list[Record] = jan_data + feb_data

# 構建MySQL連接對象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    autocommit=True
)

# 獲得游標對象
cursor = conn.cursor()

# 選擇數據庫
conn.select_db("py_sql")

# 組織SQL語句
for record in all_data:
    sql = (f"insert into orders(order_date, order_id, money, province) "
           f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')")
    # 執行sql語句
    cursor.execute(sql)

# 關閉連接對象
conn.close()