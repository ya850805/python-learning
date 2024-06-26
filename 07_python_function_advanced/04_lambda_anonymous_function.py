"""
lambda匿名函數
"""


# 定義一個函數，接受其他函數輸入
def test_func(compute):
    result = compute(1, 2)
    print(f"結果是：{result}")


# 通過lambda匿名函數的形式，將匿名函數作為參數傳入
test_func(lambda x, y: x + y)