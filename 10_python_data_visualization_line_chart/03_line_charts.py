"""
折線圖開發
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 處理數據
f_us = open("美國.txt", "r", encoding="UTF-8")
us_data = f_us.read()  # 美國的全部內容

f_jp = open("日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()  # 日本的全部內容

f_in = open("印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()  # 印度的全部內容

# 去掉不合JSON規範的開頭
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不合JSON規範的結尾(去掉最後兩個字符)
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON轉Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 取得trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 獲取日期數據，用於x軸，取2020年數據(到下標314)
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 獲取確診數據，用於y軸，取2020年數據(到下標314)
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成圖表
line = Line()
# 添加x軸數據
line.add_xaxis(us_x_data)  # x軸是共用的，所以使用一個國家的數據即可
# 添加y軸數據
line.add_yaxis("美國確診人數", us_y_data, label_opts=LabelOpts(is_show=False))  # 添加美國y軸數據
line.add_yaxis("日本確診人數", jp_y_data, label_opts=LabelOpts(is_show=False))  # 添加日本y軸數據
line.add_yaxis("印度確診人數", in_y_data, label_opts=LabelOpts(is_show=False))  # 添加印度y軸數據

# 設置全局選項
line.set_global_opts(
    # 標題設置
    title_opts=TitleOpts(title="2020年美日印三國確診人數對比折線圖", pos_left="center", pos_bottom="1%")
)

# 調用render方法，生成圖表
line.render()

# 關閉文件
f_us.close()
f_jp.close()
f_in.close()