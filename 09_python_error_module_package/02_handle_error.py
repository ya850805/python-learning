"""
捕獲異常
"""

# 基本捕獲異常語法
try:
    open("1.txt", "r", encoding="UTF-8")
except:
    print("出現異常了，因為文件不存在，我將open的模式改為w去打開")
    f = open("1.txt", "w", encoding="UTF-8")


# 捕獲指定的異常
try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出現了變量未定義的異常")
    print(e)

# 捕獲多個異常
try:
    # 1 / 0
    print(age)
except (NameError, ZeroDivisionError) as e:
    print("出現了變量未定義或者除以0的異常錯誤")

# 捕獲所有異常
try:
    # 1 / 0
    # print(name)
    # print("Hello")
    f = open("123.txt", "r", encoding="UTF-8")
except Exception as e:
    print(f"出現了異常：{e}")
    f = open("1.txt", "r", encoding="UTF-8")
else:
    print("沒有出現異常！")
finally:
    print("我是finally，有沒有異常我都要執行")
    f.close()