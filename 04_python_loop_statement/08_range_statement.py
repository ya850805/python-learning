"""
range語句
"""

# range語法1 range(num)
for x in range(10):
    print(x)

print("############")

# range語法2 range(num1, num2)
for x in range(5, 10):
    # 從5開始，到10結束(不包含10本身)的一個數字序列，數字之間的間隔是1
    print(x)

print("############")

# range語法3 range(num1, num2, step)
for x in range(5, 10, 2):
    # 從5開始，到10結束(不包含10本身)的一個數字序列，數字之間的間隔是2
    print(x)