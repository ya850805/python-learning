"""
取出列表內的偶數：使用while和for
"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while寫法
while_list = []
index = 0
while index < len(list):
    if list[index] % 2 == 0:
        while_list.append(list[index])
    index += 1

print(f"通過while循環，從列表{list}中取出偶數，組成新列表：{while_list}")

# for寫法
for_list = []
for num in list:
    if num % 2 == 0:
        for_list.append(num)

print(f"通過for循環，從列表{list}中取出偶數，組成新列表：{for_list}")