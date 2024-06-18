"""
字符串多種定義方式
"""

# 單引號定義法
name = 'Hello'
print(type(name))

# 雙引號定義法
name = "World"
print(type(name))

# 三引號定義法，寫法和多行註釋是一樣的
name = """
Hello
World
!
"""
print(type(name))

# 在字符串中包含雙引號
name = '"Hello"'
print(name)
# 在字符串中包含單引號
name = "'World'"
print(name)
# 使用轉譯字符\解除引號的效用
name = "\"你好\""
print(name)
name = '\'Hi\''
print(name)