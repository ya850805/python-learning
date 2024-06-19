"""
練習題：我要買票嗎
"""

print("歡迎來到動物園")
# 定義鍵盤輸入獲取身高數據
height = int(input("請輸入你的身高(cm)："))

# 通過if進行判斷
if height > 120:
    print("您的身高超出120cm，遊玩需要購票10元")
else:
    print("您的身高未超出120cm，可以免費遊玩")

print("祝您遊玩愉快")