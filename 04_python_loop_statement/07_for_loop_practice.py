"""
練習題：數一數有幾個a
"""

name = "itheima is a brand of itcast"
# 定義一個變量，用來統計有多少個a
count = 0

# for循環統計
for x in name:
    if x == "a":
        count += 1

print(f"{name}中共含有：{count}個字母a")