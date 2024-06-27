"""
文件的讀取
"""
import time

# 打開文件
f = open("test.txt", "r", encoding="UTF-8")
print(type(f))  # <class '_io.TextIOWrapper'>

# 讀取文件 - read()
# print(f"讀取10個字節的結果：{f.read(10)}")
# print(f"read方法讀取全部內容的結果是：{f.read()}")  # 會接續上一行讀取後的內容開始

print("-----------------------------------------------------------------------------")

# 讀取文件 - readLines()
# lines = f.readlines()  # 讀取文件的全部行，封裝到列表中(同一個f對象也會接續往下讀取)
# print(f"lines對象的類型：{type(lines)}")  # <class 'list'>
# print(f"lines對象的內容：{lines}")

# 讀取文件 - readLine()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行數據是：{line1}")
# print(f"第二行數據是：{line2}")
# print(f"第三行數據是：{line3}")

# for循環讀取文件行
# for line in f:
#     print(f"每一行數據是：{line}")

# 文件的關閉
# f.close()

# with open語法操作(操作結束會自動close文件)
with open("test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行數據是：{line}")
