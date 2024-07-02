"""
帶有時間線的柱狀圖
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["日本", "英國", "美國"])
bar1.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(
    position="right"
))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["日本", "英國", "美國"])
bar2.add_yaxis("GDP", [20, 30, 50], label_opts=LabelOpts(
    position="right"
))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["日本", "英國", "美國"])
bar3.add_yaxis("GDP", [40, 60, 90], label_opts=LabelOpts(
    position="right"
))
bar3.reversal_axis()

# 構建時間線對象
timeline = Timeline({"theme": ThemeType.ESSOS})

# 在時間線內添加柱狀圖對象
timeline.add(bar1, "點1")
timeline.add(bar2, "點2")
timeline.add(bar3, "點3")

# 設置自動播放
timeline.add_schema(
    play_interval=1000,  # 自動播放時間間隔(ms)
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 繪圖是用時間線繪圖
timeline.render("bar_chart_with_timeline.html")
