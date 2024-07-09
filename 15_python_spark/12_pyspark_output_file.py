"""
RDD輸出到文件中
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism", 1)  # 全局設置分區
sc = SparkContext(conf=conf)

# RDD1
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)

# RDD2
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)], 1)

# RDD3
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]], 1)

# 輸出到文件中
rdd1.saveAsTextFile("output1")
rdd2.saveAsTextFile("output2")
rdd3.saveAsTextFile("output3")