"""
成員方法
"""


# 定義一個帶有成員方法的類
class Student:
    name: None  # 學生姓名

    def say_hi(self):
        print(f"大家好，我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}，{msg}")


stu = Student()
stu.name = "小明"
stu.say_hi()
stu.say_hi2("請大家多多指教！")

stu2 = Student()
stu2.name = "小華"
stu2.say_hi()
stu2.say_hi2("Hello~~~")