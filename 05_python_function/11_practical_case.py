"""
ATM綜合練習
"""


# 定義變量
money = 5000000
name = input("請輸入您的姓名：")


# 查詢函數
def query(show_header):
    if show_header:
        print("----------查詢餘額----------")
    print(f"{name}，您好，您的餘額剩餘：{money}元")


# 存款函數
def deposit(num):
    print("----------存款----------")
    global money  # money在函數內部定義為全局變量
    money += num
    print(f"{name}，您好，您存款{num}元成功")
    query(False)  # 調用query函數查詢餘額


def withdraw(num):
    print("----------取款----------")
    global money
    money -= num
    print(f"{name}，您好，您取款{num}元成功")
    query(False)  # 調用query函數查詢餘額


def menu():
    print("----------主菜單----------")
    print(f"{name}，您好，歡迎使用ATM")
    print("查詢餘額\t[輸入1]")
    print("存款\t[輸入2]")
    print("取款\t[輸入3]")
    print("退出\t[輸入4]")
    return int(input("請輸入您的選擇："))


while True:
    option = menu()
    if option == 1:
        query(True)
    elif option == 2:
        deposit_money = int(input("請輸入您要存入多少錢："))
        deposit(deposit_money)
    elif option == 3:
        withdraw_money = int(input("請輸入您要取出多少錢："))
        withdraw(withdraw_money)
    elif option == 4:
        print("退出...")
        break
    else:
        print("錯誤的指令...")
