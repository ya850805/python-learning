"""
函數的說明文檔
"""


# 定義函數，進行文檔案說明
def add(x, y):
    """
    add函數可以接收2個參數，進行2數相加的功能
    :param x: 形餐x表示相加的其中一個數字
    :param y: 形餐y表示相加的另一個數字
    :return: 返回值是2數相加的結果
    """
    result = x + y
    print(f"2數相加的結果是：{result}")
    return result


add(5, 6)