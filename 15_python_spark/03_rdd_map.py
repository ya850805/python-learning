"""
數據計算_map方法
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 準備一個RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])


# 通過map方法將全部數據乘以10
# def func(data):
#     return data * 10


# rdd2 = rdd.map(func)

# 鏈式調用
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())






