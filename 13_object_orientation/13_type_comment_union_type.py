"""
Union聯合類型註解
"""

# 使用Union類型，必須先導包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "Hello", "World"]


# 可以傳入int或str，返回值可能是int或str
def func(data: Union[int, str]) -> Union[int, str]:
    pass


func("Hello")