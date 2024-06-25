"""
dic 字典
"""

# 定義字典
my_dict1 = {"person1": 99, "person2": 88, "person3": 77}

# 定義空字典
my_dict2 = {}
my_dict3 = dict()

print(f"字典1的內容是：{my_dict1}，類型：{type(my_dict1)}")
print(f"字典2的內容是：{my_dict2}，類型：{type(my_dict2)}")
print(f"字典3的內容是：{my_dict3}，類型：{type(my_dict3)}")

# 定義重複key的字典
my_dict1 = {"person1": 99, "person1": 88, "person3": 77}
print(f"重複key的字典內容是：{my_dict1}")

# 從字典中基於key獲取value
my_dict1 = {"person1": 99, "person2": 88, "person3": 77}
score1 = my_dict1["person1"]
score2 = my_dict1["person2"]
score3 = my_dict1["person3"]
print(f"person1的考試分數是：{score1}")
print(f"person2的考試分數是：{score2}")
print(f"person3的考試分數是：{score3}")

# 定義嵌套字典
stu_score_dict = {
    "person1": {
        "chinese": 77,
        "math": 66,
        "english": 33
    },
    "person2": {
        "chinese": 88,
        "math": 86,
        "english": 55
    },
    "person3": {
        "chinese": 99,
        "math": 96,
        "english": 66
    }
}
print(f"學生的考試信息是：{stu_score_dict}")

# 從嵌套字典中獲取數據
score = stu_score_dict["person2"]["chinese"]
print(f"person2的chinese分數是：{score}")
score = stu_score_dict["person3"]["english"]
print(f"person3的english分數是：{score}")