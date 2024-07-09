"""
練習題：搜索引擎日誌分析
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", 1)
sc = SparkContext(conf=conf)

# 讀取文件轉換成RDD
file_rdd = sc.textFile("search_log.txt")

# TODO 需求1：熱門搜索時間段Top3(小時精度)
# 1.1 取出全部的時間並轉換為小時
# 1.2 轉換為(小時, 1)的二元元組
# 1.3 key分組聚合value
# 1.4 排序(降序)
# 1.5 取前3
result1 = file_rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print("需求1的結果：", result1)

# TODO 需求2：熱門搜索詞Top3
# 2.1 取出全部的搜索詞
# 2.2 (詞, 1)二元元組
# 2.3 分組聚合
# 2.4 排序
# 2.5 Top3
result2 = file_rdd.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print("需求2的結果：", result2)

# TODO 需求3：統計黑马程序员關鍵字在什麼時段被搜索的最多
# 3.1 過濾內容，只保留黑马程序员關鍵字
# 3.2 轉換為(小時, 1)的二元元組
# 3.3 key分組聚合value
# 3.4 排序(降序)
# 3.5 取前1
result3 = file_rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2] == "黑马程序员").\
    map(lambda x: (x[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)
print("需求3的結果：", result3)

# TODO 需求4：將數據轉換為JSON，寫出到文件中
# 4.1 轉換為JSON格式的RDD
# 4.2 寫出為文件
file_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]}).\
    saveAsTextFile("output_json")