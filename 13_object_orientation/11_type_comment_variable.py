"""
變量的類型註解
"""
import json
import random

# 基礎數據類型註解
var_1: int = 10
var_2: str = "hello"
var_3: bool = True


# 類對象類型註解
class Student:
    pass


stu: Student = Student()

# 基礎容器類型註解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"age": 15}

# 容器類型詳細註解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "Hello", True)
my_dict: dict[str, int] = {"age": 15}

# 在注釋中進行類型註解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "John"}')  # type: dict[str, str]


def func():
    return 10


var_3 = func()  # type: int


# 類型註解的限制，類型註解只是個備註(只是提示性的)，給IDE看的，運行起來不會報錯
var_4: int = "你好"
var_5: str = 123