"""
練習題：學生信息輸入
"""


class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(1, 4):
    print(f"當前輸入第{i}位學生信息，總共需要輸入3位學生信息")
    name = input("請輸入學生姓名：")
    age = input("請輸入學生年齡：")
    address = input("請輸入學生地址：")
    stu = Student(name, age, address)
    print(f"學生{i}信息輸入完成，信息為：姓名：{stu.name}，年齡：{stu.age}，地址：{stu.address}")