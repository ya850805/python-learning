"""
魔術方法(內置方法)
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔術方法
    def __str__(self):
        return f"Student類對象，name：{self.name}：，age：{self.age}"

    # __lt__魔術方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔術方法
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("小明", 31)
stu2 = Student("小華", 36)
stu3 = Student("小李", 31)
print(stu1)
print(str(stu1))

print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 >= stu3)

print(stu1 == stu3)
print(stu1 == stu2)

