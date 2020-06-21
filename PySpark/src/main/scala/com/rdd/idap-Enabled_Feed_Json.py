from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data_df_1 = spark.read.option("multiline", "true").json("C:\\Project\\Files\\Input\\json\\idap-enabled-data.json")

# Creating a Temp View from the DataFrame
data_df_1.createOrReplaceTempView("record")

# sql_df = spark.sql("select categoryAndFeedSystemName,systemCategoryName,systemFeedName,templateName,feedId from record")
sql_df = spark.sql("select systemCategoryName,systemFeedName,templateName,feedId from record")
print(sql_df.show())

# sql_df.write.csv("C:\\Project\\Files\\Input\\idap-data")'''

data_df_2 = spark.read.option("multiline", "true").json("C:\\Project\\Files\\Input\\json\\idap-enabled-data_api_2.json")

# Creating a Temp View from the DataFrame
data_df_2.createOrReplaceTempView("records")

sql_df = spark.sql("select id,sources.datasource.name from records")
print(sql_df.show())