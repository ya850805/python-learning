"""
練習題：list的常用功能
"""

# 定義列表
ages = [21, 25, 21, 23, 22, 20]

# 追加一個數字31到尾部
ages.append(31)

# 追加一個新的列表到尾部
ages.extend([29, 33, 30])

# 取出第一個元素
print(f"第一個元素：{ages[0]}")

# 取出最後一個元素
print(f"最後一個元素：{ages[-1]}")

# 查找元素31在列表中的下標位置
index = ages.index(31)
print(f"元素31的下標：{index}")

print(f"最後列表的內容是：{ages}")