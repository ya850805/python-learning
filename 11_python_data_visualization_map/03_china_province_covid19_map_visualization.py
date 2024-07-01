"""
河南省疫情地圖開發
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 讀取文件
f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()

# 關閉文件
f.close()

# 獲取河南省數據
# json轉python字典
data_dict = json.loads(data)

# 取到河南省數據
cities_data = data_dict["areaTree"][0]["children"][2]["children"]

# 準備數據為元組放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手動添加济源市數據
data_list.append(("济源市", 5))

# 構建地圖
map = Map()

map.add("河南省疫情分佈", data_list, "河南")

# 設置全局選項
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地圖"),
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
map.render("河南省疫情地圖.html")