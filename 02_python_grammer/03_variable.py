"""
變量

演示Python中變量的相關操作
"""

# 定義一個變量，用來紀錄錢包餘額
money = 50

# 通過print語句，輸出變量紀錄的內容
print("錢包還有：", money, "元")

# 買了一個冰淇淋，花費10元
money = money - 10
print("買了冰淇淋花費10元，錢包還剩餘：", money, "元")

# 假設，每隔一小時，輸出一下錢包餘額
print("現在是下午1點，錢包餘額剩餘：", money)
print("現在是下午2點，錢包餘額剩餘：", money)
print("現在是下午3點，錢包餘額剩餘：", money)
print("現在是下午4點，錢包餘額剩餘：", money)

#########################################################
balance = 50
print("當前錢包餘額：", balance, "元")

iceCream = 10
balance = balance - iceCream
print("買了冰淇淋花費", iceCream, "元")

cola = 5
balance = balance - cola
print("買了可樂花費", cola, "元")

print("最終，錢包剩餘：", balance)