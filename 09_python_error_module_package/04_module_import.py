"""
模塊的導入
"""
import time
# 使用import導入time模塊使用sleep功能(函數)
# import time  # 導入python內置的time模塊(time.py這個代碼文件)
#
# print("你好")
# time.sleep(5)  # 通過. 就可以使用模塊內部的全部功能(類、函數、變量)
# print("我好")


# 使用from導入time的sleep功能(函數)
# from time import sleep
#
# print("你好")
# sleep(5)
# print("我好")


# 使用*導入time模塊的全部功能
# from time import *  # *表示全部的意思
# print("你好")
# sleep(5)
# print("我好")


# 使用as給特定功能加上別名
# import time as t
# print("你好")
# t.sleep(3)
# print("我好")

from time import sleep as sl
print("你好")
sl(3)
print("我好")