"""
練習題：while循環打印九九乘法表
"""

# 定義外層循環的控制變量
i = 1
while i <= 9:
    # 定義內層循環的控制變量
    j = 1
    while j <= i:
        # 內層循環的print語句，不要換行，通過\t制表符進行對其
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    print()  # print空內容，就是輸出一個換行
    i += 1