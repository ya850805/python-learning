"""
for循環的嵌套使用
"""

i = 1
for i in range(1, 101):
    print(f"今天是第{i}天")

    # 內層循環
    for j in range(1, 11):
        print(f"送出第{j}朵玫瑰花")

    print("表白～")

print(f"第{i}天表白成功")