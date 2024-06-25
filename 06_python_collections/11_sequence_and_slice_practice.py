"""
練習題：序列的切片實踐
"""

# 取得"黑马程序员"
my_str = "万过薪月，员序程马黑来，nohtyP学"

str_list = my_str.split("，")
target = str_list[1]
result = target[4::-1]
print(f"result = {result}")

# 倒序字符串，切片取出
result_1 = my_str[::-1][9:14]
print(f"方式1結果：{result_1}")

# 切片取出，然後倒序
result_2 = my_str[5:10][::-1]
print(f"方式2結果：{result_2}")

# split分隔"，" replace替換"来"為空，倒序字符串
string = my_str.split("，")[1]
result_3 = string.replace("来", "")[::-1]
print(f"方式3結果：{result_3}")
