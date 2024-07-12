"""
正則表達式使用元字符匹配
"""
import re

s = "itheima1 @@ python2 !!666 ##itccast3"

result = re.findall(r'[a-zA-Z]', s)  # 字符串前面帶上r的標記，表示字符串中轉譯字符無效，就是普通字符的意思
print(result)

# 匹配帳號，只能由字母和數字組成，長度限制6-10位
r = '^[0-9a-zA-Z]{6,10}$'
s = '1234567ACC'
print(re.findall(r, s))

# 匹配QQ號，要求純數字，長度5-11，第一位不為0
r = '^[1-9][0-9]{4,10}$'
s = '012345678'
print(re.findall(r, s))

# 匹配郵箱地址，只允許qq, 163, gmail這三種郵箱地址
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.d.e.f.g@qq.com.a.z.c.d.e'
print(re.match(r, s))