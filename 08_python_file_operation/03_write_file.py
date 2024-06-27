"""
文件的寫入
"""
import time

# 打開文件，可以指定不存在的文件，會自動創建
f = open("write.txt", "w", encoding="UTF-8")

# write寫入
f.write("Hello World!")  # 將內容寫入到內存

# flush刷新
f.flush()  # 將內存中累積的內容，寫入到硬盤中

# 關閉
f.close()  # 內置了flush的功能，會將內存的內容寫入硬盤

# 打開一個存在的文件
f = open("write.txt", "w", encoding="UTF-8")

# write寫入，因為是w模式，所以原有的內容會被刪除然後重新寫入新的內容
f.write("你好")

# close關閉
f.close()