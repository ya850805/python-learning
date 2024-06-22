"""
list列表的方法(在一個class中定義的叫做方法，不在class中定義的叫函數)
"""

my_list = ["itcast", "itheima", "python"]

# 1.1 查找某個元素在列表內的下標索引
index = my_list.index("itheima")
print(f"itheima在列表中的下標索引值是：{index}")

# 1.2 如果被查找的元素不存在，會抱錯  ValueError: 'hello' is not in list
# index = my_list.index("hello")
# print(f"hello在列表中的下標索引值是：{index}")

# 2. 修改特定下標索引的值
my_list[0] = "Tom"
print(f"列表被修改元素值後，結果是：{my_list}")

# 3. 在指定下標位置插入新元素
my_list.insert(1, "best")
print(f"列標插入元素後，結果是：{my_list}")

# 4. 在列表的尾部追加"單個"新元素
my_list.append("Nice")
print(f"列表追加了元素後，結果是：{my_list}")

# 5. 在列表的尾部追加"一批"新元素
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"列表追加了一個新的列表後，結果是：{my_list}")

# 6. 刪除指定下標索引的元素(2種方式)
my_list = ["itcast", "itheima", "python"]

# 6.1 方式一：del 列表[下標]
del my_list[2]
print(f"列表刪除元素後，結果是：{my_list}")

# 6.2 方式二：列表.pop(下標)
my_list = ["itcast", "itheima", "python"]
element = my_list.pop(2)
print(f"通過pop()方法取出元素後，列表內容：{my_list}，取出的元素是：{element}")

# 7.刪除某個元素在列表中的第一個匹配項
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
my_list.remove("itheima")
print(f"通過remove()方法移除元素後，列表的結果是：{my_list}")

# 8. 清空列表
my_list.clear()
print(f"列表被清空了，結果是：{my_list}")

# 9. 統計列表內某元素的數量
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
count = my_list.count("itheima")
print(f"列表中itheima的數量是：{count}")

# 10. 統計列表中全部元素的數量(函數)
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
count = len(my_list)
print(f"列表的元素數量總共有：{count}個")