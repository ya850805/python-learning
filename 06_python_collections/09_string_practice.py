"""
練習題：字符串練習
"""

string = "itheima itcast boxuegu"

# 統計字符串內有多少個"it"字符
count = string.count("it")
print(f"字符串{string}中it字符有{count}個")

# 將字符串內的空格，全部替換為字符"|"
new_string = string.replace(" ", "|")
print(f"{string}替換後為{new_string}")

# 按照"|"進行字符串分割，得到列表
my_list = new_string.split("|")
print(f"字符串{new_string}，按照'|'進行分割後，得到：{my_list}，類型是：{type(my_list)}")