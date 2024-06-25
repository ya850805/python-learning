"""
數據容器的通用功能
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素個數
print(f"列表 元素個數有：{len(my_list)}")
print(f"元組 元素個數有：{len(my_tuple)}")
print(f"字符串元素個數有：{len(my_str)}")
print(f"集合 元素個數有：{len(my_set)}")
print(f"字典 元素個數有：{len(my_dict)}")

# max最大值
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元組 最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是：{max(my_dict)}")

# min最小值
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元組 最小的元素是：{min(my_tuple)}")
print(f"字符串最小的元素是：{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是：{min(my_dict)}")

# 類型轉換：容器轉列表
print(f"列表轉列表的結果是：{list(my_list)}")
print(f"元組轉列表的結果是：{list(my_tuple)}")
print(f"字符串轉列表的結果是：{list(my_str)}")
print(f"集合轉列表的結果是：{list(my_set)}")
print(f"字典轉列表的結果是：{list(my_dict)}")

# 類型轉換：容器轉元組
print(f"列表轉元組的結果是：{tuple(my_list)}")
print(f"元組轉元組的結果是：{tuple(my_tuple)}")
print(f"字符串轉元組的結果是：{tuple(my_str)}")
print(f"集合轉元組的結果是：{tuple(my_set)}")
print(f"字典轉元組的結果是：{tuple(my_dict)}")

# 類型轉換：容器轉字符串
print(f"列表轉字符串的結果是：{str(my_list)}")  # "[1, 2, 3, 4, 5]"
print(f"元組轉字符串的結果是：{str(my_tuple)}")  # (1, 2, 3, 4, 5)
print(f"字符串轉字符串的結果是：{str(my_str)}")
print(f"集合轉字符串的結果是：{str(my_set)}")  # {1, 2, 3, 4, 5}
print(f"字典轉字符串的結果是：{str(my_dict)}")  # {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}

# 類型轉換：容器轉集合
print(f"列表轉集合的結果是：{set(my_list)}")
print(f"元組轉集合的結果是：{set(my_tuple)}")
print(f"字符串轉集合的結果是：{set(my_str)}")
print(f"集合轉集合的結果是：{set(my_set)}")
print(f"字典轉集合的結果是：{set(my_dict)}")

# sorted排序，排序完都會變成列表對象
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}
print(f"列表對象的排序結果：{sorted(my_list)}")
print(f"元組對象的排序結果：{sorted(my_tuple)}")
print(f"字符串對象的排序結果：{sorted(my_str)}")
print(f"集合對象的排序結果：{sorted(my_set)}")
print(f"字典對象的排序結果：{sorted(my_dict)}")

print(f"列表對象的反向排序結果：{sorted(my_list, reverse=True)}")
print(f"元組對象的反向排序結果：{sorted(my_tuple, reverse=True)}")
print(f"字符串對象的反向排序結果：{sorted(my_str, reverse=True)}")
print(f"集合對象的反向排序結果：{sorted(my_set, reverse=True)}")
print(f"字典對象的反向排序結果：{sorted(my_dict, reverse=True)}")