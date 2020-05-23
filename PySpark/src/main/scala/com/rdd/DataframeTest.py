from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType
from pyspark.sql import SparkSession

class DataframeTest():
    @staticmethod

    def dataframe_test():
        try:
            print("#############################  This is try block!  ####################################3")
            # Create Spark session
            spark = SparkSession.builder.appName("test").getOrCreate()

            # List
            data = [('Ankit', 25), ('Jalfaizy', 22), ('Saurabh', 20), ('Bala', 26)]

            # Create a schema for the dataframe
            schema = StructType([StructField('Name', StringType(), True), StructField('Age', IntegerType(), True)])

            # Convert list to RDD
            rdd = spark.sparkContext.parallelize(data)

            # Create data frame
            df = spark.createDataFrame(rdd, schema)

            print(df.printSchema())
            print(df.describe())
            print(df.describe().show())
            df.show()

        except:
            Exception("Something went wrong")

DataframeTest.dataframe_test()