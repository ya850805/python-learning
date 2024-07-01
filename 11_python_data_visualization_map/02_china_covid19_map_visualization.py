"""
疫情可視化地圖
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 讀取數據文件
f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部數據

# 關閉文件
f.close()

# 取到各個省份數據
# 將字符串json轉換為python字典
data_dict = json.loads(data)

# 從字典中取出省份的數據
province_data_list = data_dict["areaTree"][0]["children"]

# 組裝每個省份和確診人數為元組，並將各個省的數據都裝入列表內
data_list = []  # 繪圖需要用的數據列表
for province_data in province_data_list:
    province_name = province_data["name"] + "省"  # 省份名稱
    province_confirm = province_data["total"]["confirm"]  # 確診人數
    data_list.append((province_name, province_confirm))

# 創建地圖對象
map = Map()

# 添加數據
map.add("各省份確診人數", data_list, "china")

# 設置全局配置，定製分段的
map.set_global_opts(
    title_opts=TitleOpts(title="疫情地圖"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+人", "color": "#990033"}
        ]
    )
)

# 繪圖
map.render("covid.html")