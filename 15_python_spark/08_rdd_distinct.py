"""
數據計算_distinct方法
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 1, 3, 3, 5, 5, 7, 8, 8, 9, 10])

# 對RDD的數據進行去重
rdd2 = rdd.distinct()

print(rdd2.collect())