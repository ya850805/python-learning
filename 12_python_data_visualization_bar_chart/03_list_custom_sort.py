"""
擴展列表的sort方法(自定義排序)
"""

# 準備列表
my_list = [["a", 33], ["b", 55], ["c", 11]]


# 排序，基於帶名函數
def choose_sort_key(element):
    return element[1]  # 按照下標1的元素進行排序


my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)


# 排序，基於lambda匿名函數
my_list.sort(key=lambda element: element[1], reverse=False)
print(my_list)