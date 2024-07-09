"""
RDD輸出為Python對象
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子，輸出RDD為list對象
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，對RDD進行兩兩相加
num = rdd.reduce(lambda a, b: a + b)
print(num)

# take算子，取出RDD前N個元素，組成list返回
take_list = rdd.take(3)
print(take_list)

# count算子，統計RDD內有多少條數據，返回值為數字
num_count = rdd.count()
print(f"rdd內有{num_count}個元素")