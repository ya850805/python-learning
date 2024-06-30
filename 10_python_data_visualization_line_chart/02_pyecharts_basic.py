"""
pyecharts 基礎入門
"""

# 導包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 創建折線圖對象
line = Line()

# 給折線圖對象添加x軸數據
line.add_xaxis(["日本", "韓國", "美國"])

# 給折線圖對象添加y軸數據
line.add_yaxis("GDP", [10, 20, 30])

# 設置全局配置項
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)

# 通過render方法，將代碼生成為圖像
line.render()