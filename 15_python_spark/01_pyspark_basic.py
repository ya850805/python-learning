"""
獲取PySpark的執行環境入庫對象：SparkContext
並通過SparkContext對象獲取當前PySpark的版本
"""

# 導包
from pyspark import SparkConf, SparkContext

# 創建SparkConf對象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基於SparkConf類對象創建SparkContext對象
sc = SparkContext(conf=conf)

# 打印PySpark的運行版本
print(sc.version)

# 停止SparkContext對象的運行(停止PySpark程序)
sc.stop()