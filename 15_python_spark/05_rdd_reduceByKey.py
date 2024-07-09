"""
數據計算_reduceByKey方法
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])

# 求男生和女生兩個組的成績之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())