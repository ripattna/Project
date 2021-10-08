# importing the library
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

# Creating Spark Session
spark = SparkSession.builder.appName('RDDToDataFrame').getOrCreate()

# Date
columns = ["language", "users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# Converting list to RDD
rdd = spark.sparkContext.parallelize(data)
print(type(rdd))
rdd.collect()

