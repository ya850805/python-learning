"""
函數的多返回值
"""


# 使用多個變量，接收多個返回值
def test_return():
    return 1, "Hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)