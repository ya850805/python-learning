"""
tuple元組(不可修改的list)
"""

# 定義元組
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()

print(f"t1的類型是：{type(t1)}，內容是：{t1}")
print(f"t2的類型是：{type(t2)}，內容是：{t2}")
print(f"t3的類型是：{type(t3)}，內容是：{t3}")

# 定義單個元素的元組，必須帶有逗號，否則不是元組
t4 = ("hello", )
print(f"t4的類型是：{type(t4)}，內容是：{t4}")

# 元組的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的類型是：{type(t5)}，內容是：{t5}")

# 下標索引去取出內容
print(f"從嵌套元組中取出的數據是：{t5[1][2]}")

# index查找方法
t6 = ("a", "b", "c")
index = t6.index("b")
print(f"在元組t6中查找b，下標是：{index}")

# count統計方法
t7 = ("a", "b", "b", "b", "c")
count = t7.count("b")
print(f"在元組t7中統計b字符串的數量有：{count}個")

# len函數統計元組元素數量
t8 = ("a", "b", "b", "b", "c")
num = len(t8)
print(f"t8元組中的元素有：{num}個")

# 元組的遍歷(while)
index = 0
while index < len(t8):
    print(f"元組的元素有：{t8[index]}")
    index += 1

# 元組的遍歷(for)
for element in t8:
    print(f"---元組的元素有：{element}")

# 修改元組內容
# t8[0] = "name1"  # 錯誤示範，元組的元素不能修改

# 元組內部的list是可以修改的
t9 = (1, 2, ["name1", "name2"])
print(f"t9的內容是：{t9}")
t9[2][0] = "name3"
t9[2][1] = "name4"
print(f"t9的內容是：{t9}")