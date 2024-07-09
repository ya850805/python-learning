"""
數據計算_flatmap方法
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 準備一個RDD
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求：將RDD數據裡面的一個個單詞提取出來
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())