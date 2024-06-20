"""
循環中斷
"""

# 循環中斷語句continue
for i in range(1, 6):
    print("語句1")
    continue
    print("語句2")

print("#########################")

# continue的嵌套應用
for i in range(1, 6):
    print("語句1")
    for j in range(1, 6):
        print("語句2")
        continue
        print("語句3")
    print("語句4")

print("#########################")

# 循環中斷語句break
for i in range(1, 101):
    print("語句1")
    break
    print("語句2")
print("語句3")

print("#########################")

# break的嵌套應用
for i in range(1, 6):
    print("語句1")
    for j in range(1, 6):
        print("語句2")
        break
        print("語句3")
    print("語句4")