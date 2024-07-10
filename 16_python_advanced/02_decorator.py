"""
裝飾器
"""


# 裝飾器的一般寫法(閉包)
# def outer(func):
#     def inner():
#         print("我睡覺了")
#         func()
#         print("我起床了")
#
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()


# 裝飾器的快捷寫法(語法糖)
def outer(func):
    def inner():
        print("我睡覺了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1, 5))


sleep()