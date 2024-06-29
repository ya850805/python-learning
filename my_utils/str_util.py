"""
字符串處理相關工具模塊
"""


def str_reverse(s):
    """
    將字符串完成反轉
    :param s: 將被反轉的字符串
    :return:  反轉後的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照給定的下標完成給定字符串的切片
    :param s: 即將被切片的字符串
    :param x: 切片的開始下標
    :param y: 切片的結束下標
    :return: 切片完成後的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("Hello"))
    print(substr("Hello", 1, 3))