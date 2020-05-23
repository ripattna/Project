from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # Create Spark context with necessary configuration
    sc = SparkContext("local", "PySpark Word Count Example")

    # Read data from text file and split each line into words
    words = sc.textFile("C:/Project/Files/Input.Input.txt")
    print(words.collect()).show()
