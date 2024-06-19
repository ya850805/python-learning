import random

# 1. 構建一個隨機的數字變量
num = random.randint(1, 10)

guess_num = int(input("輸入你要猜的數字："))

if guess_num == num:
    print("恭喜，第一次就猜中")
else:
    if guess_num > num:
        print("你猜的數字太大了")
    else:
        print("你猜的數字太小了")
    guess_num = int(input("再次輸入你要猜的數字："))
    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜的數字太大了")
        else:
            print("你猜的數字太小了")
        guess_num = int(input("第三次輸入你要猜的數字："))
        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            print(f"三次機會用完了，沒有猜中，num = {num}")