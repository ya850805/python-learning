"""
有參數函數練習
"""


def check(temp):
    print("歡迎來到遊樂園！")
    if temp <= 37.5:
        print(f"您的體溫是{temp}，正常！")
    else:
        print(f"您的體溫是{temp}，異常！")


# 調用函數
check(36)
check(39.5)