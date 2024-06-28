"""
異常的傳遞性
"""


# 定義一個出現異常的方法
def func1():
    print("func1開始執行")
    1 / 0  # 肯定有異常，除以0的異常
    print("func1結束執行")


# 定義一個無異常的方法，調用上面有異常的方法
def func2():
    print("func2開始執行")
    func1()
    print("func2結束執行")


# 調用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出現異常了，異常的信息是：{e}")


main()