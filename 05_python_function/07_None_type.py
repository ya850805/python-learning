"""
None類型
"""


def say_hi():
    print("你好！")


result = say_hi()
print(f"無返回值函數，返回的內容是：{result}")  # None
print(f"無返回值函數，返回的內容類型是：{type(result)}")  # <class 'NoneType'>


print("######################################")


# 主動返回None的函數
def say_hi2():
    print("你好！")
    return None


result = say_hi2()
print(f"無返回值函數，返回的內容是：{result}")
print(f"無返回值函數，返回的內容類型是：{type(result)}")


print("######################################")


# None用於if判斷，None等同於False
def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None


result = check_age(16)
if not result:
    # 進入if表示result是None值，也就是False
    print("您還未成年")


print("######################################")


# None用於聲明無初始內容的變量
name = None
print(name)
