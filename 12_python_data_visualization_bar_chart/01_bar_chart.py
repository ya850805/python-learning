"""
柱狀圖基本使用
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar構建基礎柱狀圖
bar = Bar()

# 添加x軸的數據
bar.add_xaxis(["日本", "英國", "美國"])

# 添加y軸數據
bar.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(
    position="right"
))

# 反轉xy軸
bar.reversal_axis()

# 繪圖
bar.render("bar_chart_basic.html")