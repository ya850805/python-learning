"""
練習題：for循環打印九九乘法表
"""

# 外層循環控制行數
for i in range(1, 10):
    # 內層循環控制每一行的輸出
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}", end='\t')
    print()