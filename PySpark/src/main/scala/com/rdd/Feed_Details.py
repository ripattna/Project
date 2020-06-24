from pyspark.sql import SparkSession


class Feed_Detail:
    @staticmethod
    def feed_info():

        # Create Spark Session and initialize it
        spark = SparkSession.builder.appName("joins_example").getOrCreate()

        # Reading the first API json file.
        data_df1 = spark.read.option("multiline", "true").json("C:\\Project\\Files\\Input\\json\\idap-enabled-data_api_1.json")

        # Creating a Temp View from the DataFrame
        data_df1.createOrReplaceTempView("record")


        sql_df1 = spark.sql("select systemCategoryName,systemFeedName,templateName,id from record")

        # Storing the query result to a csv file.
        # sql_df.write.csv("C:\\Project\\Files\\Output\\idap-feed_info")

        data_df2 = spark.read.option("multiline", "true").json("C:\\Project\\Files\\Input\\json\\idap-enabled-data_api_2.json")

        # Creating a Temp View from the DataFrame
        data_df2.createOrReplaceTempView("records")

        sql_df2 = spark.sql("select id,sources.datasource.name[0] as Source_Table_Name from records")
        # print(sql_df.show())


        # Join the two DataFrame
        sql_df3 = sql_df1.join(sql_df2, on=['id'], how='inner')
        print(sql_df3.show())

        # Storing the query result to a csv file.
        # sql_df3.write.csv("C:\\Project\\Files\\Output\\idap-data_2")


Feed_Detail.feed_info()