"""
文件的追加寫入
"""

# 打開文件，不存在的文件
f = open("append.txt", "a", encoding="UTF-8")

# write寫入
f.write("Hello")

# flush刷新
f.flush()

# close關閉
f.close()

# 打開一個存在的文件
f = open("append.txt", "a", encoding="UTF-8")
f.write("\n你好")

# close關閉
f.close()