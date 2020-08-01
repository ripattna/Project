from pyspark.sql import SparkSession
from os.path import abspath

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

# Creating SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("demo", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("show databases").show()
spark.sql("create database demo")
spark.sql("show databases").show()