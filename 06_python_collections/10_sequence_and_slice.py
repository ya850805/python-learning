"""
序列與切片
"""

# 對list進行切片，從1開始，4結束，步長1
my_list = [0, 1, 2, 3, 4, 5, 6]
result_1 = my_list[1:4]  # 步長默認是1，可以省略不寫
print(f"結果1：{result_1}")

# 對tuple進行切片，從頭開始，到最後結束，步長1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result_2 = my_tuple[:]  # 起始和結束不寫表示從頭到尾，步長為1可以不寫
print(f"結果2：{result_2}")

# 對str進行切片，從頭開始，到最後結束，步長2
my_str = "01234567"
result_3 = my_str[::2]
print(f"結果3：{result_3}")

# 對str進行切片，從頭開始，到最後結束，步長-1
my_str = "01234567"
result_4 = my_str[::-1]  # 等同於將序列進行反轉
print(f"結果4：{result_4}")

# 對列表進行切片，從3開始，到1結束，步長-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result_5 = my_list[3:1:-1]
print(f"結果5：{result_5}")

# 對元組進行切片，從頭開始，到尾結束，步長2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result_6 = my_tuple[::-2]
print(f"結果6：{result_6}")