from pyspark.sql import SparkSession


class WriteToHive:
    @staticmethod
    def hive_write():
        try:
            # Creating SparkSession
            spark = SparkSession.builder.appName("WriteToHive").enableHiveSupport().getOrCreate()

            # Reading a sample Source Data
            df = spark.read.csv('C:\\Project\\Files\\Input\\csv\\Sample.csv', inferSchema=True, header=True)

            # Printing the type of DF
            print('The type of csv file data is:', type(df))
            # printing the data
            print(df.show())
            # printing the Schema
            print("The schema is:", df.printSchema())

            # Save df to a new table in Hive
            df.write.mode("overwrite").saveAsTable("test_db.test_table2")
            # Show the results using SELECT
            spark.sql("select * from test_db.test_table2").show()



        except ValueError:
            print("Not able to read the csv file")


if __name__ == "__main__":
    WriteToHive.hive_write()


