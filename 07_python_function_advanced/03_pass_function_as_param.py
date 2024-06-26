"""
函數作為參數傳遞
"""


# 定義一個函數，接收另一個函數作為傳入參數
def test_func(function):
    result = function(1, 2)  # 確定compute是函數
    print(f"function參數的類型是：{type(function)}")
    print(f"計算結果：{result}")


# 定義一個函數，準備作為參數傳入另一個函數
def compute(x, y):
    return x + y


# 調用，並傳入參數
test_func(compute)