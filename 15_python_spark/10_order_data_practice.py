"""
練習題
"""
import json
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 讀取文件得到RDD
file_rdd = sc.textFile("orders.txt")

# 取出一個個JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))

# 將一個個JSON字符串轉成Python字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))

# 取出城市和銷售額數據 (城市, 銷售額)
city_with_money_rdd = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))

# 按城市分組按銷售聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b)

# 案銷售額進行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1的結果：", result1_rdd.collect())

# 取出全部的商品類別
category_rdd = dict_rdd.map(lambda x: x["category"]).distinct()
print("需求2的結果：", category_rdd.collect())

# 過濾北京市的數據
beijing_data_rdd = dict_rdd.filter(lambda x: x["areaName"] == "北京")

# 取出全部商品類別
result3_rdd = beijing_data_rdd.map(lambda x: x["category"]).distinct()
print("需求3的結果：", result3_rdd.collect())