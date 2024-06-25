"""
練習題
"""
import random

# 1. 幸運數字6
num = int(input("請輸入數字："))
nums = list()
lucky = list()

for i in range(1, num + 1):
    nums.append(i)
    if i % 6 == 0:
        lucky.append(i)

print(f"nums = {nums}")
print(f"lucky = {lucky}")

# 2. 列表嵌套
classrooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for t in teachers:
    index = random.randint(0, len(classrooms) - 1)
    classrooms[index].append(t)

print(f"將8名教師隨機分配到3個教室的結果為：{classrooms}")
