"""
布林類型和比較運算符

演示布林類型的定義以及比較運算符的應用
"""

# 定義變量存儲布林類型的數據
bool_1 = True
bool_2 = False
print(f"bool_1變量的內容是：{bool_1}，類型是：{type(bool_1)}")
print(f"bool_2變量的內容是：{bool_2}，類型是：{type(bool_2)}")

# 比較運算符的使用
# ==, !=, >, <, >=, <=

# 進行內容的相等比較
num1 = 10
num2 = 10
print(f"10 == 10的結果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的結果是：{num1 != num2}")

name1 = "abc"
name2 = "ABC"
print(f"abc == ABC的結果是：{name1 == name2}")

# 大於小於，大於等於 小於等於的比較運算
num1 = 10
num2 = 5
print(f"10 > 5的結果是：{num1 > num2}")
print(f"10 < 5的結果是：{num1 < num2}")

num1 = 10
num2 = 11
print(f"10 >= 11的結果是：{num1 >= num2}")
print(f"10 <= 11的結果是：{num1 <= num2}")