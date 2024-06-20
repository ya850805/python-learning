"""
變量作用域
"""

for i in range(5):
    print(i)

# 實際上在程序可以獲取到i，不過規範上不允許這麼做
print(i)

########################

# 可以改成以下寫法
j = 0
for j in range(5):
    print(j)

print(j)