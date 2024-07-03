"""
構造方法
"""


# 使用構造方法對成員變量進行賦值 __init__
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student類創建了一個類對象")


stu = Student("小明", 31, "0912345678")
print(stu.name)
print(stu.age)
print(stu.tel)