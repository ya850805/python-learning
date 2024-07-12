"""
正則表達式
"""

import re

s = "1python itheima python"

# match"從開頭"匹配
result = re.match("python", s)
print(result)
# print(result.span())
# print(result.group())

# search
result = re.search("python", s)
print(result)

# findall
result = re.findall("python", s)
print(result)