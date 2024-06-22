"""
練習題：元組的基本操作
"""

# 紀錄一個學生的姓名、年齡、愛好
t1 = ("周杰倫", 11, ["football", "music"])

# 查詢年齡所在的下標位置
index = t1.index(11)
print(f"年齡的下標是：{index}")

# 查詢學生的姓名
print(f"學生的姓名是：{t1[0]}")

# 刪除學生愛好中的football
del t1[2][0]
print(f"刪除football愛好後，元組為：{t1}")

# 增加愛好coding
t1[2].append("coding")
print(f"增加愛好coding後，元組為：{t1}")