"""
異常、模塊、包的綜合案例

搭配my_utils包下的模塊
"""

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("ABCDE"))
print(my_utils.str_util.substr("ABCDE", 1, 4))

file_util.print_file_info("2.txt")
file_util.append_to_file("2.txt", "你好！")