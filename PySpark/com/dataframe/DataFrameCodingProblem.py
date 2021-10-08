from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType


class DataFrameCodingProblem:
    @staticmethod
    def csv_test():
        try:
            spark = SparkSession.builder.appName("Coding_Problem").getOrCreate()

            # List
            data = [('X', "a"), ('X', "a"), ('Y', "b")]

            # Convert list to RDD
            rdd = spark.sparkContext.parallelize(data)

            # Create a schema
            schema = StructType([StructField('Dept', StringType(), True), StructField('Emp', StringType(), True)])

            # Create data frame
            df_emp = spark.createDataFrame(rdd, schema)

            # Print the data frame
            df_emp.show()

            df_emp_cnt = df_emp.select("Dept").groupBy("Dept").count()

            df_emp_headcount = df_emp.join(df_emp_cnt, df_emp.Dept == df_emp_cnt.Dept) \
                .withColumnRenamed("count", "DeptHeadCount").drop(df_emp_cnt.Dept) \

            df_emp_headcount.createOrReplaceTempView("records")

            spark.sql("select * from records order by DeptHeadCount desc").show()

        except ValueError:
            print("Error in Data Retrieving")


if __name__ == "__main__":
    DataFrameCodingProblem.csv_test()

