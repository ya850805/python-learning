"""
數據類型轉換
"""

# 將數字類型轉換成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

# 將字符串轉換成數字
num = int("11")
print(type(num), num)

num2 = float("11.345")
print(type(num2), num2)

# 錯誤示例，想要將字符串轉換成數字，必須要求字符串的內容都是數字
# num3 = int("Hello")
# print(type(num3), num3)

# 整數轉浮點數
float_num = float(11)
print(type(float_num), float_num)

# 浮點數轉整數(會丟失精度，丟失小數部分，只留下整數的部分)
int_num = int(11.345)
print(type(int_num), int_num)