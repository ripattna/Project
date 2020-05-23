from logging import getLogger
from pyspark.sql import SparkSession
from os.path import abspath

if __name__ == "__main__":

    # warehouse_location points to the default location for managed databases and tables
    warehouse_location = abspath('spark-warehouse')

    # Creating SparkSession
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .config("demo", warehouse_location) \
        .enableHiveSupport() \
        .getOrCreate()

    # Setting the current database to demo
    spark.catalog.setCurrentDatabase("demo")

    table_list = spark.sql("""show tables in demo""")
    table_name = table_list.filter(table_list.tableName == "src").collect()

    if len(table_name) > 0:
        print("Table src is present in Demo database")
    else:
        print("Table not found")

    # spark.sql("create database if not exists demo")
    # spark.sql("drop table if exists src")
    # spark.sql("show database").show()
    # spark.sql("use demo")
    # spark.sql("show databases").show()
    # spark.sql("CREATE TABLE src(key INT, value STRING) USING hive")
    # spark.sql("""show tables in demo""").show()
    # spark.sql("drop table demo.employee")
    # spark.sql("LOAD DATA LOCAL IN PATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")
    #...