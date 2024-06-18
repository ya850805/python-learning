"""
數據類型
"""

# 方式1：使用print直接輸出類型信息
print(type("你好"))
print(type(666))
print(type(11.345))

# 方式2：使用變量存儲type()語句的結果
string_type = type("Hello")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

# 方式3：使用type()語句，查看變量中存儲的數據類型
name = "Hello!"
name_type = type(name)
print(name_type)