"""
函數快速體驗
"""

# 需求：統計字串的長度，不使用內置函數len()
str1 = "Hello"
str2 = "world!!!"
str3 = "python"


# count = 0
# for i in str1:
#     count += 1
# print(f"字符串{str1}的長度是：{count}")
#
# count = 0
# for i in str2:
#     count += 1
# print(f"字符串{str2}的長度是：{count}")
#
# count = 0
# for i in str3:
#     count += 1
# print(f"字符串{str3}的長度是：{count}")

# 可以使用函數來優化過程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的長度是：{count}")


my_len(str1)
my_len(str2)
my_len(str3)
