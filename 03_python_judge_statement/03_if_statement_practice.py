"""
練習題：成年人判斷
"""

print("歡迎來到遊樂場，兒童免費，成人收費。")
# 獲取鍵盤輸入
age = int(input("請輸入你的年齡："))

# 通過if判斷是否是成年人
if age >= 18:
    print("您已成年，遊玩需要買票10元")

print("祝您遊玩愉快")