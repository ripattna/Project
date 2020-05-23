from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # Create Spark context with necessary configuration
    sc = SparkContext("local", "PySpark Word Count Example")

    # Read data from text file and split each line into words
    words = sc.textFile("C:/Project/Files/Input.Input.txt")
    print(words.collect())

    # save the counts to output
    # wordCounts.saveAsTextFile


'''from PySpark import SparkContext
sc = SparkContext()
words = sc.parallelize(["scala","java","hadoop","spark","akka","spark vs hadoop","pyspark","pyspark and spark"])
counts = words.collect()
print("The elements in the RDD:", counts)
coll_Count = words.count()
print("The number of elements in the RDD:", coll_Count)
# foreach = words.foreach(words)'''