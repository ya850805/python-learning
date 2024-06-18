"""
字符串格式化
"""

# 通過占位的形式，完成拼接
name = "Jason"
message = "My name is %s" % name
print(message)

# 通過占位的形式，完成數字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "class_num = %s, avg_salary = %s" % (class_num, avg_salary)
print(message)

name = "company1"
setup_year = 2006
stock_price = 19.99
message = "name = %s, setup_year = %d, stock_price = %f" % (name, setup_year, stock_price)
print(message)