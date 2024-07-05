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
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 將兩個月份的數據合併為1個list來存儲
all_data: list[Record] = jan_data + feb_data

# 開始進行數據計算
# 將數據存放在dict {"2011-01-01": 1534, "2011-01-02": 300, ...}
data_dict = {}
for record in all_data:
    if record.date in data_dict:
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可視化圖表開發
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))  # 添加x軸數據
bar.add_yaxis("銷售額", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日銷售額")
)

bar.render("每日銷售額柱狀圖.html")