"""
變量的作用域
"""


# 局部變量
def test_a():
    num = 100
    print(num)


test_a()
# 出了函數體，局部變量就無法使用了
# print(num)


print("#################################")

# 全局變量
num = 200


def test_b():
    print(f"test_b: {num}")


def test_c():
    print(f"test_c: {num}")


test_b()
test_c()
print(num)

print("#################################")

num = 200


# 在函數內部修改全局變量
def test_d():
    print(f"test_d: {num}")


def test_e():
    # num = 500  # 這樣寫是定義一個局部變量

    global num  # 設置內部定義的變量為全局變量
    num = 500
    print(f"test_e: {num}")


test_d()
test_e()
print(num)