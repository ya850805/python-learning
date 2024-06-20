"""
練習題：猜數字
"""
import random

num = random.randint(1, 100)

# 通過一個bool類型的變量，做循環是否繼續的標記
flag = True
# 定義一個變量，紀錄總共猜測了多少次
times = 0

while flag:
    times += 1
    guess_num = int(input("猜一個數字："))
    if guess_num == num:
        print(f"猜對了，共用了{times}次")
        flag = False
    elif guess_num > num:
        print("猜的數字太大了，再試一次")
    else:
        print("猜的數字太小了，再試一次")