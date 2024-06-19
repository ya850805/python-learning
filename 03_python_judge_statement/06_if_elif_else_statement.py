"""
if elif else 多條件判斷語句使用
"""

# 通過if判斷，可以使用多條件判斷的語法
# 第一個條件就是if
if int(input("請輸入你的身高(cm)：")) < 120:
    print("身高小於120cm，可以免費")
elif int(input("請輸入你的VIP等級(1-5)：")) > 3:
    print("vip級別大於3，可以免費")
elif int(input("請告訴我今天幾號：")) == 1:
    print("今天是1號免費日，可以免費")
else:
    print("不好意思，條件都不滿足，需要買票10元")
