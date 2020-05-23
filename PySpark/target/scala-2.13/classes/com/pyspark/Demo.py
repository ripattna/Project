from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
from os.path import abspath
# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')
sparkSessionObj = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .enableHiveSupport() \
    .getOrCreate()
sparkSessionObj.sql("show databases").show()
#sparkSessionObj.sql("drop table if exists src")
# spark is an existing SparkSession
#sparkSessionObj.sql("""create database hive_test""")
#sparkSessionObj.sql("show databases").show()
#sparkSessionObj.sql("use hive_test")
#sparkSessionObj .sql("CREATE TABLE src(key INT, value STRING) USING hive")
sparkSessionObj .sql("show tables").show()
#spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

