"""
練習題：信息去重
"""

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

my_set = set()
for element in my_list:
    my_set.add(element)

print(f"列表的內容是：{my_list}")
print(f"存入集合結果：{my_set}")