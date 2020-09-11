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

# Create Database demo
spark.sql("create database if not exists demo")
# spark.sql("show databases").show()

# Setting the current database to Demo Database
spark.catalog.setCurrentDatabase("demo")


table_list = spark.sql("show tables in demo")
table_name = table_list.filter(table_list.tableName == "test").collect()

if len(table_name) > 0:
    print("Table movies is present in Demo database")
else:
    print("Table not found,Creating the table")
    spark.sql('create table test \
         (id int,commodity string,price int,version int) \
     row format delimited fields terminated by "," \
     LINES TERMINATED BY "\n" \
     stored as TEXTFILE')

    spark.sql("LOAD DATA LOCAL INPATH '/C:/Project/Files/Input/text/Test.txt' INTO TABLE test")

spark.sql("show tables").show()

spark.sql("select * from test").show()

spark.sql("select * from"
          "(select *,row_number() over (partition by commodity,version order by price desc) rn from test)v"
          " where rn=1").show()

spark.sql("SELECT id,commodity,price,version,"
          "rank() over (order by price desc) as rank,"
          "dense_rank() over (order by price desc) as denserank "
          "from test").show()

# spark.sql("drop table if exists test")

