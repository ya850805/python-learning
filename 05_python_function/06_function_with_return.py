"""
函數的返回值定義語法
"""


# 定義一個函數，完成2數相加功能
def add(a, b):
    result = a + b
    # 通過返回值，將相加的結果返回給調用者
    return result
    # 返回結果後，還想輸出一句話
    # print("Done") # 這行代碼不會執行，因為前面已經return了


# 調用函數
r = add(5, 6)
print(r)