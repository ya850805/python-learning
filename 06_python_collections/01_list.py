"""
list列表
"""

# 定義一個列表list
my_list = ["Jason", "Tom", "Python"]
print(my_list)
print(type(my_list))

my_list = ["Jason", 666, True]
print(my_list)
print(type(my_list))

# 定義一個嵌套的列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))

# 通過下標索引取出對應位置的數據
# 列表[下標索引]，從前向後0開始，每次+1，從後向前從-1開始，每次-1
my_list = ["Tom", "Lily", "Rose"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3])  # 錯誤示範，通過下標索引取數據，一定不要超出範圍

# 通過下標索引取出數據(倒序取出)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])