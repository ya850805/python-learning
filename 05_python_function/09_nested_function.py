"""
函數的嵌套調用
"""


def func_b():
    print("---2---")


def func_a():
    print("---1---")
    func_b()  # 嵌套調用func_b
    print("---3---")


func_a()