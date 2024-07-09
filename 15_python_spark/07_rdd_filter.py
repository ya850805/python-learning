"""
數據計算_filter方法
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 對RDD的數據進行過濾
rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())