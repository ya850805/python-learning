"""
Python的包
"""

# 創建一個my_package包
# 導入自定義的包中模塊，並使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1, my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()


# 通過__all__變量，控制import *
from my_package import *
my_module1.info_print1()
# my_module2.info_print2()  # __all__指定只可以使用my_module1