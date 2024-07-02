"""
GDP動態柱狀圖開發
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 讀取數據
f = open("1960-2019全球GDP数据.csv", "r", encoding="UTF-8")
data_lines = f.readlines()

# 關閉文件
f.close()

# 刪除第一條數據
data_lines.pop(0)

# 將數據轉換為字典存儲
# {年份: [[國家, GDP], [國家, GDP], [國家, GDP]...], 年份: [[國家, GDP], [國家, GDP], [國家, GDP]...]}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 國家
    gdp = float(line.split(",")[2])  # GDP(可能存在科學計數，所以轉成float)

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 創建時間軸對象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8名的國家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x軸添加國家
        y_data.append(country_gdp[1] / 100000000)  # y軸添加GDP數據

    # 構建柱狀圖
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(億)", y_data, label_opts=LabelOpts(position="right"))
    # 反轉xy軸
    bar.reversal_axis()

    # 設置每一年圖表的標題
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP數據")
    )
    timeline.add(bar, str(year))

# 設置自動播放
timeline.add_schema(
    play_interval=1000,  # 自動播放時間間隔(ms)
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 繪圖
timeline.render("1960-2019GDP-Top8.html")