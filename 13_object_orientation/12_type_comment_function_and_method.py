"""
函數(方法)的類型註解
"""


# 對形參進行類型註解
def add(x: int, y: int):
    return x + y


# 對返回值進行類型註解
def func(data: list) -> list:
    return data


# 類型註解只是提示性的，非決定性的，所以以下代碼運行不會報錯
print(func(1))