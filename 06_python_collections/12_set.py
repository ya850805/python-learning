"""
set集合

無序不重複
"""

# 定義集合
my_set = {"name1", "name2", "name3", "name1", "name2", "name3"}
my_set_empty = set()  # 空set
print(f"my_set的內容是：{my_set}，類型是：{type(my_set)}")
print(f"my_set_empty的內容是：{my_set_empty}，類型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("name4")
my_set.add("name1")
print(f"my_set添加元素後結果是：{my_set}")

# 移除元素
my_set.remove("name2")
print(f"my_set移除name2元素後結果是：{my_set}")

# 隨機取出一個元素
my_set = {"name1", "name2", "name3"}
element = my_set.pop()
print(f"集合中取出的元素是：{element}，取出元素後集合是：{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空了，結果是：{my_set}")

# 取2個集合的差集(集合1有而集合2沒有的)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集後的結果是：{set3}")
print(f"取出差集後，原有set1的內容：{set1}")
print(f"取出差集後，原有set2的內容：{set2}")

# 消除2個集合的差集(在集合1內，刪除和集合2相同的元素)
set1.difference_update(set2)
print(f"消除差集後，set1結果：{set1}")
print(f"消除差集後，set2結果：{set2}")

# 2個集合合併為1個
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"2集合合併結果：{set3}")
print(f"合併後set1：{set1}")
print(f"合併後set2：{set2}")

# 統計集合元素數量
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num = len(set1)
print(f"集合內的元素數量有：{num}個")

# 集合的遍歷(集合不支持下標索引，不能用while，但是可以用for)
set1 = {1, 2, 3, 4, 5}
for i in set1:
    print(f"集合的元素有：{i}")