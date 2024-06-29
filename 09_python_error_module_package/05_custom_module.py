"""
使用自定義模塊
"""

# 導入自定義模塊使用
# import my_module1
# my_module1.test(1, 2)

# from my_module1 import test
# test(1, 2)


# 導入不同模塊的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)


# __main__變量
from my_module1 import test


# __all__變量
from my_module1 import *
test(1, 2)
# test1(1, 2)  # import * 只會導入__all__變量中的內容