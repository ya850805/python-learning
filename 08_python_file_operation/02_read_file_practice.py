"""
練習題：單詞計數
"""

f = open("practice1.txt", "r", encoding="UTF-8")

# 方式一：讀取全部內容，通過字符串count方法統計itheima單詞數量
# count = f.read().count("itheima")
# print(f"itheima在文件中出現{count}次")


# 方式二：讀取內容，一行一行讀取
count = 0
for line in f:
    words = line.strip().split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima在文件中出現{count}次")

# 關閉文件
f.close()