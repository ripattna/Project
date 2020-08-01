from pyspark import SparkContext
sc = SparkContext()
words = sc.parallelize(["scala","java","hadoop","spark","akka","spark vs hadoop","pyspark","pyspark and spark"])
counts = words.collect()
print("The elements in the RDD:", counts)
coll_Count = words.count()
print("The number of elements in the RDD:", coll_Count)
forech=words.foreach(words)