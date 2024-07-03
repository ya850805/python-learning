"""
類
"""


# 設計一個類
class Student:
    name = None  # 紀錄學生姓名
    gender = None  # 紀錄學生性別
    nationality = None  # 紀錄學生國籍
    native_place = None  # 紀錄學生籍貫
    age = None  # 紀錄學生年齡


# 創建一個對象
stu_1 = Student()

# 對象屬性賦值
stu_1.name = "小明"
stu_1.gender = "男"
stu_1.nationality = "中國"
stu_1.native_place = "山東省"
stu_1.age = 31

# 獲取對象信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)