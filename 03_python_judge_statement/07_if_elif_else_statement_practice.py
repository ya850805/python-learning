"""
練習題：猜猜心裡數字
"""

num = 5

if int(input("請輸入第一次猜想的數字：")) == num:
    print("恭喜第一次就猜對了呢")
elif int(input("猜錯了，再猜一次：")) == num:
    print("恭喜第二次猜對了")
elif int(input("猜錯了，再猜最後一次：")) == num:
    print("恭喜，最後一次機會，你猜對了")
else:
    print(f"Sorry，全部猜錯啦，我想的是：{num}")