"""
input語句
"""

name = input("請告訴我你是誰？")
print("我知道了，你是%s" % name)

# 輸入數字類型(得到的永遠都是字符串類型)
age = input("請告訴我你的年齡：")
# 數據類型轉換
age = int(age)
print("你的年齡的類型是：%s" % type(age))