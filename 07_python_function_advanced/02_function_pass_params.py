"""
函數參數的多種使用形式
"""


def user_info(name, age, gender):
    print(f"姓名：{name}，年齡：{age}，性別：{gender}")


# 位置參數 - 默認使用形式
user_info("小明", 20, "男")

# 關鍵字參數
user_info(name="小王", age=11, gender="女")
user_info(age=10, gender="女", name="小田")  # 可以不按照參數的定義順序傳參
user_info("小美", gender="女", age=9)


# 缺省參數(默認值)，默認參數必須在最後一個
def user_info(name, age, gender="男"):
    print(f"姓名：{name}，年齡：{age}，性別：{gender}")


user_info("小天", 13)
user_info("小天", 13, "女")


# 不定長 - 位置不定長 *號
# 不定長定義的形式參數會作為元組存在，接收不定長數量的參數傳入
def user_info(*args):
    print(f"args參數的類型是：{type(args)}，內容是：{args}")


user_info(1, 2, "小明", 3, "男")


# 不定長 - 關鍵字不定長 **號
def user_info(**kwargs):
    print(f"kwargs參數的類型是：{type(kwargs)}，內容是：{kwargs}")


user_info(name="小王", age=11, gender="男", addr="台北")