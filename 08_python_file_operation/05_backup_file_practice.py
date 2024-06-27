"""
練習題：備份文件
"""

# 打開文件得到文件對象，準備讀取
fr = open("bill.txt", "r", encoding="UTF-8")
# 打開文件得到文件對象，準備寫入
fw = open("bill.txt.bak", "a", encoding="UTF-8")

# for循環讀取文件
for line in fr:
    words = line.strip("\n").split(",")
    # 判斷內容，將正式的內容寫出
    if words[len(words) - 1] != "测试":
        fw.write(line)

fr.close()
fw.close()  # 寫出文件調用close會自動flush