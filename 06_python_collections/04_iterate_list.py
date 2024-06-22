"""
list列表的循環
"""


def list_while_func():
    """
    使用while循環遍歷列表的函數
    :return: None
    """
    my_list = ["name1", "name2", "name3"]
    # 循環控制變量通過下標索引來控制，默認0
    # 每次循環將下標索引變量+1
    # 循環條件：下標索引 < 列表元素的數量

    # 定義一個變量來標記列表下標
    index = 0  # 初始值為0
    while index < len(my_list):
        # 通過index變量取出對應下標的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        # 將循環變量(index)每一次循環都+1
        index += 1


def list_for_func():
    """
    使用for循環遍歷列表的函數
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有：{element}")


list_while_func()
list_for_func()