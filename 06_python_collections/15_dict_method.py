"""
字典的常用操作
"""

my_dict = {"person1": 99, "person2": 88, "person3": 77}

# 新增元素
my_dict["person4"] = 66
print(f"字典經過新增元素後，結果：{my_dict}")

# 更新元素
my_dict["person1"] = 33
print(f"字典經過更新後，結果：{my_dict}")

# 刪除元素
score = my_dict.pop("person1")
print(f"字典中被移除一個元素後，結果：{my_dict}，person1的考試分數是：{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，內容是：{my_dict}")

# 獲取全部的key
my_dict = {"person1": 99, "person2": 88, "person3": 77}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")

# 遍歷字典
# 方式1：通過獲取到全部的key來完成遍歷
for key in keys:
    print(f"字典的key是：{key}，對應的value是：{my_dict[key]}")

# 方式2：直接對字典進行for循環，每一次循環都是直接得到key
for key in my_dict:
    print(f"***字典的key是：{key}，對應的value是：{my_dict[key]}")

# 統計字典內的元素數量
num = len(my_dict)
print(f"字典中的元素數量有：{num}個")