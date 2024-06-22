"""
字符串
"""

my_str = "itheima and itcast"

# 通過下標索引取值
value1 = my_str[2]
value2 = my_str[-16]
print(f"從字符串{my_str}取下標為2的元素，值是：{value1}")
print(f"從字符串{my_str}取下標為-16的元素，值是：{value2}")

# 字符串不能修改
# my_str[2] = "H"

# index方法
index = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下標是：{index}")

# replace方法(會得到一個新的字符串)
new_my_str = my_str.replace("it", "xx")
print(f"將字符串{my_str}進行替換後得到{new_my_str}")

# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"將字符串{my_str}進行split切分後得到{my_str_list}，類型是：{type(my_str_list)}")

# strip方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()  # 不傳入參數，會去除首尾空格
print(f"字符串{my_str}被strip後，得到：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")  # 代表去除前後字符串"1"和"2"
print(f"字符串{my_str}被strip('12')後，得到：{new_my_str}")

# 統計字符串中某字符串出現次數
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出現的次數是：{count}")

# 統計字符串的長度
num = len(my_str)
print(f"字符串{my_str}的長度是：{num}")

# 遍歷字符串(while)
str1 = "Jason"
index = 0
while index < len(str1):
    print(str1[index])
    index += 1

# 遍歷字符串(for)
for c in str1:
    print(c)