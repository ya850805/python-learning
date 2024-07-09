"""
數據計算_sortBy方法
"""

from pyspark import SparkConf, SparkContext

# 構建執行環境入口對象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 讀取數據文件
rdd = sc.textFile("hello.txt")

# 取出全部單詞
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# 將所有單詞都轉成二元元組，單詞為key，value設置為1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))

# 分組並求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)

# 對結果進行排序
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(final_rdd.collect())