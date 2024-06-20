"""
練習題：有幾個偶數
"""

num = 100
count = 0

for i in range(1, num):
    if i % 2 == 0:
        count += 1

print(f"1到{num}(不包含{num}本身)範圍內，有{count}個偶數")