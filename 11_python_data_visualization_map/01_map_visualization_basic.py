"""
地圖可視化基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts


# 準備地圖對象
map = Map()

# 準備數據
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("吉林省", 299),
    ("四川省", 399),
    ("浙江省", 499)
]

# 添加數據
map.add("測試地圖", data, "china")

# 設置全局選項
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500人", "color": "#990033"}
        ]
    )
)

# 繪圖
map.render()